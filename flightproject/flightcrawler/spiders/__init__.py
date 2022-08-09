# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy


class FlightSpider(scrapy.Spider):
    name = 'flights-track'

    def __init__(self, date=None,
                 flight_code=None,
                 flight_number_=None,
                 year=None,
                 month=None,
                 *args, **kwargs):
        super(FlightSpider, self).__init__(*args, **kwargs)
        self.start_urls = [f'https://www.flightstats.com/v2/flight-tracker/{flight_code}/{flight_number_}?year={year}&month={month}&date={date}']