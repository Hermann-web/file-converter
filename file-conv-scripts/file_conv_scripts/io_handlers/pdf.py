from pathlib import Path

import PyPDF2
from file_conv_framework.io_handler import FileReader, FileWriter


class PDFReader(FileReader):
    input_format = PyPDF2.PdfFileReader

    def _check_input_format(self, content: PyPDF2.PdfFileReader):
        return isinstance(content, PyPDF2.PdfFileReader)

    def _read_content(self, input_path: Path) -> PyPDF2.PdfFileReader:
        with open(input_path, "rb") as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
        return pdf_reader


# class PDFWriter(FileWriter):
#     output_format = canvas.Canvas

#     def _check_output_format(self, content: canvas.Canvas):
#         return isinstance(content, canvas.Canvas)

#     def _write_content(self, output_path: Path, output_content: canvas.Canvas):
#         output_content.save()
