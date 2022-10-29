from fastapi import FastAPI

app = FastAPI(
    title='Drones',
    description='Musala Soft test',
    version='1.0.0')


@app.get("/")
async def read_root():
    return {'welcome': 'Welcome to Musala Soft test (Drones)'}
