from pydantic import BaseModel, Field

from ..enums import DroneEnumModel, DroneEnumState


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

    class Config:
        orm_mode = True
