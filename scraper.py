import requests as r
from bs4 import BeautifulSoup
import csv, os
#steam search query for future development https://store.steampowered.com/search/?term=YOUR+GAME+TITLE&page=1
while True:
        url = input("Wpisz URL produktu w sklepie Steam, którego dane chcesz ściągnać: ").strip()
        if (url == "") or ("https://" not in url) or ("store.steampowered.com/app" not in url):
            print("\nPamiętaj o poprawnym adresie URL! Nie może być pusty, "
                  "musi pochodzić ze sklepu Steam, oraz musi zaczynać się od 'https://'\n")
        else:
            break

print(f"Próbuję ściągnąć dane z {url}...\n")
user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/136.0.0.0 Safari/537.36"
}

output = {
    "Title" : "N/A",
    "Price" : "N/A",
    "Release date" : "N/A",
    "Reviews" : "N/A",
    "Developer": "N/A",
}

def none_check(tag, tag_name):
    element = "N/A"
    if tag is not None:
        element = tag.get_text(strip=True)
    else:
        print(f"Warning: Element {tag_name} not found")
    return element

response = r.get(url, headers=user_agent, timeout = 10)
response.raise_for_status()

html_content = response.text
soup = BeautifulSoup(html_content, 'lxml')

title_tag = soup.find('div', id='appHubAppName')
price_tag = soup.select_one('div[class*=final_price]')
release_tag = soup.find('div', class_="date")
reviews_tag = soup.find('span', class_="game_review_summary")
developers_tag = soup.find('div', id="developers_list")

element_tags = [title_tag, price_tag, release_tag, reviews_tag, developers_tag]
keys = list(output.keys())

for i in range(len(keys)):
    key = keys[i]
    element_tag = element_tags[i]
    output[keys[i]] = none_check(element_tag,key)

counter = 1
csvfile_name = f"output_{counter}.csv"
while os.path.exists(csvfile_name):
    counter +=1
    csvfile_name = f"output_{counter}.csv"
try:
    with open(csvfile_name, mode="w",newline='',encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys, delimiter=';')

        writer.writeheader()
        writer.writerow(output)
        print(f"Zapisano wynik do pliku {csvfile_name}\n")
        for key in output.keys():
            print(key + ": " + output[key])

except IOError:
    print(f"Błąd! Nie udało się zapisać do pliku {csvfile_name}")
except Exception as e:
    print(f"Nieoczekiwany błąd podczas zapisywania: {e}")