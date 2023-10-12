import smtplib

from decouple import config

from stock_data import StockData
from news_data import NewsData

ticker = "MSFT"
company_name = "Microsoft"

price_data = StockData(ticker)
news_data = NewsData(company_name)



stock_price_change = price_data.price_change()
news_articles = news_data.get_news()

upward_trend_threshold = 0.5
downward_trend_threshold = upward_trend_threshold * -1

stock_price_percent_change = round(stock_price_change, 4) * 100 

email_message = ""

def articles():
    global email_message
    if len(news_articles) > 3:
        recent_articles = news_articles[:3]

        for article in recent_articles:
            email_message += f"{article['title']}\nBy: {article['author']}\n\nWebsite:{article['url']} \n\n"
        
    else:
        recent_articles = news_articles[:]
        
        for article in recent_articles:
            email_message += f"{article['title']}\nBy: {article['author']}\nWebsite:{article['url']} \n\n\n"

def price_check():
    
    if stock_price_percent_change >= upward_trend_threshold:
        articles()
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = config("SENDER_EMAIL") , password = config("APP_PASSWORD"))
            connection.sendmail(
                from_addr= config("SENDER_EMAIL"),
                to_addrs= config("RECEIVER_EMAIL"),
                msg = f"Subject:{company_name} stock price increased in value\n\n{email_message}"
            )
            
    elif stock_price_percent_change <= downward_trend_threshold:
        articles()
        with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
            connection.starttls()
            connection.login(user = config("SENDER_EMAIL") , password = config("APP_PASSWORD"))
            connection.sendmail(
                from_addr= config("SENDER_EMAIL"),
                to_addrs= config("RECEIVER_EMAIL"),
                msg = f"Subject:{company_name} Ticker: {ticker} stock price decreased.\n\n{email_message}"
            )

price_check()        
