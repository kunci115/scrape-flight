from enum import Enum

from tortoise import fields, models, run_async
from tortoise.contrib.pydantic import pydantic_model_creator

class Flight(models.Model):
    id = fields.IntField(pk=True)
    flight_number = fields.CharField(max_length=10)
    airline = fields.CharField(max_length=255)
    country_departure = fields.CharField(max_length=255)
    country_departure_sc = fields.CharField(max_length=10)
    country_arrival = fields.CharField(max_length=255)
    arrival_status = fields.CharField(max_length=50)  # TODO
    late_status = fields.CharField(max_length=50)  # TODO
    airport_departure = fields.CharField(max_length=255)
    flight_departure_timezone = fields.CharField(max_length=25)
    flight_departure_date = fields.CharField(max_length=255)
    scheduled_departure_time = fields.CharField(max_length=255)
    scheduled_arrival_time = fields.CharField(max_length=255)
    actual_departure_time = fields.CharField(max_length=30)
    actual_arrival_time = fields.CharField(max_length=255)
    terminal_departure = fields.CharField(max_length=255)
    gate_departure = fields.CharField(max_length=255)
    gate_arrival = fields.CharField(max_length=255)
    flight_arrival_timezone = fields.CharField(max_length=25)
    flight_arrival_date = fields.CharField(max_length=255)
    flight_arrival_time = fields.CharField(max_length=255)
    terminal_arrival = fields.CharField(max_length=255)
    flight_time_total = fields.CharField(max_length=255)
    flight_time_elapsed = fields.CharField(max_length=255)
    flight_time_remaining = fields.CharField(max_length=255)
    plane_code = fields.CharField(max_length=255),
    plane_type = fields.CharField(max_length=255)
    created_ts = fields.DatetimeField()
    last_updated_ts = fields.DatetimeField()


