import voluptuous as vol

DOMAIN = "first_bus"

CONFIG_STOP = "STOP"
CONFIG_BUSES = "BUSES"

REGEX_TIME="[0-9]{2}:[0-9]{2}"
REGEX_TIME_MINS="([0-9]{2}) mins"

DATA_SCHEMA_STOP = vol.Schema({
  vol.Required(CONFIG_STOP): str,
  vol.Optional(CONFIG_BUSES): str,
})