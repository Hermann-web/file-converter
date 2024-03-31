# File Conv Framework

The `file_conv_framework` package provides a robust framework for handling file conversion tasks in Python. It offers a set of classes and utilities designed to simplify the process of reading from and writing to different file formats efficiently.

## Features

- **Modular Input/Output Handlers**: Defines abstract base classes for file readers and writers, allowing for easy extension and customization.
- **Support for Various File Formats**: Provides built-in support for common file formats such as text, CSV, JSON, XML, Excel, and image files.
- **MIME Type Detection**: Includes a MIME type guesser utility to automatically detect the MIME type of files, facilitating seamless conversion based on file content.
- **File Type Enumeration**: Defines an enum for representing different file types, enabling easy validation and processing of input and output files.
- **Exception Handling**: Implements custom exceptions for handling errors related to unsupported file types, empty suffixes, file not found, and mismatches between file types.
- **Base Converter Class**: Offers an abstract base class for implementing specific file converters, providing a standardized interface for file conversion operations.
- **Resolved Input File Representation**: Introduces a class for representing input files with resolved file types, ensuring consistency and correctness in conversion tasks.

## Modules

- **io_handler.py**: Contains classes for reading from and writing to files, including text, CSV, JSON, XML, and image files.
- **mimes.py**: Provides a MIME type guesser utility for detecting file MIME types based on file content.
- **filetypes.py**: Defines enums and classes for representing different file types and handling file type validation.
- **base_converter.py**: Implements the base converter class and the resolved input file class for performing file conversion tasks.

## Installation

```bash
# with pip
pip install -i https://test.pypi.org/simple/file-conv-framework
# with poetry
poetry add file-conv-framework --source test-pypi
```

## Usage

The `file_conv_framework` package can be used independently to build custom file conversion utilities or integrated into larger projects for handling file format transformations efficiently.

```python
from file_conv_framework.io_handler import CsvToListReader, ListToCsvWriter
from file_conv_framework.base_converter import BaseConverter, ResolvedInputFile
from file_conv_framework.filetypes import FileType

class CSVToJSONConverter(BaseConverter):
    file_reader = CsvToListReader()
    file_writer = DictToJsonWriter()

    @classmethod
    def _get_supported_input_type(cls) -> FileType:
        return FileType.CSV

    @classmethod
    def _get_supported_output_type(cls) -> FileType:
        return FileType.JSON

    def _convert(self, input_path: Path, output_path: Path):
        # Implement conversion logic from CSV to JSON
        pass

# Usage
input_file_path = "input.csv"
output_file_path = "output.json"
input_file = ResolvedInputFile(input_file_path, is_dir=False, should_exist=True)
output_file = ResolvedInputFile(output_file_path, is_dir=False, should_exist=False, add_suffix=True)
converter = CSVToJSONConverter(input_file, output_file)
converter.convert()
```

## More Examples

The `examples` folder in this repository contains practical demonstrations of how to use the `file_conv_framework` package for file conversion tasks. Currently, it includes the following examples:

- **simple_converter.py**: Demonstrates a basic file converter that converts Excel (XLSX) files to CSV format. It utilizes the `XLXSToCSVConverter` class defined within the `file_conv_framework` package to perform the conversion.

- **cli_app_example.py**: Illustrates how to build a command-line interface (CLI) application using the `ConverterApp` class from the `file_conv_framework.converter_app` module. This CLI app allows users to specify input and output files, as well as input and output file types, for performing file conversions.

These examples serve as practical demonstrations of how to leverage the capabilities of the `file_conv_framework` package in real-world scenarios. Users can refer to these examples for guidance on building their own file conversion utilities or integrating file conversion functionality into existing projects.

## Contributing

Contributions to the `file_conv_framework` package are welcome! Feel free to submit bug reports, feature requests, or pull requests via the GitHub repository.

## Disclaimer

Please note that while the `file_conv_framework` package aims to provide a versatile framework for file conversion tasks, it may not cover every possible use case or handle all edge cases. Users are encouraged to review and customize the code according to their specific requirements.
