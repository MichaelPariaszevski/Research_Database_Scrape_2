import io
from urllib.request import Request, urlopen 

from pypdf import PdfReader

def get_pdf_from_url(url):
        """
        :param url: url to get pdf file
        :return: PdfFileReader object
        """
        remote_file = urlopen(Request(url)).read()
        memory_file = io.BytesIO(remote_file)
        pdf_file = PdfReader(memory_file)
        return pdf_file

# example_pdf=get_pdf_from_url("https://repositorioaberto.uab.pt/bitstream/10400.2/14092/1/In%20between%20identities%20and%20hope%20in%20the%20future%20experiences%20and%20trajectories%20of%20Cigano%20secondary%20students%20SI.pdf")

# print(example_pdf)

def extract_text_from_pdf(url): 
    pdf=get_pdf_from_url(url)
    
    extracted_pdf=[]
    
    for i in range(pdf.get_num_pages()):
        page=pdf.get_page(page_number=i) 
        text=page.extract_text()
        extracted_pdf.append(text)
    
    return extracted_pdf

example_extracted_pdf=extract_text_from_pdf(url="https://repositorioaberto.uab.pt/bitstream/10400.2/14092/1/In%20between%20identities%20and%20hope%20in%20the%20future%20experiences%20and%20trajectories%20of%20Cigano%20secondary%20students%20SI.pdf")

print(example_extracted_pdf)

example_extracted_pdf_2=extract_text_from_pdf(url="https://scholarship.law.slu.edu/cgi/viewcontent.cgi?article=1217&context=faculty")

print("#"*100) 

print(example_extracted_pdf_2)

