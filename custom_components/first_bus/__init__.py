from homeassistant.util.dt import utcnow

from .const import (
  DOMAIN,
)

PLATFORMS = ["sensor"]

async def async_setup_entry(hass, entry):
  """This is called from the config flow."""
  hass.data.setdefault(DOMAIN, {})

  # Forward our entry to setup our default sensors
  await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

  return True

async def options_update_listener(hass, entry):
  """Handle options update."""
  await hass.config_entries.async_reload(entry.entry_id)

async def async_unload_entry(hass, entry):
  """Unload a config entry."""

  unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

  return unload_ok