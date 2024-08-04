import os
import requests
import json

SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTICSCHOLAR_API_KEY")


def semantic_scholar_bulk_api():
    url = "https://api.semanticscholar.org/graph/v1/paper/search/bulk"

    query_params = {"query": "AI | education", "fields": "openAccessPdf"}

    headers = {"x-api-key": SEMANTIC_SCHOLAR_API_KEY}

    response = requests.get(url=url, params=query_params, headers=headers)

    if response.status_code == 200:
        print(f"Request was successful, status code: {response.status_code}")
    else:
        print(f"Request was unsuccessful, status code: {response.status_code}")

    response_loaded=json.loads(response.content)
    
    pdf_url_list=[] 
    
    for i in response_loaded["data"]: 
        if i["openAccessPdf"] is not None: 
            pdf_url_list.append(i["openAccessPdf"]["url"])

    return response_loaded, pdf_url_list


example_response, example_pdf_url_list = semantic_scholar_bulk_api()

print(example_response)
print("-"*100) 
for url in example_pdf_url_list: 
    print(url) 
    print("-")
