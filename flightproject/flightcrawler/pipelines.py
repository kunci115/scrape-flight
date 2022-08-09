# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2
from spiders.example import FlightSpider
# useful for handling different item types with a single interface
import sqlite3

from itemadapter import ItemAdapter


class FlightcrawlerPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '1234'  # your password
        database = 'flight_project'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        # self.cur.execute("""insert into flight(id, flight_number, arrival_status, late_status, flight_departure_ts, actual_departure_ts) values ( ((select max(id)+1 from flight), ?, ?, ?, ?;""", )
        # airline_id = self.cur.execute("""insert into airline(name) values (?) returning id""", (item['airlines'])).fetchone()
        self.cur.execute("""insert into flight(flight_number, airline, country_departure, country_departure_sc, country_arrival, country_arrival_short_code, arrival_status, late_status, airport_departure, flight_departure_timezone, flight_departure_date,scheduled_departure_time, scheduled_arrival_time,
                            actual_departure_time, actual_arrival_time, terminal_departure, terminal_arrival, gate_departure, gate_arrival, flight_arrival_timezone, flight_arrival_date, flight_arrival_time, terminal_arrival, flight_time_total, flight_time_elapsed,
                             flight_time_remaining, plane_code, plane_type, created_ts, last_updated_ts) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (item['flight_number'],
                                                                                                                                                                               item['airlines'],
                                                                                                                                                                               item['country_departure'],
                                                                                                                                                                               item['country_departure_short_code'],
                                                                                                                                                                               item['country_arrival'],
                                                                                                                                                                               item['country_arrival_short_code'],
                                                                                                                                                                               item['arrival_status'],
                                                                                                                                                                               item['late_status'],
                                                                                                                                                                               item['airport_departure'],
                                                                                                                                                                               item['flight_departure_timezone'],
                                                                                                                                                                               item['flight_departure_date'],
                                                                                                                                                                               item['scheduled_departure_time'],
                                                                                                                                                                               item['scheduled_arrival_time'],
                                                                                                                                                                               item['actual_departure_time'],
                                                                                                                                                                               item['actual_arrival_time'],
                                                                                                                                                                               item['terminal_departure'],
                                                                                                                                                                               item['terminal_arrival'],
                                                                                                                                                                               item['gate_departure'],
                                                                                                                                                                               item['gate_arrival'],
                                                                                                                                                                               item['flight_arrival_timezone'],
                                                                                                                                                                               item['flight_arrival_date'],
                                                                                                                                                                               item['scheduled_arrival_time'],
                                                                                                                                                                               item['terminal_arrival'],
                                                                                                                                                                               item['flight_time_total'],
                                                                                                                                                                               item['flight_time_elapsed'],
                                                                                                                                                                               item['flight_time_remaining'],
                                                                                                                                                                               item['plane_code'],
                                                                                                                                                                               item['plane_time'],
                                                                                                                                                                               item['created_ts'],
                                                                                                                                                                               item['last_updated_ts']))
        self.connection.commit()
        print("DB")
        return item
