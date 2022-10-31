from fastapi import APIRouter, HTTPException, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.db import get_db
from ..repositories import medication as crud
from ..schemas.medication import MedicationSchemaCreate, MedicationSchema

router = APIRouter()


@router.post("/", response_model=MedicationSchema)
def create_medication(
        medication: MedicationSchemaCreate, db: Session = Depends(get_db)):

    db_medication = crud.get_medication_by_name(db, name=medication.name)
    if db_medication:
        raise HTTPException(
            status_code=400, detail="Medication already registered")
    return crud.create_medication(db=db, medication=medication, )
