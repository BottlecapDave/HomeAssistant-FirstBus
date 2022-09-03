import logging
import re

from .const import (
  REGEX_TIME,
  REGEX_TIME_MINS,
)

from datetime import (timedelta)
from homeassistant.util.dt import (as_local, parse_datetime)
from .api_client import FirstBusApiClient

_LOGGER = logging.getLogger(__name__)

async def async_get_buses(api_client: FirstBusApiClient, stop, current_timestamp):
  bus_times = await api_client.async_get_buses(stop)
  for bus_time in bus_times:
    _LOGGER.debug(f'next bus: {bus_time}')
    matches = re.search(REGEX_TIME, bus_time["Due"])
    if (matches != None):
      bus_time["Due"] = as_local(parse_datetime(current_timestamp.strftime(f"%Y-%m-%dT{bus_time['Due']}{current_timestamp.strftime('%z')}")))
    else:
      matches = re.search(REGEX_TIME_MINS, bus_time["Due"])
      if (matches == None):
        if bus_time["Due"] == "Due now":
          bus_time["Due"] = current_timestamp.replace(second=0, microsecond=0)
        else:
          raise Exception(f'Unable to extract due time: {bus_time["Due"]}')
      else:
        bus_time["Due"] = current_timestamp.replace(minute=0, second=0, microsecond=0) + timedelta(minutes=int(matches[1]))

    if (bus_time["Due"] < current_timestamp.replace(second=0, microsecond=0)):
      bus_time["Due"] = bus_time["Due"] + timedelta(days=1)
  
  return bus_times

def get_next_bus(bus_times, target_buses, current_timestamp):
  for bus_time in bus_times:
    if (target_buses == None or len(target_buses) == 0 or bus_time["ServiceNumber"] in target_buses):

      if bus_time["Due"] >= current_timestamp.replace(second=0, microsecond=0):
        return bus_time

  return None

def calculate_minutes_remaining(target_timestamp, current_timestamp):
  if target_timestamp != None and target_timestamp >= current_timestamp:
    return (target_timestamp - current_timestamp).seconds // 60
  else:
    return -1