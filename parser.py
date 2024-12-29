import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)
result = BeautifulSoup(response.text, "lxml")

fn1 = result.find("div", class_="w-full rounded border")

print(fn1)