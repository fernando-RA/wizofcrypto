#!/usr/bin/python
import tweepy
import os


# class MyStreamListener(tweepy.StreamListener):
#     def on_status(self, status):
#         print(status.text)

lists = {
    "crypto": 1444390297354579969,
    "copywriting": 1444392734178037769,
    "dev": 1444390772359540739,
    "design": 1444391796587511813,
    "esports": 1444392326210768906,
    "marketing": 1444392521837293573,
    "system_design": 1444394085511487491,
    "memes": 1444390445996552198,
    "mindset": 1444392576673591303,
    "otc": 1444392646961770499,
    "stocks": 1444392965183528960,
}


# myStreamListener = MyStreamListener()
# myStream = tweepy.Stream(auth=tweepy.OAuthHandler(
#     os.getenv.TWITTER_CONSUMER_TOKEN, os.getenv.TWITTER_CONSUMER_SECRET), listener=myStreamListener())

auth = tweepy.OAuthHandler(
    os.getenv("TWITTER_CONSUMER_TOKEN"), os.getenv("TWITTER_CONSUMER_SECRET"))


def get_user_lists():
    return tweepy.api.get_lists(screen_name="vacentralorg")
