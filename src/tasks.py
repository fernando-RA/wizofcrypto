from src.telegram.bot import send_random_message
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()


@sched.scheduled_job('cron', hour=7, minute=30)
def scheduled_job():
    send_random_message()


sched.start()
