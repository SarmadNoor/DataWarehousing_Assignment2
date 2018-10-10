import tweepy
import csv
import sys

non_bmp_map=dict.fromkeys(range(0x10000,sys.maxunicode + 1),0xfffd)

def get_tweets(query):
    for tweet in tweepy.Cursor(api.search, q=query ,lang="en").items(1000):
        yield tweet
query="Halifax -filter:retweets"

consumer_key="fXroz6jlsHzWKwAwTWgUktFwe"
consumer_secret="QDf95aZVIesdY6bsMa0YuZBpCGCJYY31LLAU9kWQLaSJB8KlqO"
access_token="1047123042294542337-J7k1OV1XHLZdbbanbYV09AcNDT7m1L"
access_token_secret="AzBf8GF6jqbhf76xa5RSVcs38aCovYhQLRpvMq2n5s8iU"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

with open ('tweets.csv','w',encoding='utf-8') as extractedTweet:
    writer = csv.writer(extractedTweet)
    writer.writerow(['Tweet'])
    tweets=get_tweets(query)
    for tweet in tweets:
       writer.writerow([tweet.text.translate(non_bmp_map)])


