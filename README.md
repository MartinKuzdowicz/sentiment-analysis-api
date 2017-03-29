
# Overview
	
	Python sentiment analysis Rest service
	build on Flask microframework
	
training data for sentiment analysis comes from UC Irvine Machine Learning Repository:
[https://archive.ics.uci.edu/ml/machine-learning-databases/00331/](https://archive.ics.uci.edu/ml/machine-learning-databases/00331/)

# Requierments

	Python
	pip
	virtualenv

# how to start the app as server and install dependecies
	
	1. install virtualenv if you do not have it so far

		sudo pip install virtualenv

	2. go to 

		/sentiment-analysis-server main directory

	3. create virtualenv

		virtualenv venv

	4. activate virtualenv

		. venv/bin/activate

	5. install dependencies

		sudo pip install -r requirements.txt

	6. start Flask server

		export FLASK_APP=server.py
		Flask run --host=0.0.0.0

	Tips:
	Flask run -> is for localhost usage only
	Flask run --host=0.0.0.0 -> is when you want your app to be visible from your ip address to other devices

# how to use:

	go to browser and, type: localhost:5000/api/v1/sentiment/<text to calculate sentiment>
	or outside <your public ip address>:5000/api/v1/sentiment/<text to calculate sentiment>

# to deactivate virtualenv

	deactivate
