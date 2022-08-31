import logging
import re
import aiohttp
from .const import (
  REGEX_TIME,
  REGEX_TIME_MINS,
)

from datetime import (timedelta)
from homeassistant.util.dt import (now, as_local, parse_datetime)

_LOGGER = logging.getLogger(__name__)

class FirstBusApiClient:

  def __init__(self):
    self._base_url = 'https://www.firstbus.co.uk'

  async def async_get_next_bus(self, stop, buses):
    """Get the user's account"""
    async with aiohttp.ClientSession() as client:
      url = f'{self._base_url}/getNextBus?stop={stop}'
      async with client.get(url) as response:
        # Disable content type check as sometimes it can report text/html
        data = await response.json(content_type=None)

        if ("times" in data):
          for time in data["times"]:
            if (buses == None or len(buses) == 0 or time["ServiceNumber"] in buses):
              matches = re.search(REGEX_TIME, time["Due"])
              if (matches != None):
                local_now = now()
                time["Due"] = as_local(parse_datetime(local_now.strftime(f"%Y-%m-%dT{time['Due']}{local_now.strftime('%z')}")))
              else:
                matches = re.search(REGEX_TIME_MINS, time["Due"])
                if (matches == None):
                  if time["Due"] == "Due now":
                    time["Due"] = now()
                  else:
                    raise Exception(f'Unable to extract due time: {time["Due"]}')
                else:
                  local_now = now()
                  time["Due"] = local_now.replace(second=0, microsecond=0) + timedelta(minutes=int(matches[1]))

              if (time["Due"] < now()):
                time["Due"] = time["Due"] + timedelta(days=1)

              return time
        
        return None