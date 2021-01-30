import os
from celery import Celery

BROKER_URI = os.environ['BROKER_URI']
BACKEND_URI = os.environ['BACKEND_URI']

app = Celery(
    'celery_app',
    broker=BROKER_URI,
    backend=BACKEND_URI,
    include=['celery_task_app.tasks']
)
