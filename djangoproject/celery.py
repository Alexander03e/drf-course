import os
from celery import Celery



os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'djangoproject.settings')

app = Celery('djangoproject', broker='redis://redis:6379/0', backend='redis://redis:6379/0')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()
app.conf.update(
  broker_connection_retry_on_startup=True,
)