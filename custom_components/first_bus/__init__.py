import logging
from homeassistant.util.dt import utcnow
import asyncio

from .const import (
  DOMAIN,
)

async def async_setup_entry(hass, entry):
  """This is called from the config flow."""
  hass.data.setdefault(DOMAIN, {})

  # Forward our entry to setup our default sensors
  hass.async_create_task(
    hass.config_entries.async_forward_entry_setup(entry, "sensor")
  )

  return True

async def options_update_listener(hass, entry):
  """Handle options update."""
  await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass, entry):
  """Unload a config entry."""

  unload_ok = all(
      await asyncio.gather(
          *[hass.config_entries.async_forward_entry_unload(entry, "sensor")]
      )
  )

  return unload_ok