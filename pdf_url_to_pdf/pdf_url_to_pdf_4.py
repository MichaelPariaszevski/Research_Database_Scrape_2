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
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
            },
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

    request = Request(
        url=url,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        },
    )
    remote_file = urlopen(url=request, timeout=(120, 25)).read()
    memory_file = io.BytesIO(remote_file)
    pdf_file = PdfReader(memory_file)
    return pdf_file

def get_pdf_from_url_exception_4(url):
    """
    :param url: url to get pdf file
    :return: PdfFileReader object
    """

    request = Request(
        url=url,
        headers={
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
        },
    )
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
        except HTTPError as error:
            return error
    except URLError:
        try: 
            pdf = get_pdf_from_url_exception(url)
        except URLError as error_2: 
            return error_2
    except TimeoutError: 
        try: 
            pdf=get_pdf_from_url_exception_4(url)
        except TimeoutError as error_3: 
            return error_3
    except PdfStreamError as error_4:
        return error_4
    except EmptyFileError as error_5:
        return error_5
    except TypeError as error_6: 
        return error_6

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
for i in range(3): 
    try: 
        download_pdf_urls, pdf_urls, merged_lists, additional = download_to_view()
    except KeyError as error:
        time.sleep(3) 
        print(error) 
        continue

split_lists=[merged_lists[x: x+10] for x in range(0, len(merged_lists), 10)]

# for i in download_pdf_urls:
#     print(i)

# for url in merged_lists:
#     print("-" * 100)
#     print(url)
#     extracted_pdf = extract_text_from_pdf(url)
#     print(extracted_pdf)

# CHECK BROWSE.AI

# EmptyFileError_url = "https://jurnal.untan.ac.id/index.php/jvip/article/download/48669/pdf"

for list in split_lists:
    for url in list:
        print("-" * 100)
        print(url)
        try: 
            extracted_pdf = extract_text_from_pdf(url)
        except EmptyFileError as error: 
            # if requests.get(url).content.decode()=="": 
            print(error)
            continue
        except PdfStreamError as error_2: 
            print(error_2) 
            continue
        except TypeError as error_3: 
            print(error_3) 
            continue
        except TimeoutError as error_4: 
            print(error_4) 
            continue
        print(extracted_pdf)

# for url in split_lists[20]:
#     print("-" * 100)
#     print(url)
#     try: 
#         extracted_pdf = extract_text_from_pdf(url)
#     except EmptyFileError as error: 
#         print(error)
#         continue
#     except PdfStreamError as error_2: 
#         print(error_2) 
#         continue
#     except TypeError as error_3: 
#         print(error_3) 
#         continue
#     except TimeoutError as error_4: 
#         print(error_4) 
#         continue
#     print(extracted_pdf)

