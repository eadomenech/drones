from fastapi import APIRouter, HTTPException, Depends
from typing import List

from app.api.services.drone import DroneService
from app.api.services.medication import MedicationService
from app.api.schemas import (
    DroneSchemaCreate, DroneSchema, MedicationSchema, MedicationSchemaCreate)

router = APIRouter()

drone_service = DroneService()
medication_service = MedicationService()

@router.post("/", response_model=DroneSchema, status_code=201)
def create_drone(drone: DroneSchemaCreate):
    db_drone = drone_service.get_by_serial_number(
        serial_number=drone.serial_number)
    if db_drone:
        raise HTTPException(
            status_code=400, detail="Serial number already registered")
    return drone_service.create(drone=drone)


@router.get('/', response_model=List[DroneSchema])
def get_drones():
    return drone_service.get_all()


@router.get('/{drone_id}')
def get_drone(drone_id: int):
    return drone_service.get(drone_id)


@router.put("/{drone_id}/loading", response_model=DroneSchema, status_code=202)
def loading_drone(drone_id: int, medications: List[int]):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    for medication_id in medications:
        db_medication = medication_service.get(medication_id)
        if not db_medication:
            raise HTTPException(
                status_code=400, detail="Medication not found")
    return drone_service.loading(
        drone_id=drone_id, medications=medications)


@router.post(
    "/{drone_id}/medications/", response_model=MedicationSchema,
    status_code=201)
def create_medication_for_drone(
        drone_id: int, medication: MedicationSchemaCreate):
    db_medication = medication_service.get_by_name(name=medication.name)
    if db_medication:
        raise HTTPException(
            status_code=400, detail="Medication already registered")
    return drone_service.loading(
        drone_id=drone_id, medications=[medication])


@router.get(
    "/{drone_id}/medications/", response_model=List[MedicationSchema],
    status_code=200)
def loaded_medications(drone_id: int):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    return drone_service.medications(drone_id=drone_id)


@router.get(
    "/available/", response_model=List[DroneSchema], status_code=200)
def available_drones():
    return drone_service.available()


@router.get("/{drone_id}/battery/", response_model=int, status_code=200)
def battery_level(drone_id: int):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    return drone_service.battery_level(drone_id=drone_id)


@router.put(
    "/{drone_id}/discharge", response_model=DroneSchema, status_code=202)
def discharge_battery(drone_id: int):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    return drone_service.discharge_battery(drone_id=drone_id)


@router.put(
    "/{drone_id}/charge", response_model=DroneSchema, status_code=202)
def charge_battery(drone_id: int):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    return drone_service.charge_battery(drone_id=drone_id)


@router.put(
    "/{drone_id}/connect", response_model=DroneSchema, status_code=202)
def connect(drone_id: int):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    return drone_service.connect(drone_id=drone_id)


@router.put(
    "/{drone_id}/disconnect", response_model=DroneSchema, status_code=202)
def disconnect(drone_id: int):
    db_drone = drone_service.get(drone_id)
    if not db_drone:
        raise HTTPException(
            status_code=404, detail="Drone not found")
    return drone_service.disconnect(drone_id=drone_id)
