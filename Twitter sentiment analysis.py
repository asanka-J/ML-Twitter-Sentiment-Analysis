# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 02:15:33 2017

@author: Asanka
"""

import tweepy
from textblob import TextBlob

# Authenticate
consumer_key= 'Q9AsyQxjEMyS2uNEKccN2QFIV'
consumer_secret= 'n4ClXOimLZiItyyvxr3MZO5iJv6wNuCNo40tI02yGqKm6vngnl'

access_token='51440520-TrVTYsoAymtw9Blgx4xi15iPKKjuj6Beb0DmzRIL1'
access_token_secret='lfYEgChHsXn0SCXQv0xV1uGj1GesUVvX3O4TEkTXHhEJs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



for tweet in public_tweets:
    
    print(tweet.text ,'\n')
    
#Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    
#in output polarity mesures how positive or negative some text is , 
#subjectivity mesures how much of an opinion it is and how factual   