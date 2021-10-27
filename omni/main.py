from datetime import datetime
from twitter.tweet_scraper import search_from_specific_user
import reticker
import collections

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

extractor = reticker.TickerExtractor()

arr_of_vip_accs = [
    "PaikCapital",
    'mn_goat_trader',
    'edgarinsider',
    'GeniusTrader777'
]


SENDGRID_API_KEY = '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'
SENDGRID_SINGLE_SENDER = 'fraguilar@pm.me'


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
    print(arr_with_all_results)
    return collections.Counter(arr_with_all_results).most_common()

def prepare_email():
    top_tickers = get_tickers()[:10]
    print(top_tickers)
    html_string = '<div><h1>TOP 10</h1><ol>'

    for ticker in top_tickers:
        print(ticker)
        html_string += '<li><strong>Stock Ticker: %s</strong> <a href=https://stocktwits.com/search?q=%s>StockTwits</a> <a href=https://finance.yahoo.com/quote/%s>Yahoo Finance</a> <a href=https://stockcharts.com/h-sc/ui?s=%s>Stock Charts</a> <a href=https://www.otcmarkets.com/stock/%s/overview>OTC Makets</a></li>' % (ticker[0])
    html_string += '</ol><button href="https://buildleansaas.gumroad.com/l/FinancialFreedomWithFreelanceWriting">Get The Guide Succint Success In The Stock Market</button></div>'

    email_content = {'subject': 'Top OTC Stocks of {}'.format(
        datetime.today()), 'html': html_string}

    return email_content


def get_emails():
    # fetch product subscribers from gumroad
    # get subscribed emails
    emails = ['fraguilar@pm.me', 'fraguilar@protonmail.com',
              'fernando.aguilar@hotmail.com', 'admin@lightningleads.com', 'au.witherow@gmail.com']
    return emails()


def send_mail():
    email_content = prepare_email()
    message = Mail(
        from_email=SENDGRID_SINGLE_SENDER,
        to_emails=get_emails(),
        subject=email_content.subject,
        html_content=email_content.html)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
    return get_emails()


def cronjob():
    """
    Main cron job.
    The main cronjob to be run continuously.
    """
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    print(send_mail())
