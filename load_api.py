import tweepy
import json

TWITTER_AUTHS = 'twitter_auths.json'

def get_auths(FILE=TWITTER_AUTHS):
    '''
    Reads auth details from json file.
    '''

    with open(FILE) as f:
        return json.load(f)



def load_api(AUTHS):
    '''
    returns a tweepy API object with applied credentials.
    '''

    auth = tweepy.OAuthHandler(
        AUTHS.get('consumer_key'), AUTHS.get('consumer_secret')
        )
    auth.set_access_token(
        AUTHS.get('access_token'), AUTHS.get('access_token_secret')
        )

    return tweepy.API(auth)
