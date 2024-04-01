# Usage Examples

## Introduction

You can define your own converters like in [simple_converter.py](./simple_converter.py).
Then, you can choose some converter to create a CLI App like done [cli_app_example.py](./cli_app_example.py).
I've added support to add multiple files as input.

## multiple files support

At the beginning, i wanted to get a file then write another file. Then, i figures, for some convertions (like img to pdf) i may want to send multiple files as input
When the converter only need one file, it will just get the first element of the list of inputs

## folder saving support

After the multiple files support, i figure, sometimes, for some convertions like (pdf to img), i may want to save multiples files. So, i choose to give more flexibility in the options: output filepath (`-o`) and output file type (`-ot`)

### setting `-o` as a folder

You cannot set a folder without adding valid filetype. Because the output format needs to be infered somehow. So, le'ts proceed under the assmption the filetype (`-o`) has also been set

When you can set a folder as output_path then a filetype, the folder would be created and files would be set in it. How do that work ?

- when the converter do have a writer, only the filepath is used for saving.
  
- when you converter doent have a writer, the folder is send as the same time as a default filepath inside the folder. So, in the converter you can choose any option . Below, for example, i use the `output_file` for saving instead of the `output_folder`

    ```python
    class TXTToTXTConverter(BaseConverter):

        file_reader = TxtToStrReader()
        # no file writer means the converter will handle the saving

        @classmethod
        def _get_supported_input_type(cls) -> FileType:
            return FileType.TEXT

        @classmethod
        def _get_supported_output_type(cls) -> FileType:
            return FileType.TEXT

        def _convert(self, input_contents: List[str], output_file: Path, **kwargs):
            md_content = "\n".join(input_contents)
            output_file.write_text(md_content)
    ```

For example, the script below will save the file `examples/output/fileconv-output.md`

```bash
find examples/data -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output -ot md
```

### setting `-o` as a filepath

When you send an output path that have a suffix (like `myfile.txt`, not `myfile`), the filepath will be send to the converter.
The output format will be infered from the filetype (`-o`) is you set it. Or, it will be infered from the filepath suffix. If both (the suffix and the outputtype) are valid formats, they should match, or an error will be raised.

For example, the script below will save the file `output.f`

```bash
find examples -type f -name "*.txt" | xargs python examples/cli_app_example.py -o examples/output.f -ot md
```

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
