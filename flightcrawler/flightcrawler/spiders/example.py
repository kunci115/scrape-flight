import scrapy
import json

class FlightSpider(scrapy.Spider):
    name = 'flights-track'

    def start_requests(self):
        urls = [
            'https://www.flightstats.com/v2/flight-tracker/SQ/318?year=2022&month=8&date=6'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        flight_s = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "crILdr", " " ))]//text()').getall()
        flight_t = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "exDPyn", " " ))]//text()').getall()
        flight_number = flight_s[0]
        airlines = flight_s[1]
        country_departure_short = flight_s[2]
        country_departure = flight_s[3]

        country_arrival_short = flight_s[4]
        country_arrival = flight_s[5]

        arrival_status = flight_s[6]

        late_status = flight_s[7]

        airport_departure = flight_s[10]
        flight_departure_date = flight_s[12]
        scheduled_departure_time = flight_s[14]
        flight_departure_timezone = flight_s[15]
        actual_departure_time = flight_s[17]
        terminal_departure = flight_s[20]
        gate_departure = flight_s[22]

        airport_arrival = flight_s[25]
        flight_arrival_date = flight_s[27]
        scheduled_arrival_time = flight_s[29]
        flight_arrival_timezone = flight_s[30]
        actual_arrival_time = flight_s[32]
        terminal_arrival = flight_s[37]
        # gate_arrival = flight_s[38]

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
            # "gate_arrival": gate_arrival
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
        json_object = json.dumps(data_return, indent=4)
        with open(f'result.json', 'w' )as f:
            f.write(json_object)
        # scheduled_arrival = flight_s[6]
        # actual_arrival = flight_s[8]
        # terminal_arrival = flight_s[10]
        # gate_arrival = flight_s[11]


            # print(flight_s)
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)