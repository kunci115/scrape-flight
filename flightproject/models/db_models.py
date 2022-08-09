from enum import Enum

from tortoise import fields, models, run_async
from tortoise.contrib.pydantic import pydantic_model_creator


class Country(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    short_code = fields.CharField(max_length=10)


class Airline(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)


class Plane(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)


class Airport(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    timezone = fields.CharField(max_length=10)


class ArrivalStatus(str, Enum):
    # TODO
    Arrive = "Arrive"


class LateStatus(str, Enum):
    # TODO
    Late = "Late"


class Flight(models.Model):
    id = fields.IntField(pk=True)
    flight_number = fields.CharField(max_length=10)
    airline = fields.ForeignKeyField('models.Airline', related_name='flights')
    country_departure = fields.ForeignKeyField('models.Country', related_name='flight_departure_countries')
    country_arrival = fields.ForeignKeyField('models.Country', related_name='flight_arrival_countries')
    arrival_status = fields.CharEnumField(ArrivalStatus)  # TODO
    late_status = fields.CharEnumField(LateStatus)  # TODO
    airport_departure = fields.ForeignKeyField('models.Airport', related_name='flight_departure_airports')
    flight_departure_ts = fields.DatetimeField()
    actual_departure_ts = fields.DatetimeField()
    terminal_departure = fields.CharField(max_length=255)
    gate_departure = fields.CharField(max_length=255)
    sc_airport_arrival_id = fields.IntField()
    flight_arrival_ts = fields.DatetimeField()
    actual_arrival_ts = fields.DatetimeField()
    terminal_arrival = fields.CharField(max_length=255)
    # flight_time_total -> do we need to record this ? since this dynamic calculation (arrival_ts - now)
    plane = fields.ForeignKeyField('models.Plane', related_name='flights'),
    created_ts = fields.DatetimeField()
    last_updated_ts = fields.DatetimeField()


