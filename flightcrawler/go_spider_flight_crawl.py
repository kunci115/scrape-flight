import logging
# from a
from flightcrawler.spiders.example import FlightSpider
from scrapy.crawler import CrawlerProcess
process = CrawlerProcess()

process.crawl(FlightSpider, flight_code="SQ", flight_number_="318", year="2022", month="8", date="6")
process.start()