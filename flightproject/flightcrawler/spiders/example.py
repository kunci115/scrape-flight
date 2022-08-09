import scrapy
import json
import sys
sys.path.append("..")


class FlightSpider(scrapy.Spider):
    name = 'flights-track'


    def start_requests(self):
        # 'https://www.flightstats.com/v2/flight-tracker/SQ/318?year=2022&month=8&date=6'
        urls = [f'https://www.flightstats.com/v2/flight-tracker/{self.flight_code}/{self.flight_number_}?year={self.year}&month={self.month}&date={self.date}']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        flight_t = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "exDPyn", " " ))]//text()').getall()
        flight_number = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[0].get()
        airlines = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[1].get()
        country_departure_short = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[2].get()
        country_departure = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[3].get()

        country_arrival_short = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[4].get()
        country_arrival = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[5].get()

        arrival_status = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[6].get()

        late_status = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[7].get()

        airport_departure = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[10].get()
        flight_departure_date = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[12].get()
        scheduled_departure_time = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[14].get()
        flight_departure_timezone = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[15].get()
        actual_departure_time = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[17].get()
        terminal_departure = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[20].get()
        gate_departure = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[22].get()

        airport_arrival = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[25].get()
        flight_arrival_date = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[27].get()
        scheduled_arrival_time = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[29].get()
        flight_arrival_timezone = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[30].get()
        actual_arrival_time = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[32].get()
        terminal_arrival = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[35].get()
        gate_arrival = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()')[37].get()

        flight_time_total = flight_t[0]
        flight_time_elapsed = flight_t[1]
        flight_time_remaining = flight_t[2]

        aircraft_code = flight_t[31]
        aircraft_type = flight_t[32]
        flight_status = {
            "flight_number": flight_number,
            "airlines": airlines,
            "country_departure_short_code": country_departure_short,
            "country_departure": country_departure,
            "country_arrival_short_code": country_arrival_short,
            "country_arrival": country_arrival,
            "arrival_status": arrival_status,
            "late_status": late_status,
            "airport_departure": airport_departure,
            "flight_departure_date": flight_departure_date,
            "scheduled_departure_time": scheduled_departure_time,
            "flight_departure_timezone": flight_departure_timezone,
            "actual_departure_time": actual_departure_time,
            "terminal_departure": terminal_departure,
            "gate_departure": gate_departure,
            "airport_arrival": airport_arrival,
            "flight_arrival_date": flight_arrival_date,
            "scheduled_arrival_time": scheduled_arrival_time,
            "flight_arrival_timezone": flight_arrival_timezone,
            "actual_arrival_time": actual_arrival_time,
            "terminal_arrival": terminal_arrival,
            "gate_arrival": gate_arrival
        }
        flight_time = {
            "total": flight_time_total,
            "elapsed": flight_time_elapsed,
            "remaining": flight_time_remaining
        }
        additional_details = {
            "code": aircraft_code,
            "type": aircraft_type
        }

        data_return = {"flight_status": flight_status,
                       "flight_time": flight_time,
                       "additional_details": additional_details}


        # flight = Flight.create(flight_number=flight_number, airlines=airlines, country_departure=country_departure,
        #               country_departure_short=country_departure_short, country_arrival=country_arrival,
        #               country_arrival_short=country_arrival_short, arrival_status=arrival_status,
        #               late_status=late_status, airport_departure=airport_departure,
        #               flight_departure_date=flight_departure_date, scheduled_departure_time=scheduled_departure_time,
        #               actual_departure_time=actual_departure_time, actual_arrival_time=actual_arrival_time,
        #               terminal_departure=terminal_departure, terminal_arrival=terminal_arrival, gate_departure=gate_departure,
        #               gate_arrival=gate_arrival, airport_arrival=airport_arrival, flight_arrival_date=flight_arrival_date,
        #               scheduled_arrival_time=scheduled_arrival_time
        #               )
        # if flight:
        #     print("@@@")
        json_object = json.dumps(data_return, indent=4)
        with open(f'result.json', 'w' )as f:
            f.write(json_object)
        return data_return
