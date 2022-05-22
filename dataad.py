import pandas as pd
import os


path = "./raw_data/종목별 공매도 거래 현황/KOSPI/"
filelist = os.listdir(path)

output = pd.DataFrame(columns=['날짜', '거래량', '비중'])

df1 = pd.DataFrame(columns=['날짜', '티커', '종목명', '수량', '거래량', '비중'])

for i, files in enumerate(filelist):
    csv_file = pd.read_csv(path + files, encoding='euc-kr')
    csv_file['날짜'] = files[0:8]
    df1 = pd.concat([df1, csv_file], ignore_index=True, sort=True)

df2 = pd.DataFrame(df1, columns=['날짜', '티커', '종목명', '수량', '거래량', '비중'])

csv_file = pd.read_csv(path + filelist[0], encoding='euc-kr')
codeno = csv_file.loc[:, '티커']
codeno = codeno.tolist()

for i, num in enumerate(codeno):
    df3 = df2[df2['티커'].isin([num])]
    df3.to_csv('./raw_data/종목별 공매도 거래 현황/adj/KOSPI_2/' + num + '.csv', index=False, encoding='euc-kr')

