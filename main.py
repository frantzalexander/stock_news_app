from twilio.rest import Client
from stock_data import StockData
from news_data import NewsData

price_data = StockData()
news_data = NewsData()

stock_price_change = price_data.price_change()
news_articles = news_data.get_news()

print(stock_price_change)
print(news_articles)


# if abs()
