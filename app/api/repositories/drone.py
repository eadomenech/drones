from fastapi import HTTPException

from sqlalchemy.orm import Session
from typing import List

from ..schemas import DroneSchemaCreate
from app.api.models import DroneModel, MedicationModel


def get_drone(db: Session, drone_id: int):
    return db.query(DroneModel).get(drone_id)


def get_drone_by_serial_number(db: Session, serial_number: str):
    return db.query(DroneModel).filter(
        DroneModel.serial_number == serial_number).first()


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
            status_code=400, detail="Weight limit exceeded.")

    for medication_id in medications:
        db_medication = db.query(MedicationModel).get(medication_id)
        db_medication.drone_id = drone_id
        db.add(db_medication)
        db.commit()
        db.refresh(db_medication)



    return db_drone
