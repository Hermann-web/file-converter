from pathlib import Path

import pandas as pd
from file_conv_framework.io_handler import FileReader, FileWriter


class ExcelReader(FileReader):
    input_format = pd.DataFrame

    def _check_input_format(self, content: pd.DataFrame):
        return isinstance(content, pd.DataFrame)

    def _read_content(self, input_path: Path) -> pd.DataFrame:
        return pd.read_excel(input_path)


class ExcelWriter(FileWriter):
    output_format = pd.DataFrame

    def _check_output_format(self, content: pd.DataFrame):
        return isinstance(content, pd.DataFrame)

    def _write_content(self, output_path: Path, output_content: pd.DataFrame):
        output_content.to_excel(output_path, index=False)
