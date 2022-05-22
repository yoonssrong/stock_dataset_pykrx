# kospi200 종목 데이터셋 선별하기

import pandas as pd
from tqdm import tqdm
import os, shutil


RAWPATH = "../rltrader-master/data/c(cur2)/"
SAVEPATH = "../rltrader-master/data/c/"

kospi200list = pd.read_csv("../rltrader-master/data/kospi200.csv", encoding='utf-8')

kospi200list['code'] = [i.replace('A', '') for i in kospi200list['code']]
kospi200list = list(kospi200list['code'])
print(kospi200list)

files = os.listdir(RAWPATH)
files = tqdm(files)

for file in files:
    target = file[0:6]
    if target in kospi200list:
        shutil.copyfile(RAWPATH + file, SAVEPATH + file)
