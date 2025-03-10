# services/news_service.py
import requests
from config.settings import Config


class NewsService:
    def __init__(self):
        self.api_key = Config.NEWS_API_KEY
        self.base_url = "https://newsapi.org/v2/top-headlines"

    def get_latest_news(self):
        try:
            params = {"country": "us", "apiKey": self.api_key}
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                articles = data["articles"][:5]
                news_summary = ""
                for i, article in enumerate(articles, 1):
                    news_summary += (
                        f"{i}. {article['title']} - {article['source']['name']}\n"
                    )
                return news_summary
            else:
                return "Sorry, I couldn't fetch the news."
        except Exception as e:
            return f"Error getting news: {str(e)}"
