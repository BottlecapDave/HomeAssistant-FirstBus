import voluptuous as vol
import re

from homeassistant.config_entries import (ConfigFlow, OptionsFlow)
from homeassistant.core import callback

from .const import (
  DOMAIN,

  CONFIG_NAME,
  CONFIG_BUSES,

  DATA_SCHEMA_STOP,
  REGEX_BUSES,
)

class FirstBusConfigFlow(ConfigFlow, domain=DOMAIN): 
  """Config flow."""

  VERSION = 1

  async def async_step_user(self, user_input):
    """Setup based on user config"""

    errors = {}
    if user_input is not None:
      if CONFIG_BUSES in user_input and user_input[CONFIG_BUSES] != None:
        matches = re.search(REGEX_BUSES, user_input[CONFIG_BUSES])
        if (matches == None):
          errors[CONFIG_BUSES] = "invalid_buses"
        else:
          user_input[CONFIG_BUSES] = user_input[CONFIG_BUSES].split(",")
      else:
        user_input[CONFIG_BUSES] = []

      # Setup our basic sensors
      if len(errors) < 1:
        return self.async_create_entry(
          title=f"Bus Stop {user_input[CONFIG_NAME]}", 
          data=user_input
        )

    return self.async_show_form(
      step_id="user", data_schema=DATA_SCHEMA_STOP, errors=errors
    )

  @staticmethod
  @callback
  def async_get_options_flow(entry):
    return OptionsFlowHandler(entry)

class OptionsFlowHandler(OptionsFlow):
  """Handles options flow for the component."""

  def __init__(self, entry) -> None:
    self._entry = entry

  async def async_step_init(self, user_input):
    """Manage the options for the custom component."""

    config = dict(self._entry.data)
    if self._entry.options is not None:
      config.update(self._entry.options)

    return self.async_show_form(
      step_id="user", 
      data_schema=vol.Schema({
        vol.Optional(CONFIG_BUSES, default=config[CONFIG_BUSES]): str,
      })
    )

  async def async_step_user(self, user_input):
    """Manage the options for the custom component."""

    errors = {}
    config = dict(self._entry.data)
    if self._entry.options is not None:
      config.update(self._entry.options)

    if user_input is not None:
      config.update(user_input)

      if CONFIG_BUSES in config and config[CONFIG_BUSES] != None:
        matches = re.search(REGEX_BUSES, config[CONFIG_BUSES])
        if (matches == None):
          errors[CONFIG_BUSES] = "invalid_buses"
        else:
          config[CONFIG_BUSES] = config[CONFIG_BUSES].split(",")
      else:
        config[CONFIG_BUSES] = []

      if len(errors) < 1:
        return self.async_create_entry(title="", data=config)

    return self.async_show_form(
      step_id="user", 
      data_schema=vol.Schema({
        vol.Optional(CONFIG_BUSES, default=config[CONFIG_BUSES]): str,
      }),
      errors=errors
    )