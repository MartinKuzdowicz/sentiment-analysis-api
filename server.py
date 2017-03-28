from flask import Flask, jsonify
from sentiment_analiser import SentimentAnaliser

app = Flask(__name__)
sentAnl = SentimentAnaliser()

@app.route('/api/v1/sentiment/<sentence>')
def classifySentiment(sentence):
	sentimentWeigth = sentAnl.getSentimentWeigth(sentence)
   	return jsonify({'sentimentWeigth': sentimentWeigth})

@app.after_request
def applyAfterRequestTrigger(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response

if __name__ == '__main__':
   app.run()