import pytest
from custom_components.first_bus.utils import (async_get_buses)
from homeassistant.util.dt import (parse_datetime)

class MockedFirstBusApiClient:
  def __init__(self, buses):
    self._buses = buses

  async def async_get_buses(self, stop):
    return self._buses

now = parse_datetime('2022-01-01T10:00:00Z')

@pytest.mark.asyncio
@pytest.mark.parametrize("raw_due,expected_due",[
  ("35 mins", parse_datetime('2022-01-01T10:35:00Z')),
  ("Due now", parse_datetime('2022-01-01T10:00:00Z')),
  ("09:16", parse_datetime('2022-01-02T09:16:00Z')),
  ("11:16", parse_datetime('2022-01-01T11:16:00Z')),
])
async def test_when_get_buses_is_called_and_set_time_in_past_is_returned_then_due_timestamp_is_correct(raw_due, expected_due):
  # Arrange
  raw_buses = [{
    'ServiceRef': '0', 
    'ServiceNumber': '43', 
    'Destination': 'Newton Road Shops', 
    'Due': raw_due, 
    'IsFG': 'N', 
    'IsLive': 'Y'
  }]
  client = MockedFirstBusApiClient(raw_buses)
  stop = "TEST_STOP"

  # Act
  buses = await async_get_buses(client, stop, now)
  assert buses != None
  assert len(buses) == 1

  bus = buses[0]
  raw_bus = raw_buses[0]

  # Assert
  assert "Due" in bus
  assert bus["Due"] == expected_due

  assert "ServiceNumber" in bus
  assert bus["ServiceNumber"] == raw_bus["ServiceNumber"]

  assert "Destination" in bus
  assert bus["Destination"] == raw_bus["Destination"]

  assert "IsFG" in bus
  assert bus["IsFG"] == raw_bus["IsFG"]

  assert "IsLive" in bus
  assert bus["IsLive"] == raw_bus["IsLive"]