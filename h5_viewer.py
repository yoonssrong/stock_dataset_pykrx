import h5py
filename = './output/2020년 학습/a3c_kospi200_2/a3c_lstm_policy_20210305155707.h5'

with h5py.File(filename, "r") as f:
    # List all groups
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    # Get the data
    data = list(f[a_group_key])

