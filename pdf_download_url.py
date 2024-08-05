# import requests

# response=requests.post(url="https://olj.onlinelearningconsortium.org/index.php/olj/article/download/2001/948")

# print(response)

from semantic_scholar_api_for_scraping.semantic_scholar_api_bulk import (
    semantic_scholar_bulk_api,
)


def download_to_view():
    response_loaded, pdf_url_list, status_code = semantic_scholar_bulk_api()

    additional = {"response_loaded": response_loaded, "status_code": status_code}

    download_pdf_urls = []
    pdf_urls = []

    for i in pdf_url_list:
        if "download" in i:
            download_pdf_urls.append(i)
        elif "download" not in i:
            pdf_urls.append(i)

    # merged_lists = pdf_urls.extend(download_pdf_urls)

    return download_pdf_urls, pdf_urls, download_pdf_urls+pdf_urls, additional


# example_download_pdf_urls = download_to_view()

# for url in example_download_pdf_urls:
#     print(url)
#     print("-" * 50)


def replace_download_view():
    download_pdf_urls, pdf_urls, merged_lists, additional = download_to_view()

    view_pdf_urls = []

    for i in download_pdf_urls:
        view_url = i.replace("download", "view")
        view_pdf_urls.append(view_url)

    return view_pdf_urls, pdf_urls, merged_lists, additional


example_view_pdf_urls, example_pdf_urls, example_merged_lists, example_additional = replace_download_view()

for url in example_view_pdf_urls:
    print(url)
    print("-" * 50)

print("#" * 100)

for url_2 in example_pdf_urls:
    print(url_2)
    print("-" * 50)

print("#" * 100)
print(example_additional["status_code"])
