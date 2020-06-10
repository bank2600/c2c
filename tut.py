import requests
import datetime
from bs4 import BeautifulSoup

url = 'http://www.coasttocoastam.com'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, 'lxml')
for div in soup.find_all('div', class_='description'):
    print(div.text)(time.strftime("%d/%m/%Y")
