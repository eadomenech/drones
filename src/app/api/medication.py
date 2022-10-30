from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ..db import SessionLocal
from ..api import crud
from ..api.schemas import Medication

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=Medication)
def create_medication(
        medication: Medication, db: Session = Depends(get_db)):
    db_medication = crud.get_medication_by_name(db, name=medication.name)
    if db_medication:
        raise HTTPException(
            status_code=400, detail="Medication already registered")
    return crud.create_medication(db=db, medication=db_medication)
