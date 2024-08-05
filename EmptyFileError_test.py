import requests

url = "https://jurnal.untan.ac.id/index.php/jvip/article/download/48669/pdf"

# extracted_pdf = extract_text_from_pdf(url)
# print(extracted_pdf)

response=requests.get(url)

print(response)
print(response.content.decode(encoding="utf-8"))