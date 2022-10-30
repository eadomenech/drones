from sqlalchemy.orm import Session

from ..models.medication import MedicationModel
from ..schemas.medication import MedicationSchemaBase


def get_medication_by_name(db: Session, name: str):
    return db.query(MedicationModel).filter(
        MedicationModel.name == name).first()


def create_medication(db: Session, medication: MedicationSchemaBase):
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

# def create_drone_medication(
#         db: Session, item: schemas.MedicationCreate, drone_id: int):
#     db_item = models.Item(**item.dict(), drone_id=drone_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
