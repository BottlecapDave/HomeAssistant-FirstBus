import pytest
from datetime import timedelta
from homeassistant.util.dt import (parse_datetime)

from custom_components.first_bus.utils import (get_next_bus)

now = parse_datetime('2022-01-01T10:00:00Z')

@pytest.mark.asyncio
@pytest.mark.parametrize("target_buses,expected_bus_index",[
  (None, 1),
  ([], 1),
  (["42"], 2),
  (["19"], None),
])
async def test_when_get_next_bus_is_called_then_due_timestamp_is_correct(target_buses, expected_bus_index):
  # Arrange
  buses = [
    {
      'service_ref': '0', 
      'service_number': '49', 
      'destination': 'Newton Road Shops', 
      'due': now + timedelta(days=1, minutes=64), 
      'is_live': True
    },
    {
      'service_ref': '0', 
      'service_number': '43', 
      'destination': 'Newton Road Shops', 
      'due': now + timedelta(minutes=35), 
      'is_live': True
    },
    {
      'service_ref': '0', 
      'service_number': '42', 
      'destination': 'Newton Road Shops', 
      'due': now + timedelta(minutes=64), 
      'is_live': True
    }
  ]
  
  expected_next_bus = None
  if expected_bus_index is not None:
    expected_next_bus = buses[expected_bus_index]

  # Act
  next_bus = get_next_bus(buses, target_buses, now)

  # Assert
  if (expected_next_bus is None):
    assert next_bus is None
  else:
    assert next_bus is not None

    assert "due" in next_bus
    assert next_bus["due"] == expected_next_bus["due"]

    assert "service_number" in next_bus
    assert next_bus["service_number"] == expected_next_bus["service_number"]

    assert "destination" in next_bus
    assert next_bus["destination"] == expected_next_bus["destination"]

    assert "is_live" in next_bus
    assert next_bus["is_live"] == expected_next_bus["is_live"]

@pytest.mark.asyncio
async def test_when_get_next_bus_is_called_and_buses_in_the_past_then_correct_next_bus_is_picked():
  # Arrange
  buses = [{
    'service_ref': '0', 
    'service_number': '43', 
    'destination': 'Newton Road Shops', 
    'due': now - timedelta(minutes=35), 
    'is_live': True
  },
  {
    'service_ref': '0', 
    'service_number': '42', 
    'destination': 'Newton Road Shops', 
    'due': now + timedelta(minutes=64), 
    'is_live': True
  }]
  
  expected_next_bus = buses[1]

  # Act
  next_bus = get_next_bus(buses, [], now)

  # Assert
  if (expected_next_bus is None):
    assert next_bus is None
  else:
    assert next_bus is not None

    assert "due" in next_bus
    assert next_bus["due"] == expected_next_bus["due"]

    assert "service_number" in next_bus
    assert next_bus["service_number"] == expected_next_bus["service_number"]

    assert "destination" in next_bus
    assert next_bus["destination"] == expected_next_bus["destination"]

    assert "is_live" in next_bus
    assert next_bus["is_live"] == expected_next_bus["is_live"]

@pytest.mark.asyncio
async def test_when_subset_of_buses_looked_for_then_correct_bus_is_picked():
  # Arrange
  buses = [{
    'service_ref': '0', 
    'service_number': '12 A', 
    'destination': 'Newton Road Shops', 
    'due': now - timedelta(minutes=35), 
    'is_live': True
  },
  {
    'service_ref': '0', 
    'service_number': '12', 
    'destination': 'Newton Road Shops', 
    'due': now + timedelta(minutes=64), 
    'is_live': True
  }]
  
  expected_next_bus = buses[1]

  # Act
  next_bus = get_next_bus(buses, ["12"], now)

  # Assert
  if (expected_next_bus is None):
    assert next_bus is None
  else:
    assert next_bus is not None

    assert "due" in next_bus
    assert next_bus["due"] == expected_next_bus["due"]

    assert "service_number" in next_bus
    assert next_bus["service_number"] == expected_next_bus["service_number"]

    assert "destination" in next_bus
    assert next_bus["destination"] == expected_next_bus["destination"]

    assert "is_live" in next_bus
    assert next_bus["is_live"] == expected_next_bus["is_live"]

  
@pytest.mark.asyncio
async def test_when_buses_is_none_then_none_is_returned():
  # Arrange
  buses = None

  # Act
  next_bus = get_next_bus(buses, ["12"], now)

  # Assert
  assert next_bus is None