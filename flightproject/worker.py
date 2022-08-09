import os
from subprocess import call

from celery import Celery

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


def crawl(flight_code, flight_number_, year, month, date):
    filename = "go_spider_flight_crawl.py"
    to_month = str(int(month))
    to_date = str(int(date))
    new_month = to_month
    new_date = to_date
    try:
        # print(call(["python", filename, " ", flight_code, " ", flight_number_, " " , year , " ", str(to_month), " ", str(to_date)]))
        return call(["python", filename, flight_code, flight_number_, year , new_month, new_date])
    except Exception as e:
        print(e)

@celery.task(name="flight_crawl_task")
def flight_crawl_task(flight_code, flight_number_, year, month, date):
    try:
        crawl(flight_code, flight_number_, year, month, date)
        return True
    except Exception as e:
        print("on flight crawl task")
        print(e)