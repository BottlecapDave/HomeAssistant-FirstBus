# Setup

Setup is done entirely via the [UI](https://my.home-assistant.io/redirect/config_flow_start/?domain=first_bus).

You can setup the integration as many times as you like, with each setup tracking a different stop and potential buses from that stop. 

## Details

### Name

This is the name to help identify the stop. It will also be used in any created sensors.

### ATCO code

This identifies the stop that you're wanting to track. Instructions on how to find this, can be found in the [FAQ](./faq.md#how-do-i-find-my-atco-code)

### Buses

This is the list of buses that arrive at the designated stop that you're wanting to track. If you want any bus at the stop, leave this blank. If you are wanting multiple buses, then you will need to specify them in a comma separated list (e.g `19,20,21 A`)

## Entities

The full list of entities can be found in the [entities section](./entities.md).