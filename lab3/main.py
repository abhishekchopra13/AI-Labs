import pandas as pd
from models import naive_bayes

def main():
    # Read and load data
    data = pd.read_csv("SMSSpamCollection", sep="\t", header=None)
    data.iloc[:, 0] = data.iloc[:, 0] == "spam"

    k = 5
    accuracy = 0

    for i in range (0, k):
        accuracy += naive_bayes(data, i, k)

    accuracy /= k
    print(f"Accuracy is {accuracy}")

if __name__ == "__main__":
    main()