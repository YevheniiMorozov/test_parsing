from bs4 import BeautifulSoup
import requests

# Для записи хтмл файла сайта

url = "https://dou.ua/calendar/tags/Python/?from=evquick"

headers = {
    # Чтобы показать сайту что ты не бот
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text

# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)
# Используем запись сайта шоб все работало
# with open("index.html", "r", encoding="utf-8") as file:
#     src = file.read()

soup = BeautifulSoup(src, "lxml")
# заголовки событий
all_events = soup.find_all(class_="title")
try:
    for event in all_events:
        event_text = event.text.strip()
        event_url = event.find("a").get("href")

        print(event_url, event_text)
except:
    None