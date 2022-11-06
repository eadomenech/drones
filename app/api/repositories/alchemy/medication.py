from sqlalchemy.orm import Session

from app.api.models import MedicationModel
from app.api.schemas import MedicationSchemaCreate


class MedicationRepository(object):

    def __init__(self, db: Session):
        self.db = db

    def get(self, drone_id: int):
        return self.db.query(MedicationModel).filter(
            MedicationModel.id == drone_id).first()

    def get_by_name(self, name: str):
        return self.db.query(MedicationModel).filter(
            MedicationModel.name == name).first()

    def create(self, medication: MedicationSchemaCreate):
        db_medication = MedicationModel(
            name=medication.name,
            weight=medication.weight,
            code=medication.code,
            image=medication.image
        )

        self.db.add(db_medication)
        self.db.commit()
        self.db.refresh(db_medication)

        return db_medication

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(MedicationModel).offset(skip).limit(limit).all()

    def update(self, medication: MedicationModel):
        self.db.add(medication)
        self.db.commit()
        self.db.refresh(medication)

        return medication