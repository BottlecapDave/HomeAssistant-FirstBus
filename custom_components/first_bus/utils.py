import logging
import re
from datetime import (datetime, timedelta)
from homeassistant.util.dt import (parse_datetime)

from .const import (
  REGEX_TIME,
  REGEX_TIME_MINS,
)

_LOGGER = logging.getLogger(__name__)

def get_buses(bus_times: list, current_timestamp: datetime):
  _LOGGER.debug(f'buses: {bus_times}')
  
  for bus_time in bus_times:
    matches = re.search(REGEX_TIME, bus_time["Due"])
    if (matches is not None):
      bus_time["Due"] = parse_datetime(current_timestamp.strftime(f"%Y-%m-%dT{bus_time['Due']}{current_timestamp.strftime('%z')}"))
    else:
      matches = re.search(REGEX_TIME_MINS, bus_time["Due"])
      if (matches is None):
        if bus_time["Due"] == "Due now":
          bus_time["Due"] = current_timestamp.replace(second=0, microsecond=0)
        else:
          raise Exception(f'Unable to extract due time: {bus_time["Due"]}')
      else:
        bus_time["Due"] = current_timestamp.replace(second=0, microsecond=0) + timedelta(minutes=int(matches[1]))

    if (bus_time["Due"] < current_timestamp.replace(second=0, microsecond=0)):
      _LOGGER.debug(f'Moving due timestamp to next day: Due: {bus_time["Due"]}; Current Timestamp: {current_timestamp}')
      bus_time["Due"] = bus_time["Due"] + timedelta(days=1)
  
  return bus_times

def get_next_bus(bus_times, target_buses, current_timestamp):
  next_bus = None
  for bus_time in bus_times:
    if (target_buses is None or len(target_buses) == 0 or bus_time["ServiceNumber"] in target_buses):

      if bus_time["Due"] >= current_timestamp.replace(second=0, microsecond=0) and (next_bus is None or next_bus["Due"] > bus_time["Due"]):
        next_bus = bus_time

  return next_bus

def calculate_minutes_remaining(target_timestamp, current_timestamp):
  if target_timestamp is not None and current_timestamp is not None:
    if (target_timestamp >= current_timestamp):
      return (target_timestamp - current_timestamp).seconds // 60
    else:
      return ((current_timestamp - target_timestamp).seconds // 60) * -1
  
  return None