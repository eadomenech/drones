from typing import List, Union

from pydantic import BaseModel


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
    serial_number: str
    model: str
    weight_limit: float
    battery_capacity: float
    state: str
    items: List[Medication] = []

    class Config:
        orm_mode = True
