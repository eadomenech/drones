from pydantic import BaseModel, Field, validator

from .enums import DroneEnumModel, DroneEnumState
from typing import List, Optional


class MedicationSchemaBase(BaseModel):
    name: str = Field(regex="^[A-Za-z0-9_-]+$")
    weight: float
    code: str
    image: Optional[str]

    class Config:
        orm_mode = True


class MedicationSchemaCreate(MedicationSchemaBase):
    pass


class MedicationSchema(MedicationSchemaBase):
    id: int
    drone_id: Optional[int]

    class Config:
        orm_mode = True


class DroneSchemaBase(BaseModel):
    serial_number: str = Field(..., max_length=100)
    model: DroneEnumModel
    weight_limit: float = 500.0
    battery_capacity: int = 100
    state: DroneEnumState
    charging: bool = False

    @validator("weight_limit")
    def weight_limit_must_be_less_tham_500(cls, value):
        if float(value) > 500.0:
            raise ValueError(
                f"we expect weight limit <= 500.0, we received {value}")
        return value

    @validator("battery_capacity")
    def battery_capacity_between_0_100(cls, value):
        if value < 0 or value > 100:
            raise ValueError(
                f"we expect a value between 0 and 100, we received {value}")
        return value


class DroneSchemaCreate(DroneSchemaBase):
    pass


class DroneSchema(DroneSchemaBase):
    id: int
    medications: List[MedicationSchema] = []

    class Config:
        orm_mode = True
