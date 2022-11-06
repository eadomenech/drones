from fastapi import HTTPException

from sqlalchemy.orm import Session
from typing import List

from ..schemas import DroneSchemaCreate
from app.api.models import DroneModel, MedicationModel
from ..enums import DroneEnumState


def get_drone(db: Session, drone_id: int):
    return db.query(DroneModel).get(drone_id)


def get_drone_by_serial_number(db: Session, serial_number: str):
    return db.query(DroneModel).filter(
        DroneModel.serial_number == serial_number).first()


def loaded_medications(db: Session, drone_id: int):
    return db.query(DroneModel).get(drone_id).medications


def get_drones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DroneModel).offset(skip).limit(limit).all()


def create_drone(db: Session, drone: DroneSchemaCreate):
    db_drone = DroneModel(
        serial_number=drone.serial_number,
        model=drone.model,
        weight_limit=drone.weight_limit,
        battery_capacity=drone.battery_capacity,
        state=drone.state)

    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone


def loading_drone(db: Session, drone_id: int, medications: List[int]):
    db_drone = db.query(DroneModel).get(drone_id)
    total_weight = 0.0
    for medication_id in medications:
        db_medication = db.query(MedicationModel).get(medication_id)
        total_weight += db_medication.weight

    if total_weight > db_drone.weight_limit:
        raise HTTPException(
            status_code=400, detail="Weight limit exceeded")

    for medication_id in medications:
        db_medication = db.query(MedicationModel).get(medication_id)
        db_medication.drone_id = drone_id
        db.add(db_medication)
        db.commit()
        db.refresh(db_medication)

    db_drone.state = 'LOADING'

    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone

def is_available(drone_id: int, db: Session):
    db_drone = db.query(DroneModel).get(drone_id)
    available = True
    error = list()
    if db_drone.weight_limit <= sum([m.weight for m in db_drone.medications]):
        available = False
        error.append(
            HTTPException(status_code=400, detail="Weight limit exceeded"))
    if db_drone.state not in [DroneEnumState.IDLE, DroneEnumState.LOADING]:
        available = False
        error.append(
            HTTPException(status_code=400, detail="State not allowed"))
    if db_drone.battery_capacity < 25:
        available = False
        error.append(HTTPException(status_code=400, detail="Low battery"))

    return {'available': available, 'error': error}


def available_drones(db: Session):
    drones = []
    for drone in get_drones(db):
        if is_available(drone.id, db)['available']:
            drones.append(drone)

    return drones


def battery_level(db: Session, drone_id: int):
    db_drone = db.query(DroneModel).get(drone_id)

    return db_drone.battery_capacity


def discharge_battery(db: Session, drone_id: int):
    db_drone = db.query(DroneModel).get(drone_id)
    if db_drone.battery_capacity > 0:
        db_drone.battery_capacity -= 1
    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone


def charge_battery(db: Session, drone_id: int):
    db_drone = db.query(DroneModel).get(drone_id)
    if db_drone.battery_capacity <= 95:
        db_drone.battery_capacity += 5
    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone


def connect(db: Session, drone_id: int):
    db_drone = db.query(DroneModel).get(drone_id)
    if db_drone:
        db_drone.charging = True
    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone


def disconnect(db: Session, drone_id: int):
    db_drone = db.query(DroneModel).get(drone_id)
    if db_drone:
        db_drone.charging = False
    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone
