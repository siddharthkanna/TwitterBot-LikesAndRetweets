
import tweepy
import time
from credentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth, wait_on_rate_limit=True)


search = input("Enter Hashtag or Keyword: ")
ntweets = 10

for tweet in tweepy.Cursor(api.search_tweets, search).items(ntweets):
    try:
        tweet.favorite()
        print('Tweet Liked')#LIKES THE TWEET

        tweet.retweet()
        print('Tweet retweeted!')#RETWEETS THE TWEET

        print('Liked and Retweeted!')#To check everything is working fine or not.
        time.sleep(200)
    except tweepy.TweepyException as e:
        print(e.reason)

    except StopIteration:
        break
