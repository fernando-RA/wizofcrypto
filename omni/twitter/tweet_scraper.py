
# Imports
import snscrape.modules.twitter as sntwitter
import reticker

extractor = reticker.TickerExtractor()

def search_from_specific_user(user):
    maxTweets = 30
    tweets_list1 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:{}'.format(user)).get_items()):
        if i > maxTweets:
            break
        without_mentions = tweet.content.split("@", 1)[0]
        without_links = without_mentions.split("https://", 1)[0]
        extracted_tickers = extractor.extract(without_links)
        if (len(extracted_tickers) > 0):
            tweets_list1.append(extracted_tickers)  
    return tweets_list1

def search_from_search_query(search_query):
    
    tweets_list2 = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(search_query).get_items()):
        if i > 500:
            break
        tweets_list2.append(
            [tweet.date, tweet.id, tweet.content, tweet.user.username])

    # Creating a dataframe from the tweets list above
    # TODO 2 -> https://stackoverflow.com/a/66310138