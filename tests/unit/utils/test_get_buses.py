import pytest
from homeassistant.util.dt import (parse_datetime)

from custom_components.first_bus.utils import (get_buses)

now = parse_datetime('2022-01-01T10:23:15+01:00')

@pytest.mark.asyncio
@pytest.mark.parametrize("raw_due,expected_due",[
  ("35 mins", parse_datetime('2022-01-01T10:58:00+01:00')),
  ("Due now", parse_datetime('2022-01-01T10:23:00+01:00')),
  ("10:22", parse_datetime('2022-01-02T10:22:00+01:00')),
  ("10:23", parse_datetime('2022-01-01T10:23:00+01:00')),
  ("10:24", parse_datetime('2022-01-01T10:24:00+01:00')),
])
async def test_when_get_buses_is_called_and_set_time_in_past_is_returned_then_due_timestamp_is_correct(raw_due, expected_due):
  # Arrange
  bus_times = [
    {
      'service_ref': '0', 
      'service_number': '43', 
      'destination': 'Newton Road Shops', 
      'due': raw_due, 
      'is_live': True
    },
    {
      'service_ref': '0', 
      'service_number': '42', 
      'destination': 'Newton Road Shops', 
      'due': raw_due, 
      'is_live': True
    }
  ]

  # Act
  buses = get_buses(bus_times, now, [])
  assert buses is not None
  assert len(buses) == 2

  for i in range(2):
    bus = buses[i]
    raw_bus = bus_times[i]

    # Assert
    assert "due" in bus
    assert bus["due"] == expected_due

    assert "service_number" in bus
    assert bus["service_number"] == raw_bus["service_number"]

    assert "destination" in bus
    assert bus["destination"] == raw_bus["destination"]

    assert "is_live" in bus
    assert bus["is_live"] == raw_bus["is_live"]

@pytest.mark.asyncio
async def test_when_target_buses_is_none_then_due_timestamp_is_correct():
  # Arrange
  bus_times = [
    {
      'service_ref': '0', 
      'service_number': '43', 
      'destination': 'Newton Road Shops', 
      'due': '35 mins', 
      'is_live': True
    },
    {
      'service_ref': '0', 
      'service_number': '42', 
      'destination': 'Newton Road Shops', 
      'due': '35 mins', 
      'is_live': True
    }
  ]

  # Act
  buses = get_buses(bus_times, now, None)
  assert buses is not None
  assert len(buses) == 2

  for i in range(2):
    bus = buses[i]
    raw_bus = bus_times[i]

    # Assert
    assert "due" in bus
    assert bus["due"] == parse_datetime('2022-01-01T10:58:00+01:00')

    assert "service_number" in bus
    assert bus["service_number"] == raw_bus["service_number"]

    assert "destination" in bus
    assert bus["destination"] == raw_bus["destination"]

    assert "is_live" in bus
    assert bus["is_live"] == raw_bus["is_live"]

@pytest.mark.asyncio
async def test_when_target_buses_specified_then_only_those_buses_are_returned():
  # Arrange
  bus_times = [
    {
      'service_ref': '0', 
      'service_number': '43', 
      'destination': 'Newton Road Shops', 
      'due': '35 mins', 
      'is_live': True
    },
    {
      'service_ref': '0', 
      'service_number': '42', 
      'destination': 'Newton Road Shops', 
      'due': '35 mins', 
      'is_live': True
    }
  ]

  # Act
  buses = get_buses(bus_times, now, ["42"])
  assert buses is not None
  assert len(buses) == 1

  bus = buses[0]
  raw_bus = bus_times[1]

  # Assert
  assert "due" in bus
  assert bus["due"] == parse_datetime('2022-01-01T10:58:00+01:00')

  assert "service_number" in bus
  assert bus["service_number"] == raw_bus["service_number"]

  assert "destination" in bus
  assert bus["destination"] == raw_bus["destination"]

  assert "is_live" in bus
  assert bus["is_live"] == raw_bus["is_live"]