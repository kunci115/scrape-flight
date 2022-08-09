# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class FlightcrawlerPipeline:
    def __init__(self):
        self.con = sqlite3.connect("db.sqlite3")
        self.cur = self.con.cursor()

    def process_item(self, item, spider):
        self.cur.execute("""insert into flight (id, flight_number, arrival_status, late_status, flight_departure_ts, actual_departure_ts,
                    terminal_departure, gate_departure, sc_airport_arrival_id, flight_arrival_ts, actual_arrival_ts,
                    terminal_arrival, created_ts, last_updated_ts, airline_id, airport_departure_id, country_arrival_id,
                    country_departure_id)
values (item['flight_number'], item['arrival_status'], item['late_status'], item['flight_departure_timestamp']);""")
        return item
