import PyPDF2
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
    XMLWriter,
)
from PIL import Image

from file_conv_scripts.io_handlers import ExcelReader, ImageReader, ImageWriter


class TextToTextConverter(BaseConverter):

    file_reader = TextReader()
    file_writer = TextWriter()


class XMLToJSONConverter(BaseConverter):

    file_reader = XMLReader()
    file_writer = JSONWriter()

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

    file_reader = TextReader()
    file_writer = TextWriter()

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

    file_reader = JSONReader()
    file_writer = CSVWriter()

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

    file_reader = CSVReader()
    file_writer = XMLWriter()

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

    file_reader = ExcelReader()
    file_writer = CSVWriter()

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
    file_reader = ImageReader()
    file_writer = PDFWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.PDF

    def _convert(self, input_content: Image.Image):

        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(input_content))


class PDFToImageConverter(BaseConverter):
    file_reader = PDFReader()
    file_writer = ImageWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.PDF

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.IMAGE

    def _convert(self, input_content: PyPDF2.PdfFileReader):
        # Assuming you want to convert each page to an image
        image_list = []
        for page_num in range(input_content.numPages):
            page = input_content.getPage(page_num)
            img = page.to_image()
            image_list.append(img)
        return image_list[0]
