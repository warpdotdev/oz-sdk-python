# Changelog

## 0.14.0 (2026-07-02)

Full Changelog: [v0.13.0...v0.14.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.13.0...v0.14.0)

### Features

* Add server run runtime to agent API ([85d7ef8](https://github.com/warpdotdev/oz-sdk-python/commit/85d7ef8e6cc1380deed30f8efd6e75f062b3fa53))
* Allow for empty-prompt cloud-agent handoff ([2542fa3](https://github.com/warpdotdev/oz-sdk-python/commit/2542fa3058b5feead7f46fe5255665ef5c36528e))
* **api:** api update ([54f4c39](https://github.com/warpdotdev/oz-sdk-python/commit/54f4c39a78402eceb57dd531e4c35ed869cd10b1))
* **api:** api update ([73a49ad](https://github.com/warpdotdev/oz-sdk-python/commit/73a49ad055f94883b17b03b8a2c328881d1fe859))
* **api:** api update ([8d4b77c](https://github.com/warpdotdev/oz-sdk-python/commit/8d4b77c936054c5c125fa0747a298a64ed349a48))
* **api:** api update ([a03690f](https://github.com/warpdotdev/oz-sdk-python/commit/a03690f7a25a0887c60981a53a2224c5ba1cc26a))
* **api:** api update ([7ef54cc](https://github.com/warpdotdev/oz-sdk-python/commit/7ef54ccc0ad281b27a2e0db5cac2956bef2b93e1))
* **api:** api update ([d25946f](https://github.com/warpdotdev/oz-sdk-python/commit/d25946f832fe901339b42dcf8842a17d20b57634))
* **api:** api update ([d59deee](https://github.com/warpdotdev/oz-sdk-python/commit/d59deee2f15baa213eaa694b1bf71f94330b9d89))
* Followups for docs-syncing workflow ([4697ddc](https://github.com/warpdotdev/oz-sdk-python/commit/4697ddc9625dd3bcdcc756af1da2e2ba0fc5fff0))


### Bug Fixes

* **auth:** prioritize first auth header ([bcf94f5](https://github.com/warpdotdev/oz-sdk-python/commit/bcf94f549cd8109ac30d87f3922e5772238183b3))
* update aiohttp to resolve CVE-2026-22815 ([#25](https://github.com/warpdotdev/oz-sdk-python/issues/25)) ([03d6bc4](https://github.com/warpdotdev/oz-sdk-python/commit/03d6bc4d2253f820aa5b1fa842d382b20f2d681d))

## 0.13.0 (2026-05-21)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.12.0...v0.13.0)

### Features

* Add default harness selection for agents ([8cd06f6](https://github.com/warpdotdev/oz-sdk-python/commit/8cd06f6fcb48444e3861ff130d2fb4fa820e3aa7))
* Add per-agent AWS Bedrock OIDC inference role (backend) ([e4aadec](https://github.com/warpdotdev/oz-sdk-python/commit/e4aadec916b2bea7e05e0e263b307449002e7f8b))
* Add updated_at to agent API responses ([3188420](https://github.com/warpdotdev/oz-sdk-python/commit/318842095218a12c5b3ed1d945941e74ca5c9d54))
* **agents:** add prompt property to agent identity data model ([520c835](https://github.com/warpdotdev/oz-sdk-python/commit/520c8350b5b7850242adc082fe83a7ae666e6da6))
* **api:** api update ([b8306ad](https://github.com/warpdotdev/oz-sdk-python/commit/b8306ad8aff3c8e83f3c9549a8d78a1dfe22e7f5))
* **api:** api update ([a66cdc2](https://github.com/warpdotdev/oz-sdk-python/commit/a66cdc2b99686872998efe8592b21bb14c6320cc))
* **api:** api update ([da1ee9c](https://github.com/warpdotdev/oz-sdk-python/commit/da1ee9c25078cfbf6fb34e6e3afd09edcfe6b76b))
* **api:** api update ([32f77e1](https://github.com/warpdotdev/oz-sdk-python/commit/32f77e19c7bd30dbeacb84ce95f5e487a7c9debf))
* **api:** api update ([7ec4ab4](https://github.com/warpdotdev/oz-sdk-python/commit/7ec4ab432f4a3e6494d29d7db0b9bf3a08ba0885))
* **api:** api update ([c05564a](https://github.com/warpdotdev/oz-sdk-python/commit/c05564aa69ba70685b6778859b0574f1d2d69a33))
* **api:** api update ([0976362](https://github.com/warpdotdev/oz-sdk-python/commit/09763624c5e172aa28fa43ed18bc0e391c04331d))
* **api:** api update ([96d640c](https://github.com/warpdotdev/oz-sdk-python/commit/96d640cd68290e1a915fca51a8629cf9dab4d81d))
* **api:** api update ([2730eea](https://github.com/warpdotdev/oz-sdk-python/commit/2730eea19d91df998de5ef1b5da4989670a5889a))
* **api:** api update ([af81ef3](https://github.com/warpdotdev/oz-sdk-python/commit/af81ef3a2d48f378209cf69a3074997cb02b1b6c))
* **api:** api update ([99b2d31](https://github.com/warpdotdev/oz-sdk-python/commit/99b2d31ba1a4c2c3d79fc11c5eb8d611c55613b8))
* Codex auth: API key support. ([cb84f0c](https://github.com/warpdotdev/oz-sdk-python/commit/cb84f0c6c9625d8c0657c728d5fadae065eb37c9))
* **internal/types:** support eagerly validating pydantic iterators ([a588f0e](https://github.com/warpdotdev/oz-sdk-python/commit/a588f0e5ba27503659b5abf01d0ebc01f652950d))
* **memory:** agent identity memory store attachments — API layer ([94b5348](https://github.com/warpdotdev/oz-sdk-python/commit/94b5348152c6b0bfb03b0d3887366c4a65e397fb))
* **memory:** wire memory stores into run pipeline and add listing endpoint ([6bb74c2](https://github.com/warpdotdev/oz-sdk-python/commit/6bb74c2b695cd268fe8466fc6099f082370ba54e))
* Partial support for multiple skills per run ([e39df48](https://github.com/warpdotdev/oz-sdk-python/commit/e39df4831329c75d13b7638a2edc146a0a2f57a1))
* Resolve Bedrock region server-side and ship as AWS_REGION ([cef2591](https://github.com/warpdotdev/oz-sdk-python/commit/cef25915ca886a87aa5d567d1e3001ca746c8960))
* Retrieve memories in third party harnesses ([7689e12](https://github.com/warpdotdev/oz-sdk-python/commit/7689e121d6f22efad3d81828721f8ed900b9cd28))
* Support service account impersonation in GCP Workload Identity Federation config ([6df1722](https://github.com/warpdotdev/oz-sdk-python/commit/6df1722325b8c96d7655348e75bd82980e2bd055))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([17a8e5b](https://github.com/warpdotdev/oz-sdk-python/commit/17a8e5bf17b882a440a067fee1569caf679f8b55))

## 0.12.0 (2026-05-07)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.11.0...v0.12.0)

### Features

* [APP-3106] Specs: Explicit QueryMode for cloud agent run creation ([1d4e049](https://github.com/warpdotdev/oz-sdk-python/commit/1d4e049e5c64fdfe1f8eff8dbf7bc8256ed98182))
* [REMOTE-1481] [3/N] Add executor filter to run list API ([2dbc229](https://github.com/warpdotdev/oz-sdk-python/commit/2dbc22949c6c9475a31e74cba5eadecb018277f3))
* [REMOTE-1538] Support base model on named agents ([7634c23](https://github.com/warpdotdev/oz-sdk-python/commit/7634c231906d3fb53c9576b39fac1fa60f694790))
* Accept and persist executor on schedule and integration create/update APIs ([a8500aa](https://github.com/warpdotdev/oz-sdk-python/commit/a8500aa0b3e74221cd931b01d7e7569ad191d1f3))
* Add API support for public access on oz session link ([df940e0](https://github.com/warpdotdev/oz-sdk-python/commit/df940e09b23d2cc3d314407a8826f722b9428dca))
* Add Codex as a third-party Oz harness. ([898e18f](https://github.com/warpdotdev/oz-sdk-python/commit/898e18f8e26a2064d3bb3bdda83c08adeb91088d))
* Add Gemini as a third-party Oz harness. ([0128722](https://github.com/warpdotdev/oz-sdk-python/commit/0128722383f87f6d5a73fd0ecafc4206a3013342))
* Add parent_run_id filter to List runs endpoint ([33cf04c](https://github.com/warpdotdev/oz-sdk-python/commit/33cf04c0777d53059f8a3c73b925b468276aba2a))
* Add system prompt to resolve-prompt for harnesses. ([2b7afab](https://github.com/warpdotdev/oz-sdk-python/commit/2b7afabf4a54764ab162ac32f4dbe7fe4274ba72))
* Add trigger URL to task source. ([9662dbe](https://github.com/warpdotdev/oz-sdk-python/commit/9662dbe10cc5392271b3e56c35cb8ef95ec80eed))
* Add worker_host to AgentListSource in OpenAPI spec ([ec0982c](https://github.com/warpdotdev/oz-sdk-python/commit/ec0982ce786b2380ab89aa7298b28998c6eade46))
* **api:** api update ([88de4e2](https://github.com/warpdotdev/oz-sdk-python/commit/88de4e2765d70de416658f0ce0ef42585763efc9))
* **api:** api update ([4a0d4fc](https://github.com/warpdotdev/oz-sdk-python/commit/4a0d4fc0711f3fe0d3168c3f5f7ec2176d5b0010))
* **api:** api update ([654da59](https://github.com/warpdotdev/oz-sdk-python/commit/654da597a10a63048c5a34ca67c9d6684c72b688))
* **api:** api update ([86d389c](https://github.com/warpdotdev/oz-sdk-python/commit/86d389c610fb2b89d7fcd17ebfd06610ef2b0b90))
* **api:** api update ([15d68a1](https://github.com/warpdotdev/oz-sdk-python/commit/15d68a1db8178fd9cb5fae456ca6f341b60fd1e7))
* **api:** api update ([54f5cdc](https://github.com/warpdotdev/oz-sdk-python/commit/54f5cdc819015611f7214b8ac6632df1cebf857d))
* **api:** api update ([e290d3b](https://github.com/warpdotdev/oz-sdk-python/commit/e290d3b8cd2e8bd10a713e41992e282b704c624e))
* **api:** api update ([35565ad](https://github.com/warpdotdev/oz-sdk-python/commit/35565ada13a8a16f9117b3ca0c12279d1708d184))
* **api:** api update ([9cf2d03](https://github.com/warpdotdev/oz-sdk-python/commit/9cf2d0352242be5c7075fe971561cc36aaaf6e77))
* **api:** api update ([ed871aa](https://github.com/warpdotdev/oz-sdk-python/commit/ed871aac657265138112d98be757a0de48796e02))
* **api:** api update ([a44c455](https://github.com/warpdotdev/oz-sdk-python/commit/a44c455cb949e69b05f33f38571b40d9c0caed36))
* **api:** api update ([e24ba64](https://github.com/warpdotdev/oz-sdk-python/commit/e24ba644c9d3624019f240fd43f51079adf7d8d4))
* **api:** api update ([e5aea21](https://github.com/warpdotdev/oz-sdk-python/commit/e5aea2192017b1758d7b32d1e855015ce29e93ca))
* **api:** api update ([f94b38b](https://github.com/warpdotdev/oz-sdk-python/commit/f94b38b2ffaf344a198e89ad7ace1d7b8e93c300))
* **api:** api update ([7f419fa](https://github.com/warpdotdev/oz-sdk-python/commit/7f419faa01908e1b4a613ec2bdd708aed1a05871))
* **api:** api update ([116f06e](https://github.com/warpdotdev/oz-sdk-python/commit/116f06e5c63e8d015e7dfea47fc22ede53ebb84e))
* **api:** api update ([66c8521](https://github.com/warpdotdev/oz-sdk-python/commit/66c852194f355cedca2b34b944c398e796f064ab))
* **api:** api update ([ebd2c55](https://github.com/warpdotdev/oz-sdk-python/commit/ebd2c5520128722d88285aea9dd0caf3242d9a31))
* **api:** api update ([1ffc53b](https://github.com/warpdotdev/oz-sdk-python/commit/1ffc53b4d69eeb8060faac1903f1ba25f7a4c443))
* **api:** api update ([cf28804](https://github.com/warpdotdev/oz-sdk-python/commit/cf288045d369ed927db45ac5e5ebd994ccebb547))
* **api:** api update ([a6d82f1](https://github.com/warpdotdev/oz-sdk-python/commit/a6d82f1a71ad8e0ff5f10c43cc81938babc1444e))
* **api:** api update ([b9872f2](https://github.com/warpdotdev/oz-sdk-python/commit/b9872f2642191ef6e1d4d5d3542a08f9e2784b9e))
* **api:** api update ([0ef9c8f](https://github.com/warpdotdev/oz-sdk-python/commit/0ef9c8f483269d203a3edc7b5805f48f4263eb2f))
* Apply service-account secrets at run creation ([db0e98c](https://github.com/warpdotdev/oz-sdk-python/commit/db0e98ca667b0cfe5b8ab182db5b1d4a19584113))
* Extend service account API to support skills + secrets ([caf9c45](https://github.com/warpdotdev/oz-sdk-python/commit/caf9c4539ad1718ed194619ebf26425217265706))
* implement server-side cloud-to-cloud handoff for agent follow-ups (REMOTE-1290) ([eb873a6](https://github.com/warpdotdev/oz-sdk-python/commit/eb873a6092aa1792ca6c23f5d27a7ee66c225ea0))
* Include agent UID in scheduled agent API responses ([1714226](https://github.com/warpdotdev/oz-sdk-python/commit/1714226a85760699faacebd23cc1ea3a6bc7f0b9))
* Inject auth secrets via ambient agent config. ([6032a0c](https://github.com/warpdotdev/oz-sdk-python/commit/6032a0ccfe2ce669ce1f815ad853b912d4ca575e))
* Make conversation/session redirects public ([4c23bb6](https://github.com/warpdotdev/oz-sdk-python/commit/4c23bb6ebec32b5022a1731284d3e07b81a9f5ae))
* Memory data model scaffolding. ([4ccbe03](https://github.com/warpdotdev/oz-sdk-python/commit/4ccbe0371e7bf02c454a14bc8bc2d412dcebf290))
* support setting headers via env ([d3b4755](https://github.com/warpdotdev/oz-sdk-python/commit/d3b4755c7447d915a4e11be043b21b859f6c028d))
* Surface platform credits in the public API ([d54b3d5](https://github.com/warpdotdev/oz-sdk-python/commit/d54b3d55760fa68853130d026dfdd88a7e226c80))
* Update public API and graphql to support creating multiple service accounts and API keys ([8d537bc](https://github.com/warpdotdev/oz-sdk-python/commit/8d537bcbe75b344427bd04e5406ab066769f580a))


### Bug Fixes

* ensure file data are only sent as 1 parameter ([6720ea9](https://github.com/warpdotdev/oz-sdk-python/commit/6720ea9331a945cf2d030e20b8851a223697aab3))
* use correct field name format for multipart file arrays ([f785ff2](https://github.com/warpdotdev/oz-sdk-python/commit/f785ff2bafbd319574974549a73c21643cdb5cc5))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([b8e42cc](https://github.com/warpdotdev/oz-sdk-python/commit/b8e42cc08805eef08a3462088ba0e32cf79dac8c))


### Chores

* **internal:** more robust bootstrap script ([27c80e9](https://github.com/warpdotdev/oz-sdk-python/commit/27c80e953bc19de56ea730b0c2170aa8ffbc495a))
* **internal:** reformat pyproject.toml ([fd17af1](https://github.com/warpdotdev/oz-sdk-python/commit/fd17af10c72ed943e4023a4e9e071ac7b8db08f7))
* update SDK settings ([f2dd099](https://github.com/warpdotdev/oz-sdk-python/commit/f2dd099128bf4f98e304778556d55e80a4fd219c))

## 0.11.0 (2026-04-09)

Full Changelog: [v0.10.1...v0.11.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.10.1...v0.11.0)

### Features

* [Artifacts] public API file artifact downloads ([1d2007e](https://github.com/warpdotdev/oz-sdk-python/commit/1d2007eaa692679fdcc56a6092ffdf9ad09de6ca))
* Add harness enum to openAPI spec ([c8b44e5](https://github.com/warpdotdev/oz-sdk-python/commit/c8b44e532885d53f406babf8c0463f62d86a1fbe))
* Add parent_run_id to retrieve/list runs API response ([c5752fb](https://github.com/warpdotdev/oz-sdk-python/commit/c5752fbbceffbc322cee5dd8b111aa0ce84ce615))
* Add VMIdleTimeoutMinutes param to API ([31b5a63](https://github.com/warpdotdev/oz-sdk-python/commit/31b5a63204a2baca1a41f0b4124408d2d2b7e6a4))
* Address Stainless diagnostics ([58d59e3](https://github.com/warpdotdev/oz-sdk-python/commit/58d59e3593d27ad4bb17e340c384d9709f650806))
* **api:** api update ([9140132](https://github.com/warpdotdev/oz-sdk-python/commit/9140132ca22861c78365898e250a5c613af454a8))
* **api:** api update ([204505c](https://github.com/warpdotdev/oz-sdk-python/commit/204505c1472d5af4b9463a975fd919c5fc4dbe78))
* **api:** api update ([5e2d3ee](https://github.com/warpdotdev/oz-sdk-python/commit/5e2d3ee9400130c5a8dc2d51d1618ad292c051ab))
* **api:** api update ([1238769](https://github.com/warpdotdev/oz-sdk-python/commit/12387694506b5d0d53e527db1dcdb2ca02ae2f71))
* **api:** api update ([75b1c92](https://github.com/warpdotdev/oz-sdk-python/commit/75b1c92550babef5b0cf19689613f95131df08d7))
* **api:** api update ([4b777eb](https://github.com/warpdotdev/oz-sdk-python/commit/4b777ebbe2483c2d882597bd0ab593128f5355d9))
* **api:** api update ([9fe02aa](https://github.com/warpdotdev/oz-sdk-python/commit/9fe02aad21c71cbab837f7d335e5234e1974bb90))
* **api:** api update ([7fc79ef](https://github.com/warpdotdev/oz-sdk-python/commit/7fc79efe0897451670cb44cf29c0f99b06ffe821))
* **api:** manual updates ([ed9f4cf](https://github.com/warpdotdev/oz-sdk-python/commit/ed9f4cfa6a0db58dc3ca5564f83b09ef1a19e3a9))
* **api:** manual updates ([e52643f](https://github.com/warpdotdev/oz-sdk-python/commit/e52643fcb1408ac9f8dd6a284b9cb818f3f468ac))
* Create run for every local conversation and add filter ([aac84c5](https://github.com/warpdotdev/oz-sdk-python/commit/aac84c585eb3b0ed5262d683e544960a82eec2a2))
* Define auth secrets and inject them into the environment. ([54c505b](https://github.com/warpdotdev/oz-sdk-python/commit/54c505b2d58246abab42cda52d79df3ddbfed083))
* Endpoint to upload third-party harness block snapshots ([2f71989](https://github.com/warpdotdev/oz-sdk-python/commit/2f7198972cec56e72b802c7505fb445d10304bf4))
* Fix the harness type in the openAPI spec ([71d7204](https://github.com/warpdotdev/oz-sdk-python/commit/71d72043f6cb8d8ae6af4c01936967059936c7b0))
* ian/fix_conversation_id_nameing ([658c50b](https://github.com/warpdotdev/oz-sdk-python/commit/658c50b6b3937249034ad9e6993e598705d0c3c6))
* **internal:** implement indices array format for query and form serialization ([c518876](https://github.com/warpdotdev/oz-sdk-python/commit/c518876f3da1129d3c351982ed4a06590fd15f2e))
* Orchestrations V2: Public API endpoints ([5514980](https://github.com/warpdotdev/oz-sdk-python/commit/551498004c85dd4277069b0c059c17c7504bc18b))
* Use correct branch for Stainless PRs ([d7b298d](https://github.com/warpdotdev/oz-sdk-python/commit/d7b298d99c5dcb5e02530329fef222de92f3e9d6))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([5da3150](https://github.com/warpdotdev/oz-sdk-python/commit/5da315075e053b1a6cef709439f9972f6fd0f70f))

## 0.10.1 (2026-03-24)

Full Changelog: [v0.10.0...v0.10.1](https://github.com/warpdotdev/oz-sdk-python/compare/v0.10.0...v0.10.1)

### Chores

* update SDK settings ([8afbeb4](https://github.com/warpdotdev/oz-sdk-python/commit/8afbeb4c91e704eac42294dbe84d1469d1743027))
* update SDK settings ([c597727](https://github.com/warpdotdev/oz-sdk-python/commit/c59772779c50cabc63bb881c01b841e5d3c9544a))
* update SDK settings ([628303f](https://github.com/warpdotdev/oz-sdk-python/commit/628303fee3ec94b583573b891e9ff136857a585a))
* update SDK settings ([621aa2e](https://github.com/warpdotdev/oz-sdk-python/commit/621aa2ea925c4946c2dbd362f71859c46554038b))

## 0.10.0 (2026-03-24)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([41658e2](https://github.com/warpdotdev/oz-sdk-python/commit/41658e206812a57e27f97c1f7e0be57bedcbd3c6))
* **api:** error and error_code as types ([9766f85](https://github.com/warpdotdev/oz-sdk-python/commit/9766f85585ff3553f1f366476a3a6806f2534b22))
* **api:** fix ScheduledAgentHistoryItem name ([ac75431](https://github.com/warpdotdev/oz-sdk-python/commit/ac754319e41b73d323cf9a36cbcf1c4dce2902bb))
* **api:** fix schema version issues ([9c2f6a3](https://github.com/warpdotdev/oz-sdk-python/commit/9c2f6a32fa06812860efa1d76893dd8d2b60d176))
* **api:** sorting ([0cc041e](https://github.com/warpdotdev/oz-sdk-python/commit/0cc041edf53d26c4f38c64faa7fd065d7a6760ab))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([4f3ec38](https://github.com/warpdotdev/oz-sdk-python/commit/4f3ec385748655ca8fde2457ffe402f8bf30db56))
* **pydantic:** do not pass `by_alias` unless set ([45e0377](https://github.com/warpdotdev/oz-sdk-python/commit/45e0377a495aa67b0ee7d4415cbf13b526dbbf7e))
* sanitize endpoint path params ([da2a124](https://github.com/warpdotdev/oz-sdk-python/commit/da2a124f15c2b69f67905cfe4b75b52d90ece562))


### Chores

* **ci:** skip lint on metadata-only changes ([c2c0d4a](https://github.com/warpdotdev/oz-sdk-python/commit/c2c0d4af8460e7d1d86fa8c14f2480323308b9a2))
* **ci:** skip uploading artifacts on stainless-internal branches ([1ef523c](https://github.com/warpdotdev/oz-sdk-python/commit/1ef523caca4d137def551560de8c8a75c761d0f9))
* **internal:** tweak CI branches ([21f9e2e](https://github.com/warpdotdev/oz-sdk-python/commit/21f9e2e8065a3202a149b3a2440c5adb7d084681))
* **internal:** update gitignore ([e9e4aef](https://github.com/warpdotdev/oz-sdk-python/commit/e9e4aef20150ac3560f00edc2078979dacde8549))
* update SDK settings ([b897579](https://github.com/warpdotdev/oz-sdk-python/commit/b89757977744858277d095a752392e2faff0bb71))
* update SDK settings ([e4510a6](https://github.com/warpdotdev/oz-sdk-python/commit/e4510a6259d03bf4cd24b40df6243f6c879e6fb3))

## 0.9.0 (2026-03-03)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.8.0...v0.9.0)

### Features

* **api:** manual updates ([26fc085](https://github.com/warpdotdev/oz-sdk-python/commit/26fc0852ddd9352fe7564cba64f34203d940ac57))
* **api:** manual updates ([1f89eca](https://github.com/warpdotdev/oz-sdk-python/commit/1f89eca19e244721d77837d5aafbf0e1de20aee7))

## 0.8.0 (2026-03-03)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.7.0...v0.8.0)

### Features

* **api:** manual updates ([1d27527](https://github.com/warpdotdev/oz-sdk-python/commit/1d275270bac34036ba2d2f9795792f2b71fdad3f))


### Chores

* **ci:** bump uv version ([646ee4e](https://github.com/warpdotdev/oz-sdk-python/commit/646ee4e0381123a3b24e63c4829e32c7ffc3160d))
* **docs:** add missing descriptions ([4777a8f](https://github.com/warpdotdev/oz-sdk-python/commit/4777a8fd9d5e9644a694695190d1dc6d4c1c9941))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([3c14f7a](https://github.com/warpdotdev/oz-sdk-python/commit/3c14f7ae100fbb6df1a9f7109fd77057cf10a780))

## 0.7.0 (2026-02-23)

Full Changelog: [v0.6.2...v0.7.0](https://github.com/warpdotdev/oz-sdk-python/compare/v0.6.2...v0.7.0)

### Features

* **api:** manual updates ([1b38e09](https://github.com/warpdotdev/oz-sdk-python/commit/1b38e0943935c83c0283523fc045eb2ff2f56109))
* **api:** manual updates ([73b719a](https://github.com/warpdotdev/oz-sdk-python/commit/73b719a978f70ae36bd374535d80372dfaf1d47f))


### Chores

* **internal:** make `test_proxy_environment_variables` more resilient ([de1744e](https://github.com/warpdotdev/oz-sdk-python/commit/de1744eeddf1780ca9bae2690f0ed0b17406754f))

## 0.6.2 (2026-02-23)

Full Changelog: [v0.6.1...v0.6.2](https://github.com/warpdotdev/oz-sdk-python/compare/v0.6.1...v0.6.2)

### Chores

* format all `api.md` files ([99ca557](https://github.com/warpdotdev/oz-sdk-python/commit/99ca5575a5159bc024bbf427d41a25347fe5b0f1))
* **internal:** add request options to SSE classes ([f66a316](https://github.com/warpdotdev/oz-sdk-python/commit/f66a3167892c0c98bd77f141ef325b5c2f576f09))
* **internal:** bump dependencies ([c487a61](https://github.com/warpdotdev/oz-sdk-python/commit/c487a61c88362ebc3b48785830d1e3b16bd7dcfe))
* **internal:** fix lint error on Python 3.14 ([25d5626](https://github.com/warpdotdev/oz-sdk-python/commit/25d56264996ae48e38696524f244e99a32316cc3))
* **internal:** remove mock server code ([e4b9075](https://github.com/warpdotdev/oz-sdk-python/commit/e4b90753f07d4f5da5a1075e893bb87424530cb5))
* update mock server docs ([c253a23](https://github.com/warpdotdev/oz-sdk-python/commit/c253a238f5902a71fbd033f3e0bc0ec74406e9b9))
* update SDK settings ([82ead07](https://github.com/warpdotdev/oz-sdk-python/commit/82ead07e4501a6e23e5db060074a5c180b0947c6))

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
