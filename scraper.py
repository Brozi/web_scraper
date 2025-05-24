import requests as r
from bs4 import BeautifulSoup
import csv
while True:
        url = input("Wpisz URL produktu w sklepie Steam, którego dane chcesz ściągnać: ").strip()
        if (url == "") or ("https://" not in url) or ("store.steampowered.com/app" not in url):
            print("\nPamiętaj o poprawnym adresie URL! Nie może być pusty, "
                  "musi pochodzić ze sklepu Steam, oraz musi zaczynać się od 'https://'\n")
        else:
            break
#print(f"Próbuję ściągnąć dane z {url}")
#url = "https://store.steampowered.com/app/1326470/Sons_Of_The_Forest/"
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/136.0.0.0 Safari/537.36"
}

game_info = {
    "Title" : "",
    "Price" : "",
    "Release date" : "",
    "Reviews" : "",
}

def none_check(element_tag):
    element = "N/A"
    if element_tag is not None:
        element = element_tag.get_text(strip=True)
    else:
        print(f"Warning: Element {element_tag} not found")
    return element

response = r.get(url, headers=user_agent, timeout = 10)
response.raise_for_status()

html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')

title_tag = soup.find('div', id='appHubAppName')
price_tag = soup.find('div', class_="game_purchase_price price")
release_tag = soup.find('div', class_="date")
reviews_tag = soup.find('span', class_="game_review_summary")
developers_tag = soup.find('div', id="developers_list")

element_tags = [title_tag, price_tag, release_tag, reviews_tag, developers_tag]
game = []

for entry in element_tags:
    game.append(none_check(entry))
print(game)





