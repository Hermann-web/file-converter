"""
File Type Definitions Module

This module defines enums and classes related to different file types.
"""

from enum import Enum
from collections import namedtuple
from pathlib import Path

from file_conv_framework.mimes import guess_mime_type_from_file

class UnsupportedFileTypeError(Exception):
    """Exception raised for unsupported file types."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class EmptySuffixError(UnsupportedFileTypeError):
    """Exception raised for unsupported file types."""

    def __init__(self):
        self.message = "Filetype not parsed from empty suffix."
        super().__init__(self.message)

class FileNotFoundError(Exception):
    """Exception raised for file not found errors."""

    def __init__(self, file_path):
        self.file_path = file_path
        message = f"File '{file_path}' does not exist."
        super().__init__(message)

class MismatchedException(Exception):
    def __init__(self, label, claimed_val, expected_vals):
        super().__init__(f"Mismatched {label}: Found '{claimed_val}', Expected one of '{expected_vals}'")



MimeType = namedtuple('MimeType', ['extensions', 'mime_types', 'upper_mime_types'], defaults=[(),(),()])

class FileType(Enum):
    NOTYPE = MimeType([], [])
    CSV = MimeType(['csv'], ['text/csv'])
    EXCEL = MimeType(['xls', 'xlsx'], ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'])
    JSON = MimeType(['json'], ['application/json'])
    JPG = MimeType(['jpg'], ['image/jpeg'])
    JPEG = MimeType(['jpeg'], ['image/jpeg'])
    PNG = MimeType(['png'], ['image/png'])
    GIF = MimeType(['gif'], ['image/gif'])
    XML = MimeType(['xml'], ['application/xml', 'text/xml'])
    MARKDOWN = MimeType(['md'], ['text/markdown'], ['text/plain'])
    TEXT = MimeType(['txt'], ['text/plain'])  # put it at bottom as many other filetypes may be marked as text/plain too
    UNHANDLED = MimeType([], [])

    @classmethod
    def from_suffix(cls, suffix: str, raise_err: bool = False):
        suffix = suffix.lower().lstrip('.')
        if not suffix:
            if raise_err:
                raise EmptySuffixError()
            else:
                return cls.NOTYPE
        for member in cls:
            if member.value.extensions and suffix in member.value.extensions:
                return member
        
        if raise_err:
            raise UnsupportedFileTypeError(f"Unhandled filetype from suffix={suffix}")
        else:
            return cls.UNHANDLED
        
    @classmethod
    def from_mimetype(cls, file_path: str, raise_err: bool = False):
        
        file = Path(file_path)

        if not file.exists():
            raise FileNotFoundError(file_path)
        
        file_mimetype = guess_mime_type_from_file(str(file))

        for member in cls:
            if member.value.mime_types and file_mimetype in member.value.mime_types:
                return member
        
        if raise_err:
            raise UnsupportedFileTypeError(f"Unhandled filetype from mimetype={file_mimetype}")
        else:
            return cls.UNHANDLED
    

    # @classmethod
    # def from_content(cls, path: Path, raise_err=False):
    #     file_path = Path(path)
    #     file_type = get_file_type(file_path)['f_type']
    #     # print(file_type)
    #     return file_type #text/plain, application/json, text/xml, image/png, application/csv, image/gif, ...
    #     member = cls.UNHANDLED
    #     return member

    @classmethod
    def from_path(cls, path: Path, read_content=False, raise_err=False):
        file_path = Path(path)
        
        raise_err1 = raise_err and (not read_content)
        raise_err2 = raise_err
        
        # get member from suffix
        member1 = cls.from_suffix(file_path.suffix, raise_err=raise_err1)
        
        # if we're not checking the file content, return
        if not read_content:
            return member1

        # the file should exists for content reading
        if not file_path.exists():
            raise FileNotFoundError(f"File '{file_path}' does not exist.")
        
        # get member from content
        member2 = cls.from_mimetype(file_path, raise_err=raise_err2)
        
        # if suffix didnt give a filetype, use the one from content
        if not member1.is_true_filetype():
            return member2
        
        assert member1==member2
        
        return member1
    
    def is_true_filetype(self):
        return len(self.value.extensions) != 0
    
    def get_suffix(self):
        ext = self.value.extensions[0] if self.is_true_filetype() else ''
        return '.' + ext
    
    def is_valid_suffix(self, suffix: str, raise_err=False):
        _val = FileType.from_suffix(suffix=suffix)
        is_valid = _val == self
        if raise_err and not is_valid:
            raise MismatchedException(f"suffix ({suffix})", _val, self.value.extensions)
        return is_valid
    
    def is_valid_path(self, path: Path, raise_err=False, read_content=False):
        _val = FileType.from_path(path, read_content=read_content)
        is_valid = _val == self
        if raise_err and not is_valid:
            raise MismatchedException(f"suffix/mime-type ({path})", _val, self.value)
        return is_valid

    def is_valid_mime_type(self, path: Path, raise_err=False):
        _val = FileType.from_mimetype(path)
        is_valid = _val == self
        
        # many things can be text/plain
        if _val==FileType.TEXT and 'text/plain' in self.value.upper_mime_types:
            is_valid = True
        
        if raise_err and not is_valid:
            raise MismatchedException(f"content-type({path})", _val, self.value.mime_types)
        return is_valid

def test_file_type_parsing():
    # Test parsing of different file types
    text_path = Path('test.txt')
    csv_path = Path('data.csv')
    excel_path = Path('results.xlsx')
    json_path = Path('config.json')
    img_path = Path('picture.jpg')
    
    assert FileType.from_path(text_path) == FileType.TEXT
    assert FileType.from_path(csv_path) == FileType.CSV
    assert FileType.from_path(excel_path) == FileType.EXCEL
    assert FileType.from_path(json_path) == FileType.JSON
    assert FileType.from_path(img_path) == FileType.JPG
    assert FileType.from_path(Path('no_extension')) == FileType.NOTYPE
    assert FileType.from_path(Path('unknown.xyz')) == FileType.UNHANDLED


def test_file_type_matching():
    # Test matching of different file types
    text_path = Path('test.txt')
    csv_path = Path('data.csv')
    excel_path = Path('results.xlsx')
    json_path = Path('config.json')
    img_path = Path('picture.jpg')
    
    assert FileType.TEXT.is_valid_path(text_path)
    assert not FileType.TEXT.is_valid_path(csv_path)
    
    assert FileType.CSV.is_valid_path(csv_path)
    assert not FileType.CSV.is_valid_path(excel_path)
    
    assert FileType.EXCEL.is_valid_path(excel_path)
    assert not FileType.EXCEL.is_valid_path(json_path)
    
    assert FileType.JSON.is_valid_path(json_path)
    assert not FileType.JSON.is_valid_path(img_path)
    
    assert FileType.JPG.is_valid_path(img_path)
    assert not FileType.JPG.is_valid_path(text_path)
    
    assert FileType.NOTYPE.is_valid_path(Path('no_extension'))
    assert not FileType.NOTYPE.is_valid_path(text_path)
    
    assert FileType.UNHANDLED.is_valid_path(Path('unknown.xyz'))
    assert not FileType.UNHANDLED.is_valid_path(csv_path)

if __name__ == '__main__':
    test_file_type_parsing()
    test_file_type_matching()
    print("All tests passed!")
