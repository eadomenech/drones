from typing import List

from app.api.schemas import DroneSchemaCreate
from app.api.models import DroneModel
from app.api.enums import DroneEnumState
from app.api.repositories.alchemy.drone import DroneRepository
from .medication import MedicationService


class DroneService(object):

    def __init__(self):
        self.drone_repository = DroneRepository()
        self.medication_service = MedicationService()

    def get(self, drone_id: int):
        return self.drone_repository.get_drone(drone_id)

    def get_by_serial_number(self, serial_number: str):
        return self.drone_repository.get_drone_by_serial_number(serial_number)

    def medications(self, drone_id: int):
        return self.drone_repository.medications(drone_id)

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.drone_repository.get_drones(skip, limit)

    def create(self, drone: DroneSchemaCreate):
        return self.drone_repository.create_drone(drone)

    def loading(self, drone_id: int, medications: List[int]):
        errors = list()
        db_drone = self.get_drone(drone_id)

        if not db_drone:
            errors.append("Drone not found")

        total_weight = 0.0
        for medication_id in medications:
            db_medication = self.medication_service.get(medication_id)
            total_weight += db_medication.weight

        if total_weight > db_drone.weight_limit:
            errors.append("Weight limit exceeded")

        for medication_id in medications:
            db_medication = self.medication_service.get(medication_id)
            db_medication.drone_id = drone_id
            self.medication_service.update(db_medication)

        db_drone.state = 'LOADING'

        return {
            'success': len(errors) == 0,
            'errors': errors,
            'drone': self.update(db_drone)}

    def update(self, db_drone: DroneModel):
        return self.drone_repository.update(db_drone)

    def is_available(self, drone_id: int):
        db_drone = self.get(drone_id)
        errors = list()
        if db_drone.weight_limit <= sum(
            [m.weight for m in db_drone.medications]):
            errors.append("Weight limit exceeded")
        if db_drone.state not in [DroneEnumState.IDLE, DroneEnumState.LOADING]:
            errors.append("State not allowed")
        if db_drone.battery_capacity < 25:
            errors.append("Low battery")

        return {'available': len(errors) == 0, 'errors': errors}

    def available(self):
        drones = list()
        for drone in self.get_all():
            if self.is_available(drone.id)['available']:
                drones.append(drone)

        return drones

    def battery_level(self, drone_id: int):
        db_drone = self.get(drone_id)

        return db_drone.battery_capacity

    def discharge_battery(self, drone_id: int):
        db_drone = self.get(drone_id)
        if db_drone.battery_capacity > 0:
            db_drone.battery_capacity -= 1

        return self.update(db_drone)

    def charge_battery(self, drone_id: int):
        db_drone = self.get(drone_id)
        if db_drone.battery_capacity <= 95:
            db_drone.battery_capacity += 5

        return self.update(db_drone)

    def connect(self, drone_id: int):
        db_drone = self.get(drone_id)
        if db_drone:
            db_drone.charging = True

        return self.update(db_drone)

    def disconnect(self, drone_id: int):
        db_drone = self.get(drone_id)
        if db_drone:
            db_drone.charging = False

        return self.update(db_drone)
