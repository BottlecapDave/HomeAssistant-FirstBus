# Entities

Below is the list of entities that will be created with each instance of the integration.

### Next Bus

`sensor.first_bus_<<NAME_OF_SENSOR>>_next_bus`

This will provide the number of minutes until one of the specified buses (or any if no specific buses were specified) reach the bus stop. If there is no known next bus, then `none`/`unknown` will be returned.

The sensor will pull the latest times for the stop every **5 minutes**. This is done so that the unofficial API isn't hammered and support is taken away, and I felt 5 minutes was long enough so that information wasn't too stale. This means that there is a chance that the time won't reflect the times on the app/website if they are updated within this 5 minute timeframe.

The following attributes are available in addition

| Attribute | Notes |
|-----------|-------|
| `ServiceNumber` | The name/number of the next bus |
| `Destination` | The destination of the next bus |
| `Due` | The timestamp of when the next bus is due, in ISO format |
| `IsFG` | Determines if the bus is a First bus (`Y`) or not (`N`) |
| `IsLive` | Determines if the bus is being tracked (`Y`) or is from the timetable (`N`) |
| `stop` | The ATCO code of the bus stop that is being tracked |