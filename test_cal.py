import os
from ft_ti import *


PATH = './raw_data/OHLCV/'
files = os.listdir(PATH)

for file in files:
    stock_df = pd.read_csv(PATH + file, encoding='euc-kr')
    stock_df.set_index('날짜', inplace=True)

    stock_df = calMA(stock_df)
    print(stock_df)
