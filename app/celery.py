from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from shared.scheduler import beat_scheduler

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# config task schedulers
app.conf.beat_schedule = beat_scheduler
