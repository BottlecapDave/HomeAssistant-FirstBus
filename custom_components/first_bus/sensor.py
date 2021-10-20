from datetime import timedelta
import logging

from homeassistant.util.dt import (now, as_utc)
from homeassistant.components.sensor import (
    DEVICE_CLASS_TIMESTAMP,
    SensorEntity,
)
from .const import (
  CONFIG_STOP,
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

  @property
  def unique_id(self):
    """The id of the sensor."""
    return f"first_bus_{self._data[CONFIG_STOP]}_next_bus"
    
  @property
  def name(self):
    """Name of the sensor."""
    return f"First Bus {self._data[CONFIG_STOP]} Next Bus"

  @property
  def device_class(self):
    """The type of sensor"""
    return DEVICE_CLASS_TIMESTAMP

  @property
  def icon(self):
    """Icon of the sensor."""
    return "mdi:camera-timer"

  @property
  def extra_state_attributes(self):
    """Attributes of the sensor."""
    return self._attributes

  @property
  def state(self):
    """The state of the sensor."""
    return self._state

  async def async_update(self):
    """Retrieve the latest consumption"""
    # We only need to do this every half an hour
    current_datetime = now()
    if (current_datetime.minute % 30) == 0 or self._state == None:
      _LOGGER.info('Updating OctopusEnergyLatestElectricityReading')

      period_from = as_utc(current_datetime - timedelta(hours=1))
      period_to = as_utc(current_datetime)
      data = await self._client.async_electricity_consumption(self._mpan, self._serial_number, period_from, period_to)
      if data != None and len(data) > 0:
        self._state = data[0]["consumption"]
      else:
        self._state = 0