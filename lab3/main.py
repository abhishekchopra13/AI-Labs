import pandas as pd
from models import multinomial_naive_bayes, multivariate_naive_bayes

def main():
    # Read and load data
    data = pd.read_csv("SMSSpamCollection", sep="\t", header=None)
    data.iloc[:, 0] = data.iloc[:, 0] == "spam"

    k = 5
    accuracy_multinomial = 0
    accuracy_multivariate = 0

    for i in range (0, k):
        accuracy_multinomial += multinomial_naive_bayes(data, i, k)
        accuracy_multivariate += multivariate_naive_bayes(data, i, k)

    accuracy_multivariate /= k
    accuracy_multinomial /= k
    print(f"{k}-fold accuracy for Multinomial Naive Bayes: {accuracy_multinomial}")
    print(f"{k}-fold accuracy for Multivariate Naive Bayes: {accuracy_multivariate}")

if __name__ == "__main__":
    main()