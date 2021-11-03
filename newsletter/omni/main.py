from datetime import datetime
from twitter.tweet_scraper import search_from_specific_user
import reticker
import collections
import sys
import requests

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Personalization, Email, Content, To, From

extractor = reticker.TickerExtractor()

arr_of_vip_accs = [
    'edgarinsider',
    'GeniusTrader777',
    'stockballa',
    'ClairvoyantINVT',
    'WhalePenny',
    'SaraGoingUp',
    'Jcazz17',
    'greatstockpicks',
    'FatCash7',
    'ArrrgToTheMoon',
    'TESLAQUEEN10',
    'JohnRSpano1',
    'ecgreendays',
    'AngryRed316'
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
    print('arr_with_all_results',arr_with_all_results)
    return collections.Counter(arr_with_all_results).most_common()


def prepare_email():
    top_tickers = get_tickers()[:10]
    html_string = '<div><h1>TOP 10</h1><ol>'
    for ticker in top_tickers:
        html_string += f'<li><strong>Ticker: {ticker[0]}</strong> <ul><li><a href=https://stocktwits.com/search?q={ticker[0]}>StockTwits</a></li> <li><a href=https://finance.yahoo.com/quote/{ticker[0]}>Yahoo Finance</a></li> <li><a href=https://stockcharts.com/h-sc/ui?s={ticker[0]}>Stock Charts</a></li> <li><a href=https://www.otcmarkets.com/stock/{ticker[0]}/overview>OTC Makets</a></li></ul></li>'
    html_string += '</ol><a href="https://buildleansaas.gumroad.com/l/FinancialFreedomWithFreelanceWriting">Get The Guide Succint Success In The Stock Market</a></div>'

    email_content = {'subject': 'Top OTC Stocks of {}'.format(
        datetime.today()), 'html': Content("text/html", html_string)}

    return email_content


def get_emails():
    emails = [To('fraguilar@pm.me'), To('fraguilar@protonmail.com'),
              To('fernando.aguilar@hotmail.com.br'), To('admin@lightningleads.co'), To('au.witherow@gmail.com')]
    
    url_endpoint = f'https://api.gumroad.com/v2/products/{GUMROAD_PRODUCT_ID}/subscribers'
    subscibers = requests.get(url_endpoint, params={"access_token":GUMROAD_API_KEY}).json().get('subscribers')
    for subscriber in subscibers:
        emails.append(subscriber.get('email'))
    
    print('subs', emails)
    
    return emails


def send_mail():
    email_content = prepare_email()
    message = Mail(
        from_email=From(SENDGRID_SINGLE_SENDER, "FRAG"),
        to_emails=get_emails(),
        subject=email_content['subject'],
        html_content=email_content['html'],
        is_multiple=True
    )
    try:
        print('sending email', email_content)
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.client.mail.send.post(request_body=message.get())
        print('EMAIL SENT', response)
    except Exception as e:
        print('Error sending email')
        print(e)


def cronjob():
    print("Cron job is running")
    print("Tick! The time is: %s" % datetime.now())
    send_mail()

cronjob()