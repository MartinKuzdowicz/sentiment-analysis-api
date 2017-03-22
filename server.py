from flask import Flask
from SentimentAnaliser import SentimentAnaliser

app = Flask(__name__)
sentAnl = SentimentAnaliser()

@app.route('/api/v1/sentiment/<sentence>')
def hello_world(sentence):
	sentimentWeigth = sentAnl.getSentimentWeigth(sentence)
   	return '{ sentimentWeigth: ' + str(sentimentWeigth) + '}'

if __name__ == '__main__':
   app.run()