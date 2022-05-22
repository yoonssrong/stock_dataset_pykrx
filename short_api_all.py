from pykrx import stock
import time
from datetime import date, timedelta



# 종목별 공매도 현황

# tickers_kospi = stock.get_market_ticker_list("코스피")
tickers_kospi = ['005930']

for i, code in enumerate(tickers_kospi) :
    print("코스피 :", i, "/", len(tickers_kospi))
    df = stock.get_shorting_status_by_date("20160630", "20200604", code)
    df.to_csv('./raw_data/종목별 공매도 현황/KOSPI/' + code + '.csv', index=True, encoding='euc-kr')
    time.sleep(1)


# tickers_kosdaq = stock.get_market_ticker_list("코스닥")
#
# for i, code in enumerate(tickers_kosdaq) :
#     print("코스닥 :", i, "/", len(tickers_kosdaq))
#     df = stock.get_shorting_status_by_date("20190101", "20191231", code)
#     df.to_csv('./raw_data/종목별 공매도 현황/KOSDAQ/' + code + '.csv', index=True, encoding='euc-kr')
#     time.sleep(1)



# 종목별 공매도 거래 현황

# sdate = "2016-06-30"  # start 날짜
# edate = "2020-06-04"  # end 날짜
#
# d1 = date(int(sdate.split('-')[0]), int(sdate.split('-')[1]), int(sdate.split('-')[2]))
# d2 = date(int(edate.split('-')[0]), int(edate.split('-')[1]), int(edate.split('-')[2]))
# delta = d2 - d1
#
# datelist = []
#
# for i in range(delta.days + 1):
#     # print(d1 + timedelta(days=i))
#     strdate = d1 + timedelta(days=i)
#     datelist.append(strdate)
#
# for i, d_date in enumerate(datelist):
#     d_date = d_date.strftime("%Y%m%d")
#     df = stock.get_shorting_volume_by_ticker(d_date, "코스피")
#
#     if len(df) is 0:
#         pass
#     else :
#         df.to_csv('./raw_data/종목별 공매도 거래 현황/KOSPI/' + d_date + '.csv', index=True, encoding='euc-kr')
#
#     time.sleep(1)
#     print("코스피 :", i+1, "/", len(datelist))

# for i, d_date in enumerate(datelist):
#     d_date = d_date.strftime("%Y%m%d")
#     df = stock.get_shorting_volume_by_ticker(d_date, "코스닥")
#
#     if len(df) is 0:
#         pass
#     else :
#         df.to_csv('./raw_data/종목별 공매도 거래 현황/KOSDAQ/' + d_date + '.csv', index=True, encoding='euc-kr')
#
#     time.sleep(1)
#     print("코스닥 :", i+1, "/", len(datelist))

print("Finish!")

