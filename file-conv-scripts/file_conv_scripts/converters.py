from file_conv_framework.base_converter import BaseConverter
from file_conv_framework.filetypes import FileType
from file_conv_framework.io_handler import (
    CSVReader,
    CSVWriter,
    JSONReader,
    JSONWriter,
    TextReader,
    TextWriter,
    XMLReader,
)

from file_conv_scripts.io_handlers import ExcelReader


class TextToTextConverter(BaseConverter, TextReader, TextWriter):
    def __init__(self):
        super().__init__()


class XMLToJSONConverter(BaseConverter, XMLReader, JSONWriter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.XML

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.JSON

    def _convert(self, input_content: str):
        json_data = {}
        return json_data


class TXTToMDConverter(TextToTextConverter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.TEXT

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.MARKDOWN

    def _convert(self, input_content: str):
        md_content = input_content
        return md_content


class JSONToCSVConverter(BaseConverter, JSONReader, CSVWriter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.JSON

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.CSV

    def _convert(self, input_content: dict):
        json_data: dict = input_content
        columns, rows = ["a", "b"], [["a1", "b1"], ["a2", "b2"]]
        return columns, rows


class CSVToXMLConverter(BaseConverter, CSVReader, TextWriter):

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.CSV

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.XML

    def _convert(self, input_content):
        columns, rows = ["a", "b"], [["a1", "b1"], ["a2", "b2"]]
        xml_text = ""
        return xml_text

class XLXSToCSVConverter(BaseConverter, ExcelReader, CSVWriter):
    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.EXCEL

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.CSV

    def _convert(self, input_content):
        # Assuming input_content is a pandas DataFrame representing the Excel data
        # You may need to adjust this according to your specific use case
        csv_content = input_content.to_csv(index=False)
        return csv_content
