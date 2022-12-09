#!/usr/bin/env python
"""
Provide url and save_dir to download your pdf file, and crop it automatically. Command line usage:
python download_pdf.py [url] --save_dir(optional) [dir] --crop(optional) [list]
requirements: https://pypi.org/project/PyPDF2/
```pip install PyPDF2```
example:
```python download_and_crop.py.py https://arxiv.org/pdf/2004.13639.pdf ```
"""

import requests
import os
import argparse
from PyPDF2 import PdfWriter, PdfReader


def download_pdf(pdf_url, save_dir, margins):
    """
    Provide url and save_dir to download your pdf file.
    :param pdf_url: e.g. "https://aclanthology.org/P16-1154.pdf"
    :param save_dir: default is "tmp"
    """
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print("Directory '%s' created" % save_dir)

    pdf_path = os.path.join(save_dir, pdf_url.split("/")[-1])

    if not os.path.exists(pdf_path):
        response = requests.get(pdf_url)
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print("'%s' saved" % pdf_path)
    else:
        print("'%s' already exist" % pdf_path)
    
    if margins:
        crop_pdf(pdf_path, margins)

        
def crop_pdf(pdf_path, margins):
    reader = PdfReader(pdf_path)
    writer = PdfWriter()

    num_pages = len(reader.pages)
    print("The document has %s pages." % num_pages)


    for i in range(num_pages):
        page = reader.pages[i]
        page.mediaBox.upper_right = (page.mediabox.right - margins[0], page.mediabox.top - margins[1])
        page.mediaBox.lower_left = (page.mediabox.left + margins[0], page.mediabox.bottom + margins[1])

        writer.add_page(page)

    new_path = pdf_path[:-4]+"-new"+".pdf"
    with open(new_path, "wb") as f:
        writer.write(f)
    print("The file cropped with {} margins".format(str(margins)))

    
    

def main():
    parser = argparse.ArgumentParser(description="Provide url and save_dir to download your pdf file.")
    parser.add_argument("url", type=str, help="e.g. https://aclanthology.org/P16-1154.pdf")
    parser.add_argument("--save_dir", type=str, default='tmp', help="default is tmp")
    parser.add_argument("--crop", type=int, default=[60, 60*29.7/21], nargs='+', help="margins: right, top. Note that the A4 size is 21cm*29.7cm.")
    args = parser.parse_args()
    download_pdf(args.url, args.save_dir, args.crop)


if __name__ == "__main__":
    main()
