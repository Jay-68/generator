from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# sets the default django settings module for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'generator.settings')

app = Celery('generator')

# Ensures I don't touch the configuration settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from django apps
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request:{self.request!r}')
