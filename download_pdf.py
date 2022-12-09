#!/usr/bin/env python
"""
Provide url and save_dir to download your pdf file. Command line usage:
python download_pdf.py [url] --save_dir(optional) [dir]
"""

import requests
import os
import argparse


def download_pdf(pdf_url, save_dir):
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


def main():
    parser = argparse.ArgumentParser(description="Provide url and save_dir to download your pdf file.")
    parser.add_argument("url", type=str, help="e.g. https://aclanthology.org/P16-1154.pdf")
    parser.add_argument("--save_dir", type=str, default='tmp', help="default is tmp")
    args = parser.parse_args()
    download_pdf(args.url, args.save_dir)


if __name__ == "__main__":
    main()
