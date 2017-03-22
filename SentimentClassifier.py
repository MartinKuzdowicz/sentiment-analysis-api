from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
import sys  
import os

reload(sys)  
sys.setdefaultencoding('utf8')

def _getFilePath(filename):
	return os.path.join(os.path.dirname(__file__), 'resources/training_data/'+filename)

with open(_getFilePath('imdb_labelled.txt'), 'r') as text_file:
    lines = text_file.read().split('\n')
with open(_getFilePath('amazon_cells_labelled.txt'), 'r') as text_file:
    lines += text_file.read().split('\n')
with open(_getFilePath('yelp_labelled.txt'), 'r') as text_file:
    lines += text_file.read().split('\n')

lines = [line.split('\t') for line in lines if len(line.split('\t'))==2 and line.split('\t')[1] <> '']

train_documents = [line[0] for line in lines]
train_labels = [int(line[1]) for line in lines]

count_vectorizer = CountVectorizer(binary='true')
count_vectorizer._validate_vocabulary()
train_documents = count_vectorizer.fit_transform(train_documents)

from sklearn.naive_bayes import BernoulliNB
classifier = BernoulliNB().fit(train_documents,train_labels)

def getSentimentWeigth(text):
	return classifier.predict(count_vectorizer.transform([text]))

example_text = "this is the best movied"

print(getSentimentWeigth(example_text))

