# File Conversion Scripts

The `file_conv_scripts` package provides a collection of Python scripts for file conversion tasks, built on top of the `file_conv_framework` framework. These scripts offer functionalities to convert various file formats, including text, CSV, JSON, XML, Excel, and image files, making it easy to handle different types of data transformations efficiently.

## Features

- **Extensive Conversion Support**: The package includes scripts for converting between various file formats, including text, XML, JSON, CSV, and Excel.
- **Integration with `file_conv_framework`**: Utilizes classes from the `file_conv_framework` package for file I/O operations, MIME type detection, and exception handling.
- **Modular Converter Classes**: Each conversion script is backed by a custom converter class tailored to handle specific file format conversions, extending the base converter class provided by `file_conv_framework`.
- **Flexible Input/Output Handling**: Supports reading from and writing to different file formats seamlessly, leveraging the capabilities of `file_conv_framework`.
- **Custom File Handlers**: Implements custom file reader and writer classes for Excel and image files, demonstrating extensibility and versatility.
- **Command-Line Interface**: Offers a command-line interface for executing file conversion tasks, allowing users to specify input and output file paths and types conveniently.
- **Extensibility**: Other input/output pairs converters can be easily added to augment the existing functionality, providing flexibility for handling a wider range of file formats.
- **Direct Integration**: For specific projects, each converter script can directly leverage the separated package `file_conv_framework` to build custom converters tailored to project requirements.

## Classes

- `ConverterApp`: Main application class that orchestrates file conversion tasks using converter classes from `file_conv_framework`.
- `TextToTextConverter`: Converts text files to text files, inheriting from the base converter class provided by `file_conv_framework`.
- `XMLToJSONConverter`: Converts XML files to JSON files, demonstrating the use of framework classes for MIME type-based conversion.
- `TXTToMDConverter`: Converts text files to Markdown files, showcasing subclassing and customization of converter functionalities.
- `JSONToCSVConverter`: Converts JSON files to CSV files, highlighting the integration with `file_conv_framework` for file I/O operations.
- `CSVToXMLConverter`: Converts CSV files to XML files, leveraging the flexibility of `file_conv_framework` for handling different file types.
- `XLXSToCSVConverter`: Converts Excel files to CSV files, demonstrating custom file reader and writer classes for Excel files.

## Getting Started

To use the `file_conv_scripts` package, follow these steps:

1. Install the package along with its dependencies using your preferred package manager.
2. Import the required classes into your Python scripts or applications, ensuring that the `file_conv_framework` package is accessible.
3. Utilize the provided converter classes to perform file format conversions as needed, specifying input and output file paths and types.
4. Execute the scripts either programmatically or via the command-line interface, providing necessary arguments for file conversion tasks.

## Example Usage

Here's an example demonstrating how to use the `file_conv_scripts` package for converting an PNG file to PDF:

```bash
python file_conv_scripts/app.py examples/input/example.png -o examples/input/example.pdf
# or 
python file_conv_scripts/app.py examples/input/example.png -ot pdf
```

This command executes the `ConverterApp` class, initiating the conversion process from an PNG file to a PDF file using the appropriate converter classes.

## Contribution

Contributions to the `file_conv_scripts` package are welcome! Feel free to submit bug reports, feature requests, or pull requests via the GitHub repository. Additionally, consider extending the functionality by adding support for additional file formats or improving existing converter classes.
