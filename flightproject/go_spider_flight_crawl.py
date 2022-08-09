import sys
from multiprocessing import Queue, Process
from flightcrawler.spiders.example import FlightSpider
from scrapy import crawler
from twisted.internet import reactor


def run_spider(spider, flight_code, flight_number, year, month, date):
    def f(q):
        try:
            runner = crawler.CrawlerRunner()
            deferred = runner.crawl(spider, flight_code="SQ", flight_number_="318", year="2022", month="8", date="6")
            deferred.addBoth(lambda _: reactor.stop())
            reactor.run()
            q.put(None)
        except Exception as e:
            q.put(e)

    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    result = q.get()
    p.join()

    if result is not None:
        raise result


if __name__ == "__main__":
    flight_code = sys.argv[1]
    flight_number = sys.argv[2]
    year = sys.argv[2]
run_spider(FlightSpider)