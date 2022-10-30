from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ...db import SessionLocal
from ..repositories import medication as crud
from ..schemas.medication import MedicationSchemaCreate, MedicationSchema

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=MedicationSchema)
def create_medication(
        medication: MedicationSchemaCreate, db: Session = Depends(get_db)):
    db_medication = crud.get_medication_by_name(db, name=medication.name)
    if db_medication:
        raise HTTPException(
            status_code=400, detail="Medication already registered")
    return crud.create_medication(db=db, medication=db_medication)
