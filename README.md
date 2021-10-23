# HomeAssistant-FirstBus

Custom component built to bring you bus times for First Buses. This was built because buses in my area stopped having live times available in [UK Transport integration](https://www.home-assistant.io/integrations/uk_transport/), and time tabled based times were only available using the more expensive `nextbuses` call.

** WARNING: This component uses a private API used by [First Bus website](https://www.firstbus.co.uk/next-bus), so it could break at any time. I will do my best to keep the component working. **

## How to install

To install, place the contents of `custom_components` into the `<config directory>/custom_components` folder of your Home Assistant installation.

## How to setup

Setup is done entirely via the [UI](https://my.home-assistant.io/redirect/config_flow_start/?domain=first_bus).

The `ATCO code` for your stop can be found in the same way that [UK Transport](https://www.home-assistant.io/integrations/uk_transport/) outlines.
    
1. On [OpenStreetMap.org](https://www.openstreetmap.org/) zoom right in on a bus stop you’re interested in.
2. Click the layers picker button on the right hand side.
3. Tick the ‘map data’ layer, and wait for clickable objects to load.
4. Click the bus stop node to reveal its tags on the left.

`Buses` are the buses you want to filter to. If you want all buses, leave this blank. If you want multiple buses, these must be separated by commas.