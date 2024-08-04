import requests
from bs4 import BeautifulSoup
import os 

USERNAME=os.getenv("LOGIN_USERNAME") 
PASSWORD=os.getenv("LOGIN_PASSWORD")

def scrape_html_shibboleth(url, login_url, username, password):
    # Create a session
    session = requests.Session()
    
    # Perform the login
    login_payload = {
        'username': username,
        'password': password
    }
    login_response = session.post(login_url, data=login_payload)
    
    # Check if the login was successful
    if login_response.status_code == 200:
        # Fetch the HTML content of the target web page
        print(login_response.content)
        print("-"*100)
        print("Login was successful")
        response = session.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            raise Exception(f"Failed to retrieve content from {url}, status code: {response.status_code}")
    else:
        raise Exception(f"Failed to login, status code: {login_response.status_code}")

# Example usage
login_url = 'https://login-ebsco-com.mission.idm.oclc.org/?custId=s8431115&groupId=main&profId=ehost&requestIdentifier=bb10045f-5459-4a55-9f7e-8ea59da58627&acrValues=useronly&ui_locales=en&redirect_uri=https://logon.ebsco.zone/api/dispatcher/continue/prompted?state=OWMzYjYyMDNhMWU3NGMyNjljN2Y0NzJlOWUzOTAyYWQ='
url = 'https://web-p-ebscohost-com.mission.idm.oclc.org/ehost/resultsadvanced?vid=2&sid=5dc0e4f3-6501-4b2a-affb-e8bbe800b343%40redis&bquery=AI&bdata=JmRiPWE5aCZjbGkwPUZUJmNsdjA9WSZ0eXBlPTEmc2VhcmNoTW9kZT1BbmQmc2l0ZT1laG9zdC1saXZl'
username = USERNAME
password = PASSWORD
html_content = scrape_html_shibboleth(url, login_url, username, password)
print(html_content.prettify())