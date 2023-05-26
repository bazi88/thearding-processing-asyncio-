from threading import Thread
import logging
import requests
from lxml import html

class Stock(Thread):
    def __init__(self, symbol):
        super().__init__()
        print(f"Starting to read stock {symbol}")
        self.symbol = symbol
        self.url = f'https://finance.yahoo.com/quote/{symbol}'
        self.price = None

    def run(self):
        response = requests.get(self.url , headers={'User-Agent': 'Custom'})
        if response.status_code == 200:
            tree = html.fromstring(response.text)
            price_text = tree.xpath(
                '//*[@id="quote-header-info"]/div[3]/div[1]/div[1]/fin-streamer[1]/text()')
            if price_text:
                try:
                    self.price = float(price_text[0].replace(',', ''))
                except ValueError:
                    self.price = None

    def __str__(self):
        return f'{self.symbol}\t{self.price}'

stocks = ['NVDA', 'GOOGL', 'AAPL', 'META']
threading = []

for stock in stocks:
    t = Stock(stock)
    t.start()
    threading.append(t)

for t in threading:
    t.join()
    print(t)
