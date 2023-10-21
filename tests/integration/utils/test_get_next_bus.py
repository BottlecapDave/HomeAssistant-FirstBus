from datetime import datetime
import pytz
import pytest

from homeassistant.util.dt import (now)

from custom_components.first_bus.api_client import FirstBusApiClient
from custom_components.first_bus.utils import (get_buses, get_next_bus)

stops = ["0170SGB20116", "3800C509801", "2200YEA00934"]

@pytest.mark.asyncio
@pytest.mark.parametrize("target_buses",[
  ([]),
  (None),
  (["6", "99", "350"]),
])
async def test_when_get_next_bus_is_called_then_next_bus_is_returned(target_buses):
    # Arrange
    client = FirstBusApiClient()

    # We need to check a bunch of stops as they won't all have next buses available
    passes = 0
    for stop in stops:
        try:
            # Act
            bus_times = await client.async_get_bus_times(stop)
            buses = get_buses(bus_times, now())
            assert buses is not None
            assert len(buses) > 0
            
            next_bus = get_next_bus(buses, target_buses, now())

            # Assert
            assert next_bus is not None
            assert "Due" in next_bus
            assert next_bus["Due"].replace(tzinfo=pytz.UTC) >= datetime.utcnow().replace(tzinfo=pytz.UTC)

            assert "ServiceNumber" in next_bus
            if target_buses is not None and len(target_buses) > 0:
                assert next_bus["ServiceNumber"] in target_buses

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