import pandas as pd
import os
import numpy as np



path = "./raw_data/KOSDAQ/"

filelist = os.listdir(path)

name = []
rank = []
for i, file_name in enumerate(filelist):
    csv_path = path + file_name
    if i == 0:
        df = pd.read_csv(csv_path)
        df = df.iloc[:, [0,1]]
    else:
        basket = pd.read_csv(csv_path)
        basket = basket.iloc[:, [0,1]]
        df = pd.concat([df, basket], axis=0)

df.to_csv('./test.csv', index=False, encoding='euc-kr')

print(df)