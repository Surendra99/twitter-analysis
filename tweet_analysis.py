import pandas as pd
from stream import stream_tweets
from pandas import ExcelWriter
from pandas import ExcelFile
from nltk.corpus import stopwords
from textblob import TextBlob
from textblob import Word
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS 
import re

def analyze_sentiment(tweet):
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity ==0:
        return 'Neutral'
    else:
        return 'Negative'

def analyze_tweets():
    stream_tweets('Byjus',file_name='my_tweets')
    df = pd.read_excel('my_tweets.xlsx')

    # removes retweets as they are duplicates.
    df = df[~df.Tweets.str.startswith('RT')]

    # removed users tags,hash tags and urls
    df['clean_tweet'] = df['Tweets'].apply(lambda x: ' '.join(re.sub('(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)', ' ', x).split()))

    # removes standard stop words.
    stop = stopwords.words('english')
    df['clean_tweet'] = df['clean_tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))

    # TO lower case
    df['clean_tweet'] = df['clean_tweet'].apply(lambda x: " ".join(x.lower() for x in x.split()).lstrip())

    # removes numbers
    df['clean_tweet'] = df['clean_tweet'].apply(lambda x: ''.join([i for i in x if not i.isdigit()]))

    # Removes Punctuation
    df['clean_tweet'] = df['clean_tweet'].str.replace('[^\w\s]','')

    #counts no of words in a tweet
    df['words'] = df['clean_tweet'].apply(lambda x: len(x.split()))

    # removes frequent words in a tweet
    freq = pd.Series(' '.join(df['clean_tweet']).split()).value_counts()[:10]
    df['clean_tweet'] = df['clean_tweet'].apply(lambda x: " ".join(x for x in x.split() if x not in freq))

    # Lemmatization converts the word to root word
    df['clean_tweet'] = df['clean_tweet'].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    df['Sentiment'] = df['clean_tweet'].apply(lambda x: analyze_sentiment(x))
    return df

def word_freq():
    df = analyze_tweets()
    all_tweets = ' '.join(tweet for tweet in df['clean_tweet'])
    wordfreq = {}
    for word in all_tweets.split():
        if word not in wordfreq:
            wordfreq[word] = 0 
        wordfreq[word] += 1    
    return wordfreq

def sentiment_analysis():
    df = analyze_tweets()
    sentimane_ap = {'Positive':0,'Neutral':0,'Negative':0}
    for sentiment in df['Sentiment']:
        sentimane_ap[sentiment]+=1
    return sentimane_ap    
