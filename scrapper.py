import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Wear-Your-Opinion-Printed-T-Shirt/dp/B09BZFM6SY/ref=sr_1_4_sspa?crid=3SRLZDG0M0VNR&dchild=1&keywords=code&qid=1635232842&s=apparel&sprefix=cod%2Cfashion%2C254&sr=1-4-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUkJSMEVXVzZUMzBKJmVuY3J5cHRlZElkPUEwODQxOTMwMzMxVUJVT0ZJRVc5SyZlbmNyeXB0ZWRBZElkPUEwMTc4MzAwMTJIVEJGSjhFODdXQiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# print(soup)

results = soup.find(id="Blog1")
job_elements = results.find_all("h3", class_="post-title entry-title item-title")

print(job_elements)





