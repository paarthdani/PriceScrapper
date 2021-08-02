import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

print(soup)