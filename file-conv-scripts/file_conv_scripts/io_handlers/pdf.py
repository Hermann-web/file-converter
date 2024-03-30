from pathlib import Path

from file_conv_framework.io_handler import FileReader, FileWriter
from PyPDF2 import PdfReader


class PdfToPypdfReader(FileReader):
    input_format = PdfReader

    def _check_input_format(self, content: PdfReader):
        return isinstance(content, PdfReader)

    def _read_content(self, input_path: Path) -> PdfReader:
        pdf_reader = PdfReader(input_path)
        return pdf_reader


# class PDFWriter(FileWriter):
#     output_format = canvas.Canvas

#     def _check_output_format(self, content: canvas.Canvas):
#         return isinstance(content, canvas.Canvas)

#     def _write_content(self, output_path: Path, output_content: canvas.Canvas):
#         output_content.save()
