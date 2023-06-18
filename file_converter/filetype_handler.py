from enum import Enum
from pathlib import Path


class FileType(Enum):
    NOTYPE = []
    TEXT = ['txt']
    CSV = ['csv']
    EXCEL = ['xls', 'xlsx']
    JSON = ['json']
    IMG = ['jpg', 'jpeg', 'png', 'gif']
    XML = ['xml']
    MARKDOWN = ['md']
    UNHANDLED = []
    
    @classmethod
    def from_suffix(cls, suffix: str):
        suffix = suffix.lower().lstrip('.')
        if not suffix:
            return cls.NOTYPE
        for member in cls:
            if member.value and suffix in member.value:
                return member
        return cls.UNHANDLED
    
    @classmethod
    def from_path(cls, path: Path):
        suffix = Path(path).suffix
        member = cls.from_suffix(suffix)
        return member
    
    def matches_suffix(self, path: Path):
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
    assert FileType.from_path(img_path) == FileType.IMG
    assert FileType.from_path(Path('no_extension')) == FileType.NOTYPE
    assert FileType.from_path(Path('unknown.xyz')) == FileType.UNHANDLED

def test_file_type_matching():
    # Test matching of different file types
    text_path = Path('test.txt')
    csv_path = Path('data.csv')
    excel_path = Path('results.xlsx')
    json_path = Path('config.json')
    img_path = Path('picture.jpg')
    
    assert FileType.TEXT.matches_suffix(text_path)
    assert not FileType.TEXT.matches_suffix(csv_path)
    
    assert FileType.CSV.matches_suffix(csv_path)
    assert not FileType.CSV.matches_suffix(excel_path)
    
    assert FileType.EXCEL.matches_suffix(excel_path)
    assert not FileType.EXCEL.matches_suffix(json_path)
    
    assert FileType.JSON.matches_suffix(json_path)
    assert not FileType.JSON.matches_suffix(img_path)
    
    assert FileType.IMG.matches_suffix(img_path)
    assert not FileType.IMG.matches_suffix(text_path)
    
    assert FileType.NOTYPE.matches_suffix(Path('no_extension'))
    assert not FileType.NOTYPE.matches_suffix(text_path)
    
    assert FileType.UNHANDLED.matches_suffix(Path('unknown.xyz'))
    assert not FileType.UNHANDLED.matches_suffix(csv_path)

if __name__ == '__main__':
    test_file_type_parsing()
    test_file_type_matching()
    print("All tests passed!")
