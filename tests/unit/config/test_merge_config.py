import pytest
from custom_components.first_bus.config import (merge_config)
from custom_components.first_bus.const import CONFIG_BUSES, CONFIG_NAME, CONFIG_STOP

@pytest.mark.asyncio
async def test_when_no_options_or_updated_config_supplied_then_no_changes_made():
  # Arrange
  data = {
    CONFIG_NAME: "name",
    CONFIG_STOP: "stop",
    CONFIG_BUSES: "buses"
  }
  options = None
  updated_config = None

  # Act
  config = merge_config(data, options, updated_config)

  # Assert
  assert config is not None
  assert config[CONFIG_NAME] == data[CONFIG_NAME]
  assert config[CONFIG_STOP] == data[CONFIG_STOP]
  assert config[CONFIG_BUSES] == data[CONFIG_BUSES]

@pytest.mark.asyncio
async def test_when_options_supplied_then_option_changes_made():
  # Arrange
  data = {
    CONFIG_NAME: "name",
    CONFIG_STOP: "stop",
    CONFIG_BUSES: "buses"
  }
  options = {
    CONFIG_NAME: "option name",
    CONFIG_STOP: "option stop",
    CONFIG_BUSES: "option buses"
  }
  updated_config = None

  # Act
  config = merge_config(data, options, updated_config)

  # Assert
  assert config is not None
  assert config[CONFIG_NAME] == options[CONFIG_NAME]
  assert config[CONFIG_STOP] == options[CONFIG_STOP]
  assert config[CONFIG_BUSES] == options[CONFIG_BUSES]

@pytest.mark.asyncio
async def test_when_updated_config_supplied_then_option_changes_made():
  # Arrange
  data = {
    CONFIG_NAME: "name",
    CONFIG_STOP: "stop",
    CONFIG_BUSES: "buses"
  }
  options = {
    CONFIG_NAME: "option name",
    CONFIG_STOP: "option stop",
    CONFIG_BUSES: "option buses"
  }
  updated_config = {
    CONFIG_NAME: "updated name",
    CONFIG_STOP: "updated stop",
    CONFIG_BUSES: "updated buses"
  }

  # Act
  config = merge_config(data, options, updated_config)

  # Assert
  assert config is not None
  assert config[CONFIG_NAME] == updated_config[CONFIG_NAME]
  assert config[CONFIG_STOP] == updated_config[CONFIG_STOP]
  assert config[CONFIG_BUSES] == updated_config[CONFIG_BUSES]

@pytest.mark.asyncio
async def test_when_buses_not_updated_supplied_in_update_then_buses_removed():
  # Arrange
  data = {
    CONFIG_NAME: "name",
    CONFIG_STOP: "stop",
    CONFIG_BUSES: "buses"
  }
  options = {
    CONFIG_NAME: "option name",
    CONFIG_STOP: "option stop",
    CONFIG_BUSES: "option buses"
  }
  updated_config = {
    CONFIG_NAME: "updated name",
    CONFIG_STOP: "updated stop",
  }

  # Act
  config = merge_config(data, options, updated_config)

  # Assert
  assert config is not None
  assert config[CONFIG_NAME] == updated_config[CONFIG_NAME]
  assert config[CONFIG_STOP] == updated_config[CONFIG_STOP]
  assert CONFIG_BUSES not in config