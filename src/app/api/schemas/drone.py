from typing import List, Optional
from pydantic import BaseModel, Field

from .medication import MedicationSchema
from ..models.enums import DroneEnumModel, DroneEnumState


class DroneSchemaBase(BaseModel):
    serial_number: str = Field(..., max_length=100)
    model: DroneEnumModel
    weight_limit: float
    battery_capacity: int
    state: DroneEnumState
    items: List[MedicationSchema] = []


class DroneSchemaCreate(DroneSchemaBase):
    pass


class DroneSchema(DroneSchemaBase):
    id: Optional[int]

    class Config:
        orm_mode = True
