import yfinance as yf


class CallAPI(object):

    def __init__(self, ticker):

        self.ticker = yf.Ticker(ticker)

    def get_history(self):

        return self.ticker.history(period='max')

