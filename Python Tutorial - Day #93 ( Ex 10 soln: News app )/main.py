import requests
import json

API_KEY = "" #newsapi key here

topic = input("Give your topic: ")
country = input("Enter your country's code ( 2 letters ): ")
pagesize = input("Enter page size: ")

url = f"https://newsapi.org/v2/top-headlines?"

params = {
    "apiKey":API_KEY,
    "country":country,
    "category":topic,
    "pageSize":pagesize
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    articles = data["articles"]
    # print(data)

    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Description:\n {article['description']}")
        print(f"Url: {article['url']}")
