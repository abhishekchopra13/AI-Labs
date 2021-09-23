import pandas as pd
from math import log

def multinomial_naive_bayes(train: pd.DataFrame, test: str) -> str:
   
    # Number of rows in training dataset
    n_rows = train.shape[0] 

    # Inherent probability of each class
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

    pxc = {} # stores probability of each word in DL and CV task

    count_DL = 0
    count_CV = 0

    # Iterating in training dataset to calculate P(word / Class) 
    for index, row in train.iterrows():
        words = row[1].split(" ")
        if row[0] == 0:
            count_DL += len(words)
        else:
            count_CV += len(words)
        for word in words:
            if word in pxc:
                if row[0] == 0:
                    # update frequency for appropriate class
                    pxc[word] = (pxc[word][0] + 1, pxc[word][1])
                else:
                    pxc[word] = (pxc[word][0], pxc[word][1] + 1)
            else:
                if row[0] == 0:
                    pxc[word] = (1, 0)
                else:
                    pxc[word] = (0, 1)

    for key in pxc:
        # printing vocabulary
        print(f"{key}: {pxc[key]}")
        # Add-one Laplace Smoothning for Multinomial
        pxc[key] = ((pxc[key][0] + 1)/(count_DL + len(pxc)), (pxc[key][1] + 1)/(count_CV + len(pxc)))


    # Testing on the parameters estimated
    words = test.split(" ")
    score_DL = log(pi[0])
    score_CV = log(pi[1])

    for word in words:
        if word not in pxc:
            continue
        score_CV += log(pxc[word][1])
        score_DL += log(pxc[word][0])

    if (score_CV >= score_DL):
        return "CV", pxc, score_DL, score_CV
    else:
        return "DL", pxc, score_DL, score_CV

def multivariate_naive_bayes(train: pd.DataFrame, test: str) -> str:
    n_rows = train.shape[0]

    # Inherent probability of each class
    pi = {
        0: 0,
        1: 0
    }

    for index, row in train.iterrows():
        if row[0] == 1:
            pi[1] += 1
        else:
            pi[0] += 1

    for word in pi:
        pi[word] /= train.shape[0]

    pxc = {}    # stores probability of each word in DL and CV task

    count_DL = 0
    count_CV = 0

    # Iterating in training dataset to calculate P(word / Class) 
    for index, row in train.iterrows():
        words = row[1].split(" ")
        if row[0] == 0:
            count_DL += 1
        else:
            count_CV += 1
        for word in set(words):
            if word in pxc:
                if row[0] == 0:
                    # update frequency for appropriate class
                    pxc[word] = (pxc[word][0] + 1, pxc[word][1])
                else:
                    pxc[word] = (pxc[word][0], pxc[word][1] + 1)
            else:
                if row[0] == 0:
                    pxc[word] = (1, 0)
                else:
                    pxc[word] = (0, 1)

    for word in pxc:
        # Add-one Laplace Smoothning for Multivariate
        pxc[word] = ((pxc[word][0] + 1)/(count_DL + 2), (pxc[word][1] + 1)/(count_CV + 2))

    # Testing on the parameters estimated
    words = test.split(" ")
    score_DL = log(pi[0])
    score_CV = log(pi[1])

    for word in pxc:
        if word in words:
            score_CV += log(pxc[word][1])
            score_DL += log(pxc[word][0])
        else:
            score_CV += log(1 - pxc[word][1])
            score_DL += log(1 - pxc[word][0])

    if (score_CV >= score_DL):
        return "CV", pxc, score_DL, score_CV
    else:
        return "DL", pxc, score_DL, score_CV