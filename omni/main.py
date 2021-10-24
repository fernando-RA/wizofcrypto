from datetime import datetime
from twitter.tweet_scraper import search_from_specific_user
import reticker

extractor = reticker.TickerExtractor()

arr_of_vip_accs = [
    "mn_goat_trader"
]

def get_tickers():
    arr_with_all_results = []
    for user in arr_of_vip_accs:
        search_results = extractor.extract(search_from_specific_user(user))
        print('search results', search_results)
        arr_with_all_results.push(search_results)
    # here -> #duplicates are the counts, loop through the results and find dict where the key is the tickername and the count is how many times we find it in the arr
    # after that we sort the dict by the counts and so the ones that habe highest counts goes to the top 
    # finally we send this to another function called prepare_email(ticker_scores):

def prepare_email ():
    # top otc stocks of the last 24 hours
    
    # 1. $TGGI [stocktwits] [yahoo] [stockcharts] [otcmarkets] [twitter]
    # 2. do it for the scored tickers of the day
    
    # get the guide to succinct stock market success on gumroad
    # presale item <link> | # get your referral link
    
    return

def get_emails():
    # fetch product subscribers from gumroad
    # get subscribed emails
    return

def send_mail():
    # get_emails()    
    # get tickers, prepare email, loop over emails, send them in a batch
    # sg.send()
    
    return



def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    send_mail()

