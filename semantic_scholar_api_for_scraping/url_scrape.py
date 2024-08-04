import requests
from bs4 import BeautifulSoup

def scrape_html(url):
    # Fetch the HTML content of the web page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        raise Exception(f"Failed to retrieve content from {url}, status code: {response.status_code}")

# Example usage
url = 'https://example.com'
html_content = scrape_html("https://web-p-ebscohost-com.mission.idm.oclc.org/ehost/detail/detail?vid=3&sid=67bc973b-cb9e-46a5-b180-87bea2f33755%40redis&bdata=JnNpdGU9ZWhvc3QtbGl2ZQ%3d%3d#AN=178325334&db=a9h")
print(html_content.prettify())