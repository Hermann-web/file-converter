"""
Base Converter Module

This module serves as a foundation for creating file conversion utilities. It facilitates the development
of file converters through abstract base classes, managing file types, and handling input and output files
efficiently. The module is designed to be extendible, supporting various file formats and conversion strategies.

Classes:
- ResolvedInputFile: Manages file paths and types, resolving them as needed.
- BaseConverter: An abstract base class for creating specific file format converters, enforcing the implementation
                 of file conversion logic.

Exceptions:
- ValueError: Raised when file paths or types are incompatible or unsupported.
- AssertionError: Ensured for internal consistency checks, confirming that file types match expected values.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from file_conv_framework.filetypes import EmptySuffixError, FileType
from file_conv_framework.io_handler import FileReader, FileWriter, SamePathReader
from file_conv_framework.logger import logger


class ResolvedInputFile:
    """
    Handles resolving the file type of a given file, managing path adjustments and optional content reading.
    """

    def __init__(self, file_path, file_type=None, add_suffix=False, read_content=False):
        """
        Initializes an instance of ResolvedInputFile with options for type resolution and path modification.

        Args:
            file_path (str): The path to the file.
            file_type (FileType, optional): The explicit type of the file. If None, attempts to resolve based on the path or content.
            add_suffix (bool, optional): Whether to append the resolved file type's suffix to the file path. Defaults to False.
            read_content (bool, optional): Whether to read the file's content to assist in type resolution. Defaults to False.
        """
        # Convert file_path to Path object
        self.file_path = Path(file_path)

        # Resolve the file type
        self.file_type = self.__resolve_filetype__(file_type, file_path, read_content)
        assert self.file_type.is_true_filetype()

        # Get the suffix corresponding to the resolved file type
        self.suffix = self.file_type.get_suffix()

        # Optionally add suffix to the file path
        if add_suffix:
            self.file_path = self.file_path.with_suffix(self.suffix)

    def __resolve_filetype__(self, file_type, file_path, read_content) -> FileType:
        """
        Determines the file type, utilizing the provided type, file path, or content as needed.

        Args:
            file_type (FileType or str, optional): An explicit file type or extension.
            file_path (str): The path to the file, used if file_type is not provided.
            read_content (bool): Indicates if file content should be used to help resolve the file type.

        Returns:
            FileType: The resolved file type.
        """
        if not file_type:
            try:
                file_type = FileType.from_path(
                    file_path, read_content=read_content, raise_err=True
                )
            except EmptySuffixError:
                raise ValueError("filepath suffix is emtpy but file_type not set")
            return file_type

        resolved_file_type = FileType.from_suffix(file_type, raise_err=True)

        file_type_from_path = FileType.from_path(
            file_path, read_content=read_content, raise_err=False
        )

        if file_type_from_path.is_true_filetype():
            assert file_type_from_path == resolved_file_type

        return resolved_file_type

    def __str__(self):
        """
        Returns the absolute file path as a string.

        Returns:
            str: The resolved file path.
        """
        return str(Path(self.file_path).resolve())


class BaseConverter(ABC):
    """
    Abstract base class for file conversion, defining the template for input to output file conversion.
    """

    file_reader: FileReader = None
    file_writer: FileWriter = None

    def __init__(self, input_file: ResolvedInputFile, output_file: ResolvedInputFile):
        """
        Sets up the converter with specified input and output files, ensuring compatibility.

        Args:
            input_file (ResolvedInputFile): The input file with resolved type.
            output_file (ResolvedInputFile): The output file where the converted data will be saved.
        """
        self.input_file = input_file
        self.output_file = output_file
        self._check_file_types()

        # self.input_format = self.file_reader.input_format
        # self.output_format = self.file_writer.output_format
        self.check_io_handlers()

    def convert(self):
        """
        Orchestrates the file conversion process, including reading, converting, and writing the file.
        """
        # log
        logger.info(
            f"Convertion of {self.get_supported_input_type()} to {self.get_supported_output_type()}..."
        )
        logger.info(f"input = {self.input_file}")

        # read file
        logger.info("read file from io ...")
        self.input_content = self._read_content(self.input_file.file_path)
        logger.info("done")

        # check
        logger.info("check input content ...")
        assert self._check_input_format(self.input_content)
        logger.info("done")

        # convert file
        logger.info("converting file ...")
        if self.file_writer is None:
            logger.info("writer: false")
            self._convert(
                input_content=self.input_content, output_path=self.output_file.file_path
            )
            logger.info("done")
        else:
            logger.info("writer: true")
            self.output_content = self._convert(input_content=self.input_content)
            assert self._check_output_format(self.output_content)
            logger.info("done")

            # save file
            logger.info("write content to io ...")
            self._write_content(self.output_file.file_path, self.output_content)
            logger.info("done")

        # log
        logger.info(f"output = {self.output_file}")
        logger.info("succeed")

    def _check_file_types(self):
        """
        Validates that the provided files have acceptable and supported file types for conversion.
        """
        if not isinstance(self.input_file, ResolvedInputFile):
            raise ValueError("Invalid input file")

        if not isinstance(self.output_file, ResolvedInputFile):
            raise ValueError("Invalid output file")

        if self.input_file.file_type != self.get_supported_input_type():
            raise ValueError("Unsupported input file type")

        if self.output_file.file_type != self.get_supported_output_type():
            raise ValueError("Unsupported output file type")

    def check_io_handlers(self):
        """
        Ensures that valid I/O handlers (file reader and writer) are set for the conversion.
        """
        if self.file_reader is None:
            self.file_reader = SamePathReader()

        if not isinstance(self.file_reader, FileReader):
            raise ValueError("Invalid file reader")

        if self.file_writer is None:
            return

        if not isinstance(self.file_writer, FileWriter):
            raise ValueError("Invalid file writer")

    @classmethod
    def get_input_type(cls):
        return cls.get_supported_input_type()

    @classmethod
    def get_output_type(cls):
        return cls.get_supported_output_type()

    @classmethod
    def get_supported_input_type(cls) -> FileType:
        """
        Defines the supported input file type for this converter.

        Returns:
            FileType: The file type supported for input.
        """
        input_type = cls._get_supported_input_type()
        if not isinstance(input_type, FileType):
            raise ValueError("Invalid supported input file type")
        return input_type

    @classmethod
    def get_supported_output_type(cls) -> FileType:
        """
        Defines the supported output file type for this converter.

        Returns:
            FileType: The file type supported for output.
        """
        output_type = cls._get_supported_output_type()
        if not isinstance(output_type, FileType):
            raise ValueError("Invalid supported output file type")
        return output_type

    @classmethod
    @abstractmethod
    def _get_supported_input_type(cls) -> FileType:
        """
        Abstract method to define the supported input file type by the converter.

        Returns:
            FileType: The supported input file type.
        """
        pass

    @classmethod
    @abstractmethod
    def _get_supported_output_type(cls) -> FileType:
        """
        Abstract method to define the supported output file type by the converter.

        Returns:
            FileType: The supported output file type.
        """
        pass

    @abstractmethod
    def _convert(self):
        """
        Abstract method to be implemented by subclasses to perform the actual file conversion process.
        """
        logger.info("conversion method not implemented")

    def _read_content(self, input_path: Path):
        return self.file_reader._read_content(input_path)

    def _check_input_format(self, input_content):
        return self.file_reader._check_input_format(input_content)

    def _check_output_format(self, output_content):
        return self.file_writer._check_output_format(output_content)

    def _write_content(self, output_path: Path, output_content):
        return self.file_writer._write_content(output_path, output_content)
