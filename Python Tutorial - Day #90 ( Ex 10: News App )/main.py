import requests

API = "" #<- Put your api key from newsapi here.
url = "https://newsapi.org/v2/top-headlines"

params = {
    "country":"us",
    "category":"Technology",
    "pageSize": 5,
}

headers = {
    "X-Api-key": API
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    articles = data["articles"]

    for i, article in enumerate(articles):
        print(f"{i}. {article['title']}")
        print(f" Source: {article['source']['name']}")
        print(f" URL: {article['url']}\n")
else:
    print("Error: ",response.status_code, response.text)
