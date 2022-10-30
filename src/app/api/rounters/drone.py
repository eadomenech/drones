from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from ...db import SessionLocal
from ..repositories import drone as crud
from ..schemas.drone import DroneSchemaCreate, DroneSchema

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=DroneSchema)
def create_drone(drone: DroneSchemaCreate, db: Session = Depends(get_db)):
    db_drone = crud.get_drone_by_serial_number(
        db, serial_number=drone.serial_number)
    if db_drone:
        raise HTTPException(
            status_code=400, detail="Serial number already registered")
    return crud.create_drone(db=db, drone=drone)
