import json
from pathlib import Path

class TextReader:
    input_format = str
    
    def _check_input_format(self, content:str):
        return isinstance(content, str)
    
    def _read_content(self, input_path:Path) -> str:
        return input_path.read_text()


class TextWriter:
    output_format = str
    
    def _check_output_format(self, content:str):
        return isinstance(content, str)
    
    def _write_content(self, output_path:Path, output_content:str):
        output_path.write_text(output_content)


class CSVReader:
    input_format = Tuple[List, List[List[str]] #list of column names and list of rows; a ow is a list of cells
    
    def _check_input_format(self, content:CSVToXMLConverter.input_format):
        return True
    
    def _read_content(self, input_path:Path) -> CSVToXMLConverter.input_format:
        # get input
        input_data = input_path.read_text()
        # get rows and columns from input
        columns = ["a", "b"]
        rows = [ ["a1", "b1"], ["a2", "b2"] ]
        return columns, rows


class CSVWriter:
    output_format = Tuple[List, List[List[str]] #list of column names and list of rows; a ow is a list of cells
    
    def _check_output_format(self, content:CSVToXMLConverter.output_format):
        return True
    
    def _write_content(self, output_path:Path, output_content:CSVToXMLConverter.output_format):
        columns, rows = output_content
        csv_data_str = ""
        output_path.write_text(csv_data_str)


class JSONReader:
    input_format = dict
    
    def _check_input_format(self, content:dict):
        return isinstance(content, dict)
    
    def _read_content(self, input_path:Path) -> dict:
        return json.loads(input_path.read_text())


class JSONWriter:
    output_format = dict
    
    def _check_output_format(self, content:dict):
        return isinstance(content, dict)
    
    def _write_content(self, output_path:Path, output_content:dict):
        return output_path.write_text(json.dumps(output_content))

