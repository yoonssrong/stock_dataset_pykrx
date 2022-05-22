import os
import pandas as pd
from tqdm import tqdm


PATH = "./raw_data/OHLCV_2010-2021/"
savePATH = "./raw_data/OHLCV_2010-2021_merge/"

folders = os.listdir(PATH)

for folder in tqdm(folders):
    files = os.listdir(os.path.join(PATH, folder))
    mergeFolder = os.listdir(savePATH)

    for file in files:
        ticker = pd.read_csv(os.path.join(PATH, folder, file), encoding='utf-8')

        if file in mergeFolder:
            pre_file = pd.read_csv(os.path.join(savePATH, file), encoding='utf-8')
            output = pd.concat([pre_file, ticker])
        else:
            output = ticker

        output.to_csv(savePATH + file, index=False, encoding='utf-8')

print("Finish")