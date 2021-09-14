import pandas as pd
from math import log

def multinomial_naive_bayes(data: pd.DataFrame, i: int, k: int):
    n_rows = data.shape[0]
    size_of_each_fold = n_rows//k
    test = data.iloc[i*size_of_each_fold: (i+1)*size_of_each_fold, :]
    train = data.drop(range(i*size_of_each_fold, (i+1)*size_of_each_fold))

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

    pxc = {} # stores probability of each word in spam and normal messages

    count_ham = 0
    count_spam = 0

    # Iterating in training dataset to calculate P(word / Class) 
    for index, row in train.iterrows():
        words = row[1].split(" ")
        if row[0] == 0:
            count_ham += len(words)
        else:
            count_spam += len(words)
        for word in words:
            if word in pxc:
                if row[0] == 0:
                    pxc[word] = (pxc[word][0] + 1, pxc[word][1])
                else:
                    pxc[word] = (pxc[word][0], pxc[word][1] + 1)
            else:
                if row[0] == 0:
                    pxc[word] = (1, 0)
                else:
                    pxc[word] = (0, 1)

    for key in pxc:
        # Add-one Laplace Smoothning for Multinomial
        pxc[key] = ((pxc[key][0] + 1)/(count_ham + len(pxc)), (pxc[key][1] + 1)/(count_spam + len(pxc)))

    correct_predictions = 0

    # Testing on the parameters estimated
    for index, row in test.iterrows():
        words = row[1].split(" ")
        prob_ham = log(pi[0])
        prob_spam = log(pi[1])

        for word in words:
            if word not in pxc:
                continue
            prob_spam += log(pxc[word][1])
            prob_ham += log(pxc[word][0])


        if (prob_spam >= prob_ham) and row[0] == 1:
            correct_predictions += 1
        elif (prob_spam < prob_ham) and row[0] == 0:
            correct_predictions += 1

    return correct_predictions / test.shape[0]

def multivariate_naive_bayes(data: pd.DataFrame, i: int, k: int):
    n_rows = data.shape[0]
    size_of_each_fold = n_rows//k
    test = data.iloc[i*size_of_each_fold: (i+1)*size_of_each_fold, :]
    train = data.drop(range(i*size_of_each_fold, (i+1)*size_of_each_fold))

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

    pxc = {} # probability this word is spam given word occurs

    count_ham = 0
    count_spam = 0

    # Iterating in training dataset to calculate P(word / Class) 
    for index, row in train.iterrows():
        words = row[1].split(" ")
        if row[0] == 0:
            count_ham += 1
        else:
            count_spam += 1
        for word in set(words):
            if word in pxc:
                if row[0] == 0:
                    pxc[word] = (pxc[word][0] + 1, pxc[word][1])
                else:
                    pxc[word] = (pxc[word][0], pxc[word][1] + 1)
            else:
                if row[0] == 0:
                    pxc[word] = (1, 0)
                else:
                    pxc[word] = (0, 1)

    for key in pxc:
        # Add-one Laplace Smoothning for Multivariate
        pxc[key] = ((pxc[key][0] + 1)/(count_ham + 2), (pxc[key][1] + 1)/(count_spam + 2))

    correct_predictions = 0

    # Testing on the parameters estimated
    for index, row in test.iterrows():
        words = row[1].split(" ")
        prob_ham = log(pi[0])
        prob_spam = log(pi[1])
        
        for word in set(words):
            if word not in pxc:
                continue
            prob_spam += log(pxc[word][1])
            prob_ham += log(pxc[word][0])
            
        if (prob_spam >= prob_ham) and row[0] == 1:
            correct_predictions += 1
        elif (prob_spam < prob_ham) and row[0] == 0:
            correct_predictions += 1

    return correct_predictions / test.shape[0]