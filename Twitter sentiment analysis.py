# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 02:15:33 2017

@author: Asanka
"""

import pandas as pd
import tweepy
from textblob import TextBlob
import numpy as np
import csv

# Open/create a file to append data to
csvFile = open('./result.csv', 'a',newline='')

#Use csv writer
csvWriter = csv.writer(csvFile)

# Authenticate
consumer_key= 'Q9AsyQxjEMyS2uNEKccN2QFIV'
consumer_secret= 'n4ClXOimLZiItyyvxr3MZO5iJv6wNuCNo40tI02yGqKm6vngnl'

access_token='51440520-TrVTYsoAymtw9Blgx4xi15iPKKjuj6Beb0DmzRIL1'
access_token_secret='lfYEgChHsXn0SCXQv0xV1uGj1GesUVvX3O4TEkTXHhEJs'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Srilanka')

print(type(public_tweets))

csvWriter.writerow(['created_at','text'])
for tweet in public_tweets:
    
    print(tweet.text ,'\n')
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
#Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)#in output polarity mesures how positive or negative some text is , #subjectivity mesures how much of an opinion it is and how factual 

csvFile.close()


dataSet=pd.read_csv('result.csv')
dataSet.set_index('created_at')