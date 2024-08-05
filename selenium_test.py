from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
 
# The place we will direct our WebDriver to
url = 'https://downloads.hindawi.com/journals/wcmc/2022/5503834.pdf'

# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome()

# Directing the driver to the defined url
driver.get(url)

time.sleep(10000)


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()))

# selenium 3
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=Service('/usr/local/bin/chromedriver'))
# driver.maximize_window()
# driver.get('https://stackoverflow.com/questions/68543285/chrome-browser-closes-immediately-after-loading-from-selenium')