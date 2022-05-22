import pandas as pd
import numpy as np

def weighted_mean(weight_array):
    def inner(x):
        return (weight_array * x).mean()
    return inner

def calMA(df):
    # SMA
    df['sma5'] = df['close'].rolling(5).mean()
    df['sma20'] = df['close'].rolling(20).mean()
    df['sma100'] = df['close'].rolling(100).mean()
    df['sma200'] = df['close'].rolling(200).mean()

    # EMA
    df['ema5'] = df['close'].ewm(5).mean()
    df['ema20'] = df['close'].ewm(20).mean()
    df['ema100'] = df['close'].ewm(100).mean()
    df['ema200'] = df['close'].ewm(200).mean()

    # WMA
    weights = np.arange(1, 6)
    df['wma5'] = df['close'].rolling(5).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw=True)
    weights = np.arange(1, 21)
    df['wma20'] = df['close'].rolling(20).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw=True)
    weights = np.arange(1, 101)
    df['wma100'] = df['close'].rolling(100).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw=True)
    weights = np.arange(1, 201)
    df['wma200'] = df['close'].rolling(200).apply(lambda prices: np.dot(prices, weights) / weights.sum(), raw=True)
    return df

def calMACD(df, short=12, long=26, signal=9):
    df['MACD'] = df['close'].ewm(span=short, min_periods=long-1, adjust=False).mean() - df['close'].ewm(span=long, min_periods=long-1, adjust=False).mean()
    df['MACD_Signal'] = df['MACD'].ewm(span=signal, min_periods=signal-1, adjust=False).mean()
    df['MACD_OSC'] = df['MACD'] - df['MACD_Signal']
    return df

def calRSI(df, period=14):
    date_index = df.index.astype('str')
    U = np.where(df.diff(1)['close'] > 0, df.diff(1)['close'], 0)  # df.diff를 통해 (기준일 종가 - 기준일 전일 종가)를 계산하여 0보다 크면 증가분을 감소했으면 0을 넣어줌
    D = np.where(df.diff(1)['close'] < 0, df.diff(1)['close'] *(-1), 0)  # df.diff를 통해 (기준일 종가 -기준일 전일 종가)를 계산하여 0보다 작으면 감소분을 증가했으면 0을 넣어줌
    AU = pd.DataFrame(U, index=date_index).rolling(window=period).mean()  # AU, period=14일 동안의 U의 평균
    AD = pd.DataFrame(D, index=date_index).rolling(window=period).mean()  # AD, period=14일 동안의 D의 평균
    RSI = AU / (AD+AU) * 100  # 0부터 1로 표현되는 RSI에 100을 곱함

    df.insert(len(df.columns), "RSI", RSI)  # 원래 dataframe에 'RSI'컬럼을 추가
    df.insert(len(df.columns), "RSI Signal",
    df['RSI'].rolling(window=9).mean())  # RSI Signal(RSI 이동평균)을 구해서 추가함
    return df

def calBol(df):
    df['bol_mid'] = df['close'].rolling(window=20).mean()  # 20일 이동평균값
    df['bol_upper'] = df['bol_mid'] + 2 * df['close'].rolling(window=20).std()  # 볼린저 상단 밴드
    df['bol_down'] = df['bol_mid'] - 2 * df['close'].rolling(window=20).std()  # 볼린저 하단 밴드
    df['bol_b'] = (df['close'] - df['bol_down']) / (df['bol_upper'] - df['bol_down'])
    df['bol_w'] = (df['bol_upper'] - df['bol_down']) / df['bol_mid']
    return df

def calStochastic(df):
    # Fast %K = ((현재가 - n기간 중 최저가) / (n기간 중 최고가 - n기간 중 최저가)) * 100
    fast_k = ((df['close'] - df['low'].rolling(5).min()) / (df['high'].rolling(5).max() - df['low'].rolling(5).min())) * 100
    # Slow %K = Fast %K의 m기간 이동평균(SMA)
    slow_k = fast_k.rolling(3).mean()
    # Slow %D = Slow %K의 t기간 이동평균(SMA)
    slow_d = slow_k.rolling(3).mean()

    df['fast_k'] = fast_k
    df['slow_k'] = slow_k
    df['slow_d'] = slow_d
    return df

def calDMI(df, n_days1=5, n_days2=10):
    std_close = df['close'].rolling(min_periods=n_days1, window=n_days1, center=False).std()
    std_ma = std_close.rolling(min_periods=n_days2, window=n_days2, center=False).mean()
    vi = std_close / std_ma
    td = 14 // vi
    td[np.isnan(td)] = 5
    td[td < 5] = 5 ; td[td > 30] = 30

    delta = df['close'].diff()

    dUp, dDown = delta.copy(), delta.copy()
    dUp[dUp < 0] = 0
    dDown[dDown > 0] = 0

    dUp[np.isnan(dUp)] = 0
    dDown[np.isnan(dDown)] = 0

    RolUp, RolDown = np.zeros(len(df)), np.zeros(len(df))
    for i in range(1, len(df)):
        RolUp[i] = sum(dUp[int(max(i-td[i]+1, 0)):(i+1)])
        RolDown[i] = sum(dDown.abs()[int(max(i-td[i]+1, 0)):(i+1)])

    df['DMI'] = RolUp / (RolUp + RolDown) * 100
    return df


def trix(df, n=18):
    EX1 = df['close'].ewm(span=n, min_periods=n).mean()
    EX2 = EX1.ewm(span=n, min_periods=n).mean()
    EX3 = EX2.ewm(span=n, min_periods=n).mean()
    i = 0
    ROC_l = [np.nan]
    while i + 1 <= len(df)-1:
        ROC = (EX3[i + 1] - EX3[i]) / EX3[i]
        ROC_l.append(ROC)
        i = i + 1

    Trix = pd.Series(ROC_l, name='Trix_' + str(n))
    df = df.join(Trix)
    return df
