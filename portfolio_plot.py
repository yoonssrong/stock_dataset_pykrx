from datetime import datetime   # 패키지 - 모듈 (이름 같음)
import pandas as pd   # csv file read
import matplotlib.pyplot as plt   # 시계열 시각화


PATH = './output/'

df = pd.read_csv(PATH + "portfolio_plot.csv")
print(df.head(5))


fig = plt.figure(figsize = (12, 4))
chart = fig.add_subplot(1,1,1)

chart.plot(df['DQN'], color='red', label='DQN')
chart.plot(df['A2C'], color='blue', label='A2C')
chart.plot(df['A3C'], color='green', label='A3C')
chart.plot(df['kospi'], color='gray', label='kospi')
chart.plot(df['kospi200'], color='tan', label='kospi200')


plt.xlabel('Trading Day')
plt.ylabel('return')
plt.legend(loc='best')
plt.show()
