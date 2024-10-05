from homeassistant.helpers.entity import Entity

async def async_setup_entry(hass, config_entry, async_add_entities):
    async_add_entities([AEGWasherSensor()])

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
        data = get_washer_status()
        if data:
            self._state = data.get("status")

import requests
from homeassistant.helpers.entity import Entity
from .const import API_KEY, BASE_URL

def get_washer_status():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.get(f"{BASE_URL}devices/washer/status", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None