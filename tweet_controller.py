from flask import Flask,escape,request
from tweet_analysis import word_freq
from tweet_analysis import sentiment_analysis
import json
import tweepy
from flask_cors import CORS
from Authenticate import authenticate
import asyncio
from flask import Flask
import datetime

app = Flask(__name__)
app.config["DEBUG"] = True
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/', methods=['GET'])
def hello():
    name = request.args.get("name","world")
    return f"Hello, {escape(name)}!"

@app.route('/wordcloud',methods=['GET'])
def get_words_count():
    loaded_dict = json.dumps(word_freq())
    return loaded_dict

@app.route('/sentiment',methods=['GET'])
def get_sentiment_analysis():
    loaded_dict = json.dumps(sentiment_analysis())
    return loaded_dict 

app.run()