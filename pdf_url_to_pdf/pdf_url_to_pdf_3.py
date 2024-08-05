import io
from urllib.request import Request, urlopen 
import requests

from pypdf import PdfReader

import ssl
context = ssl._create_unverified_context()

def get_pdf_from_url(url):
        """
        :param url: url to get pdf file
        :return: PdfFileReader object
        """
        remote_file = urlopen(Request(url)).read()
        memory_file = io.BytesIO(remote_file)
        pdf_file = PdfReader(memory_file)
        return pdf_file

def extract_text_from_pdf(url): 
    pdf=get_pdf_from_url(url)
    
    extracted_pdf=[]
    
    for i in range(pdf.get_num_pages()):
        page=pdf.get_page(page_number=i) 
        text=page.extract_text()
        extracted_pdf.append(text)
    
    return extracted_pdf

# example=extract_text_from_pdf(url="https://www.journals.ac.za/index.php/sajhe/article/view/1602/1848")

# print(example)

example_2=extract_text_from_pdf(url="https://olj.onlinelearningconsortium.org/index.php/olj/article/download/2001/948") 

print(example_2)

# print(requests.get(url="https://www.journals.ac.za/index.php/sajhe/article/view/1602/1848").content.decode())

# print(requests.get(url="https://ojs.literacyinstitute.org/index.php/ijqr/article/view/980/423"))