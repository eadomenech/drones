from typing import List
from pydantic import BaseModel, Field


class Medication(BaseModel):
    id: int
    name: str
    weight: float
    code:str
    image: str
    drone_id: int

    class Config:
        orm_mode = True


class Drone(BaseModel):
    id: int
    serial_number: str = Field(..., max_length=100)
    model: str
    weight_limit: float
    battery_capacity: float
    state: str
    items: List[Medication] = []

    class Config:
        orm_mode = True
