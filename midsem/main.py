import pandas as pd
from models import multinomial_naive_bayes, multivariate_naive_bayes

def main():

    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    # Read and load training data
    train_data = pd.read_csv("dataset.txt", sep=":", header=None)
    train_data.iloc[:, 0] = train_data.iloc[:, 0] == "CV"
    for i in range (0, train_data.shape[0]):
        for ele in train_data.iloc[i, 1]:
            if ele in punc:
                train_data.iloc[i, 1] = train_data.iloc[i, 1].replace(ele, "")

    # Read the test data
    with open("test.txt") as f:
        test = f.readline()
    # Cleaning the test data, by removing punctuations leads to better results
    for ele in test:
        if ele in punc:
            test = test.replace(ele, "")

    print("Printing details for Vocaulary:\n")
    print("Word: (times in DL, times in CV)")
    # get prediction, parameters and score for corresponding model
    results_multinomial, pxc_multinomial, score_multinomial_DL, score_multinomial_CV = multinomial_naive_bayes(train_data, test)
    results_multivariate, pxc_multivariate, score_multivariate_DL, score_multivariate_CV = multivariate_naive_bayes(train_data, test)
    print("")
    print(f"(i) Prediction of Multivariate Naive Bayes: {results_multivariate}")
    print(f"Score DL: {score_multivariate_DL}, Score CV: {score_multivariate_CV}")
    print(f"(ii) Prediction of Multinomial Naive Bayes: {results_multinomial}")
    print(f"Score DL: {score_multinomial_DL}, Score CV: {score_multinomial_CV}")
    print("")
    print("Value of parameters for Multinomial:")
    print("Word: (parameter for DL, for CV)\n")
    for key in pxc_multinomial:
        print(f"{key}: {pxc_multinomial[key]}")
    print("")
    print("Value of parameters for Multivariate:")
    print("Word: (parameter for DL, for CV)\n")
    for key in pxc_multivariate:
        print(f"{key}: {pxc_multivariate[key]}")

if __name__ == "__main__":
    main()