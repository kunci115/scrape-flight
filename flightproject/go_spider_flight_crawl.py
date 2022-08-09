import sys
from multiprocessing import Queue, Process
from flightcrawler.spiders.example import FlightSpider
from scrapy import crawler
from twisted.internet import reactor


def run_spider(spider, flight_code, flight_number, year, month, date):
    def f(q, flight_code, flight_number, year, month, date):
        try:
            runner = crawler.CrawlerRunner()
            deferred = runner.crawl(spider, flight_code=flight_code, flight_number_=flight_number, year=year, month=month, date=date)
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q, flight_code, flight_number, year, month, date))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result


if __name__ == "__main__":
    flight_code = sys.argv[1]
    flight_number = sys.argv[2]
    year = sys.argv[3]
    month = sys.argv[4]
    date = sys.argv[5]
    print("in " + flight_code, flight_number, year, month, date)
    run_spider(FlightSpider, flight_code, flight_number, year, month, date)