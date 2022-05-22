from pykrx import stock
import time
from datetime import date, timedelta
import os


path1 = './raw_data/merge/KOSDAQ/'
path2 = './raw_data/merge/KOSPI/'


filelist1 = os.listdir(path1)
filelist2 = os.listdir(path2)


# for i, ticker in enumerate(filelist1):
#     ticker = ticker[0:6]
#     df = stock.get_market_ohlcv_by_date("20190101", "20191231", ticker)
#     time.sleep(1)
#
#     df.to_csv('./raw_data/OHLCV/' + ticker + '.csv', index=True, encoding='euc-kr')
#
#     print("OHLCV 코스닥 :", i+1, "/", len(filelist1))

for i, ticker in enumerate(filelist2):
    ticker = ticker[0:6]
    df = stock.get_market_ohlcv_by_date("20160630", "20200604", ticker)
    time.sleep(1)

    df.to_csv('./raw_data/KOSPI/' + ticker + '.csv', index=True, encoding='euc-kr')

    print("OHLCV 코스피 :", i+1, "/", len(filelist2))

# fundamental api
# for i, ticker in enumerate(filelist1):
#     ticker = ticker[0:6]
#     df = stock.get_market_fundamental_by_date("20190101", "20191231", ticker)
#     time.sleep(1)
#
#     df.to_csv('./raw_data/fundamental/' + ticker + '.csv', index=True, encoding='euc-kr')
#
#     print("fundamental 코스닥 :", i+1, "/", len(filelist1))
#
# for i, ticker in enumerate(filelist2):
#     ticker = ticker[0:6]
#     df = stock.get_market_fundamental_by_date("20190101", "20191231", ticker)
#     time.sleep(1)
#
#     df.to_csv('./raw_data/fundamental/' + ticker + '.csv', index=True, encoding='euc-kr')
#
#     print("fundamental 코스피 :", i+1, "/", len(filelist2))

print("Finish!")
