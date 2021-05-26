import seaborn as sns
import numpy as np
import pandas as pd
def to_sequences(data, seq_len):
    d = []
  #  import numpy as np
    for index in range(len(data) - seq_len):
        d.append(data[index: index + seq_len])

    return np.array(d)
def preprocess(data_raw, seq_len, train_split):

    data = to_sequences(data_raw, seq_len)

    num_train = int(train_split * data.shape[0])
    X_train = data[:num_train, :-1, :]
    y_train = data[:num_train, -1, :]

    X_test = data[num_train:, :-1, :]
    y_test = data[num_train:, -1, :]

    return X_train, y_train, X_test, y_test
def corr(path):
    for fname in glob.glob(path):
    data = pd.read_csv(fname).set_index('Date')
    cryptocurrency = fname.split('coin_')[1].split('.csv')[0]
    if len(data)>1500 and cryptocurrency != 'Bitcoin':
        data = data.rename(columns={"Close":cryptocurrency})
        columns.append(cryptocurrency)
        df=pd.merge(df,data[cryptocurrency], how='inner', left_index=True, right_index=True)
        corrMatrix = df.corr()
        sns.heatmap(corrMatrix, annot=True)
        plt.show()