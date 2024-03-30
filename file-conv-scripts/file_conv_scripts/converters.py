from pathlib import Path

from file_conv_framework.base_converter import BaseConverter
from file_conv_framework.filetypes import FileType
from file_conv_framework.io_handler import (
    CsvToListReader,
    DictToJsonWriter,
    JsonToDictReader,
    ListToCsvWriter,
    StrToTxtWriter,
    StrToXmlWriter,
    TxtToStrReader,
    XmlToStrReader,
)
from PIL import Image
from PyPDF2 import PdfReader

from file_conv_scripts.io_handlers import (
    ImgToPillowReader,
    PillowToImgReader,
    SpreadsheetToPandasReader,
)
from file_conv_scripts.io_handlers.pdf import PdfToPypdfReader


class TextToTextConverter(BaseConverter):

    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()


class XMLToJSONConverter(BaseConverter):

    file_reader = XmlToStrReader()
    file_writer = DictToJsonWriter()

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


class JSONToCSVConverter(BaseConverter):

    file_reader = JsonToDictReader()
    file_writer = ListToCsvWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.JSON

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.CSV

    def _convert(self, input_content: dict):
        json_data: dict = input_content
        columns, rows = ["a", "b"], [["a1", "b1"], ["a2", "b2"]]
        rows.insert(0, columns)
        return rows


class CSVToXMLConverter(BaseConverter):

    file_reader = CsvToListReader()
    file_writer = StrToXmlWriter()

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


class XLXSToCSVConverter(BaseConverter):

    file_reader = SpreadsheetToPandasReader()
    file_writer = ListToCsvWriter()

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


class ImageToPDFConverter(BaseConverter):
    file_reader = ImgToPillowReader()
    file_writer = None

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.PDF

    def _convert(self, input_content: Image.Image, output_path: Path):
        input_content = input_content.convert("RGB")
        input_content.save(output_path)


class PDFToImageConverter(BaseConverter):
    file_reader = PdfToPypdfReader()
    file_writer = None

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.PDF

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.IMAGE

    def _convert(self, input_content: PdfReader, output_path: Path):
        # Assuming you want to convert each page to an image
        page = input_content.pages[0]
        output_path.mkdir()

        for count, image_file_object in enumerate(page.images):
            fpath = output_path / f"{count}-{image_file_object.name}"
            with open(str(fpath), "wb") as fp:
                fp.write(image_file_object.data)
