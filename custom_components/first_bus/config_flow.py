import voluptuous as vol
import logging

from homeassistant.config_entries import (ConfigFlow, OptionsFlow)
from homeassistant.core import callback

from .const import (
  CONFIG_STOP,
  DOMAIN,

  CONFIG_NAME,
  CONFIG_BUSES,

  DATA_SCHEMA_STOP,
)

from .config import merge_config, async_validate_main_config

_LOGGER = logging.getLogger(__name__)

def get_atco_codes(hass):
  atco_codes: list[str] = []  
  for entry in hass.config_entries.async_entries(DOMAIN, include_ignore=False):
    atco_code = entry.data[CONFIG_STOP]
    atco_codes.append(atco_code)

  return atco_codes

description_placeholders = {
  "faq_atco_code_url": "https://bottlecapdave.github.io/HomeAssistant-FirstBus/faq/#how-do-i-find-my-atco-code",
}

class FirstBusConfigFlow(ConfigFlow, domain=DOMAIN): 
  """Config flow."""

  VERSION = 1

  async def async_step_user(self, user_input):
    """Setup based on user config"""

    errors = {}
    if user_input is not None:
      atco_codes = get_atco_codes(self.hass)
      (errors, config) = await async_validate_main_config(user_input, atco_codes)

      # Setup our basic sensors
      if len(errors) < 1:
        return self.async_create_entry(
          title=f"Bus Stop {config[CONFIG_NAME]}", 
          data=config
        )

    return self.async_show_form(
      step_id="user", data_schema=DATA_SCHEMA_STOP, errors=errors, description_placeholders=description_placeholders
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

    config = merge_config(self._entry.data, self._entry.options)

    return self.async_show_form(
      step_id="user", 
      data_schema=self.add_suggested_values_to_schema(
        vol.Schema({
          vol.Optional(CONFIG_BUSES): str,
        }),
        {
          CONFIG_BUSES: ','.join(config[CONFIG_BUSES])
        }
      ),
      description_placeholders=description_placeholders
    )

  async def async_step_user(self, user_input):
    """Manage the options for the custom component."""

    errors = {}
    
    config = merge_config(self._entry.data, self._entry.options, user_input if user_input is not None else {})

    _LOGGER.debug(f"Update config {config}")

    (errors, config) = await async_validate_main_config(config)

    if len(errors) < 1:
      return self.async_create_entry(title="", data=config)

    return self.async_show_form(
      step_id="user", 
      data_schema=self.add_suggested_values_to_schema(
        vol.Schema({
          vol.Optional(CONFIG_BUSES): str,
        }),
        {
          CONFIG_BUSES: ','.join(config[CONFIG_BUSES])
        }
      ),
      description_placeholders=description_placeholders,
      errors=errors
    )