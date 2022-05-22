from pykrx import stock
import time
from datetime import date, timedelta
import os


savePath = './raw_data/paper/'

tickers = stock.get_market_ticker_list("20170102")
print(tickers)

# OHLCV api
# if not os.path.exists(savePath + 'OHLCV/'):
#     os.mkdir(savePath + 'OHLCV/')
# for i, ticker in enumerate(tickers):
#     df = stock.get_market_ohlcv_by_date("20160101", "20210630", ticker)
#     time.sleep(1)
#
#     df.to_csv(savePath + 'OHLCV/' + ticker + '.csv', index=True, encoding='euc-kr')
#
#     print("OHLCV 코스피 :", i+1, "/", len(tickers))

# fundamental api
if not os.path.exists(savePath + 'fundamental/'):
    os.mkdir(savePath + 'fundamental/')
for i, ticker in enumerate(tickers):
    df = stock.get_market_fundamental_by_date("20160101", "20210630", ticker)
    time.sleep(1)

    df.to_csv(savePath + 'fundamental/' + ticker + '.csv', index=True, encoding='euc-kr')

    print("fundamental 코스피 :", i+1, "/", len(tickers))

print("Finish!")
