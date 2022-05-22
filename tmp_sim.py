import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np
from scipy.spatial.distance import *
from statsmodels.tsa.stattools import coint, adfuller, kpss
import dtw



PATH = './raw_data/'

raw = pd.read_csv(os.path.join(PATH, 'tmp_sim.csv'), index_col='date')

# 비교 기준 구간
d_start = '2021-01-10'
d_end = '2021-06-30'

df = raw[d_start:d_end]

dqn = df['DQN'].values
a2c = df['A2C'].values
a3c = df['A3C'].values
kospi200 = df['kospi200'].values

dqn_norm = (dqn - dqn.mean()) / dqn.std()
a2c_norm = (a2c - a2c.mean()) / a2c.std()
a3c_norm = (a3c - a3c.mean()) / a3c.std()
kospi200_norm = (kospi200 - kospi200.mean()) / kospi200.std()

# sim_dqn = (dqn_norm, kospi200_norm)
# sim_a2c = jaccard(a2c_norm, kospi200_norm)
# sim_a3c = jaccard(a3c_norm, kospi200_norm)
#
# print(sim_dqn, sim_a2c, sim_a3c)

# plt.plot(dqn_norm, label='dqn')
# plt.plot(a2c_norm, label='a2c')
# plt.plot(a3c_norm, label='a3c')
# plt.plot(kospi200_norm, label='kospi200')
# plt.legend()
# plt.show()



# # 1차 차분
# kospi200_diff = pd.DataFrame(kospi200).diff()[1:]
# dqn_diff = pd.DataFrame(dqn).diff()[1:]
# a2c_diff = pd.DataFrame(a2c).diff()[1:]
# a3c_diff = pd.DataFrame(a3c).diff()[1:]
#
# # 단위근 검정
# def adf_test(timeseries):
#     print("Results of Dickey-Fuller Test:")
#     dftest = adfuller(timeseries, autolag="AIC")
#     dfoutput = pd.Series( dftest[0:4],
#                          index=[ "Test Statistic", "p-value", "#Lags Used", "Number of Observations Used", ], )
#
#     for key, value in dftest[4].items():
#         dfoutput["Critical Value (%s)" % key] = value
#     print(dfoutput)
# adf_test(a3c_diff)
#
# # 공적분 검정
# _, p_value, _ = coint(dqn_diff, kospi200_diff)
# print('correlation: ', df.A3C.corr(df.kospi200))
# print('cointegration test p-value: ', p_value)



print(dtw.dtw(a3c_norm, kospi200_norm, keep_internals=True))
dtw.dtw(a3c_norm, kospi200_norm, keep_internals=True).plot(type="twoway")
