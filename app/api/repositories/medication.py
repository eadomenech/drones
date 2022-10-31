from sqlalchemy.orm import Session

from app.api.models.medication import MedicationModel
from ..schemas.medication import MedicationSchemaCreate


def get_medication(db: Session, drone_id: int):
    return db.query(MedicationModel).filter(
        MedicationModel.id == drone_id).first()


def get_medication_by_name(db: Session, name: str):
    return db.query(MedicationModel).filter(
        MedicationModel.name == name).first()


def create_medication(db: Session, medication: MedicationSchemaCreate):
    db_medication = MedicationModel(
        name=medication.name,
        weight=medication.weight,
        code=medication.code,
        image=medication.image)

    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)

    return db_medication


def get_medications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(MedicationModel).offset(skip).limit(limit).all()
