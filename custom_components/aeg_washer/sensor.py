# sensor.py
import requests
from homeassistant.helpers.entity import Entity
from .const import API_KEY, BASE_URL

def get_washer_status():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}appliances", headers=headers)
    if response.status_code == 200:
        devices = response.json()
        for device in devices:
            if device['type'] == 'washer':
                return device
    return None

class AEGWasherSensor(Entity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return "AEG Washer Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        device = get_washer_status()
        if device:
            self._state = device.get("status")
