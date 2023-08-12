from datetime import timedelta
import pytest
from custom_components.first_bus.utils import (calculate_minutes_remaining)
from homeassistant.util.dt import (parse_datetime)

now = parse_datetime('2022-01-01T10:00:00Z')

@pytest.mark.asyncio
@pytest.mark.parametrize("target_timestamp,expected_minutes_remaining",[
  (None, None),
  (now + timedelta(minutes=35), 35),
  (now - timedelta(seconds=31), 0),
  (now - timedelta(minutes=2), -2),
])
async def test_when_calculate_minutes_remaining_is_called_then_result_is_correct(target_timestamp, expected_minutes_remaining):
  # Act
  minutes_remaining = calculate_minutes_remaining(target_timestamp, now)

  # Assert
  assert minutes_remaining == expected_minutes_remaining