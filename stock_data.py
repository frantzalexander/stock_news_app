import requests
from decouple import config

class StockData:
    def __init__(self, stock_ticker: str = "MSFT"):
        
        self.alpha_vantage_api_endpoint = "https://www.alphavantage.co/query"
        self.alpha_vantage_api_key = config("ALPHA_VANTAGE_API_KEY")
        self.stock = stock_ticker
        self.parameters = {
            "function": "TIME_SERIES_DAILY",
            "symbol": self.stock,
            "apikey": self.alpha_vantage_api_key 
        }
        self.response = requests.get(
            url = self.alpha_vantage_api_endpoint,
            params = self.parameters
        )
        self.response.raise_for_status()
        self.data = self.response.json()
        
    def price_change(self) -> float:
        self.daily_msft_stock_data = self.data["Time Series (Daily)"]
        self.daily_msft_stock_date_listing = [date for date in self.data["Time Series (Daily)"].keys()]
        self.price_listing = [float(self.daily_msft_stock_data[i]["4. close"]) for i in self.daily_msft_stock_date_listing]
        
        self.price_difference = self.price_listing[1] - self.price_listing[2]
        self.stock_price_percent_change = self.price_difference / self.price_listing[2]
        
        return self.stock_price_percent_change

