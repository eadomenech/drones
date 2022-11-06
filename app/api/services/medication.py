from app.api.models import MedicationModel
from app.api.schemas import MedicationSchemaCreate
from app.api.repositories.alchemy.medication import MedicationRepository


class MedicationService(object):

    def __init__(self):
        self.repository = MedicationRepository()

    def get(self, drone_id: int):
        return self.repository.get(drone_id)

    def get_by_name(self, name: str):
        return self.repository.get_by_name(name)

    def create(self, medication: MedicationSchemaCreate):
        return self.repository.create(medication)

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.repository.medication_repository.get_all(skip, limit)

    def update(self, medication: MedicationModel):
        return self.repository.update(medication)
