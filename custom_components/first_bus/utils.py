import logging
import re
from datetime import (datetime, timedelta)
from homeassistant.util.dt import (parse_datetime)

from .const import (
  REGEX_TIME,
  REGEX_TIME_MINS,
)

_LOGGER = logging.getLogger(__name__)

def get_buses(bus_times: list | None, current_timestamp: datetime, target_buses: list[str]):
  _LOGGER.debug(f'buses: {bus_times}')

  buses_to_return = []
  if bus_times is None:
    return None
  
  for bus_time in bus_times:
    if (target_buses is not None and len(target_buses) > 0 and bus_time["service_number"] not in target_buses):
      continue

    matches = re.search(REGEX_TIME, bus_time["due"])
    if (matches is not None):
      bus_time["due"] = parse_datetime(current_timestamp.strftime(f"%Y-%m-%dT{bus_time['due']}{current_timestamp.strftime('%z')}"))
    else:
      matches = re.search(REGEX_TIME_MINS, bus_time["due"])
      if (matches is None):
        if bus_time["due"] == "Due now":
          bus_time["due"] = current_timestamp.replace(second=0, microsecond=0)
        else:
          raise Exception(f'Unable to extract due time: {bus_time["due"]}')
      else:
        bus_time["due"] = current_timestamp.replace(second=0, microsecond=0) + timedelta(minutes=int(matches[1]))

    if (bus_time["due"] < current_timestamp.replace(second=0, microsecond=0)):
      _LOGGER.debug(f'Moving due timestamp to next day: Due: {bus_time["due"]}; Current Timestamp: {current_timestamp}')
      bus_time["due"] = bus_time["due"] + timedelta(days=1)

    buses_to_return.append(bus_time)
  
  return buses_to_return

def get_next_bus(bus_times: list | None, target_buses: list[str], current_timestamp: datetime):
  next_bus = None
  if bus_times is not None:
    for bus_time in bus_times:
      if (target_buses is None or len(target_buses) == 0 or bus_time["service_number"] in target_buses):

        if bus_time["due"] >= current_timestamp.replace(second=0, microsecond=0) and (next_bus is None or next_bus["due"] > bus_time["due"]):
          next_bus = bus_time

  return next_bus

def calculate_minutes_remaining(target_timestamp: datetime, current_timestamp: datetime):
  if target_timestamp is not None and current_timestamp is not None:
    if (target_timestamp >= current_timestamp):
      return (target_timestamp - current_timestamp).seconds // 60
    else:
      return ((current_timestamp - target_timestamp).seconds // 60) * -1
  
  return None