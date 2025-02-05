from unittest import mock
import pytest
from custom_components.first_bus.config import async_validate_config
from custom_components.first_bus.const import CONFIG_NAME, CONFIG_STOP, CONFIG_BUSES
from custom_components.first_bus.api_client import FirstBusApiClient

@pytest.mark.asyncio
async def test_when_data_valid_then_no_errors_returned():
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123",
    CONFIG_BUSES: "12 A,12B,12"
  }

  async def async_mocked_get_bus_times(*args, **kwargs):
    return []

  # Act
  with mock.patch.multiple(FirstBusApiClient, async_get_bus_times=async_mocked_get_bus_times):
    (errors, config) = await async_validate_config(original_config)

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

  async def async_mocked_get_bus_times(*args, **kwargs):
    return []

  # Act
  with mock.patch.multiple(FirstBusApiClient, async_get_bus_times=async_mocked_get_bus_times):
    (errors, config) = await async_validate_config(original_config)

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

  async def async_mocked_get_bus_times(*args, **kwargs):
    return []

  # Act
  with mock.patch.multiple(FirstBusApiClient, async_get_bus_times=async_mocked_get_bus_times):
    (errors, config) = await async_validate_config(original_config)

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

  async def async_mocked_get_bus_times(*args, **kwargs):
    return []

  # Act
  with mock.patch.multiple(FirstBusApiClient, async_get_bus_times=async_mocked_get_bus_times):
    (errors, config) = await async_validate_config(original_config)

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

  async def async_mocked_get_bus_times(*args, **kwargs):
    return []

  # Act
  with mock.patch.multiple(FirstBusApiClient, async_get_bus_times=async_mocked_get_bus_times):
    (errors, config) = await async_validate_config(original_config)

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

@pytest.mark.asyncio
async def test_when_bus_stop_is_invalid_then_no_errors_returned():
  # Arrange
  original_config = {
    CONFIG_NAME: "test",
    CONFIG_STOP: "123",
    CONFIG_BUSES: ""
  }

  async def async_mocked_get_bus_times(*args, **kwargs):
    return None

  # Act
  with mock.patch.multiple(FirstBusApiClient, async_get_bus_times=async_mocked_get_bus_times):
    (errors, config) = await async_validate_config(original_config)

    # Assert
    assert CONFIG_NAME not in errors
    assert CONFIG_BUSES not in errors
    assert CONFIG_STOP in errors
    assert errors[CONFIG_STOP] == "invalid_stop"

    assert CONFIG_NAME in config
    assert config[CONFIG_NAME] == original_config[CONFIG_NAME]
    assert CONFIG_STOP in config
    assert config[CONFIG_STOP] == original_config[CONFIG_STOP]
    assert CONFIG_BUSES in config
    assert config[CONFIG_BUSES] == []