from celery import Celery

app = Celery(
    'celery_app',
    broker='amqp://guest:guest@localhost:5672',
    backend='redis://localhost:6379/0',
    include=['celery_task_app.tasks']
)
