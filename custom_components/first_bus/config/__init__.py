import logging
import re

from ..api_client import FirstBusApiClient
from ..const import CONFIG_BUSES, CONFIG_STOP, REGEX_BUSES

_LOGGER = logging.getLogger(__name__)

def merge_config(data: dict, options: dict, updated_config: dict = None):
  config = dict(data)
  if options is not None:
    config.update(options)

  if updated_config is not None:
    config.update(updated_config)

    if CONFIG_BUSES not in updated_config:
      del config[CONFIG_BUSES]

  _LOGGER.debug(f'data: {data}; options: {options}; updated_config: {updated_config};')

  return config

async def async_validate_main_config(config: dict):
  new_config = dict(config)
  errors = {}
  client = FirstBusApiClient()

  if CONFIG_STOP in new_config:
    buses = await client.async_get_bus_times(new_config[CONFIG_STOP])
    if buses is None:
      errors[CONFIG_STOP] = "invalid_stop"

  if CONFIG_BUSES in new_config and new_config[CONFIG_BUSES] is not None and len(new_config[CONFIG_BUSES]) > 0:
    matches = re.search(REGEX_BUSES, new_config[CONFIG_BUSES])
    if (matches is None):
      errors[CONFIG_BUSES] = "invalid_buses"
    else:
      new_config[CONFIG_BUSES] = new_config[CONFIG_BUSES].split(",")
  else:
    new_config[CONFIG_BUSES] = []

  return (errors, new_config)