'''
functions to handle tweet objects as received in the stream
'''

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from database import connect_to_database, insert_single
from datetime import datetime

def get_text(tweet):
    '''
    Get the text from a tweet object (as json) - tests for truncated.
    '''
    if tweet['truncated'] == False:
        return tweet['text']
    else:
        return tweet['extended_tweet'].get('full_text')


def test_for_retweet(tweet):
    '''
    returns True if the tweet is a retweet
    '''
    if 'retweeted_status' in tweet:
        return True
    else:
        return False

def create_output(tweet, user):
    '''
    Creates a dict of values from tweet to be stored
    '''
    time_format = '%a %b %d %H:%M:%S %z %Y'
    sent_analyzer = SentimentIntensityAnalyzer()
    tweet_text = get_text(tweet)

    output =     {
            'timestamp': datetime.strptime(tweet['created_at'], time_format),
            'id': user['id'],
            'name': user['name'],
            'screen_name': user['screen_name'],
            'location': user['location'],
            'text': tweet_text,
            'sentiment': sent_analyzer.polarity_scores(tweet_text).get('compound')
        }

    return output

def convert_tweet_object(tweet_object):
    '''
    converts tweet object to 2 dicts, tweet and user
    '''
    return tweet_object._json, tweet_object.user._json


def handle_tweet(tweet_object, n_tweets):
    tweet, user = convert_tweet_object(tweet_object)

    if not test_for_retweet(tweet):
        output = create_output(tweet, user)
        # Connect to database
        db_connection = connect_to_database('tweets01')
        insert_single(db_connection, 'tweets', output)
        print(output['text'])
