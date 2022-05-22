# 날짜를 기준으로 데이터셋 선별하기

import pandas as pd
from tqdm import tqdm
import os


PATH = "./raw_data/paper/p/"

files = os.listdir(PATH)
files = tqdm(files)

for file in files:
    stock_df = pd.read_csv(PATH + file, encoding='euc-kr')
    stock_df['date'] = pd.to_datetime(stock_df['date'], format='%Y-%m-%d')
    stock_df.set_index('date', inplace=True)

    target = stock_df['2017-01-01':'2021-06-30']

    for i in range(0, 35):
        if 'inf' in target.iloc[:, i]:
            print(file)

