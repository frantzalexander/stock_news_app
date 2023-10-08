import requests

from decouple import config

news_api_endpoint = "https://newsapi.org/v2/everything"

parameters = {
    "q": "microsoft",
    "apiKey": config("NEWS_API_KEY"),
    "sources": "bloomberg"
}

response = requests.get(
    url = news_api_endpoint,
    params= parameters
)

response.raise_for_status()

news_data = response.json()

