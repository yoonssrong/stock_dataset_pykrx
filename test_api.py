from pykrx import stock
from pykrx.website.krx.bond.wrap import KrxBond
import time, os
from datetime import date, timedelta
import pandas_datareader.data as web
import datetime

# tickers = stock.get_market_ticker_list("20210105")
# print(tickers)
# print(len(tickers))

start = datetime.datetime(2020, 8, 1)
end = datetime.datetime(2020, 12, 31)
stock_df = web.DataReader('088260.KS', "yahoo", start, end)
print(stock_df)


# df = stock.get_shorting_status_by_date("20200102", "20201116", "032620")
# print(df)

# df = stock.get_market_ohlcv_by_date("20200210", "20200213", "032620")
# print(df.head(3))

# df = stock.get_index_kospi_ohlcv_by_date("20180101", "20201116", "코스피 200", freq='d')
# df = stock.get_etf_ticker_list("20201117")
# df = stock.get_index_ticker_list("20201117", market="KOSPI")
# print(df)


# kb = KrxBond()
# df = kb.get_treasury_yields_in_kerb_market("20181230")
# # CD91 = df.loc['CD(91일)', '수익률']
# print(df)

