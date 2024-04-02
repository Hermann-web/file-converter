# Table of Contents

* [openconv](#openconv)
* [openconv.io\_handlers.img\_pillow](#openconv.io_handlers.img_pillow)
  * [ImageToPillowReader](#openconv.io_handlers.img_pillow.ImageToPillowReader)
  * [PillowToImageWriter](#openconv.io_handlers.img_pillow.PillowToImageWriter)
* [openconv.io\_handlers](#openconv.io_handlers)
* [openconv.io\_handlers.img\_opencv](#openconv.io_handlers.img_opencv)
  * [ImageToOpenCVReader](#openconv.io_handlers.img_opencv.ImageToOpenCVReader)
  * [OpenCVToImageWriter](#openconv.io_handlers.img_opencv.OpenCVToImageWriter)
* [openconv.io\_handlers.pdf](#openconv.io_handlers.pdf)
  * [PdfToPyPdfReader](#openconv.io_handlers.pdf.PdfToPyPdfReader)
  * [PyPdfToPdfWriter](#openconv.io_handlers.pdf.PyPdfToPdfWriter)
* [openconv.io\_handlers.spreadsheet](#openconv.io_handlers.spreadsheet)
  * [SpreadsheetToPandasReader](#openconv.io_handlers.spreadsheet.SpreadsheetToPandasReader)
  * [PandasToSpreadsheetWriter](#openconv.io_handlers.spreadsheet.PandasToSpreadsheetWriter)
* [openconv.io\_handlers.video](#openconv.io_handlers.video)
  * [VideoArrayWriter](#openconv.io_handlers.video.VideoArrayWriter)
* [openconv.app](#openconv.app)
  * [ConverterApp](#openconv.app.ConverterApp)
  * [main](#openconv.app.main)
* [openconv.converters](#openconv.converters)
  * [TextToTextConverter](#openconv.converters.TextToTextConverter)
  * [XMLToJSONConverter](#openconv.converters.XMLToJSONConverter)
  * [TXTToMDConverter](#openconv.converters.TXTToMDConverter)
  * [JSONToCSVConverter](#openconv.converters.JSONToCSVConverter)
  * [CSVToXMLConverter](#openconv.converters.CSVToXMLConverter)
  * [XLSXToCSVConverter](#openconv.converters.XLSXToCSVConverter)
  * [ImageToPDFConverter](#openconv.converters.ImageToPDFConverter)
  * [ImageToPDFConverterWithPyPdf2](#openconv.converters.ImageToPDFConverterWithPyPdf2)
  * [PDFToImageConverter](#openconv.converters.PDFToImageConverter)
  * [PDFToImageExtractor](#openconv.converters.PDFToImageExtractor)
  * [ImageToVideoConverterWithPillow](#openconv.converters.ImageToVideoConverterWithPillow)
  * [ImageToVideoConverterWithOpenCV](#openconv.converters.ImageToVideoConverterWithOpenCV)
* [openconv.utils.image\_to\_video](#openconv.utils.image_to_video)

<a id="openconv"></a>

# openconv

<a id="openconv.io_handlers.img_pillow"></a>

# openconv.io\_handlers.img\_pillow

Image File I/O Handlers

This module provides classes for reading and writing image files using the Pillow library. It includes abstract base classes
and concrete implementations for converting between image files and Pillow Image objects.

<a id="openconv.io_handlers.img_pillow.ImageToPillowReader"></a>

## ImageToPillowReader Objects

```python
class ImageToPillowReader(FileReader)
```

Reads an image file and returns a Pillow Image object.

<a id="openconv.io_handlers.img_pillow.PillowToImageWriter"></a>

## PillowToImageWriter Objects

```python
class PillowToImageWriter(FileWriter)
```

Writes a Pillow Image object to an image file.

<a id="openconv.io_handlers"></a>

# openconv.io\_handlers

<a id="openconv.io_handlers.img_opencv"></a>

# openconv.io\_handlers.img\_opencv

File: img_opencv.py
Author: Hermann Agossou
Description: This module provides classes for reading and writing images using OpenCV.

<a id="openconv.io_handlers.img_opencv.ImageToOpenCVReader"></a>

## ImageToOpenCVReader Objects

```python
class ImageToOpenCVReader(FileReader)
```

Reads an image file and returns an OpenCV image object.

<a id="openconv.io_handlers.img_opencv.OpenCVToImageWriter"></a>

## OpenCVToImageWriter Objects

```python
class OpenCVToImageWriter(FileWriter)
```

Writes an OpenCV image object to an image file.

<a id="openconv.io_handlers.pdf"></a>

# openconv.io\_handlers.pdf

PDF File I/O Handlers

This module provides classes for reading and writing PDF files using the PyPDF2 library. It includes abstract base classes
and concrete implementations for converting between PDF files and PyPDF2 PdfReader objects.

<a id="openconv.io_handlers.pdf.PdfToPyPdfReader"></a>

## PdfToPyPdfReader Objects

```python
class PdfToPyPdfReader(FileReader)
```

Reads a PDF file and returns a [PyPDF2 PdfReader object](https://pypdf2.readthedocs.io/en/3.0.0/modules/PdfReader.html).

<a id="openconv.io_handlers.pdf.PyPdfToPdfWriter"></a>

## PyPdfToPdfWriter Objects

```python
class PyPdfToPdfWriter(FileWriter)
```

Writes the provided [PyPDF2 PdfWriter object](https://pypdf2.readthedocs.io/en/3.0.0/modules/PdfWriter.html)

<a id="openconv.io_handlers.spreadsheet"></a>

# openconv.io\_handlers.spreadsheet

Spreadsheet I/O Handlers

This module provides classes for reading and writing spreadsheet files using the pandas library. It includes abstract base classes
and concrete implementations for converting between spreadsheet files and pandas DataFrame objects.

<a id="openconv.io_handlers.spreadsheet.SpreadsheetToPandasReader"></a>

## SpreadsheetToPandasReader Objects

```python
class SpreadsheetToPandasReader(FileReader)
```

Reads a spreadsheet file and returns a pandas DataFrame object.

<a id="openconv.io_handlers.spreadsheet.PandasToSpreadsheetWriter"></a>

## PandasToSpreadsheetWriter Objects

```python
class PandasToSpreadsheetWriter(FileWriter)
```

Writes a pandas DataFrame object to a spreadsheet file.

<a id="openconv.io_handlers.video"></a>

# openconv.io\_handlers.video

<a id="openconv.io_handlers.video.VideoArrayWriter"></a>

## VideoArrayWriter Objects

```python
class VideoArrayWriter(FileWriter)
```

Writes a video to a file using a list of image arrays.

<a id="openconv.app"></a>

# openconv.app

Main Module

This module contains the main application logic.

<a id="openconv.app.ConverterApp"></a>

## ConverterApp Objects

```python
class ConverterApp(BaseConverterApp)
```

Application for file conversion.

<a id="openconv.app.main"></a>

#### main

```python
def main()
```

Main function to run the file conversion application.

<a id="openconv.converters"></a>

# openconv.converters

Conversion Handlers

This module provides classes for converting between different file formats. It includes concrete implementations of conversion classes for various file types.

<a id="openconv.converters.TextToTextConverter"></a>

## TextToTextConverter Objects

```python
class TextToTextConverter(BaseConverter)
```

Converts text files to text format.

<a id="openconv.converters.XMLToJSONConverter"></a>

## XMLToJSONConverter Objects

```python
class XMLToJSONConverter(BaseConverter)
```

Converts XML files to JSON format.

<a id="openconv.converters.TXTToMDConverter"></a>

## TXTToMDConverter Objects

```python
class TXTToMDConverter(TextToTextConverter)
```

Converts text files to Markdown format.

<a id="openconv.converters.JSONToCSVConverter"></a>

## JSONToCSVConverter Objects

```python
class JSONToCSVConverter(BaseConverter)
```

Converts JSON files to CSV format.

<a id="openconv.converters.CSVToXMLConverter"></a>

## CSVToXMLConverter Objects

```python
class CSVToXMLConverter(BaseConverter)
```

Converts CSV files to XML format.

<a id="openconv.converters.XLSXToCSVConverter"></a>

## XLSXToCSVConverter Objects

```python
class XLSXToCSVConverter(BaseConverter)
```

Converts Excel files to CSV format.

<a id="openconv.converters.ImageToPDFConverter"></a>

## ImageToPDFConverter Objects

```python
class ImageToPDFConverter(BaseConverter)
```

Converts image files to PDF format.

<a id="openconv.converters.ImageToPDFConverterWithPyPdf2"></a>

## ImageToPDFConverterWithPyPdf2 Objects

```python
class ImageToPDFConverterWithPyPdf2(BaseConverter)
```

Converts image files to PDF format using PyPDF2.

<a id="openconv.converters.PDFToImageConverter"></a>

## PDFToImageConverter Objects

```python
class PDFToImageConverter(BaseConverter)
```

Converts PDF files to image format.

<a id="openconv.converters.PDFToImageExtractor"></a>

## PDFToImageExtractor Objects

```python
class PDFToImageExtractor(BaseConverter)
```

Converts PDF files to image format.

<a id="openconv.converters.ImageToVideoConverterWithPillow"></a>

## ImageToVideoConverterWithPillow Objects

```python
class ImageToVideoConverterWithPillow(BaseConverter)
```

Converts image files to video format.

<a id="openconv.converters.ImageToVideoConverterWithOpenCV"></a>

## ImageToVideoConverterWithOpenCV Objects

```python
class ImageToVideoConverterWithOpenCV(BaseConverter)
```

Converts image files to video format.

<a id="openconv.utils.image_to_video"></a>

# openconv.utils.image\_to\_video

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

