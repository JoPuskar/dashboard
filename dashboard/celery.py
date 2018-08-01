from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dashboard.settings')

app = Celery('dashboard')

app.conf.broker_url = 'redis://localhost:6379/0'

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['visualizations'])

app.conf.timezone = 'Asia/Katmandu'

task_track_started = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
    print(self.AsyncResult(self.request.id).state)
