from sqlalchemy.orm import Session

from app.api.models import MedicationModel
from ..schemas import MedicationSchemaCreate


def create_drone_medication(
        db: Session, medication: MedicationSchemaCreate, drone_id: int):

    db_medication = MedicationModel(**medication.dict(), drone_id=drone_id)

    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)

    return db_medication