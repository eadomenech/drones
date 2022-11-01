from typing import Optional
from pydantic import BaseModel

from .drone import DroneSchema


class MedicationSchemaBase(BaseModel):
    name: str
    weight: float
    code: str
    image: Optional[str]
    drone: Optional[DroneSchema]

    class Config:
        orm_mode = True


class MedicationSchemaCreate(MedicationSchemaBase):
    pass


class MedicationSchema(MedicationSchemaBase):
    id: int

    class Config:
        orm_mode = True
