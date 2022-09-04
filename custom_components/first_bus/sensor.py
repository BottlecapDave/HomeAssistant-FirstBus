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
from .utils import (
  get_next_bus,
  async_get_buses,
  calculate_minutes_remaining
)

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
    self._buses = []
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
    return calculate_minutes_remaining(self._state, now()) 

  async def async_update(self):
    """Retrieve the next bus"""
    self._minsSinceLastUpdate = self._minsSinceLastUpdate - 1

    # We only want to update every 5 minutes so we don't hammer the service
    if self._minsSinceLastUpdate <= 0:
      buses = await async_get_buses(self._client, self._data[CONFIG_STOP], now())
      self._buses = buses
      self._minsSinceLastUpdate = 5
    
    next_bus = get_next_bus(self._buses, self._data[CONFIG_BUSES], now())
    self._attributes = next_bus
    if (self._attributes == None):
      self._attributes = {}
    
    self._attributes["stop"] = self._data[CONFIG_STOP]

    if next_bus != None:
      self._state = next_bus["Due"]
    else:
      self._state = None