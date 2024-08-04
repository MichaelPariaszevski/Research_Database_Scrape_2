# import requests

# response=requests.post(url="https://olj.onlinelearningconsortium.org/index.php/olj/article/download/2001/948")

# print(response)

from semantic_scholar_api_for_scraping.semantic_scholar_api_bulk import (
    semantic_scholar_bulk_api,
)


def download_to_view():
    response_loaded, pdf_url_list = semantic_scholar_bulk_api()

    download_pdf_urls = []

    for i in pdf_url_list:
        if "download" in i:
            download_pdf_urls.append(i)

    return download_pdf_urls


# example_download_pdf_urls = download_to_view()

# for url in example_download_pdf_urls:
#     print(url)
#     print("-" * 50)


def replace_download_view():
    download_pdf_urls = download_to_view()

    view_pdf_urls = []

    for i in download_pdf_urls:
        view_url=i.replace("download", "view")
        view_pdf_urls.append(view_url)

    return view_pdf_urls


example_view_pdf_urls = replace_download_view()

for url in example_view_pdf_urls:
    print(url)
    print("-" * 50)
