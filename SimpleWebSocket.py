import tweepy
from Authenticate import authenticate
import asyncio
import datetime
import websockets

tweets = []
class MyStreamListener(tweepy.StreamListener):
    def on_status(self,status):
        tweets.append(status.text)
    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            return False

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        print(now)
        await websocket.send(now)

api = authenticate()
myStream = tweepy.Stream(auth = api.auth, listener= MyStreamListener())
myStream.filter(track=['trump'],is_async=True)

start_server = websockets.serve(time, "127.0.0.1", 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
