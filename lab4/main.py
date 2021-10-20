from utils import processInput, Question, getMean
from DecisionTree import DecisionTree
from collections import Counter
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix

dataset, avgLength, unigrams, bigrams, trigrams, postags = processInput("traindata.txt")

labels = [row[0] for row in dataset]
labels = list(set(labels))
print("Labels for prediction:", labels)

# Extract top ngrams

# 500 top 1-gram
unigram_count = Counter(unigrams).most_common(500)
# 300 top 2-gram
bigram_count = Counter(bigrams).most_common(300)
# 200 top 3-gram
trigram_count = Counter(trigrams).most_common(200)
# 500 top POS_Tags
tags_count = Counter(postags).most_common(500)


def prepareQuestions(uniFlag=True, biFlag=True, triFlag=True, posFlag=True, lenFlag=True):
    questions = []

    if lenFlag:
        questions.append(Question(2, avgLength))

    if uniFlag:
        for gram in unigram_count:
            questions.append(Question(3, gram[0]))

    if biFlag:
        for gram in bigram_count:
            questions.append(Question(4, gram[0]))

    if triFlag:
        for gram in trigram_count:
            questions.append(Question(5, gram[0]))

    if posFlag:
        for gram in tags_count:
            questions.append(Question(6, gram[0]))

    return questions


allQuestions = prepareQuestions()


def getPrediction(classifier, test_data):
    predicted_values = []
    for row in test_data:
        prediction = classifier.classify(row)
        predicted_values.append(prediction)

    return predicted_values


def get10FoldCVResult():
    print("Preparing 10-fold cross-validation results...")
    kf = KFold(10, shuffle=True, random_state=1)

    precision = []
    f_score = []
    recall = []
    for trainIds, testIds in kf.split(dataset):
        train_data = []
        test_data = []
        for x in trainIds:
            train_data.append(dataset[x])

        print("Training...")
        dTreeCf = DecisionTree(train_data, allQuestions, "gini")

        actual_values = []

        for x in testIds:
            test_data.append(dataset[x])

            actual = dataset[x][0]
            actual_values.append(actual)

        predicted_values = getPrediction(dTreeCf, test_data)

        precision.append(precision_score(actual_values, predicted_values, average='macro'))
        recall.append(recall_score(actual_values, predicted_values, average='macro'))
        f_score.append(f1_score(actual_values, predicted_values, average='macro'))

    print("Avg. Precision:", getMean(precision))
    print("Avg. Recall:", getMean(recall))
    print("Avg. F-Score:", getMean(f_score))


get10FoldCVResult()

testData, tavgLen, tUnigrams, tBigrams, tTrigrams, tPostags = processInput("testdata.txt")


def featureAblationReport():
    print("Feature ablation report(avgLength, unigrams, bigrams, trigrams, postags): ")
    features = ["Unigrams", "Bigrams", "Trigrams", "POS_Tags", "AvgLength"]

    for case in range(1 << 5):
        params = [True] * 5
        for t in range(5):
            if (case & (1 << t)):
                continue
            else:
                params[t] = False

        # prepareQuestions with True params only.
        print("\n\nTraining DecisionTree with ", end="")
        for t in range(5):
            if params[t]:
                print(features[t], end="; ")
            else:
                print("No", features[t], end="; ")
        print("\n---------------------------------------------------------------")

        dTreeCf = DecisionTree(dataset,
                               prepareQuestions(params[0], params[1], params[2], params[3], params[4]),
                               "gini")

        predicted_values = getPrediction(dTreeCf, testData)
        actual_values = [row[0] for row in testData]

        matrix = confusion_matrix(actual_values, predicted_values, labels=labels)
        acc = matrix.diagonal() / matrix.sum(axis=1)

        accuracy_report = dict(zip(labels, acc))

        print("Accuracy Report:", accuracy_report)


featureAblationReport()

criteria = ['entropy', 'gini', 'miserror']


def getModelReport(criteria):
    print(f"\n\nTraining model with {criteria} information gain...")
    dTreeCf = DecisionTree(dataset, allQuestions, criteria)
    predicted_values = getPrediction(dTreeCf, testData)
    actual_values = [row[0] for row in testData]

    matrix = confusion_matrix(actual_values, predicted_values, labels=labels)

    precision = precision_score(actual_values, predicted_values, average='macro')
    recall = recall_score(actual_values, predicted_values, average='macro')
    f_score = f1_score(actual_values, predicted_values, average='macro')

    return precision, recall, f_score, matrix


for c in criteria:
    precision, recall, f_score, matrix = getModelReport(c)
    print(f"'{c}' Model Report")
    print("----------------------------")
    print("Precision:", precision)
    print("Recall:", recall)
    print("F-Score:", f_score)
    print("Confusion Matrix:\n", matrix)
