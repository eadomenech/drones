import time
import requests

base_url = 'http://localhost:8001/'
while True:
    time.sleep(5)
    drones = requests.get(url=base_url+'drones/').json()
    for drone in drones:
        if drone['charging']:
            r = requests.put(url=base_url + f"drones/{drone['id']}/charge/")
        r = requests.put(url=base_url + f"drones/{drone['id']}/discharge/")