# File Conversion Framework and Scripts

This repository contains two complementary packages for handling file conversion tasks in Python: [`file_conv_framework`](./file_conv_framework) and [`file_conv_scripts`](./file_conv_scripts). The `file_conv_framework` package offers a robust framework for file conversion operations, while the `file_conv_scripts` package provides a collection of Python scripts built on top of the framework for convenient file format conversions.

## [`file_conv_framework`](./file_conv_framework)

The `file_conv_framework` package provides a versatile framework for handling file conversions efficiently. It offers modular input/output handlers, MIME type detection, exception handling, and a base converter class for implementing specific conversion logic. Key features include:

- **Modular Input/Output Handlers**: Abstract base classes for file readers and writers.
- **Support for Various Formats**: Built-in support for text, CSV, JSON, XML, Excel, and image files.
- **MIME Type Detection**: Automatic detection of MIME types for seamless conversion.
- **File Type Enumeration**: Enum for representing different file types.
- **Exception Handling**: Custom exceptions for error handling.
- **Base Converter Class**: Abstract base class for specific converters.
- **Resolved Input File Representation**: Class for representing input files with resolved types.

For more details and usage examples, please refer to the [`file_conv_framework` README](./file-conv-framework/README.md).

## [`file_conv_scripts`](./file_conv_scripts)

The `file_conv_scripts` package offers a set of Python scripts for file conversion tasks, built on the `file_conv_framework`. It extends the framework's capabilities by providing pre-built converter classes for various file format conversions. Key features include:

- **Extensive Conversion Support**: Scripts for text, XML, JSON, CSV, and Excel conversions.
- **Integration with Framework**: Utilizes classes from `file_conv_framework`.
- **Modular Converter Classes**: Custom converter classes for specific conversions.
- **Flexible Input/Output Handling**: Seamless reading and writing of different file formats.
- **Custom File Handlers**: Support for custom reader and writer classes.
- **Command-Line Interface**: CLI for executing conversion tasks conveniently.
- **Extensibility**: Easily extendable for handling more file formats.

For more details and usage examples, please refer to the [`file_conv_scripts` README](./file-conv-scripts/README.md).

<!-- ## Getting Started

To use the packages:

1. Install the packages and dependencies using your preferred package manager.
2. Import required classes into your scripts or applications.
3. Utilize provided converter classes for file conversions.
4. Execute scripts either programmatically or via CLI. -->

## Example Usage

Here's an example of converting an XML file to JSON using the `file_conv_scripts` package:

```bash
cd file_conv_scripts
poetry install
python file_conv_scripts/app.py input.xml -t XML -o output.json -ot JSON
```

This command utilizes the `ConverterApp` class to convert an XML file to a JSON file.

## Contribution

Contributions to this repository are welcome! Feel free to submit bug reports, feature requests, or pull requests via GitHub. Consider extending functionality by adding support for additional file formats or improving existing converter classes.

## Contact

For any inquiries or support, please contact [agossouhermann7@gmail.com].

## similar projects

- <https://github.com/Tichau/FileConverter>: a C# destop project for conversion
- <https://github.com/bipinkrish/File-Converter-Bot>: python desktop app foor conversion use 3rd party tools for conversion
