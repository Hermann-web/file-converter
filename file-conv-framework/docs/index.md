# Table of Contents

* [file\_conv\_framework](#file_conv_framework)
* [file\_conv\_framework.logger](#file_conv_framework.logger)
  * [setup\_logger](#file_conv_framework.logger.setup_logger)
* [file\_conv\_framework.converter\_app](#file_conv_framework.converter_app)
  * [BaseConverterApp](#file_conv_framework.converter_app.BaseConverterApp)
    * [\_\_init\_\_](#file_conv_framework.converter_app.BaseConverterApp.__init__)
    * [add\_converter\_pair](#file_conv_framework.converter_app.BaseConverterApp.add_converter_pair)
    * [get\_supported\_conversions](#file_conv_framework.converter_app.BaseConverterApp.get_supported_conversions)
    * [run](#file_conv_framework.converter_app.BaseConverterApp.run)
* [file\_conv\_framework.io\_handler](#file_conv_framework.io_handler)
  * [FileReader](#file_conv_framework.io_handler.FileReader)
    * [check\_input\_format](#file_conv_framework.io_handler.FileReader.check_input_format)
    * [read\_content](#file_conv_framework.io_handler.FileReader.read_content)
  * [FileWriter](#file_conv_framework.io_handler.FileWriter)
    * [check\_output\_format](#file_conv_framework.io_handler.FileWriter.check_output_format)
    * [write\_content](#file_conv_framework.io_handler.FileWriter.write_content)
  * [SamePathReader](#file_conv_framework.io_handler.SamePathReader)
  * [TxtToStrReader](#file_conv_framework.io_handler.TxtToStrReader)
  * [StrToTxtWriter](#file_conv_framework.io_handler.StrToTxtWriter)
  * [CsvToListReader](#file_conv_framework.io_handler.CsvToListReader)
  * [ListToCsvWriter](#file_conv_framework.io_handler.ListToCsvWriter)
  * [JsonToDictReader](#file_conv_framework.io_handler.JsonToDictReader)
  * [DictToJsonWriter](#file_conv_framework.io_handler.DictToJsonWriter)
  * [XmlToStrReader](#file_conv_framework.io_handler.XmlToStrReader)
  * [StrToXmlWriter](#file_conv_framework.io_handler.StrToXmlWriter)
* [file\_conv\_framework.mimes](#file_conv_framework.mimes)
  * [MimeGuesser](#file_conv_framework.mimes.MimeGuesser)
    * [\_\_new\_\_](#file_conv_framework.mimes.MimeGuesser.__new__)
    * [get\_mime\_guesser](#file_conv_framework.mimes.MimeGuesser.get_mime_guesser)
    * [guess\_mime\_type\_from\_file](#file_conv_framework.mimes.MimeGuesser.guess_mime_type_from_file)
  * [guess\_mime\_type\_from\_file](#file_conv_framework.mimes.guess_mime_type_from_file)
* [file\_conv\_framework.filetypes](#file_conv_framework.filetypes)
  * [UnsupportedFileTypeError](#file_conv_framework.filetypes.UnsupportedFileTypeError)
  * [EmptySuffixError](#file_conv_framework.filetypes.EmptySuffixError)
  * [FileNotFoundError](#file_conv_framework.filetypes.FileNotFoundError)
  * [MismatchedException](#file_conv_framework.filetypes.MismatchedException)
  * [FileType](#file_conv_framework.filetypes.FileType)
    * [TEXT](#file_conv_framework.filetypes.FileType.TEXT)
    * [from\_suffix](#file_conv_framework.filetypes.FileType.from_suffix)
    * [from\_mimetype](#file_conv_framework.filetypes.FileType.from_mimetype)
    * [from\_path](#file_conv_framework.filetypes.FileType.from_path)
    * [is\_true\_filetype](#file_conv_framework.filetypes.FileType.is_true_filetype)
    * [get\_suffix](#file_conv_framework.filetypes.FileType.get_suffix)
    * [is\_valid\_suffix](#file_conv_framework.filetypes.FileType.is_valid_suffix)
    * [is\_valid\_path](#file_conv_framework.filetypes.FileType.is_valid_path)
    * [is\_valid\_mime\_type](#file_conv_framework.filetypes.FileType.is_valid_mime_type)
  * [test\_file\_type\_parsing](#file_conv_framework.filetypes.test_file_type_parsing)
  * [test\_file\_type\_matching](#file_conv_framework.filetypes.test_file_type_matching)
* [file\_conv\_framework.base\_converter](#file_conv_framework.base_converter)
  * [ResolvedInputFile](#file_conv_framework.base_converter.ResolvedInputFile)
    * [\_\_init\_\_](#file_conv_framework.base_converter.ResolvedInputFile.__init__)
    * [\_\_resolve\_filetype\_\_](#file_conv_framework.base_converter.ResolvedInputFile.__resolve_filetype__)
    * [\_\_str\_\_](#file_conv_framework.base_converter.ResolvedInputFile.__str__)
  * [BaseConverter](#file_conv_framework.base_converter.BaseConverter)
    * [\_\_init\_\_](#file_conv_framework.base_converter.BaseConverter.__init__)
    * [convert](#file_conv_framework.base_converter.BaseConverter.convert)
    * [check\_io\_handlers](#file_conv_framework.base_converter.BaseConverter.check_io_handlers)
    * [get\_supported\_input\_type](#file_conv_framework.base_converter.BaseConverter.get_supported_input_type)
    * [get\_supported\_output\_type](#file_conv_framework.base_converter.BaseConverter.get_supported_output_type)

<a id="file_conv_framework"></a>

# file\_conv\_framework

<a id="file_conv_framework.logger"></a>

# file\_conv\_framework.logger

<a id="file_conv_framework.logger.setup_logger"></a>

#### setup\_logger

```python
def setup_logger(log_file="logs/app.log")
```

Setup logger configuration.

<a id="file_conv_framework.converter_app"></a>

# file\_conv\_framework.converter\_app

Main Module

This module contains the main application logic.

<a id="file_conv_framework.converter_app.BaseConverterApp"></a>

## BaseConverterApp Objects

```python
class BaseConverterApp()
```

Main application class responsible for managing file conversions.

<a id="file_conv_framework.converter_app.BaseConverterApp.__init__"></a>

#### \_\_init\_\_

```python
def __init__(input_file_path: str,
             input_file_type: FileType = None,
             output_file_path: str = None,
             output_file_type: FileType = None)
```

Initializes the BaseConverterApp instance.

**Arguments**:

* `input_file_path` _str_ - The path to the input file.
* `input_file_type` _FileType, optional_ - The type of the input file. Defaults to None.
* `output_file_path` _str, optional_ - The path to the output file. Defaults to None.
* `output_file_type` _FileType, optional_ - The type of the output file. Defaults to None.

<a id="file_conv_framework.converter_app.BaseConverterApp.add_converter_pair"></a>

#### add\_converter\_pair

```python
def add_converter_pair(converter_class: Type[BaseConverter])
```

Adds a converter pair to the application.

**Arguments**:

* `converter_class` _Type[BaseConverter]_ - The converter class to add.
  
**Raises**:

* `ValueError` - If the converter class is invalid.

<a id="file_conv_framework.converter_app.BaseConverterApp.get_supported_conversions"></a>

#### get\_supported\_conversions

```python
def get_supported_conversions() -> Tuple[Tuple[FileType]]
```

Retrieves the supported conversions.

**Returns**:

* `Tuple[Tuple[FileType]]` - A tuple of tuples representing supported conversions.

<a id="file_conv_framework.converter_app.BaseConverterApp.run"></a>

#### run

```python
def run()
```

Runs the conversion process.

<a id="file_conv_framework.io_handler"></a>

# file\_conv\_framework.io\_handler

Input/Output Handler Module

This module is designed to provide a structured approach to handling file input and output operations across various
formats such as plain text, CSV, JSON, and potentially XML. It introduces a set of abstract base classes and concrete
implementations for reading from and writing to files, ensuring type safety and format consistency through method
signatures and runtime checks.

<a id="file_conv_framework.io_handler.FileReader"></a>

## FileReader Objects

```python
class FileReader(ABC)
```

Abstract base class for file readers.

<a id="file_conv_framework.io_handler.FileReader.check_input_format"></a>

#### check\_input\_format

```python
@abstractmethod
def check_input_format(content: Any) -> bool
```

Checks if the provided content matches the expected input format.

**Arguments**:

* `content` _Any_ - The content to be checked.
  
**Returns**:

* `bool` - True if the content matches the expected input format, False otherwise.

<a id="file_conv_framework.io_handler.FileReader.read_content"></a>

#### read\_content

```python
@abstractmethod
def read_content(input_path: Path) -> Any
```

Reads and returns the content from the given input path.

**Arguments**:

* `input_path` _Path_ - The path to the input file.
  
**Returns**:

* `Any` - The content read from the input file.

<a id="file_conv_framework.io_handler.FileWriter"></a>

## FileWriter Objects

```python
class FileWriter(ABC)
```

Abstract base class for file writers.

<a id="file_conv_framework.io_handler.FileWriter.check_output_format"></a>

#### check\_output\_format

```python
@abstractmethod
def check_output_format(content: Any) -> bool
```

Checks if the provided content matches the expected output format.

**Arguments**:

* `content` _Any_ - The content to be checked.
  
**Returns**:

* `bool` - True if the content matches the expected output format, False otherwise.

<a id="file_conv_framework.io_handler.FileWriter.write_content"></a>

#### write\_content

```python
@abstractmethod
def write_content(output_path: Path, output_content: Any)
```

Writes the provided content to the given output path.

**Arguments**:

* `output_path` _Path_ - The path to the output file.
* `output_content` _Any_ - The content to be written to the output file.

<a id="file_conv_framework.io_handler.SamePathReader"></a>

## SamePathReader Objects

```python
class SamePathReader(FileReader)
```

A FileReader that returns the input path itself, useful for operations where the file path is the desired output.

<a id="file_conv_framework.io_handler.TxtToStrReader"></a>

## TxtToStrReader Objects

```python
class TxtToStrReader(FileReader)
```

Reads content from a text file and returns it as a string.

<a id="file_conv_framework.io_handler.StrToTxtWriter"></a>

## StrToTxtWriter Objects

```python
class StrToTxtWriter(FileWriter)
```

Writes a string to a text file.

<a id="file_conv_framework.io_handler.CsvToListReader"></a>

## CsvToListReader Objects

```python
class CsvToListReader(FileReader)
```

Reads content from a CSV file and returns it as a list of lists, where each sublist represents a row.

<a id="file_conv_framework.io_handler.ListToCsvWriter"></a>

## ListToCsvWriter Objects

```python
class ListToCsvWriter(FileWriter)
```

Writes content as a list of lists to a CSV file, where each sublist represents a row.

<a id="file_conv_framework.io_handler.JsonToDictReader"></a>

## JsonToDictReader Objects

```python
class JsonToDictReader(FileReader)
```

Reads content from a JSON file and returns it as a dictionary.

<a id="file_conv_framework.io_handler.DictToJsonWriter"></a>

## DictToJsonWriter Objects

```python
class DictToJsonWriter(FileWriter)
```

Writes content from a dictionary to a JSON file.

<a id="file_conv_framework.io_handler.XmlToStrReader"></a>

## XmlToStrReader Objects

```python
class XmlToStrReader(FileReader)
```

Reads content from an XML file and returns it as a string.

<a id="file_conv_framework.io_handler.StrToXmlWriter"></a>

## StrToXmlWriter Objects

```python
class StrToXmlWriter(FileWriter)
```

Writes content as a string to an XML file.

<a id="file_conv_framework.mimes"></a>

# file\_conv\_framework.mimes

MIME Type Guesser Module

This module provides a singleton class for guessing MIME types from file paths using the python-magic library.

<a id="file_conv_framework.mimes.MimeGuesser"></a>

## MimeGuesser Objects

```python
class MimeGuesser()
```

Singleton class for guessing MIME types from file paths using the python-magic library.

<a id="file_conv_framework.mimes.MimeGuesser.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls)
```

Creates a new instance of the class if it doesn't exist already.

**Returns**:

* `MimeGuesser` - The instance of the MimeGuesser class.

<a id="file_conv_framework.mimes.MimeGuesser.get_mime_guesser"></a>

#### get\_mime\_guesser

```python
def get_mime_guesser()
```

Returns the mime_guesser instance.

**Returns**:

* `magic.Magic` - The instance of the mime_guesser.

<a id="file_conv_framework.mimes.MimeGuesser.guess_mime_type_from_file"></a>

#### guess\_mime\_type\_from\_file

```python
@classmethod
def guess_mime_type_from_file(cls, file_path)
```

Guesses the MIME type from the file path.

**Arguments**:

* `file_path` _str_ - The path to the file.
  
**Returns**:

* `str` - The guessed MIME type.
  
**Raises**:

* `ImportError` - If the python-magic library is not imported.

<a id="file_conv_framework.mimes.guess_mime_type_from_file"></a>

#### guess\_mime\_type\_from\_file

```python
def guess_mime_type_from_file(file_path)
```

Guesses the MIME type from the file path.

**Arguments**:

* `file_path` _str_ - The path to the file.
  
**Returns**:

* `str` - The guessed MIME type.

<a id="file_conv_framework.filetypes"></a>

# file\_conv\_framework.filetypes

File Type Definitions Module

This module provides a comprehensive framework for handling various file types within a file conversion context.
It defines classes and enumerations for identifying, validating, and working with different file types, based on
file extensions, MIME types, and optionally, file content. It also includes custom exceptions for handling common
errors related to file type processing.

Classes:
* UnsupportedFileTypeError: Custom exception for handling unsupported file types.
* EmptySuffixError: Specialized exception for cases where a file's suffix does not provide enough information
                    to determine its type.
* FileNotFoundError: Raised when a specified file does not exist.
* MismatchedException: Exception for handling cases where there's a mismatch between expected and actual file attributes.
* FileType: Enum class that encapsulates various file types supported by the system, providing methods for
            type determination from file attributes.

Functions:
* test_file_type_parsing(): Demonstrates and validates the parsing functionality for various file types.
* test_file_type_matching(): Tests the matching and validation capabilities of the FileType class.

Dependencies:
* collections.namedtuple: For defining simple classes for storing MIME type information.
* enum.Enum: For creating the FileType enumeration.
* pathlib.Path: For file path manipulations and checks.
* file_conv_framework.mimes.guess_mime_type_from_file: Utility function to guess MIME type from a file path.

<a id="file_conv_framework.filetypes.UnsupportedFileTypeError"></a>

## UnsupportedFileTypeError Objects

```python
class UnsupportedFileTypeError(Exception)
```

Exception raised for handling cases of unsupported file types.

<a id="file_conv_framework.filetypes.EmptySuffixError"></a>

## EmptySuffixError Objects

```python
class EmptySuffixError(UnsupportedFileTypeError)
```

Exception raised when a file's suffix does not provide enough information to determine its type.

<a id="file_conv_framework.filetypes.FileNotFoundError"></a>

## FileNotFoundError Objects

```python
class FileNotFoundError(Exception)
```

Exception raised when the specified file cannot be found.

<a id="file_conv_framework.filetypes.MismatchedException"></a>

## MismatchedException Objects

```python
class MismatchedException(Exception)
```

Exception raised for mismatches between expected and actual file attributes.

<a id="file_conv_framework.filetypes.FileType"></a>

## FileType Objects

```python
class FileType(Enum)
```

Enumeration of supported file types with methods for type determination and validation.

<a id="file_conv_framework.filetypes.FileType.TEXT"></a>

#### TEXT

put it at bottom as many other filetypes may be marked as text/plain too

<a id="file_conv_framework.filetypes.FileType.from_suffix"></a>

#### from\_suffix

```python
@classmethod
def from_suffix(cls, suffix: str, raise_err: bool = False)
```

Determines a FileType from a file's suffix.

**Arguments**:

* `suffix` _str_ - The file suffix (extension).
* `raise_err` _bool, optional_ - Whether to raise an exception if the type is unhandled. Defaults to False.
  
**Returns**:

* `FileType` - The determined FileType enumeration member.
  
**Raises**:

* `EmptySuffixError` - If the suffix is empty and raise_err is True.
* `UnsupportedFileTypeError` - If the file type is unhandled and raise_err is True.

<a id="file_conv_framework.filetypes.FileType.from_mimetype"></a>

#### from\_mimetype

```python
@classmethod
def from_mimetype(cls, file_path: str, raise_err: bool = False)
```

Determines a FileType from a file's MIME type.

**Arguments**:

* `file_path` _str_ - The path to the file.
* `raise_err` _bool, optional_ - Whether to raise an exception if the type is unhandled. Defaults to False.
  
**Returns**:

* `FileType` - The determined FileType enumeration member.
  
**Raises**:

* `FileNotFoundError` - If the file does not exist.
* `UnsupportedFileTypeError` - If the file type is unhandled and raise_err is True.

<a id="file_conv_framework.filetypes.FileType.from_path"></a>

#### from\_path

```python
@classmethod
def from_path(cls, path: Path, read_content=False, raise_err=False)
```

Determines the FileType of a file based on its path. Optionally reads the file's content to verify its type.

**Arguments**:

* `path` _Path_ - The path to the file.
* `read_content` _bool, optional_ - If True, the method also checks the file's content to determine its type.
  Defaults to False.
* `raise_err` _bool, optional_ - If True, raises exceptions for unsupported types or when file does not exist.
  Defaults to False.
  
**Returns**:

* `FileType` - The determined FileType enumeration member based on the file's suffix and/or content.
  
**Raises**:

* `FileNotFoundError` - If the file does not exist when attempting to read its content.
* `UnsupportedFileTypeError` - If the file type is unsupported and raise_err is True.
* `AssertionError` - If there is a mismatch between the file type determined from the file's suffix and its content.

<a id="file_conv_framework.filetypes.FileType.is_true_filetype"></a>

#### is\_true\_filetype

```python
def is_true_filetype()
```

Determines if the FileType instance represents a supported file type based on the presence of defined extensions.

**Returns**:

* `bool` - True if the FileType has at least one associated file extension, False otherwise.

<a id="file_conv_framework.filetypes.FileType.get_suffix"></a>

#### get\_suffix

```python
def get_suffix()
```

Retrieves the primary file extension associated with the FileType.

**Returns**:

* `str` - The primary file extension for the FileType, prefixed with a period.
  Returns an empty string if the FileType does not have an associated extension.

<a id="file_conv_framework.filetypes.FileType.is_valid_suffix"></a>

#### is\_valid\_suffix

```python
def is_valid_suffix(suffix: str, raise_err=False)
```

Validates whether a given file extension matches the FileType's expected extensions.

**Arguments**:

* `suffix` _str_ - The file extension to validate, including the leading period (e.g., ".txt").
* `raise_err` _bool, optional_ - If True, raises a MismatchedException for invalid extensions.
  Defaults to False.
  
**Returns**:

* `bool` - True if the suffix matches one of the FileType's extensions, False otherwise.
  
**Raises**:

* `MismatchedException` - If the suffix does not match and raise_err is True.

<a id="file_conv_framework.filetypes.FileType.is_valid_path"></a>

#### is\_valid\_path

```python
def is_valid_path(path: Path, raise_err=False, read_content=False)
```

Validates whether the file at a given path matches the FileType, optionally checking the file's content.

**Arguments**:

* `path` _Path_ - The path to the file to validate.
* `raise_err` _bool, optional_ - If True, raises a MismatchedException for a mismatching file type.
  Defaults to False.
* `read_content` _bool, optional_ - If True, also validates the file's content type against the FileType.
  Defaults to False.
  
**Returns**:

* `bool` - True if the file's type matches the FileType, based on its path and optionally its content.
  False otherwise.
  
**Raises**:

* `MismatchedException` - If the file's type does not match and raise_err is True.

<a id="file_conv_framework.filetypes.FileType.is_valid_mime_type"></a>

#### is\_valid\_mime\_type

```python
def is_valid_mime_type(path: Path, raise_err=False)
```

Validates whether the MIME type of the file at the specified path aligns with the FileType's expected MIME types.

This method first determines the FileType based on the file's actual MIME type (determined by reading the file's content)
and then checks if this determined FileType matches the instance calling this method. Special consideration is given to
FileType.TEXT, where a broader compatibility check is performed due to the generic nature of text MIME types.

**Arguments**:

* `path` _Path_ - The path to the file whose MIME type is to be validated.
* `raise_err` _bool, optional_ - If True, a MismatchedException is raised if the file's MIME type does not match
  the expected MIME types of the FileType instance. Defaults to False.
  
**Returns**:

* `bool` - True if the file's MIME type matches the expected MIME types for this FileType instance or if special
  compatibility conditions are met (e.g., for FileType.TEXT with "text/plain"). Otherwise, False.
  
**Raises**:

* `MismatchedException` - If raise_err is True and the file's MIME type does not match the expected MIME types
  for this FileType instance, including detailed information about the mismatch.

<a id="file_conv_framework.filetypes.test_file_type_parsing"></a>

#### test\_file\_type\_parsing

```python
def test_file_type_parsing()
```

Tests for validating the functionality of file type parsing.

<a id="file_conv_framework.filetypes.test_file_type_matching"></a>

#### test\_file\_type\_matching

```python
def test_file_type_matching()
```

Tests for validating the functionality of file type matching.

<a id="file_conv_framework.base_converter"></a>

# file\_conv\_framework.base\_converter

Base Converter Module

This module serves as a foundation for creating file conversion utilities. It facilitates the development
of file converters through abstract base classes, managing file types, and handling input and output files
efficiently. The module is designed to be extendible, supporting various file formats and conversion strategies.

Classes:
* ResolvedInputFile: Manages file paths and types, resolving them as needed.
* BaseConverter: An abstract base class for creating specific file format converters, enforcing the implementation
                 of file conversion logic.

Exceptions:
* ValueError: Raised when file paths or types are incompatible or unsupported.
* AssertionError: Ensured for internal consistency checks, confirming that file types match expected values.

<a id="file_conv_framework.base_converter.ResolvedInputFile"></a>

## ResolvedInputFile Objects

```python
class ResolvedInputFile()
```

Handles resolving the file type of a given file, managing path adjustments and optional content reading.

<a id="file_conv_framework.base_converter.ResolvedInputFile.__init__"></a>

#### \_\_init\_\_

```python
def __init__(file_path, file_type=None, add_suffix=False, read_content=False)
```

Initializes an instance of ResolvedInputFile with options for type resolution and path modification.

**Arguments**:

* `file_path` _str_ - The path to the file.
* `file_type` _FileType, optional_ - The explicit type of the file. If None, attempts to resolve based on the path or content.
* `add_suffix` _bool, optional_ - Whether to append the resolved file type's suffix to the file path. Defaults to False.
* `read_content` _bool, optional_ - Whether to read the file's content to assist in type resolution. Defaults to False.

<a id="file_conv_framework.base_converter.ResolvedInputFile.__resolve_filetype__"></a>

#### \_\_resolve\_filetype\_\_

```python
def __resolve_filetype__(file_type, file_path, read_content) -> FileType
```

Determines the file type, utilizing the provided type, file path, or content as needed.

**Arguments**:

* `file_type` _FileType or str, optional_ - An explicit file type or extension.
* `file_path` _str_ - The path to the file, used if file_type is not provided.
* `read_content` _bool_ - Indicates if file content should be used to help resolve the file type.
  
**Returns**:

* `FileType` - The resolved file type.

<a id="file_conv_framework.base_converter.ResolvedInputFile.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Returns the absolute file path as a string.

**Returns**:

* `str` - The resolved file path.

<a id="file_conv_framework.base_converter.BaseConverter"></a>

## BaseConverter Objects

```python
class BaseConverter(ABC)
```

Abstract base class for file conversion, defining the template for input to output file conversion.

<a id="file_conv_framework.base_converter.BaseConverter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(input_file: ResolvedInputFile, output_file: ResolvedInputFile)
```

Sets up the converter with specified input and output files, ensuring compatibility.

**Arguments**:

* `input_file` _ResolvedInputFile_ - The input file with resolved type.
* `output_file` _ResolvedInputFile_ - The output file where the converted data will be saved.

<a id="file_conv_framework.base_converter.BaseConverter.convert"></a>

#### convert

```python
def convert()
```

Orchestrates the file conversion process, including reading, converting, and writing the file.

<a id="file_conv_framework.base_converter.BaseConverter.check_io_handlers"></a>

#### check\_io\_handlers

```python
def check_io_handlers()
```

Ensures that valid I/O handlers (file reader and writer) are set for the conversion.

<a id="file_conv_framework.base_converter.BaseConverter.get_supported_input_type"></a>

#### get\_supported\_input\_type

```python
@classmethod
def get_supported_input_type(cls) -> FileType
```

Defines the supported input file type for this converter.

**Returns**:

* `FileType` - The file type supported for input.

<a id="file_conv_framework.base_converter.BaseConverter.get_supported_output_type"></a>

#### get\_supported\_output\_type

```python
@classmethod
def get_supported_output_type(cls) -> FileType
```

Defines the supported output file type for this converter.

**Returns**:

* `FileType` - The file type supported for output.
