import pytest

from custom_components.first_bus.api_client import FirstBusApiClient

stops = ["0170SGB20116", "3800C509801", "2200YEA00934"]

@pytest.mark.asyncio
async def test_when_get_buses_is_called_then_next_bus_is_returned():
    # Arrange
    client = FirstBusApiClient()

    # We need to check a bunch of stops as they won't all have next buses available
    passes = 0
    for stop in stops:
        try:
            # Act
            buses = await client.async_get_buses(stop)
            assert buses is not None
            assert len(buses) > 0
            
            # Assert
            for bus in buses:
                assert bus is not None
                
                assert "Due" in bus
                assert bus["Due"] is not None

                assert "ServiceNumber" in bus
                assert bus["ServiceNumber"] is not None

                assert "Destination" in bus
                bus["Destination"] is not None

                assert "IsFG" in bus
                assert bus["IsFG"] == "Y" or bus["IsFG"] == "N"

                assert "IsLive" in bus
                assert bus["IsLive"] == "Y" or bus["IsFG"] == "N"

            passes += 1
        except:
            # Ignore any thrown exceptions
            pass
        
    assert passes > 0