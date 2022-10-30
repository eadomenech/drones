from typing import List, Optional
from pydantic import BaseModel, Field

from .medication import MedicationSchema


class DroneSchemaBase(BaseModel):
    serial_number: str = Field(..., max_length=100)
    model: str
    weight_limit: float
    battery_capacity: int
    state: str
    # items: List[MedicationSchema] = []

class DroneSchemaCreate(DroneSchemaBase):
    pass

class DroneSchema(DroneSchemaBase):
    id: Optional[int]

    class Config:
        orm_mode = True
