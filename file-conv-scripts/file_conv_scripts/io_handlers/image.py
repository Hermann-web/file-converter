from pathlib import Path

from file_conv_framework.io_handler import FileReader, FileWriter
from PIL import Image


class ImgToPillowReader(FileReader):
    input_format = Image.Image

    def _check_input_format(self, content: Image.Image):
        return isinstance(content, Image.Image)

    def _read_content(self, input_path: Path) -> Image.Image:
        return Image.open(input_path)


class PillowToImgReader(FileWriter):
    output_format = Image.Image

    def _check_output_format(self, content: Image.Image):
        return isinstance(content, Image.Image)

    def _write_content(self, output_path: Path, output_content: Image.Image):
        output_content.save(output_path)
