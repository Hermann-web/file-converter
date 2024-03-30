"""
Input/Output Handler Module

This module provides classes for reading from and writing to files.
"""

import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, List


class FileReader(ABC):
    input_format = None

    @abstractmethod
    def _check_input_format(self, content):
        pass

    @abstractmethod
    def _read_content(self, input_path):
        pass


class FileWriter(ABC):
    output_format = None

    @abstractmethod
    def _check_output_format(self, content):
        pass

    @abstractmethod
    def _write_content(self, output_path, output_content):
        pass


class TxtToStrReader(FileReader):
    input_format = str

    def _check_input_format(self, content: str):
        return isinstance(content, str)

    def _read_content(self, input_path: Path) -> str:
        return input_path.read_text()


class StrToTxtWriter(FileWriter):
    output_format = str

    def _check_output_format(self, content: str):
        return isinstance(content, str)

    def _write_content(self, output_path: Path, output_content: str):
        output_path.write_text(output_content)


class CsvToListReader(FileReader):
    input_format = List[List[str]]

    def _check_input_format(self, content: List[List[str]]):
        return isinstance(content, list) and all(
            isinstance(row, list) for row in content
        )

    def _read_content(self, input_path: Path) -> List[List[str]]:
        with open(input_path, "r", newline="") as csvfile:
            reader = csv.reader(csvfile)
            return [row for row in reader]


class ListToCsvWriter(FileWriter):
    output_format = List[List[str]]

    def _check_output_format(self, content: List[List[str]]):
        return isinstance(content, list) and all(
            isinstance(row, list) for row in content
        )

    def _write_content(self, output_path: Path, output_content: List[List[str]]):
        with open(output_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in output_content:
                writer.writerow(row)


class JsonToDictReader(FileReader):
    input_format = Dict[str, Any]

    def _check_input_format(self, content: Dict[str, Any]):
        return isinstance(content, dict)

    def _read_content(self, input_path: Path) -> Dict[str, Any]:
        return json.loads(input_path.read_text())


class DictToJsonWriter(FileWriter):
    output_format = Dict[str, Any]

    def _check_output_format(self, content: Dict[str, Any]):
        return isinstance(content, dict)

    def _write_content(self, output_path: Path, output_content: Dict[str, Any]):
        return output_path.write_text(json.dumps(output_content))


class XmlToStrReader(FileReader):
    input_format = str

    def _check_input_format(self, content: str):
        # Add your XML validation logic here
        return isinstance(content, str)

    def _read_content(self, input_path: Path) -> str:
        return input_path.read_text()


class StrToXmlWriter(FileWriter):
    output_format = str

    def _check_output_format(self, content: str):
        # Add your XML validation logic here
        return isinstance(content, str)

    def _write_content(self, output_path: Path, output_content: str):
        output_path.write_text(output_content)
