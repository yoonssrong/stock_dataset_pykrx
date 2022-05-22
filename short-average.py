import os
import pandas as pd
import numpy as np

path = './raw_data/종목별 공매도 거래 현황/KOSPI/'

files = os.listdir(path)
means = []

for file in files[49:102]:
    csv_file = pd.read_csv(path + file, encoding='euc-kr')

    means.append(np.mean(csv_file['비중']))

print(np.mean(means))