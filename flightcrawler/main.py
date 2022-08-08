import logging
# from a
from celery.result import AsyncResult
from starlette.responses import JSONResponse
from subprocess import call
from scrapy.crawler import CrawlerProcess
from models.model import ModelFlightStatus
from fastapi import FastAPI, Response, BackgroundTasks
from worker import flight_crawl_task
from multiprocessing import Queue, Process
from flightcrawler.spiders.example import FlightSpider
from scrapy import crawler
from twisted.internet import reactor, defer
app = FastAPI(title="Flight Status Scrapper")


async def flight_crawl(data):
    try:
        flight_number = data['flight_number']
        date = data['date']
        airline_code = data['airline_code']

        # process.crawl(FlightSpider, flight_code="SQ", flight_number_="318", year="2022", month="8", date="6")

        task = flight_crawl_task.delay(flight_number, date, airline_code)
        status = {"status": "Crawling Start",
                  "task_id": task.id}
        return status, 200
    except Exception as e:
        raise e
        # return e.args, 400


@app.post('/crawl/start',
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
        "task_status": task_result.status,
        "task_result": task_result.result
    }
    return JSONResponse(result)
