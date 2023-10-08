from twilio.rest import Client
from stock_data import StockData


data = StockData()

stock_price_change = data.price_change()

print(stock_price_change)

# if abs()
