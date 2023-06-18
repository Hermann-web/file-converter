from pathlib import Path
from abc import ABC, abstractmethod
from file_converter.filetype_handler import FileType

class InputFile:
    def __init__(self, file_path, file_type=None):
        self.file_path = Path(file_path)
        if file_type:
            self.file_type = FileType.from_suffix(file_type)
        else:
            self.file_type = FileType.from_path(file_path)
    
    def __str__(self):
        return str(Path(self.file_path).resolve())


class BaseConverter(ABC):
    def __init__(self, input_file: InputFile, output_file: InputFile):
        self.input_file = input_file
        self.output_file = output_file
        self._check_file_types()

    def convert(self):
        # log
        print(f"Converting {self.get_supported_input_type()} to {self.get_supported_output_type()}...")
        print(f"input = {self.input_file}")
        # convert file
        self._convert(self.input_file.file_path, self.output_file.file_path)
        # # save file
        # self.output_file.file_path.
        # log
        print(f"output = {self.output_file}")
        print("succeed")

    def _check_file_types(self):
        if not isinstance(self.input_file, InputFile):
            raise ValueError("Invalid input file")

        if not isinstance(self.output_file, InputFile):
            raise ValueError("Invalid output file")

        if self.input_file.file_type != self.get_supported_input_type():
            raise ValueError("Unsupported input file type")

        if self.output_file.file_type != self.get_supported_output_type():
            raise ValueError("Unsupported output file type")

    @classmethod
    def get_input_type(cls):
        return cls.get_supported_input_type()

    @classmethod
    def get_output_type(cls):
        return cls.get_supported_output_type()

    @classmethod
    def get_supported_input_type(cls) -> FileType:
        input_type = cls._get_supported_input_type()
        if not isinstance(input_type, FileType):
            raise ValueError("Invalid supported input file type")
        return input_type

    @classmethod
    def get_supported_output_type(cls) -> FileType:
        output_type = cls._get_supported_output_type()
        if not isinstance(output_type, FileType):
            raise ValueError("Invalid supported output file type")
        return output_type

    @classmethod
    @abstractmethod
    def _get_supported_input_type(cls) -> FileType:
        pass

    @classmethod
    @abstractmethod
    def _get_supported_output_type(cls) -> FileType:
        pass

    @abstractmethod
    def _convert(self, input_path:Path, output_path:Path):
        print("conversion method not implemented")
