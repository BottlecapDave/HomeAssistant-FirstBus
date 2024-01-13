# HomeAssistant-FirstBus

![installation_badge](https://img.shields.io/badge/dynamic/json?color=41BDF5&logo=home-assistant&label=integration%20usage&suffix=%20installs&cacheSeconds=15600&url=https://analytics.home-assistant.io/custom_integrations.json&query=$.first_bus.total) [![](https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&color=%23fe8e86)](https://github.com/sponsors/bottlecapdave)

- [HomeAssistant-FirstBus](#homeassistant-firstbus)
  - [How to install](#how-to-install)
    - [HACS](#hacs)
    - [Manual](#manual)
  - [How to setup](#how-to-setup)
  - [Docs](#docs)
  - [FAQ](#faq)
  - [Sponsorship](#sponsorship)

Custom component built to bring you bus times for First Buses. This was built because buses in my area stopped having live times available in [UK Transport integration](https://www.home-assistant.io/integrations/uk_transport/), and time tabled based times were only available using the more expensive `nextbuses` call.

This is unofficial and in no way endorsed by First Bus.

** WARNING: This component uses a private API used by [First Bus website](https://www.firstbus.co.uk/next-bus), so it could break at any time. I will do my best to keep the component working. **

## How to install

### HACS

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

This integration can be installed directly via HACS. To install:

* [Add the repository](https://my.home-assistant.io/redirect/hacs_repository/?owner=BottlecapDave&repository=homeassistant-firstbus&category=integration) to your HACS installation
* Click `Download`

### Manual

You should take the latest [published release](https://github.com/BottlecapDave/HomeAssistant-FirstBus/releases). The current state of `develop` will be in flux and therefore possibly subject to change.

To install, place the contents of `custom_components` into the `<config directory>/custom_components` folder of your Home Assistant installation. Once installed, don't forget to restart your home assistant instance for the integration to be picked up.

## How to setup

Please follow the [setup guide](https://bottlecapdave.github.io/HomeAssistant-FirstBus/setup/account) to setup the integration. This guide details the configuration, along with the sensors that will be available to you.

## Docs

To get full use of the integration, please visit the [docs](https://bottlecapdave.github.io/HomeAssistant-FirstBus/).

## FAQ

Before raising anything, please read through the [faq](https://bottlecapdave.github.io/HomeAssistant-FirstBus/faq). If you have questions, then you can raise a [discussion](https://github.com/BottlecapDave/HomeAssistant-FirstBus/discussions). If you have found a bug or have a feature request please [raise it](https://github.com/BottlecapDave/HomeAssistant-FirstBus/issues) using the appropriate report template.

## Sponsorship

If you are enjoying the integration, why not if possible, make a one off or monthly [GitHub sponsorship](https://github.com/sponsors/bottlecapdave).