import argparse
from pathlib import Path
from typing import Type, Tuple
from file_converter.filetype_handler import FileType
from file_converter.convertion_handler import InputFile, BaseConverter
from file_converter.converters import (
    XMLToJSONConverter,
    JSONToCSVConverter,
    CSVToXMLConverter,
    TXTToMDConverter
)

class ConverterApp:
    def __init__(self, input_file_path, input_file_type=None, output_file_path=None, output_file_type=None):
        self.converters = {}
        self.input_file = InputFile(input_file_path, file_type=input_file_type)
        if output_file_path:
            self.output_file = InputFile(output_file_path, file_type=output_file_type)
        else:
            output_file_path = str(Path(input_file_path).with_suffix(''))
            self.output_file = InputFile(output_file_path, file_type=output_file_type)
        
        self.add_converter_pair(XMLToJSONConverter)
        self.add_converter_pair(JSONToCSVConverter)
        self.add_converter_pair(CSVToXMLConverter)
        self.add_converter_pair(TXTToMDConverter)

    def add_converter_pair(self, converter_class: Type[BaseConverter]):
        # Check if the converter_class is a subclass of BaseConverter
        if not issubclass(converter_class, BaseConverter):
            raise ValueError("Invalid converter class")
        
        # Add the converter pair to the converters dictionary
        self.converters[(converter_class.get_input_type(), converter_class.get_output_type())] = converter_class
    
    def get_supported_conversions(self) -> Tuple[Tuple[FileType]]:
        return tuple(self.converters.keys())

    def run(self):
        if self.output_file:
            converter_class = self.converters.get((self.input_file.file_type, self.output_file.file_type))
            if converter_class:
                converter = converter_class(self.input_file, self.output_file)
                converter.convert()
            else:
                _ = '\n ' + '\n '.join(map(lambda x: f"{x[0]} -> {x[1]}",self.get_supported_conversions()))
                print(f"Conversion not supported. Supported convertions are {_}")
        else:
            print("Output file path not provided")



def main():
    parser = argparse.ArgumentParser(description="File BaseConverter App")
    parser.add_argument(
        'file',
        type=str,
        help='Path to the input file'
    )
    parser.add_argument(
        '-t',
        '--input-file-type',
        type=str,
        help='Type of the input file'
    )
    parser.add_argument(
        '-o',
        '--output-file',
        type=str,
        default="",
        help='Path to the output file (optional)'
    )
    parser.add_argument(
        '-ot',
        '--output-file-type',
        type=str,
        help='Type of the output file (optional)'
    )
    args = parser.parse_args()

    input_file_path = args.file
    input_file_type = args.input_file_type
    output_file_path = args.output_file
    output_file_type = args.output_file_type

    app = ConverterApp(input_file_path, input_file_type, output_file_path, output_file_type)
    app.run()


if __name__ == '__main__':
    main()

