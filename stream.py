import tweepy
import numpy
import pandas as pd
from Authenticate import authenticate
# This is a standard API which can fetch only tweets from the past one week
def stream_tweets(data,file_name):
    
    df = pd.DataFrame(columns=['Tweets', 'User', 'User_statuses_count', 
                             'User_followers', 'User_location', 'User_verified',
                             'Fav_count', 'RT_count', 'Tweet_date'])
    api = authenticate()                             
    i=0
    for tweet in tweepy.Cursor(api.search,q=data,count=100,lang='en').items():
        df.loc[i,'Tweets'] = tweet.text
        df.loc[i,'User'] = tweet.user.name
        df.loc[i, 'User_location'] = tweet.user.location
        df.loc[i, 'User_verified'] = tweet.user.verified
        df.loc[i, 'fav_count'] = tweet.favorite_count
        df.loc[i, 'rt_count'] = tweet.retweet_count
        df.loc[i, 'tweet_date'] = tweet.created_at
        df.to_excel('{}.xlsx'.format(file_name))
        i+=1
        if i == 5000:
            break
        else:
            pass