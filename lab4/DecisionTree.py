from math import log2
from copy import deepcopy


def class_counts(rows):
    counts = {}
    for row in rows:
        label = row[0]
        if label not in counts:
            counts[label] = 0
        counts[label] += 1
    return counts


def gini_index(rows):
    counts = class_counts(rows)
    impurity = 1
    for lbl in counts:
        prob_of_lbl = counts[lbl] / len(rows)
        impurity -= prob_of_lbl ** 2
    return impurity


def misclassifcation_error(rows):
    counts = class_counts(rows)
    max_prob = 0
    for lbl in counts:
        prob_of_lbl = counts[lbl] / len(rows)
        if prob_of_lbl > max_prob:
            max_prob = prob_of_lbl
    return 1 - max_prob


def entropy(rows):
    counts = class_counts(rows)
    impurity = 0
    for lbl in counts:
        prob_of_lbl = counts[lbl] / len(rows)
        impurity -= prob_of_lbl * log2(prob_of_lbl)
    return impurity


criteriaFunc = {
    "gini": gini_index,
    "entropy": entropy,
    "miserror": misclassifcation_error
}


def info_gain(left, right, current_uncertainty, criteria):
    prob = len(left) / (len(left) + len(right))
    return current_uncertainty - prob * criteria(left) - (1 - prob) * criteria(right)


def partition(rows, question):
    trueRows = []
    falseRows = []
    for row in rows:
        if question.match(row):
            trueRows.append(row)
        else:
            falseRows.append(row)
    return trueRows, falseRows


def findBestSplit(rows, questions, criteria):
    best_gain = 0
    best_question = None
    current_uncertainty = criteria(rows)

    for question in questions:
        trueRows, falseRows = partition(rows, question)
        if not trueRows or not falseRows:
            continue

        gain = info_gain(trueRows, falseRows, current_uncertainty, criteria)
        if gain >= best_gain:
            best_gain, best_question = gain, question

    return best_gain, best_question


class DecisionTree:
    def __init__(self, trainData, questions, criteria):
        self.root = self.formTree(trainData, deepcopy(questions), criteriaFunc[criteria])

    class DecisionNode:
        def __init__(self, question, trueChild, falseChild):
            self.question = question
            self.trueChild = trueChild
            self.falseChild = falseChild

    class Leaf:
        def __init__(self, rows):
            counts = class_counts(rows)
            self.prediction = next(iter(counts))

    def formTree(self, dataset, questions, criteria):
        gain, question = findBestSplit(dataset, questions, criteria)

        if gain == 0:
            return self.Leaf(dataset)

        trueRows, falseRows = partition(dataset, question)
        questions.remove(question)

        trueChild = self.formTree(trueRows, questions, criteria)
        falseChild = self.formTree(falseRows, questions, criteria)

        return self.DecisionNode(question, trueChild, falseChild)

    def classify(self, row):
        def classifyRow(node, row):
            if isinstance(node, self.Leaf):
                return node.prediction

            if node.question.match(row):
                return classifyRow(node.trueChild, row)
            else:
                return classifyRow(node.falseChild, row)

        return classifyRow(self.root, row)
