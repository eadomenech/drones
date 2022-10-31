from typing import Optional
from pydantic import BaseModel


class MedicationSchemaBase(BaseModel):
    id: Optional[int]
    name: str
    weight: float
    code: str
    image: str
    drone_id: int

    class Config:
        orm_mode = True


class MedicationSchemaCreate(MedicationSchemaBase):
    pass


class MedicationSchema(MedicationSchemaBase):
    id: Optional[int]

    class Config:
        orm_mode = True
