from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db import get_db
from ..repositories import drone as service
from ..schemas import DroneSchemaCreate, DroneSchema

router = APIRouter()


@router.post("/", response_model=DroneSchema, status_code=201)
def create_drone(drone: DroneSchemaCreate, db: Session = Depends(get_db)):
    db_drone = service.get_drone_by_serial_number(
        db, serial_number=drone.serial_number)
    if db_drone:
        raise HTTPException(
            status_code=400, detail="Serial number already registered")
    return service.create_drone(db=db, drone=drone)


@router.get('/', response_model=List[DroneSchema])
def get_drones(db: Session = Depends(get_db)):
    return service.get_drones(db)


@router.get('/{drone_id}')
def get_drone(drone_id: int, db: Session = Depends(get_db)):
    return service.get_drone(db, drone_id)


@router.put("/{drone_id}/loading", response_model=DroneSchema, status_code=202)
def loading_drone(
        drone_id: int, medications: List[int], db: Session = Depends(get_db)):
    db_drone = service.get_drone(db, drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    else:
        return service.loading_drone(
            db=db, drone_id=drone_id, medications=medications)
