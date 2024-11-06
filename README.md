# File Conversion Framework and Scripts

This repository contains two complementary packages for handling file conversion tasks in Python: [`opencf-core`](./opencf-core/) and [`opencf`](./opencf). The `opencf-core` package offers a robust framework for file conversion operations, while the `opencf` package provides a collection of Python scripts built on top of the framework for convenient file format conversions.

## [`opencf-core`](./opencf-core/)

The `opencf-core` package provides a versatile framework for handling file conversions efficiently. It offers modular input/output handlers, MIME type detection, exception handling, and a base converter class for implementing specific conversion logic. Key features include:

- **Modular Input/Output Handlers**: Abstract base classes for file readers and writers.
- **Support for Various Formats**: Built-in support for text, CSV, JSON, XML, Excel, and image files.
- **MIME Type Detection**: Automatic detection of MIME types for seamless conversion.
- **File Type Enumeration**: Enum for representing different file types.
- **Exception Handling**: Custom exceptions for error handling.
- **Base Converter Class**: Abstract base class for specific converters.
- **Resolved Input File Representation**: Class for representing input files with resolved types.

For more details and usage examples, please refer to the [`opencf-core` README](./opencf-core/README.md).

## [`opencf`](./opencf/)

The `opencf` package offers a set of Python scripts for file conversion tasks, built on the `opencf-core`. It extends the framework's capabilities by providing pre-built converter classes for various file format conversions. Key features include:

- **Extensive Conversion Support**: Scripts for text, XML, JSON, CSV, and Excel conversions.
- **Integration with Framework**: Utilizes classes from `opencf-core`.
- **Modular Converter Classes**: Custom converter classes for specific conversions.
- **Flexible Input/Output Handling**: Seamless reading and writing of different file formats.
- **Custom File Handlers**: Support for custom reader and writer classes.
- **Command-Line Interface**: CLI for executing conversion tasks conveniently.
- **Extensibility**: Easily extendable for handling more file formats.

For more details and usage examples, please refer to the [`opencf` README](./opencf/README.md).

<!-- ## Getting Started

To use the packages:

1. Install the packages and dependencies using your preferred package manager.
2. Import required classes into your scripts or applications.
3. Utilize provided converter classes for file conversions.
4. Execute scripts either programmatically or via CLI. -->

## Example Usage

Here's an example of converting an XML file to JSON using the `opencf` package:

```bash
cd pyconvtool
poetry install
python pyconvtool/app.py input.xml -t XML -o output.json -ot JSON
```

This command utilizes the `ConverterApp` class to convert an XML file to a JSON file.

## Contribution

Contributions to this repository are welcome! Feel free to submit bug reports, feature requests, or pull requests via GitHub. Consider extending functionality by adding support for additional file formats or improving existing converter classes.

## Contact

For any inquiries or support, please contact [agossouhermann7@gmail.com].

## similar projects

- <https://github.com/Tichau/FileConverter>: a C# destop project for conversion
- <https://github.com/bipinkrish/File-Converter-Bot>: python desktop app foor conversion use 3rd party tools for conversion
- <https://pypi.org/project/aspose-words>: platform independant pytho module, to convert between different file formats essentially those related to Office proprietrary ones
- [pandoc](https://github.com/boisgera/pandoc): convert many document and markdown to pdf and more
