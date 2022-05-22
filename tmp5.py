import os
import pandas as pd
import numpy as np



df = pd.read_csv("./raw_data/paper/merge2/000040.csv", encoding='euc-kr')

def trix(df, n=18):
    EX1 = df['close'].ewm(span=n, min_periods=n).mean()
    EX2 = EX1.ewm(span=n, min_periods=n).mean()
    EX3 = EX2.ewm(span=n, min_periods=n).mean()
    i = 0
    ROC_l = [np.nan]

    print(df.index[-1])
    print(len(df)-1)

    # while i + 1 <= len(df)-1:
    #     ROC = (EX3[i + 1] - EX3[i]) / EX3[i]
    #     ROC_l.append(ROC)
    #     i = i + 1

    # Trix = pd.Series(ROC_l, name='Trix_' + str(n))
    # df = df.join(Trix)
    return df

tmp = trix(df)
# print(tmp)