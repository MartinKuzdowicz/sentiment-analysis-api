from flask import Flask, jsonify
from sentiment_analiser import SentimentAnaliser

app = Flask(__name__)
sentAnl = SentimentAnaliser()

@app.route('/api/v1/sentiment/<sentence>')
def hello_world(sentence):
	sentimentWeigth = sentAnl.getSentimentWeigth(sentence)
   	return jsonify({'sentimentWeigth': sentimentWeigth})

if __name__ == '__main__':
   app.run()