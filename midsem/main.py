import pandas as pd
from models import multinomial_naive_bayes, multivariate_naive_bayes

def main():
    # Read and load training data
    train_data = pd.read_csv("dataset.txt", sep=":", header=None)
    train_data.iloc[:, 0] = train_data.iloc[:, 0] == "CV"

    # Read the test data
    with open("test.txt") as f:
        test = f.readline()

    print("Printing details for Vocaulary:\n")
    print("Word: (times in DL, times in CV)")
    # get prediction, parameters and score for corresponding model
    results_multinomial, pxc_multinomial, score_multinomial = multinomial_naive_bayes(train_data, test)
    results_multivariate, pxc_multivariate, score_multivariate = multivariate_naive_bayes(train_data, test)
    print("")
    print(f"(i) Prediction of Multivariate Naive Bayes: {results_multivariate} with confidence: {score_multivariate}")
    print(f"(ii) Prediction of Multinomial Naive Bayes: {results_multinomial} with confidence: {score_multinomial}")
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