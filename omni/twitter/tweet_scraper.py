
# Imports
import snscrape.modules.twitter as sntwitter
import pandas as pd

# Below are two ways of scraping using the Python Wrapper.
# Comment or uncomment as you need. If you currently run the script as is it will scrape both queries
# then output two different csv files.

# Query by username
# Setting variables to be used below


def search_from_specific_user(user):
    maxTweets = 3000

    # Creating list to append tweet data to
    tweets_list1 = []

    # Using TwitterSearchScraper to scrape data
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:fernand0aguilar').get_items()):
        if i > maxTweets:
            break
        without_mentions = tweet.content.split("@", 1)[0]
        without_links = without_mentions.split("https://", 1)[0]
        tweets_list1.append([without_links])

    # Creating a dataframe from the tweets list above
    tweets_df1 = pd.DataFrame(tweets_list1, columns=['Tweet Content'])

    # Display first 5 entries from dataframe
    tweets_df1.head()

    # Export dataframe into a CSV
    tweets_df1.to_csv('user-tweets.csv', sep=';', index=False)


def search_from_search_query(search_query):
    # Creating list to append tweet data to
    tweets_list2 = []

    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('its the elephant since:2020-06-01 until:2020-07-31').get_items()):
        if i > 500:
            break
        tweets_list2.append(
            [tweet.date, tweet.id, tweet.content, tweet.user.username])

    # Creating a dataframe from the tweets list above
    tweets_df2 = pd.DataFrame(tweets_list2, columns=[
                            'Datetime', 'Tweet Id', 'Text', 'Username'])
