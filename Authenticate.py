import tweepy

def authenticate():
    consumer_token = 'XXXXXXX'
    consumer_secret = 'XXXXX'

    access_token = 'XXXX'
    access_token_secret = 'XXX'

    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    return api