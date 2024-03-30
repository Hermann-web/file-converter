"""
Main Module

This module contains the main application logic.
"""

import argparse

from file_conv_framework.converter_app import BaseConverterApp

from file_conv_scripts.converters import (
    CSVToXMLConverter,
    ImageToPDFConverter,
    JSONToCSVConverter,
    PDFToImageConverter,
    TXTToMDConverter,
    XLXSToCSVConverter,
    XMLToJSONConverter,
)


class ConverterApp(BaseConverterApp):

    converters = [
        XMLToJSONConverter,
        JSONToCSVConverter,
        CSVToXMLConverter,
        TXTToMDConverter,
        XLXSToCSVConverter,
        ImageToPDFConverter,
        PDFToImageConverter,
    ]


def main():
    parser = argparse.ArgumentParser(description="File BaseConverter App")
    parser.add_argument("file", type=str, help="Path to the input file")
    parser.add_argument(
        "-t", "--input-file-type", type=str, help="Type of the input file"
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=str,
        default="",
        help="Path to the output file (optional)",
    )
    parser.add_argument(
        "-ot", "--output-file-type", type=str, help="Type of the output file (optional)"
    )
    args = parser.parse_args()

    input_file_path = args.file
    input_file_type = args.input_file_type
    output_file_path = args.output_file
    output_file_type = args.output_file_type

    app = ConverterApp(
        input_file_path, input_file_type, output_file_path, output_file_type
    )
    app.run()


if __name__ == "__main__":
    main()
