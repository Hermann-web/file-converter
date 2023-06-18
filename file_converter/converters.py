from filetype_handler import FileType
from convertion_handler import BaseConverter
from pathlib import Path

class XMLToJSONConverter(BaseConverter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.XML

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.JSON

    def _convert(self, input_path:Path, output_path:Path):
        return


class TXTToMDConverter(BaseConverter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.MARKDOWN

    def _convert(self, input_path:Path, output_path:Path):
        input_content = input_path.read_text()
        output_path.write_text(input_content)
        return


class JSONToCSVConverter(BaseConverter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.JSON

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.CSV

    def _convert(self, input_path:Path, output_path:Path):
        return


class CSVToXMLConverter(BaseConverter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.CSV

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.XML

    def _convert(self, input_path:Path, output_path:Path):
        return


