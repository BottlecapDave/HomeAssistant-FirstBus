from datetime import (timedelta)
import logging

from homeassistant.util.dt import (now)
from homeassistant.components.sensor import (
    SensorEntity,
)
from .const import (
  CONFIG_NAME,
  CONFIG_STOP,
  CONFIG_BUSES
)

from .api_client import (FirstBusApiClient)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(minutes=1)

async def async_setup_entry(hass, entry, async_add_entities):
  """Setup sensors based on our entry"""

  entities = [FirstBusNextBus(entry.data)]

  async_add_entities(entities, True)

class FirstBusNextBus(SensorEntity):
  """Sensor for the next bus."""

  def __init__(self, data):
    """Init sensor."""

    self._client = FirstBusApiClient()
    self._data = data
    self._attributes = {}
    self._state = None
    self._minsSinceLastUpdate = 0

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"first_bus_{self._data[CONFIG_STOP]}_next_bus"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"First Bus {self._data[CONFIG_NAME]} Next Bus"

  @property
  def icon(self):
    """Icon of the sensor."""
    return "mdi:bus"

  @property
  def extra_state_attributes(self):
    """Attributes of the sensor."""
    return self._attributes

  @property
  def native_unit_of_measurement(self):
    return "minutes"

  @property
  def state(self):
    """The state of the sensor."""
    current_datetime = now()
    if self._state != None:
      return (self._state - current_datetime).seconds // 60
    else:
      return -1 

  async def async_update(self):
    """Retrieve the next bus"""
    self._minsSinceLastUpdate = self._minsSinceLastUpdate + 1

    # We only want to update every 5 minutes so we don't hammer the service
    if self._minsSinceLastUpdate >= 5:
      next_time = await self._client.async_get_next_bus(self._data[CONFIG_STOP], self._data[CONFIG_BUSES])
      self._attributes = next_time
      self._attributes["stop"] = self._data[CONFIG_STOP]
      self._minsSinceLastUpdate = 0

      if next_time != None:
        self._state = next_time["Due"]
      else:
        self._state = None