# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlightcrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    flight_number = scrapy.Field()
    airlines = scrapy.Field()
    country_departure_short = scrapy.Field()
    country_departure = scrapy.Field()
    country_arrival_short = scrapy.Field()
    country_arrival = scrapy.Field()
    arrival_status = scrapy.Field()
    late_status = scrapy.Field()
    airport_departure = scrapy.Field()
    flight_departure_date = scrapy.Field()
    scheduled_departure_time = scrapy.Field()
    flight_departure_timezone = scrapy.Field()
    actual_departure_time = scrapy.Field()
    terminal_departure = scrapy.Field()
    gate_departure = scrapy.Field()
    airport_arrival = scrapy.Field()
    flight_arrival_date = scrapy.Field()
    scheduled_arrival_time = scrapy.Field()
    flight_arrival_timezone = scrapy.Field()
    actual_arrival_time = scrapy.Field()
    terminal_arrival = scrapy.Field()
    gate_arrival = scrapy.Field()
    flight_time_total = scrapy.Field()
    flight_time_elapsed = scrapy.Field()
    flight_time_remaining = scrapy.Field()
    aircraft_code = scrapy.Field()
    aircraft_type = scrapy.Field()
