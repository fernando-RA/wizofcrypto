import os
from celery.schedules import crontab    
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")

app = Celery('celery_config')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()