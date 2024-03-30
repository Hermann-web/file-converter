"""
Conversion Handlers

This module provides classes for converting between different file formats. It includes concrete implementations of conversion classes for various file types.
"""

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
from PIL import Image as PillowImage
from PyPDF2 import PdfReader, PdfWriter

from file_conv_scripts.io_handlers import (
    ImageToPillowReader,
    PdfToPyPdfReader,
    PyPdfToPdfWriter,
    SpreadsheetToPandasReader,
)


class TextToTextConverter(BaseConverter):
    """
    Converts text files to text format.
    """

    file_reader = TxtToStrReader()
    file_writer = StrToTxtWriter()


class XMLToJSONConverter(BaseConverter):
    """
    Converts XML files to JSON format.
    """

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
    """
    Converts text files to Markdown format.
    """

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
    """
    Converts JSON files to CSV format.
    """

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
    """
    Converts CSV files to XML format.
    """

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


class XLSXToCSVConverter(BaseConverter):
    """
    Converts Excel files to CSV format.
    """

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
    """
    Converts image files to PDF format.
    """

    file_reader = ImageToPillowReader()
    file_writer = None

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.PDF

    def _convert(self, input_content: PillowImage.Image, output_path: Path):
        input_content = input_content.convert("RGB")
        input_content.save(output_path)


class ImageToPDFConverterWithPyPdf2(BaseConverter):
    """
    Converts image files to PDF format using PyPDF2.
    """

    file_reader = ImageToPillowReader()
    file_writer = PyPdfToPdfWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.PDF

    def _convert(self, input_content: PillowImage.Image):
        # Create a new PDF document
        pdf_writer = PdfWriter()

        # Add the image as a page to the PDF document
        width, height = input_content.size
        pdf_page = pdf_writer.add_blank_page(width=width, height=height)
        pdf_page.merge_page(input_content)

        return pdf_writer


class PDFToImageConverter(BaseConverter):
    """
    Converts PDF files to image format.
    """

    file_reader = PdfToPyPdfReader()
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
