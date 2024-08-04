import os
import requests
import json

SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTICSCHOLAR_API_KEY")

def semantic_scholar_api_request():
    url = "https://api.semanticscholar.org/graph/v1/paper/search"

    query_params = {"query": "Ai in education"}

    # SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTICSCHOLAR_API_KEY")

    headers = {"x-api-key": SEMANTIC_SCHOLAR_API_KEY}

    response = requests.get(url=url, params=query_params, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        # print(response_data)
        # print("#" * 100)

        paperId_list = []
        title_list = []

        for i in response_data["data"]:
            paperId = i["paperId"]
            # print(paperId)

            title = i["title"]
            # print(title)

            # print("-" * 50)

            paperId_list.append(paperId)
            title_list.append(title)
        return paperId_list, title_list
    else:
        print(
            f"Request failed with status code: {response.status_code}, {response.text}"
        )
        return None


def semantic_scholar_batch_api():
    url = "https://api.semanticscholar.org/graph/v1/paper/batch"

    params = {"fields": "openAccessPdf"}

    paperId_list, title_list = semantic_scholar_api_request()

    json_ids = {"ids": paperId_list}
    
    # SEMANTIC_SCHOLAR_API_KEY = os.getenv("SEMANTICSCHOLAR_API_KEY")

    headers = {"x-api-key": SEMANTIC_SCHOLAR_API_KEY}

    response = requests.post(url=url, params=params, json=json_ids, headers=headers)

    # print("#" * 100)
    # print(response)
    # print("-" * 50)
    # print(type(response))

    json_response = json.dumps(response.json(), indent=2)

    # print("-" * 50)
    # print(f"json response: {json_response}")

    return json_response


def semantic_scholar_batch_parse():
    json_response = semantic_scholar_batch_api()

    json_response_dict=json.loads(json_response)

    pdf_url_list = []

    for i in json_response_dict:
        # print(i)
        if i["openAccessPdf"] is not None:
            pdf_url_list.append(i["openAccessPdf"]["url"])

    return pdf_url_list


pdf_url_list_example = semantic_scholar_batch_parse()

print("#" * 100)
print(pdf_url_list_example)
