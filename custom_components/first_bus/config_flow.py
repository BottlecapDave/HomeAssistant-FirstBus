import voluptuous as vol

from homeassistant.config_entries import (ConfigFlow, OptionsFlow)
from homeassistant.core import callback

from .const import (
  DOMAIN,

  CONFIG_STOP,
  CONFIG_BUSES,

  DATA_SCHEMA_STOP,
)

class FirstBusConfigFlow(ConfigFlow, domain=DOMAIN): 
  """Config flow."""

  VERSION = 1

  async def async_step_user(self, user_input):
    """Setup based on user config"""

    if user_input is not None:
      # Setup our basic sensors
      return self.async_create_entry(
        title=f"Bus Stop {user_input[CONFIG_STOP]}", 
        data=user_input
      )

    return self.async_show_form(
      step_id="user", data_schema=DATA_SCHEMA_STOP
    )

  @staticmethod
  @callback
  def async_get_options_flow(entry):
    return OptionsFlowHandler(entry)

class OptionsFlowHandler(OptionsFlow):
  """Handles options flow for the component."""

  def __init__(self, entry) -> None:
    self._entry = entry

  async def async_step_user(self, user_input):
    """Manage the options for the custom component."""

    if user_input is not None:
      config = dict(self._entry.data)
      config.update(user_input)
      return self.async_create_entry(title="", data=config)

    return self.async_show_form(
      step_id="user", data_schema=vol.Schema({
        vol.Required(CONFIG_BUSES, default=config[CONFIG_BUSES]): str,
      })
    )