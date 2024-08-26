from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_design_pattern.settings')
app = Celery('django_design_pattern', include=["ngr_diag_isaco_app"])
# app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.task_track_started = True


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))