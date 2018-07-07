import tweepy
from load_api import get_auths, load_api
from stream_listener_ import StreamListener_
from database import connect_to_database

def start_stream(keywords):
    n_tweets = 0
    api = load_api(get_auths())
    listener = StreamListener_()
    stream = tweepy.Stream(api.auth, listener)

    stream.filter(track = keywords)

if __name__ == '__main__':
    start_stream(['Trump'])
