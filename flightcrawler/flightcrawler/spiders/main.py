from scrapy.settings import Settings

from example import FlightSpider
from scrapy.crawler import CrawlerProcess
process = CrawlerProcess(settings={
    # "FEEDS": {
    #     "items.json": {"format": "json"},
    # },
})

process.crawl(FlightSpider)
process.start()