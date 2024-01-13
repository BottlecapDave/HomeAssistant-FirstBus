# FAQ

## How do I find my ATCO code?

The `ATCO code` for your stop can be found in the same way that [UK Transport](https://www.home-assistant.io/integrations/uk_transport/) outlines.
    
1. On [OpenStreetMap.org](https://www.openstreetmap.org/) zoom right in on a bus stop you’re interested in.
2. Click the layers picker button on the right hand side.
3. Tick the ‘map data’ layer, and wait for clickable objects to load.
4. Click the bus stop node to reveal its tags on the left.

However, there have been reports of missing ATCO codes. Therefore alternatively, you can follow the following instructions:

1. Navigate to https://www.firstbus.co.uk/next-bus and type your location
2. Open up the development tools on your browser (usually F12) and go to the network tab
3. Click on the stop that you're after and look at the network request. This should make a request to https://www.firstbus.co.uk/api/get-next-bus?stop=XXX. The value you're after will be in the response and also the value of XXX.

## How do I increase the logs for the integration?

If you are having issues, it would be helpful to include Home Assistant logs as part of any raised issue. This can be done by following the [instructions](https://www.home-assistant.io/docs/configuration/troubleshooting/#enabling-debug-logging) outlined by Home Assistant.

You should run these logs for about a day and then include the contents in the issue. Please be sure to remove any personal identifiable information from the logs before including them.