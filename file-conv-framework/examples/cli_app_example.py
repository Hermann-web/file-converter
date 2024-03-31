"""
Main Module

This module contains the main application logic.
"""

import argparse
import sys

from simple_converter import TXTToMDConverter, TXTToTXTConverter

sys.path.append(".")

from file_conv_framework.converter_app import BaseConverterApp


class ConverterApp(BaseConverterApp):

    converters = [TXTToMDConverter, TXTToTXTConverter]


def main():
    """
    # Usage Example

    ## Usage Example of TXTToTXTConverter to merge txt files
    
    ```bash
    find examples -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output -ot txt
    # or
    python examples/cli_app_example.py examples/cli_app_example.py examples/data/example.txt -o examples/output -ot txt
    # or 
    python examples/cli_app_example.py examples/data/example.txt  examples/data/example2.txt -o examples/output/example.txt
    ```

    ## Usage Examples of TXTToMDConverter to merge txt files into a md file

    ```bash
    find examples -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output.md
    ```

    """
    parser = argparse.ArgumentParser(description="File BaseConverter App")
    parser.add_argument("files", nargs="+", type=str, help="Paths to the input files")
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

    input_file_paths = args.files
    input_file_type = args.input_file_type
    output_file_path = args.output_file
    output_file_type = args.output_file_type
    print("input_file_paths = ", input_file_paths)

    app = ConverterApp(
        input_file_paths, input_file_type, output_file_path, output_file_type
    )
    app.run()


if __name__ == "__main__":
    main()
