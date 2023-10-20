import re
from ..const import CONFIG_BUSES, REGEX_BUSES

def validate_config(config: dict):
  new_config = dict(config)
  errors = {}
  if CONFIG_BUSES in new_config and new_config[CONFIG_BUSES] is not None and len(new_config[CONFIG_BUSES]) > 0:
    matches = re.search(REGEX_BUSES, new_config[CONFIG_BUSES])
    if (matches is None):
      errors[CONFIG_BUSES] = "invalid_buses"
    else:
      new_config[CONFIG_BUSES] = new_config[CONFIG_BUSES].split(",")
  else:
    new_config[CONFIG_BUSES] = []

  return (errors, new_config)
    