import tweepy
from handle_tweets import handle_tweet

# Initiate a custom stream listener
class StreamListener_(tweepy.StreamListener):
    def on_status(self, status):
        # This is where we can control what happens when a tweet is received.
        n_tweets = 0
        n_tweets = handle_tweet(status, n_tweets)

    def on_error(self, status_code):
        if status_code == 420:
            # Disconnect stream (by returning false)
            print('Disconnected error 420')
            return False
