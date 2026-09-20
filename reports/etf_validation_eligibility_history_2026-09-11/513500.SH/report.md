# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`do_not_trade`
- 建议：不交易，直至补齐并复核缺失或无效证据。
- 阻断项：stable_parameter_region, missing_research_evidence, strategy_metrics, benchmark_metrics, strategy_exposure, benchmark_exposure, no_stable_training_parameters, run_manifest, selected_config, experiment_metadata

## 策略与买入持有比较

证据缺失或无效，不能生成策略与买入持有比较。

## OOS 分布

无可用 OOS 窗口证据。

## 执行、换手与成本

执行证据缺失或无效。

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-11",
  "config_hashes": [
    ""
  ],
  "training_surface": [
    {
      "window_id": "wf_000",
      "grid": [
        {
          "config_hash": "f6b877f3dea41247ace7a39e777e2d4b447a149ec4484b84b0ac6649e6790b93",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4428552102,
            -0.04779351249999987,
            -0.14922093740000014,
            -0.12978451430000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9f8d66390e22e841dbc879446df494747fe0e69404b4bb4c04c136d2b5046189",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.38775681250000005,
            -0.052671331399999834,
            -0.13958670000000012,
            -0.12014349669999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.33456291579999997,
            -0.05740152959999979,
            -0.12562650460000013,
            -0.10696503729999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "da28e066148553678760b45c21a54f0f815cb41838c646423fedd4acd0c69f0d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2809681173,
            -0.062409693999999766,
            -0.11054463500000014,
            -0.09270639929999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "90d6ff7ed79e50c4dddaaed58adbfdc177b6bf9b378de9d013c1d4240154e606",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.22911709330000002,
            -0.06747498249999972,
            -0.09622754470000014,
            -0.07880357589999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "43950e3f259617cc483404f6d6415d25f5b84e7eb334812843c5e9177958cce0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5102633808,
            -0.045799397699999855,
            -0.15943401460000015,
            -0.13375432690000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8bce2fd4652d535226e8dc035f7242084edc778cd386a1bba082c130a02ff6fd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.45470395790000007,
            -0.05062433919999982,
            -0.15751457830000012,
            -0.1293574806
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.39988945500000006,
            -0.05556395449999978,
            -0.15214058900000013,
            -0.12492873159999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "77bd9770c8d5ec308e8b7fd0fadfa8fbf6cead744a6e15323ae2a4260b80ad42",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.34578761150000004,
            -0.06051241059999975,
            -0.14613175190000013,
            -0.11797253349999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0664477e5295e0bc1c74559f720de476589a1201e90ca5c2c2645acf217e5a1e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2935121465,
            -0.06552829369999971,
            -0.13782340880000013,
            -0.10949609969999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5132cd3db68e157dd3153cb3ae9792dee9a4b1c862130fd622636843c2b36730",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5083360330000001,
            -0.043731891699999845,
            -0.16378082470000013,
            -0.13435167450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0a8f9b6084c1d444d5b9dacff3681205d0b72ae817079b8f300cb12517cbc6fc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.45282183220000005,
            -0.048625681099999804,
            -0.14892058330000013,
            -0.11966138630000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4673076614000001,
            -0.05358827519999977,
            -0.15499433430000012,
            -0.12247774379999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "77c0310211df78935d4962e65b3e258ba298c8d9fd368ecda7590f2158d215b1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4138720993000001,
            -0.05858527009999973,
            -0.15993245780000012,
            -0.12350957859999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2b1ca3a349c41d3e74f6ea219a4c0fe30f94bd0c8d69053d8a263b0a0abd2acc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3612909624000001,
            -0.0636950177999997,
            -0.14578106560000012,
            -0.10929800629999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c952cae7bd45116005f8eb31266d51ce6c128f513baffac095de4b6cb97384f6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4556310407000001,
            -0.05004996039999984,
            -0.15044740860000014,
            -0.12307278620000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4deabe0573cbeae491a145f8e4d20f916f5c910661a4c80d8fc5167f3190b561",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.49616933400000013,
            -0.04662584729999979,
            -0.16675096220000013,
            -0.13197327120000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4399702786000001,
            -0.05175246469999975,
            -0.15242440200000013,
            -0.11702652250000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2542c5a0c6a70a2692a3038a43bcea945893d0495b2c1713e03b0f9afdf6620a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4781680747000001,
            -0.056738973599999715,
            -0.16566965210000012,
            -0.12580809029999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c1f8d05174940de5abab81e70dbabad9d91d52b696bb409bdd2ab6d799a45da8",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.42733730180000007,
            -0.06186844089999968,
            -0.15131086660000012,
            -0.11164750149999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e43174b66cae18536744c3921b38ea3b06411d2aafef1ba96738db80f17ae80b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.442591191,
            -0.049725249899999865,
            -0.14241474640000015,
            -0.11944948240000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3986694fa6674e967c35c294ac4055fbd72f2cc3fda3b61e52db297456a13d8f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3875436806,
            -0.05458926579999983,
            -0.12798222150000013,
            -0.10511313710000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.33436993839999996,
            -0.0592986695999998,
            -0.11318740800000014,
            -0.09072589480000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "222df6d8f13727d94d27e59090092450a9d1437210027cc7ba1e9ed6e9669731",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2807777181,
            -0.06420295959999976,
            -0.09896003430000014,
            -0.07651214329999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1955c130371fbd273746ee973f8ff228037a1edbf3c4f5811acb4c15e0cf6dda",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.22895897919999997,
            -0.06922348479999972,
            -0.08473196860000014,
            -0.06236135449999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bb96bcaf6239a8f480b471f3bd6f4f2edad305f90a5fe68ac611f0a7034ec535",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5106800927,
            -0.04980696359999985,
            -0.15161267440000015,
            -0.12688789330000005
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "259b394408833371c897a4a9317235e9c836670ca8171b17b53da30eb4a6a0c9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4551564514,
            -0.054665850599999816,
            -0.14680134130000014,
            -0.11821128400000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3991236339,
            -0.05961703419999978,
            -0.14029739790000015,
            -0.108498597
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "183a91bd23a755b7e87e0ab603de83e23b8219e506dd76397e078a1cf902c167",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3462371772,
            -0.06436284549999974,
            -0.13216519740000016,
            -0.0976171025
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "260012ec18d23eb314b1bd71c33087541eee3662ea1fdbc37c0ba619bcac2dbb",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2940345753,
            -0.0693504585999997,
            -0.12064685450000015,
            -0.08378378909999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c848623e0be20099dc48e20d39b8cb65688053a8a496ec4aa885783422556572",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5069183859,
            -0.04780811839999983,
            -0.15456568430000014,
            -0.12797624850000006
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "08bb1f5360f9a1daa71255445b28f2b85a25bbf9afeafe227384fc93068725f1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.45145550230000003,
            -0.05263201309999979,
            -0.13993402900000015,
            -0.11329485610000005
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4662300472,
            -0.05968054759999976,
            -0.14344084740000015,
            -0.11239832780000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0c65d2ef761411d63b3e7d181c2d998d0df2dcf703efd602be2fad87e1da59dc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4128054635,
            -0.06460133589999972,
            -0.14372297670000014,
            -0.10721598339999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3c50ec6e404a0402a3f98be24cad12d2a6bb4f1a9ce1917679cbf45896f6efd0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3589514034,
            -0.06967959709999968,
            -0.12936403920000014,
            -0.0928433561
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "13140adfdb638ee59aee50db7ac7a68bf94b4aeb3cd69660a93f3b3954d57fc0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.45820274990000004,
            -0.052853488699999854,
            -0.14159785110000014,
            -0.11590388840000007
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6d151393122f9975d3a3fbbdfde74da7330ecc39667716a01b5d15571ac979f7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.49312860160000005,
            -0.05216761919999977,
            -0.15493869150000014,
            -0.12345401830000005
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4382423917,
            -0.057018628799999735,
            -0.14014642170000013,
            -0.10899127500000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "80899914e7291fc258eeddf6520efbf7fe1b0287b99fc96d0a62841279df7425",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4766639456,
            -0.0648019428999997,
            -0.15024137220000014,
            -0.11261156640000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4769bcc53bde368b7006c19ea230e03bc28764d38036f94954f64cec059dcb85",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4235168696,
            -0.06974131379999968,
            -0.13604684090000013,
            -0.09837109830000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f6d7509f3f5c1634fea76f4dd53e98841aa76151e5c756d7dfd55b79d67dc8f8",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.41828414729999996,
            -0.04667265869999986,
            -0.13284034190000016,
            -0.11212250490000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cff9859d4a5f2814140612668f4daacf34db624bbfeb4347eae64ec9f633685b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3635592311,
            -0.05146845129999983,
            -0.11704208440000013,
            -0.0977861596
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.31049913269999996,
            -0.05626881159999979,
            -0.10247211450000014,
            -0.08347489449999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9b285843c53cb0e98fbb611366f677a98327b135bad0b9ffb777bf5f8f2ea648",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.257144641,
            -0.06120277549999975,
            -0.08824484050000014,
            -0.06911066449999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3b113e92d617b95e71b3d485144a8bf07623fdd5476c359cde7bf0af5e60b9ba",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.205573628,
            -0.06621340369999971,
            -0.07389581110000014,
            -0.054959875699999966
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "eec8e6bf15537c408060e82aa9252bc11c299b5ededb53194b719629a246267c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4622680851,
            -0.043824594199999845,
            -0.14740802510000015,
            -0.12339104270000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1fb848b69f408dc3ba8d7bd85ebc85edda0535045ed94aad7ab28c6599beaf4d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4070893658,
            -0.0485793756999998,
            -0.13852909050000015,
            -0.11171533339999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3515406045,
            -0.05344461319999977,
            -0.12687423730000014,
            -0.09744757889999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4734c020226fa7443033daa844967e4699044f02fbfcdd5f6005cd5984d5532d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2991167945,
            -0.058463440599999736,
            -0.11267494640000014,
            -0.08338098539999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e062b42fc995eb71bc33d23b0a1a7171cd43966949db71673235e334018a8b9f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2473702289,
            -0.06338038449999969,
            -0.09655089670000014,
            -0.06902235539999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0380f680c2ed4cb0751113688c497ae2ca73f1769aab860b0851287c65fe1fac",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.504645749,
            -0.03986788649999984,
            -0.15280975570000013,
            -0.12757486680000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a7e68e5035096e8601e3fc70bed10c2f2d51007849d3f7759c8601c0d59a51de",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.44937504240000004,
            -0.04462385949999981,
            -0.13814910910000014,
            -0.1131440262
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.394773152,
            -0.05069663809999975,
            -0.13716436430000015,
            -0.10767082399999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9f72db2d6091f70ef6f2c28a733136150b7d98312604e238d2900953d4d65ab4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3421011008,
            -0.05560448739999971,
            -0.13197922320000013,
            -0.09731035919999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1b7e2c5e7b5958dc5a4167102c649e3905f2a20047667578f26da46fe53ae2b2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.288891669,
            -0.06062155259999967,
            -0.11770471590000015,
            -0.08329167629999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4fc55be6dc74c3f50156a7e114ea4978acdb95ed567f20d6bbf0c18ba03b48c2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4554220134,
            -0.04371786369999984,
            -0.14083807910000015,
            -0.11823218870000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c828166e74ca3a3a5edaf08d9a9cc9318061f12eaf8a971288d9fe9aa94f0002",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.48999724510000003,
            -0.04156168019999979,
            -0.15263092850000015,
            -0.12283852769999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.43527608570000004,
            -0.046355397299999754,
            -0.13805105050000013,
            -0.10852726259999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d6dfb2a62a2c81350ef9e449a06dc69ac134a1e3741a97bf3776f014a02b7bde",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.38232062380000004,
            -0.05286773889999968,
            -0.14197648580000014,
            -0.10597783449999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4e1a984b1c95dcc573ae3ac61d76713bc6516583278750a0006153bff7d9df6a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3295667789,
            -0.05794115099999965,
            -0.12761754830000013,
            -0.09206321919999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "589b9e99b2cc99c9bf11c7d143c4316f35fae491362d7df2a95b2a38cea057ef",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3999848709,
            -0.046696015699999864,
            -0.12546423000000015,
            -0.11406790610000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "446dc1803e4c7a85e81fa0757a3f673cc8f49dc153680f00a73418f382fe40fc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.34510591069999996,
            -0.051503562199999825,
            -0.11087147410000014,
            -0.09973156080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.29211878729999996,
            -0.05627293179999979,
            -0.09637602630000014,
            -0.08542029569999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "61a86f69f97281212bca1d76dff4959aded7bc8ae179fd65e9a35b51766efe9a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2386080785,
            -0.06120967359999975,
            -0.08206432210000014,
            -0.07132121449999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "266908ce86922ef9e2da585eb6b06dc860b8cc72327a6b50d62c098f123fd428",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.18705467539999998,
            -0.06620228219999971,
            -0.06787124590000014,
            -0.05717052569999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "db3ce2343cab6d1650bea124ea4ff260409091058133b2b9bd6fe8a6fd2ff9a4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.424444383,
            -0.04415675089999984,
            -0.13885931280000013,
            -0.127035561
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "deba15173d77c901d382e9f5272229ae1cba6daa2726b4bb6ce9634e86a14da7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.36811375869999996,
            -0.0489256765999998,
            -0.12715268230000015,
            -0.11586517639999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3147967439,
            -0.05376970009999977,
            -0.11268367360000014,
            -0.10155043599999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a43d42200543c8fee6ecea4bd84917ea1bcf540d535e043f6a521a06832f55f1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2611866325,
            -0.058723695399999734,
            -0.09845639960000015,
            -0.08754932539999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e2cff1ab7f737919236ab95a7fedc68c273418b1b4245a5f6ac6c54916c93f70",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.20937171519999997,
            -0.0636705831999997,
            -0.08413636150000015,
            -0.07354663949999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e15d48069bf09f9bb10971f06b1a917c4b07e6c1a074d0d1388e0185650d24cd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4477551883,
            -0.04165261799999982,
            -0.14476334820000014,
            -0.13255593670000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5a17506ad28bbda515701fea8e5e9ce9e4f8bde66bd49b5febd4aad94e2a76b2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3923441972,
            -0.04650695129999978,
            -0.13025711080000013,
            -0.11827657429999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.33889845620000003,
            -0.051322542699999744,
            -0.12476126420000014,
            -0.11265189389999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2850114145,
            -0.056309914199999714,
            -0.11495750910000015,
            -0.10356997489999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b54f48b12b36135d832f2f0ecb43d61a4941bcf07a971027a9accc6831847aea",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.23293337539999998,
            -0.06128369389999967,
            -0.10063901500000014,
            -0.08977475039999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d726ac15f78e72d7171a62d66dcf57ed06bd6d2e3d2d36113bbde161c0666e27",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4722219736,
            -0.052652419899999844,
            -0.13832392250000014,
            -0.12511321210000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3b8400990f65f2f5c0b5d93d3ebecb37df16eedcd649695660efe4d79ce973b7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.41664630810000003,
            -0.044067944099999756,
            -0.14192786270000016,
            -0.1298186247
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3616972556,
            -0.04889643159999972,
            -0.12734798470000014,
            -0.11550735959999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a8b1e9c488ff9b024597f84b549df68bca23d0664c4df78a57248136fcff3c3c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3087963077,
            -0.05379925239999969,
            -0.12528676100000014,
            -0.11312218799999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "45451ae22fd54f5fcc4a8c83f4e0e0fcc2755c40142cb91352153ea353ce96a3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2552991181,
            -0.05885097399999965,
            -0.11113767160000015,
            -0.09921747269999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e5da6823593cc26f966c1b236eb2179524508f51ac24bb8ecc1ae9cf0512a2d2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.398875989,
            -0.04567866729999988,
            -0.12431357530000015,
            -0.11343657190000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0cbf63fff76abf8f86447fff223cc640736f864eaa9919c9dbc89d1c0d125adb",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3440937491,
            -0.050455223099999835,
            -0.10968192000000014,
            -0.0991307411
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.29010289559999997,
            -0.0552446427999998,
            -0.09519738000000014,
            -0.08482647389999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "961cfe76def7b11fe2351283e3ebd181a0c11106d5a65042f1ccade8bdfaaa3b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.23799357329999998,
            -0.06017699759999977,
            -0.08088721980000015,
            -0.07067388509999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "17c7279512899f3a91bea351e1b53d236bffc52f4a909e0f96befb2127ba1987",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1865170584,
            -0.06514217119999972,
            -0.06666460800000014,
            -0.05655371079999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c2723042d21e0f63b5e375cfd0cc6b239d7d1319ce461a03c6a1a2ef7049a724",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.42219111499999995,
            -0.04220520159999987,
            -0.13840944780000014,
            -0.1272165067
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c732a62eeaa84162fc5a884fcc09486a2b9ee5c9039b8d9a0d76f72351d048d6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3673126472,
            -0.047029742999999825,
            -0.12635792080000013,
            -0.1146360216
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3118273383,
            -0.05181916269999979,
            -0.11034491990000014,
            -0.10045676419999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5a60d04000e8a42a7ef2a4dfd58e04047fee6e55af55b1d752e8f78c30a7fad1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2595636328,
            -0.056760747399999756,
            -0.09609465280000015,
            -0.08633468989999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5d600521d8ec100f51d0d336c6543e9781171444d584310acb517b6041a05a64",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.20793183469999998,
            -0.06176497649999972,
            -0.08187204100000015,
            -0.07227849639999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "21afa2e296937da975f586f16b52eb519be169e613d16ecd15cd50de513cdbcd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.44409656929999997,
            -0.03877972149999985,
            -0.14389815230000014,
            -0.13298433180000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3891281155,
            -0.043604262899999816,
            -0.12939191490000015,
            -0.1185534912
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3348445927,
            -0.04836729169999978,
            -0.12389606830000015,
            -0.11292881079999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d6b5f0adf9731cb102e277bd3fb3c7f60594548d2231a497b32c94673cd0b667",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.28239487459999996,
            -0.05338815269999975,
            -0.11356747070000013,
            -0.10173100309999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "757cb14275a89bc4c9e5a29a7520d973e34a22ebd3401c538b8a321442b8fd5b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2306451196,
            -0.05830860549999971,
            -0.09924397810000013,
            -0.08770532409999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b6449162a482e7a08f99c096b1423ca1e879ffa87022184dd0cff292e8213cf6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4673195683,
            -0.03538063229999984,
            -0.13742419250000015,
            -0.1245933681
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4948e389709741f3f9c362d58fe2624e794f41e6d5ef2b7968b00962535749d6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4121177022,
            -0.040118567299999804,
            -0.14102813270000014,
            -0.1303389922
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.35646901129999997,
            -0.04494181159999977,
            -0.12644825470000015,
            -0.11587624889999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2b8cce8c37110946254601751fec91e8b1a3052ace950c33d369bc1269f4e54c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.30389963919999996,
            -0.04996277259999973,
            -0.12438703100000015,
            -0.11364955339999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d8d5c98b26ff14e3212cd6294dddc02b69e28e1725828e71a010ae9c00e64f87",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2520841245,
            -0.0548729952999997,
            -0.11023794160000014,
            -0.09959335989999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9b0ed793b8789210beddbfe561da3142bf989c157269bda13aa9d2e732098470",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.39863807539999996,
            -0.04553343299999989,
            -0.12440354830000014,
            -0.11259762260000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "529b14ba63795fde28f27d0ddc49d26555b3ea64714f8b42d3e97419429806f3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3439925855,
            -0.05029775889999985,
            -0.10977189300000015,
            -0.0982612773
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.28990097119999997,
            -0.055087178599999814,
            -0.09528135480000013,
            -0.0839570101
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3cc7b53f43c230cbc0bbe5e407576b80e5c3c8401dd8cf82ff397d5c07f70d48",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.23777701699999998,
            -0.060009656699999775,
            -0.08110461010000014,
            -0.06980442129999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b313af62bdd5d8e3e6b7fef4e167294ef0b09dc0cc58c92f6913a9a1385bd71c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1863421259,
            -0.06496270039999974,
            -0.06675058220000014,
            -0.05565373249999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c043be32382e64bdbba090ec810f1ccf50a09fe8648fc8a3408bbd2ab9ac73c6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4216382959,
            -0.042020480899999886,
            -0.13898527500000013,
            -0.12741144820000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "45fc5ff3ccb51fbcbd9cfe0f8880bfce401d63eea9bdb37ca7711e56fdfe51f1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3667721881,
            -0.04678480679999985,
            -0.12706716350000014,
            -0.1129806076
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3113464976,
            -0.051564449799999815,
            -0.11052686530000014,
            -0.09877083569999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7c2b3fc2dbedd2b079ebdeca8887a83fb588fd2a1d89ed4f35c2ff52d779728b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.259109784,
            -0.05649380459999978,
            -0.09627060000000014,
            -0.08461824689999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2893c794a262dfeeb1d55eb234d4bbc50613e92208bd8509d365e79e48e8e243",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2076637595,
            -0.06150311899999974,
            -0.08204998760000014,
            -0.07056205339999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7826433e193e4ac82cc351ff0995a6b514018d7da192d993bd018af86f9827f0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4433386028,
            -0.03851730549999988,
            -0.14489530860000013,
            -0.13327524450000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8cbfd1cd2d9316edcb8d2b295fa7dd39a4888c1b6c1a9fd7cd02af0f71389581",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.38828174819999994,
            -0.04327185469999985,
            -0.13026365330000014,
            -0.11884440390000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.33404321189999997,
            -0.048012876899999814,
            -0.12490122220000015,
            -0.11321972349999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "77548bc87ab8ee39a946a4bb2c139e0addd6da3a1b8a8eb663acbcf366d946f3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.28167110679999996,
            -0.05303872319999978,
            -0.11436277650000012,
            -0.09922561079999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "23c50db9ddba5ebfe44269566b665b6b65bbdf61def5dfe671d025e6d5a010b1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.23008489369999996,
            -0.05793746939999974,
            -0.10025712960000013,
            -0.08537587899999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8a8f91fb3f844ba6dfc5dfcf5bdbde75f84903dd70fbf2739c509a094fde215b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.466100949,
            -0.0443309173999999,
            -0.13742419250000015,
            -0.12498325110000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "812af4d1fa0b091fb7419ff0da1d71ce91fe65a0a3224bbcf41431dcebd0b08d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.41108081939999996,
            -0.03975890259999985,
            -0.14218778470000015,
            -0.1307288752
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.35538535149999995,
            -0.04449992479999981,
            -0.12774132220000015,
            -0.1162661319
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cbe67dbd8ea3ade52ec52ba1d9625b2a6f87d9e55ccafd9a64fd847a889053cc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.30299791589999997,
            -0.049487350299999774,
            -0.12568809610000015,
            -0.11403943639999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "461c154a7e2353f2283c499ac85775b992b924de41d0fec46d9f06b5172f7142",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2511007977,
            -0.05441408719999974,
            -0.11141358880000014,
            -0.09998324289999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f06c82a4eeb01c2ca1b3775d507f3fdf523eac9e7bd4f72ae421cb474e7f3e8d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3997328614,
            -0.04777088509999989,
            -0.12450946880000015,
            -0.10677112270000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fde5f8993452adb198b2aebe545089a0c13eb1c9000759d5e47c483b81d0ca3b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3450259135,
            -0.05257383179999985,
            -0.10987781350000014,
            -0.0924347774
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2908728412,
            -0.057363251499999816,
            -0.09539281810000014,
            -0.07797203409999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9b49243fc490f86a5308087d28dcd0c8743ca5e9e7f2f9f5645275731e7a26ee",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2387110582,
            -0.06229540629999978,
            -0.08121607340000014,
            -0.06381944529999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "46f84d8aed1026e2d80d880921222dcafc41aee81ce7ffb4371076fddea389b7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1872147091,
            -0.06724844999999974,
            -0.06685713590000014,
            -0.049668756499999966
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a742864c7a1208b39c7fae284c174b8dd0af4d1de90c2fad405dab24d97015e9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4238936841,
            -0.046624229199999895,
            -0.13884531700000013,
            -0.11544351060000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fd673b08ae5457fc2c262ed05bda3c5d6934808f9935cbade4c0d6172f79ad0f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3688739313,
            -0.05138855509999986,
            -0.12532623040000015,
            -0.1011071653
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.31332532479999997,
            -0.05617797479999982,
            -0.11075880420000014,
            -0.08664442199999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0be1879f481ad47d63cb1e9e3839ecd1e8b8a47f13b42f9c203ebdd2d8b36c92",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26096569519999996,
            -0.06114575039999978,
            -0.09654352660000015,
            -0.07258632849999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cd527804e36527d86170dc60b7b5297223c9325a141bce31c0379910247fe5f4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.20936662569999998,
            -0.06612818479999974,
            -0.08231800460000015,
            -0.05861510949999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "02951609451a1a3666f9e27a5c317b82fb9d83367c6c4907f4a9d530a074a829",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4467380638,
            -0.04547757329999989,
            -0.14489530860000013,
            -0.12411589849999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "18fc14e280c2cfd24eb7a861ce0ea745639459e640b134c7b93c1eee85bd3f1a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3915204644,
            -0.05024189919999986,
            -0.13026365330000014,
            -0.10977955319999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.33709045429999995,
            -0.05503131889999982,
            -0.12468728640000015,
            -0.09549627969999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "64e3052ef8fa0319a7c2533e42c13b53422f82ad86eb68d7701d663c462fd129",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.284513146,
            -0.05999156439999979,
            -0.11170966160000015,
            -0.08143818619999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8088cc365f89e6679290e380387e1324139d60bed3aa5ee409fd03ee528e9a99",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.23271482989999998,
            -0.06493820809999976,
            -0.09759147400000015,
            -0.06738199269999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8bcb1085f091f1ae946199c14e23c1ba1e975e65f06096e4aa24df9a5387bf01",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.4707839282,
            -0.0443309173999999,
            -0.13742419250000015,
            -0.1211153645
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2ea28b5fd16155856db1a6aaf045c7c6a38ceefbc42b4e51cb92f1e5a3291080",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.41548723759999995,
            -0.04905662249999986,
            -0.14218778470000015,
            -0.11853691559999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.35954293789999997,
            -0.053884662999999826,
            -0.12774132220000015,
            -0.10416866759999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8e9ceaba7690e6d3faceede615245b6d1a7554518ab91ac3b377c4df97f4c0a3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3068827413,
            -0.05884490849999979,
            -0.12540218190000013,
            -0.09011057409999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fb7cf5a396194be308efbdd959d12d7a0c48b1193d5a2caac5caa3adc4c65a92",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2547430911,
            -0.06378142209999976,
            -0.11112567520000013,
            -0.07623385039999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "318930da62df7a9a4b135893117f29e6080cdee95f09a82d0197d3413840c2a1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3772771561,
            -0.04777088509999989,
            -0.12234320780000013,
            -0.10648320910000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "824e648c83a8f7c5d611f1044280116ee112dafff48f1898aadbcdd7cc416908",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3226313048,
            -0.05257383179999985,
            -0.10776499200000014,
            -0.0921468638
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2686580845,
            -0.057363251499999816,
            -0.09315457870000013,
            -0.0776841205
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "71cb3c31412438e23d4b9bff35ae94c701cf15c333086d98008bcf43077b98f0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165663954,
            -0.06229540629999978,
            -0.07886732270000013,
            -0.06353153169999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "65e02eee14f0acb0a825dacbe164cfa06365c84cde2b215e2174efcc30cf82c1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.16524989829999998,
            -0.06724844999999974,
            -0.06464180070000014,
            -0.04938084289999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a10c8020a0773c04afed2636a58bedf090d4fbf98ff1d3b60925e0ea4e097776",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37754707509999996,
            -0.046624229199999895,
            -0.13743728400000013,
            -0.11486768340000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3738ae7a721e173bf76984f66c2f685bc435209fd4dab537ffc550a62a23d7b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3227734711,
            -0.05138855509999986,
            -0.12102715390000013,
            -0.1005313381
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26890101159999996,
            -0.05617797479999982,
            -0.10641674060000013,
            -0.08606859479999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "19d00bceaeaee45b90711aedc56891ccd0aec187c04e0c1df0557f9894ba521c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2167913279,
            -0.06114575039999978,
            -0.09212948460000013,
            -0.07201050129999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "56cb7fb31d203469a3f1c85e5c30ae6f448173b6cf02c6203dc31a8c63b6dd5c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1654568362,
            -0.06612818479999974,
            -0.07792686680000013,
            -0.05785981249999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "aa322358aee7ceed5d28526185f0ecc94c244a13c6344d41457546a6a739dfb8",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37782599139999995,
            -0.04547757329999989,
            -0.14609940280000014,
            -0.1232521577
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "25d46927d3049e38377b2aab3cdec3957e2a5adf6b1a27fe97889bc46891180e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3230253955,
            -0.05024189919999986,
            -0.13146774750000015,
            -0.1089158124
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2691439387,
            -0.05503131889999982,
            -0.12254901700000012,
            -0.09445306909999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "daa598de199db4f2abe5d43ad5487cc9e98f006ac89533dc04afd523606d5df7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.21703988959999998,
            -0.05999156439999979,
            -0.10539164650000013,
            -0.08056544809999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0752a8b6c7a878a88b448142929f6a9f3be2c1ed8c4201bee06a7d6faa25ea99",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.16569260349999998,
            -0.06493820809999976,
            -0.09102507790000013,
            -0.06650925459999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a6454c26597b01d0276b684c62019f613b394f2ff7eaaf890673936236e2a537",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.0443309173999999,
            -0.13897018410000014,
            -0.11996371010000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bd323451f9997167020ef8b4d4563d57e755f853e5a756382be5fefaf5d43de9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3232863172,
            -0.04905662249999986,
            -0.14373377630000014,
            -0.1172057914
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2693868658,
            -0.053884662999999826,
            -0.12928731380000014,
            -0.10300801589999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6b5bf2db39c7a5312bb922ccbb7f79eb56adc7b97c17b591d33d8da2a6250bc1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.217261025,
            -0.05884490849999979,
            -0.12250868360000011,
            -0.08894992239999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "edcf6df73115739f59495a635a2f6e95889a072a90f65715f3683de0279b6036",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.16589954140000002,
            -0.06378142209999976,
            -0.10819364400000012,
            -0.07489372889999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "89ad7adcecda2efcf8cbd6a6401ed3e6ed96b851083accd850f6a0c518aa15b3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04803143929999989,
            -0.12055174540000015,
            -0.10509410230000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fbe5f873390f4fa9623ed2084060dd9b386dcb41caa2b71b95f0f2129cf57a56",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.05279576519999985,
            -0.10596053350000015,
            -0.09066326170000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.05757918669999981,
            -0.09135012020000015,
            -0.0764254982
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8d2fb7a3cdb517396e8b9acf88ea220280c39c0d59402311d007504ddef79d5c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.06254976229999978,
            -0.07700942470000015,
            -0.06227290939999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e2c8bb705339dcc5463a443085ff18111efcc79131fc23f37b0689f00224e812",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06746438519999974,
            -0.06280535180000014,
            -0.048122220599999974
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e63647ca2002739cec51718c1fc3233e1fa1a415c34c193d001a7c1cd59f7a79",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04706809599999989,
            -0.13360452310000015,
            -0.11221995430000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8d4112ab3315d7d1ddc27a4d870f5e4b35afd1d22a3825b4b4fafb3f73ad8f3b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.051832421899999856,
            -0.11704798140000014,
            -0.09778911370000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.056654464199999824,
            -0.10274029940000015,
            -0.08355135019999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1421bd391e699bf7e3db84dd519ed0f9abd810d6436050bef6fa5aac1639def6",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.061583618999999784,
            -0.08844004730000014,
            -0.06939876139999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d6db03d900f41c0c72fa21236bdcea5a570191d0749630206087c435ff3a8898",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06656005519999975,
            -0.07409101790000014,
            -0.05532157419999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5a99c08a7ed7f5f806cf0a005980f33c6f44c53c9af3ff9ec74ea537e9ac3156",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.046118380999999896,
            -0.14170281110000013,
            -0.11927230470000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a01c832be39f3c46cd5b376ca93ac9936e7882bf59f762681abd6bb6e5fae186",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.05090769939999986,
            -0.12707115580000014,
            -0.1049149657
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.05569112089999982,
            -0.11690225600000015,
            -0.09067720219999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b66db6d06efa7d1e620ced97604377222cfc7a690e9e12414f834e4ae2dde28d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.06065889649999979,
            -0.09956793860000014,
            -0.07659811499999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "290d66f51c3334521564ebbf587b2c8f96dd3feca2c2d788144f482ee2e0e5c3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06559201189999975,
            -0.08533333040000014,
            -0.06267240599999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fa155e38f105769756379f1664a8105153b41ea206f3fa703f1dea61f6e2fc4a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.0451936584999999,
            -0.13589619550000015,
            -0.1173809615
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "26296eafe932dd4ff9512c67b6adb54a054d9512ee6fe088c015bb6b30ae16ef",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.049982976899999865,
            -0.13779119300000015,
            -0.11204081769999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.054766398399999826,
            -0.12350413820000014,
            -0.09780305419999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "20c920b02310daf4b859f8b813f29af3b4d257da9ba48b2d64b95f4328dde275",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05972064569999979,
            -0.11502047520000014,
            -0.08372396699999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4b29dc52dae93fa89372642c660f99eeca7df753f4baaa1174e66a58541fe27d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06468968189999975,
            -0.10074242450000015,
            -0.06979825799999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ca6aa7709729328d94aa19e8129a8ec3f86ce1d32039e064fb623fbb8f1ac58e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04719005939999988,
            -0.11880676580000014,
            -0.10531103720000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c4e015ead6169a716f5f5e9c559d43e096fc921f96389ef1a18f5749d64d333b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.05195438529999985,
            -0.10417511050000014,
            -0.09103867270000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.05675143509999981,
            -0.08967811870000014,
            -0.076649431
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "dcaf4f81927c472859f6300f1b7ac9cec525bb1864c151d3d4070612ae8e5df4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.06168358989999977,
            -0.07536795850000014,
            -0.062496842199999986
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "eb49287bc547c6e506f3aadb7eda6b7daada828a03319fcee65cf5fdd3c3fd6a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06663663359999975,
            -0.06100902100000015,
            -0.04834615339999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8001ce7a61e6bbc527399ec1395b7cefc4fdc1a06d706c582a8a9beb5ebe3b02",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04541459219999988,
            -0.12828520830000015,
            -0.11266082200000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "268cf23cf0dce23398307940260e0cecf8d96d17daf5edc865eaaa770f936901",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.050178918099999845,
            -0.11365200900000014,
            -0.09838845750000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.054937347099999805,
            -0.09915501720000014,
            -0.0839992158
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1543bfd39152b539b9476475cdaa1d411c13d91f416cbff3ba8211a1b4f61a45",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05991458749999977,
            -0.08501871590000014,
            -0.069846627
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "11a928c621365eb7f902d7635a77ce6899022428a591ed6644c79dd42f8bf607",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06486603119999973,
            -0.07074266460000014,
            -0.05576943979999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d6db90ed5261d686d5775a7fe7c23cbce9b135bff6dee12a51a8f348722dcbcd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.043639124999999876,
            -0.13795902350000014,
            -0.11993710520000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a71457d47e5c1fa6cd81dc8bc2295e36bc60f4d0e12fac791b33187fe27c62b3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.04836483009999984,
            -0.12341179840000015,
            -0.10573824230000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.0531712446999998,
            -0.10872288840000013,
            -0.09134900060000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "04c0ca5fbcf902e5b9afe76b36a90ca3ad2104030989324ad9d294df660cfa89",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05810059949999977,
            -0.09449561440000015,
            -0.07726991339999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "64ca51cf505764cc7dcd808efa152085d9373da22f33c6e151902050d8ddf2c4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06309532879999973,
            -0.08021801910000015,
            -0.06327770069999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "26b18365a7e4237cc73053f1f6c404fdd94246aa4e16544ee34c6b1bfe516a85",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04182503699999987,
            -0.13544932960000014,
            -0.11826969480000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6c762a7a83d430eb4aae46bc3b939d9320278f039a0d1733b209ae55c6e64f75",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.046589362899999834,
            -0.13285676270000013,
            -0.11301452550000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.051395777499999795,
            -0.11836131490000015,
            -0.0986987854
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a6346dd7e1804c75cf8dd0eb15ee8b4c4797741b2f0c1cb674ef99891c3fa9e9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05637311789999976,
            -0.10414791580000014,
            -0.08477817429999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d3c336ea2c30970cb838c9559f28ef5afffee91fabd06beb0c1839e49256766d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06127864079999973,
            -0.08987032050000014,
            -0.07070098709999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a38ca9017ee7323d6ca2fa38e717ced6f522427e0f6ce2d771d4ec8eeb087dcf",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04719005939999988,
            -0.11839988790000014,
            -0.10441130720000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8f4a1199d5a21df79951d1f560023a1fa23122d88707a3f69ce4c077993f95e8",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.05195438529999985,
            -0.10376823260000015,
            -0.09013894270000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.05675143509999981,
            -0.08927124080000014,
            -0.0756761994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4db6c5d5762841c37dc4de1bc30a10cd0e27c01bfab964bf6c8365bcc5313082",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.06168358989999977,
            -0.07496108060000015,
            -0.06156712119999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ffcbf75f862ff7b602b47b861df9fc8a853843804e38aef1f90875d90a3822e7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06663663359999975,
            -0.060602143100000144,
            -0.04741643239999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b3b9838498a218b2c75976ab65e15e6c8076bb286d1ea658b3fbbf8b7e944b0b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04541459219999988,
            -0.12747145250000014,
            -0.11078786040000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9aab49f04c34ce9b0218247ceb595fe069b32faa5bdcebea8b02ec4761a1c832",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.050178918099999845,
            -0.11283825320000014,
            -0.09655900650000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.054937347099999805,
            -0.09834126140000014,
            -0.0820962632
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6a052b308f6ab167426ab2a7e99b79c37ceafef5132f04f03ebf5c5e3dece9d5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05991458749999977,
            -0.08402955720000015,
            -0.06798718499999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "081a8609b5d2788de7dedead3776df8fed29be1556ee3ac5015b21181e073d7f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06486603119999973,
            -0.06975350590000014,
            -0.05388000679999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "064c3f82e8595dcab77015ea88579873dec1e16e29d5a987e51204197ce9414d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.043639124999999876,
            -0.13656298690000016,
            -0.11716441360000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3a2b9e6812b3f6ca0f3a545088ae9cbf0150071f297f84c671e4ca96a08d7fb",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.04836483009999984,
            -0.12201576180000015,
            -0.10293555970000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.0531712446999998,
            -0.10741128200000014,
            -0.088516327
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0cad56c70b53c6f45b92078a0eb03bb554e4515d6c3eca9cc7cee91426f915e9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05810059949999977,
            -0.09326398400000015,
            -0.07440724879999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9e3707d9ca4dd26f414d299f19d60bc43cbdbf2bf2b6da6219c626e1973457ae",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06309532879999973,
            -0.07898638870000015,
            -0.06045854669999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4e816f70069fec6fbef680ba41095962ee77e9ff072ca18af5f553cdcfd997e2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.37705723709999994,
            -0.04182503699999987,
            -0.13364641510000014,
            -0.11826969480000003
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e4fc4425fef1519fb6942a195045717cd0d7d9196af4d4bbd9def08121347069",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.3224293804,
            -0.046589362899999834,
            -0.13121825440000015,
            -0.10931211290000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.26847415469999997,
            -0.051395777499999795,
            -0.11672280660000015,
            -0.0948928802
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "40da851baa2cf49bf7ef0a57c4209c8c76198f9c0a177a116a76f059fcdf01bf",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.2165102183,
            -0.05637311789999976,
            -0.10233400460000014,
            -0.08094227809999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b846a0a7e4c43066dab6457e533f7c7c435e82ee1372dd35cc746ba1dbbf7394",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.1650929604,
            -0.06127864079999973,
            -0.08805640930000014,
            -0.06687861049999998
          ],
          "positive_window_share": 0.25
        }
      ],
      "trend": [
        {
          "config_hash": "1fec94aa0bead42b20075940b637e819472c020dce8613fa5a3c7aa21734fd06",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.1485066816000001,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "adbca544282724c5a7a2958f71250737af4685caeb95879a42bc97e6fba41fa0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1485066816000001,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e731b06b6b8a57905247003db6fe52b6b03c796f946f86db5ff1d9a78d7bc936",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1485066816000001,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "46f7afbe4f52f52cf8832a43b79598af956b8e0d3541d6425464a97964d756c0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1536050566000001,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0efce7b04e5e193de8d96ae22d700309b50d9ec1b26b72a73c3a1a9f6769501d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.14711699530000008,
            -0.12063378330000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1b03d2707a07fe802f1760263c82b3d4b8342a455e2139542829ce33055346c3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14711699530000008,
            -0.12063378330000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cc26b8dbf9aabc5a954cdba7f15445f6906c516ab4ca332c472c7970122b880a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14711699530000008,
            -0.12063378330000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "de68c4ccc59411bff11772363170338b6761dbd0f39bd7fc8c794de5cfd5259e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1536599970000001,
            -0.12063378330000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b3ab56d68fdcaada002d2614a264764fe445837a7212d9cef39fd0934e9a098b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.1473674157000001,
            -0.11864429210000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3b3386f66538a319e0467b3a0b591520efa06cc1ee02fe2bfe05a4bfdea1895",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1473674157000001,
            -0.11864429210000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8bf92734c3d2ba8e6c3dd7f599c5b43e34620f9479e5c24f9b34ccbe045b4947",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1473674157000001,
            -0.11864429210000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cf9cde26dba3c73a5567f30c5d5a03c684d25c008ef9fb3ad24b61ff1e53e962",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1536599970000001,
            -0.11864429210000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0c441452555d21094fcf63b740acffe7a9176260632649cedf006f78d5c922dc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.15003043320000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "23d1e52eeccaf4bc0cb8853853c2be63a69dd7762b18d7289741c7e7f37b98f9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15003043320000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a5c471fd8ef46b803b80689400b2fc0c30d0ff6a0d4e6a27deb9881f27514916",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15003043320000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "37ce18ea991b11a33fd546c75664f8cafed609d4a7311f44011f1ac689f5ecbe",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15333240340000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c4ecea34d33f8e9ff517190ef1639a0078c204de4df752764eafe9f1f8ec39cd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.1487305885000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c4d5b093333d5f925ed448b6d6d3817b80258f4b6df0402ff62d7ff6e5de0d90",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1487305885000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ddcf08c0eb422a69906267785f04df8ddf6ada327f9f7dbfc623ef071dcdcb28",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1487305885000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "548bde01f4ae3b39c455be93505eda30b321c79668d9f8acde7f81aac0feefc0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15333240340000012,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b1ce106b9791d9b2313e33ad5d36230eb1a10a96118d83ef7b6350514a957bd9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.1486923585000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bd61e6ffa991468a6062bf4047742d76be80658e74f9212ae8482ed6d90027cf",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1486923585000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9fcab2c463797c9b28ee01148cc476784bb2473b84bf8f2ae68c546f3cb9c946",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1486923585000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "61609ced85a7068bb6b227a8778db35ac30701765ed24a2d414765a7965417f9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15333240340000012,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1a8b7c2b566250e4974b9accd1eb288e0b1c3b9ece047603707261bce302dd08",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.15003043320000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "07a6da34a90c5c24e8cfdef1b9c07e2ff039d51fce0b917d7a4ba2527844daa4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15003043320000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "441990e611d4bfed0a753adb7d990a66af9681ccb20bb032d058f3e3bf793c67",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15003043320000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d00659d885e156983f250b8d53e6c117947d0afc46d076fdcf1e024dacb4145d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15333240340000012,
            -0.12667545560000004
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bc6f099a3c49e384ab643559ec0ec44d65d442396a1dc177bb4c7181ac52ae54",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.1491157040000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "492d3075b7505d752fc4569124324cf50ec4e1e12399bff92d72a757be0abcea",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1491157040000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ebab91384cb73c29a059a5f61ee4cb1db962fd86e95224f09308839b0f4f4a7d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1491157040000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4266ee5cc6a9ac907f421389ef9cf425c951ac9475f81729c7ed50f0150b1b7d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15333240340000012,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6a23f24486bb79be48113d97b10bbba4ac19f7ddef0e43e81ec8d1dc67ff9092",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0377073579,
            -0.1490785836000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "be75d5c8e26860196c89f31b797698e558e2c7568cb1a802d2a09507366516ca",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1490785836000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9a5ffaf7d90c7cd06362d27f96a11d349d1b8f1dd81f180cf81cb93f13789ea5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1490785836000001,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fc714e5166dab9d576b2cca6b8263c9609f4ba786bf9b50769aa593b8e6c47d5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15333240340000012,
            -0.12290532450000002
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1a1d82ea59c99bfe7ac50c54c249f33eecaf9e8d07e4abf76bdd391e3652f99b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14288377690000006,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "915b629158bae600eedb793e1b7461db1bca2642934e70e963373d51bb0eec9d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14288377690000006,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "505ad729a6207cc8be7b2d3fe972a46ba111f58eeaa7b3b530a2cfa2e1d371ac",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14288377690000006,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "59b014959d6ca4769d4753c652daf0ccb38e962e5c3d4d3ea42fec5bd2a2a57a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15318423320000008,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e77bf2a8d1f196188c97d7cfc708d2f57c96d69e508253e83cf169f5c4d6c81c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14157613370000005,
            -0.10500613419999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "add329e8e27ecebe1d584cb1f14ba572d35710aea60476ca8ccbc31431672993",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14157613370000005,
            -0.10500613419999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c8d96d02fef2052aa1b5b4f37d053341689597b833962dea2b09040dda9cd81d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14157613370000005,
            -0.10500613419999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "64e8b768141ab52605621addcd48eb9cc31b1ffcd58858b53f7d3015b5511af3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15319340800000006,
            -0.10500613419999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14185111210000004,
            -0.10293166419999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9a8031973c8ec766ac9566a91c4f700fd8d2a7712f8f4e3641c67b8135e77bca",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14185111210000004,
            -0.10293166419999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4a09e9f42c304e0c0f941aa4fb00cfc45f473ebaa326e8c08008a0a2a91e8d4c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14185111210000004,
            -0.10293166419999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c54abf54583ce691431dbb42312227a0d225834bfc9a325757243da770f414aa",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15319340800000006,
            -0.10293166419999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "387050649e85b36d7c6e999764671f946e30e8f6587f959815efda2fee8967c9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.1459103633000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6d0b27b35b089a17eb96ff6e8962cf760fda88c3a3d4da56f20518c119a22fea",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1459103633000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7e25e305550d53d8dd69c7eeb54c0b6e13240426682cf97ea575590254e15a8f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1459103633000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "09c907ccffba9c79389da45ffbc273ef56ff552a01e37bb47bf4b4f538584933",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1526846268000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "330e9079a8741ac5ed4d998877d62b08834a5251908efa8b14fa9b09f101662a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14420201190000004,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "eadf7cacdbca92462104fbb663d7c89152d0846f8079544838f53c144e80b383",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14420201190000004,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2c75c42046ef3a6d0f0febae245bcf1a0d429394847dcdc593062e759c731b73",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14420201190000004,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bdfeea35c79ba78c3054cc430396a6f0454ffcb4c0eefca49e78830b92de5ccc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1526846268000001,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3d16b6890afaf109d0c4451863565fe56cb71dd1454039aa22d95648f62fe42d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14420201190000004,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e22018ff8811c7b7c47fb6ee98be4a18af5dd760741f1521c9a5e5246a5dcead",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14420201190000004,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4c5dbff3038888fbc8ba660d551023c7213bc3c92e7d698161e4831ddb927e16",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14420201190000004,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f985f1617e9bb77ea62699fce58cc6011e56a4fb40c9d3565f854b8ed05f5e4c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1526846268000001,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1a0ba2f00044f420ffb20d85ffd3b630915c4f0587b631a9e61e8fc68b943b2c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.1459103633000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ae2f1ec1405653fbbf289a5f020fe4b9ab1365648959be0631bcd1db772eadad",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1459103633000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "50aeca7dbe7571cfa0dd145f2032d40a70a44efb66da2450d2ac21fc20d8ac95",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1459103633000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "02ed4b871a3ac2dc98111f5f7dba62b21c61af723cae0b25f7d3fa568b6642e4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1526846268000001,
            -0.11140944080000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "13e36312d75235095a99fb4673caba20941b36b205e0f88c729e7bc1900c423e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14470016910000005,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9755e4a2985929b24476e74975b3281dcf102f99fc184339e833c99c9365e566",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14470016910000005,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a2606ff0dd53e64bdaed4879ebef55587c576527665e09aaceec8068c023f1fa",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14470016910000005,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0a073f60f2b4e958cf7bb14f680436f06eb26b748c281a78271005a1011caa57",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1526846268000001,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "42105ee5fa31f194122fe24f85377d35b1afea27da9bbed7fe4efa1b04df9b81",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.040822131899999996,
            -0.14470016910000005,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b4a19d9ee57a1ed883fc45f2d940417ba33b9bcd8854935c3d9ed02a29df5c44",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14470016910000005,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a05a3729a4575c24923de713a0ba59f30f2cfd21472905bb9a557e2e85fe5392",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14470016910000005,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cd978ede184d59c0797473a5f7cf0173d393d3398a9aa841a8dc97ea58a53cb5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1526846268000001,
            -0.1079068174
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c1144d55f4b001966183229609c62f71533195749e340dc147b58b34996d34b1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.13799086100000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b7aa686834fba404e57ce646e62ea5ae9ce6b33df36f634aa733cced8430673f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13799086100000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b7c893047999c7d6c75f8da734604fb8e463ffc56e36cbccd00fa3732bfff73c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13799086100000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c2faa48b20285145059a9507df7fb128457be7916c87597372a667e3535514da",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15263141030000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "376261879bb3a98cb9d9f885ebc4606248424ee5623184ed545ba758deb3d361",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.13751645780000002,
            -0.09398533239999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1c9aaeaf1c01aaa86bd6f9b2a9def8c7f55b76815b48c037012df2db186a7ad9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13751645780000002,
            -0.09398533239999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "53ae75468006b31323bf7c8217cd72f20b714d1c350e56945d1b7cb891a67f57",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13751645780000002,
            -0.09398533239999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "dcbdfc7b407f6dae2709dbf78aaa01157de1752506623e224a3c54d9dcbd44cc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15263141030000005,
            -0.09398533239999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d1a7f1bab43c17c56cf770ea8414ee06ce61b60f10d4a20f8959f14d48824bba",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.13772462100000002,
            -0.09267567159999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bfc4d87ac49a11a984a17ee8bc2a235c4905e425284c08722bc83a3787c3da0f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13772462100000002,
            -0.09267567159999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "90e95eca032bfe50e881261b29e392fa034ba82c6ca75e51bb44c3dd72c9275c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13772462100000002,
            -0.09267567159999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ec4085c7e24702acce52ee2a5997e551a4978c5f8741df94c163d6422bc23f7c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15263141030000005,
            -0.09267567159999995
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "696913cb4f51a33bf3935b51da3b38e1dcd6d1a97557ef171529553b4d7bfbf7",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.14184720720000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f403091f4d2bc6ab744045f21d94ccd7cdb6bb69adac3cb07ebeb46eaf36f684",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14184720720000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6fc8e2eef32a9bbeedf4d1623087ba3891701d13c78d22843cdf57a1c9bb12be",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14184720720000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c2209a5b405bac286c73284d9fc581c16a425d179dcff71abdeaa8710254fe0f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1520307391000001,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "52db97a65a1d4ad3cfa5799f59629bcab32d4cb9e84027e5ec07afc0fc759dea",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.14058917790000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "520cb3507a916dc9d9f2fa51dacd4e7c3511bbf9eee1fcdf03da237bb9f07e11",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14058917790000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "74615fd57e7c943c143fd077540a3361517eb745a26477811b844f682456d219",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14058917790000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e9e04869e6239071f9dd8cce64bab3d8eeb7ca305ff95b34978dc8aedbbd705c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1520307391000001,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "13a36acfc6269b30b569bb601b5e16abcb027c50365afdcb43ae693eeb166958",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.14058917790000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d576233a8b8830e3532da4d368e8f230e4de74243f423ae4693135f0662ad5a3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14058917790000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "44cb7392c928f53c521015a2cd2d0d65ae8766b2261ffc6f5861bc3196ad086f",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14058917790000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b5ae512c057c4cca149fc22aa5ab060d43221cfcfb62184e6b988b8670e045e0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1520307391000001,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ec7cbbe41821b4534745fc5abe749c3fa818c012a03773917d564783155e3c9b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.14184720720000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cd308639566094e1248179f35cda2c75f4b3f108d88965087b313c6e2c18ad0c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14184720720000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "45fc69735e2a6498f6345128fd7d46a7e5ad7bc5aa540c5fe68355a5a078e402",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14184720720000005,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ce25616a08a3a713d3baa8fbe9c681a24d2d0ae6253ec78d562b4a0e52cefb9e",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1520307391000001,
            -0.09877776739999997
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f3b1956a637c63c935fb3bb6eb3e713d0e7881edf280d7cd43341778f5d206ec",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.14103211860000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4ef5f2e60b0a12f9c3dfdfc50ff212dda872ca3811ba7eb1a418cd635500ee86",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14103211860000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f38dda51d631dae80a08a0027a6f82f3f06d6328bca9e8c207522a8316d0a562",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14103211860000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5bf8412a3fe2565df7fe2ecd3cf0bf8ef854466aaaa317215f6937328ff3ab18",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1520307391000001,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1b8a1433cd25010fb5c550b3665e973d63467cfe7baa46e828f42e0e3914c235",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0439827114,
            -0.14103211860000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6c62868387b90bf0e5d50a007eb97dff2c5f410ac777bb74e949f24ca4545cd4",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14103211860000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bf18cc0ff8f31c28dd27bd53bea9a4b8740f08d9cba11a3a14cacc6d1091b9ef",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.14103211860000003,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f08a6c33adf0cb5410922ccb5eb4e34f92024956a5c0332e80e647bee7cb2a01",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1520307391000001,
            -0.09632089279999996
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3de7c13e774d534c952c8462bc02d4706ba6c2da63098dcc633d9891959119c9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.13511804430000002,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "161dbc35e812294ca418d3a491ac83452d7dae568d1e5be10421ee4e19fdab27",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13511804430000002,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1e3c5a3a25ba0ff260f82888076b19bd3e2497627e62d17545f54d5382b673a9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13511804430000002,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b9bc2fd53b37952d0fa31d7ee6c7abb2df29fc0c936f761b0b4d5de89d3b3c65",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1519756345,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1424ccb6f148503ef949aaec1c140dfeedf287a16154036803144b75c5de03c2",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.13480436720000002,
            -0.08640714369999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a164ba23ba9524e034fe07bfe24aea3b27db569bc592dca70655d980b21fcdd3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13480436720000002,
            -0.08640714369999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fd3352c6d16146fc47234c6239e5393864ac990b33c70cd0570d7c36192d1a49",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13480436720000002,
            -0.08640714369999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7ec3d94889c6256057b589f9a9349e6f11c29591facbfc6dd184ffe7dc58d8de",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1519756345,
            -0.08640714369999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d352ec1510356ccb70944864be43f48121546077644fccd6d3b4ebe46472fbb3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.1349272656,
            -0.08590478149999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "42881131aa958b37001b7427d92d5475137405fe28d79f77e10b24316f77ab3c",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1349272656,
            -0.08590478149999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ed0dd236355b7a8d9f42cd954e2aba0cca2d130aeb2e511c8145e52b3b5c9229",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1349272656,
            -0.08590478149999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a7e3098ae1d238b85a68bf710352484a836546f125d4abdecafda4bd5b6ce8e1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1519756345,
            -0.08590478149999992
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9b43cfb13d4e03c1d855e2b81d3146f84cdd7f6155194208cff59649e4fafedd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.13807653800000003,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "275334c7d66460505e7c71e7f1bc8e971d6b44f3af26a6b8dba212d744d4d00a",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13807653800000003,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0dee04873a3ddf671052ea481c0d968718285776ddcfc900e5af011213ad542b",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13807653800000003,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8538b7affe3bb97a027406cdbf0ee82edbf2a14cf9b0164e0f3b16e518dcce49",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15140886250000005,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "05063fd72167d3a3a2da97e7c8c63023ebe7fe845967932f2a3a68b2d9023574",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.1377627609,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "707d5fac1ebe3f88df9b8bca06082ec5f029dbaaa67f900f17bdbb99418ae959",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1377627609,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "12643fc27869a63bcca87e3e38c0aae6f7825f6728622759920ecebf182931d1",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1377627609,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2d4e420f979f519ab7261ed8c86ca8308618af6e63b56f5476e2d2fce0fd8a14",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15140886250000005,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "76c2fdbf72a6ee26af1f5ea026eca75afdfcee1086f79c917047a7c7ab3c01ed",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.1377627609,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bcaf1067a4e98787b432db5b6681a208b9eea62150fe336c1090df3b4f678dfc",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1377627609,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b54d6a3fa555012188e6f740379a78f0dd22cd68864cae4eb9e915ce67e8baaa",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.1377627609,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "17c9c940096d43a773c4905d1982dc3a9c901fae82b8de14cfb27f6844ce84c0",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15140886250000005,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0165967a82c576ce3dbbcae3a03db3d0b9766a1b6ba0de5459235753d980e642",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.13807653800000003,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "091fbd2cc185b592a8e7b80f30e3e73fb8f3034ef10dcb197ae208d1892901d3",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13807653800000003,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "17dbff0a23e5d013e2d4b110485364f1d520f1dd5b5b79ea9cec2328e6048ff9",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13807653800000003,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a7d1bc64be18eec70f804ccb675f4de3265988e1f7041b8dac11721a645fbccd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15140886250000005,
            -0.08903910769999993
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "81f56cf56a5de341c5d98c82cf7d5803225386e334d2d1d583526e9c4ea5e855",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.13806785240000002,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "512697187c6fe64646e9ff21e491e8e481880ebae3fbd0e5138c76ee036ec1d5",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13806785240000002,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "673a28cda6786a76d77f41b3d518b2dc00aa5c1482c95959af2c5318831043bd",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13806785240000002,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "64e6f60cccaa85fd39f8b1fa74bc32547aeab8eb0fc0ea90356ebdca81ab94da",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15140886250000005,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f20359ca6d891690d890c115b86a566a971340c2017016139abfe828870ecff8",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0470974854,
            -0.13806785240000002,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "891e4aac1326376aff627803dcff3b5d016adb3f7c1d241c033375b50f4f5659",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13806785240000002,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4bfb9404f1e53fa2d8ba993a154c73bc83122dfdb210429965cadb5122d6cb5d",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.13806785240000002,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "443522543e3e8dd041a7ffeee4af344efccc3ec16395b525bc91265308a4d846",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.5480370374,
            -0.0344925839,
            -0.15140886250000005,
            -0.08768695749999994
          ],
          "positive_window_share": 0.25
        }
      ]
    }
  ],
  "run_manifest": {
    "benchmark_specs": [
      {
        "benchmark_id": "buy_and_hold",
        "rebalance_sessions": null,
        "target_weight": 1.0,
        "version": "1"
      }
    ],
    "experiment": {
      "allowed_axes": {
        "add_n": [
          0.5,
          0.75,
          1.0
        ],
        "amount_ratio_min": [
          null,
          1.0,
          1.2,
          1.5
        ],
        "atr_stop_multiple": [
          2.0,
          3.0,
          4.0
        ],
        "cooldown_sessions": [
          0,
          3,
          5,
          10
        ],
        "fixed_initial_pct": [
          0.3,
          0.4,
          0.5,
          0.6,
          0.7
        ],
        "max_units": [
          2,
          3,
          4
        ],
        "require_macd_bullish": [
          false,
          true
        ],
        "risk_per_unit": [
          0.0025,
          0.005,
          0.0075,
          0.01
        ],
        "step_pct": [
          0.01,
          0.015,
          0.02,
          0.025,
          0.03,
          0.035,
          0.04,
          0.045,
          0.05,
          0.055,
          0.06
        ],
        "stop_n": [
          1.5,
          2.0,
          2.5,
          3.0
        ],
        "unit_pct": [
          0.05,
          0.1,
          0.15,
          0.2
        ]
      },
      "as_of_date": "2026-09-11",
      "benchmarks": [
        {
          "benchmark_id": "buy_and_hold",
          "rebalance_sessions": null,
          "target_weight": 1.0,
          "version": "1"
        }
      ],
      "experiment_id": "fixed-etf-adaptive-validation-v1",
      "start_date": "2021-01-01",
      "strategy": {
        "config": {
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "sell_tax_rate": 0.0,
            "slippage_bps": 3.0,
            "transfer_fee_rate": 0.0
          },
          "grid": {
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5,
            "fixed_initial_pct": 0.5,
            "initial_model": "fixed",
            "max_grid_per_day": 1,
            "step_pct": 0.02,
            "unit_pct": 0.1
          },
          "trend": {
            "add_n": 0.5,
            "amount_ratio_min": null,
            "max_units": 4,
            "require_macd_bullish": true,
            "risk_per_unit": 0.005,
            "stop_n": 2.0
          }
        },
        "policy_id": "full_adaptive",
        "strategy_id": "full_adaptive",
        "version": "1"
      },
      "target_codes": [
        "513500.SH"
      ]
    },
    "experiment_hash": "b59b3021fac04f1ffb48eabb902b8b7097be475b919902a3282488e14692cb67",
    "experiment_windows": [
      {
        "benchmark_specs": [],
        "candidate_scores": [
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "02951609451a1a3666f9e27a5c317b82fb9d83367c6c4907f4a9d530a074a829",
            "cost_drag": 0.000865195925,
            "cvar5_improvement": 0.03464620130895089,
            "drawdown_improvement": 0.16926073573222933,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0128157852760227,
            "sortino_excess": -1.7907135175912194,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0380f680c2ed4cb0751113688c497ae2ca73f1769aab860b0851287c65fe1fac",
            "cost_drag": 0.001254456775,
            "cvar5_improvement": 0.03719303691157057,
            "drawdown_improvement": 0.18379284055889694,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.2041448765022067,
            "sortino_excess": -2.0754504227154666,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "04c0ca5fbcf902e5b9afe76b36a90ca3ad2104030989324ad9d294df660cfa89",
            "cost_drag": 0.001313494025,
            "cvar5_improvement": 0.02018388727797488,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.30181290193418064,
            "sortino_excess": -0.8307961877024028,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "064c3f82e8595dcab77015ea88579873dec1e16e29d5a987e51204197ce9414d",
            "cost_drag": 0.000840088875,
            "cvar5_improvement": 0.031362683925151645,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6646079711151862,
            "sortino_excess": -1.356319605303509,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0664477e5295e0bc1c74559f720de476589a1201e90ca5c2c2645acf217e5a1e",
            "cost_drag": 0.0024909307,
            "cvar5_improvement": 0.022645333524839262,
            "drawdown_improvement": 0.10646816006355633,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.064600062623985,
            "sortino_excess": -1.9045309123980718,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0752a8b6c7a878a88b448142929f6a9f3be2c1ed8c4201bee06a7d6faa25ea99",
            "cost_drag": 0.00151750105,
            "cvar5_improvement": 0.016736799658421536,
            "drawdown_improvement": 0.07687248928810198,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3119542471564712,
            "sortino_excess": -0.9042931109657601,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "081a8609b5d2788de7dedead3776df8fed29be1556ee3ac5015b21181e073d7f",
            "cost_drag": 0.00146291265,
            "cvar5_improvement": 0.01643136541540369,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.16502096493227114,
            "sortino_excess": -0.5151835600368271,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "08bb1f5360f9a1daa71255445b28f2b85a25bbf9afeafe227384fc93068725f1",
            "cost_drag": 0.00149136575,
            "cvar5_improvement": 0.03342606019411729,
            "drawdown_improvement": 0.16319245940721322,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.9299340094960116,
            "sortino_excess": -1.732151452956021,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0a8f9b6084c1d444d5b9dacff3681205d0b72ae817079b8f300cb12517cbc6fc",
            "cost_drag": 0.0019144714,
            "cvar5_improvement": 0.03337637220601288,
            "drawdown_improvement": 0.16175185225168365,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0876320324087487,
            "sortino_excess": -1.8872578774448012,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0be1879f481ad47d63cb1e9e3839ecd1e8b8a47f13b42f9c203ebdd2d8b36c92",
            "cost_drag": 0.00133999435,
            "cvar5_improvement": 0.022356608621219423,
            "drawdown_improvement": 0.10589468096437682,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3133952943447965,
            "sortino_excess": -0.8124084185249634,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0c65d2ef761411d63b3e7d181c2d998d0df2dcf703efd602be2fad87e1da59dc",
            "cost_drag": 0.0019879749000000003,
            "cvar5_improvement": 0.029123715445915403,
            "drawdown_improvement": 0.14177494371058663,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.1653786709336622,
            "sortino_excess": -1.9771765101590708,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0cad56c70b53c6f45b92078a0eb03bb554e4515d6c3eca9cc7cee91426f915e9",
            "cost_drag": 0.001313670275,
            "cvar5_improvement": 0.020184107176237323,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2753687519681388,
            "sortino_excess": -0.7791909714096068,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0cbf63fff76abf8f86447fff223cc640736f864eaa9919c9dbc89d1c0d125adb",
            "cost_drag": 0.00111505055,
            "cvar5_improvement": 0.028695831062943412,
            "drawdown_improvement": 0.1379804012104272,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.300839388653573,
            "sortino_excess": -0.7510085024970035,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
            "cost_drag": 0.0011383758000000001,
            "cvar5_improvement": 0.02408959404072802,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.583504659450548,
            "sortino_excess": -1.3002356008457985,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "11a928c621365eb7f902d7635a77ce6899022428a591ed6644c79dd42f8bf607",
            "cost_drag": 0.001462810575,
            "cvar5_improvement": 0.01643195640764881,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17852566818221793,
            "sortino_excess": -0.5449160427628745,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "13140adfdb638ee59aee50db7ac7a68bf94b4aeb3cd69660a93f3b3954d57fc0",
            "cost_drag": 0.0012996363500000002,
            "cvar5_improvement": 0.03454217154683866,
            "drawdown_improvement": 0.1692766204785518,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8673898031471121,
            "sortino_excess": -1.6492751907858343,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1421bd391e699bf7e3db84dd519ed0f9abd810d6436050bef6fa5aac1639def6",
            "cost_drag": 0.0013140691250000001,
            "cvar5_improvement": 0.020288034594120014,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22010217699506085,
            "sortino_excess": -0.6672107350621954,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1543bfd39152b539b9476475cdaa1d411c13d91f416cbff3ba8211a1b4f61a45",
            "cost_drag": 0.0012939447999999998,
            "cvar5_improvement": 0.0201457677451275,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.21854145589445056,
            "sortino_excess": -0.6130248169238779,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
            "cost_drag": 0.001267023625,
            "cvar5_improvement": 0.028059322978761625,
            "drawdown_improvement": 0.13481170624582797,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7773746315664087,
            "sortino_excess": -1.5525820056966335,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "17c7279512899f3a91bea351e1b53d236bffc52f4a909e0f96befb2127ba1987",
            "cost_drag": 0.001591624675,
            "cvar5_improvement": 0.017514675109418353,
            "drawdown_improvement": 0.08207334950121645,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.164849054727653,
            "sortino_excess": -0.49992279208167373,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "183a91bd23a755b7e87e0ab603de83e23b8219e506dd76397e078a1cf902c167",
            "cost_drag": 0.001930258825,
            "cvar5_improvement": 0.026118427128875504,
            "drawdown_improvement": 0.12597115347018673,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8728178909435449,
            "sortino_excess": -1.6395710389483242,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
            "cost_drag": 0.00163942295,
            "cvar5_improvement": 0.03190015896988322,
            "drawdown_improvement": 0.15490556718518642,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8779436668689635,
            "sortino_excess": -1.660140028157156,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "18fc14e280c2cfd24eb7a861ce0ea745639459e640b134c7b93c1eee85bd3f1a",
            "cost_drag": 0.0010114270999999999,
            "cvar5_improvement": 0.030929122580994124,
            "drawdown_improvement": 0.1496270800354272,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6712817582672153,
            "sortino_excess": -1.384746981435538,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1955c130371fbd273746ee973f8ff228037a1edbf3c4f5811acb4c15e0cf6dda",
            "cost_drag": 0.0020202239500000004,
            "cvar5_improvement": 0.0193600686033545,
            "drawdown_improvement": 0.09202217890764183,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.29619189098906246,
            "sortino_excess": -0.7959998035614532,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "19d00bceaeaee45b90711aedc56891ccd0aec187c04e0c1df0557f9894ba521c",
            "cost_drag": 0.001326368875,
            "cvar5_improvement": 0.020328531568286765,
            "drawdown_improvement": 0.09500090995358776,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.26114122046591676,
            "sortino_excess": -0.7416443938128365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1b7e2c5e7b5958dc5a4167102c649e3905f2a20047667578f26da46fe53ae2b2",
            "cost_drag": 0.002062835725,
            "cvar5_improvement": 0.02255505340170847,
            "drawdown_improvement": 0.1073563271554954,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6123343520577708,
            "sortino_excess": -1.3165536240419642,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
            "cost_drag": 0.0011087242999999998,
            "cvar5_improvement": 0.0237875061012543,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1891831710430047,
            "sortino_excess": -0.46278020852905244,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
            "cost_drag": 0.00214718975,
            "cvar5_improvement": 0.03296611329604098,
            "drawdown_improvement": 0.1594873994649461,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.3483406536850226,
            "sortino_excess": -2.220814984234556,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1fb848b69f408dc3ba8d7bd85ebc85edda0535045ed94aad7ab28c6599beaf4d",
            "cost_drag": 0.001461625225,
            "cvar5_improvement": 0.031699455597230725,
            "drawdown_improvement": 0.15374394570828964,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7985578191774001,
            "sortino_excess": -1.5218643600213473,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
            "cost_drag": 0.00122640985,
            "cvar5_improvement": 0.02486801205954759,
            "drawdown_improvement": 0.11880461117082797,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.24693893350135776,
            "sortino_excess": -0.6279926483915563,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "20c920b02310daf4b859f8b813f29af3b4d257da9ba48b2d64b95f4328dde275",
            "cost_drag": 0.001332234175,
            "cvar5_improvement": 0.020410935140572645,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5099172152349318,
            "sortino_excess": -1.2205766675666792,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "21afa2e296937da975f586f16b52eb519be169e613d16ecd15cd50de513cdbcd",
            "cost_drag": 0.0009576758499999999,
            "cvar5_improvement": 0.03464434610224926,
            "drawdown_improvement": 0.1686003621072293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0547167178192323,
            "sortino_excess": -1.8653009796807365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "222df6d8f13727d94d27e59090092450a9d1437210027cc7ba1e9ed6e9669731",
            "cost_drag": 0.0018501215500000001,
            "cvar5_improvement": 0.023076196308892225,
            "drawdown_improvement": 0.11038014598372115,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3595604511552384,
            "sortino_excess": -0.9065788817655005,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
            "cost_drag": 0.0014145332250000001,
            "cvar5_improvement": 0.02594761135738205,
            "drawdown_improvement": 0.12378871546242151,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.49667041132305845,
            "sortino_excess": -1.1658255543557705,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "23c50db9ddba5ebfe44269566b665b6b65bbdf61def5dfe671d025e6d5a010b1",
            "cost_drag": 0.00164091285,
            "cvar5_improvement": 0.019677353493378756,
            "drawdown_improvement": 0.09261530832621648,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4907263694964803,
            "sortino_excess": -1.1758427850624624,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2542c5a0c6a70a2692a3038a43bcea945893d0495b2c1713e03b0f9afdf6620a",
            "cost_drag": 0.0025181771,
            "cvar5_improvement": 0.031904463469767,
            "drawdown_improvement": 0.15508758258263672,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.507711951744247,
            "sortino_excess": -2.374434404752481,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "259b394408833371c897a4a9317235e9c836670ca8171b17b53da30eb4a6a0c9",
            "cost_drag": 0.0015362729,
            "cvar5_improvement": 0.033579984085477056,
            "drawdown_improvement": 0.1645060682049404,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.1719206159589024,
            "sortino_excess": -1.9757532179655564,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "25d46927d3049e38377b2aab3cdec3957e2a5adf6b1a27fe97889bc46891180e",
            "cost_drag": 0.0009960326750000001,
            "cvar5_improvement": 0.02781773905302938,
            "drawdown_improvement": 0.13266376873973645,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6526919522186508,
            "sortino_excess": -1.3815554045631986,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
            "cost_drag": 0.0011722358250000002,
            "cvar5_improvement": 0.02605453011012079,
            "drawdown_improvement": 0.124534699570828,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3858078805263936,
            "sortino_excess": -0.9414518387557583,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "260012ec18d23eb314b1bd71c33087541eee3662ea1fdbc37c0ba619bcac2dbb",
            "cost_drag": 0.0021246485,
            "cvar5_improvement": 0.02243021148479837,
            "drawdown_improvement": 0.10746708213928216,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7199547656363914,
            "sortino_excess": -1.467140292576508,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "26296eafe932dd4ff9512c67b6adb54a054d9512ee6fe088c015bb6b30ae16ef",
            "cost_drag": 0.000998668575,
            "cvar5_improvement": 0.027812480991910138,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8038751787985641,
            "sortino_excess": -1.5770536263610233,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "266908ce86922ef9e2da585eb6b06dc860b8cc72327a6b50d62c098f123fd428",
            "cost_drag": 0.001673361375,
            "cvar5_improvement": 0.017451318858199692,
            "drawdown_improvement": 0.08172510000975478,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.18262963354815898,
            "sortino_excess": -0.5278051671507742,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "268cf23cf0dce23398307940260e0cecf8d96d17daf5edc865eaaa770f936901",
            "cost_drag": 0.000988517825,
            "cvar5_improvement": 0.02759921375068633,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.33601511952076335,
            "sortino_excess": -0.8397771035938049,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "26b18365a7e4237cc73053f1f6c404fdd94246aa4e16544ee34c6b1bfe516a85",
            "cost_drag": 0.0007999728500000001,
            "cvar5_improvement": 0.03136207170264759,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6274800141803369,
            "sortino_excess": -1.3083346393704078,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2893c794a262dfeeb1d55eb234d4bbc50613e92208bd8509d365e79e48e8e243",
            "cost_drag": 0.0016128669,
            "cvar5_improvement": 0.01857549735104272,
            "drawdown_improvement": 0.08719202477621646,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.285232107412177,
            "sortino_excess": -0.8103704538577909,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "290d66f51c3334521564ebbf587b2c8f96dd3feca2c2d788144f482ee2e0e5c3",
            "cost_drag": 0.00150521375,
            "cvar5_improvement": 0.016666891519420125,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2539022921885565,
            "sortino_excess": -0.8074716661452295,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2b1ca3a349c41d3e74f6ea219a4c0fe30f94bd0c8d69053d8a263b0a0abd2acc",
            "cost_drag": 0.0025335486,
            "cvar5_improvement": 0.025808072739066046,
            "drawdown_improvement": 0.12202527957164847,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.1649531923069294,
            "sortino_excess": -1.9802666732767895,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2b8cce8c37110946254601751fec91e8b1a3052ace950c33d369bc1269f4e54c",
            "cost_drag": 0.0015036962249999999,
            "cvar5_improvement": 0.024653736003470764,
            "drawdown_improvement": 0.11634816696437683,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.820958669140426,
            "sortino_excess": -1.6322870343500357,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
            "cost_drag": 0.001138844175,
            "cvar5_improvement": 0.023892510225635603,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4862305167213108,
            "sortino_excess": -1.1184185950059673,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2ea28b5fd16155856db1a6aaf045c7c6a38ceefbc42b4e51cb92f1e5a3291080",
            "cost_drag": 0.001032038075,
            "cvar5_improvement": 0.03204536432984687,
            "drawdown_improvement": 0.1555067733354272,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.009795248978302,
            "sortino_excess": -1.7928849700720408,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "318930da62df7a9a4b135893117f29e6080cdee95f09a82d0197d3413840c2a1",
            "cost_drag": 0.0008543032499999999,
            "cvar5_improvement": 0.031406838256104366,
            "drawdown_improvement": 0.15199593103558792,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3219378941751374,
            "sortino_excess": -0.7651518901186846,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3986694fa6674e967c35c294ac4055fbd72f2cc3fda3b61e52db297456a13d8f",
            "cost_drag": 0.001540252725,
            "cvar5_improvement": 0.030546072531284284,
            "drawdown_improvement": 0.14825724883621424,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6010028192858116,
            "sortino_excess": -1.2954410449571019,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3b113e92d617b95e71b3d485144a8bf07623fdd5476c359cde7bf0af5e60b9ba",
            "cost_drag": 0.0018741324,
            "cvar5_improvement": 0.01836347436308733,
            "drawdown_improvement": 0.08685604426730292,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17833969975101815,
            "sortino_excess": -0.5420318548055456,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3b8400990f65f2f5c0b5d93d3ebecb37df16eedcd649695660efe4d79ce973b7",
            "cost_drag": 0.001286797625,
            "cvar5_improvement": 0.031643290802626844,
            "drawdown_improvement": 0.1533329800652564,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0886300963448574,
            "sortino_excess": -1.8883416249615366,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3c50ec6e404a0402a3f98be24cad12d2a6bb4f1a9ce1917679cbf45896f6efd0",
            "cost_drag": 0.002161914025,
            "cvar5_improvement": 0.025390316045783477,
            "drawdown_improvement": 0.12283295706819758,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8984278763874876,
            "sortino_excess": -1.696026145321635,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3cc7b53f43c230cbc0bbe5e407576b80e5c3c8401dd8cf82ff397d5c07f70d48",
            "cost_drag": 0.00139318455,
            "cvar5_improvement": 0.021160701023937602,
            "drawdown_improvement": 0.10026551141437681,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.20607239711989495,
            "sortino_excess": -0.555468311881194,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
            "cost_drag": 0.0011281231250000001,
            "cvar5_improvement": 0.02384457484127753,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2648716507264735,
            "sortino_excess": -0.6994050681315865,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "40da851baa2cf49bf7ef0a57c4209c8c76198f9c0a177a116a76f059fcdf01bf",
            "cost_drag": 0.0013330623500000002,
            "cvar5_improvement": 0.020204271915745618,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.37344324970391196,
            "sortino_excess": -0.9904270060998004,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
            "cost_drag": 0.0013088938999999999,
            "cvar5_improvement": 0.02609418545585478,
            "drawdown_improvement": 0.12417420294582798,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.43613861745608595,
            "sortino_excess": -1.100123419588606,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "43950e3f259617cc483404f6d6415d25f5b84e7eb334812843c5e9177958cce0",
            "cost_drag": 0.001661356375,
            "cvar5_improvement": 0.03729271537590323,
            "drawdown_improvement": 0.18298242624065106,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.5391871523880596,
            "sortino_excess": -2.4097074230358344,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "446dc1803e4c7a85e81fa0757a3f673cc8f49dc153680f00a73418f382fe40fc",
            "cost_drag": 0.001197438375,
            "cvar5_improvement": 0.02861604635199044,
            "drawdown_improvement": 0.13765176364405823,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3316408071231858,
            "sortino_excess": -0.7959693792854875,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "45451ae22fd54f5fcc4a8c83f4e0e0fcc2755c40142cb91352153ea353ce96a3",
            "cost_drag": 0.001823016825,
            "cvar5_improvement": 0.02058019005436433,
            "drawdown_improvement": 0.09663962727885297,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6772269168109901,
            "sortino_excess": -1.4328349417219461,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "45fc5ff3ccb51fbcbd9cfe0f8880bfce401d63eea9bdb37ca7711e56fdfe51f1",
            "cost_drag": 0.001115864225,
            "cvar5_improvement": 0.029751937363021133,
            "drawdown_improvement": 0.14355201096042722,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6296029469311178,
            "sortino_excess": -1.3474309382006362,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "461c154a7e2353f2283c499ac85775b992b924de41d0fec46d9f06b5172f7142",
            "cost_drag": 0.001662547075,
            "cvar5_improvement": 0.02071387434749268,
            "drawdown_improvement": 0.09771528432621646,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6796716230041127,
            "sortino_excess": -1.4440605598328007,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
            "cost_drag": 0.001128196025,
            "cvar5_improvement": 0.02384470546940377,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2461637993110542,
            "sortino_excess": -0.6602286769042492,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "46f84d8aed1026e2d80d880921222dcafc41aee81ce7ffb4371076fddea389b7",
            "cost_drag": 0.0014804250999999999,
            "cvar5_improvement": 0.017470865043055277,
            "drawdown_improvement": 0.08223376217621647,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.15999402489264908,
            "sortino_excess": -0.4544049152943994,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4734c020226fa7443033daa844967e4699044f02fbfcdd5f6005cd5984d5532d",
            "cost_drag": 0.0018116612500000003,
            "cvar5_improvement": 0.0242144852280715,
            "drawdown_improvement": 0.11550337644822845,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4600076993191725,
            "sortino_excess": -1.1063960949119798,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4769bcc53bde368b7006c19ea230e03bc28764d38036f94954f64cec059dcb85",
            "cost_drag": 0.002247862625,
            "cvar5_improvement": 0.028328865791507382,
            "drawdown_improvement": 0.13808938506360516,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0584943211285225,
            "sortino_excess": -1.9270613501560205,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4948e389709741f3f9c362d58fe2624e794f41e6d5ef2b7968b00962535749d6",
            "cost_drag": 0.0011377642749999999,
            "cvar5_improvement": 0.032044575714944526,
            "drawdown_improvement": 0.1546783894854272,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0561855783433176,
            "sortino_excess": -1.8713829316843233,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4b29dc52dae93fa89372642c660f99eeca7df753f4baaa1174e66a58541fe27d",
            "cost_drag": 0.001499367775,
            "cvar5_improvement": 0.0167216717203341,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.40520673060498946,
            "sortino_excess": -1.0631049446608898,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
            "cost_drag": 0.0020322218,
            "cvar5_improvement": 0.030036869430323132,
            "drawdown_improvement": 0.14398096773274735,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.3475778499025524,
            "sortino_excess": -2.149914262505411,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4db6c5d5762841c37dc4de1bc30a10cd0e27c01bfab964bf6c8365bcc5313082",
            "cost_drag": 0.001275160125,
            "cvar5_improvement": 0.020081990982529482,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.15100159672581737,
            "sortino_excess": -0.4016060643586745,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4deabe0573cbeae491a145f8e4d20f916f5c910661a4c80d8fc5167f3190b561",
            "cost_drag": 0.00209395345,
            "cvar5_improvement": 0.03485196297288215,
            "drawdown_improvement": 0.17070607242227928,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.5737003371305893,
            "sortino_excess": -2.3837743175158206,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4e1a984b1c95dcc573ae3ac61d76713bc6516583278750a0006153bff7d9df6a",
            "cost_drag": 0.002114801675,
            "cvar5_improvement": 0.024550935741888675,
            "drawdown_improvement": 0.11733984808809353,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.776559744529607,
            "sortino_excess": -1.5332348173776085,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4e816f70069fec6fbef680ba41095962ee77e9ff072ca18af5f553cdcfd997e2",
            "cost_drag": 0.0007999942250000001,
            "cvar5_improvement": 0.03136207170264759,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5869105197734219,
            "sortino_excess": -1.2667586318006443,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4fc55be6dc74c3f50156a7e114ea4978acdb95ed567f20d6bbf0c18ba03b48c2",
            "cost_drag": 0.0012370463,
            "cvar5_improvement": 0.03497398731000588,
            "drawdown_improvement": 0.1713830163292503,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.718096244976409,
            "sortino_excess": -1.414809924411484,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "5132cd3db68e157dd3153cb3ae9792dee9a4b1c862130fd622636843c2b36730",
            "cost_drag": 0.0017693562500000002,
            "cvar5_improvement": 0.036804308782372494,
            "drawdown_improvement": 0.1809199858000415,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.593309231311461,
            "sortino_excess": -2.4005906795769563,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "529b14ba63795fde28f27d0ddc49d26555b3ea64714f8b42d3e97419429806f3",
            "cost_drag": 0.0010861027,
            "cvar5_improvement": 0.028633252231769317,
            "drawdown_improvement": 0.13795511031042723,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3056784741438075,
            "sortino_excess": -0.742755844131741,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
            "cost_drag": 0.0012909113,
            "cvar5_improvement": 0.02725838264253417,
            "drawdown_improvement": 0.12978851654582796,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7013946734054324,
            "sortino_excess": -1.47516646765731,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "56cb7fb31d203469a3f1c85e5c30ae6f448173b6cf02c6203dc31a8c63b6dd5c",
            "cost_drag": 0.00149502375,
            "cvar5_improvement": 0.016624900128834885,
            "drawdown_improvement": 0.07682759215333276,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.21378733354577867,
            "sortino_excess": -0.6540573916248876,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "589b9e99b2cc99c9bf11c7d143c4316f35fae491362d7df2a95b2a38cea057ef",
            "cost_drag": 0.001053837,
            "cvar5_improvement": 0.03235807719217654,
            "drawdown_improvement": 0.15711960645487577,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4375435782374991,
            "sortino_excess": -1.00339828864434,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "5a17506ad28bbda515701fea8e5e9ce9e4f8bde66bd49b5febd4aad94e2a76b2",
            "cost_drag": 0.001228126575,
            "cvar5_improvement": 0.03066502601633525,
            "drawdown_improvement": 0.14801915642586122,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.712866760597866,
            "sortino_excess": -1.4581602181646067,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "5a60d04000e8a42a7ef2a4dfd58e04047fee6e55af55b1d752e8f78c30a7fad1",
            "cost_drag": 0.0014758811,
            "cvar5_improvement": 0.022406540270973642,
            "drawdown_improvement": 0.10555816536437684,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.34560505733145913,
            "sortino_excess": -0.9386855414915057,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "5a99c08a7ed7f5f806cf0a005980f33c6f44c53c9af3ff9ec74ea537e9ac3156",
            "cost_drag": 0.0008398317,
            "cvar5_improvement": 0.03149668410878338,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8156641879375963,
            "sortino_excess": -1.5805084167479364,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "5d600521d8ec100f51d0d336c6543e9781171444d584310acb517b6041a05a64",
            "cost_drag": 0.001645936575,
            "cvar5_improvement": 0.01870265058155291,
            "drawdown_improvement": 0.08725904357621647,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2812609104238149,
            "sortino_excess": -0.8212005366492963,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
            "cost_drag": 0.001767185675,
            "cvar5_improvement": 0.03279312298355854,
            "drawdown_improvement": 0.16079166619324362,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.133670696839637,
            "sortino_excess": -2.027238040432899,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "61a86f69f97281212bca1d76dff4959aded7bc8ae179fd65e9a35b51766efe9a",
            "cost_drag": 0.0015050497,
            "cvar5_improvement": 0.021163335477747503,
            "drawdown_improvement": 0.09995833323273629,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22141082244127747,
            "sortino_excess": -0.5903340251523671,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
            "cost_drag": 0.002237544425,
            "cvar5_improvement": 0.031446497158489635,
            "drawdown_improvement": 0.15150119598694198,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.1876014840285272,
            "sortino_excess": -1.9987892187035903,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "64ca51cf505764cc7dcd808efa152085d9373da22f33c6e151902050d8ddf2c4",
            "cost_drag": 0.001481288825,
            "cvar5_improvement": 0.01648174995471817,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.24562781773751008,
            "sortino_excess": -0.7298054008463706,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "64e3052ef8fa0319a7c2533e42c13b53422f82ad86eb68d7701d663c462fd129",
            "cost_drag": 0.001370083325,
            "cvar5_improvement": 0.02352401036586886,
            "drawdown_improvement": 0.11162754366437683,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4873806947538525,
            "sortino_excess": -1.1443631451594207,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
            "cost_drag": 0.00117762445,
            "cvar5_improvement": 0.027210757267603095,
            "drawdown_improvement": 0.13033598194582796,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6108940483185865,
            "sortino_excess": -1.297063411267998,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "65e02eee14f0acb0a825dacbe164cfa06365c84cde2b215e2174efcc30cf82c1",
            "cost_drag": 0.0014728156000000001,
            "cvar5_improvement": 0.01645884613226387,
            "drawdown_improvement": 0.07677590912318685,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1413485871879973,
            "sortino_excess": -0.42634056299051404,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
            "cost_drag": 0.00127866945,
            "cvar5_improvement": 0.027052425032586085,
            "drawdown_improvement": 0.12960217134582797,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7358926207301433,
            "sortino_excess": -1.4977997998099974,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6a052b308f6ab167426ab2a7e99b79c37ceafef5132f04f03ebf5c5e3dece9d5",
            "cost_drag": 0.001294044625,
            "cvar5_improvement": 0.020145411291909512,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.20272626458949666,
            "sortino_excess": -0.5788309670047732,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6b5bf2db39c7a5312bb922ccbb7f79eb56adc7b97c17b591d33d8da2a6250bc1",
            "cost_drag": 0.00134463915,
            "cvar5_improvement": 0.020482181723734866,
            "drawdown_improvement": 0.0951042336833777,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6218777425022546,
            "sortino_excess": -1.3641249658658745,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
            "cost_drag": 0.001147122875,
            "cvar5_improvement": 0.02403731518675235,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4535307884338013,
            "sortino_excess": -1.1079444615636163,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6c762a7a83d430eb4aae46bc3b939d9320278f039a0d1733b209ae55c6e64f75",
            "cost_drag": 0.00099908445,
            "cvar5_improvement": 0.027634235956148605,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7274732221440153,
            "sortino_excess": -1.4669626761292274,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6d151393122f9975d3a3fbbdfde74da7330ecc39667716a01b5d15571ac979f7",
            "cost_drag": 0.0015951986249999998,
            "cvar5_improvement": 0.0350703862079231,
            "drawdown_improvement": 0.17233711696493348,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.3846107928730864,
            "sortino_excess": -2.2587806274626367,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "71cb3c31412438e23d4b9bff35ae94c701cf15c333086d98008bcf43077b98f0",
            "cost_drag": 0.0013039831000000001,
            "cvar5_improvement": 0.02017141589614963,
            "drawdown_improvement": 0.09494473149632765,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17399247120496708,
            "sortino_excess": -0.47364180373198767,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "757cb14275a89bc4c9e5a29a7520d973e34a22ebd3401c538b8a321442b8fd5b",
            "cost_drag": 0.0016772138000000002,
            "cvar5_improvement": 0.019874579797660358,
            "drawdown_improvement": 0.09275536480121646,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.483921996099878,
            "sortino_excess": -1.1832539373100954,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
            "cost_drag": 0.0011476915249999998,
            "cvar5_improvement": 0.02387180141542221,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.34306267147318226,
            "sortino_excess": -0.9036865490887447,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "77548bc87ab8ee39a946a4bb2c139e0addd6da3a1b8a8eb663acbcf366d946f3",
            "cost_drag": 0.0014707677,
            "cvar5_improvement": 0.02336531735509679,
            "drawdown_improvement": 0.11093103386437683,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6102106119782584,
            "sortino_excess": -1.3460327737264053,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "77bd9770c8d5ec308e8b7fd0fadfa8fbf6cead744a6e15323ae2a4260b80ad42",
            "cost_drag": 0.0022797879,
            "cvar5_improvement": 0.026315593635928124,
            "drawdown_improvement": 0.12492018506140895,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.2037269311991203,
            "sortino_excess": -2.0318992821892565,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "77c0310211df78935d4962e65b3e258ba298c8d9fd368ecda7590f2158d215b1",
            "cost_drag": 0.002363818575,
            "cvar5_improvement": 0.029414495056591227,
            "drawdown_improvement": 0.14055092273525627,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.5029979196469136,
            "sortino_excess": -2.28486124657231,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "7826433e193e4ac82cc351ff0995a6b514018d7da192d993bd018af86f9827f0",
            "cost_drag": 0.000945330725,
            "cvar5_improvement": 0.03448835608759883,
            "drawdown_improvement": 0.16841087048222933,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.1029739194472863,
            "sortino_excess": -1.8941189407201033,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
            "cost_drag": 0.0013378834000000001,
            "cvar5_improvement": 0.02491955825704279,
            "drawdown_improvement": 0.11881420225036624,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.26735828436162057,
            "sortino_excess": -0.6709979259428286,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
            "cost_drag": 0.0012790927500000002,
            "cvar5_improvement": 0.02830743138843492,
            "drawdown_improvement": 0.13508262119582798,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7344697250066179,
            "sortino_excess": -1.5270651077704307,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "7c2b3fc2dbedd2b079ebdeca8887a83fb588fd2a1d89ed4f35c2ff52d779728b",
            "cost_drag": 0.00144323365,
            "cvar5_improvement": 0.022269569443955747,
            "drawdown_improvement": 0.10544470316437685,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3488132929772755,
            "sortino_excess": -0.9254048859330359,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8001ce7a61e6bbc527399ec1395b7cefc4fdc1a06d706c582a8a9beb5ebe3b02",
            "cost_drag": 0.000844863125,
            "cvar5_improvement": 0.031345269958291934,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.45694130203557765,
            "sortino_excess": -1.0692622448335705,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8088cc365f89e6679290e380387e1324139d60bed3aa5ee409fd03ee528e9a99",
            "cost_drag": 0.001540728,
            "cvar5_improvement": 0.019833072402256912,
            "drawdown_improvement": 0.09325879237621645,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.39265496261897964,
            "sortino_excess": -0.9991448161863239,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "80899914e7291fc258eeddf6520efbf7fe1b0287b99fc96d0a62841279df7425",
            "cost_drag": 0.00207325075,
            "cvar5_improvement": 0.03178234829003481,
            "drawdown_improvement": 0.15691962952814525,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.258645475186055,
            "sortino_excess": -2.1865321725658955,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "812af4d1fa0b091fb7419ff0da1d71ce91fe65a0a3224bbcf41431dcebd0b08d",
            "cost_drag": 0.00112520255,
            "cvar5_improvement": 0.03183608746516286,
            "drawdown_improvement": 0.1544191687854272,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.1004675360233476,
            "sortino_excess": -1.8964985885865713,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
            "cost_drag": 0.0020748057,
            "cvar5_improvement": 0.027029714211248806,
            "drawdown_improvement": 0.12888837676242015,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7070777265894568,
            "sortino_excess": -1.4927674364831292,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
            "cost_drag": 0.00110240515,
            "cvar5_improvement": 0.030958291313045144,
            "drawdown_improvement": 0.14902899281042722,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6788463452628697,
            "sortino_excess": -1.4425420565924225,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "824e648c83a8f7c5d611f1044280116ee112dafff48f1898aadbcdd7cc416908",
            "cost_drag": 0.000997862475,
            "cvar5_improvement": 0.02764541593085533,
            "drawdown_improvement": 0.13256532246168662,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.25752092602264004,
            "sortino_excess": -0.6237985424154634,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "89ad7adcecda2efcf8cbd6a6401ed3e6ed96b851083accd850f6a0c518aa15b3",
            "cost_drag": 0.00084177925,
            "cvar5_improvement": 0.031385156975187734,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2851961461904489,
            "sortino_excess": -0.6927205763963937,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8a8f91fb3f844ba6dfc5dfcf5bdbde75f84903dd70fbf2739c509a094fde215b",
            "cost_drag": 0.000869369775,
            "cvar5_improvement": 0.035537078236422874,
            "drawdown_improvement": 0.1740314570322293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8589204017975485,
            "sortino_excess": -1.6091784648374376,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8bcb1085f091f1ae946199c14e23c1ba1e975e65f06096e4aa24df9a5387bf01",
            "cost_drag": 0.0008296533250000001,
            "cvar5_improvement": 0.03574702244599639,
            "drawdown_improvement": 0.1751882018322293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7757773336119953,
            "sortino_excess": -1.5135368726118332,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8bce2fd4652d535226e8dc035f7242084edc778cd386a1bba082c130a02ff6fd",
            "cost_drag": 0.0018468768249999999,
            "cvar5_improvement": 0.033721671254093,
            "drawdown_improvement": 0.1633594252143692,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.5075959276241897,
            "sortino_excess": -2.284043123871887,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8cbfd1cd2d9316edcb8d2b295fa7dd39a4888c1b6c1a9fd7cd02af0f71389581",
            "cost_drag": 0.0010900577,
            "cvar5_improvement": 0.030770754657833372,
            "drawdown_improvement": 0.14883140098542721,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7185712608733524,
            "sortino_excess": -1.4655139215761264,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8d2fb7a3cdb517396e8b9acf88ea220280c39c0d59402311d007504ddef79d5c",
            "cost_drag": 0.0012912363,
            "cvar5_improvement": 0.020157788086081305,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.15615617466811926,
            "sortino_excess": -0.43691457583606075,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8d4112ab3315d7d1ddc27a4d870f5e4b35afd1d22a3825b4b4fafb3f73ad8f3b",
            "cost_drag": 0.0010083009250000002,
            "cvar5_improvement": 0.027718359642219623,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3476935377718192,
            "sortino_excess": -0.9277424593994754,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8e9ceaba7690e6d3faceede615245b6d1a7554518ab91ac3b377c4df97f4c0a3",
            "cost_drag": 0.001371997575,
            "cvar5_improvement": 0.024601855880469987,
            "drawdown_improvement": 0.11706594248937682,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.700870780895851,
            "sortino_excess": -1.4294330292675739,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "8f4a1199d5a21df79951d1f560023a1fa23122d88707a3f69ce4c077993f95e8",
            "cost_drag": 0.0009693118250000001,
            "cvar5_improvement": 0.027549419559522736,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22107018372228188,
            "sortino_excess": -0.5109181422303164,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "90d6ff7ed79e50c4dddaaed58adbfdc177b6bf9b378de9d013c1d4240154e606",
            "cost_drag": 0.002445019225,
            "cvar5_improvement": 0.01955786493799117,
            "drawdown_improvement": 0.09164830322366113,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.43555154825203735,
            "sortino_excess": -1.1039500361228056,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
            "cost_drag": 0.0016257230000000001,
            "cvar5_improvement": 0.0279130650176133,
            "drawdown_improvement": 0.134165908974807,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6044733823085338,
            "sortino_excess": -1.2876218261059464,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "961cfe76def7b11fe2351283e3ebd181a0c11106d5a65042f1ccade8bdfaaa3b",
            "cost_drag": 0.001422149075,
            "cvar5_improvement": 0.021227460160465204,
            "drawdown_improvement": 0.10030565048937681,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.20127752181948394,
            "sortino_excess": -0.5588205781776778,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
            "cost_drag": 0.001124929375,
            "cvar5_improvement": 0.0238601283573777,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1878577485174281,
            "sortino_excess": -0.4876433133531319,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9aab49f04c34ce9b0218247ceb595fe069b32faa5bdcebea8b02ec4761a1c832",
            "cost_drag": 0.0009887161249999999,
            "cvar5_improvement": 0.027599313355561657,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3116343509511613,
            "sortino_excess": -0.7913529614902857,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9b0ed793b8789210beddbfe561da3142bf989c157269bda13aa9d2e732098470",
            "cost_drag": 0.0009421489,
            "cvar5_improvement": 0.03238282088850658,
            "drawdown_improvement": 0.1573897386322293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3974529945322411,
            "sortino_excess": -0.9348608842079246,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9b285843c53cb0e98fbb611366f677a98327b135bad0b9ffb777bf5f8f2ea648",
            "cost_drag": 0.0017051766499999999,
            "cvar5_improvement": 0.022081189431138445,
            "drawdown_improvement": 0.10512769539461475,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.21835269920101102,
            "sortino_excess": -0.6131766504585574,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9b49243fc490f86a5308087d28dcd0c8743ca5e9e7f2f9f5645275731e7a26ee",
            "cost_drag": 0.0013107334750000002,
            "cvar5_improvement": 0.021188620565064615,
            "drawdown_improvement": 0.10048502171437682,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1958147441711614,
            "sortino_excess": -0.5076368900390633,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
            "cost_drag": 0.001676685375,
            "cvar5_improvement": 0.02997446139345151,
            "drawdown_improvement": 0.14488000973878723,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8521868640831766,
            "sortino_excess": -1.6065183944314385,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9e3707d9ca4dd26f414d299f19d60bc43cbdbf2bf2b6da6219c626e1973457ae",
            "cost_drag": 0.0014815927249999998,
            "cvar5_improvement": 0.016482014763654747,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22392710642788805,
            "sortino_excess": -0.6864016221036142,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9f72db2d6091f70ef6f2c28a733136150b7d98312604e238d2900953d4d65ab4",
            "cost_drag": 0.0018922590250000002,
            "cvar5_improvement": 0.026299661822607644,
            "drawdown_improvement": 0.1261100183268073,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7897791535094294,
            "sortino_excess": -1.526858154219615,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9f8d66390e22e841dbc879446df494747fe0e69404b4bb4c04c136d2b5046189",
            "cost_drag": 0.001850945675,
            "cvar5_improvement": 0.030702760542034323,
            "drawdown_improvement": 0.14780669376863412,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.9554130077736316,
            "sortino_excess": -1.7800779591603928,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a01c832be39f3c46cd5b376ca93ac9936e7882bf59f762681abd6bb6e5fae186",
            "cost_drag": 0.0009833768999999999,
            "cvar5_improvement": 0.027771783842328288,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5499036933696069,
            "sortino_excess": -1.23389011877978,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a10c8020a0773c04afed2636a58bedf090d4fbf98ff1d3b60925e0ea4e097776",
            "cost_drag": 0.0008570471499999999,
            "cvar5_improvement": 0.03149356191566146,
            "drawdown_improvement": 0.15206337001009562,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6521579439444789,
            "sortino_excess": -1.3668925415161557,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a38ca9017ee7323d6ca2fa38e717ced6f522427e0f6ce2d771d4ec8eeb087dcf",
            "cost_drag": 0.000825771125,
            "cvar5_improvement": 0.031311774593528734,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2700696808488642,
            "sortino_excess": -0.6104702636600029,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a43d42200543c8fee6ecea4bd84917ea1bcf540d535e043f6a521a06832f55f1",
            "cost_drag": 0.00158171375,
            "cvar5_improvement": 0.02220283453019294,
            "drawdown_improvement": 0.10491123782333914,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.39310424303425007,
            "sortino_excess": -0.9972072289329104,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
            "cost_drag": 0.001741000225,
            "cvar5_improvement": 0.031562769190697636,
            "drawdown_improvement": 0.153403706862485,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0179841749213625,
            "sortino_excess": -1.8450868062525094,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a6346dd7e1804c75cf8dd0eb15ee8b4c4797741b2f0c1cb674ef99891c3fa9e9",
            "cost_drag": 0.0013330142,
            "cvar5_improvement": 0.020204530708455574,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4155145094131427,
            "sortino_excess": -1.0648629683057589,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a6454c26597b01d0276b684c62019f613b394f2ff7eaaf890673936236e2a537",
            "cost_drag": 0.0007996603999999999,
            "cvar5_improvement": 0.031532854565360514,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7238753760537531,
            "sortino_excess": -1.4754083268695992,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a71457d47e5c1fa6cd81dc8bc2295e36bc60f4d0e12fac791b33187fe27c62b3",
            "cost_drag": 0.000983889375,
            "cvar5_improvement": 0.027618780830164617,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5160982288568435,
            "sortino_excess": -1.1508139585958164,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a742864c7a1208b39c7fae284c174b8dd0af4d1de90c2fad405dab24d97015e9",
            "cost_drag": 0.00086585995,
            "cvar5_improvement": 0.03358704099882979,
            "drawdown_improvement": 0.16361964080722932,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7214943187477423,
            "sortino_excess": -1.426375133840056,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a7e68e5035096e8601e3fc70bed10c2f2d51007849d3f7759c8601c0d59a51de",
            "cost_drag": 0.0014022548749999999,
            "cvar5_improvement": 0.03368068117731622,
            "drawdown_improvement": 0.1642279270967771,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7988855620789146,
            "sortino_excess": -1.548177938865017,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a8b1e9c488ff9b024597f84b549df68bca23d0664c4df78a57248136fcff3c3c",
            "cost_drag": 0.0016549902,
            "cvar5_improvement": 0.024309081567738356,
            "drawdown_improvement": 0.11532175634153777,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.851426975717975,
            "sortino_excess": -1.639405010337249,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "aa322358aee7ceed5d28526185f0ecc94c244a13c6344d41457546a6a739dfb8",
            "cost_drag": 0.000852302375,
            "cvar5_improvement": 0.031531845032125895,
            "drawdown_improvement": 0.15213305695042026,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.984831261150338,
            "sortino_excess": -1.7719842589145833,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
            "cost_drag": 0.0011433323999999999,
            "cvar5_improvement": 0.024895540497887322,
            "drawdown_improvement": 0.11904757867082799,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23409687292927106,
            "sortino_excess": -0.5697645647688284,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
            "cost_drag": 0.0017206155749999999,
            "cvar5_improvement": 0.029797580907112212,
            "drawdown_improvement": 0.14478535426174777,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.006748797162305,
            "sortino_excess": -1.7873978675609488,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
            "cost_drag": 0.0011746955,
            "cvar5_improvement": 0.02827031944761934,
            "drawdown_improvement": 0.13582310284582796,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7220168402357452,
            "sortino_excess": -1.466373827778964,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b313af62bdd5d8e3e6b7fef4e167294ef0b09dc0cc58c92f6913a9a1385bd71c",
            "cost_drag": 0.001562739075,
            "cvar5_improvement": 0.017447598651198513,
            "drawdown_improvement": 0.08202961637621647,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.16841594687848138,
            "sortino_excess": -0.4953132647377515,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b3b9838498a218b2c75976ab65e15e6c8076bb286d1ea658b3fbbf8b7e944b0b",
            "cost_drag": 0.0008449337750000001,
            "cvar5_improvement": 0.0313453379065426,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.4197028113183751,
            "sortino_excess": -1.0013101176251393,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b54f48b12b36135d832f2f0ecb43d61a4941bcf07a971027a9accc6831847aea",
            "cost_drag": 0.00180353775,
            "cvar5_improvement": 0.019570810299359073,
            "drawdown_improvement": 0.091781497587415,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5325672626641018,
            "sortino_excess": -1.2278542572061901,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b6449162a482e7a08f99c096b1423ca1e879ffa87022184dd0cff292e8213cf6",
            "cost_drag": 0.0009371729250000001,
            "cvar5_improvement": 0.03566685993366446,
            "drawdown_improvement": 0.17433611185722933,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7149791546162065,
            "sortino_excess": -1.4564681693066106,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b66db6d06efa7d1e620ced97604377222cfc7a690e9e12414f834e4ae2dde28d",
            "cost_drag": 0.0013371997250000002,
            "cvar5_improvement": 0.020358795938691877,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.31650291518758555,
            "sortino_excess": -0.9237124287960391,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
            "cost_drag": 0.0011591333499999998,
            "cvar5_improvement": 0.02410995900892932,
            "drawdown_improvement": 0.11357453233140558,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5451927504358391,
            "sortino_excess": -1.2393673122464652,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b846a0a7e4c43066dab6457e533f7c7c435e82ee1372dd35cc746ba1dbbf7394",
            "cost_drag": 0.001500441825,
            "cvar5_improvement": 0.0165030245349361,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2984357056056001,
            "sortino_excess": -0.8644816613206674,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
            "cost_drag": 0.0011505485,
            "cvar5_improvement": 0.024150244557843953,
            "drawdown_improvement": 0.11363520662202936,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6983359553704205,
            "sortino_excess": -1.4579129889654348,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "bb96bcaf6239a8f480b471f3bd6f4f2edad305f90a5fe68ac611f0a7034ec535",
            "cost_drag": 0.0013506264249999998,
            "cvar5_improvement": 0.037228590432832664,
            "drawdown_improvement": 0.18422829607133187,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.2724378701191255,
            "sortino_excess": -2.2055068774075357,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "bd323451f9997167020ef8b4d4563d57e755f853e5a756382be5fefaf5d43de9",
            "cost_drag": 0.001011235025,
            "cvar5_improvement": 0.02785462844749219,
            "drawdown_improvement": 0.13272894858343096,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.9740361261610728,
            "sortino_excess": -1.7672298899113785,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
            "cost_drag": 0.00114825655,
            "cvar5_improvement": 0.02397853822420966,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.27074601367041823,
            "sortino_excess": -0.771324260785702,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c043be32382e64bdbba090ec810f1ccf50a09fe8648fc8a3408bbd2ab9ac73c6",
            "cost_drag": 0.000951243825,
            "cvar5_improvement": 0.03348109664275123,
            "drawdown_improvement": 0.1630697937572293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8718453862576584,
            "sortino_excess": -1.6465497270515694,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c1f8d05174940de5abab81e70dbabad9d91d52b696bb409bdd2ab6d799a45da8",
            "cost_drag": 0.0026511435749999998,
            "cvar5_improvement": 0.028945874931692157,
            "drawdown_improvement": 0.13783453970269374,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.272939744870617,
            "sortino_excess": -2.124422231850017,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
            "cost_drag": 0.0014195779250000002,
            "cvar5_improvement": 0.027018977669354505,
            "drawdown_improvement": 0.1290859020159868,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.733613622352713,
            "sortino_excess": -1.487540409883356,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c2723042d21e0f63b5e375cfd0cc6b239d7d1319ce461a03c6a1a2ef7049a724",
            "cost_drag": 0.0009637770500000001,
            "cvar5_improvement": 0.03361062760283034,
            "drawdown_improvement": 0.1632079985322293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8364199830766782,
            "sortino_excess": -1.625245357216428,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c3738ae7a721e173bf76984f66c2f685bc435209fd4dab537ffc550a62a23d7b",
            "cost_drag": 0.001021160775,
            "cvar5_improvement": 0.027762874274381483,
            "drawdown_improvement": 0.13260083647685905,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.41844929225106614,
            "sortino_excess": -1.0449881655865219,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c3a2b9e6812b3f6ca0f3a545088ae9cbf0150071f297f84c671e4ca96a08d7fb",
            "cost_drag": 0.000983959575,
            "cvar5_improvement": 0.027618378824363216,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.46848040628055987,
            "sortino_excess": -1.0664661007701781,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
            "cost_drag": 0.001137233325,
            "cvar5_improvement": 0.023881001605827276,
            "drawdown_improvement": 0.11345318375015795,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.20909712438860173,
            "sortino_excess": -0.5308061935936068,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c4e015ead6169a716f5f5e9c559d43e096fc921f96389ef1a18f5749d64d333b",
            "cost_drag": 0.0009692138,
            "cvar5_improvement": 0.027549313920867204,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23064709054422033,
            "sortino_excess": -0.5330451749645517,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
            "cost_drag": 0.0014313968500000002,
            "cvar5_improvement": 0.027965319705159905,
            "drawdown_improvement": 0.13403348296966672,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7694165213947406,
            "sortino_excess": -1.5417544924071684,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c732a62eeaa84162fc5a884fcc09486a2b9ee5c9039b8d9a0d76f72351d048d6",
            "cost_drag": 0.0011482763250000002,
            "cvar5_improvement": 0.029888191171228838,
            "drawdown_improvement": 0.14367312573542723,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6242551473106632,
            "sortino_excess": -1.357654633392302,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
            "cost_drag": 0.001276180075,
            "cvar5_improvement": 0.02595759696778643,
            "drawdown_improvement": 0.12405399277082799,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.43752399360353234,
            "sortino_excess": -1.0837822484638704,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c828166e74ca3a3a5edaf08d9a9cc9318061f12eaf8a971288d9fe9aa94f0002",
            "cost_drag": 0.0014922396,
            "cvar5_improvement": 0.035364700980612326,
            "drawdown_improvement": 0.17415000549174092,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.2024080282866367,
            "sortino_excess": -2.0721456661285673,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c848623e0be20099dc48e20d39b8cb65688053a8a496ec4aa885783422556572",
            "cost_drag": 0.0013461831000000002,
            "cvar5_improvement": 0.036971608099934,
            "drawdown_improvement": 0.18241154086227906,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.3862998597793124,
            "sortino_excess": -2.261491981885791,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c952cae7bd45116005f8eb31266d51ce6c128f513baffac095de4b6cb97384f6",
            "cost_drag": 0.0015060453999999998,
            "cvar5_improvement": 0.034343940584637356,
            "drawdown_improvement": 0.16596767539472737,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0880513318224558,
            "sortino_excess": -1.824420723047102,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ca6aa7709729328d94aa19e8129a8ec3f86ce1d32039e064fb623fbb8f1ac58e",
            "cost_drag": 0.0008256731000000001,
            "cvar5_improvement": 0.03131169770018997,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.28339304510256114,
            "sortino_excess": -0.6398234142369313,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.035,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cbe67dbd8ea3ade52ec52ba1d9625b2a6f87d9e55ccafd9a64fd847a889053cc",
            "cost_drag": 0.0014915084999999999,
            "cvar5_improvement": 0.02439101874803742,
            "drawdown_improvement": 0.11612273613937682,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8570603688587106,
            "sortino_excess": -1.6540203085487968,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
            "cost_drag": 0.0011475115249999998,
            "cvar5_improvement": 0.023872151820766314,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3770582025014716,
            "sortino_excess": -0.9672017085059603,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cd527804e36527d86170dc60b7b5297223c9325a141bce31c0379910247fe5f4",
            "cost_drag": 0.001510185075,
            "cvar5_improvement": 0.01865224756969345,
            "drawdown_improvement": 0.08760374132621646,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2583353649321147,
            "sortino_excess": -0.716149789040821,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
            "cost_drag": 0.00113869755,
            "cvar5_improvement": 0.02389230948910569,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5383321540367085,
            "sortino_excess": -1.2075102086243552,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cff9859d4a5f2814140612668f4daacf34db624bbfeb4347eae64ec9f633685b",
            "cost_drag": 0.001395882825,
            "cvar5_improvement": 0.029567025494892256,
            "drawdown_improvement": 0.1428958638021407,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3403193329372753,
            "sortino_excess": -0.8557459387941871,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
            "cost_drag": 0.00153768875,
            "cvar5_improvement": 0.02585185573977024,
            "drawdown_improvement": 0.12400443082003246,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.26747580747256716,
            "sortino_excess": -0.7079639422549762,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d3c336ea2c30970cb838c9559f28ef5afffee91fabd06beb0c1839e49256766d",
            "cost_drag": 0.0015002637749999999,
            "cvar5_improvement": 0.01650321858470148,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.33245221640738937,
            "sortino_excess": -0.9275729854138886,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
            "cost_drag": 0.001108696925,
            "cvar5_improvement": 0.02378763983965986,
            "drawdown_improvement": 0.11340724482387277,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.18128643224334146,
            "sortino_excess": -0.443711092932756,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d6b5f0adf9731cb102e277bd3fb3c7f60594548d2231a497b32c94673cd0b667",
            "cost_drag": 0.0015072047499999999,
            "cvar5_improvement": 0.023568876896005245,
            "drawdown_improvement": 0.11111197581437682,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6086412320117476,
            "sortino_excess": -1.3613130691090871,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d6db03d900f41c0c72fa21236bdcea5a570191d0749630206087c435ff3a8898",
            "cost_drag": 0.0014829385,
            "cvar5_improvement": 0.01657866991668324,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17846490214539534,
            "sortino_excess": -0.58850370067971,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d6db90ed5261d686d5775a7fe7c23cbce9b135bff6dee12a51a8f348722dcbcd",
            "cost_drag": 0.000840020925,
            "cvar5_improvement": 0.031362683925151645,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.7388112536426568,
            "sortino_excess": -1.4689851080972525,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d6dfb2a62a2c81350ef9e449a06dc69ac134a1e3741a97bf3776f014a02b7bde",
            "cost_drag": 0.001960125625,
            "cvar5_improvement": 0.02823154927610503,
            "drawdown_improvement": 0.13600758328256063,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0221071813103655,
            "sortino_excess": -1.786429004662992,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d726ac15f78e72d7171a62d66dcf57ed06bd6d2e3d2d36113bbde161c0666e27",
            "cost_drag": 0.001016662,
            "cvar5_improvement": 0.03523910689464659,
            "drawdown_improvement": 0.17295181437985357,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.9200467027805501,
            "sortino_excess": -1.6627886833199983,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "d8d5c98b26ff14e3212cd6294dddc02b69e28e1725828e71a010ae9c00e64f87",
            "cost_drag": 0.00167430985,
            "cvar5_improvement": 0.020986846834582865,
            "drawdown_improvement": 0.09794711602621647,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6476570305188503,
            "sortino_excess": -1.4242467764523727,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "da28e066148553678760b45c21a54f0f815cb41838c646423fedd4acd0c69f0d",
            "cost_drag": 0.002275419525,
            "cvar5_improvement": 0.0232703871499766,
            "drawdown_improvement": 0.10996217480706952,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5371684769767242,
            "sortino_excess": -1.2640630976909324,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "daa598de199db4f2abe5d43ad5487cc9e98f006ac89533dc04afd523606d5df7",
            "cost_drag": 0.0013497091249999999,
            "cvar5_improvement": 0.020426036313216833,
            "drawdown_improvement": 0.09504900357826795,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.38873413172283405,
            "sortino_excess": -1.0379854317530641,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "db3ce2343cab6d1650bea124ea4ff260409091058133b2b9bd6fe8a6fd2ff9a4",
            "cost_drag": 0.0010678272000000002,
            "cvar5_improvement": 0.03341789436330742,
            "drawdown_improvement": 0.16252588841414684,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8665476922393184,
            "sortino_excess": -1.6342959535411172,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "dcaf4f81927c472859f6300f1b7ac9cec525bb1864c151d3d4070612ae8e5df4",
            "cost_drag": 0.00127505985,
            "cvar5_improvement": 0.020081832509670716,
            "drawdown_improvement": 0.09493070087464628,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.15743560435351356,
            "sortino_excess": -0.417341257535466,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.6,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
            "cost_drag": 0.0016355126999999998,
            "cvar5_improvement": 0.023269696456585526,
            "drawdown_improvement": 0.1101375928594435,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6642196678311729,
            "sortino_excess": -1.406992559470801,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
            "cost_drag": 0.001160341425,
            "cvar5_improvement": 0.0240245516435769,
            "drawdown_improvement": 0.11351385804078176,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.31992195791358985,
            "sortino_excess": -0.8572440948653842,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "deba15173d77c901d382e9f5272229ae1cba6daa2726b4bb6ce9634e86a14da7",
            "cost_drag": 0.001251210925,
            "cvar5_improvement": 0.029636093532520804,
            "drawdown_improvement": 0.14270468832947378,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6751693981352982,
            "sortino_excess": -1.3988866114444862,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e062b42fc995eb71bc33d23b0a1a7171cd43966949db71673235e334018a8b9f",
            "cost_drag": 0.0020031187,
            "cvar5_improvement": 0.020493869919310712,
            "drawdown_improvement": 0.09715045953933715,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.33977770281093295,
            "sortino_excess": -0.9440014698863084,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.15
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e15d48069bf09f9bb10971f06b1a917c4b07e6c1a074d0d1388e0185650d24cd",
            "cost_drag": 0.0010831954250000002,
            "cvar5_improvement": 0.034349519121810904,
            "drawdown_improvement": 0.16761384085950023,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.0893295594827066,
            "sortino_excess": -1.8846779358992558,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e2c8bb705339dcc5463a443085ff18111efcc79131fc23f37b0689f00224e812",
            "cost_drag": 0.001460516075,
            "cvar5_improvement": 0.016438271497559276,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.12561220431254244,
            "sortino_excess": -0.3944250309978277,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.025,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e2cff1ab7f737919236ab95a7fedc68c273418b1b4245a5f6ac6c54916c93f70",
            "cost_drag": 0.001748484025,
            "cvar5_improvement": 0.018512384259308817,
            "drawdown_improvement": 0.086622158191553,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3204156210193952,
            "sortino_excess": -0.8716429259967273,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e43174b66cae18536744c3921b38ea3b06411d2aafef1ba96738db80f17ae80b",
            "cost_drag": 0.0013303386999999997,
            "cvar5_improvement": 0.03429228274890655,
            "drawdown_improvement": 0.16784289064882355,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.8978744399909988,
            "sortino_excess": -1.649158517543215,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e4fc4425fef1519fb6942a195045717cd0d7d9196af4d4bbd9def08121347069",
            "cost_drag": 0.000999354225,
            "cvar5_improvement": 0.027634235956148605,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6554189248461953,
            "sortino_excess": -1.3578175677781303,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e5da6823593cc26f966c1b236eb2179524508f51ac24bb8ecc1ae9cf0512a2d2",
            "cost_drag": 0.0009709731500000001,
            "cvar5_improvement": 0.03245097370107938,
            "drawdown_improvement": 0.1574492170322293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3926130578345709,
            "sortino_excess": -0.946325728657779,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e63647ca2002739cec51718c1fc3233e1fa1a415c34c193d001a7c1cd59f7a79",
            "cost_drag": 0.0008446008500000001,
            "cvar5_improvement": 0.0314517885799184,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5444423018104043,
            "sortino_excess": -1.2184840662455303,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.03,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
            "cost_drag": 0.00125516705,
            "cvar5_improvement": 0.024933952296217966,
            "drawdown_improvement": 0.11885509227082797,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.24223014448002805,
            "sortino_excess": -0.6340760296362473,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.055,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "eb49287bc547c6e506f3aadb7eda6b7daada828a03319fcee65cf5fdd3c3fd6a",
            "cost_drag": 0.001443978675,
            "cvar5_improvement": 0.016362152099880498,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.12651643987827466,
            "sortino_excess": -0.376939666430623,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.045,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "edcf6df73115739f59495a635a2f6e95889a072a90f65715f3683de0279b6036",
            "cost_drag": 0.001511580175,
            "cvar5_improvement": 0.01681554637399174,
            "drawdown_improvement": 0.07692417231824791,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.49343830708603287,
            "sortino_excess": -1.190087250483015,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "eec8e6bf15537c408060e82aa9252bc11c299b5ededb53194b719629a246267c",
            "cost_drag": 0.0012751610000000001,
            "cvar5_improvement": 0.03542082897816798,
            "drawdown_improvement": 0.17336892217684852,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.036507990532102,
            "sortino_excess": -1.787074244815768,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "f06c82a4eeb01c2ca1b3775d507f3fdf523eac9e7bd4f72ae421cb474e7f3e8d",
            "cost_drag": 0.000858670575,
            "cvar5_improvement": 0.03242406555808391,
            "drawdown_improvement": 0.1576634351322293,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.36701896629075276,
            "sortino_excess": -0.8306366586360427,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.01,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "f6b877f3dea41247ace7a39e777e2d4b447a149ec4484b84b0ac6649e6790b93",
            "cost_drag": 0.0016102052750000002,
            "cvar5_improvement": 0.03441429720369753,
            "drawdown_improvement": 0.1673615354708544,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -1.2191938027539242,
            "sortino_excess": -2.039021085639252,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "f6d7509f3f5c1634fea76f4dd53e98841aa76151e5c756d7dfd55b79d67dc8f8",
            "cost_drag": 0.001235856325,
            "cvar5_improvement": 0.033333704879018766,
            "drawdown_improvement": 0.1623828411591433,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5046561097578399,
            "sortino_excess": -1.1227470607739205,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.3,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "fa155e38f105769756379f1664a8105153b41ea206f3fa703f1dea61f6e2fc4a",
            "cost_drag": 0.000799661375,
            "cvar5_improvement": 0.031525304020192296,
            "drawdown_improvement": 0.15194098450779708,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.6205670274211237,
            "sortino_excess": -1.3483302061134355,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "fb7cf5a396194be308efbdd959d12d7a0c48b1193d5a2caac5caa3adc4c65a92",
            "cost_drag": 0.001543980925,
            "cvar5_improvement": 0.02092499463053299,
            "drawdown_improvement": 0.09859785767621645,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5595319300323482,
            "sortino_excess": -1.2471065802695818,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.05,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "fbe5f873390f4fa9623ed2084060dd9b386dcb41caa2b71b95f0f2129cf57a56",
            "cost_drag": 0.000985311775,
            "cvar5_improvement": 0.027623204725543932,
            "drawdown_improvement": 0.13251488050599602,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22960696701748035,
            "sortino_excess": -0.5664780182263545,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "fd673b08ae5457fc2c262ed05bda3c5d6934808f9935cbade4c0d6172f79ad0f",
            "cost_drag": 0.0010315216499999999,
            "cvar5_improvement": 0.02985673999166156,
            "drawdown_improvement": 0.1440634467604272,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.5118243964531124,
            "sortino_excess": -1.1503786241183702,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.4,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.04,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "fde5f8993452adb198b2aebe545089a0c13eb1c9000759d5e47c483b81d0ca3b",
            "cost_drag": 0.0010028940750000002,
            "cvar5_improvement": 0.02866369543116179,
            "drawdown_improvement": 0.13821344231042723,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.28836327555518376,
            "sortino_excess": -0.6703881670349595,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.015,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
            "cost_drag": 0.001681025275,
            "cvar5_improvement": 0.026845320566912363,
            "drawdown_improvement": 0.12932834441947091,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.44827530246785907,
            "sortino_excess": -1.0550345364576783,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.7,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.06,
                "unit_pct": 0.05
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ffcbf75f862ff7b602b47b861df9fc8a853843804e38aef1f90875d90a3822e7",
            "cost_drag": 0.00144407895,
            "cvar5_improvement": 0.016362337828459257,
            "drawdown_improvement": 0.07673671366301865,
            "exposure_ratio": 0.6091269841269841,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.12091145548455817,
            "sortino_excess": -0.3630520125844244,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "0165967a82c576ce3dbbcae3a03db3d0b9766a1b6ba0de5459235753d980e642",
            "cost_drag": 0.0007820402,
            "cvar5_improvement": 0.03939157475763567,
            "drawdown_improvement": 0.20454108850525304,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "02ed4b871a3ac2dc98111f5f7dba62b21c61af723cae0b25f7d3fa568b6642e4",
            "cost_drag": 0.0003181703,
            "cvar5_improvement": 0.04151395066828137,
            "drawdown_improvement": 0.21063583169352829,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "05063fd72167d3a3a2da97e7c8c63023ebe7fe845967932f2a3a68b2d9023574",
            "cost_drag": 0.000827058375,
            "cvar5_improvement": 0.03934136917865246,
            "drawdown_improvement": 0.2045036655815924,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "07a6da34a90c5c24e8cfdef1b9c07e2ff039d51fce0b917d7a4ba2527844daa4",
            "cost_drag": 0.0002868756,
            "cvar5_improvement": 0.041966944261551266,
            "drawdown_improvement": 0.21158386932602263,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "091fbd2cc185b592a8e7b80f30e3e73fb8f3034ef10dcb197ae208d1892901d3",
            "cost_drag": 0.000702064825,
            "cvar5_improvement": 0.04021540331079148,
            "drawdown_improvement": 0.20769231388025303,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "09c907ccffba9c79389da45ffbc273ef56ff552a01e37bb47bf4b4f538584933",
            "cost_drag": 0.0003181703,
            "cvar5_improvement": 0.04151395066828137,
            "drawdown_improvement": 0.21063583169352829,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0a073f60f2b4e958cf7bb14f680436f06eb26b748c281a78271005a1011caa57",
            "cost_drag": 0.00034826445,
            "cvar5_improvement": 0.04147652276249916,
            "drawdown_improvement": 0.21050015313643194,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "0c441452555d21094fcf63b740acffe7a9176260632649cedf006f78d5c922dc",
            "cost_drag": 0.00032556910000000003,
            "cvar5_improvement": 0.04175914080977127,
            "drawdown_improvement": 0.21078017582602263,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "0dee04873a3ddf671052ea481c0d968718285776ddcfc900e5af011213ad542b",
            "cost_drag": 0.000702064825,
            "cvar5_improvement": 0.04021540331079148,
            "drawdown_improvement": 0.20769231388025303,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "0efce7b04e5e193de8d96ae22d700309b50d9ec1b26b72a73c3a1a9f6769501d",
            "cost_drag": 0.00039654154999999995,
            "cvar5_improvement": 0.041577994000140936,
            "drawdown_improvement": 0.21025442480715822,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "12643fc27869a63bcca87e3e38c0aae6f7825f6728622759920ecebf182931d1",
            "cost_drag": 0.0007470830000000001,
            "cvar5_improvement": 0.04016519773180827,
            "drawdown_improvement": 0.20765489095659237,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "13a36acfc6269b30b569bb601b5e16abcb027c50365afdcb43ae693eeb166958",
            "cost_drag": 0.0007017029500000001,
            "cvar5_improvement": 0.0399548354160538,
            "drawdown_improvement": 0.20626700821415295,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "13e36312d75235095a99fb4673caba20941b36b205e0f88c729e7bc1900c423e",
            "cost_drag": 0.0005622870250000001,
            "cvar5_improvement": 0.04073468637703364,
            "drawdown_improvement": 0.20811597774072127,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "1424ccb6f148503ef949aaec1c140dfeedf287a16154036803144b75c5de03c2",
            "cost_drag": 0.0008280064999999999,
            "cvar5_improvement": 0.039332158662139974,
            "drawdown_improvement": 0.20450132630152917,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "161dbc35e812294ca418d3a491ac83452d7dae568d1e5be10421ee4e19fdab27",
            "cost_drag": 0.0007026914000000001,
            "cvar5_improvement": 0.040215533637168115,
            "drawdown_improvement": 0.2076898887870944,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "17c9c940096d43a773c4905d1982dc3a9c901fae82b8de14cfb27f6844ce84c0",
            "cost_drag": 0.0005256084,
            "cvar5_improvement": 0.040669127037593476,
            "drawdown_improvement": 0.20873306391437807,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "17dbff0a23e5d013e2d4b110485364f1d520f1dd5b5b79ea9cec2328e6048ff9",
            "cost_drag": 0.000702064825,
            "cvar5_improvement": 0.04021540331079148,
            "drawdown_improvement": 0.20769231388025303,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1a0ba2f00044f420ffb20d85ffd3b630915c4f0587b631a9e61e8fc68b943b2c",
            "cost_drag": 0.00047874142499999996,
            "cvar5_improvement": 0.040868954296805475,
            "drawdown_improvement": 0.20851867893313625,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1a1d82ea59c99bfe7ac50c54c249f33eecaf9e8d07e4abf76bdd391e3652f99b",
            "cost_drag": 0.000488094825,
            "cvar5_improvement": 0.0408407685075295,
            "drawdown_improvement": 0.20849316652212493,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "1a8b7c2b566250e4974b9accd1eb288e0b1c3b9ece047603707261bce302dd08",
            "cost_drag": 0.00032556910000000003,
            "cvar5_improvement": 0.04175914080977127,
            "drawdown_improvement": 0.21078017582602263,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "1b03d2707a07fe802f1760263c82b3d4b8342a455e2139542829ce33055346c3",
            "cost_drag": 0.00035784805,
            "cvar5_improvement": 0.041785797451920924,
            "drawdown_improvement": 0.21105811830715823,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "1b8a1433cd25010fb5c550b3665e973d63467cfe7baa46e828f42e0e3914c235",
            "cost_drag": 0.0007011881250000001,
            "cvar5_improvement": 0.03998210839557155,
            "drawdown_improvement": 0.20627122536894854,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "1c9aaeaf1c01aaa86bd6f9b2a9def8c7f55b76815b48c037012df2db186a7ad9",
            "cost_drag": 0.00063610095,
            "cvar5_improvement": 0.040556292916740684,
            "drawdown_improvement": 0.20862027482535672,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "1e3c5a3a25ba0ff260f82888076b19bd3e2497627e62d17545f54d5382b673a9",
            "cost_drag": 0.0007026914000000001,
            "cvar5_improvement": 0.040215533637168115,
            "drawdown_improvement": 0.2076898887870944,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "1fec94aa0bead42b20075940b637e819472c020dce8613fa5a3c7aa21734fd06",
            "cost_drag": 0.0003301312,
            "cvar5_improvement": 0.04174463015617515,
            "drawdown_improvement": 0.21076842451361666,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "23d1e52eeccaf4bc0cb8853853c2be63a69dd7762b18d7289741c7e7f37b98f9",
            "cost_drag": 0.0002868756,
            "cvar5_improvement": 0.041966944261551266,
            "drawdown_improvement": 0.21158386932602263,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "275334c7d66460505e7c71e7f1bc8e971d6b44f3af26a6b8dba212d744d4d00a",
            "cost_drag": 0.000702064825,
            "cvar5_improvement": 0.04021540331079148,
            "drawdown_improvement": 0.20769231388025303,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2c75c42046ef3a6d0f0febae245bcf1a0d429394847dcdc593062e759c731b73",
            "cost_drag": 0.000510360725,
            "cvar5_improvement": 0.04111612858347596,
            "drawdown_improvement": 0.2096959241763279,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "2d4e420f979f519ab7261ed8c86ca8308618af6e63b56f5476e2d2fce0fd8a14",
            "cost_drag": 0.0005256084,
            "cvar5_improvement": 0.040669127037593476,
            "drawdown_improvement": 0.20873306391437807,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "330e9079a8741ac5ed4d998877d62b08834a5251908efa8b14fa9b09f101662a",
            "cost_drag": 0.000562747725,
            "cvar5_improvement": 0.04070433907285644,
            "drawdown_improvement": 0.20811353717632788,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "376261879bb3a98cb9d9f885ebc4606248424ee5623184ed545ba758deb3d361",
            "cost_drag": 0.0007023828249999999,
            "cvar5_improvement": 0.03993715888720894,
            "drawdown_improvement": 0.20624774295035675,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "37ce18ea991b11a33fd546c75664f8cafed609d4a7311f44011f1ac689f5ecbe",
            "cost_drag": 0.00021436815000000002,
            "cvar5_improvement": 0.042084550538379194,
            "drawdown_improvement": 0.21187070808237712,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "387050649e85b36d7c6e999764671f946e30e8f6587f959815efda2fee8967c9",
            "cost_drag": 0.00047874142499999996,
            "cvar5_improvement": 0.040868954296805475,
            "drawdown_improvement": 0.20851867893313625,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3d16b6890afaf109d0c4451863565fe56cb71dd1454039aa22d95648f62fe42d",
            "cost_drag": 0.000562747725,
            "cvar5_improvement": 0.04070433907285644,
            "drawdown_improvement": 0.20811353717632788,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "3de7c13e774d534c952c8462bc02d4706ba6c2da63098dcc633d9891959119c9",
            "cost_drag": 0.000782666775,
            "cvar5_improvement": 0.0393917050840123,
            "drawdown_improvement": 0.20453866341209442,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "42105ee5fa31f194122fe24f85377d35b1afea27da9bbed7fe4efa1b04df9b81",
            "cost_drag": 0.0005622870250000001,
            "cvar5_improvement": 0.04073468637703364,
            "drawdown_improvement": 0.20811597774072127,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "4266ee5cc6a9ac907f421389ef9cf425c951ac9475f81729c7ed50f0150b1b7d",
            "cost_drag": 0.000244835375,
            "cvar5_improvement": 0.042019592655475675,
            "drawdown_improvement": 0.21169797311045763,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "42881131aa958b37001b7427d92d5475137405fe28d79f77e10b24316f77ab3c",
            "cost_drag": 0.0007809151750000001,
            "cvar5_improvement": 0.04014325201517409,
            "drawdown_improvement": 0.20762269849242407,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "441990e611d4bfed0a753adb7d990a66af9681ccb20bb032d058f3e3bf793c67",
            "cost_drag": 0.0002868756,
            "cvar5_improvement": 0.041966944261551266,
            "drawdown_improvement": 0.21158386932602263,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "443522543e3e8dd041a7ffeee4af344efccc3ec16395b525bc91265308a4d846",
            "cost_drag": 0.0005256084,
            "cvar5_improvement": 0.040669127037593476,
            "drawdown_improvement": 0.20873306391437807,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "44cb7392c928f53c521015a2cd2d0d65ae8766b2261ffc6f5861bc3196ad086f",
            "cost_drag": 0.000635421075,
            "cvar5_improvement": 0.04057396944558554,
            "drawdown_improvement": 0.20863954008915292,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "45fc69735e2a6498f6345128fd7d46a7e5ad7bc5aa540c5fe68355a5a078e402",
            "cost_drag": 0.00056814705,
            "cvar5_improvement": 0.040677785558859716,
            "drawdown_improvement": 0.20872556521754135,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "46f7afbe4f52f52cf8832a43b79598af956b8e0d3541d6425464a97964d756c0",
            "cost_drag": 0.00024403145,
            "cvar5_improvement": 0.042039320934150144,
            "drawdown_improvement": 0.21159960299432917,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "492d3075b7505d752fc4569124324cf50ec4e1e12399bff92d72a757be0abcea",
            "cost_drag": 0.00035716052500000005,
            "cvar5_improvement": 0.04182832440233635,
            "drawdown_improvement": 0.21116162523985732,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4a09e9f42c304e0c0f941aa4fb00cfc45f473ebaa326e8c08008a0a2a91e8d4c",
            "cost_drag": 0.0005613474750000001,
            "cvar5_improvement": 0.04105405030910382,
            "drawdown_improvement": 0.20935787940355427,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "4bfb9404f1e53fa2d8ba993a154c73bc83122dfdb210429965cadb5122d6cb5d",
            "cost_drag": 0.000747105875,
            "cvar5_improvement": 0.04018312768840202,
            "drawdown_improvement": 0.20765416100482711,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4c5dbff3038888fbc8ba660d551023c7213bc3c92e7d698161e4831ddb927e16",
            "cost_drag": 0.000510360725,
            "cvar5_improvement": 0.04111612858347596,
            "drawdown_improvement": 0.2096959241763279,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "4ef5f2e60b0a12f9c3dfdfc50ff212dda872ca3811ba7eb1a418cd635500ee86",
            "cost_drag": 0.00063490625,
            "cvar5_improvement": 0.040601242425103296,
            "drawdown_improvement": 0.2086437572439485,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "505ad729a6207cc8be7b2d3fe972a46ba111f58eeaa7b3b530a2cfa2e1d371ac",
            "cost_drag": 0.000435707825,
            "cvar5_improvement": 0.04125255801814901,
            "drawdown_improvement": 0.21007555352212495,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "50aeca7dbe7571cfa0dd145f2032d40a70a44efb66da2450d2ac21fc20d8ac95",
            "cost_drag": 0.000426354425,
            "cvar5_improvement": 0.04128074380742499,
            "drawdown_improvement": 0.21010106593313627,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "512697187c6fe64646e9ff21e491e8e481880ebae3fbd0e5138c76ee036ec1d5",
            "cost_drag": 0.000747105875,
            "cvar5_improvement": 0.04018312768840202,
            "drawdown_improvement": 0.20765416100482711,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "520cb3507a916dc9d9f2fa51dacd4e7c3511bbf9eee1fcdf03da237bb9f07e11",
            "cost_drag": 0.000635421075,
            "cvar5_improvement": 0.04057396944558554,
            "drawdown_improvement": 0.20863954008915292,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "52db97a65a1d4ad3cfa5799f59629bcab32d4cb9e84027e5ec07afc0fc759dea",
            "cost_drag": 0.0007017029500000001,
            "cvar5_improvement": 0.0399548354160538,
            "drawdown_improvement": 0.20626700821415295,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "53ae75468006b31323bf7c8217cd72f20b714d1c350e56945d1b7cb891a67f57",
            "cost_drag": 0.00063610095,
            "cvar5_improvement": 0.040556292916740684,
            "drawdown_improvement": 0.20862027482535672,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "548bde01f4ae3b39c455be93505eda30b321c79668d9f8acde7f81aac0feefc0",
            "cost_drag": 0.000244835375,
            "cvar5_improvement": 0.042019592655475675,
            "drawdown_improvement": 0.21169797311045763,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "59b014959d6ca4769d4753c652daf0ccb38e962e5c3d4d3ea42fec5bd2a2a57a",
            "cost_drag": 0.0003660719,
            "cvar5_improvement": 0.0414255721257211,
            "drawdown_improvement": 0.2101065904247031,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "5bf8412a3fe2565df7fe2ecd3cf0bf8ef854466aaaa317215f6937328ff3ab18",
            "cost_drag": 0.000438811375,
            "cvar5_improvement": 0.04102519709855609,
            "drawdown_improvement": 0.20951202260771828,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "61609ced85a7068bb6b227a8778db35ac30701765ed24a2d414765a7965417f9",
            "cost_drag": 0.000244835375,
            "cvar5_improvement": 0.042019592655475675,
            "drawdown_improvement": 0.21169797311045763,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "64e6f60cccaa85fd39f8b1fa74bc32547aeab8eb0fc0ea90356ebdca81ab94da",
            "cost_drag": 0.0005256084,
            "cvar5_improvement": 0.040669127037593476,
            "drawdown_improvement": 0.20873306391437807,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "64e8b768141ab52605621addcd48eb9cc31b1ffcd58858b53f7d3015b5511af3",
            "cost_drag": 0.00039778895,
            "cvar5_improvement": 0.0413496418227808,
            "drawdown_improvement": 0.20987247179096277,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "673a28cda6786a76d77f41b3d518b2dc00aa5c1482c95959af2c5318831043bd",
            "cost_drag": 0.000747105875,
            "cvar5_improvement": 0.04018312768840202,
            "drawdown_improvement": 0.20765416100482711,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "696913cb4f51a33bf3935b51da3b38e1dcd6d1a97557ef171529553b4d7bfbf7",
            "cost_drag": 0.000634428925,
            "cvar5_improvement": 0.04005865152932797,
            "drawdown_improvement": 0.20635303334254138,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "6a23f24486bb79be48113d97b10bbba4ac19f7ddef0e43e81ec8d1dc67ff9092",
            "cost_drag": 0.000396073925,
            "cvar5_improvement": 0.041619659908713275,
            "drawdown_improvement": 0.2103547409735895,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "6c62868387b90bf0e5d50a007eb97dff2c5f410ac777bb74e949f24ca4545cd4",
            "cost_drag": 0.00063490625,
            "cvar5_improvement": 0.040601242425103296,
            "drawdown_improvement": 0.2086437572439485,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6d0b27b35b089a17eb96ff6e8962cf760fda88c3a3d4da56f20518c119a22fea",
            "cost_drag": 0.000426354425,
            "cvar5_improvement": 0.04128074380742499,
            "drawdown_improvement": 0.21010106593313627,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "6fc8e2eef32a9bbeedf4d1623087ba3891701d13c78d22843cdf57a1c9bb12be",
            "cost_drag": 0.00056814705,
            "cvar5_improvement": 0.040677785558859716,
            "drawdown_improvement": 0.20872556521754135,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "707d5fac1ebe3f88df9b8bca06082ec5f029dbaaa67f900f17bdbb99418ae959",
            "cost_drag": 0.0007470830000000001,
            "cvar5_improvement": 0.04016519773180827,
            "drawdown_improvement": 0.20765489095659237,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "74615fd57e7c943c143fd077540a3361517eb745a26477811b844f682456d219",
            "cost_drag": 0.000635421075,
            "cvar5_improvement": 0.04057396944558554,
            "drawdown_improvement": 0.20863954008915292,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "76c2fdbf72a6ee26af1f5ea026eca75afdfcee1086f79c917047a7c7ab3c01ed",
            "cost_drag": 0.000827058375,
            "cvar5_improvement": 0.03934136917865246,
            "drawdown_improvement": 0.2045036655815924,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "7e25e305550d53d8dd69c7eeb54c0b6e13240426682cf97ea575590254e15a8f",
            "cost_drag": 0.000426354425,
            "cvar5_improvement": 0.04128074380742499,
            "drawdown_improvement": 0.21010106593313627,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "7ec3d94889c6256057b589f9a9349e6f11c29591facbfc6dd184ffe7dc58d8de",
            "cost_drag": 0.00058259795,
            "cvar5_improvement": 0.040554238400949995,
            "drawdown_improvement": 0.2081511841600595,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "81f56cf56a5de341c5d98c82cf7d5803225386e334d2d1d583526e9c4ea5e855",
            "cost_drag": 0.00082708125,
            "cvar5_improvement": 0.03935929913524621,
            "drawdown_improvement": 0.20450293562982713,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "8538b7affe3bb97a027406cdbf0ee82edbf2a14cf9b0164e0f3b16e518dcce49",
            "cost_drag": 0.00050889595,
            "cvar5_improvement": 0.040669127037593476,
            "drawdown_improvement": 0.20873306391437807,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "891e4aac1326376aff627803dcff3b5d016adb3f7c1d241c033375b50f4f5659",
            "cost_drag": 0.000747105875,
            "cvar5_improvement": 0.04018312768840202,
            "drawdown_improvement": 0.20765416100482711,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "8bf92734c3d2ba8e6c3dd7f599c5b43e34620f9479e5c24f9b34ccbe045b4947",
            "cost_drag": 0.00040458034999999994,
            "cvar5_improvement": 0.04174867639741066,
            "drawdown_improvement": 0.21081599905676354,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "90e95eca032bfe50e881261b29e392fa034ba82c6ca75e51bb44c3dd72c9275c",
            "cost_drag": 0.0006787265499999999,
            "cvar5_improvement": 0.040528624103661696,
            "drawdown_improvement": 0.20847981742169033,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "915b629158bae600eedb793e1b7461db1bca2642934e70e963373d51bb0eec9d",
            "cost_drag": 0.000435707825,
            "cvar5_improvement": 0.04125255801814901,
            "drawdown_improvement": 0.21007555352212495,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
            "cost_drag": 0.0006137344750000001,
            "cvar5_improvement": 0.040642260798484306,
            "drawdown_improvement": 0.20777549240355425,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9755e4a2985929b24476e74975b3281dcf102f99fc184339e833c99c9365e566",
            "cost_drag": 0.000509900025,
            "cvar5_improvement": 0.041146475887653154,
            "drawdown_improvement": 0.2096983647407213,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "9a5ffaf7d90c7cd06362d27f96a11d349d1b8f1dd81f180cf81cb93f13789ea5",
            "cost_drag": 0.000357380425,
            "cvar5_improvement": 0.04182746336049326,
            "drawdown_improvement": 0.2111584344735895,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9a8031973c8ec766ac9566a91c4f700fd8d2a7712f8f4e3641c67b8135e77bca",
            "cost_drag": 0.0005613474750000001,
            "cvar5_improvement": 0.04105405030910382,
            "drawdown_improvement": 0.20935787940355427,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "9b43cfb13d4e03c1d855e2b81d3146f84cdd7f6155194208cff59649e4fafedd",
            "cost_drag": 0.0007820402,
            "cvar5_improvement": 0.03939157475763567,
            "drawdown_improvement": 0.20454108850525304,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "9fcab2c463797c9b28ee01148cc476784bb2473b84bf8f2ae68c546f3cb9c946",
            "cost_drag": 0.00035757414999999993,
            "cvar5_improvement": 0.041804371417883825,
            "drawdown_improvement": 0.2111555511230664,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a05a3729a4575c24923de713a0ba59f30f2cfd21472905bb9a557e2e85fe5392",
            "cost_drag": 0.000509900025,
            "cvar5_improvement": 0.041146475887653154,
            "drawdown_improvement": 0.2096983647407213,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "a164ba23ba9524e034fe07bfe24aea3b27db569bc592dca70655d980b21fcdd3",
            "cost_drag": 0.000748031125,
            "cvar5_improvement": 0.040155987215295785,
            "drawdown_improvement": 0.20765255167652916,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a2606ff0dd53e64bdaed4879ebef55587c576527665e09aaceec8068c023f1fa",
            "cost_drag": 0.000509900025,
            "cvar5_improvement": 0.041146475887653154,
            "drawdown_improvement": 0.2096983647407213,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "a5c471fd8ef46b803b80689400b2fc0c30d0ff6a0d4e6a27deb9881f27514916",
            "cost_drag": 0.0002868756,
            "cvar5_improvement": 0.041966944261551266,
            "drawdown_improvement": 0.21158386932602263,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "a7d1bc64be18eec70f804ccb675f4de3265988e1f7041b8dac11721a645fbccd",
            "cost_drag": 0.00050889595,
            "cvar5_improvement": 0.040669127037593476,
            "drawdown_improvement": 0.20873306391437807,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "a7e3098ae1d238b85a68bf710352484a836546f125d4abdecafda4bd5b6ce8e1",
            "cost_drag": 0.0005967574000000001,
            "cvar5_improvement": 0.040554238400949995,
            "drawdown_improvement": 0.2081511841600595,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "adbca544282724c5a7a2958f71250737af4685caeb95879a42bc97e6fba41fa0",
            "cost_drag": 0.00029143770000000004,
            "cvar5_improvement": 0.041952433607955135,
            "drawdown_improvement": 0.21157211801361667,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "add329e8e27ecebe1d584cb1f14ba572d35710aea60476ca8ccbc31431672993",
            "cost_drag": 0.000510720375,
            "cvar5_improvement": 0.0410936166348222,
            "drawdown_improvement": 0.20961459027402735,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ae2f1ec1405653fbbf289a5f020fe4b9ab1365648959be0631bcd1db772eadad",
            "cost_drag": 0.000426354425,
            "cvar5_improvement": 0.04128074380742499,
            "drawdown_improvement": 0.21010106593313627,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "b1ce106b9791d9b2313e33ad5d36230eb1a10a96118d83ef7b6350514a957bd9",
            "cost_drag": 0.00039626765,
            "cvar5_improvement": 0.04159656796610383,
            "drawdown_improvement": 0.21035185762306638,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "b3ab56d68fdcaada002d2614a264764fe445837a7212d9cef39fd0934e9a098b",
            "cost_drag": 0.00044327385,
            "cvar5_improvement": 0.04154087294563067,
            "drawdown_improvement": 0.21001230555676353,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b4a19d9ee57a1ed883fc45f2d940417ba33b9bcd8854935c3d9ed02a29df5c44",
            "cost_drag": 0.000509900025,
            "cvar5_improvement": 0.041146475887653154,
            "drawdown_improvement": 0.2096983647407213,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "b54d6a3fa555012188e6f740379a78f0dd22cd68864cae4eb9e915ce67e8baaa",
            "cost_drag": 0.0007470830000000001,
            "cvar5_improvement": 0.04016519773180827,
            "drawdown_improvement": 0.20765489095659237,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "b5ae512c057c4cca149fc22aa5ab060d43221cfcfb62184e6b988b8670e045e0",
            "cost_drag": 0.000438811375,
            "cvar5_improvement": 0.04102519709855609,
            "drawdown_improvement": 0.20951202260771828,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "b7aa686834fba404e57ce646e62ea5ae9ce6b33df36f634aa733cced8430673f",
            "cost_drag": 0.0005790605000000001,
            "cvar5_improvement": 0.04064999356750923,
            "drawdown_improvement": 0.20870159914844,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "b7c893047999c7d6c75f8da734604fb8e463ffc56e36cbccd00fa3732bfff73c",
            "cost_drag": 0.0005790605000000001,
            "cvar5_improvement": 0.04064999356750923,
            "drawdown_improvement": 0.20870159914844,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "b9bc2fd53b37952d0fa31d7ee6c7abb2df29fc0c936f761b0b4d5de89d3b3c65",
            "cost_drag": 0.0005655889500000001,
            "cvar5_improvement": 0.04057181860500765,
            "drawdown_improvement": 0.2081511841600595,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "bc6f099a3c49e384ab643559ec0ec44d65d442396a1dc177bb4c7181ac52ae54",
            "cost_drag": 0.000395854025,
            "cvar5_improvement": 0.041620520950556364,
            "drawdown_improvement": 0.2103579317398573,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "bcaf1067a4e98787b432db5b6681a208b9eea62150fe336c1090df3b4f678dfc",
            "cost_drag": 0.0007470830000000001,
            "cvar5_improvement": 0.04016519773180827,
            "drawdown_improvement": 0.20765489095659237,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "bd61e6ffa991468a6062bf4047742d76be80658e74f9212ae8482ed6d90027cf",
            "cost_drag": 0.00035757414999999993,
            "cvar5_improvement": 0.041804371417883825,
            "drawdown_improvement": 0.2111555511230664,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "bdfeea35c79ba78c3054cc430396a6f0454ffcb4c0eefca49e78830b92de5ccc",
            "cost_drag": 0.00034826445,
            "cvar5_improvement": 0.04147652276249916,
            "drawdown_improvement": 0.21050015313643194,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "be75d5c8e26860196c89f31b797698e558e2c7568cb1a802d2a09507366516ca",
            "cost_drag": 0.000357380425,
            "cvar5_improvement": 0.04182746336049326,
            "drawdown_improvement": 0.2111584344735895,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "bf18cc0ff8f31c28dd27bd53bea9a4b8740f08d9cba11a3a14cacc6d1091b9ef",
            "cost_drag": 0.00063490625,
            "cvar5_improvement": 0.040601242425103296,
            "drawdown_improvement": 0.2086437572439485,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "bfc4d87ac49a11a984a17ee8bc2a235c4905e425284c08722bc83a3787c3da0f",
            "cost_drag": 0.0006787265499999999,
            "cvar5_improvement": 0.040528624103661696,
            "drawdown_improvement": 0.20847981742169033,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "c1144d55f4b001966183229609c62f71533195749e340dc147b58b34996d34b1",
            "cost_drag": 0.000645342375,
            "cvar5_improvement": 0.040030859537977484,
            "drawdown_improvement": 0.20632906727344003,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "c2209a5b405bac286c73284d9fc581c16a425d179dcff71abdeaa8710254fe0f",
            "cost_drag": 0.000418780025,
            "cvar5_improvement": 0.04102519709855609,
            "drawdown_improvement": 0.20951202260771828,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "c2faa48b20285145059a9507df7fb128457be7916c87597372a667e3535514da",
            "cost_drag": 0.00047794782500000006,
            "cvar5_improvement": 0.040921141863735244,
            "drawdown_improvement": 0.2088893934271014,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "c3b3386f66538a319e0467b3a0b591520efa06cc1ee02fe2bfe05a4bfdea1895",
            "cost_drag": 0.00040458034999999994,
            "cvar5_improvement": 0.04174867639741066,
            "drawdown_improvement": 0.21081599905676354,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "c4d5b093333d5f925ed448b6d6d3817b80258f4b6df0402ff62d7ff6e5de0d90",
            "cost_drag": 0.00035713165,
            "cvar5_improvement": 0.04180576944002141,
            "drawdown_improvement": 0.21116196166614357,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "c4ecea34d33f8e9ff517190ef1639a0078c204de4df752764eafe9f1f8ec39cd",
            "cost_drag": 0.00039582515,
            "cvar5_improvement": 0.04159796598824142,
            "drawdown_improvement": 0.21035826816614356,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c54abf54583ce691431dbb42312227a0d225834bfc9a325757243da770f414aa",
            "cost_drag": 0.00041667145000000007,
            "cvar5_improvement": 0.0413496418227808,
            "drawdown_improvement": 0.20987247179096277,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c8d96d02fef2052aa1b5b4f37d053341689597b833962dea2b09040dda9cd81d",
            "cost_drag": 0.000510720375,
            "cvar5_improvement": 0.0410936166348222,
            "drawdown_improvement": 0.20961459027402735,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "cc26b8dbf9aabc5a954cdba7f15445f6906c516ab4ca332c472c7970122b880a",
            "cost_drag": 0.00035784805,
            "cvar5_improvement": 0.041785797451920924,
            "drawdown_improvement": 0.21105811830715823,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "cd308639566094e1248179f35cda2c75f4b3f108d88965087b313c6e2c18ad0c",
            "cost_drag": 0.00056814705,
            "cvar5_improvement": 0.040677785558859716,
            "drawdown_improvement": 0.20872556521754135,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cd978ede184d59c0797473a5f7cf0173d393d3398a9aa841a8dc97ea58a53cb5",
            "cost_drag": 0.00034826445,
            "cvar5_improvement": 0.04147652276249916,
            "drawdown_improvement": 0.21050015313643194,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "ce25616a08a3a713d3baa8fbe9c681a24d2d0ae6253ec78d562b4a0e52cefb9e",
            "cost_drag": 0.000418780025,
            "cvar5_improvement": 0.04102519709855609,
            "drawdown_improvement": 0.20951202260771828,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "cf9cde26dba3c73a5567f30c5d5a03c684d25c008ef9fb3ad24b61ff1e53e962",
            "cost_drag": 0.000297975675,
            "cvar5_improvement": 0.04193416594666435,
            "drawdown_improvement": 0.21126102052378545,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "d00659d885e156983f250b8d53e6c117947d0afc46d076fdcf1e024dacb4145d",
            "cost_drag": 0.00021436815000000002,
            "cvar5_improvement": 0.042084550538379194,
            "drawdown_improvement": 0.21187070808237712,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "d1a7f1bab43c17c56cf770ea8414ee06ce61b60f10d4a20f8959f14d48824bba",
            "cost_drag": 0.0007450084250000001,
            "cvar5_improvement": 0.03990949007412996,
            "drawdown_improvement": 0.20610728554669036,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "d352ec1510356ccb70944864be43f48121546077644fccd6d3b4ebe46472fbb3",
            "cost_drag": 0.00086089055,
            "cvar5_improvement": 0.03931942346201828,
            "drawdown_improvement": 0.20447147311742409,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "d576233a8b8830e3532da4d368e8f230e4de74243f423ae4693135f0662ad5a3",
            "cost_drag": 0.000635421075,
            "cvar5_improvement": 0.04057396944558554,
            "drawdown_improvement": 0.20863954008915292,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "dcbdfc7b407f6dae2709dbf78aaa01157de1752506623e224a3c54d9dcbd44cc",
            "cost_drag": 0.000498589075,
            "cvar5_improvement": 0.04089094879573377,
            "drawdown_improvement": 0.20886881879908614,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "ddcf08c0eb422a69906267785f04df8ddf6ada327f9f7dbfc623ef071dcdcb28",
            "cost_drag": 0.00035713165,
            "cvar5_improvement": 0.04180576944002141,
            "drawdown_improvement": 0.21116196166614357,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "de68c4ccc59411bff11772363170338b6761dbd0f39bd7fc8c794de5cfd5259e",
            "cost_drag": 0.000279348475,
            "cvar5_improvement": 0.04193416594666435,
            "drawdown_improvement": 0.21126102052378545,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e22018ff8811c7b7c47fb6ee98be4a18af5dd760741f1521c9a5e5246a5dcead",
            "cost_drag": 0.000510360725,
            "cvar5_improvement": 0.04111612858347596,
            "drawdown_improvement": 0.2096959241763279,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "e731b06b6b8a57905247003db6fe52b6b03c796f946f86db5ff1d9a78d7bc936",
            "cost_drag": 0.00029143770000000004,
            "cvar5_improvement": 0.041952433607955135,
            "drawdown_improvement": 0.21157211801361667,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e77bf2a8d1f196188c97d7cfc708d2f57c96d69e508253e83cf169f5c4d6c81c",
            "cost_drag": 0.000563107375,
            "cvar5_improvement": 0.04068182712420269,
            "drawdown_improvement": 0.20803220327402733,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "e9e04869e6239071f9dd8cce64bab3d8eeb7ca305ff95b34978dc8aedbbd705c",
            "cost_drag": 0.000438811375,
            "cvar5_improvement": 0.04102519709855609,
            "drawdown_improvement": 0.20951202260771828,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "eadf7cacdbca92462104fbb663d7c89152d0846f8079544838f53c144e80b383",
            "cost_drag": 0.000510360725,
            "cvar5_improvement": 0.04111612858347596,
            "drawdown_improvement": 0.2096959241763279,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "ebab91384cb73c29a059a5f61ee4cb1db962fd86e95224f09308839b0f4f4a7d",
            "cost_drag": 0.00035716052500000005,
            "cvar5_improvement": 0.04182832440233635,
            "drawdown_improvement": 0.21116162523985732,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "ec4085c7e24702acce52ee2a5997e551a4978c5f8741df94c163d6422bc23f7c",
            "cost_drag": 0.0005151738749999999,
            "cvar5_improvement": 0.04089094879573377,
            "drawdown_improvement": 0.20886881879908614,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "ec7cbbe41821b4534745fc5abe749c3fa818c012a03773917d564783155e3c9b",
            "cost_drag": 0.000634428925,
            "cvar5_improvement": 0.04005865152932797,
            "drawdown_improvement": 0.20635303334254138,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "ed0dd236355b7a8d9f42cd954e2aba0cca2d130aeb2e511c8145e52b3b5c9229",
            "cost_drag": 0.0007809151750000001,
            "cvar5_improvement": 0.04014325201517409,
            "drawdown_improvement": 0.20762269849242407,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f08a6c33adf0cb5410922ccb5eb4e34f92024956a5c0332e80e647bee7cb2a01",
            "cost_drag": 0.000438811375,
            "cvar5_improvement": 0.04102519709855609,
            "drawdown_improvement": 0.20951202260771828,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "f20359ca6d891690d890c115b86a566a971340c2017016139abfe828870ecff8",
            "cost_drag": 0.00082708125,
            "cvar5_improvement": 0.03935929913524621,
            "drawdown_improvement": 0.20450293562982713,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f38dda51d631dae80a08a0027a6f82f3f06d6328bca9e8c207522a8316d0a562",
            "cost_drag": 0.00063490625,
            "cvar5_improvement": 0.040601242425103296,
            "drawdown_improvement": 0.2086437572439485,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f3b1956a637c63c935fb3bb6eb3e713d0e7881edf280d7cd43341778f5d206ec",
            "cost_drag": 0.0007011881250000001,
            "cvar5_improvement": 0.03998210839557155,
            "drawdown_improvement": 0.20627122536894854,
            "exposure_ratio": 0.10515873015873016,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.0,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f403091f4d2bc6ab744045f21d94ccd7cdb6bb69adac3cb07ebeb46eaf36f684",
            "cost_drag": 0.00056814705,
            "cvar5_improvement": 0.040677785558859716,
            "drawdown_improvement": 0.20872556521754135,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.75,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "f985f1617e9bb77ea62699fce58cc6011e56a4fb40c9d3565f854b8ed05f5e4c",
            "cost_drag": 0.00034826445,
            "cvar5_improvement": 0.04147652276249916,
            "drawdown_improvement": 0.21050015313643194,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 1.0,
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "fc714e5166dab9d576b2cca6b8263c9609f4ba786bf9b50769aa593b8e6c47d5",
            "cost_drag": 0.000244835375,
            "cvar5_improvement": 0.042019592655475675,
            "drawdown_improvement": 0.21169797311045763,
            "exposure_ratio": 0.07539682539682539,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 5,
                "fixed_initial_pct": 0.5,
                "initial_model": "fixed",
                "max_grid_per_day": 1,
                "step_pct": 0.02,
                "unit_pct": 0.1
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "fd3352c6d16146fc47234c6239e5393864ac990b33c70cd0570d7c36192d1a49",
            "cost_drag": 0.000748031125,
            "cvar5_improvement": 0.040155987215295785,
            "drawdown_improvement": 0.20765255167652916,
            "exposure_ratio": 0.09325396825396826,
            "family": "trend_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          }
        ],
        "excess_attribution": null,
        "execution_cost_config": null,
        "screened_axes": {
          "grid_only": [
            [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ]
          ],
          "trend_only": [
            [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ]
          ]
        },
        "selected_scores": {},
        "strategy_spec": null,
        "window_id": "wf_000"
      }
    ],
    "strategy_spec": {
      "config": {
        "cost": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "grid": {
          "atr_stop_multiple": 3.0,
          "cooldown_sessions": 5,
          "fixed_initial_pct": 0.5,
          "initial_model": "fixed",
          "max_grid_per_day": 1,
          "step_pct": 0.02,
          "unit_pct": 0.1
        },
        "trend": {
          "add_n": 0.5,
          "amount_ratio_min": null,
          "max_units": 4,
          "require_macd_bullish": true,
          "risk_per_unit": 0.005,
          "stop_n": 2.0
        }
      },
      "policy_id": "full_adaptive",
      "strategy_id": "full_adaptive",
      "version": "1"
    }
  }
}

## 事件归因

[
  {
    "window_id": "wf_000",
    "trade_points": [],
    "by_reason": {},
    "invested_sessions": 0,
    "cash_sessions": 0,
    "rejected_order_count": 0
  }
]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

Missing or invalid experiment evidence; no research action can be inferred.
