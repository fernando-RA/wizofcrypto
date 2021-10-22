import logging
from celery.schedules import crontab_parser
from backend.celery import app

from telegram.bot import send_random_message

def return_3 ():
        return 3

@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    logging.info('estou configurando')
    # Calls test('hello') every 10 seconds.
    # sender.add_periodic_task(30.0, get_notifications_profiles.s(), name='add every 30')

    # Calls test('world') every 30 seconds
    # sender.add_periodic_task(30.0, get_notifications_profiles.s('world'), expires=10)
   
    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        30.0, send_random_message(), expires=10,
    )
    
    sender.add_periodic_task(
        crontab_parser(hour=7, minute=30, day_of_week=1),
        return_3(),
    )