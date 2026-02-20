## [2.0.5](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v2.0.4...v2.0.5) (2026-02-20)


### Bug Fixes

* Added additional checks that bus stops haven't already been configured ([a9bb88e](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/a9bb88edb6a56392da713041883784ce5883035a))
* Fixed translation issue (15 minutes dev time) ([b83770a](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/b83770a427b16ea7e11a56e614de5f602e4f1626))

## [2.0.4](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v2.0.3...v2.0.4) (2025-03-13)


### Bug Fixes

* Added additional clarification to name (Thanks @ZackaryH8) ([78b3049](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/78b3049fe832e1a721e7571406df144e1724cfaf))
* Fixed issue with bus sensor throwing error if API returns invalid result (15 minutes dev time) ([634b8a8](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/634b8a866af69d0d3170faaacdcee846cadd9045))

## [2.0.3](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v2.0.2...v2.0.3) (2025-02-05)


### Bug Fixes

* Updated setup to check bus stop is recognised by First Bus (30 minutes dev time) ([ec4ca50](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/ec4ca5073528dc94246ccf16ec7c7ebde5d7ea03))

## [2.0.2](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v2.0.1...v2.0.2) (2024-09-24)


### Bug Fixes

* Fixed buses attribute to only return target buses if specified ([a246509](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/a246509b7d896cd8783e9095c7d45aabf1cb240d))

## [2.0.1](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v2.0.0...v2.0.1) (2024-06-29)


### Bug Fixes

* Fixed ATCO link when setting up integration ([5dfdae5](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/5dfdae5871c72c6e66b980193e87c76128726f89))
* Fixed warning around use of deprecated HA function (15 minutes dev time) ([757e873](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/757e87322b15bacf9fef75f7d1f155cf2402414b))

# [2.0.0](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.2.0...v2.0.0) (2024-01-20)


### Bug Fixes

* renamed attributes to have consistent naming style and updated Y/N based attributes to return bool ([6e1caba](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/6e1caba23725d65021763dfd867f012b5965640f))


### Features

* Added data_last_updated attribute to sensor ([e47f2a3](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/e47f2a399ca53a8cfc4dc6e14fcdf6ac08936eb8))


### BREAKING CHANGES

* Any reliances on attributes (e.g. automations) will need to be updated based on new naming structure
and return types. IsFG attribute has been removed as value always seems to be false.

# [1.2.0](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.1.4...v1.2.0) (2024-01-13)


### Features

* Added buses attribute to sensor (Thanks [@garthy](https://github.com/garthy)) ([39994d1](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/39994d1fbbdbfb04b798b60a0f98a0768e23160a))

## [1.1.4](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.1.3...v1.1.4) (2023-10-21)


### Bug Fixes

* Fixed unsetting buses for existing entries ([0703fca](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/0703fca5ea7c17d447697bb962b8f01336d9c864))
* Updated bus filters to support buses with with spaces ([c8fe0a2](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/c8fe0a2a825281914465c5ed550981f49d253759))

## [1.1.3](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.1.2...v1.1.3) (2023-08-12)


### Bug Fixes

* Fixed sensor not reporting -1 when the bus is due ([e0ebd06](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/e0ebd065ba3fc5ece573823baf2271a51f54aac1))

## [1.1.2](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.1.1...v1.1.2) (2022-09-05)


### Bug Fixes

* **sensor:** Fixed minutes remaining to take account if target bus time is before now ([55a27ec](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/55a27ecbcc0cd61e506c4221454715f6da5b0df5))
* **sensor:** Updated sensor to get next bus straight away ([d1d8017](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/d1d8017d9f2ad01cad3a6f6124ccb2bea89f49bb))

## [1.1.1](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.1.0...v1.1.1) (2022-09-02)


### Bug Fixes

* **sensor:** Added unit of measurement so value isn't present in log book ([7cc38bf](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/7cc38bfb3ec6c61b09f915cb5b1d77597e19e8e0))

# [1.1.0](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.0.3...v1.1.0) (2022-09-02)


### Bug Fixes

* **config:** Fixed updating buses to other buses ([9297c86](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/9297c86575d8200f3a6339c354e87554c0b99566))


### Features

* **sensor:** Added stop code to bus sensor ([536fa87](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/536fa87eb4b1c24a36d168dfc1dcbbbaeff07877))

## [1.0.3](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.0.2...v1.0.3) (2022-08-31)


### Bug Fixes

* **api-client:** Fixed retrieving buses when no specific buses are specified ([7b31424](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/7b31424348a30171714f216c2d36772f8eae3bd2))

## [1.0.1](https://github.com/BottlecapDave/HomeAssistant-FirstBus/compare/v1.0.0...v1.0.1) (2021-10-30)


### Bug Fixes

* Added fix for when first bus report that the bus is due now ([c915a94](https://github.com/BottlecapDave/HomeAssistant-FirstBus/commit/c915a94ddd4c55e8355a9d3223ad0e25e72395f2))
