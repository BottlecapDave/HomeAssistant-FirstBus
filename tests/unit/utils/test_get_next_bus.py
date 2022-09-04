import pytest
from datetime import timedelta
from custom_components.first_bus.utils import (get_next_bus)
from homeassistant.util.dt import (parse_datetime)

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
      'ServiceRef': '0', 
      'ServiceNumber': '49', 
      'Destination': 'Newton Road Shops', 
      'Due': now + timedelta(days=1, minutes=64), 
      'IsFG': 'N', 
      'IsLive': 'Y'
    },
    {
    'ServiceRef': '0', 
    'ServiceNumber': '43', 
    'Destination': 'Newton Road Shops', 
    'Due': now + timedelta(minutes=35), 
    'IsFG': 'N', 
    'IsLive': 'Y'
    },
    {
      'ServiceRef': '0', 
      'ServiceNumber': '42', 
      'Destination': 'Newton Road Shops', 
      'Due': now + timedelta(minutes=64), 
      'IsFG': 'N', 
      'IsLive': 'Y'
    }
  ]
  
  expected_next_bus = None
  if expected_bus_index != None:
    expected_next_bus = buses[expected_bus_index]

  # Act
  next_bus = get_next_bus(buses, target_buses, now)

  # Assert
  if (expected_next_bus == None):
    assert next_bus == None
  else:
    assert next_bus != None

    assert "Due" in next_bus
    assert next_bus["Due"] == expected_next_bus["Due"]

    assert "ServiceNumber" in next_bus
    assert next_bus["ServiceNumber"] == expected_next_bus["ServiceNumber"]

    assert "Destination" in next_bus
    assert next_bus["Destination"] == expected_next_bus["Destination"]

    assert "IsFG" in next_bus
    assert next_bus["IsFG"] == expected_next_bus["IsFG"]

    assert "IsLive" in next_bus
    assert next_bus["IsLive"] == expected_next_bus["IsLive"]

@pytest.mark.asyncio
async def test_when_get_next_bus_is_called_and_buses_in_the_past_then_correct_next_bus_is_picked():
  # Arrange
  buses = [{
    'ServiceRef': '0', 
    'ServiceNumber': '43', 
    'Destination': 'Newton Road Shops', 
    'Due': now - timedelta(minutes=35), 
    'IsFG': 'N', 
    'IsLive': 'Y'
  },
  {
    'ServiceRef': '0', 
    'ServiceNumber': '42', 
    'Destination': 'Newton Road Shops', 
    'Due': now + timedelta(minutes=64), 
    'IsFG': 'N', 
    'IsLive': 'Y'
  }]
  
  expected_next_bus = buses[1]

  # Act
  next_bus = get_next_bus(buses, [], now)

  # Assert
  if (expected_next_bus == None):
    assert next_bus == None
  else:
    assert next_bus != None

    assert "Due" in next_bus
    assert next_bus["Due"] == expected_next_bus["Due"]

    assert "ServiceNumber" in next_bus
    assert next_bus["ServiceNumber"] == expected_next_bus["ServiceNumber"]

    assert "Destination" in next_bus
    assert next_bus["Destination"] == expected_next_bus["Destination"]

    assert "IsFG" in next_bus
    assert next_bus["IsFG"] == expected_next_bus["IsFG"]

    assert "IsLive" in next_bus
    assert next_bus["IsLive"] == expected_next_bus["IsLive"]