from fastapi import FastAPI, File, UploadFile

from .api.rounters import drone, medication
from .db import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='Drones',
    description='Musala Soft test',
    version='1.0.0')


@app.get("/")
async def read_root():
    return {'welcome': 'Welcome to Musala Soft test (Drones)'}

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename, 'wb') as f:
            f.write(contents)
    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


app.include_router(drone.router, prefix="/drones", tags=["drones"])
app.include_router(
    medication.router, prefix="/medications", tags=["medications"])
