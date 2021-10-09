import string
import nltk
from collections import Counter
from nltk import ngrams
from nltk.tokenize import sent_tokenize
from copy import deepcopy
import operator
from math import log2


header = ['Label', 'Text', 'Length', 'Unigram', 'Bigram', 'Trigram']


class Feature:
    def __init__(self, col, val):
        self.column = col
        self.value = val

    def match(self, ex):
        val = ex[self.column]

        if is_numeric(val):
            return val <= self.value
        return self.value in val

    def __repr__(self):
        condition = "exists"
        return "Does %s %s %s?" % (
            header[self.column], str(self.value), condition)


class Leaf:
    def __init__(self, r):
        self.predictions = class_fref(r)


class DecisionNode:
    def __init__(self,
                 feat,
                 true_b,
                 false_b):
        self.Feature = feat
        self.true_branch = true_b
        self.false_branch = false_b


def is_numeric(val):
    return isinstance(val, int) or isinstance(val, float)


# Returns n-grams
def get_ngrams(data, n):
    tokens = [token for token in data.split(" ") if token != ""]
    res = list(ngrams(tokens, n))
    return res


def frequent_grams(g, top_n):
    return Counter(g).most_common(top_n)


def get_pos_tag(text, stop_words):
    tokenized = sent_tokenize(text)
    words_list = nltk.word_tokenize(tokenized[0])
    words_list = [w for w in words_list if not w in stop_words]
    tagged = nltk.pos_tag(words_list)
    return tagged


def build_data(file_path, stop_words):
    data = []
    uni = []
    bi = []
    tri = []
    pos = []
    file = open(file_path, encoding="ISO-8859-1")

    for line in file:
        line = line.split(':')
        row = [line[0], ' '.join(line[1].split(' ')[1:]).translate(str.maketrans('', '', string.punctuation)).rstrip()]

        length = len(row[1].split(' '))
        unigram = get_ngrams(row[1], 1)
        bigram = get_ngrams(row[1], 2)
        trigram = get_ngrams(row[1], 3)
        postag = get_pos_tag(row[1], stop_words)

        row.append(length)
        row.append(unigram)
        uni.extend(unigram)
        row.append(bigram)
        bi.extend(bigram)
        row.append(trigram)
        tri.extend(trigram)
        row.append(postag)
        pos.extend(postag)
        data.append(row)

    return data, uni, bi, tri, pos


def class_fref(rows):
    counts = {}
    for row in rows:
        label = row[0]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def gini(rows):
    counts = class_fref(rows)
    imp = 1
    for label in counts:
        prob_of_label = counts[label] / float(len(rows))
        imp -= prob_of_label**2
    return imp


def misclassifcation_error(rows):
    counts = class_fref(rows)
    max_prob = 0
    for label in counts:
        prob_of_label = counts[label] / float(len(rows))
        if prob_of_label > max_prob:
            max_prob = prob_of_label
    return 1 - max_prob


def entropy(rows):
    counts = class_fref(rows)
    imp = 0
    for label in counts:
        prob_of_label = counts[label] / float(len(rows))
        imp -= prob_of_label*log2(prob_of_label)
    return imp


def info_gain(left, right, curr_uncertainty, func):
    p = float(len(left)) / (len(left) + len(right))
    return curr_uncertainty - p * func(left) - (1 - p) * func(right)


def partition(rows, Feature):
    true_rows = []
    false_rows = []

    for row in rows:
        if Feature.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)
    return true_rows, false_rows


def find_best_split(rows, Features, func):
    best_gain = 0
    best_feature = None
    current_uncertainty = func(rows)

    for f in Features:
        true_rows, false_rows = partition(rows, f)
        if len(true_rows) == 0 or len(false_rows) == 0:
            continue

        gain = info_gain(true_rows, false_rows, current_uncertainty, func)

        if gain >= best_gain:
            best_gain, best_feature = gain, f

    return best_gain, best_feature


def form_tree(rows, Features, func):
    gain, Feature = find_best_split(rows, Features, func)

    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, Feature)
    Features.remove(Feature)

    true_branch = form_tree(true_rows, Features, func)
    false_branch = form_tree(false_rows, Features, func)

    return DecisionNode(Feature, true_branch, false_branch)


def classify_row(node, row):
    if isinstance(node, Leaf):
        return node.predictions

    if node.Feature.match(row):
        return classify_row(node.true_branch, row)
    else:
        return classify_row(node.false_branch, row)


def train(data, Features, func):
    return form_tree(data, deepcopy(Features), func)


def classify(root, rows):
    predictions = []
    for r in rows:
        predictions.append(max(classify_row(root, r).items(), key=operator.itemgetter(1))[0])
    return predictions


def get_data_in_index(data, index):
    l = []
    for i in range(len(data)):
        if i in index:
            l.append(data[i])
    return l


def get_actual_labels(act_data):
    act_labels = []
    for d in act_data:
        act_labels.append(d[0])
    return act_labels

