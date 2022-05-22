from pykrx import stock
import time
from datetime import date, timedelta




sdate = "2019-09-01"  # start 날짜
edate = "2019-09-19"  # end 날짜

d1 = date(int(sdate.split('-')[0]), int(sdate.split('-')[1]), int(sdate.split('-')[2]))
d2 = date(int(edate.split('-')[0]), int(edate.split('-')[1]), int(edate.split('-')[2]))
delta = d2 - d1

datelist = []

for i in range(delta.days + 1):
    # print(d1 + timedelta(days=i))
    strdate = d1 + timedelta(days=i)
    datelist.append(strdate)

# print(datelist)

for i in datelist:
    i = i.strftime("%Y%m%d")
    df = stock.get_shorting_volume_top50(i, market="코스닥")
    print(i)
    print(df.head())

    # # 거래일 아닌 날은 패스하고 거래일 데이터만 저장
    # if len(df) is 0:
    #     pass
    # else :
    #     # df.to_csv("./raw_data/KOSDAQ/shorting_top50_%s.csv" % i, index=True, encoding="utf-8-sig")
    #     df.to_csv("./shorting_test.csv" % i, index=True, encoding="utf-8-sig")

    time.sleep(1)
