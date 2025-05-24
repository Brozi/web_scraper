import requests as r
from bs4 import BeautifulSoup


URL = "https://store.steampowered.com/app/1326470/Sons_Of_The_Forest/"
response = r.get(URL, timeout = 10)
response.raise_for_status()
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
title_tag = soup.find('div', id='appHubAppName')
if title_tag is not None:
    title = title_tag.get_text(strip=True)








