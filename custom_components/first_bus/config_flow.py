from custom_components.first_bus.config import validate_config
import voluptuous as vol
import re
import logging

from homeassistant.config_entries import (ConfigFlow, OptionsFlow)
from homeassistant.core import callback

from .const import (
  DOMAIN,

  CONFIG_NAME,
  CONFIG_BUSES,

  DATA_SCHEMA_STOP,
  REGEX_BUSES,
)

_LOGGER = logging.getLogger(__name__)

class FirstBusConfigFlow(ConfigFlow, domain=DOMAIN): 
  """Config flow."""

  VERSION = 1

  async def async_step_user(self, user_input):
    """Setup based on user config"""

    if user_input is not None:
      (errors, config) = validate_config(user_input)

      # Setup our basic sensors
      if len(errors) < 1:
        return self.async_create_entry(
          title=f"Bus Stop {config[CONFIG_NAME]}", 
          data=config
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
        vol.Optional(CONFIG_BUSES, default=','.join(config[CONFIG_BUSES])): str,
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

    _LOGGER.debug(f"Update config {config}")

    (errors, config) = validate_config(config)

    if len(errors) < 1:
      return self.async_create_entry(title="", data=config)

    return self.async_show_form(
      step_id="user", 
      data_schema=vol.Schema({
        vol.Optional(CONFIG_BUSES, default=','.join(config[CONFIG_BUSES])): str,
      }),
      errors=errors
    )