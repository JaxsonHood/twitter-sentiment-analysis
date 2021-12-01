import re
import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
  
class Twit(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        # creating object of TwitterClient Class
        self.client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAMMnWAEAAAAAv0QQfWDgDqhKg3%2BjNG6a9meyjfE%3DrlJW43h46mB5hSQRzV9Jfh7nhqEh8lewadR2Jlz0wmvfIJKmjZ')
        self.analyzer = SentimentIntensityAnalyzer()
  
    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    
    def rounder(self, num):
        if num > 0: return 1
        if num < 0: return -1
        return 0
  
    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        return analysis.sentiment.polarity
    
    def get_results(self, tweets):
        total_polarity = 0
        total_polarity_rounded = 0
        
        size = len(tweets)
        
        for tweet in tweets:
            score = tweet['sentiment_score']
            total_polarity += score
            total_polarity_rounded += self.rounder(score)
            
        avg_score = total_polarity / size
        avg_rounded_score = total_polarity_rounded / size
            
        return tweets, avg_score, avg_rounded_score, size
            
  
    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []
  
        try:
            # call twitter api to fetch tweets
              # Replace with your own search query
            fetched_tweets = self.client.search_recent_tweets(query=query, tweet_fields=['context_annotations'], max_results=count)
            
            if fetched_tweets.meta['result_count'] < 1:
                return [], 0, 0, 0
            else:
                # parsing tweets one by one
                for tweet in fetched_tweets.data:
                    # empty dictionary to store required params of a tweet
                    parsed_tweet = {}
    
                    # saving text of tweet
                    parsed_tweet['text'] = tweet.text
                    # saving sentiment of tweet
                    parsed_tweet['sentiment_score'] = self.get_tweet_sentiment(tweet.text)
    
                    # appending parsed tweet to tweets list
                    tweets.append(parsed_tweet)
    
                # return parsed tweets
                return self.get_results(tweets)
  
        except tweepy.TweepyException as e:
            # print error (if any)
            print("Error : " + str(e))
        