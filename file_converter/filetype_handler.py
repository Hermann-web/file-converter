from enum import Enum
from pathlib import Path


class FileType(Enum):
    NOTYPE = []
    TEXT = ['txt']
    CSV = ['csv']
    EXCEL = ['xls', 'xlsx']
    JSON = ['json']
    ## IMG
    JPG = ['jpg']
    JPEG = ['jpeg']
    PNG = ['png']
    GIF = ['gif']

    XML = ['xml']
    MARKDOWN = ['md']
    UNHANDLED = []
    
    @classmethod
    def from_suffix(cls, suffix: str, raise_err:bool=False):
        suffix = suffix.lower().lstrip('.')
        if not suffix:
            if raise_err:
                raise ValueError("filetype not parse from empty suffix")
            else:
                return cls.NOTYPE
        for member in cls:
            if member.value and suffix in member.value:
                return member
        
        if raise_err:
            raise ValueError(f"unhandled filetype from suffix={suffix}")
        else:
            return cls.UNHANDLED
    
    @classmethod
    def from_path(cls, path: Path, raise_err=False):
        suffix = Path(path).suffix
        member = cls.from_suffix(suffix, raise_err=raise_err)
        return member
    
    def is_true_filetype(self):
        return len(self.value) != 0
    
    def get_suffix(self):
        if not self.is_true_filetype():
            return '.'
        return '.' + self.value[0]
    
    def is_valid_suffix(self, suffix: str):
        return FileType.from_suffix(suffix=suffix) == self

    def is_valid_path(self, path: Path):
        return FileType.from_path(path) == self

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
