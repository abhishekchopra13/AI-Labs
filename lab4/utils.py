from nltk import ngrams, pos_tag
from nltk.corpus import stopwords
from string import punctuation

stop_words = set(stopwords.words('english'))


def getMean(values):
	return sum(values) / len(values)


def getPosTag(line):
	words = [word for word in line if word not in stop_words]
	tagged = pos_tag(words)
	return tagged


def processInput(filepath):
	file = open(filepath)

	dataset = []
	Unigrams = []
	Bigrams = []
	Trigrams = []
	posTagged = []
	avgLength = 0

	for line in file:
		sample = line.split()
		classname = sample[0].split(':')[0]
		question = ' '.join(sample[1:]).translate(str.maketrans('', '', punctuation)).rstrip()

		sample = question.split()

		length = len(sample)
		unigrams = list(ngrams(sample, 1))
		bigrams = list(ngrams(sample, 2))
		trigrams = list(ngrams(sample, 3))
		posTag = getPosTag(sample)

		row = [classname, question, length, unigrams, bigrams, trigrams, posTag]

		dataset.append(row)
		avgLength += length
		Unigrams.extend(unigrams)
		Bigrams.extend(bigrams)
		Trigrams.extend(trigrams)
		posTagged.extend(posTag)

	avgLength /= len(dataset)

	return dataset, avgLength, Unigrams, Bigrams, Trigrams, posTagged


class Question:
	Header = ['Class', 'Text', 'Length', 'Unigrams', 'Bigrams', 'Trigrams', 'POS_Tag']
	
	def __init__(self, colId, value):
		self.colId = colId
		self.value = value

	def match(self, row):
		val = row[self.colId]

		if self.colId == 2:
			return val >= self.value

		return self.value in val

	def __str__(self):
		return f"Does {Question.Header[self.colId]} contains {self.value}?"
		