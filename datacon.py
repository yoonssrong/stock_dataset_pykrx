import pandas as pd
import os


path1 = "./paper/OHLCV/"
path2 = "./paper/fundamental/"

filelist1 = os.listdir(path1)
filelist2 = os.listdir(path2)

for i, files in enumerate(filelist1):
    try:
        csv_data1 = pd.read_csv(path1 + files, encoding='euc-kr')
        csv_data2 = pd.read_csv(path2 + files, encoding='euc-kr')

        df = pd.merge(csv_data1, csv_data2, on="날짜")

        df.to_csv('./raw_data/paper/merge/' + files, index=False, encoding='euc-kr')
    except:
        pass
