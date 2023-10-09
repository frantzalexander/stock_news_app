import requests

from decouple import config

class NewsData:
    def __init__(self, company_name: str = "microsoft"):
        self.company_name = company_name
        self.news_api_endpoint = "https://newsapi.org/v2/everything"

        self.parameters = {
            "q": self.company_name,
            "apiKey": config("NEWS_API_KEY"),
            "sources": "bloomberg"
        }
        
    def get_news(self):
        self.response = requests.get(
            url = self.news_api_endpoint,
            params = self.parameters
        )
        
        self.response.raise_for_status()
        self.news_data = self.response.json()
        self.news_article_data = self.news_data["articles"]

        return self.news_article_data