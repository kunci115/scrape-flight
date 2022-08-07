import os
import time
from celery import Celery
from scrapy.crawler import CrawlerProcess
from flightcrawler.spiders import FlightSpider

celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")


@celery.task(name="flight_crawl_task")
def flight_crawl_task(flight_number, date, airline_code):
    process = CrawlerProcess()

    process.crawl(FlightSpider, flight_code="SQ", flight_number_="318", year="2022", month="8", date="6")
    process.start()
    return True
