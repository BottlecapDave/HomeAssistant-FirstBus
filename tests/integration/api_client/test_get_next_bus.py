from datetime import datetime
import pytz
import pytest

from custom_components.first_bus.api_client import FirstBusApiClient

stops = ["0170SGB20077", "3800C509801", "2200YEA00934"]

@pytest.mark.asyncio
@pytest.mark.parametrize("buses",[
  ([]),
  (None),
  (["19"]),
])
async def test_when_get_next_bus_is_called_then_next_bus_is_returned(buses):
    # Arrange
    client = FirstBusApiClient()

    # We need to check a bunch of stops as they won't all have next buses available
    passes = 0
    for stop in stops:
        try:
            # Act
            next_bus = await client.async_get_next_bus(stop, buses)

            # Assert
            assert next_bus != None
            assert "Due" in next_bus
            assert next_bus["Due"].replace(tzinfo=pytz.UTC) >= datetime.utcnow().replace(tzinfo=pytz.UTC)

            assert "ServiceNumber" in next_bus

            assert "Destination" in next_bus

            assert "IsFG" in next_bus
            assert next_bus["IsFG"] == "Y" or next_bus["IsFG"] == "N"

            assert "IsLive" in next_bus
            assert next_bus["IsLive"] == "Y" or next_bus["IsFG"] == "N"

            passes += 1
        except:
            # Ignore any thrown exceptions
            pass
        
    assert passes > 0