"""
Main Module

This module contains the main application logic.
"""

from pathlib import Path
from typing import List, Tuple, Type

from file_conv_framework.base_converter import BaseConverter, ResolvedInputFile
from file_conv_framework.filetypes import FileType
from file_conv_framework.logger import logger

class BaseConverterApp:

    converters: List[Type[BaseConverter]] = []

    def __init__(
        self,
        input_file_path,
        input_file_type=None,
        output_file_path=None,
        output_file_type=None,
    ):
        self._dict_converters = {}
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
        # Check if the converter_class is a subclass of BaseConverter
        if not issubclass(converter_class, BaseConverter):
            raise ValueError("Invalid converter class")

        # Add the converter pair to the converters dictionary
        self._dict_converters[
            (converter_class.get_input_type(), converter_class.get_output_type())
        ] = converter_class

    def get_supported_conversions(self) -> Tuple[Tuple[FileType]]:
        return tuple(self._dict_converters.keys())

    def run(self):
        if self.output_file:
            converter_class = self._dict_converters.get(
                (self.input_file.file_type, self.output_file.file_type)
            )
            if converter_class:
                converter = converter_class(self.input_file, self.output_file)
                converter.convert()
            else:
                _ = "\n " + "\n ".join(
                    map(lambda x: f"{x[0]} -> {x[1]}", self.get_supported_conversions())
                )
                logger.error(f"Conversion not supported. Supported convertions are {_}")
        else:
            logger.error("Output file path not provided")
