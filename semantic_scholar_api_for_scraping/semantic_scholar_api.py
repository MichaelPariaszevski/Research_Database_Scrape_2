import os
import requests

url = "https://api.semanticscholar.org/graph/v1/paper/search"

query_params = {"query": "AI"}

SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTICSCHOLAR_API_KEY")

headers = {"x-api-key": SEMANTIC_SCHOLAR_API_KEY}

response = requests.get(url=url, params=query_params, headers=headers)

if response.status_code == 200:
    response_data = response.json()
    print(response_data)
    print("#" * 100)
    for i in response_data["data"]:
        print(i["paperId"])
        print(i["title"])
        print("-" * 50)
else:
    print(f"Request failed with status code: {response.status_code}, {response.text}")
