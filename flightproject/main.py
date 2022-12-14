import logging
# from a
from celery.result import AsyncResult
from starlette.responses import JSONResponse
from subprocess import call
from scrapy.crawler import CrawlerProcess

from models.db_models import Flight
from models.model import ModelFlightStatus
from fastapi import FastAPI, Response, BackgroundTasks
from worker import flight_crawl_task
import datetime
from multiprocessing import Queue, Process
from flightcrawler.spiders.example import FlightSpider
from scrapy import crawler
from twisted.internet import reactor, defer
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise

app = FastAPI(title="Flight Status Scrapper")


async def flight_crawl(data):
    try:
        flight_number = data['flight_number']
        date = data['date']
        airline_code = data['airline_code']

        # confirm datetime
        format = '%Y-%m-%d'
        datetime_confirmation = datetime.datetime.strptime(date, format)
        confirmed_date = str(datetime_confirmation.date()).split('-')
        year = confirmed_date[0]
        month = confirmed_date[1]
        date = confirmed_date[2]
        flight_code = flight_number[:2]
        flight_number_ = flight_number[2:]

        # process.crawl(FlightSpider, flight_code="SQ", flight_number_="318", year="2022", month="8", date="6")

        # dd = await Airline.create(name="test")
        # await dd.save()
        # print(dd)
        task = flight_crawl_task.delay(flight_code, flight_number_, year, int(month), int(date))

        status = {"status": "Crawling Start",
                  "task_id": task.id}
        return status, 200

    except ValueError:
        return "Date Time Error , format YYYY-mm-dd"
    except Exception as e:
        raise e
        # return e.args, 400


@app.get('/crawl/start',
          summary="Submit every request to flight 3rd party"
          )
async def submit_api_router(req: ModelFlightStatus, resp:Response):
    data = req.dict()
    logging.info(data)
    resp_json, resp.status_code = await flight_crawl(data)
    return resp_json


@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status
    }
    return JSONResponse(result)

register_tortoise(
    app,
    db_url="postgres://postgres:1234@postgre:5432/flight_project",
    modules={"models": ["models.db_models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
