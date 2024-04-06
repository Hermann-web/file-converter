"""
Conversion Handlers

This module provides classes for converting between different file formats. It includes concrete implementations of conversion classes for various file types.
"""

from pathlib import Path
from typing import Dict, List

import numpy as np
import pandas as pd
from convcore.base_converter import BaseConverter
from convcore.filetypes import FileType
from convcore.io_handler import (
    CsvToListReader,
    DictToJsonWriter,
    JsonToDictReader,
    ListToCsvWriter,
    StrToTxtWriter,
    StrToXmlWriter,
    TxtToStrReader,
    XmlToStrReader,
)
from cv2.typing import MatLike
from PIL import Image as PillowImage
from PyPDF2 import PdfReader, PdfWriter

from .io_handlers import (
    FramesToGIFWriterWithImageIO,
    ImageToOpenCVReader,
    ImageToPillowReader,
    PdfToPyPdfReader,
    PyPdfToPdfWriter,
    SpreadsheetToPandasReader,
    VideoArrayWriter,
    VideoToFramesReaderWithOpenCV,
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

    def _convert(self, input_contents: List[str]):
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

    def _convert(self, input_contents: List[str]):
        md_content = "\n".join(input_contents)
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

    def _convert(self, input_contents: List[Dict]):
        json_data: dict = input_contents[0]
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

    def _convert(self, input_contents):
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

    def _convert(self, input_contents: List[pd.DataFrame]):
        # Assuming input_content is a pandas DataFrame representing the Excel data
        # You may need to adjust this according to your specific use case
        df = input_contents[0]
        csv_content = df.to_csv(index=False)
        return csv_content


class ImageToPDFConverter(BaseConverter):
    """
    Converts image files to PDF format.
    """

    file_reader = ImageToPillowReader()
    file_writer = None
    folder_as_output = False

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.PDF

    def _convert(self, input_contents: List[PillowImage.Image], output_file: Path):
        images = input_contents

        # Create a list of all the input images and convert them to RGB
        images = [img.convert("RGB") for img in images]

        # Save the PDF file
        images[0].save(output_file, save_all=True, append_images=images[1:])


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

    def _convert(self, input_contents: List[PillowImage.Image]):
        # Create a new PDF document
        pdf_writer = PdfWriter()

        all_pages = input_contents

        for page in all_pages:
            # Add the image as a page to the PDF document
            width, height = page.size
            pdf_page = pdf_writer.add_blank_page(width=width, height=height)
            pdf_page.merge_page(page)

        return pdf_writer


# class ImageToPDFConverterWithImg2pdf(BaseConverter):
#     """
#     Converts image files to PDF format using img2pdf.
#     """

#     file_reader = None
#     file_writer = None

#     @classmethod
#     def _get_supported_input_type(cls) -> FileType:
#         return FileType.IMAGE

#     @classmethod
#     def _get_supported_output_type(cls) -> FileType:
#         return FileType.PDF

#     def _convert(self, input_contents: List[Path], outputfile: Path):
#         filepaths = input_contents
#         # Convert images to PDF using img2pdf
#         with open(output_file, "wb") as f:
#             f.write(img2pdf.convert(filepaths))


class PDFToImageConverter(BaseConverter):
    """
    Converts PDF files to image format.
    """

    file_reader = PdfToPyPdfReader()
    file_writer = None
    folder_as_output = True

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.PDF

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.IMAGE

    def _convert(self, input_contents: List[PdfReader], output_folder: Path):
        # Assuming you want to convert each page to an image
        pass


class PDFToImageExtractor(BaseConverter):
    """
    Converts PDF files to image format.
    """

    file_reader = PdfToPyPdfReader()
    file_writer = None
    folder_as_output = True

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.PDF

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.IMAGE

    def _convert(self, input_contents: List[PdfReader], output_folder: Path):
        """
        - read more [here](https://pypdf2.readthedocs.io/en/3.0.0/user/extract-images.html)
        """
        pdf_file = input_contents[0]

        for page_num, page in enumerate(pdf_file.pages):
            for count, img in enumerate(page.images):
                fpath = output_folder / f"page{page_num+1}-fig{count+1}-{img.name}"
                with open(str(fpath), "wb") as fp:
                    fp.write(img.data)


class ImageToVideoConverterWithPillow(BaseConverter):
    """
    Converts image files to video format.
    """

    file_reader = ImageToPillowReader()
    file_writer = VideoArrayWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.VIDEO

    def _convert(self, input_contents: List[PillowImage.Image]):
        """
        Converts a list of image files to a video file.

        Args:
            input_contents (List[PillowImage.Image]): List of input images.
            output_file (Path): Output video file path.
        """
        # Convert Pillow images to numpy arrays
        image_arrays = [np.array(img) for img in input_contents]

        # Convert list of numpy based opencv images to numpy array
        image_arrays = np.asarray(input_contents)

        return image_arrays


class ImageToVideoConverterWithOpenCV(BaseConverter):
    """
    Converts image files to video format.
    """

    file_reader = ImageToOpenCVReader()
    file_writer = VideoArrayWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.IMAGE

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.VIDEO

    def _convert(self, input_contents: List[np.ndarray]):
        """
        Converts a list of image files to a video file.

        Args:
            input_contents (List[np.ndarray]): List of input images.
            output_file (Path): Output video file path.
        """
        # Convert list of numpy based opencv images to numpy array
        image_arrays = np.asarray(input_contents)

        return image_arrays


class VideoToGIFConverter(BaseConverter):
    """
    Converts a video file to GIF format.
    """

    file_reader = VideoToFramesReaderWithOpenCV()
    file_writer = FramesToGIFWriterWithImageIO()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.VIDEO

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.GIF

    def _convert(self, input_contents: List[List[MatLike]]):
        """
        Converts a list of video frames to a GIF.

        Args:
            input_contents (List[MatLike]): List of video frames.

        Returns:
            bytes: The converted GIF content.
        """
        video_frames = input_contents[0]
        # Write video frames to GIF
        return video_frames
