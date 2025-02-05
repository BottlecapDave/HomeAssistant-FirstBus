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
            buses = await client.async_get_bus_times(stop)
            assert buses is not None
            assert len(buses) > 0
            
            # Assert
            for bus in buses:
                assert bus is not None
                
                assert "due" in bus
                assert bus["due"] is not None

                assert "service_number" in bus
                assert bus["service_number"] is not None

                assert "destination" in bus
                bus["destination"] is not None

                assert "is_live" in bus
                assert bus["is_live"] == True or bus["is_live"] == False

            passes += 1
        except:
            # Ignore any thrown exceptions
            pass
        
    assert passes > 0

@pytest.mark.asyncio
async def test_when_get_buses_is_called_with_invalid_stop_then_none_is_returned():
    # Arrange
    client = FirstBusApiClient()

    # Act
    buses = await client.async_get_bus_times("123")
    assert buses is None