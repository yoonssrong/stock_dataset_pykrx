from pykrx import stock
import pandas as pd


def return_name(market):
    Market = []

    for ticker in market:
        Value = stock.get_market_ticker_name(ticker)
        Market.append([Value, ticker])

    df = pd.DataFrame(Market, columns=['회사명', '상장번호'])
    return df


KOSPI = stock.get_market_ticker_list(market="KOSPI")
