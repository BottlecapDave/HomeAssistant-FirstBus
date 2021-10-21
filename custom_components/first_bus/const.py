import voluptuous as vol

DOMAIN = "first_bus"

CONFIG_NAME = "Name"
CONFIG_STOP = "Stop"
CONFIG_BUSES = "Buses"

REGEX_TIME="[0-9]{2}:[0-9]{2}"
REGEX_TIME_MINS="([0-9]+) mins"

DATA_SCHEMA_STOP = vol.Schema({
  vol.Required(CONFIG_NAME): str,
  vol.Required(CONFIG_STOP): str,
  vol.Optional(CONFIG_BUSES): str,
})