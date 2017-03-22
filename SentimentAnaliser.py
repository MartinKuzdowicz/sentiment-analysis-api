from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
import sys  
import os

reload(sys)  
sys.setdefaultencoding('utf8')

def _getFilePath(filename):
	return os.path.join(os.path.dirname(__file__), 'resources/training_data/'+filename)

def _mapToWeight(sentimentBinaryResult):
	if sentimentBinaryResult == 1:
		return 0.8
	else:
		return 0.4

class SentimentAnaliser:

	def __init__(self):
		with open(_getFilePath('imdb_labelled.txt'), 'r') as text_file:
		    lines = text_file.read().split('\n')
		with open(_getFilePath('amazon_cells_labelled.txt'), 'r') as text_file:
		    lines += text_file.read().split('\n')
		with open(_getFilePath('yelp_labelled.txt'), 'r') as text_file:
		    lines += text_file.read().split('\n')

		lines = [line.split('\t') for line in lines if len(line.split('\t'))==2 and line.split('\t')[1] <> '']

		train_documents = [line[0] for line in lines]
		train_labels = [int(line[1]) for line in lines]

		self.count_vectorizer = CountVectorizer(binary='true')
		self.count_vectorizer._validate_vocabulary()
		train_documents = self.count_vectorizer.fit_transform(train_documents)

		self.classifier = BernoulliNB().fit(train_documents,train_labels)

	def getSentimentWeigth(self, text):
		binaryRes = self.classifier.predict(self.count_vectorizer.transform([text]))
		return _mapToWeight(binaryRes)


