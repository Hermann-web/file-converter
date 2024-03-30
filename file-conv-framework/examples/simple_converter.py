import sys
from pathlib import Path

sys.path.append(".")

from file_conv_framework.base_converter import BaseConverter, ResolvedInputFile
from file_conv_framework.filetypes import FileType
from file_conv_framework.io_handler import FileReader, StrToTxtWriter, TxtToStrReader


class TXTToMDConverter(BaseConverter):

    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.MARKDOWN

    def _convert(self, input_content: str):
        md_content = input_content
        return md_content


if __name__ == "__main__":
    input_file_path = "examples/data/example.txt"
    output_file_path = "examples/data/example.md"

    input_file = ResolvedInputFile(input_file_path)
    output_file = ResolvedInputFile(output_file_path, add_suffix=True)

    converter = TXTToMDConverter(input_file, output_file)
    converter.convert()
