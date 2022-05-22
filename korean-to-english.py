import pandas as pd
import os
from tqdm import tqdm

PATH = './raw_data/paper/merge/'
SAVEPATH = './raw_data/paper/merge2/'

files = os.listdir(PATH)
files = tqdm(files)

for file in files:
    df = pd.read_csv(PATH + file, encoding='euc-kr')

    # df.drop(['DIV', 'EPS', 'BPS'], axis=1, inplace=True)
    df.rename({'날짜':'date', '시가':'open', '고가':'high', '저가':'low', '종가':'close', '거래량':'volume'}, axis='columns', inplace=True)

    df.to_csv(SAVEPATH + file, index=False, encoding='euc-kr')
