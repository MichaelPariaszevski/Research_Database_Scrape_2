import io 
from urllib.request import Request, urlopen 

from pypdf import PdfReader 

from semantic_scholar_api_for_scraping.semantic_scholar_api_batch import semantic_scholar_batch_parse

def get_pdf_from_url(): 
    url_list=semantic_scholar_batch_parse()
    
    pdf_file_list=[] 
    
    for i in url_list: 
        remote_file=urlopen(Request(i)).read() 
        memory_file=io.BytesIO(remote_file) 
        pdf_file=PdfReader(memory_file) 
        pdf_file_list.append(pdf_file)
        
    return pdf_file_list

pdf_file_list_example=get_pdf_from_url() 

print(pdf_file_list_example)