import tweepy

def authenticate():
    consumer_token = 'zHLw4LctqzC5oyC87smSXvOo0'
    consumer_secret = '8Gbw485DHlnRByXcTugITnD2yXs8WEGii2NVh65k0WUTOBmB24'

    access_token = '1057806133-SgTRDEjJDEeUo2o6rEn6dGfZadpk0HCj12yTN1g'
    access_token_secret = 'aiy9fEif6HUMzHdmZ0JPXYarUdjm9D0zbdOCwoUrR4FzB'

    auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    return api