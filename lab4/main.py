import nltk
from sklearn.model_selection import KFold
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, confusion_matrix
from statistics import mean
from nltk.corpus import stopwords
from utils import build_data, frequent_grams, Feature, get_data_in_index, train, get_actual_labels, classify, gini, \
    entropy, misclassifcation_error

# Download required modules
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Get the set of English stop words
stop_words = set(stopwords.words('english'))

data, uni, bi, tri, pos = build_data('./traindata.txt', stop_words)

unigram_counts = frequent_grams(uni, 500)
bigram_counts = frequent_grams(bi, 300)
trigram_counts = frequent_grams(tri, 200)
pos_counts = frequent_grams(pos, 500)
avgLength = mean([row[2] for row in data])
print(avgLength)

Features = []

for y in unigram_counts:
    Features.append(Feature(3, y[0]))

for y in bigram_counts:
    Features.append(Feature(4, y[0]))

for y in trigram_counts:
    Features.append(Feature(5, y[0]))

for y in pos_counts:
    Features.append(Feature(6, y[0]))

Features.append(Feature(2, avgLength))

print(len(Features))
# print(Features[1500])


kfold = KFold(n_splits=10, shuffle=True, random_state=1)
precision = []
recall = []
f_score = []
i = 0

for trainInd, testInd in kfold.split(data):
    train_data = get_data_in_index(data, trainInd)
    test_data = get_data_in_index(data, testInd)

    root = train(train_data, Features, gini)

    prediction = classify(root, test_data)

    actual = get_actual_labels(test_data)
    predicted = prediction

    #     print(classification_report(actual, predicted))
    precision.append(precision_score(actual, predicted, average='macro'))
    recall.append(recall_score(actual, predicted, average='macro'))
    f_score.append(f1_score(actual, predicted, average='macro'))

    print("Training ...")

print("Precision Score: " + str(mean(precision)))
print("Recall Score: " + str(mean(recall)))
print("F-Score: " + str(mean(f_score)))


# ## Part 2
# - All
# - Unigram, Bigram, Trigram, POS
# - Unigram, Bigram, Trigram

def get_report(traindata, testdata, uni_flag=True, bi_flag=True, tri_flag=True, pos_flag=True, len_flag=True,
               func=gini):
    all_features = []

    if uni_flag:
        for y in unigram_counts:
            all_features.append(Feature(3, y[0]))

    if bi_flag:
        for y in bigram_counts:
            all_features.append(Feature(4, y[0]))

    if tri_flag:
        for y in trigram_counts:
            all_features.append(Feature(5, y[0]))

    if pos_flag:
        for y in pos_counts:
            all_features.append(Feature(6, y[0]))

    if len_flag:
        all_features.append(Feature(2, avgLength))

    print("No of Features: " + str(len(all_features)))
    print("Training ...")
    root = train(traindata, all_features, func)
    print("Predicting ...")
    prediction = classify(root, testdata)
    actual = get_actual_labels(testdata)
    print("Prediction done ...")
    matrix = confusion_matrix(actual, prediction)
    acc = matrix.diagonal() / matrix.sum(axis=1)
    accuracy_report = dict(zip(classes, acc))

    return accuracy_report, root, prediction, actual


classes = ['ABBR', 'DESC', 'ENTY', 'HUM', 'LOC', 'NUM']
testdata = build_data('./testdata.txt', stop_words)[0]
len(testdata)

print(get_report(traindata=data, testdata=testdata)[0])

print(get_report(traindata=data, testdata=testdata, func=entropy)[0])

print(get_report(traindata=data, testdata=testdata, func=misclassifcation_error)[0])

print(get_report(traindata=data, testdata=testdata, len_flag=False)[0])

print(get_report(traindata=data, testdata=testdata, len_flag=False, func=entropy)[0])

print(get_report(traindata=data, testdata=testdata, len_flag=False, func=misclassifcation_error)[0])

print(get_report(traindata=data, testdata=testdata, len_flag=False, pos_flag=False)[0])

print(get_report(traindata=data, testdata=testdata, len_flag=False, pos_flag=False, func=entropy)[0])

print(get_report(traindata=data, testdata=testdata, len_flag=False, pos_flag=False, func=misclassifcation_error)[0])


# Error Analysis
def get_wrong_prediction(prediction, actual, dataset):
    data_list = []
    for i in range(len(prediction)):
        if prediction[i] != actual[i]:
            data_list.append(dataset[i])
    return data_list


_, root_gini, prediction_gini, actual_gini = get_report(traindata=data, testdata=testdata)
wrong_data = get_wrong_prediction(prediction_gini, actual_gini, testdata)
print(len(wrong_data))

_, root_entropy, prediction_entropy, actual_entropy = get_report(traindata=data, testdata=wrong_data, func=entropy)
wrong_data_en = get_wrong_prediction(prediction_entropy, actual_entropy, wrong_data)
print(len(wrong_data_en))

_, root_mis, prediction_mis, actual_mis = get_report(traindata=data, testdata=wrong_data, func=misclassifcation_error)
wrong_data_mis = get_wrong_prediction(prediction_entropy, actual_entropy, wrong_data)
print(len(wrong_data_mis))
