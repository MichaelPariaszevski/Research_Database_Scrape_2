import io
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
import requests

from pypdf import PdfReader
from pypdf.errors import PdfStreamError, EmptyFileError

import ssl

context = ssl._create_unverified_context()

import sys
import os
import time

sys.path.append(os.getcwd())  # In Ubuntu, this line is necessary as well

from pdf_download_url import download_to_view


def get_pdf_from_url(url):
    """
    :param url: url to get pdf file
    :return: PdfFileReader object
    """
    remote_file = urlopen(Request(url), timeout=10).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfReader(memory_file)
    return pdf_file


def get_pdf_from_url_exception(url):
    """
    :param url: url to get pdf file
    :return: PdfFileReader object
    """
    remote_file = urlopen(Request(url), timeout=10, context=context).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfReader(memory_file)
    return pdf_file


def get_pdf_from_url_exception_2(url):
    """
    :param url: url to get pdf file
    :return: PdfFileReader object
    """
    remote_file = urlopen(
        Request(
            url=url,
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"},
        ),
        timeout=10,
    ).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfReader(memory_file)
    return pdf_file

def get_pdf_from_url_exception_3(url):
    """
    :param url: url to get pdf file
    :return: PdfFileReader object
    """
    
    request=Request(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"})
    remote_file = urlopen(url=request, timeout=(120, 25)).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfReader(memory_file)
    return pdf_file


def extract_text_from_pdf(url):
    try:
        pdf = get_pdf_from_url(url)
    except HTTPError:
        try: 
            pdf = get_pdf_from_url_exception_2(url)
        except HTTPError: 
            return None
    except URLError:
        pdf = get_pdf_from_url_exception(url)
    except PdfStreamError or EmptyFileError:
        return None

    extracted_pdf = []

    for i in range(pdf.get_num_pages()):
        page = pdf.get_page(page_number=i)
        text = page.extract_text()
        extracted_pdf.append(text)

    return extracted_pdf


# def extract_text_from_pdf_basic(url):
#     pdf = get_pdf_from_url(url)

#     extracted_pdf = []

#     for i in range(pdf.get_num_pages()):
#         page = pdf.get_page(page_number=i)
#         text = page.extract_text()
#         extracted_pdf.append(text)

#     return extracted_pdf


# example_2=extract_text_from_pdf_basic(url="https://olj.onlinelearningconsortium.org/index.php/olj/article/download/2001/948")

# print(example_2)

# example_3 = extract_text_from_pdf(
#     url="https://www.journals.ac.za/index.php/sajhe/article/download/1602/1848"
# )

# print(example_3)

# ---------------------------------------------------------------------------------------------------
download_pdf_urls, pdf_urls, merged_lists, additional = download_to_view()

for i in download_pdf_urls:
    print(i)

for url in merged_lists:
    print("-" * 100)
    print(url)
    extracted_pdf = extract_text_from_pdf(url)
    print(extracted_pdf)
    
# CHECK BROWSE.AI
