from apscheduler.schedulers.blocking import BlockingScheduler

# Main cronjob function.
from main import cronjob

# Create an instance of scheduler and add function.
scheduler = BlockingScheduler()
scheduler.add_job(cronjob, trigger='cron', hour='08', minute='45')

scheduler.start()