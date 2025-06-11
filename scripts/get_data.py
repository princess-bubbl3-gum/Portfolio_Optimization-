import yfinance as yf


def get_data(tickers, start, end):
    return yf.download(tickers, start, end, auto_adjust = False)['Adj Close']
    