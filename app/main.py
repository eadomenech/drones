from celery import Celery
from fastapi import FastAPI

from app.api.routers import drone, medication
from app.db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Drones',
    description='Musala Soft test',
    version='1.0.0')

celery = Celery(
    __name__,
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/0"
)


@app.get("/")
async def read_root():
    return {'welcome': 'Welcome to Musala Soft test (Drones)'}

@celery.task
def update_drone_battery():
    import time
    time.sleep(5)
    return True

celery.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.update_drone_battery',
        'schedule': 300.0
    },
}


app.include_router(drone.router, prefix="/drones", tags=["drones"])
app.include_router(
    medication.router, prefix="/medications", tags=["medications"])
