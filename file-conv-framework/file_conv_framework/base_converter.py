"""
Base Converter Module

This module provides base classes for file conversion.
"""

from abc import ABC, abstractmethod
from pathlib import Path

from file_conv_framework.filetypes import EmptySuffixError, FileType
from file_conv_framework.io_handler import FileReader, FileWriter
from file_conv_framework.logger import logger

class ResolvedInputFile:
    """
    Represents a file with resolved file type.
    """

    def __init__(self, file_path, file_type=None, add_suffix=False, read_content=False):
        """
        Initializes an instance of ResolvedInputFile.

        Args:
            file_path (str): The path to the file.
            file_type (FileType, optional): The type of the file. Defaults to None.
            add_suffix (bool, optional): Whether to add suffix to the file path. Defaults to False.
            read_content (bool, optional): Whether to read the content of the file. Defaults to False.
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
        Resolve the file type based on the provided information.

        Args:
            file_type (FileType or str, optional): The file type or file extension. Defaults to None.
            file_path (str): The path to the file.
            read_content (bool): Whether to read the content of the file.

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
        Returns a string representation of the resolved file path.
        """
        return str(Path(self.file_path).resolve())


class BaseConverter(ABC):

    file_reader: FileReader = None
    file_writer: FileWriter = None

    def __init__(self, input_file: ResolvedInputFile, output_file: ResolvedInputFile):
        self.input_file = input_file
        self.output_file = output_file
        self._check_file_types()

        self.input_format = self.file_reader.input_format
        self.output_format = self.file_reader.input_format
        self.check_io_handlers()

    def convert(self):
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
        self.output_content = self._convert(self.input_content)
        logger.info("done")

        # check
        logger.info("check output content ...")
        assert self._check_output_format(self.output_content)
        logger.info("done")

        # save file
        logger.info("write content to io")
        self._write_content(self.output_file.file_path, self.output_content)
        logger.info("done")

        # log
        logger.info(f"output = {self.output_file}")
        logger.info("succeed")

    def _check_file_types(self):
        if not isinstance(self.input_file, ResolvedInputFile):
            raise ValueError("Invalid input file")

        if not isinstance(self.output_file, ResolvedInputFile):
            raise ValueError("Invalid output file")

        if self.input_file.file_type != self.get_supported_input_type():
            raise ValueError("Unsupported input file type")

        if self.output_file.file_type != self.get_supported_output_type():
            raise ValueError("Unsupported output file type")

    def check_io_handlers(self):
        if not isinstance(self.file_reader, FileReader):
            raise ValueError("Invalid file reader")

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
        input_type = cls._get_supported_input_type()
        if not isinstance(input_type, FileType):
            raise ValueError("Invalid supported input file type")
        return input_type

    @classmethod
    def get_supported_output_type(cls) -> FileType:
        output_type = cls._get_supported_output_type()
        if not isinstance(output_type, FileType):
            raise ValueError("Invalid supported output file type")
        return output_type

    @classmethod
    @abstractmethod
    def _get_supported_input_type(cls) -> FileType:
        pass

    @classmethod
    @abstractmethod
    def _get_supported_output_type(cls) -> FileType:
        pass

    @abstractmethod
    def _convert(self, input_path: Path, output_path: Path):
        logger.info("conversion method not implemented")

    def _read_content(self, input_path: Path):
        return self.file_reader._read_content(input_path)

    def _check_input_format(self, input_content):
        return self.file_reader._check_input_format(input_content)

    def _check_output_format(self, output_content):
        return self.file_writer._check_output_format(output_content)

    def _write_content(self, output_path: Path, output_content):
        return self.file_writer._write_content(output_path, output_content)
