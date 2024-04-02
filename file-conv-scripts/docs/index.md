# Table of Contents

* [file\_conv\_scripts](#file_conv_scripts)
* [file\_conv\_scripts.io\_handlers.img\_pillow](#file_conv_scripts.io_handlers.img_pillow)
  * [ImageToPillowReader](#file_conv_scripts.io_handlers.img_pillow.ImageToPillowReader)
  * [PillowToImageWriter](#file_conv_scripts.io_handlers.img_pillow.PillowToImageWriter)
* [file\_conv\_scripts.io\_handlers](#file_conv_scripts.io_handlers)
* [file\_conv\_scripts.io\_handlers.img\_opencv](#file_conv_scripts.io_handlers.img_opencv)
  * [ImageToOpenCVReader](#file_conv_scripts.io_handlers.img_opencv.ImageToOpenCVReader)
  * [OpenCVToImageWriter](#file_conv_scripts.io_handlers.img_opencv.OpenCVToImageWriter)
* [file\_conv\_scripts.io\_handlers.pdf](#file_conv_scripts.io_handlers.pdf)
  * [PdfToPyPdfReader](#file_conv_scripts.io_handlers.pdf.PdfToPyPdfReader)
  * [PyPdfToPdfWriter](#file_conv_scripts.io_handlers.pdf.PyPdfToPdfWriter)
* [file\_conv\_scripts.io\_handlers.spreadsheet](#file_conv_scripts.io_handlers.spreadsheet)
  * [SpreadsheetToPandasReader](#file_conv_scripts.io_handlers.spreadsheet.SpreadsheetToPandasReader)
  * [PandasToSpreadsheetWriter](#file_conv_scripts.io_handlers.spreadsheet.PandasToSpreadsheetWriter)
* [file\_conv\_scripts.io\_handlers.video](#file_conv_scripts.io_handlers.video)
  * [VideoArrayWriter](#file_conv_scripts.io_handlers.video.VideoArrayWriter)
* [file\_conv\_scripts.app](#file_conv_scripts.app)
  * [ConverterApp](#file_conv_scripts.app.ConverterApp)
  * [main](#file_conv_scripts.app.main)
* [file\_conv\_scripts.converters](#file_conv_scripts.converters)
  * [TextToTextConverter](#file_conv_scripts.converters.TextToTextConverter)
  * [XMLToJSONConverter](#file_conv_scripts.converters.XMLToJSONConverter)
  * [TXTToMDConverter](#file_conv_scripts.converters.TXTToMDConverter)
  * [JSONToCSVConverter](#file_conv_scripts.converters.JSONToCSVConverter)
  * [CSVToXMLConverter](#file_conv_scripts.converters.CSVToXMLConverter)
  * [XLSXToCSVConverter](#file_conv_scripts.converters.XLSXToCSVConverter)
  * [ImageToPDFConverter](#file_conv_scripts.converters.ImageToPDFConverter)
  * [ImageToPDFConverterWithPyPdf2](#file_conv_scripts.converters.ImageToPDFConverterWithPyPdf2)
  * [PDFToImageConverter](#file_conv_scripts.converters.PDFToImageConverter)
  * [PDFToImageExtractor](#file_conv_scripts.converters.PDFToImageExtractor)
  * [ImageToVideoConverterWithPillow](#file_conv_scripts.converters.ImageToVideoConverterWithPillow)
  * [ImageToVideoConverterWithOpenCV](#file_conv_scripts.converters.ImageToVideoConverterWithOpenCV)
* [file\_conv\_scripts.utils.image\_to\_video](#file_conv_scripts.utils.image_to_video)

<a id="file_conv_scripts"></a>

# file\_conv\_scripts

<a id="file_conv_scripts.io_handlers.img_pillow"></a>

# file\_conv\_scripts.io\_handlers.img\_pillow

Image File I/O Handlers

This module provides classes for reading and writing image files using the Pillow library. It includes abstract base classes
and concrete implementations for converting between image files and Pillow Image objects.

<a id="file_conv_scripts.io_handlers.img_pillow.ImageToPillowReader"></a>

## ImageToPillowReader Objects

```python
class ImageToPillowReader(FileReader)
```

Reads an image file and returns a Pillow Image object.

<a id="file_conv_scripts.io_handlers.img_pillow.PillowToImageWriter"></a>

## PillowToImageWriter Objects

```python
class PillowToImageWriter(FileWriter)
```

Writes a Pillow Image object to an image file.

<a id="file_conv_scripts.io_handlers"></a>

# file\_conv\_scripts.io\_handlers

<a id="file_conv_scripts.io_handlers.img_opencv"></a>

# file\_conv\_scripts.io\_handlers.img\_opencv

File: img_opencv.py
Author: Hermann Agossou
Description: This module provides classes for reading and writing images using OpenCV.

<a id="file_conv_scripts.io_handlers.img_opencv.ImageToOpenCVReader"></a>

## ImageToOpenCVReader Objects

```python
class ImageToOpenCVReader(FileReader)
```

Reads an image file and returns an OpenCV image object.

<a id="file_conv_scripts.io_handlers.img_opencv.OpenCVToImageWriter"></a>

## OpenCVToImageWriter Objects

```python
class OpenCVToImageWriter(FileWriter)
```

Writes an OpenCV image object to an image file.

<a id="file_conv_scripts.io_handlers.pdf"></a>

# file\_conv\_scripts.io\_handlers.pdf

PDF File I/O Handlers

This module provides classes for reading and writing PDF files using the PyPDF2 library. It includes abstract base classes
and concrete implementations for converting between PDF files and PyPDF2 PdfReader objects.

<a id="file_conv_scripts.io_handlers.pdf.PdfToPyPdfReader"></a>

## PdfToPyPdfReader Objects

```python
class PdfToPyPdfReader(FileReader)
```

Reads a PDF file and returns a [PyPDF2 PdfReader object](https://pypdf2.readthedocs.io/en/3.0.0/modules/PdfReader.html).

<a id="file_conv_scripts.io_handlers.pdf.PyPdfToPdfWriter"></a>

## PyPdfToPdfWriter Objects

```python
class PyPdfToPdfWriter(FileWriter)
```

Writes the provided [PyPDF2 PdfWriter object](https://pypdf2.readthedocs.io/en/3.0.0/modules/PdfWriter.html)

<a id="file_conv_scripts.io_handlers.spreadsheet"></a>

# file\_conv\_scripts.io\_handlers.spreadsheet

Spreadsheet I/O Handlers

This module provides classes for reading and writing spreadsheet files using the pandas library. It includes abstract base classes
and concrete implementations for converting between spreadsheet files and pandas DataFrame objects.

<a id="file_conv_scripts.io_handlers.spreadsheet.SpreadsheetToPandasReader"></a>

## SpreadsheetToPandasReader Objects

```python
class SpreadsheetToPandasReader(FileReader)
```

Reads a spreadsheet file and returns a pandas DataFrame object.

<a id="file_conv_scripts.io_handlers.spreadsheet.PandasToSpreadsheetWriter"></a>

## PandasToSpreadsheetWriter Objects

```python
class PandasToSpreadsheetWriter(FileWriter)
```

Writes a pandas DataFrame object to a spreadsheet file.

<a id="file_conv_scripts.io_handlers.video"></a>

# file\_conv\_scripts.io\_handlers.video

<a id="file_conv_scripts.io_handlers.video.VideoArrayWriter"></a>

## VideoArrayWriter Objects

```python
class VideoArrayWriter(FileWriter)
```

Writes a video to a file using a list of image arrays.

<a id="file_conv_scripts.app"></a>

# file\_conv\_scripts.app

Main Module

This module contains the main application logic.

<a id="file_conv_scripts.app.ConverterApp"></a>

## ConverterApp Objects

```python
class ConverterApp(BaseConverterApp)
```

Application for file conversion.

<a id="file_conv_scripts.app.main"></a>

#### main

```python
def main()
```

Main function to run the file conversion application.

<a id="file_conv_scripts.converters"></a>

# file\_conv\_scripts.converters

Conversion Handlers

This module provides classes for converting between different file formats. It includes concrete implementations of conversion classes for various file types.

<a id="file_conv_scripts.converters.TextToTextConverter"></a>

## TextToTextConverter Objects

```python
class TextToTextConverter(BaseConverter)
```

Converts text files to text format.

<a id="file_conv_scripts.converters.XMLToJSONConverter"></a>

## XMLToJSONConverter Objects

```python
class XMLToJSONConverter(BaseConverter)
```

Converts XML files to JSON format.

<a id="file_conv_scripts.converters.TXTToMDConverter"></a>

## TXTToMDConverter Objects

```python
class TXTToMDConverter(TextToTextConverter)
```

Converts text files to Markdown format.

<a id="file_conv_scripts.converters.JSONToCSVConverter"></a>

## JSONToCSVConverter Objects

```python
class JSONToCSVConverter(BaseConverter)
```

Converts JSON files to CSV format.

<a id="file_conv_scripts.converters.CSVToXMLConverter"></a>

## CSVToXMLConverter Objects

```python
class CSVToXMLConverter(BaseConverter)
```

Converts CSV files to XML format.

<a id="file_conv_scripts.converters.XLSXToCSVConverter"></a>

## XLSXToCSVConverter Objects

```python
class XLSXToCSVConverter(BaseConverter)
```

Converts Excel files to CSV format.

<a id="file_conv_scripts.converters.ImageToPDFConverter"></a>

## ImageToPDFConverter Objects

```python
class ImageToPDFConverter(BaseConverter)
```

Converts image files to PDF format.

<a id="file_conv_scripts.converters.ImageToPDFConverterWithPyPdf2"></a>

## ImageToPDFConverterWithPyPdf2 Objects

```python
class ImageToPDFConverterWithPyPdf2(BaseConverter)
```

Converts image files to PDF format using PyPDF2.

<a id="file_conv_scripts.converters.PDFToImageConverter"></a>

## PDFToImageConverter Objects

```python
class PDFToImageConverter(BaseConverter)
```

Converts PDF files to image format.

<a id="file_conv_scripts.converters.PDFToImageExtractor"></a>

## PDFToImageExtractor Objects

```python
class PDFToImageExtractor(BaseConverter)
```

Converts PDF files to image format.

<a id="file_conv_scripts.converters.ImageToVideoConverterWithPillow"></a>

## ImageToVideoConverterWithPillow Objects

```python
class ImageToVideoConverterWithPillow(BaseConverter)
```

Converts image files to video format.

<a id="file_conv_scripts.converters.ImageToVideoConverterWithOpenCV"></a>

## ImageToVideoConverterWithOpenCV Objects

```python
class ImageToVideoConverterWithOpenCV(BaseConverter)
```

Converts image files to video format.

<a id="file_conv_scripts.utils.image_to_video"></a>

# file\_conv\_scripts.utils.image\_to\_video

images_to_video.py

A script to convert a sequence of images into a video file using OpenCV.

Dependencies:
- OpenCV (cv2): A computer vision library for image and video processing.
- pathlib: An object-oriented interface to filesystem paths.

Usage:
$ python images_to_video.py <input_images> <output_video>

**Arguments**:

- `input_images` - List of input image files to be converted into a video file.
- `Example` - image1.jpg image2.jpg
- `output_video` - Path to the output video file.
- `Example` - output_video.avi
  

**Example**:

  $ python images_to_video.py image1.jpg image2.jpg output_video.avi
  
- `Author` - Hermann Agossou
- `Date` - Date of creation/modification

