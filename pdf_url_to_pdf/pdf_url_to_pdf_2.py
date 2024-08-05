import requests

url = "https://repositorioaberto.uab.pt/bitstream/10400.2/14092/1/In%20between%20identities%20and%20hope%20in%20the%20future%20experiences%20and%20trajectories%20of%20Cigano%20secondary%20students%20SI.pdf"
r = requests.get(url, stream=True)

with open("pdf_folder", 'wb') as fd:
    for chunk in r.iter_content(chunk_size=1500):
        fd.write(chunk)
#     response=requests.get(url=url)
#     response_decoded=response.decode(encoding="utf-8")
#     fd.write(response_decoded)

url_2="https://www.journals.ac.za/index.php/sajhe/article/view/1602/1848" 

response=requests.get(url=url_2, stream=True) 

with open("pdf_folder_2", "wb") as fd: 
    for chunk in response.iter_content(chunk_size=1500): 
        fd.write(chunk)