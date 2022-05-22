import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns


pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


data_path = 'C:/Users/YSS/Desktop/'

df_price = pd.read_csv(os.path.join(data_path, '005930.csv'), encoding='euc-kr')

pd.to_datetime(df_price['날짜'], format='%Y%m%d')

df_price['날짜'] = pd.to_datetime(df_price['날짜'], format='%Y%m%d')

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scale_cols = ['거래량', '비중', '공매도', '잔고', '공매도금액', '잔고금액', '시가', '고가', '저가', '종가', '등락']
df_scaled = scaler.fit_transform(df_price[scale_cols])
# df_scaled = df_price[scale_cols]

df_scaled = pd.DataFrame(df_scaled)
df_scaled.columns = scale_cols

TEST_SIZE = 200

train = df_scaled[:-TEST_SIZE]
test = df_scaled[-TEST_SIZE:]


def make_dataset(data, label, window_size=20):
    feature_list = []
    label_list = []
    for i in range(len(data) - window_size):
        feature_list.append(np.array(data.iloc[i:i+window_size]))
        label_list.append(np.array(label.iloc[i+window_size]))
    return np.array(feature_list), np.array(label_list)

feature_cols = ['거래량', '비중', '공매도', '잔고', '공매도금액', '잔고금액', '시가', '고가', '저가']
label_cols = ['등락']

train_feature = train[feature_cols]
train_label = train[label_cols]

# train dataset
train_feature, train_label = make_dataset(train_feature, train_label, 20)

# train, validation set 생성
from sklearn.model_selection import train_test_split

x_train, x_valid, y_train, y_valid = train_test_split(train_feature, train_label, test_size=0.2)
# print(x_train.shape, x_valid.shape)
# (138, 20, 9) (35, 20, 9)

# test dataset (실제 예측 해볼 데이터)

test_feature = test[feature_cols]
test_label = test[label_cols]

test_feature, test_label = make_dataset(test_feature, test_label, 20)
# print(test_feature.shape, test_label.shape)
# (30, 20, 9) (30, 1)

from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers import LSTM

model = Sequential()
model.add(LSTM(256,
               input_shape=(train_feature.shape[1], train_feature.shape[2]),
               activation='sigmoid',
               inner_activation='hard_sigmoid',
               return_sequences=True)
          )
model.add(Dropout(0.5))
model.add(LSTM(256,
               input_shape=(train_feature.shape[1], train_feature.shape[2]),
               activation='sigmoid',
               inner_activation='hard_sigmoid',
               return_sequences=False)
          )
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model_path = 'C:/Users/YSS/Desktop/test/'

model.compile(loss='binary_crossentropy', optimizer='rmsprop')
early_stop = EarlyStopping(monitor='val_loss', patience=5)
filename = os.path.join(model_path, 'tmp_checkpoint.h5')
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='auto')

history = model.fit(x_train, y_train,
                    epochs=20,
                    batch_size=16,
                    validation_data=(x_valid, y_valid),
                    callbacks=[checkpoint])

# weight 로딩
model.load_weights(filename)

# 예측
pred = model.predict(test_feature)

# print(test_label)
print(pred)

# plt.figure(figsize=(12, 9))
# plt.plot(test_label, label='actual')
# plt.plot(pred, label='prediction')
# plt.legend()
# plt.show()