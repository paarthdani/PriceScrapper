import requests
from bs4 import BeautifulSoup

URL = "https://prsundar.blogspot.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup)

results = soup.find(id="Blog1")
job_elements = results.find_all("h3", class_="post-title entry-title item-title")

print(job_elements)





