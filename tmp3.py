# 일별 kospi 200 지수 수집

from pykrx import stock


savePath = './raw_data/'

index = ['1150', '1151', '1152', '1153', '1154', '1155', '1156', '1157', '1158', '1159', '1160']

# for i in index:
#     df = stock.get_index_ohlcv_by_date("20170102", "20201230", i)  # 1001:코스피, 1028:코스피200
#     df.to_csv(savePath + 'OHLCV_kospi200_{}_Train.csv'.format(i), index=True, encoding='euc-kr')

# df = stock.get_index_ohlcv_by_date("20170102", "20201230", '1001')  # 1001:코스피, 1028:코스피200
# df.to_csv(savePath + 'OHLCV_kospi200_Train.csv', index=True, encoding='euc-kr')

df = stock.get_market_ticker_list("20201230", "KOSPI200")