import os
from subprocess import call

from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


def crawl():
    filename = "go_spider_flight_crawl.py"
    return call(["python", filename])


@celery.task(name="flight_crawl_task")
def flight_crawl_task(flight_number, date, airline_code):
    crawl()
    return True
