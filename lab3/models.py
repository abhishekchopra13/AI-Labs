import pandas as pd

def naive_bayes(data: pd.DataFrame, i: int, k: int):
    n_rows = data.shape[0]
    size_of_each_fold = n_rows//k
    test = data.iloc[i*size_of_each_fold: (i+1)*size_of_each_fold, :]
    train = data.drop(range(i*size_of_each_fold, (i+1)*size_of_each_fold))

    pi = {
        0: 0,
        1: 0
    }

    for index, row in train.iterrows():
        if row[0] == 1:
            pi[1] += 1
        else:
            pi[0] += 1

    for key in pi:
        pi[key] /= train.shape[0]

    print(pi[0], pi[1])


    return 0