"""
Input/Output Handler Module

This module provides classes for reading from and writing to files.
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any

class TextReader:
    input_format = str
    
    def _check_input_format(self, content: str):
        return isinstance(content, str)
    
    def _read_content(self, input_path: Path) -> str:
        return input_path.read_text()


class TextWriter:
    output_format = str
    
    def _check_output_format(self, content: str):
        return isinstance(content, str)
    
    def _write_content(self, output_path: Path, output_content: str):
        output_path.write_text(output_content)

class CSVReader:
    input_format = List[List[str]]
    
    def _check_input_format(self, content: List[List[str]]):
        return isinstance(content, list) and all(isinstance(row, list) for row in content)
    
    def _read_content(self, input_path: Path) -> List[List[str]]:
        with open(input_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]

class CSVWriter:
    output_format = List[List[str]]
    
    def _check_output_format(self, content: List[List[str]]):
        return isinstance(content, list) and all(isinstance(row, list) for row in content)
    
    def _write_content(self, output_path: Path, output_content: List[List[str]]):
        with open(output_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in output_content:
                writer.writerow(row)

class JSONReader:
    input_format = Dict[str, Any]
    
    def _check_input_format(self, content: Dict[str, Any]):
        return isinstance(content, dict)
    
    def _read_content(self, input_path: Path) -> Dict[str, Any]:
        return json.loads(input_path.read_text())


class JSONWriter:
    output_format = Dict[str, Any]
    
    def _check_output_format(self, content: Dict[str, Any]):
        return isinstance(content, dict)
    
    def _write_content(self, output_path: Path, output_content: Dict[str, Any]):
        return output_path.write_text(json.dumps(output_content))

class XMLReader:
    input_format = str
    
    def _check_input_format(self, content: str):
        # Add your XML validation logic here
        return isinstance(content, str)
    
    def _read_content(self, input_path: Path) -> str:
        return input_path.read_text()


class XMLWriter:
    output_format = str
    
    def _check_output_format(self, content: str):
        # Add your XML validation logic here
        return isinstance(content, str)
    
    def _write_content(self, output_path: Path, output_content: str):
        output_path.write_text(output_content)
