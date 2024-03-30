#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Hermann Agossou"

import img2pdf

# pillow=10.2.0
from PIL import Image


def convert_to_pdf(input_files, output_path, backend="pillow"):
    if backend == "pillow":
        # Create a list of all the input images and convert them to RGB
        images = [Image.open(file).convert("RGB") for file in input_files]

        # Save the PDF file
        images[0].save(output_path, save_all=True, append_images=images[1:])
    elif backend == "img2pdf":
        # Convert images to PDF using img2pdf
        with open(output_path, "wb") as f:
            f.write(img2pdf.convert(input_files))
    else:
        raise ValueError("Invalid backend. Choose either 'pillow' or 'img2pdf'")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Convert images to PDF using PIL")
    parser.add_argument("input", nargs="+", help="Input image files")
    parser.add_argument("-o", "--output", required=True, help="Output PDF file")
    args = parser.parse_args()

    if args.input and args.output:
        convert_to_pdf(args.input, args.output)
