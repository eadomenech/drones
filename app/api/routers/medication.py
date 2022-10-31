from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from ..repositories import medication as service
from ..schemas.medication import MedicationSchemaCreate, MedicationSchema

router = APIRouter()


@router.post("/", response_model=MedicationSchema)
def create_medication(
    medication: MedicationSchemaCreate, db: Session = Depends(get_db)):
    db_medication = service.get_medication_by_name(db, name=medication.name)
    if db_medication:
        raise HTTPException(
            status_code=400, detail="Medication already registered")
    return service.create_medication(db=db, medication=medication, )


@router.get('/', response_model=List[MedicationSchema])
def get_medications(db: Session = Depends(get_db)):
    return service.get_medications(db)


@router.get('/{medication_id}')
def get_medication(medication_id: int, db: Session = Depends(get_db)):
    return service.get_medication(db, medication_id)
