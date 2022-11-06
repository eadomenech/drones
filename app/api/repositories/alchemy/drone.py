from sqlalchemy.orm import Session

from app.api.models import DroneModel, MedicationModel
from app.api.schemas import DroneSchemaCreate


class DroneRepository(object):

    def __init__(self):
        self.db = Session()

    def get(self, drone_id: int):
        return self.db.query(DroneModel).get(drone_id)

    def get_by_serial_number(self, serial_number: str):
        return self.db.query(DroneModel).filter(
            DroneModel.serial_number == serial_number).first()

    def medications(self, drone_id: int):
        return self.db.query(DroneModel).get(drone_id).medications

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(DroneModel).offset(skip).limit(limit).all()

    def create(self, drone: DroneSchemaCreate):
        db_drone = DroneModel(
            serial_number=drone.serial_number,
            model=drone.model,
            weight_limit=drone.weight_limit,
            battery_capacity=drone.battery_capacity,
            state=drone.state)

        self.db.add(db_drone)
        self.db.commit()
        self.db.refresh(db_drone)

        return db_drone

    def update(self, drone: DroneModel):
        self.db.add(drone)
        self.db.commit()
        self.db.refresh(drone)

        return drone