import aiohttp

class FirstBusApiClient:

  def __init__(self):
    self._base_url = 'https://www.firstbus.co.uk'

  async def async_get_buses(self, stop):
    """Get the user's account"""
    async with aiohttp.ClientSession() as client:
      url = f'{self._base_url}/getNextBus?stop={stop}'
      async with client.get(url) as response:
        # Disable content type check as sometimes it can report text/html
        data = await response.json(content_type=None)

        if ("times" in data):
          return data["times"]
        
        return []