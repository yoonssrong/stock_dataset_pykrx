import os
from tqdm import tqdm
from ft_ti import *

PATH = './raw_data/tmp/'
savePATH = './raw_data/tmp/'

files = os.listdir(PATH)
files = tqdm(files)

for file in files:
    stock_df = pd.read_csv(PATH + file, encoding='euc-kr')
    stock_df.set_index('date', inplace=True)

    # 테크니컬 인디케이터 계산
    stock_df = calMA(stock_df)
    stock_df = calMACD(stock_df)
    stock_df = calRSI(stock_df)
    stock_df = calBol(stock_df)
    stock_df = calStochastic(stock_df)

    # 저장
    if not os.path.exists(savePATH):
        os.mkdir(savePATH)
    stock_df.to_csv(savePATH + file, index=True, encoding='euc-kr')

print('Finish!')
