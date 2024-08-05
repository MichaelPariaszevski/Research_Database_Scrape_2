# import requests
# # import PyPDF2

# url = "https://downloads.hindawi.com/journals/wcmc/2022/5503834.pdf"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
# }


# response = requests.get(url=url, headers=headers)

# print(response.status_code)

import requests

url = "https://downloads.hindawi.com/journals/wcmc/2022/5503834.pdf"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.hindawi.com/",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}


response = requests.get(url=url, headers=headers)    
response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
print(response.status_code)
