from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.services.medication import MedicationService as medication_service
from app.api.schemas import MedicationSchemaCreate, MedicationSchema

router = APIRouter()


@router.post("/", response_model=MedicationSchema, status_code=201)
def create_medication(medication: MedicationSchemaCreate):
    db_medication = medication_service.get_by_name(name=medication.name)
    if db_medication:
        raise HTTPException(
            status_code=400, detail="Medication already registered")
    return medication_service.create(medication=medication)


@router.get('/', response_model=List[MedicationSchema])
def get_medications():
    return medication_service.get_all()


@router.get('/{medication_id}')
def get_medication(medication_id: int,):
    return medication_service.get(medication_id)
