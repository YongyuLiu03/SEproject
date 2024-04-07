import os
import json
import requests
from bs4 import BeautifulSoup, Tag

import undetected_chromedriver as webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--use_subprocess")


USERNAME = "yyklc"
PASSWORD = "030302_LiuYongyu"

proxy = 'http://{}:{}@unblock.oxylabs.io:60000'.format(USERNAME, PASSWORD)

proxies = {
    'http': proxy,
    'https': proxy
}

chrome_options.add_argument(f"--proxy-server={proxies}")


# curl 'https://sandbox.oxylabs.io/products/' -U 'yyklc:030302_LiuYongyu' -x 'unblock.oxylabs.io:60000' -H 'x-oxylabs-geo-location: United States' -k 

page = "https://sis.nyu.edu/psc/csprod/EMPLOYEE/SA/c/NYU_SR.NYU_CLS_SRCH.GBL"

response = requests.get(page, proxies=proxies, verify=False)

print(response.status_code)
content = response.content


# headless=False

browser = webdriver.Chrome(options=chrome_options)


browser.get(page)

browser.save_screenshot("screenshot.png")


soup = BeautifulSoup(response.text, "html.parser")

print(soup.body)