from datetime import datetime
from twitter.tweet_scraper import search_from_specific_user
import reticker
import collections

extractor = reticker.TickerExtractor()

arr_of_vip_accs = [
    "fernand0aguilar",
    "PaikCapital",
]


def count_duplicates(arr):
    count = {}
    for i in arr:
        if not i in count:
            count[i] = 1
        else:
            count[i] += 1
    return count


def get_tickers():
    arr_with_all_results = []
    for user in arr_of_vip_accs:
        for tweet in search_from_specific_user(user):
            for ticker in tweet:
                arr_with_all_results.append(ticker)
    return collections.Counter(arr_with_all_results).most_common()
    # [('ONE', 4), ('FTM', 3), ('LUNA', 2), ('AVAX', 2), ('SOL', 2), ('SPELL', 2), ('TEST', 1), ('THIS', 1), ('JUST', 1), ('TESTIN', 1), ('CRV', 1), ('GYRO', 1), ('GN', 1), ('GM', 1), ('ETH', 1), ('AXS', 1), ('BTC', 1), ('SYN', 1), ('JOE', 1), ('SCRT', 1), ('ALL', 1), ('TIME', 1), ('HIGHS', 1)]


def prepare_email():
    # top otc stocks of the last 24 hours

    # 1. $TGGI [stocktwits] [yahoo] [stockcharts] [otcmarkets] [twitter]
    # 2. do it for the scored tickers of the day

    # get the guide to succinct stock market success on gumroad
    # presale item <link> | # get your referral link\
    tickers_dict = [{
        'name': t[0],
        'score': t[1],
        "stocktwits": 'https://stocktwits.com/search?q=' + t[0],
        "yahoo": 'https://finance.yahoo.com/quote/' + t[0],
        "stockcharts": 'https://stockcharts.com/h-sc/ui?s=' + t[0],
        "otcmarkets": f'https://www.otcmarkets.com/stock/{t[0]}/overview',
    } for t in get_tickers()]

    return tickers_dict


def get_emails():
    # fetch product subscribers from gumroad
    # get subscribed emails
    return prepare_email()


def send_mail():
    # get_emails()
    # get tickers, prepare email, loop over emails, send them in a batch
    # sg.send()

    return get_emails()


def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    print(send_mail())
