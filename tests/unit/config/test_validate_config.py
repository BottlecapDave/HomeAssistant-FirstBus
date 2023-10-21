import pytest
from custom_components.first_bus.config import (validate_config)
from custom_components.first_bus.const import CONFIG_NAME, CONFIG_STOP, CONFIG_BUSES

@pytest.mark.asyncio
async def test_when_data_valid_then_no_errors_returned():
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123",
    CONFIG_BUSES: "12 A,12B,12"
  }

  # Act
  (errors, config) = validate_config(original_config)

  # Assert
  assert CONFIG_NAME not in errors
  assert CONFIG_STOP not in errors
  assert CONFIG_BUSES not in errors

  assert CONFIG_NAME in config
  assert config[CONFIG_NAME] == original_config[CONFIG_NAME]
  assert CONFIG_STOP in config
  assert config[CONFIG_STOP] == original_config[CONFIG_STOP]
  assert CONFIG_BUSES in config
  assert config[CONFIG_BUSES] == ["12 A", "12B", "12"]

@pytest.mark.asyncio
async def test_when_buses_not_present_then_buses_empty_array():
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123"
  }

  # Act
  (errors, config) = validate_config(original_config)

  # Assert
  assert CONFIG_NAME not in errors
  assert CONFIG_STOP not in errors
  assert CONFIG_BUSES not in errors

  assert CONFIG_NAME in config
  assert config[CONFIG_NAME] == original_config[CONFIG_NAME]
  assert CONFIG_STOP in config
  assert config[CONFIG_STOP] == original_config[CONFIG_STOP]
  assert CONFIG_BUSES in config
  assert config[CONFIG_BUSES] == []

@pytest.mark.asyncio
async def test_when_buses_none_then_buses_empty_array():
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123",
    CONFIG_BUSES: None
  }

  # Act
  (errors, config) = validate_config(original_config)

  # Assert
  assert CONFIG_NAME not in errors
  assert CONFIG_STOP not in errors
  assert CONFIG_BUSES not in errors

  assert CONFIG_NAME in config
  assert config[CONFIG_NAME] == original_config[CONFIG_NAME]
  assert CONFIG_STOP in config
  assert config[CONFIG_STOP] == original_config[CONFIG_STOP]
  assert CONFIG_BUSES in config
  assert config[CONFIG_BUSES] == []

@pytest.mark.asyncio
async def test_when_buses_empty_then_buses_empty_array():
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123",
    CONFIG_BUSES: ""
  }

  # Act
  (errors, config) = validate_config(original_config)

  # Assert
  assert CONFIG_NAME not in errors
  assert CONFIG_STOP not in errors
  assert CONFIG_BUSES not in errors

  assert CONFIG_NAME in config
  assert config[CONFIG_NAME] == original_config[CONFIG_NAME]
  assert CONFIG_STOP in config
  assert config[CONFIG_STOP] == original_config[CONFIG_STOP]
  assert CONFIG_BUSES in config
  assert config[CONFIG_BUSES] == []

@pytest.mark.asyncio
@pytest.mark.parametrize("bus_value",[
  ("A-B"),
  ("12,12B,"),
])
async def test_when_buses_not_valid_then_buses_empty_array(bus_value: str):
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123",
    CONFIG_BUSES: bus_value
  }

  # Act
  (errors, config) = validate_config(original_config)

  # Assert
  assert CONFIG_NAME not in errors
  assert CONFIG_STOP not in errors
  assert CONFIG_BUSES in errors
  assert errors[CONFIG_BUSES] == "invalid_buses"

  assert CONFIG_NAME in config
  assert config[CONFIG_NAME] == original_config[CONFIG_NAME]
  assert CONFIG_STOP in config
  assert config[CONFIG_STOP] == original_config[CONFIG_STOP]
  assert CONFIG_BUSES in config
  assert config[CONFIG_BUSES] == original_config[CONFIG_BUSES]