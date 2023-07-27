import tweepy
import os

twitter_api_key = os.environ['TWITTER-API-KEY']
twitter_api_secret = os.environ['TWITTER-API-SECRET']

authentication = tweepy.AppAuthHandler(twitter_api_key, twitter_api_secret)
api_object = tweepy.API(authentication)

import pandas as pd

tweet_dataset = []
tweets = api_object.search_tweets(q='paypal -filter:retweets -filter:replies', lang = "en", result_type="recent", count = 100)
 
for tweet in tweets:
    tweet_content = {'id': tweet.id, 'date': tweet.created_at, 'user_name':tweet.user.screen_name, 'text':tweet.text,}
    tweet_dataset.append(tweet_content)

tweet_dataframe = pd.DataFrame(tweet_dataset)
print(tweet_dataframe.shape)
tweet_dataframe.head()

