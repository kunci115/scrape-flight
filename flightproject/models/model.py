from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class ModelFlightStatus(BaseModel):
    flight_number: str = Field(None, description='Flight Number')
    date: str = Field(None, description='Date')
    airline_code: str = Field(None, description='Airline Code')
    