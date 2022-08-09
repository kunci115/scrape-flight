# scrape-flight

How to use

1. Docker-compose build
2. docker-compose up
3. http://localhost:8000/crawl/start
    GET PARAM
{"flight_number": "SQ318",
 "date": "2022-08-06",
  "airline_code": "SQ"}

it will return {
    "status": "Crawling Start",
    "task_id": "450a97de-1545-4e27-aa00-a5fe9de0c903"
}
4. http://localhost:8000/tasks/f4e7c24a-a70e-4870-9c5e-daf6bf3d73fb
    it will return {
    "task_id": "f4e7c24a-a70e-4870-9c5e-daf6bf3d73fb",
    "task_status": "SUCCESS",
    "task_result": true
}


I'm still having problem with inserting scrapy to postgresql