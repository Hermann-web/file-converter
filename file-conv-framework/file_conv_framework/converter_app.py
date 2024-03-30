"""
Main Module

This module contains the main application logic.
"""

from pathlib import Path
from typing import Dict, List, Tuple, Type

from file_conv_framework.base_converter import BaseConverter, ResolvedInputFile
from file_conv_framework.filetypes import FileType
from file_conv_framework.logger import logger


class BaseConverterApp:
    """
    Main application class responsible for managing file conversions.
    """

    converters: List[Type[BaseConverter]] = []

    def __init__(
        self,
        input_file_path: str,
        input_file_type: FileType = None,
        output_file_path: str = None,
        output_file_type: FileType = None,
    ):
        """
        Initializes the BaseConverterApp instance.

        Args:
            input_file_path (str): The path to the input file.
            input_file_type (FileType, optional): The type of the input file. Defaults to None.
            output_file_path (str, optional): The path to the output file. Defaults to None.
            output_file_type (FileType, optional): The type of the output file. Defaults to None.
        """
        self._dict_converters: Dict[Tuple[FileType, FileType], Type[BaseConverter]] = {}
        self.input_file = ResolvedInputFile(
            input_file_path,
            file_type=input_file_type,
            add_suffix=False,
            read_content=True,
        )
        if not output_file_path:
            output_file_path = str(Path(input_file_path).with_suffix(""))
            assert (
                output_file_type is not None
            ), "either output_file_path or output_file_type should be set "
        self.output_file = ResolvedInputFile(
            output_file_path,
            file_type=output_file_type,
            add_suffix=True,
            read_content=False,
        )

        for _conv_class in self.converters:
            self.add_converter_pair(_conv_class)

    def add_converter_pair(self, converter_class: Type[BaseConverter]):
        """
        Adds a converter pair to the application.

        Args:
            converter_class (Type[BaseConverter]): The converter class to add.

        Raises:
            ValueError: If the converter class is invalid.
        """
        # Check if the converter_class is a subclass of BaseConverter
        if not issubclass(converter_class, BaseConverter):
            raise ValueError("Invalid converter class")

        # Add the converter pair to the converters dictionary
        self._dict_converters[
            (converter_class.get_input_type(), converter_class.get_output_type())
        ] = converter_class

    def get_supported_conversions(self) -> Tuple[Tuple[FileType]]:
        """
        Retrieves the supported conversions.

        Returns:
            Tuple[Tuple[FileType]]: A tuple of tuples representing supported conversions.
        """
        return tuple(self._dict_converters.keys())

    def run(self):
        """
        Runs the conversion process.
        """
        # get converter class
        converter_class = self._dict_converters.get(
            (self.input_file.file_type, self.output_file.file_type)
        )

        # make sure a converter class exists
        if converter_class is None:
            _ = "\n " + "\n ".join(
                map(lambda x: f"{x[0]} -> {x[1]}", self.get_supported_conversions())
            )
            logger.error(f"Conversion not supported. Supported convertions are {_}")
            return

        # instanciate the converter
        converter = converter_class(self.input_file, self.output_file)

        # run the convertion pipeline
        converter.convert()
