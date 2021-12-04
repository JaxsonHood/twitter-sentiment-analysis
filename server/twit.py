import re
import tweepy
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
    
    def tweet_analysis(self, text):
        results = self.analyzer.polarity_scores(text)
        return results
    
    def get_results(self, tweets):
        compounded_score = 0
        size = len(tweets)
        
        for tweet in tweets:
            score = tweet['analysis']['compound']
            compounded_score += score
            
        avg_score = round((compounded_score / size), 4)
        overall_sentiment = "neutral"
        
        if avg_score >= 0.05:
            overall_sentiment = "positive"
        if avg_score <= -0.05:
            overall_sentiment = "negative"
                
        
        return tweets, avg_score, overall_sentiment, size
            
  
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
                    parsed_tweet['analysis'] = self.tweet_analysis(tweet.text)
    
                    # appending parsed tweet to tweets list
                    tweets.append(parsed_tweet)
    
                # return parsed tweets
                return self.get_results(tweets)
  
        except tweepy.TweepyException as e:
            # print error (if any)
            print("Error : " + str(e))
        