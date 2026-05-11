from celery import Celery

from .config import settings

app = Celery(
    "clinic-ms",
    broker=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
    backend=f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}",
)

app.autodiscover_tasks(["app.tasks.email_tasks"])
