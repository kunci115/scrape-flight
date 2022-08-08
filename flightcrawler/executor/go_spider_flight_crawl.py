from multiprocessing import Queue, Process
from flightcrawler.spiders.example import FlightSpider
from scrapy import crawler
from twisted.internet import reactor


def run_spider(spider):
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

run_spider(FlightSpider)