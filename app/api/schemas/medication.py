from typing import Optional
from pydantic import BaseModel


class MedicationSchemaBase(BaseModel):
    name: str
    weight: float
    code: str
    image: Optional[str]
    drone_id: Optional[int]

    class Config:
        orm_mode = True


class MedicationSchemaCreate(MedicationSchemaBase):
    pass


class MedicationSchema(MedicationSchemaBase):
    id: int

    class Config:
        orm_mode = True
