
# Imports
import snscrape.modules.twitter as sntwitter

def search_from_specific_user(user):
    maxTweets = 100

    # Creating list to append tweet data to
    tweets_list1 = []
    print('here')
    # Using TwitterSearchScraper to scrape data
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(user)).get_items()):
        if i > maxTweets:
            break
        without_mentions = tweet.content.split("@", 1)[0]
        without_links = without_mentions.split("https://", 1)[0]
        tweets_list1.append([without_links])

    # Creating a dataframe from the tweets list above
    return tweets_list1
    # TODO ->     https://stackoverflow.com/a/41786472

def search_from_search_query(search_query):
    
    tweets_list2 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query).get_items()):
        if i > 500:
            break
        tweets_list2.append(
            [tweet.date, tweet.id, tweet.content, tweet.user.username])

    # Creating a dataframe from the tweets list above
    # TODO 2 -> https://stackoverflow.com/a/66310138