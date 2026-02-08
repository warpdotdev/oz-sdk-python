# Changelog

## 0.6.1 (2026-02-08)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/warpdotdev/oz-sdk-python/compare/v0.6.0...v0.6.1)

### Chores

* update SDK settings ([c20dd4b](https://github.com/warpdotdev/oz-sdk-python/commit/c20dd4bda0c41e2bf167e1617521d9c66d6f98fd))
* update SDK settings ([59aa425](https://github.com/warpdotdev/oz-sdk-python/commit/59aa4254f18291861ee7fb656d57566df41ad750))
* update SDK settings ([ea483d5](https://github.com/warpdotdev/oz-sdk-python/commit/ea483d53c6242d60ece124e03510a9be6a94ffa2))

## 0.6.0 (2026-02-08)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** manual updates ([75fe5e5](https://github.com/warpdotdev/oz-sdk-python/commit/75fe5e5c5ea9e044895c1bd7f1c5ab150214c8e7))

## 0.5.0 (2026-02-08)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.4.0...v0.5.0)

### Features

* **api:** modify openapi trigger ([db2d311](https://github.com/warpdotdev/oz-sdk-python/commit/db2d3116a353cc7a5b552e09769372264f6353b8))


### Chores

* update SDK settings ([f233ca0](https://github.com/warpdotdev/oz-sdk-python/commit/f233ca083a6cf8f49bb47f9fa348dcc3aa2b5f1c))
* update SDK settings ([7857217](https://github.com/warpdotdev/oz-sdk-python/commit/78572179b9ad2c50849060db1d6d3981dd83297b))
* update SDK settings ([181c928](https://github.com/warpdotdev/oz-sdk-python/commit/181c9281ec380c5aaa09de344584fe413b67728f))

## 0.4.0 (2026-02-06)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/warpdotdev/warp-sdk-python/compare/v0.3.0...v0.4.0)

### ⚠ BREAKING CHANGES

* **api:** catch up openapi, rename tasks -> runs

### Features

* **api:** add addnl filters to runs endpoint ([c8bf51d](https://github.com/warpdotdev/warp-sdk-python/commit/c8bf51d62e4141183a77a387f2658ad5ba0255f4))
* **api:** add artifacts, worker_host, and new source types ([4aa1225](https://github.com/warpdotdev/warp-sdk-python/commit/4aa12253c3cd40bbd8460dfe6602fed5080554a4))
* **api:** add computer_use_enabled param ([69cf9ca](https://github.com/warpdotdev/warp-sdk-python/commit/69cf9ca7a2b514997baa3377a9e4d96e5fc14b29))
* **api:** add models for agent skill, user profile ([8105304](https://github.com/warpdotdev/warp-sdk-python/commit/8105304447af1bb4a28bf629cf116063621abfb5))
* **api:** add schedules to runs ([df1b59a](https://github.com/warpdotdev/warp-sdk-python/commit/df1b59a976df5898fdd893f42173c0247b934b15))
* **api:** add schedules, agent list, skill-spec ([1927318](https://github.com/warpdotdev/warp-sdk-python/commit/1927318b5b2a4115b3f1ec2be7db86f1e8e0d321))
* **api:** catch up openapi, rename tasks -&gt; runs ([fe8c5b3](https://github.com/warpdotdev/warp-sdk-python/commit/fe8c5b3f2da07a415ecd21d0f1ae5985e45f1a4d))
* **api:** created at filter in list view ([71adb45](https://github.com/warpdotdev/warp-sdk-python/commit/71adb45481ca3248d892e62ff767b9ea011e7f21))
* **api:** new run source types ([3237b0f](https://github.com/warpdotdev/warp-sdk-python/commit/3237b0fb12e6a28199f7ac86c8fc1fef6f96888e))
* **api:** update artifacts ([578be41](https://github.com/warpdotdev/warp-sdk-python/commit/578be418b8f7f0e45f427bfc5c9d98f2970a31eb))
* **client:** add custom JSON encoder for extended type support ([68f4b61](https://github.com/warpdotdev/warp-sdk-python/commit/68f4b61fd83b1f5576b72ad6ea3a28cd58e06a68))
* **client:** add support for binary request streaming ([c64e6c4](https://github.com/warpdotdev/warp-sdk-python/commit/c64e6c44b6d02a63609d02f4976a7977dc3b0045))


### Chores

* **ci:** upgrade `actions/github-script` ([713ae7d](https://github.com/warpdotdev/warp-sdk-python/commit/713ae7d03ee5f04eeac42b9a213d96ccc91d06d7))
* **internal:** update `actions/checkout` version ([fd0a90f](https://github.com/warpdotdev/warp-sdk-python/commit/fd0a90fae32b8a7e352217e3672e63b9b4dbc594))


### Documentation

* **dev:** Add WARP.md file ([7f1b835](https://github.com/warpdotdev/warp-sdk-python/commit/7f1b835240574dc517d424dca84251f86c4b1276))

## 0.3.0 (2026-01-05)

Full Changelog: [v0.2.1...v0.3.0](https://github.com/warpdotdev/warp-sdk-python/compare/v0.2.1...v0.3.0)

### Features

* **api:** fix array query parameter formatting ([d1a1243](https://github.com/warpdotdev/warp-sdk-python/commit/d1a1243a0ab6b853b2340f8e7d3652bfe05ded20))

## 0.2.1 (2025-12-19)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/warpdotdev/warp-sdk-python/compare/v0.2.0...v0.2.1)

### Bug Fixes

* use async_to_httpx_files in patch method ([c02afdb](https://github.com/warpdotdev/warp-sdk-python/commit/c02afdbec958df84a3e1ec73e213e683c79b04e8))


### Chores

* **internal:** add `--fix` argument to lint script ([46a9b4b](https://github.com/warpdotdev/warp-sdk-python/commit/46a9b4bdceac62a8939f66b0227943d18db5393f))

## 0.2.0 (2025-12-17)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/warpdotdev/warp-sdk-python/compare/v0.1.1...v0.2.0)

### Features

* **api:** manual updates ([2fc23de](https://github.com/warpdotdev/warp-sdk-python/commit/2fc23de0e1d42443e691350804605243c5902026))


### Chores

* update SDK settings ([a94be20](https://github.com/warpdotdev/warp-sdk-python/commit/a94be20a45967c6ec5bd95dcc3ffcf457db84305))

## 0.1.1 (2025-12-17)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/warpdotdev/warp-sdk-python/compare/v0.1.0...v0.1.1)

### Documentation

* add environment and config usage documentation ([487b1cf](https://github.com/warpdotdev/warp-sdk-python/commit/487b1cfac5fcd89d4c91f88903ef8b601da8269d))

## 0.1.0 (2025-12-17)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/warpdotdev/warp-sdk-python/compare/v0.0.1...v0.1.0)

### Features

* **api:** manual updates ([4d4a408](https://github.com/warpdotdev/warp-sdk-python/commit/4d4a4082d453daeb3d388ac1a23cf951ada27a9e))
* **api:** manual updates ([cd0ec74](https://github.com/warpdotdev/warp-sdk-python/commit/cd0ec747479cbb56159a361853787871c1c61395))


### Chores

* **internal:** add missing files argument to base client ([041d054](https://github.com/warpdotdev/warp-sdk-python/commit/041d0540f460ed7ecee3ed66a8db6ea9ae607360))
* speedup initial import ([c6fa047](https://github.com/warpdotdev/warp-sdk-python/commit/c6fa04747ba3b056f9dff28e564e25b4e257ca5e))
* update SDK settings ([217b866](https://github.com/warpdotdev/warp-sdk-python/commit/217b866ef03a583415f0fcdd65385ee76d53c664))
* update SDK settings ([cc95759](https://github.com/warpdotdev/warp-sdk-python/commit/cc9575998cf34b016f70f8209043a02ad1677399))


### Refactors

* **internal:** switch from rye to uv ([d4cdfd0](https://github.com/warpdotdev/warp-sdk-python/commit/d4cdfd0384b63f1ce244cdbb4327043cff02f682))
