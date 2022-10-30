from fastapi import FastAPI

from .api import schemas, models, crud
from .api import drone, medication
from .db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Drones',
    description='Musala Soft test',
    version='1.0.0')


@app.get("/")
async def read_root():
    return {'welcome': 'Welcome to Musala Soft test (Drones)'}


app.include_router(drone.router, prefix="/drones", tags=["drones"])
app.include_router(
    medication.router, prefix="/medications", tags=["medications"])
