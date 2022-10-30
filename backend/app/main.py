from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Drones',
    description='Musala Soft test',
    version='1.0.0')

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_root():
    return {'welcome': 'Welcome to Musala Soft test (Drones)'}

@app.post("/drones/", response_model=schemas.Drone)
def create_drone(drone: schemas.Drone, db: Session = Depends(get_db)):
    db_drone = crud.get_drone_by_serial_number(
        db, serial_number=drone.serial_number)
    if db_drone:
        raise HTTPException(
            status_code=400, detail="Serial number already registered")
    return crud.create_drone(db=db, drone=drone)
