import requests as r
from bs4 import BeautifulSoup
import csv
URL = "https://store.steampowered.com/app/1326470/Sons_Of_The_Forest/"
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/136.0.0.0 Safari/537.36"
}
response = r.get(URL, headers=user_agent, timeout = 10)
response.raise_for_status()
html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')
title_tag = soup.find('div', id='appHubAppName')
title = "N/A"
if title_tag is not None:
    title = title_tag.get_text(strip=True)
else:
    print("Warning: Element not found")

price_tag = soup.find('div', class_="game_purchase_price price")
price = "N/A"
if price_tag is not None:
    price = price_tag.get_text(strip=True)
else:
    print("Warning: Element not found")

release_tag = soup.find('div', class_="date")
release = "N/A"
if release_tag is not None:
    release = release_tag.get_text(strip=True)
else:
    print("Warning: Element not found")

reviews_tag = soup.find('span', class_="game_review_summary")
reviews = "N/A"
if reviews_tag is not None:
    reviews = reviews_tag.get_text(strip=True)
else:
    print("Warning: Element not found")

game_info = {
    "Title" : title,
    "Price" : price,
    "Release date" : release,
    "Reviews" : reviews,
}

print(game_info)





