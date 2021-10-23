from datetime import datetime
from twitter.tweet_scraper import search_from_specific_user


def get_tweets():
    arr_of_vip_accs = [
        "fernand0aguilar"
    ]
    for user in arr_of_vip_accs:
        search_results = search_from_specific_user(user)
        print('search results', search_results)

def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())