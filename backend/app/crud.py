from sqlalchemy.orm import Session

import models, schemas


def get_drone(db: Session, drone_id: int):
    return db.query(models.Drone).filter(models.Drone.id == drone_id).first()


def get_drone_by_serial_number(db: Session, serial_number: str):
    return db.query(models.Drone).filter(
        models.Drone.serial_number == serial_number).first()


def get_drones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Drone).offset(skip).limit(limit).all()


def create_drone(db: Session, drone: schemas.Drone):
    db_drone = models.Drone(
        serial_number=drone.serial_number,
        model=drone.model,
        weight_limit=drone.weight_limit,
        battery_capacity=drone.battery_capacity,
        state=drone.state)

    db.add(db_drone)
    db.commit()
    db.refresh(db_drone)

    return db_drone


def get_medications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Medication).offset(skip).limit(limit).all()


# def create_drone_medication(
#         db: Session, item: schemas.MedicationCreate, drone_id: int):
#     db_item = models.Item(**item.dict(), drone_id=drone_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
