
# Imports
import snscrape.modules.twitter as sntwitter
import reticker

extractor = reticker.TickerExtractor()

def search_from_specific_user(user):
    maxTweets = 20
    tweets_list1 = []
    print(user)
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{user}').get_items()):
        if i > maxTweets:
            break
        without_mentions = tweet.content.split("@", 1)[0]
        without_links = without_mentions.split("https://", 1)[0]
        extracted_tickers = extractor.extract(without_links)
        if (len(extracted_tickers) > 0):
            tweets_list1.append(extracted_tickers)
    return tweets_list1