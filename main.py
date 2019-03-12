from fsia.tweetgatherer.TwitterClient import twitterClient
from fsia.tweetgatherer.TweetAnalyzer import tweet_analyzer
import fsia.tweetgatherer.TweetCriteria as tweet_criteria
import fsia.tweetgatherer.TweetManager as tweet_manager
import fsia.usgsgatherer.USGSFloodManager as flood_real_time
import fsia.usgsgatherer.USGSFloodCriteria as usgs_criteria
import fsia.nasagatherer.NasaManager as nasa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import sys
import datetime
import time

if __name__ == "__main__":
    nasa_manager = nasa.NasaGatherer()
    urls = []
    #urls.append("https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_VIC025_A_EA_D.001/2019/02/FLDAS_VIC025_A_EA_D.A20190201.001.nc.nc4")
    #urls.append("https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_VIC025_A_EA_D.001/2019/02/FLDAS_VIC025_A_EA_D.A20190209.001.nc.nc4")
    #urls.append("https://hydro1.gesdisc.eosdis.nasa.gov/opendap/FLDAS/FLDAS_VIC025_A_EA_D.001/2019/02/FLDAS_VIC025_A_EA_D.A20190208.001.nc.nc4")
    #nasa_manager.getNasaEarthData(urls)
    #nasa_manager.readNasaNetCDF()
    #nasa_manager.getEarthData()
    flood_manager = flood_real_time.usgsFloodManager()
    flood_criteria = usgs_criteria.usgsCriteria()
    flood_parameter = ["00065", "00045"]
    flood_criteria.setStationNumber('02169500').setParameters(flood_parameter).setSince("2019-03-01").setUntil("2019-03-05").setRegion("sc")
    flood_manager.getFloodDataCSV(flood_criteria)
    flood_manager.getImageWaterWatch("02169506")
    frames = []
    #get data from NWS 
    twitter = tweet_analyzer()
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("weatherchannel").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter.analyze_sentiment(tweet) for tweet in df['Tweets']])
    df.to_csv("flood.csv")
    time.sleep(1)
    flood_real_time = flood_manager.getRealTimeWaterWatch()
    flood_real_time.to_csv("flood-realtime.csv")

    '''
    #This is gathering tweet and USGS water data Dont delete
    twitter_client = twitterClient("weatherchannel")
    api = twitter_client.get_twitter_api()
    twitter_analyzer = tweet_analyzer()
    tweets = api.user_timeline(screen_name="weatherchannel")
    twitter_client.get_image_tweet()
    frames = []
    #get data from weather channel
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("weatherchannel").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)
    '''
    '''
    frames = []
    #get data from NWS 
    twitter = tweet_analyzer()
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("primpla").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)
    
    df = pd.concat(frames)
    df.to_csv('data_twitter.csv')
    '''
    '''
    #get data from NWSEastern ‏
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("NWSEastern‏").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)

    #get data from NWSEastern ‏
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("USGS").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)

    #get data from NWSEastern ‏
    tweeter_criteria = tweet_criteria.TweetCriteria()
    tweeter_criteria.setUsername("NHC_Atlantic").setSince("2018-09-07").setUntil("2018-10-7").setMaxTweets(10000)
    tweet = tweet_manager.TweetManager.getTweets(tweeter_criteria)
    df = twitter_analyzer.tweets_to_dataframe(tweet)
    df['sentiment'] = np.array([twitter_analyzer.analyze_sentiment(tweet) for tweet in df['Tweets']])
    frames.append(df)
    time.sleep(1)
    df = pd.concat(frames)
    df.to_csv('data_twitter.csv')
    '''
    '''
    flood_real_time = flood_real_time.usgsFloodRealTime()
    df = pd.DataFrame(flood_real_time.getWaterWatch())
    df['flow_dt'] = pd.to_datetime(df['flow_dt'])
    df.sort_values('flow_dt')
    i = 0
    frames = []
    frames.append(df)
    #time.sleep(15*60)
    while i <= 192:
        temp_df = pd.DataFrame(flood_real_time.getWaterWatch())
        frames.append(temp_df)
        time.sleep(15*60)
        i = i+1
    df = pd.concat(frames)
    df.to_csv('flood.csv')
    
    flood_real_time = flood_real_time.usgsFloodRealTime()
    flood_real_time.getImageWaterWatch()
    time.sleep(1)

    '''


