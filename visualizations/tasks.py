from __future__ import absolute_import, unicode_literals
from django.core import management

from celery import shared_task


@shared_task()
def synchronize_every_day():
    print("This is running every midnight!")
    management.call_command('synchronize')