from sqlalchemy.orm import Session

from ..schemas.drone import DroneSchemaCreate
from app.api.models.drone import DroneModel


def get_drone(db: Session, drone_id: int):
    return db.query(DroneModel).filter(DroneModel.id == drone_id).first()


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
