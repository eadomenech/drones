from pydantic import BaseModel, Field

from .enums import DroneEnumModel, DroneEnumState
from typing import List, Optional


class MedicationSchemaBase(BaseModel):
    name: str
    weight: float
    code: str
    image: Optional[str]

    class Config:
        orm_mode = True


class MedicationSchemaCreate(MedicationSchemaBase):
    pass


class MedicationSchema(MedicationSchemaBase):
    id: int
    drone_id: int

    class Config:
        orm_mode = True


class DroneSchemaBase(BaseModel):
    serial_number: str = Field(..., max_length=100)
    model: DroneEnumModel
    weight_limit: float
    battery_capacity: int
    state: DroneEnumState


class DroneSchemaCreate(DroneSchemaBase):
    pass


class DroneSchema(DroneSchemaBase):
    id: int
    medications: List[MedicationSchema] = []

    class Config:
        orm_mode = True