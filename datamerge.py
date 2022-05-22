import pandas as pd
import os
from datetime import date, timedelta


path1 = "./raw_data/merge/KOSPI/"
path2 = "./raw_data/temp/OHLCV/"
path3 = "./raw_data/temp/fundamental/"

filelist1 = os.listdir(path1)
filelist2 = os.listdir(path2)
filelist3 = os.listdir(path3)

# 일단 날짜 형식 변경
# for i, files in enumerate(filelist2):
#     try:
#         df1 = pd.read_csv(path2 + files, encoding='euc-kr')
#         strdate = df1.loc[:, '날짜'].tolist()
#
#         basket = []
#
#         for j, sdate in enumerate(strdate):
#             day = date(int(sdate.split('-')[0]), int(sdate.split('-')[1]), int(sdate.split('-')[2]))
#             day = day.strftime("%Y%m%d")
#             basket.append(day)
#
#         del df1['날짜']
#         df1['날짜'] = basket
#
#         df1.to_csv('D:/project/pykrx-master/raw_data/temp/OHLCV/'+ files, index=False, encoding='euc-kr')
#         print(i)
#     except:
#         pass

for i, files in enumerate(filelist1):
    try:
        df1 = pd.read_csv(path1 + files, encoding='euc-kr')
        df2 = pd.read_csv(path2 + files, encoding='euc-kr')
        df3 = pd.read_csv(path3 + files, encoding='euc-kr')

        del df1['수량']
        del df2['거래량']

        df = pd.merge(df1, df2, on="날짜")
        df = pd.merge(df, df3, on="날짜")

        df.to_csv('./raw_data/merge2/KOSPI/' + files, index=False, encoding='euc-kr')
    except:
        print(i)
        pass
