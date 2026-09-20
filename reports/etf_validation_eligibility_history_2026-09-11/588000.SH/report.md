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
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1833904678000001,
            0.07479618139999991,
            0.06209792040000011,
            0.12067003850000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9f8d66390e22e841dbc879446df494747fe0e69404b4bb4c04c136d2b5046189",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1862118319000001,
            0.08336673379999993,
            0.06697323290000012,
            0.09449145400000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1883226858000001,
            0.09179274349999994,
            0.06810950320000016,
            0.06894704340000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "da28e066148553678760b45c21a54f0f815cb41838c646423fedd4acd0c69f0d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19073174360000014,
            0.10050806129999998,
            0.06907899000000017,
            0.04376060860000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "90d6ff7ed79e50c4dddaaed58adbfdc177b6bf9b378de9d013c1d4240154e606",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19278393700000016,
            0.10900580739999999,
            0.06987735610000019,
            0.019350650800000258
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "43950e3f259617cc483404f6d6415d25f5b84e7eb334812843c5e9177958cce0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1669024843000001,
            0.07560733619999987,
            0.057844464900000156,
            0.10615939340000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8bce2fd4652d535226e8dc035f7242084edc778cd386a1bba082c130a02ff6fd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18025597770000013,
            0.08730054589999992,
            0.05997451500000018,
            0.08018942350000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18717839580000015,
            0.09362049279999998,
            0.06537318420000021,
            0.05495219380000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "77bd9770c8d5ec308e8b7fd0fadfa8fbf6cead744a6e15323ae2a4260b80ad42",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18961458970000017,
            0.1022094895,
            0.07227086280000022,
            0.030260385600000272
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0664477e5295e0bc1c74559f720de476589a1201e90ca5c2c2645acf217e5a1e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1916028524000002,
            0.11095275580000002,
            0.08104781780000025,
            0.007134942300000308
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5132cd3db68e157dd3153cb3ae9792dee9a4b1c862130fd622636843c2b36730",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16327358480000012,
            0.07339905869999987,
            0.057816382000000194,
            0.09169501350000023
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0a8f9b6084c1d444d5b9dacff3681205d0b72ae817079b8f300cb12517cbc6fc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16590992220000014,
            0.0819349700999999,
            0.05893155130000022,
            0.06619366830000026
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16267164020000016,
            0.0937942169999999,
            0.06094081570000025,
            0.04236325600000029
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "77c0310211df78935d4962e65b3e258ba298c8d9fd368ecda7590f2158d215b1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18134376830000018,
            0.10731754059999996,
            0.06379052700000026,
            0.019824825000000323
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2b1ca3a349c41d3e74f6ea219a4c0fe30f94bd0c8d69053d8a263b0a0abd2acc",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.18349633510000019,
            0.11605262529999999,
            0.06463744900000029,
            -0.0012066404999996894
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c952cae7bd45116005f8eb31266d51ce6c128f513baffac095de4b6cb97384f6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15562646690000012,
            0.0740983532999999,
            0.06758084970000021,
            0.0819276886000003
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4deabe0573cbeae491a145f8e4d20f916f5c910661a4c80d8fc5167f3190b561",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15852104060000016,
            0.08175671429999988,
            0.05968498680000026,
            0.05463876670000031
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1608086721000002,
            0.0903313584999999,
            0.06079079050000028,
            0.03270840270000033
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2542c5a0c6a70a2692a3038a43bcea945893d0495b2c1713e03b0f9afdf6620a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1558303992000002,
            0.10350340959999993,
            0.06294971890000033,
            0.011463441900000343
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c1f8d05174940de5abab81e70dbabad9d91d52b696bb409bdd2ab6d799a45da8",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.1598406285000002,
            0.11215760739999994,
            0.06389229170000034,
            -0.002801438799999667
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e43174b66cae18536744c3921b38ea3b06411d2aafef1ba96738db80f17ae80b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1825672291000001,
            0.0762886951999999,
            0.06337704560000007,
            0.12816325600000011
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3986694fa6674e967c35c294ac4055fbd72f2cc3fda3b61e52db297456a13d8f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1852876235000001,
            0.08483091509999992,
            0.0644114638000001,
            0.10177548500000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18742885780000013,
            0.09332821519999993,
            0.06529250030000011,
            0.07601329870000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "222df6d8f13727d94d27e59090092450a9d1437210027cc7ba1e9ed6e9669731",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18984025340000013,
            0.10198458699999996,
            0.06618595450000013,
            0.050676264600000215
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1955c130371fbd273746ee973f8ff228037a1edbf3c4f5811acb4c15e0cf6dda",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19192709790000015,
            0.11054469579999998,
            0.06701166560000016,
            0.02604428620000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bb96bcaf6239a8f480b471f3bd6f4f2edad305f90a5fe68ac611f0a7034ec535",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1660345642000001,
            0.07849599179999985,
            0.058620823900000084,
            0.12035575160000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "259b394408833371c897a4a9317235e9c836670ca8171b17b53da30eb4a6a0c9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17639665190000012,
            0.0859529688999999,
            0.06373473010000011,
            0.09426377380000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18300771240000016,
            0.09619207209999994,
            0.07327524700000013,
            0.0686136800000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "183a91bd23a755b7e87e0ab603de83e23b8219e506dd76397e078a1cf902c167",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18733557570000017,
            0.10488417619999997,
            0.07416111620000015,
            0.04353176050000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "260012ec18d23eb314b1bd71c33087541eee3662ea1fdbc37c0ba619bcac2dbb",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18943420620000018,
            0.1135396746,
            0.07498008540000017,
            0.019081642400000265
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c848623e0be20099dc48e20d39b8cb65688053a8a496ec4aa885783422556572",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16216978720000014,
            0.07590252469999985,
            0.058046579800000095,
            0.11276883830000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "08bb1f5360f9a1daa71255445b28f2b85a25bbf9afeafe227384fc93068725f1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16467348920000013,
            0.08436048749999987,
            0.05900688550000012,
            0.08673569930000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16129516520000015,
            0.09799463859999986,
            0.061844176600000134,
            0.06141741800000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0c65d2ef761411d63b3e7d181c2d998d0df2dcf703efd602be2fad87e1da59dc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17526569030000017,
            0.10525481829999994,
            0.06905255570000017,
            0.03644918900000027
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3c50ec6e404a0402a3f98be24cad12d2a6bb4f1a9ce1917679cbf45896f6efd0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1774326460000002,
            0.11377850679999996,
            0.06982729230000019,
            0.012073497900000285
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "13140adfdb638ee59aee50db7ac7a68bf94b4aeb3cd69660a93f3b3954d57fc0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15562646690000012,
            0.07102213699999985,
            0.05747878310000009,
            0.1051404272000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6d151393122f9975d3a3fbbdfde74da7330ecc39667716a01b5d15571ac979f7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15703201600000016,
            0.08503347039999987,
            0.05962416730000013,
            0.07926654520000023
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15927370100000018,
            0.09360913289999989,
            0.06051326110000015,
            0.054007809200000256
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "80899914e7291fc258eeddf6520efbf7fe1b0287b99fc96d0a62841279df7425",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1540226834000002,
            0.10906388189999987,
            0.06390166680000017,
            0.02932508770000028
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4769bcc53bde368b7006c19ea230e03bc28764d38036f94954f64cec059dcb85",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1580422875000002,
            0.11771640599999988,
            0.06449757260000019,
            0.008529886200000308
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f6d7509f3f5c1634fea76f4dd53e98841aa76151e5c756d7dfd55b79d67dc8f8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18348580350000007,
            0.07658630989999987,
            0.060123585500000076,
            0.13000171310000008
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cff9859d4a5f2814140612668f4daacf34db624bbfeb4347eae64ec9f633685b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1862061979000001,
            0.0851051951999999,
            0.0612117438000001,
            0.10353832450000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1884697737000001,
            0.09362578589999992,
            0.06214701960000012,
            0.07775958920000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9b285843c53cb0e98fbb611366f677a98327b135bad0b9ffb777bf5f8f2ea648",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19078185880000012,
            0.10228215769999993,
            0.06298957200000013,
            0.052413541600000196
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3b113e92d617b95e71b3d485144a8bf07623fdd5476c359cde7bf0af5e60b9ba",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19275641040000013,
            0.11084258379999995,
            0.06390450580000015,
            0.027670077100000218
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "eec8e6bf15537c408060e82aa9252bc11c299b5ededb53194b719629a246267c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1705550348000001,
            0.07944181909999987,
            0.0532713822000001,
            0.12391423310000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1fb848b69f408dc3ba8d7bd85ebc85edda0535045ed94aad7ab28c6599beaf4d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1841870675000001,
            0.0880077512999999,
            0.05841531060000013,
            0.09772890520000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18664815990000014,
            0.09656519009999992,
            0.06643561220000015,
            0.07201682300000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4734c020226fa7443033daa844967e4699044f02fbfcdd5f6005cd5984d5532d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18891608670000015,
            0.10531294449999992,
            0.06728556860000016,
            0.046888769400000196
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e062b42fc995eb71bc33d23b0a1a7171cd43966949db71673235e334018a8b9f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19104674610000016,
            0.11391316589999995,
            0.06818730550000018,
            0.022308776800000235
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0380f680c2ed4cb0751113688c497ae2ca73f1769aab860b0851287c65fe1fac",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1622213890000001,
            0.07726617469999986,
            0.04992850170000013,
            0.11788745780000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a7e68e5035096e8601e3fc70bed10c2f2d51007849d3f7759c8601c0d59a51de",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16474346430000011,
            0.08580676209999988,
            0.05078780160000015,
            0.09184436450000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16789527780000013,
            0.09949488319999991,
            0.053803675800000166,
            0.06629586480000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9f72db2d6091f70ef6f2c28a733136150b7d98312604e238d2900953d4d65ab4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18713517530000018,
            0.10813849079999993,
            0.0611291637000002,
            0.04124574870000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1b7e2c5e7b5958dc5a4167102c649e3905f2a20047667578f26da46fe53ae2b2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18923946680000017,
            0.11695966809999994,
            0.06199704000000022,
            0.016795218700000253
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4fc55be6dc74c3f50156a7e114ea4978acdb95ed567f20d6bbf0c18ba03b48c2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15562646690000012,
            0.07102213699999985,
            0.05053084200000013,
            0.11182496300000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c828166e74ca3a3a5edaf08d9a9cc9318061f12eaf8a971288d9fe9aa94f0002",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15706319850000014,
            0.08695427999999986,
            0.04874945120000017,
            0.08594998760000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.15926393730000016,
            0.09549356739999988,
            0.049725638600000184,
            0.0605851316000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d6dfb2a62a2c81350ef9e449a06dc69ac134a1e3741a97bf3776f014a02b7bde",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16283478720000016,
            0.11116853559999992,
            0.053198703800000205,
            0.03568003490000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4e1a984b1c95dcc573ae3ac61d76713bc6516583278750a0006153bff7d9df6a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16669838650000016,
            0.11989479759999994,
            0.053969697500000226,
            0.013123858500000252
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "589b9e99b2cc99c9bf11c7d143c4316f35fae491362d7df2a95b2a38cea057ef",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18177757040000006,
            0.07832377859999988,
            0.061977130900000066,
            0.1317348092000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "446dc1803e4c7a85e81fa0757a3f673cc8f49dc153680f00a73418f382fe40fc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1844783080000001,
            0.0868479848999999,
            0.06304319730000009,
            0.10527533490000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1867072315000001,
            0.09540093089999992,
            0.0640987068000001,
            0.07938786870000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "61a86f69f97281212bca1d76dff4959aded7bc8ae179fd65e9a35b51766efe9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18909895660000012,
            0.10406262369999994,
            0.06491431670000013,
            0.05404857910000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "266908ce86922ef9e2da585eb6b06dc860b8cc72327a6b50d62c098f123fd428",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19102952020000014,
            0.11263872249999995,
            0.06572692450000014,
            0.02932992500000023
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "db3ce2343cab6d1650bea124ea4ff260409091058133b2b9bd6fe8a6fd2ff9a4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17063405850000007,
            0.08299408109999987,
            0.06808963740000007,
            0.12724431740000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "deba15173d77c901d382e9f5272229ae1cba6daa2726b4bb6ce9634e86a14da7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17779477080000008,
            0.09159768959999989,
            0.06908543100000009,
            0.10091561080000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1830183939000001,
            0.10017080109999991,
            0.07012785620000012,
            0.07523283060000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a43d42200543c8fee6ecea4bd84917ea1bcf540d535e043f6a521a06832f55f1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18531130660000014,
            0.10895623179999994,
            0.07113450160000014,
            0.049963492500000206
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e2cff1ab7f737919236ab95a7fedc68c273418b1b4245a5f6ac6c54916c93f70",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18740965150000014,
            0.11759412949999995,
            0.07207032430000015,
            0.02539009890000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e15d48069bf09f9bb10971f06b1a917c4b07e6c1a074d0d1388e0185650d24cd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16233942440000007,
            0.08262790899999986,
            0.06329530440000009,
            0.12286146180000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5a17506ad28bbda515701fea8e5e9ce9e4f8bde66bd49b5febd4aad94e2a76b2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16486149970000008,
            0.09122184539999988,
            0.0642582869000001,
            0.09674112920000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1680133132000001,
            0.1049686364999999,
            0.07630426510000013,
            0.0710337161000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b54f48b12b36135d832f2f0ecb43d61a4941bcf07a971027a9accc6831847aea",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17951131580000015,
            0.12252444669999996,
            0.07826204710000016,
            0.02138707720000027
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d726ac15f78e72d7171a62d66dcf57ed06bd6d2e3d2d36113bbde161c0666e27",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1557845143000001,
            0.07102213699999985,
            0.05638693310000009,
            0.11846757110000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3b8400990f65f2f5c0b5d93d3ebecb37df16eedcd649695660efe4d79ce973b7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1571614136000001,
            0.09419982929999987,
            0.06664050520000012,
            0.0924015658000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1594209844000001,
            0.10279347559999988,
            0.06768034820000013,
            0.06687376360000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a8b1e9c488ff9b024597f84b549df68bca23d0664c4df78a57248136fcff3c3c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16287768100000014,
            0.11858046279999993,
            0.08330987280000016,
            0.041824219900000265
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45451ae22fd54f5fcc4a8c83f4e0e0fcc2755c40142cb91352153ea353ce96a3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16686209370000013,
            0.12737675639999993,
            0.08443682630000017,
            0.017524200800000278
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e5da6823593cc26f966c1b236eb2179524508f51ac24bb8ecc1ae9cf0512a2d2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18365508720000007,
            0.07589916419999988,
            0.06269095750000006,
            0.1313998145000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cbf63fff76abf8f86447fff223cc640736f864eaa9919c9dbc89d1c0d125adb",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18638020950000006,
            0.08440374019999991,
            0.06381070050000008,
            0.10497038810000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1887394604000001,
            0.09292907709999992,
            0.0648785178000001,
            0.07909235190000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "961cfe76def7b11fe2351283e3ebd181a0c11106d5a65042f1ccade8bdfaaa3b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19114450650000012,
            0.10150757229999993,
            0.06560120310000012,
            0.0537856740000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "17c7279512899f3a91bea351e1b53d236bffc52f4a909e0f96befb2127ba1987",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1931318289000001,
            0.11012408159999995,
            0.06647448960000014,
            0.028987288000000222
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c2723042d21e0f63b5e375cfd0cc6b239d7d1319ce461a03c6a1a2ef7049a724",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17540191780000006,
            0.07793428149999988,
            0.06960489570000007,
            0.1266429644000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c732a62eeaa84162fc5a884fcc09486a2b9ee5c9039b8d9a0d76f72351d048d6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1844933383000001,
            0.0864648084999999,
            0.0706480449000001,
            0.10028915800000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1869548213000001,
            0.09497709049999992,
            0.07169511310000011,
            0.07451462360000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5a60d04000e8a42a7ef2a4dfd58e04047fee6e55af55b1d752e8f78c30a7fad1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1894046662000001,
            0.10361656889999994,
            0.07272070950000013,
            0.0493160625000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5d600521d8ec100f51d0d336c6543e9781171444d584310acb517b6041a05a64",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19135144050000014,
            0.11220702719999995,
            0.07361774280000015,
            0.02469564870000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "21afa2e296937da975f586f16b52eb519be169e613d16ecd15cd50de513cdbcd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16942520120000007,
            0.07988767349999988,
            0.06465378870000008,
            0.12191971820000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17206587260000009,
            0.0884569386999999,
            0.0656571247000001,
            0.09569760080000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1753379575000001,
            0.09708872099999992,
            0.07856850210000013,
            0.07005242590000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d6b5f0adf9731cb102e277bd3fb3c7f60594548d2231a497b32c94673cd0b667",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18750054560000012,
            0.10572266549999994,
            0.07961140880000014,
            0.044920535000000206
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "757cb14275a89bc4c9e5a29a7520d973e34a22ebd3401c538b8a321442b8fd5b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18969677610000013,
            0.11436761689999997,
            0.08061636670000016,
            0.020416323600000258
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b6449162a482e7a08f99c096b1423ca1e879ffa87022184dd0cff292e8213cf6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16515171730000008,
            0.07549876139999984,
            0.05818151110000009,
            0.11710934520000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4948e389709741f3f9c362d58fe2624e794f41e6d5ef2b7968b00962535749d6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.16662459750000008,
            0.0905126859999999,
            0.0684699667000001,
            0.09106780720000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1690467285000001,
            0.09918300649999992,
            0.06951970370000013,
            0.0655099389000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2b8cce8c37110946254601751fec91e8b1a3052ace950c33d369bc1269f4e54c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17271572780000014,
            0.10781695099999994,
            0.08641290250000015,
            0.04057563970000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d8d5c98b26ff14e3212cd6294dddc02b69e28e1725828e71a010ae9c00e64f87",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17468383480000013,
            0.11651756459999996,
            0.08754023810000017,
            0.016164060100000266
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9b0ed793b8789210beddbfe561da3142bf989c157269bda13aa9d2e732098470",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18228072760000005,
            0.07738003829999988,
            0.05974725420000007,
            0.13208201910000011
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "529b14ba63795fde28f27d0ddc49d26555b3ea64714f8b42d3e97419429806f3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18500584990000007,
            0.0859052442999999,
            0.06070808630000009,
            0.10563958880000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1873251620000001,
            0.09443048119999992,
            0.06174447710000011,
            0.07973401230000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3cc7b53f43c230cbc0bbe5e407576b80e5c3c8401dd8cf82ff397d5c07f70d48",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1896918960000001,
            0.10300887639999995,
            0.062467262400000126,
            0.05434940310000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b313af62bdd5d8e3e6b7fef4e167294ef0b09dc0cc58c92f6913a9a1385bd71c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19169187730000012,
            0.11162538569999997,
            0.06329132140000016,
            0.029623478800000214
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c043be32382e64bdbba090ec810f1ccf50a09fe8648fc8a3408bbd2ab9ac73c6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17882019220000006,
            0.08088559659999989,
            0.06320265160000008,
            0.12791881150000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45fc5ff3ccb51fbcbd9cfe0f8880bfce401d63eea9bdb37ca7711e56fdfe51f1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18143461840000008,
            0.0894108025999999,
            0.0642244240000001,
            0.10159649620000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1838674870000001,
            0.09800990769999993,
            0.06522775710000012,
            0.07583301900000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "7c2b3fc2dbedd2b079ebdeca8887a83fb588fd2a1d89ed4f35c2ff52d779728b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18612372490000012,
            0.10664918609999993,
            0.06606241610000015,
            0.050560829000000196
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2893c794a262dfeeb1d55eb234d4bbc50613e92208bd8509d365e79e48e8e243",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18814286820000012,
            0.11526037439999995,
            0.06693490280000017,
            0.02592030920000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "7826433e193e4ac82cc351ff0995a6b514018d7da192d993bd018af86f9827f0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17527361490000007,
            0.08434455069999988,
            0.060276163400000096,
            0.12384420140000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8cbfd1cd2d9316edcb8d2b295fa7dd39a4888c1b6c1a9fd7cd02af0f71389581",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17797298300000008,
            0.0929344458999999,
            0.06123934590000012,
            0.09760200440000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18029155550000012,
            0.10162700029999992,
            0.06873843510000013,
            0.0718569664000002
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "77548bc87ab8ee39a946a4bb2c139e0addd6da3a1b8a8eb663acbcf366d946f3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18260721290000012,
            0.11028157479999995,
            0.06964866410000016,
            0.04670738730000021
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "23c50db9ddba5ebfe44269566b665b6b65bbdf61def5dfe671d025e6d5a010b1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18467753280000013,
            0.11894695619999995,
            0.07048709600000018,
            0.022168180400000237
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8a8f91fb3f844ba6dfc5dfcf5bdbde75f84903dd70fbf2739c509a094fde215b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17040415300000009,
            0.07549876139999984,
            0.052360995200000114,
            0.11971603300000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "812af4d1fa0b091fb7419ff0da1d71ce91fe65a0a3224bbcf41431dcebd0b08d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1743970515000001,
            0.09645876219999991,
            0.06253137200000013,
            0.09358257210000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1768185597000001,
            0.10514951269999992,
            0.06354105550000015,
            0.06800478640000021
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cbe67dbd8ea3ade52ec52ba1d9625b2a6f87d9e55ccafd9a64fd847a889053cc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17916869990000012,
            0.11386505929999993,
            0.07315251690000017,
            0.04293732560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "461c154a7e2353f2283c499ac85775b992b924de41d0fec46d9f06b5172f7142",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18112852370000015,
            0.12263739599999995,
            0.07406661880000019,
            0.018535480900000262
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f06c82a4eeb01c2ca1b3775d507f3fdf523eac9e7bd4f72ae421cb474e7f3e8d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18228072760000005,
            0.07738003829999988,
            0.05801845060000006,
            0.1341291423000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fde5f8993452adb198b2aebe545089a0c13eb1c9000759d5e47c483b81d0ca3b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18500584990000007,
            0.0859052442999999,
            0.05893725500000008,
            0.10756059520000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1873251620000001,
            0.09443048119999992,
            0.0599238559000001,
            0.08157898220000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9b49243fc490f86a5308087d28dcd0c8743ca5e9e7f2f9f5645275731e7a26ee",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1896918960000001,
            0.10300887639999995,
            0.06069637900000012,
            0.056229290600000176
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "46f84d8aed1026e2d80d880921222dcafc41aee81ce7ffb4371076fddea389b7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19169187730000012,
            0.11162538569999997,
            0.06141731030000014,
            0.031435373600000205
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a742864c7a1208b39c7fae284c174b8dd0af4d1de90c2fad405dab24d97015e9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17882019220000006,
            0.08088559659999989,
            0.059649961000000064,
            0.13191056760000008
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fd673b08ae5457fc2c262ed05bda3c5d6934808f9935cbade4c0d6172f79ad0f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18143461840000008,
            0.0894108025999999,
            0.06056880570000008,
            0.10540511610000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1838674870000001,
            0.09800990769999993,
            0.0615402111000001,
            0.07953659970000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0be1879f481ad47d63cb1e9e3839ecd1e8b8a47f13b42f9c203ebdd2d8b36c92",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18612372490000012,
            0.10664918609999993,
            0.06237011800000013,
            0.05419763370000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cd527804e36527d86170dc60b7b5297223c9325a141bce31c0379910247fe5f4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18814286820000012,
            0.11526037439999995,
            0.06309784930000015,
            0.029460820800000204
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "02951609451a1a3666f9e27a5c317b82fb9d83367c6c4907f4a9d530a074a829",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17527361490000007,
            0.08434455069999988,
            0.06128151170000007,
            0.1296910508000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "18fc14e280c2cfd24eb7a861ce0ea745639459e640b134c7b93c1eee85bd3f1a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17797298300000008,
            0.0929344458999999,
            0.06225429990000009,
            0.10330238510000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18029155550000012,
            0.10162700029999992,
            0.06322544560000011,
            0.07745061990000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "64e3052ef8fa0319a7c2533e42c13b53422f82ad86eb68d7701d663c462fd129",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18260721290000012,
            0.11028157479999995,
            0.06404025700000013,
            0.05212487950000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8088cc365f89e6679290e380387e1324139d60bed3aa5ee409fd03ee528e9a99",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18467753280000013,
            0.11894695619999995,
            0.06482036640000015,
            0.027432634900000225
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8bcb1085f091f1ae946199c14e23c1ba1e975e65f06096e4aa24df9a5387bf01",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17040415300000009,
            0.07549876139999984,
            0.053683033600000075,
            0.12747247610000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2ea28b5fd16155856db1a6aaf045c7c6a38ceefbc42b4e51cb92f1e5a3291080",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1743970515000001,
            0.09645876219999991,
            0.0638708551000001,
            0.10117382680000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1768185597000001,
            0.10514951269999992,
            0.06489053860000012,
            0.07536474010000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8e9ceaba7690e6d3faceede615245b6d1a7554518ab91ac3b377c4df97f4c0a3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17916869990000012,
            0.11386505929999993,
            0.06572549150000014,
            0.05010574820000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fb7cf5a396194be308efbdd959d12d7a0c48b1193d5a2caac5caa3adc4c65a92",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18112852370000015,
            0.12263739599999995,
            0.06649060540000015,
            0.025511630200000218
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "318930da62df7a9a4b135893117f29e6080cdee95f09a82d0197d3413840c2a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18656170210000006,
            0.07679179549999988,
            0.05801845060000006,
            0.13512204270000008
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "824e648c83a8f7c5d611f1044280116ee112dafff48f1898aadbcdd7cc416908",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18932247640000008,
            0.0852350714999999,
            0.05893725500000008,
            0.10855998710000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1916834387000001,
            0.09385235769999992,
            0.0599238559000001,
            0.08261937140000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "71cb3c31412438e23d4b9bff35ae94c701cf15c333086d98008bcf43077b98f0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1940501727000001,
            0.10243287389999994,
            0.06069637900000012,
            0.057254452100000186
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "65e02eee14f0acb0a825dacbe164cfa06365c84cde2b215e2174efcc30cf82c1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19598317410000013,
            0.11101521179999996,
            0.06141731030000014,
            0.032342449300000214
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a10c8020a0773c04afed2636a58bedf090d4fbf98ff1d3b60925e0ea4e097776",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18747746800000006,
            0.0796655974999999,
            0.059649961000000064,
            0.1339059159000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c3738ae7a721e173bf76984f66c2f685bc435209fd4dab537ffc550a62a23d7b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19013354440000008,
            0.0881931437999999,
            0.06056880570000008,
            0.10739539760000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1925944046000001,
            0.09675138859999993,
            0.0615402111000001,
            0.08147465790000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "19d00bceaeaee45b90711aedc56891ccd0aec187c04e0c1df0557f9894ba521c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1948922927000001,
            0.10544374869999995,
            0.06237011800000013,
            0.056026733400000195
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "56cb7fb31d203469a3f1c85e5c30ae6f448173b6cf02c6203dc31a8c63b6dd5c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19688776850000012,
            0.11403536559999997,
            0.06309784930000015,
            0.031252058700000224
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "aa322358aee7ceed5d28526185f0ecc94c244a13c6344d41457546a6a739dfb8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1883308595000001,
            0.0826306180999999,
            0.06128151170000007,
            0.13270980890000011
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "25d46927d3049e38377b2aab3cdec3957e2a5adf6b1a27fe97889bc46891180e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19104821030000008,
            0.09115121609999992,
            0.06225429990000009,
            0.10617140410000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1934364246000001,
            0.09983028379999993,
            0.06322544560000011,
            0.08035182460000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "daa598de199db4f2abe5d43ad5487cc9e98f006ac89533dc04afd523606d5df7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1957794058000001,
            0.10846390249999996,
            0.06404025700000013,
            0.054882519900000176
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0752a8b6c7a878a88b448142929f6a9f3be2c1ed8c4201bee06a7d6faa25ea99",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19789137590000014,
            0.11719158279999997,
            0.06482036640000015,
            0.030186218900000228
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a6454c26597b01d0276b684c62019f613b394f2ff7eaaf890673936236e2a537",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17399874890000008,
            0.08047062319999987,
            0.053683033600000075,
            0.13149368210000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bd323451f9997167020ef8b4d4563d57e755f853e5a756382be5fefaf5d43de9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19184725510000009,
            0.09413434009999992,
            0.0638708551000001,
            0.10500201460000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1943567316000001,
            0.10281300779999994,
            0.06489053860000012,
            0.07915554860000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6b5bf2db39c7a5312bb922ccbb7f79eb56adc7b97c17b591d33d8da2a6250bc1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19671719410000013,
            0.11146596169999996,
            0.06572549150000014,
            0.05379192930000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "edcf6df73115739f59495a635a2f6e95889a072a90f65715f3683de0279b6036",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19871866810000013,
            0.12022101559999998,
            0.06649060540000015,
            0.02904208020000021
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "89ad7adcecda2efcf8cbd6a6401ed3e6ed96b851083accd850f6a0c518aa15b3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18464869160000005,
            0.07746394409999988,
            0.05811042300000006,
            0.13512204270000008
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fbe5f873390f4fa9623ed2084060dd9b386dcb41caa2b71b95f0f2129cf57a56",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18737381390000007,
            0.0859564824999999,
            0.05902922740000007,
            0.10855998710000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1897347762000001,
            0.09455969599999992,
            0.060015828300000094,
            0.08261937140000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8d2fb7a3cdb517396e8b9acf88ea220280c39c0d59402311d007504ddef79d5c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1921015102000001,
            0.10309191909999994,
            0.060788351400000114,
            0.057254452100000186
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e2c8bb705339dcc5463a443085ff18111efcc79131fc23f37b0689f00224e812",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19403451160000013,
            0.11174818879999995,
            0.06150928270000013,
            0.032342449300000214
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e63647ca2002739cec51718c1fc3233e1fa1a415c34c193d001a7c1cd59f7a79",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18351579500000006,
            0.08089808499999988,
            0.05983390580000005,
            0.1339059159000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8d4112ab3315d7d1ddc27a4d870f5e4b35afd1d22a3825b4b4fafb3f73ad8f3b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18617187140000008,
            0.0894685999999999,
            0.06075275050000008,
            0.10739539760000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1885970796000001,
            0.09805108349999991,
            0.061739151400000095,
            0.08147465790000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1421bd391e699bf7e3db84dd519ed0f9abd810d6436050bef6fa5aac1639def6",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1908949677000001,
            0.10673577089999994,
            0.06255606220000011,
            0.056026733400000195
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d6db03d900f41c0c72fa21236bdcea5a570191d0749630206087c435ff3a8898",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19285479150000012,
            0.11539204059999997,
            0.06328379350000013,
            0.031252058700000224
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5a99c08a7ed7f5f806cf0a005980f33c6f44c53c9af3ff9ec74ea537e9ac3156",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18235617600000006,
            0.08441020249999989,
            0.06155742890000006,
            0.13270980890000011
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a01c832be39f3c46cd5b376ca93ac9936e7882bf59f762681abd6bb6e5fae186",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18503787480000009,
            0.0930117805999999,
            0.06253021710000008,
            0.10617140410000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1873904371000001,
            0.10169003529999993,
            0.0635033622000001,
            0.08035182460000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b66db6d06efa7d1e620ced97604377222cfc7a690e9e12414f834e4ae2dde28d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18968710020000012,
            0.11040788579999994,
            0.06432017300000012,
            0.054882519900000176
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "290d66f51c3334521564ebbf587b2c8f96dd3feca2c2d788144f482ee2e0e5c3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19179907030000012,
            0.11916556209999996,
            0.06510028240000014,
            0.030186218900000228
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fa155e38f105769756379f1664a8105153b41ea206f3fa703f1dea61f6e2fc4a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17399874890000008,
            0.07755848289999986,
            0.05405092320000005,
            0.13149368210000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "26296eafe932dd4ff9512c67b6adb54a054d9512ee6fe088c015bb6b30ae16ef",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1837882571000001,
            0.0965032680999999,
            0.06424074410000008,
            0.10500201460000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1862514155000001,
            0.10523301589999992,
            0.06522668530000009,
            0.07915554860000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "20c920b02310daf4b859f8b813f29af3b4d257da9ba48b2d64b95f4328dde275",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18857622600000012,
            0.11402884299999994,
            0.06604854210000011,
            0.05379192930000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4b29dc52dae93fa89372642c660f99eeca7df753f4baaa1174e66a58541fe27d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19057770000000016,
            0.12278858389999997,
            0.06686449320000014,
            0.02904208020000021
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ca6aa7709729328d94aa19e8129a8ec3f86ce1d32039e064fb623fbb8f1ac58e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18464869160000005,
            0.07524446869999987,
            0.06035509700000005,
            0.13512204270000008
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4e015ead6169a716f5f5e9c559d43e096fc921f96389ef1a18f5749d64d333b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18737381390000007,
            0.0837440049999999,
            0.06134757200000007,
            0.10855998710000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1897347762000001,
            0.09226934189999991,
            0.0622745834000001,
            0.08261937140000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dcaf4f81927c472859f6300f1b7ac9cec525bb1864c151d3d4070612ae8e5df4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1921015102000001,
            0.10080166499999993,
            0.06309204050000011,
            0.057254452100000186
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "eb49287bc547c6e506f3aadb7eda6b7daada828a03319fcee65cf5fdd3c3fd6a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19403451160000013,
            0.10934899499999995,
            0.06380782580000013,
            0.032342449300000214
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8001ce7a61e6bbc527399ec1395b7cefc4fdc1a06d706c582a8a9beb5ebe3b02",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18351579500000006,
            0.07644410869999986,
            0.06437193190000005,
            0.1339059159000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "268cf23cf0dce23398307940260e0cecf8d96d17daf5edc865eaaa770f936901",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18617187140000008,
            0.08494364499999987,
            0.06537940240000008,
            0.10739539760000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1885970796000001,
            0.0934689818999999,
            0.06633094660000009,
            0.08147465790000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1543bfd39152b539b9476475cdaa1d411c13d91f416cbff3ba8211a1b4f61a45",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1908949677000001,
            0.10208299059999992,
            0.06723078000000011,
            0.056026733400000195
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "11a928c621365eb7f902d7635a77ce6899022428a591ed6644c79dd42f8bf607",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19285479150000012,
            0.11063032059999994,
            0.06799319360000014,
            0.031252058700000224
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d6db90ed5261d686d5775a7fe7c23cbce9b135bff6dee12a51a8f348722dcbcd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18235617600000006,
            0.07769544179999985,
            0.06838346110000006,
            0.13270980890000011
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a71457d47e5c1fa6cd81dc8bc2295e36bc60f4d0e12fac791b33187fe27c62b3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18503787480000009,
            0.08619497809999987,
            0.06942127010000007,
            0.10617140410000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1873904371000001,
            0.09472021499999989,
            0.0704663861000001,
            0.08035182460000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "04c0ca5fbcf902e5b9afe76b36a90ca3ad2104030989324ad9d294df660cfa89",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18968710020000012,
            0.10333612369999992,
            0.07128704320000012,
            0.054882519900000176
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "64ca51cf505764cc7dcd808efa152085d9373da22f33c6e151902050d8ddf2c4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19179907030000012,
            0.11191164619999994,
            0.07207778960000014,
            0.030186218900000228
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "26b18365a7e4237cc73053f1f6c404fdd94246aa4e16544ee34c6b1bfe516a85",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17399874890000008,
            0.07889508179999985,
            0.05909714190000005,
            0.13149368210000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6c762a7a83d430eb4aae46bc3b939d9320278f039a0d1733b209ae55c6e64f75",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1837882571000001,
            0.08739461809999986,
            0.07344779480000008,
            0.10500201460000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1862514155000001,
            0.09594484749999987,
            0.07444387300000009,
            0.07915554860000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a6346dd7e1804c75cf8dd0eb15ee8b4c4797741b2f0c1cb674ef99891c3fa9e9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18857622600000012,
            0.10456075619999991,
            0.07538293470000011,
            0.05379192930000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d3c336ea2c30970cb838c9559f28ef5afffee91fabd06beb0c1839e49256766d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19057770000000016,
            0.11319297179999993,
            0.07617908680000013,
            0.02904208020000021
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a38ca9017ee7323d6ca2fa38e717ced6f522427e0f6ce2d771d4ec8eeb087dcf",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18587828370000004,
            0.07524446869999987,
            0.060956916400000054,
            0.1353095555000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8f4a1199d5a21df79951d1f560023a1fa23122d88707a3f69ce4c077993f95e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18849270990000005,
            0.0837440049999999,
            0.061870415100000076,
            0.10871450140000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19093834590000008,
            0.09226934189999991,
            0.0628415608000001,
            0.08282743380000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4db6c5d5762841c37dc4de1bc30a10cd0e27c01bfab964bf6c8365bcc5313082",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1931983838000001,
            0.10080166499999993,
            0.06362877940000011,
            0.05730073560000018
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ffcbf75f862ff7b602b47b861df9fc8a853843804e38aef1f90875d90a3822e7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19524198130000012,
            0.10934899499999995,
            0.06438879900000014,
            0.03249276240000021
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b3b9838498a218b2c75976ab65e15e6c8076bb286d1ea658b3fbbf8b7e944b0b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18581428310000006,
            0.07644410869999986,
            0.06547729290000005,
            0.1343054923000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9aab49f04c34ce9b0218247ceb595fe069b32faa5bdcebea8b02ec4761a1c832",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18847035950000007,
            0.08494364499999987,
            0.06654309350000008,
            0.10781552360000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19091599550000007,
            0.0934689818999999,
            0.06751383920000009,
            0.08185924000000017
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6a052b308f6ab167426ab2a7e99b79c37ceafef5132f04f03ebf5c5e3dece9d5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19317603340000009,
            0.10208299059999992,
            0.06834318640000012,
            0.056364584500000176
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "081a8609b5d2788de7dedead3776df8fed29be1556ee3ac5015b21181e073d7f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1952612811000001,
            0.11063032059999994,
            0.06911939580000014,
            0.031610434200000204
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "064c3f82e8595dcab77015ea88579873dec1e16e29d5a987e51204197ce9414d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18575028250000006,
            0.07769544179999985,
            0.07009594720000005,
            0.13326790080000012
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c3a2b9e6812b3f6ca0f3a545088ae9cbf0150071f297f84c671e4ca96a08d7fb",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18840635890000007,
            0.08619497809999987,
            0.07115644210000008,
            0.10672539480000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19085199490000007,
            0.09472021499999989,
            0.0721861176000001,
            0.08085037680000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cad56c70b53c6f45b92078a0eb03bb554e4515d6c3eca9cc7cee91426f915e9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1931536830000001,
            0.10333612369999992,
            0.07301516480000012,
            0.05548205630000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9e3707d9ca4dd26f414d299f19d60bc43cbdbf2bf2b6da6219c626e1973457ae",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19523893070000012,
            0.11191164619999994,
            0.07383400280000013,
            0.03069626330000022
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4e816f70069fec6fbef680ba41095962ee77e9ff072ca18af5f553cdcfd997e2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17857244750000004,
            0.07889508179999985,
            0.05909714190000005,
            0.1322323201000001
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e4fc4425fef1519fb6942a195045717cd0d7d9196af4d4bbd9def08121347069",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.18834235830000007,
            0.08739461809999986,
            0.07574145410000008,
            0.10584226660000014
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19078799430000007,
            0.09594484749999987,
            0.0767599182000001,
            0.07991362570000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "40da851baa2cf49bf7ef0a57c4209c8c76198f9c0a177a116a76f059fcdf01bf",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1930896824000001,
            0.10456075619999991,
            0.07774086730000011,
            0.05449404270000019
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b846a0a7e4c43066dab6457e533f7c7c435e82ee1372dd35cc746ba1dbbf7394",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.19517493010000012,
            0.11319297179999993,
            0.07855970530000014,
            0.02972912450000023
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "21689e24dc18ba601d9f14348099e07264d8de1eaf474dc390d782e652382168",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5287352a22ba877f8449d3c07f2c4e42cae86b2e142fc23e5322283e2bda91b8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ad84e5361d1b7f8a10535519b1342c8f50295bb009b4d311a1e2cd4fe8f768c1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "34c7658bc1bd300e0bad621d7909f6ddff945fe70ebc2bac87801f94c07953f8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "72584a40092f0707d80fa28f36e4b2219156f0bca376ac1717ab21cc31f30c4d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17746133340000014,
            0.11364992039999994,
            0.07726948870000014,
            0.04587858560000024
          ],
          "positive_window_share": 1.0
        }
      ],
      "trend": [
        {
          "config_hash": "1fec94aa0bead42b20075940b637e819472c020dce8613fa5a3c7aa21734fd06",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.049521290799999826,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "adbca544282724c5a7a2958f71250737af4685caeb95879a42bc97e6fba41fa0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.049521290799999826,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e731b06b6b8a57905247003db6fe52b6b03c796f946f86db5ff1d9a78d7bc936",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.049521290799999826,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "46f7afbe4f52f52cf8832a43b79598af956b8e0d3541d6425464a97964d756c0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.049521290799999826,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0efce7b04e5e193de8d96ae22d700309b50d9ec1b26b72a73c3a1a9f6769501d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.04914103139999983,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1b03d2707a07fe802f1760263c82b3d4b8342a455e2139542829ce33055346c3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.04914103139999983,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cc26b8dbf9aabc5a954cdba7f15445f6906c516ab4ca332c472c7970122b880a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.04914103139999983,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "de68c4ccc59411bff11772363170338b6761dbd0f39bd7fc8c794de5cfd5259e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04914103139999983,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b3ab56d68fdcaada002d2614a264764fe445837a7212d9cef39fd0934e9a098b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.04796437319999983,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c3b3386f66538a319e0467b3a0b591520efa06cc1ee02fe2bfe05a4bfdea1895",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.04796437319999983,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8bf92734c3d2ba8e6c3dd7f599c5b43e34620f9479e5c24f9b34ccbe045b4947",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.04796437319999983,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cf9cde26dba3c73a5567f30c5d5a03c684d25c008ef9fb3ad24b61ff1e53e962",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04796437319999983,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0c441452555d21094fcf63b740acffe7a9176260632649cedf006f78d5c922dc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "23d1e52eeccaf4bc0cb8853853c2be63a69dd7762b18d7289741c7e7f37b98f9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a5c471fd8ef46b803b80689400b2fc0c30d0ff6a0d4e6a27deb9881f27514916",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "37ce18ea991b11a33fd546c75664f8cafed609d4a7311f44011f1ac689f5ecbe",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4ecea34d33f8e9ff517190ef1639a0078c204de4df752764eafe9f1f8ec39cd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4d5b093333d5f925ed448b6d6d3817b80258f4b6df0402ff62d7ff6e5de0d90",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ddcf08c0eb422a69906267785f04df8ddf6ada327f9f7dbfc623ef071dcdcb28",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "548bde01f4ae3b39c455be93505eda30b321c79668d9f8acde7f81aac0feefc0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b1ce106b9791d9b2313e33ad5d36230eb1a10a96118d83ef7b6350514a957bd9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bd61e6ffa991468a6062bf4047742d76be80658e74f9212ae8482ed6d90027cf",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9fcab2c463797c9b28ee01148cc476784bb2473b84bf8f2ae68c546f3cb9c946",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "61609ced85a7068bb6b227a8778db35ac30701765ed24a2d414765a7965417f9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1a8b7c2b566250e4974b9accd1eb288e0b1c3b9ece047603707261bce302dd08",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "07a6da34a90c5c24e8cfdef1b9c07e2ff039d51fce0b917d7a4ba2527844daa4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "441990e611d4bfed0a753adb7d990a66af9681ccb20bb032d058f3e3bf793c67",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.178875277,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d00659d885e156983f250b8d53e6c117947d0afc46d076fdcf1e024dacb4145d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04919439279999983,
            0.0589571504,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bc6f099a3c49e384ab643559ec0ec44d65d442396a1dc177bb4c7181ac52ae54",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "492d3075b7505d752fc4569124324cf50ec4e1e12399bff92d72a757be0abcea",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ebab91384cb73c29a059a5f61ee4cb1db962fd86e95224f09308839b0f4f4a7d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4266ee5cc6a9ac907f421389ef9cf425c951ac9475f81729c7ed50f0150b1b7d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.047207011399999825,
            0.06034030380000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6a23f24486bb79be48113d97b10bbba4ac19f7ddef0e43e81ec8d1dc67ff9092",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "be75d5c8e26860196c89f31b797698e558e2c7568cb1a802d2a09507366516ca",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9a5ffaf7d90c7cd06362d27f96a11d349d1b8f1dd81f180cf81cb93f13789ea5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1775866641,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fc714e5166dab9d576b2cca6b8263c9609f4ba786bf9b50769aa593b8e6c47d5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.047052044899999826,
            0.059056504800000006,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1a1d82ea59c99bfe7ac50c54c249f33eecaf9e8d07e4abf76bdd391e3652f99b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.050173005599999834,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "915b629158bae600eedb793e1b7461db1bca2642934e70e963373d51bb0eec9d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.050173005599999834,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "505ad729a6207cc8be7b2d3fe972a46ba111f58eeaa7b3b530a2cfa2e1d371ac",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.050173005599999834,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "59b014959d6ca4769d4753c652daf0ccb38e962e5c3d4d3ea42fec5bd2a2a57a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.050173005599999834,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e77bf2a8d1f196188c97d7cfc708d2f57c96d69e508253e83cf169f5c4d6c81c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04950890079999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "add329e8e27ecebe1d584cb1f14ba572d35710aea60476ca8ccbc31431672993",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04950890079999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c8d96d02fef2052aa1b5b4f37d053341689597b833962dea2b09040dda9cd81d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04950890079999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "64e8b768141ab52605621addcd48eb9cc31b1ffcd58858b53f7d3015b5511af3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04950890079999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04753172229999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9a8031973c8ec766ac9566a91c4f700fd8d2a7712f8f4e3641c67b8135e77bca",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04753172229999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4a09e9f42c304e0c0f941aa4fb00cfc45f473ebaa326e8c08008a0a2a91e8d4c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04753172229999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c54abf54583ce691431dbb42312227a0d225834bfc9a325757243da770f414aa",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04753172229999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "387050649e85b36d7c6e999764671f946e30e8f6587f959815efda2fee8967c9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6d0b27b35b089a17eb96ff6e8962cf760fda88c3a3d4da56f20518c119a22fea",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "7e25e305550d53d8dd69c7eeb54c0b6e13240426682cf97ea575590254e15a8f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "09c907ccffba9c79389da45ffbc273ef56ff552a01e37bb47bf4b4f538584933",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "330e9079a8741ac5ed4d998877d62b08834a5251908efa8b14fa9b09f101662a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "eadf7cacdbca92462104fbb663d7c89152d0846f8079544838f53c144e80b383",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2c75c42046ef3a6d0f0febae245bcf1a0d429394847dcdc593062e759c731b73",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bdfeea35c79ba78c3054cc430396a6f0454ffcb4c0eefca49e78830b92de5ccc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3d16b6890afaf109d0c4451863565fe56cb71dd1454039aa22d95648f62fe42d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e22018ff8811c7b7c47fb6ee98be4a18af5dd760741f1521c9a5e5246a5dcead",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4c5dbff3038888fbc8ba660d551023c7213bc3c92e7d698161e4831ddb927e16",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f985f1617e9bb77ea62699fce58cc6011e56a4fb40c9d3565f854b8ed05f5e4c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1a0ba2f00044f420ffb20d85ffd3b630915c4f0587b631a9e61e8fc68b943b2c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ae2f1ec1405653fbbf289a5f020fe4b9ab1365648959be0631bcd1db772eadad",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "50aeca7dbe7571cfa0dd145f2032d40a70a44efb66da2450d2ac21fc20d8ac95",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1805990902,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "02ed4b871a3ac2dc98111f5f7dba62b21c61af723cae0b25f7d3fa568b6642e4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04951920959999983,
            0.0645238556,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "13e36312d75235095a99fb4673caba20941b36b205e0f88c729e7bc1900c423e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9755e4a2985929b24476e74975b3281dcf102f99fc184339e833c99c9365e566",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a2606ff0dd53e64bdaed4879ebef55587c576527665e09aaceec8068c023f1fa",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0a073f60f2b4e958cf7bb14f680436f06eb26b748c281a78271005a1011caa57",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04567203009999983,
            0.06684307000000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "42105ee5fa31f194122fe24f85377d35b1afea27da9bbed7fe4efa1b04df9b81",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b4a19d9ee57a1ed883fc45f2d940417ba33b9bcd8854935c3d9ed02a29df5c44",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a05a3729a4575c24923de713a0ba59f30f2cfd21472905bb9a557e2e85fe5392",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17829103570000002,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cd978ede184d59c0797473a5f7cf0173d393d3398a9aa841a8dc97ea58a53cb5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04567203009999983,
            0.06475586700000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c1144d55f4b001966183229609c62f71533195749e340dc147b58b34996d34b1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.050824720399999836,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b7aa686834fba404e57ce646e62ea5ae9ce6b33df36f634aa733cced8430673f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.050824720399999836,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b7c893047999c7d6c75f8da734604fb8e463ffc56e36cbccd00fa3732bfff73c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.050824720399999836,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c2faa48b20285145059a9507df7fb128457be7916c87597372a667e3535514da",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.050824720399999836,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "376261879bb3a98cb9d9f885ebc4606248424ee5623184ed545ba758deb3d361",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.049939108999999836,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1c9aaeaf1c01aaa86bd6f9b2a9def8c7f55b76815b48c037012df2db186a7ad9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.049939108999999836,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "53ae75468006b31323bf7c8217cd72f20b714d1c350e56945d1b7cb891a67f57",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.049939108999999836,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dcbdfc7b407f6dae2709dbf78aaa01157de1752506623e224a3c54d9dcbd44cc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.049939108999999836,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d1a7f1bab43c17c56cf770ea8414ee06ce61b60f10d4a20f8959f14d48824bba",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.047428250299999836,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bfc4d87ac49a11a984a17ee8bc2a235c4905e425284c08722bc83a3787c3da0f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.047428250299999836,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "90e95eca032bfe50e881261b29e392fa034ba82c6ca75e51bb44c3dd72c9275c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.047428250299999836,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ec4085c7e24702acce52ee2a5997e551a4978c5f8741df94c163d6422bc23f7c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.047428250299999836,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "696913cb4f51a33bf3935b51da3b38e1dcd6d1a97557ef171529553b4d7bfbf7",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f403091f4d2bc6ab744045f21d94ccd7cdb6bb69adac3cb07ebeb46eaf36f684",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6fc8e2eef32a9bbeedf4d1623087ba3891701d13c78d22843cdf57a1c9bb12be",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c2209a5b405bac286c73284d9fc581c16a425d179dcff71abdeaa8710254fe0f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "52db97a65a1d4ad3cfa5799f59629bcab32d4cb9e84027e5ec07afc0fc759dea",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "520cb3507a916dc9d9f2fa51dacd4e7c3511bbf9eee1fcdf03da237bb9f07e11",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "74615fd57e7c943c143fd077540a3361517eb745a26477811b844f682456d219",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e9e04869e6239071f9dd8cce64bab3d8eeb7ca305ff95b34978dc8aedbbd705c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "13a36acfc6269b30b569bb601b5e16abcb027c50365afdcb43ae693eeb166958",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d576233a8b8830e3532da4d368e8f230e4de74243f423ae4693135f0662ad5a3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "44cb7392c928f53c521015a2cd2d0d65ae8766b2261ffc6f5861bc3196ad086f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b5ae512c057c4cca149fc22aa5ab060d43221cfcfb62184e6b988b8670e045e0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ec7cbbe41821b4534745fc5abe749c3fa818c012a03773917d564783155e3c9b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "cd308639566094e1248179f35cda2c75f4b3f108d88965087b313c6e2c18ad0c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45fc69735e2a6498f6345128fd7d46a7e5ad7bc5aa540c5fe68355a5a078e402",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1823229034,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ce25616a08a3a713d3baa8fbe9c681a24d2d0ae6253ec78d562b4a0e52cefb9e",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.049835383799999834,
            0.07009056079999999,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f3b1956a637c63c935fb3bb6eb3e713d0e7881edf280d7cd43341778f5d206ec",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4ef5f2e60b0a12f9c3dfdfc50ff212dda872ca3811ba7eb1a418cd635500ee86",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f38dda51d631dae80a08a0027a6f82f3f06d6328bca9e8c207522a8316d0a562",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5bf8412a3fe2565df7fe2ecd3cf0bf8ef854466aaaa317215f6937328ff3ab18",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04468817419999983,
            0.07299036430000003,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1b8a1433cd25010fb5c550b3665e973d63467cfe7baa46e828f42e0e3914c235",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "6c62868387b90bf0e5d50a007eb97dff2c5f410ac777bb74e949f24ca4545cd4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bf18cc0ff8f31c28dd27bd53bea9a4b8740f08d9cba11a3a14cacc6d1091b9ef",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.17918056840000002,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f08a6c33adf0cb5410922ccb5eb4e34f92024956a5c0332e80e647bee7cb2a01",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04468817419999983,
            0.07049275930000001,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3de7c13e774d534c952c8462bc02d4706ba6c2da63098dcc633d9891959119c9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05146963319999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "161dbc35e812294ca418d3a491ac83452d7dae568d1e5be10421ee4e19fdab27",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05146963319999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1e3c5a3a25ba0ff260f82888076b19bd3e2497627e62d17545f54d5382b673a9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05146963319999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b9bc2fd53b37952d0fa31d7ee6c7abb2df29fc0c936f761b0b4d5de89d3b3c65",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.05146963319999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1424ccb6f148503ef949aaec1c140dfeedf287a16154036803144b75c5de03c2",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.05042573419999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a164ba23ba9524e034fe07bfe24aea3b27db569bc592dca70655d980b21fcdd3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.05042573419999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "fd3352c6d16146fc47234c6239e5393864ac990b33c70cd0570d7c36192d1a49",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.05042573419999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "7ec3d94889c6256057b589f9a9349e6f11c29591facbfc6dd184ffe7dc58d8de",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.05042573419999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d352ec1510356ccb70944864be43f48121546077644fccd6d3b4ebe46472fbb3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04758203759999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "42881131aa958b37001b7427d92d5475137405fe28d79f77e10b24316f77ab3c",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04758203759999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ed0dd236355b7a8d9f42cd954e2aba0cca2d130aeb2e511c8145e52b3b5c9229",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04758203759999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a7e3098ae1d238b85a68bf710352484a836546f125d4abdecafda4bd5b6ce8e1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04758203759999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9b43cfb13d4e03c1d855e2b81d3146f84cdd7f6155194208cff59649e4fafedd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "275334c7d66460505e7c71e7f1bc8e971d6b44f3af26a6b8dba212d744d4d00a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0dee04873a3ddf671052ea481c0d968718285776ddcfc900e5af011213ad542b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "8538b7affe3bb97a027406cdbf0ee82edbf2a14cf9b0164e0f3b16e518dcce49",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "05063fd72167d3a3a2da97e7c8c63023ebe7fe845967932f2a3a68b2d9023574",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "707d5fac1ebe3f88df9b8bca06082ec5f029dbaaa67f900f17bdbb99418ae959",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "12643fc27869a63bcca87e3e38c0aae6f7825f6728622759920ecebf182931d1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2d4e420f979f519ab7261ed8c86ca8308618af6e63b56f5476e2d2fce0fd8a14",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "76c2fdbf72a6ee26af1f5ea026eca75afdfcee1086f79c917047a7c7ab3c01ed",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "bcaf1067a4e98787b432db5b6681a208b9eea62150fe336c1090df3b4f678dfc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "b54d6a3fa555012188e6f740379a78f0dd22cd68864cae4eb9e915ce67e8baaa",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "17c9c940096d43a773c4905d1982dc3a9c901fae82b8de14cfb27f6844ce84c0",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0165967a82c576ce3dbbcae3a03db3d0b9766a1b6ba0de5459235753d980e642",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "091fbd2cc185b592a8e7b80f30e3e73fb8f3034ef10dcb197ae208d1892901d3",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "17dbff0a23e5d013e2d4b110485364f1d520f1dd5b5b79ea9cec2328e6048ff9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1840450377,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a7d1bc64be18eec70f804ccb675f4de3265988e1f7041b8dac11721a645fbccd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.05015155799999984,
            0.075657266,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "81f56cf56a5de341c5d98c82cf7d5803225386e334d2d1d583526e9c4ea5e855",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "512697187c6fe64646e9ff21e491e8e481880ebae3fbd0e5138c76ee036ec1d5",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "673a28cda6786a76d77f41b3d518b2dc00aa5c1482c95959af2c5318831043bd",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "64e6f60cccaa85fd39f8b1fa74bc32547aeab8eb0fc0ea90356ebdca81ab94da",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04405746429999984,
            0.07866042230000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f20359ca6d891690d890c115b86a566a971340c2017016139abfe828870ecff8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "891e4aac1326376aff627803dcff3b5d016adb3f7c1d241c033375b50f4f5659",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "4bfb9404f1e53fa2d8ba993a154c73bc83122dfdb210429965cadb5122d6cb5d",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1802875935,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "443522543e3e8dd041a7ffeee4af344efccc3ec16395b525bc91265308a4d846",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.1773014638,
            0.04405746429999984,
            0.07607533830000002,
            0.2204015784
          ],
          "positive_window_share": 1.0
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
        "588000.SH"
      ]
    },
    "experiment_hash": "c1a92863f0ebad10d8d8ec11dc004d7ee269fbd3e72adbbe72027d37ee7857b2",
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
            "cost_drag": 0.00097916575,
            "cvar5_improvement": 0.027597925206653124,
            "drawdown_improvement": 0.2303029072777557,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6393681528928683,
            "sortino_excess": 1.1133350597401412,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001347216975,
            "cvar5_improvement": 0.027019086514880726,
            "drawdown_improvement": 0.22462945730489942,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1836743528474779,
            "sortino_excess": 0.8443479584455048,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001356401025,
            "cvar5_improvement": 0.02055207322215074,
            "drawdown_improvement": 0.18705480043329503,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.466269970975217,
            "sortino_excess": 1.2233008195632147,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008407047,
            "cvar5_improvement": 0.027340782221681514,
            "drawdown_improvement": 0.2298015373808785,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6078586474556364,
            "sortino_excess": 1.2775316637405347,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0034785057,
            "cvar5_improvement": 0.01906085744596442,
            "drawdown_improvement": 0.17730671994665986,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6608743158027227,
            "sortino_excess": 1.404722802119702,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001704211775,
            "cvar5_improvement": 0.018484315760596216,
            "drawdown_improvement": 0.17450114507571202,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5195957161192145,
            "sortino_excess": 1.2954796529205401,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00149473985,
            "cvar5_improvement": 0.01756488809280487,
            "drawdown_improvement": 0.1721949035882368,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44483185660963165,
            "sortino_excess": 1.1989238551572292,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017702074,
            "cvar5_improvement": 0.025032357806055245,
            "drawdown_improvement": 0.21145484245432022,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3580988549244474,
            "sortino_excess": 1.0199749357445071,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022728198,
            "cvar5_improvement": 0.02475895396765316,
            "drawdown_improvement": 0.20884828292819915,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.38548846971762907,
            "sortino_excess": 1.1988153489435691,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014191820999999998,
            "cvar5_improvement": 0.02011907681771495,
            "drawdown_improvement": 0.18638753979747086,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4514013527365383,
            "sortino_excess": 1.2189882592011552,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00255628445,
            "cvar5_improvement": 0.021570347008860558,
            "drawdown_improvement": 0.18976572874142866,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5707870507474899,
            "sortino_excess": 1.1461631847461324,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001319840825,
            "cvar5_improvement": 0.020734225110627953,
            "drawdown_improvement": 0.18822590244213558,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5001478083765677,
            "sortino_excess": 1.2687455951633448,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013170882,
            "cvar5_improvement": 0.024346467691234643,
            "drawdown_improvement": 0.21078939425976842,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3822571098806372,
            "sortino_excess": 1.1560245622447605,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00125743145,
            "cvar5_improvement": 0.023617655672476423,
            "drawdown_improvement": 0.20558470766233541,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6247211537004231,
            "sortino_excess": 1.2321906466786867,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001522756675,
            "cvar5_improvement": 0.01745017742574529,
            "drawdown_improvement": 0.17143733887231613,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4274036636283498,
            "sortino_excess": 1.1748508631984014,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001487644225,
            "cvar5_improvement": 0.026022415640425907,
            "drawdown_improvement": 0.21857707520692218,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14208883548268014,
            "sortino_excess": 0.8900946433477261,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001371964225,
            "cvar5_improvement": 0.020067550576010437,
            "drawdown_improvement": 0.18608014782918306,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4484613040691803,
            "sortino_excess": 1.245440598812633,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00133222985,
            "cvar5_improvement": 0.019835801297565715,
            "drawdown_improvement": 0.1848735903249457,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4119476719710796,
            "sortino_excess": 1.1577526747824507,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014563692,
            "cvar5_improvement": 0.023466866252397568,
            "drawdown_improvement": 0.20413703178165424,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6378643894405311,
            "sortino_excess": 1.3195925327016305,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00184442575,
            "cvar5_improvement": 0.017094751370877407,
            "drawdown_improvement": 0.16978545489382363,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4227419354881409,
            "sortino_excess": 1.182967655384896,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002525190625,
            "cvar5_improvement": 0.02135843697772488,
            "drawdown_improvement": 0.18991864371084155,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6127473264499494,
            "sortino_excess": 1.2917740179669885,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017742790500000002,
            "cvar5_improvement": 0.023249753587097452,
            "drawdown_improvement": 0.20004822455779195,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2954102354628209,
            "sortino_excess": 1.0123449657062304,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011278193,
            "cvar5_improvement": 0.02558622264962243,
            "drawdown_improvement": 0.2172001197939603,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5836132612697618,
            "sortino_excess": 1.24685241033634,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0024509113999999998,
            "cvar5_improvement": 0.017753293595792422,
            "drawdown_improvement": 0.1715973799555064,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4551795847537352,
            "sortino_excess": 1.1414543173964942,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014626245750000001,
            "cvar5_improvement": 0.019955515676472243,
            "drawdown_improvement": 0.18544157147023577,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4437333682711578,
            "sortino_excess": 1.1856890054243032,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002401249375,
            "cvar5_improvement": 0.0191021819551971,
            "drawdown_improvement": 0.17787530271902757,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5678331367197036,
            "sortino_excess": 1.3152365894559732,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00112757955,
            "cvar5_improvement": 0.021357786109558585,
            "drawdown_improvement": 0.19633472273376384,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3375197308384056,
            "sortino_excess": 1.061470030313332,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0026216155500000003,
            "cvar5_improvement": 0.02351716100320638,
            "drawdown_improvement": 0.19908414123543788,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.45298036737795766,
            "sortino_excess": 1.1901559796275702,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001700839125,
            "cvar5_improvement": 0.025069374773372538,
            "drawdown_improvement": 0.2144686800581871,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.48627236925762685,
            "sortino_excess": 1.1937326541711142,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001287564625,
            "cvar5_improvement": 0.021499591428988746,
            "drawdown_improvement": 0.19704829383187292,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3687279497306321,
            "sortino_excess": 1.128368730040257,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001436212675,
            "cvar5_improvement": 0.02146079398436749,
            "drawdown_improvement": 0.19179441398951302,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6020667226693549,
            "sortino_excess": 1.3078900282764734,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001174752375,
            "cvar5_improvement": 0.027346982615852514,
            "drawdown_improvement": 0.2272556727356552,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4672493420800383,
            "sortino_excess": 1.0667864819761907,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022600829,
            "cvar5_improvement": 0.020121036482992606,
            "drawdown_improvement": 0.18503686965803076,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4429704084719843,
            "sortino_excess": 1.1316380808663151,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017528773250000001,
            "cvar5_improvement": 0.022915439330811086,
            "drawdown_improvement": 0.19982933111451504,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5757378986876334,
            "sortino_excess": 1.3606709856488712,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001809656425,
            "cvar5_improvement": 0.01869228288788317,
            "drawdown_improvement": 0.17590834354108614,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5645362076071847,
            "sortino_excess": 1.3709668852669812,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002988355375,
            "cvar5_improvement": 0.021815302749034246,
            "drawdown_improvement": 0.18747744467036587,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4850356151051933,
            "sortino_excess": 1.169730753131839,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019858166,
            "cvar5_improvement": 0.025326605378115687,
            "drawdown_improvement": 0.21434324088721976,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4868307085496042,
            "sortino_excess": 1.0545393439888402,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001178565175,
            "cvar5_improvement": 0.025228648523261694,
            "drawdown_improvement": 0.21574280511255098,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5572680238911667,
            "sortino_excess": 1.2619207182605585,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012385464,
            "cvar5_improvement": 0.022529822921743256,
            "drawdown_improvement": 0.20011464447546298,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4483608633702232,
            "sortino_excess": 1.2083525485420605,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0027141956249999996,
            "cvar5_improvement": 0.019286165816154256,
            "drawdown_improvement": 0.17656183052764635,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6005819985574885,
            "sortino_excess": 1.3084217168099384,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011040268,
            "cvar5_improvement": 0.025536028091008647,
            "drawdown_improvement": 0.21890082784376175,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.662298129788036,
            "sortino_excess": 1.1076212100032405,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001978574725,
            "cvar5_improvement": 0.017099411653004375,
            "drawdown_improvement": 0.1698212320917124,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4392542514519978,
            "sortino_excess": 1.1971143677597231,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001001018675,
            "cvar5_improvement": 0.024605825563966715,
            "drawdown_improvement": 0.2125484635325787,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3956419156767743,
            "sortino_excess": 1.138141848128936,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008549340999999999,
            "cvar5_improvement": 0.02718051451090158,
            "drawdown_improvement": 0.22741278161667475,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.32106158111620947,
            "sortino_excess": 0.9355021931443339,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001735734125,
            "cvar5_improvement": 0.01772419472866135,
            "drawdown_improvement": 0.17292890202519046,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.48173479298253635,
            "sortino_excess": 1.2753934711774284,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015928143500000002,
            "cvar5_improvement": 0.01860791180774888,
            "drawdown_improvement": 0.17545396497594865,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5254585962828269,
            "sortino_excess": 1.327247991006329,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0034586555499999997,
            "cvar5_improvement": 0.019699394955634567,
            "drawdown_improvement": 0.17816715065686006,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6498316421072807,
            "sortino_excess": 1.4367061157767655,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018927925250000002,
            "cvar5_improvement": 0.021771506155496265,
            "drawdown_improvement": 0.19057779392194057,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6436792002556743,
            "sortino_excess": 1.4300522130864635,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00115825135,
            "cvar5_improvement": 0.02348157164710595,
            "drawdown_improvement": 0.20460855417420454,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5994839483904082,
            "sortino_excess": 1.341079851186698,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001171473875,
            "cvar5_improvement": 0.025857346859662653,
            "drawdown_improvement": 0.21867311085071506,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6868853087249001,
            "sortino_excess": 1.160152858660056,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009306000499999999,
            "cvar5_improvement": 0.02630595871256899,
            "drawdown_improvement": 0.22476660907943274,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3302171144001321,
            "sortino_excess": 1.0479637182238066,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019227259250000001,
            "cvar5_improvement": 0.02486854276356746,
            "drawdown_improvement": 0.21272905262503095,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4453947761310815,
            "sortino_excess": 1.1377192162810617,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020729535,
            "cvar5_improvement": 0.017380762998464406,
            "drawdown_improvement": 0.1712432121219348,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4211547502059521,
            "sortino_excess": 1.1738970603137269,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015610193000000002,
            "cvar5_improvement": 0.02527152628874607,
            "drawdown_improvement": 0.21321094785086117,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5813942530628103,
            "sortino_excess": 1.1694094255367977,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0027436120249999998,
            "cvar5_improvement": 0.019617882680080526,
            "drawdown_improvement": 0.17809833254918833,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5753444640853864,
            "sortino_excess": 1.2254496244970965,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014722383,
            "cvar5_improvement": 0.019065260746194544,
            "drawdown_improvement": 0.1833274248715476,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3864283973075754,
            "sortino_excess": 1.1433561339735436,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001152431275,
            "cvar5_improvement": 0.022234665396910155,
            "drawdown_improvement": 0.1985517420966995,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.39843477855665715,
            "sortino_excess": 1.142402026828127,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001336760625,
            "cvar5_improvement": 0.021270239305209715,
            "drawdown_improvement": 0.19086463538905468,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5746094040057298,
            "sortino_excess": 1.3419802829234024,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015841856500000001,
            "cvar5_improvement": 0.023011052101620477,
            "drawdown_improvement": 0.19967894382047344,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5216450146038504,
            "sortino_excess": 1.3359628827191592,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002046428075,
            "cvar5_improvement": 0.027155156626660296,
            "drawdown_improvement": 0.22441173402729098,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3515093981826425,
            "sortino_excess": 1.064484223232816,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014503915,
            "cvar5_improvement": 0.02429515596998638,
            "drawdown_improvement": 0.21082535047219786,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4121973242028988,
            "sortino_excess": 1.1753532834734162,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002277128475,
            "cvar5_improvement": 0.01965965947795246,
            "drawdown_improvement": 0.17909792384537807,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7318223019161385,
            "sortino_excess": 1.490841808849606,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001207762475,
            "cvar5_improvement": 0.024897398984095227,
            "drawdown_improvement": 0.2140097217552946,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4919538390128064,
            "sortino_excess": 1.2798662977870578,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018835929250000001,
            "cvar5_improvement": 0.019326802325269236,
            "drawdown_improvement": 0.17897314225785094,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6532282363967454,
            "sortino_excess": 1.4321330854581507,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011248336249999999,
            "cvar5_improvement": 0.022355530070025578,
            "drawdown_improvement": 0.19934072015914944,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42467719204443327,
            "sortino_excess": 1.1778351719671345,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00157011105,
            "cvar5_improvement": 0.0166766010009261,
            "drawdown_improvement": 0.16998842241211076,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3996135365211223,
            "sortino_excess": 1.1463055683019268,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002055755475,
            "cvar5_improvement": 0.020846863774322582,
            "drawdown_improvement": 0.18918208170918085,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5226128567249537,
            "sortino_excess": 1.290317121374147,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0024648097000000003,
            "cvar5_improvement": 0.020166332794028824,
            "drawdown_improvement": 0.17978673241419488,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5317866681730341,
            "sortino_excess": 1.1505739806197337,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014060834249999998,
            "cvar5_improvement": 0.025519817177128274,
            "drawdown_improvement": 0.2147751884904516,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5165058205095809,
            "sortino_excess": 1.1143659765671683,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00162388345,
            "cvar5_improvement": 0.019232268507890726,
            "drawdown_improvement": 0.1782813711060608,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5924575945991987,
            "sortino_excess": 1.353098544602418,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0030212811250000006,
            "cvar5_improvement": 0.02313206549840975,
            "drawdown_improvement": 0.19982364632427912,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5819651303037823,
            "sortino_excess": 1.2879975937760488,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001289206825,
            "cvar5_improvement": 0.019005833582153672,
            "drawdown_improvement": 0.18303810873351045,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36965327946641807,
            "sortino_excess": 1.1007085587708088,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002492720675,
            "cvar5_improvement": 0.024736755540123695,
            "drawdown_improvement": 0.20652808268778408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3853433169303759,
            "sortino_excess": 1.1361399149619897,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00219441275,
            "cvar5_improvement": 0.019495270553197278,
            "drawdown_improvement": 0.17870031551788368,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4720914826331276,
            "sortino_excess": 1.1837337240647337,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008138499499999998,
            "cvar5_improvement": 0.027411042322240082,
            "drawdown_improvement": 0.22899106794843302,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.38944649483021854,
            "sortino_excess": 1.0065686320190304,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00128424555,
            "cvar5_improvement": 0.026218525408339806,
            "drawdown_improvement": 0.2203533519505625,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.008459005737184666,
            "sortino_excess": 0.8171274267107108,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002119088025,
            "cvar5_improvement": 0.026667536457234495,
            "drawdown_improvement": 0.22036638320458835,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3308245166065026,
            "sortino_excess": 1.1036363678108285,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011379054500000002,
            "cvar5_improvement": 0.02394148345567508,
            "drawdown_improvement": 0.21098707103427405,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.35606390828059575,
            "sortino_excess": 1.122087819288676,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00160719615,
            "cvar5_improvement": 0.023560656799196267,
            "drawdown_improvement": 0.2025697506249793,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5705027951297281,
            "sortino_excess": 1.3795903571534238,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016535872499999999,
            "cvar5_improvement": 0.017569303813956626,
            "drawdown_improvement": 0.17197059721394753,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.45511583462053495,
            "sortino_excess": 1.1872421586115964,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013015255000000002,
            "cvar5_improvement": 0.026671973536258685,
            "drawdown_improvement": 0.2249723085757427,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4299203608655128,
            "sortino_excess": 1.1963502615170523,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014554074750000002,
            "cvar5_improvement": 0.025289471843817673,
            "drawdown_improvement": 0.21411699510699875,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5081960680435645,
            "sortino_excess": 1.2156294435417543,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017678460000000002,
            "cvar5_improvement": 0.020738169383802782,
            "drawdown_improvement": 0.18602088141383352,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5141846287203851,
            "sortino_excess": 1.3254211196577592,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009221937,
            "cvar5_improvement": 0.02735773058363392,
            "drawdown_improvement": 0.23045328090742315,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6178141215739098,
            "sortino_excess": 1.0624513923529793,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001958382975,
            "cvar5_improvement": 0.018417697666453285,
            "drawdown_improvement": 0.17261985245754125,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5157001366347196,
            "sortino_excess": 1.3218847636051663,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001979248175,
            "cvar5_improvement": 0.023689946465305138,
            "drawdown_improvement": 0.2021808216593831,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4557477845503709,
            "sortino_excess": 1.053717796574693,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017857287500000001,
            "cvar5_improvement": 0.01949244952381791,
            "drawdown_improvement": 0.18321891151025058,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42389650178216165,
            "sortino_excess": 1.1819279604843071,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002607791825,
            "cvar5_improvement": 0.023036209690737865,
            "drawdown_improvement": 0.1961875158340464,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42440002336599597,
            "sortino_excess": 1.2061054349700657,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001545416525,
            "cvar5_improvement": 0.018265724022550583,
            "drawdown_improvement": 0.17361393232487626,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.47441584170036766,
            "sortino_excess": 1.2345459603073106,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001462116725,
            "cvar5_improvement": 0.021034787670366276,
            "drawdown_improvement": 0.18941648635788147,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5343429528249071,
            "sortino_excess": 1.287867573110966,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012824424500000001,
            "cvar5_improvement": 0.023359997348138487,
            "drawdown_improvement": 0.20317845632523115,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5490806139842794,
            "sortino_excess": 1.263520235667074,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016048113999999997,
            "cvar5_improvement": 0.016597894677908,
            "drawdown_improvement": 0.1695019161079896,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.39687924043045925,
            "sortino_excess": 1.0754502692872854,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014391084499999999,
            "cvar5_improvement": 0.02322001598667023,
            "drawdown_improvement": 0.20308620804219643,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.593853908933512,
            "sortino_excess": 1.3562695675628798,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00130389905,
            "cvar5_improvement": 0.019951881812141813,
            "drawdown_improvement": 0.18563099792331195,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.43185503534249525,
            "sortino_excess": 1.1853550804760646,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015657036250000002,
            "cvar5_improvement": 0.0212808295930999,
            "drawdown_improvement": 0.1905409837692746,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5964477966620083,
            "sortino_excess": 1.350612976437103,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012249329750000002,
            "cvar5_improvement": 0.023160005487205156,
            "drawdown_improvement": 0.2027148237969341,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5346998191904059,
            "sortino_excess": 1.2729141207187442,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001048676625,
            "cvar5_improvement": 0.025284247848978855,
            "drawdown_improvement": 0.21644370127978904,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5663089908997965,
            "sortino_excess": 1.2340197453918162,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00193104805,
            "cvar5_improvement": 0.02498036206640663,
            "drawdown_improvement": 0.20958310049383103,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3679449803593862,
            "sortino_excess": 0.9434210240662473,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00141162835,
            "cvar5_improvement": 0.01899322984392323,
            "drawdown_improvement": 0.18295446210485555,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3751701175328933,
            "sortino_excess": 1.0566027419943804,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00207407695,
            "cvar5_improvement": 0.01928144099810454,
            "drawdown_improvement": 0.17546511363481399,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.617780714172817,
            "sortino_excess": 1.4472669395014837,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011416717,
            "cvar5_improvement": 0.022998773979702215,
            "drawdown_improvement": 0.20195741734487369,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5092001099100526,
            "sortino_excess": 1.2724527338082532,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001621138,
            "cvar5_improvement": 0.02099001018711197,
            "drawdown_improvement": 0.1893721366954693,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5717717503052222,
            "sortino_excess": 1.367006737939191,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003289015875,
            "cvar5_improvement": 0.021079259687257677,
            "drawdown_improvement": 0.18833046435605336,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6161311276352152,
            "sortino_excess": 1.3532751153839904,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00330493255,
            "cvar5_improvement": 0.021592684355715965,
            "drawdown_improvement": 0.18868597783592408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.662941446114345,
            "sortino_excess": 1.3526383893963372,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001080465175,
            "cvar5_improvement": 0.02726017276034239,
            "drawdown_improvement": 0.22859645325681244,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.620395585638055,
            "sortino_excess": 1.1655274643593652,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016016633000000002,
            "cvar5_improvement": 0.021885795223190816,
            "drawdown_improvement": 0.19689282572951688,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.41271687060226014,
            "sortino_excess": 1.1715017381079178,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015660033749999999,
            "cvar5_improvement": 0.023713101554399832,
            "drawdown_improvement": 0.20259068423968252,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5251722882383487,
            "sortino_excess": 1.2329364074475304,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00154580875,
            "cvar5_improvement": 0.02011687109705137,
            "drawdown_improvement": 0.18633507924882983,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4733084385675262,
            "sortino_excess": 1.268716811225894,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008519099,
            "cvar5_improvement": 0.02688946745804519,
            "drawdown_improvement": 0.2267248321472255,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.41062188216499934,
            "sortino_excess": 1.1432727803073959,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016504752000000003,
            "cvar5_improvement": 0.018692541222938022,
            "drawdown_improvement": 0.1759193099868726,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5323622838400874,
            "sortino_excess": 1.3028674094140378,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002323267825,
            "cvar5_improvement": 0.0217460182037334,
            "drawdown_improvement": 0.18883276016770464,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5018644850783114,
            "sortino_excess": 1.0581416088702555,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001296658325,
            "cvar5_improvement": 0.025406923457829633,
            "drawdown_improvement": 0.21645209795812245,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6696465679388663,
            "sortino_excess": 1.212444430716842,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0026943538000000003,
            "cvar5_improvement": 0.022602644096692884,
            "drawdown_improvement": 0.19934150354745528,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4615434611185037,
            "sortino_excess": 1.1993164635851743,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001323963575,
            "cvar5_improvement": 0.025484152014630633,
            "drawdown_improvement": 0.21488147648123965,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4698455084565717,
            "sortino_excess": 1.2004265146203685,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001080150275,
            "cvar5_improvement": 0.023853790672841477,
            "drawdown_improvement": 0.21056758347479526,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3371098094046721,
            "sortino_excess": 1.034067484827792,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008620724249999999,
            "cvar5_improvement": 0.026363724451191686,
            "drawdown_improvement": 0.22508199273884755,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.33540451568121554,
            "sortino_excess": 1.1080353416650786,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001043862125,
            "cvar5_improvement": 0.026913256805932803,
            "drawdown_improvement": 0.2242118733709994,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2113758316419731,
            "sortino_excess": 0.9720192845714378,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00092149175,
            "cvar5_improvement": 0.027304349529683483,
            "drawdown_improvement": 0.22647336632837858,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22890893622739697,
            "sortino_excess": 0.8990558058757958,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0026507322499999997,
            "cvar5_improvement": 0.025228463479502795,
            "drawdown_improvement": 0.21287103608925675,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5727581060622802,
            "sortino_excess": 1.2837282263857226,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001229402975,
            "cvar5_improvement": 0.02529235663334336,
            "drawdown_improvement": 0.21553103507910434,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5706262557011083,
            "sortino_excess": 1.2849932037723757,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013412895750000002,
            "cvar5_improvement": 0.01905009800084715,
            "drawdown_improvement": 0.1832754747799514,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.37773824713217796,
            "sortino_excess": 1.1395137308460086,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010411929000000001,
            "cvar5_improvement": 0.024826616297515734,
            "drawdown_improvement": 0.21377913890114586,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4483576892419354,
            "sortino_excess": 1.2196543797516206,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015055980500000002,
            "cvar5_improvement": 0.021747882475261708,
            "drawdown_improvement": 0.19247153167871475,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6213864749613986,
            "sortino_excess": 1.3429339347572935,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000959189925,
            "cvar5_improvement": 0.023845010365881148,
            "drawdown_improvement": 0.21066697979310972,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.33112597728807247,
            "sortino_excess": 1.059108302880543,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00306990995,
            "cvar5_improvement": 0.017886682307944424,
            "drawdown_improvement": 0.17220149043115437,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4714925557699231,
            "sortino_excess": 1.1888364363573798,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001873151475,
            "cvar5_improvement": 0.02295939530184888,
            "drawdown_improvement": 0.2022315586747313,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5348044690495082,
            "sortino_excess": 1.2778253157320598,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016516088000000002,
            "cvar5_improvement": 0.019488329606686443,
            "drawdown_improvement": 0.18316321240249178,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4035199079585637,
            "sortino_excess": 1.1648187147114077,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011599298,
            "cvar5_improvement": 0.02147770205197148,
            "drawdown_improvement": 0.19696455446463834,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.35848992647237277,
            "sortino_excess": 1.1216132333702071,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000974442375,
            "cvar5_improvement": 0.02472393479809642,
            "drawdown_improvement": 0.21335014485886428,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42916268939552044,
            "sortino_excess": 1.1841057378896225,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009890879749999998,
            "cvar5_improvement": 0.02639583243262155,
            "drawdown_improvement": 0.22515111918382458,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3548279769414668,
            "sortino_excess": 1.1301754881637596,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018825652500000002,
            "cvar5_improvement": 0.01976736034814042,
            "drawdown_improvement": 0.18467718027563074,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.40248646299209384,
            "sortino_excess": 1.15466948093354,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013777372750000002,
            "cvar5_improvement": 0.019070432160208158,
            "drawdown_improvement": 0.18338919512896026,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3770961208672128,
            "sortino_excess": 1.1219648056525726,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001744422375,
            "cvar5_improvement": 0.02319809675751544,
            "drawdown_improvement": 0.2017005298321153,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.387979317011162,
            "sortino_excess": 1.0925255106739193,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001509387025,
            "cvar5_improvement": 0.018447249443721652,
            "drawdown_improvement": 0.17475948266557614,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5027931268187923,
            "sortino_excess": 1.2724925323858542,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00221345315,
            "cvar5_improvement": 0.021202480995650117,
            "drawdown_improvement": 0.18989320188566322,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5717639030916277,
            "sortino_excess": 1.2872436902874573,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002538284625,
            "cvar5_improvement": 0.024827343442405288,
            "drawdown_improvement": 0.21336806528759825,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4812439507463475,
            "sortino_excess": 1.2262689951365013,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010717786250000001,
            "cvar5_improvement": 0.02537217834464533,
            "drawdown_improvement": 0.2166928106147876,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5621671676732538,
            "sortino_excess": 1.2049090741882909,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000979612175,
            "cvar5_improvement": 0.027017089725843303,
            "drawdown_improvement": 0.22736967617942674,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4734421368500523,
            "sortino_excess": 1.210372941028204,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008100417,
            "cvar5_improvement": 0.026295164117022367,
            "drawdown_improvement": 0.22484971452050834,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.32277586875530384,
            "sortino_excess": 1.0523669374745246,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019369646500000002,
            "cvar5_improvement": 0.02064551197317183,
            "drawdown_improvement": 0.186148577884013,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5588421714757639,
            "sortino_excess": 1.3512180928847908,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002090621725,
            "cvar5_improvement": 0.02311376051429443,
            "drawdown_improvement": 0.19840453548527323,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4055364819587964,
            "sortino_excess": 1.0482507752818189,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013811362250000002,
            "cvar5_improvement": 0.02103140245977619,
            "drawdown_improvement": 0.189330267502943,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5253976931428103,
            "sortino_excess": 1.2795222731143614,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000882075825,
            "cvar5_improvement": 0.02736385109496505,
            "drawdown_improvement": 0.2274593129318168,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30547925246674795,
            "sortino_excess": 1.032030796243646,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001024216,
            "cvar5_improvement": 0.02507633463722137,
            "drawdown_improvement": 0.21480019596979918,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.48252987347718945,
            "sortino_excess": 1.2125703003409496,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009380184249999999,
            "cvar5_improvement": 0.027255089091791855,
            "drawdown_improvement": 0.22834461297084427,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.49826175339847756,
            "sortino_excess": 1.1753881087166975,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00150099965,
            "cvar5_improvement": 0.02513036830979764,
            "drawdown_improvement": 0.21292867141130234,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25397548943335835,
            "sortino_excess": 0.9682228669817141,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00210478865,
            "cvar5_improvement": 0.021503925038109342,
            "drawdown_improvement": 0.1908817735123224,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7508040713015947,
            "sortino_excess": 1.432253142029725,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001028648225,
            "cvar5_improvement": 0.02723467598296565,
            "drawdown_improvement": 0.22951714139617538,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6244418984513074,
            "sortino_excess": 1.1436250443854534,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00119522745,
            "cvar5_improvement": 0.021500801244553985,
            "drawdown_improvement": 0.1970838826762824,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3577318151668109,
            "sortino_excess": 1.1011327725516187,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0023006699,
            "cvar5_improvement": 0.023363736853067793,
            "drawdown_improvement": 0.20256603907553408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6196295981161786,
            "sortino_excess": 1.2367222259970088,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00132601,
            "cvar5_improvement": 0.02390892175548745,
            "drawdown_improvement": 0.20629891116333646,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.649765383409074,
            "sortino_excess": 1.2782002795399445,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001664331975,
            "cvar5_improvement": 0.016676066751105726,
            "drawdown_improvement": 0.16996144672674193,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4079947403903143,
            "sortino_excess": 1.1650920741915354,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000825303525,
            "cvar5_improvement": 0.027005395778122505,
            "drawdown_improvement": 0.22750631317735495,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.45827953994032117,
            "sortino_excess": 1.206226831846576,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002230626075,
            "cvar5_improvement": 0.019129072963506532,
            "drawdown_improvement": 0.17568992200624658,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6558858473903516,
            "sortino_excess": 1.4553855929751363,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001099514025,
            "cvar5_improvement": 0.02687073694582504,
            "drawdown_improvement": 0.2244112187293594,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22771322078527545,
            "sortino_excess": 0.9921272961781733,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00140392805,
            "cvar5_improvement": 0.02088197351914811,
            "drawdown_improvement": 0.18893144087196703,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5240597028164087,
            "sortino_excess": 1.3063211388131948,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001332603125,
            "cvar5_improvement": 0.023027433189059754,
            "drawdown_improvement": 0.20176690394934024,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5287569887435442,
            "sortino_excess": 1.2946882076241595,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015249148500000001,
            "cvar5_improvement": 0.019033089860830892,
            "drawdown_improvement": 0.17734903249328618,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5648833860611933,
            "sortino_excess": 1.3410908171909335,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013841411250000001,
            "cvar5_improvement": 0.023405098948427412,
            "drawdown_improvement": 0.20436415377958073,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6227818884918055,
            "sortino_excess": 1.3016075174986494,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015068149,
            "cvar5_improvement": 0.02731075370687789,
            "drawdown_improvement": 0.22648855399198875,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36581921357714287,
            "sortino_excess": 0.9127765667586722,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00122998155,
            "cvar5_improvement": 0.025372601391001292,
            "drawdown_improvement": 0.21763900014134277,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6688889431402041,
            "sortino_excess": 1.202580359757397,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001192354675,
            "cvar5_improvement": 0.022465990939392236,
            "drawdown_improvement": 0.1997802251080704,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44185987055325765,
            "sortino_excess": 1.2337245668682706,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010595348,
            "cvar5_improvement": 0.027117741401638012,
            "drawdown_improvement": 0.2282075413002637,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5433882089691993,
            "sortino_excess": 1.2730835868744756,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003088325575,
            "cvar5_improvement": 0.02040976215506172,
            "drawdown_improvement": 0.17913480493872883,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5239347511974533,
            "sortino_excess": 1.2700011910998135,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00178811505,
            "cvar5_improvement": 0.023359917752290238,
            "drawdown_improvement": 0.2025690281986559,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6584052227313114,
            "sortino_excess": 1.399215830061759,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001199832925,
            "cvar5_improvement": 0.02730165195673083,
            "drawdown_improvement": 0.22740846429441372,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5115277862350931,
            "sortino_excess": 1.2877311447875752,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011291249,
            "cvar5_improvement": 0.024744467861355486,
            "drawdown_improvement": 0.21313924062796027,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44161517220844354,
            "sortino_excess": 1.2047194750781376,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009903043,
            "cvar5_improvement": 0.025252680035866233,
            "drawdown_improvement": 0.21596911261492002,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5393298239104349,
            "sortino_excess": 1.284219998647034,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00122934185,
            "cvar5_improvement": 0.021421662740859698,
            "drawdown_improvement": 0.1966433295442528,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3551382590086166,
            "sortino_excess": 1.0420204510998228,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000978753275,
            "cvar5_improvement": 0.02378779760452107,
            "drawdown_improvement": 0.21028893870293325,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.31731429405237477,
            "sortino_excess": 1.039218011085727,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001720204825,
            "cvar5_improvement": 0.023459539464951457,
            "drawdown_improvement": 0.20199199280537813,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5694965240789001,
            "sortino_excess": 1.273235268869014,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00142876035,
            "cvar5_improvement": 0.02523760396489496,
            "drawdown_improvement": 0.21362936965701496,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5505401081472024,
            "sortino_excess": 1.359683527866494,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013623050750000002,
            "cvar5_improvement": 0.022529939237821203,
            "drawdown_improvement": 0.20005664148699565,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.47486575584483415,
            "sortino_excess": 1.2696849059017123,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00161686845,
            "cvar5_improvement": 0.02507681322754044,
            "drawdown_improvement": 0.21126517722200294,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23410245906322838,
            "sortino_excess": 0.8916555719969165,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001616915275,
            "cvar5_improvement": 0.02694867208020617,
            "drawdown_improvement": 0.2233376591708792,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.31876322894961984,
            "sortino_excess": 0.890034497765933,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00196775815,
            "cvar5_improvement": 0.025623513171915382,
            "drawdown_improvement": 0.21569539925715459,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42654296307430495,
            "sortino_excess": 1.4882371520738467,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008295227749999999,
            "cvar5_improvement": 0.026238728137976376,
            "drawdown_improvement": 0.22444243319045723,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3019060056273846,
            "sortino_excess": 1.0231251627996518,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00169694735,
            "cvar5_improvement": 0.021435811935827782,
            "drawdown_improvement": 0.19242571127558433,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6746131741689463,
            "sortino_excess": 1.44372791836915,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001177382075,
            "cvar5_improvement": 0.022827897384845294,
            "drawdown_improvement": 0.2008156215076945,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.46685394342737124,
            "sortino_excess": 1.2166994196060243,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016091196,
            "cvar5_improvement": 0.017724070983696227,
            "drawdown_improvement": 0.17293609703002363,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.462415075729008,
            "sortino_excess": 1.2325265413574777,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001202176625,
            "cvar5_improvement": 0.02324247700097965,
            "drawdown_improvement": 0.20305884403245217,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5369945914850516,
            "sortino_excess": 1.2658835700306308,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001546232425,
            "cvar5_improvement": 0.024557259710035625,
            "drawdown_improvement": 0.2123801388640127,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3828336475793255,
            "sortino_excess": 1.1362900249103045,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001698305675,
            "cvar5_improvement": 0.022189352338436528,
            "drawdown_improvement": 0.19838803060846538,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3877703245718419,
            "sortino_excess": 1.1388617012892495,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015688880749999998,
            "cvar5_improvement": 0.018795127927344793,
            "drawdown_improvement": 0.175821222790659,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5239422493470884,
            "sortino_excess": 1.2882219441082288,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001108177175,
            "cvar5_improvement": 0.021413171718854485,
            "drawdown_improvement": 0.19673051006928652,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.34896744152731385,
            "sortino_excess": 1.0775946990934753,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00188505905,
            "cvar5_improvement": 0.021472748947662205,
            "drawdown_improvement": 0.18889191072580075,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6322090166980181,
            "sortino_excess": 1.4530427851370367,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015626767,
            "cvar5_improvement": 0.01767771083721076,
            "drawdown_improvement": 0.17260744227724478,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.45936685282260614,
            "sortino_excess": 1.2562442364221165,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008746258250000001,
            "cvar5_improvement": 0.02716292408241789,
            "drawdown_improvement": 0.2286037833953652,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.523967944524931,
            "sortino_excess": 1.1856263205077133,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020513324,
            "cvar5_improvement": 0.021291925216825616,
            "drawdown_improvement": 0.18901280455154149,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44395619149037724,
            "sortino_excess": 1.1225595942840523,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011980589,
            "cvar5_improvement": 0.026412273279642223,
            "drawdown_improvement": 0.22225967431891738,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1067540325311063,
            "sortino_excess": 0.8430057923664354,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002080423375,
            "cvar5_improvement": 0.019801776747124775,
            "drawdown_improvement": 0.1783381477579648,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6337714864281052,
            "sortino_excess": 1.4584491817366831,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0028804969,
            "cvar5_improvement": 0.020266236240538187,
            "drawdown_improvement": 0.18563549096966228,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4633693867303415,
            "sortino_excess": 1.190642049264295,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001514326475,
            "cvar5_improvement": 0.020763274794844154,
            "drawdown_improvement": 0.18798369450017835,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5179695915659979,
            "sortino_excess": 1.2967376915817483,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001347074175,
            "cvar5_improvement": 0.02716924771540088,
            "drawdown_improvement": 0.22758693717021639,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6084060618443113,
            "sortino_excess": 1.3039569243950382,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001309180825,
            "cvar5_improvement": 0.018949584272062947,
            "drawdown_improvement": 0.18269180250208836,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36054464688341287,
            "sortino_excess": 1.0886448661668526,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001280932225,
            "cvar5_improvement": 0.02236281775245151,
            "drawdown_improvement": 0.19915852201201664,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.43602433632882465,
            "sortino_excess": 1.1895660426936214,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015572222249999998,
            "cvar5_improvement": 0.02513090105746312,
            "drawdown_improvement": 0.21374166670577116,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5892661218583342,
            "sortino_excess": 1.3573210140039358,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022448492,
            "cvar5_improvement": 0.0187066876909127,
            "drawdown_improvement": 0.175694228711888,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.523142783083554,
            "sortino_excess": 1.2999858683544503,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001304822875,
            "cvar5_improvement": 0.027166577413768996,
            "drawdown_improvement": 0.22613468550650034,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5302023187452095,
            "sortino_excess": 1.1201112748180808,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015344896750000001,
            "cvar5_improvement": 0.016653818270552637,
            "drawdown_improvement": 0.16982643823937513,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.39953031414618123,
            "sortino_excess": 1.1605123275353857,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002127296725,
            "cvar5_improvement": 0.01832646216562205,
            "drawdown_improvement": 0.17277439122259153,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5552583657956024,
            "sortino_excess": 1.3493604140833708,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017737913000000001,
            "cvar5_improvement": 0.027087307169307497,
            "drawdown_improvement": 0.22688991694698574,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4749264375182639,
            "sortino_excess": 1.1355593923241964,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010064235000000002,
            "cvar5_improvement": 0.025521392663035786,
            "drawdown_improvement": 0.21803723212783624,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6509661685917357,
            "sortino_excess": 1.3246674819669408,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001168091925,
            "cvar5_improvement": 0.026719403152389496,
            "drawdown_improvement": 0.2249112212809707,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.388968318999101,
            "sortino_excess": 1.1762422731861553,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00089192235,
            "cvar5_improvement": 0.027108297487274446,
            "drawdown_improvement": 0.22800175622870683,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4795544207997464,
            "sortino_excess": 1.1757144414817842,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001466995975,
            "cvar5_improvement": 0.02191987207742126,
            "drawdown_improvement": 0.19685982654677212,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.38950013709546283,
            "sortino_excess": 1.154504169957577,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00150190235,
            "cvar5_improvement": 0.01655140656438828,
            "drawdown_improvement": 0.16923504961091002,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.383856962773951,
            "sortino_excess": 1.1149577517947291,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00175575545,
            "cvar5_improvement": 0.019065164733227075,
            "drawdown_improvement": 0.17702029426606453,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5860545357435445,
            "sortino_excess": 1.3691343721029292,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013087304749999998,
            "cvar5_improvement": 0.027061912771273587,
            "drawdown_improvement": 0.22656007242418436,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3064600264117213,
            "sortino_excess": 0.9796346336303515,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008975080750000001,
            "cvar5_improvement": 0.026397927146478553,
            "drawdown_improvement": 0.22524678629462608,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.33706370252522483,
            "sortino_excess": 1.0837892747315803,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00237669575,
            "cvar5_improvement": 0.026925542537215828,
            "drawdown_improvement": 0.226060064923024,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4595026918902179,
            "sortino_excess": 1.1974648323418944,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013972447750000001,
            "cvar5_improvement": 0.02681726563698793,
            "drawdown_improvement": 0.2265392912544523,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.39206847081829416,
            "sortino_excess": 1.1386733522090025,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008541385,
            "cvar5_improvement": 0.027250495487583244,
            "drawdown_improvement": 0.22746150923329708,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23310108810326094,
            "sortino_excess": 0.8260242401817135,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016923089500000001,
            "cvar5_improvement": 0.01949265197035677,
            "drawdown_improvement": 0.17896074000549142,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6069774159608738,
            "sortino_excess": 1.3412260769562327,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00101122005,
            "cvar5_improvement": 0.023910968065234458,
            "drawdown_improvement": 0.2108916493037172,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.34160513366862133,
            "sortino_excess": 1.1084669419530067,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010870120750000002,
            "cvar5_improvement": 0.024920482816052823,
            "drawdown_improvement": 0.21408894835461495,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4581811419887201,
            "sortino_excess": 1.2016235751278188,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010466116750000001,
            "cvar5_improvement": 0.0239436342520035,
            "drawdown_improvement": 0.21104726661937984,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.34310251889485643,
            "sortino_excess": 1.088044263846351,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002075129775,
            "cvar5_improvement": 0.022511268196058087,
            "drawdown_improvement": 0.1987180621917969,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.43509817542583307,
            "sortino_excess": 1.1264927201689332,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00148171335,
            "cvar5_improvement": 0.01660814331210374,
            "drawdown_improvement": 0.16961982754568308,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.39194935304749234,
            "sortino_excess": 1.1263408007515774,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 2.0,
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
            "config_hash": "21689e24dc18ba601d9f14348099e07264d8de1eaf474dc390d782e652382168",
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 4.0,
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
            "config_hash": "5287352a22ba877f8449d3c07f2c4e42cae86b2e142fc23e5322283e2bda91b8",
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": true
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 3,
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
            "config_hash": "34c7658bc1bd300e0bad621d7909f6ddff945fe70ebc2bac87801f94c07953f8",
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": true
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 10,
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
            "config_hash": "72584a40092f0707d80fa28f36e4b2219156f0bca376ac1717ab21cc31f30c4d",
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
                "cooldown_sessions": 0,
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
            "config_hash": "ad84e5361d1b7f8a10535519b1342c8f50295bb009b4d311a1e2cd4fe8f768c1",
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020415157500000003,
            "cvar5_improvement": 0.021316997185762167,
            "drawdown_improvement": 0.18909924651978408,
            "exposure_ratio": 0.4503968253968254,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.6755471786070781,
            "sortino_excess": 1.4541271362479633,
            "stable": true
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00026348775,
            "cvar5_improvement": 0.028180922537104115,
            "drawdown_improvement": 0.2528762596442694,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000130070925,
            "cvar5_improvement": 0.031056335175778493,
            "drawdown_improvement": 0.261393164937501,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00037758315,
            "cvar5_improvement": 0.02626771083430113,
            "drawdown_improvement": 0.2465713823903009,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000149998125,
            "cvar5_improvement": 0.03166280520955293,
            "drawdown_improvement": 0.2631197015476756,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026348775,
            "cvar5_improvement": 0.028180922537104115,
            "drawdown_improvement": 0.2528762596442694,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000130070925,
            "cvar5_improvement": 0.031056335175778493,
            "drawdown_improvement": 0.261393164937501,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0001898122,
            "cvar5_improvement": 0.030008942871633176,
            "drawdown_improvement": 0.2582321532514512,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000149998125,
            "cvar5_improvement": 0.03166280520955293,
            "drawdown_improvement": 0.2631197015476756,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026348775,
            "cvar5_improvement": 0.028180922537104115,
            "drawdown_improvement": 0.2528762596442694,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021595335,
            "cvar5_improvement": 0.030871261091549494,
            "drawdown_improvement": 0.26053142190375245,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00037758315,
            "cvar5_improvement": 0.02626771083430113,
            "drawdown_improvement": 0.2465713823903009,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0003575777,
            "cvar5_improvement": 0.027108220792216725,
            "drawdown_improvement": 0.2492031265407379,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000275169225,
            "cvar5_improvement": 0.029142632175953073,
            "drawdown_improvement": 0.25525682534758276,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000377265675,
            "cvar5_improvement": 0.026263457898688284,
            "drawdown_improvement": 0.2465332337438613,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026546895,
            "cvar5_improvement": 0.028137329744762376,
            "drawdown_improvement": 0.2527114192683708,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000293136575,
            "cvar5_improvement": 0.027364762729914203,
            "drawdown_improvement": 0.25055188825767644,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026348775,
            "cvar5_improvement": 0.028180922537104115,
            "drawdown_improvement": 0.2528762596442694,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000187664325,
            "cvar5_improvement": 0.030491743681733484,
            "drawdown_improvement": 0.25966688599362475,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00018921532499999999,
            "cvar5_improvement": 0.030457081763461333,
            "drawdown_improvement": 0.2595349162311024,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000149998125,
            "cvar5_improvement": 0.03166280520955293,
            "drawdown_improvement": 0.2631197015476756,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021595335,
            "cvar5_improvement": 0.030871261091549494,
            "drawdown_improvement": 0.26053142190375245,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0003575777,
            "cvar5_improvement": 0.027108220792216725,
            "drawdown_improvement": 0.2492031265407379,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032794275,
            "cvar5_improvement": 0.027600063483800518,
            "drawdown_improvement": 0.2505614656021759,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026546895,
            "cvar5_improvement": 0.028137329744762376,
            "drawdown_improvement": 0.2527114192683708,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00015077362499999998,
            "cvar5_improvement": 0.03164528571734049,
            "drawdown_improvement": 0.26305276702371544,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000149998125,
            "cvar5_improvement": 0.03166280520955293,
            "drawdown_improvement": 0.2631197015476756,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026348775,
            "cvar5_improvement": 0.028180922537104115,
            "drawdown_improvement": 0.2528762596442694,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000275169225,
            "cvar5_improvement": 0.029142632175953073,
            "drawdown_improvement": 0.25525682534758276,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000262865575,
            "cvar5_improvement": 0.027873154424629717,
            "drawdown_improvement": 0.2519752361401194,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000275169225,
            "cvar5_improvement": 0.029142632175953073,
            "drawdown_improvement": 0.25525682534758276,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032794275,
            "cvar5_improvement": 0.027600063483800518,
            "drawdown_improvement": 0.2505614656021759,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000102451425,
            "cvar5_improvement": 0.03194571352206626,
            "drawdown_improvement": 0.26398630086359814,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000187664325,
            "cvar5_improvement": 0.030491743681733484,
            "drawdown_improvement": 0.25966688599362475,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000299969975,
            "cvar5_improvement": 0.028720762311781396,
            "drawdown_improvement": 0.2540681357314404,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026546895,
            "cvar5_improvement": 0.028137329744762376,
            "drawdown_improvement": 0.2527114192683708,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000299969975,
            "cvar5_improvement": 0.028720762311781396,
            "drawdown_improvement": 0.2540681357314404,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000147008425,
            "cvar5_improvement": 0.03133673230914862,
            "drawdown_improvement": 0.2621566433505996,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00043696082500000003,
            "cvar5_improvement": 0.025427595269670155,
            "drawdown_improvement": 0.24387875798478606,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000149998125,
            "cvar5_improvement": 0.03166280520955293,
            "drawdown_improvement": 0.2631197015476756,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000293136575,
            "cvar5_improvement": 0.027364762729914203,
            "drawdown_improvement": 0.25055188825767644,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0003575777,
            "cvar5_improvement": 0.027108220792216725,
            "drawdown_improvement": 0.2492031265407379,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000225491175,
            "cvar5_improvement": 0.029331197327320785,
            "drawdown_improvement": 0.2562531161478583,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00010322692499999998,
            "cvar5_improvement": 0.031928194029853814,
            "drawdown_improvement": 0.263919366339638,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021545835,
            "cvar5_improvement": 0.030886383620845007,
            "drawdown_improvement": 0.2605931651726682,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000323046925,
            "cvar5_improvement": 0.02848310766337355,
            "drawdown_improvement": 0.25315546231031677,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00040785415,
            "cvar5_improvement": 0.02575931913958562,
            "drawdown_improvement": 0.24514803450785796,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000299969975,
            "cvar5_improvement": 0.028720762311781396,
            "drawdown_improvement": 0.2540681357314404,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032817645,
            "cvar5_improvement": 0.027605663792998874,
            "drawdown_improvement": 0.2506005526512881,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00018921532499999999,
            "cvar5_improvement": 0.030457081763461333,
            "drawdown_improvement": 0.2595349162311024,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000187664325,
            "cvar5_improvement": 0.030491743681733484,
            "drawdown_improvement": 0.25966688599362475,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00037758315,
            "cvar5_improvement": 0.02626771083430113,
            "drawdown_improvement": 0.2465713823903009,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032817645,
            "cvar5_improvement": 0.027605663792998874,
            "drawdown_improvement": 0.2506005526512881,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032817645,
            "cvar5_improvement": 0.027605663792998874,
            "drawdown_improvement": 0.2506005526512881,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032794275,
            "cvar5_improvement": 0.027600063483800518,
            "drawdown_improvement": 0.2505614656021759,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000147008425,
            "cvar5_improvement": 0.03133673230914862,
            "drawdown_improvement": 0.2621566433505996,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000131621925,
            "cvar5_improvement": 0.03102167325750634,
            "drawdown_improvement": 0.2612611951749786,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00022745260000000002,
            "cvar5_improvement": 0.028855769835771417,
            "drawdown_improvement": 0.2548504014877556,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00016744980000000002,
            "cvar5_improvement": 0.031066456489329493,
            "drawdown_improvement": 0.26138157212397883,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000262865575,
            "cvar5_improvement": 0.027873154424629717,
            "drawdown_improvement": 0.2519752361401194,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000189844525,
            "cvar5_improvement": 0.029999465775829622,
            "drawdown_improvement": 0.25818395224410606,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00037758315,
            "cvar5_improvement": 0.02626771083430113,
            "drawdown_improvement": 0.2465713823903009,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000225491175,
            "cvar5_improvement": 0.029331197327320785,
            "drawdown_improvement": 0.2562531161478583,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023589972500000003,
            "cvar5_improvement": 0.030616107801025878,
            "drawdown_improvement": 0.25981809394604743,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0003575777,
            "cvar5_improvement": 0.027108220792216725,
            "drawdown_improvement": 0.2492031265407379,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000187664325,
            "cvar5_improvement": 0.030491743681733484,
            "drawdown_improvement": 0.25966688599362475,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000225491175,
            "cvar5_improvement": 0.029331197327320785,
            "drawdown_improvement": 0.2562531161478583,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00037758315,
            "cvar5_improvement": 0.02626771083430113,
            "drawdown_improvement": 0.2465713823903009,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032817645,
            "cvar5_improvement": 0.027605663792998874,
            "drawdown_improvement": 0.2506005526512881,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00040785415,
            "cvar5_improvement": 0.02575931913958562,
            "drawdown_improvement": 0.24514803450785796,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000187664325,
            "cvar5_improvement": 0.030491743681733484,
            "drawdown_improvement": 0.25966688599362475,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0002625481,
            "cvar5_improvement": 0.02786890148901687,
            "drawdown_improvement": 0.25193708749367977,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00037758315,
            "cvar5_improvement": 0.02626771083430113,
            "drawdown_improvement": 0.2465713823903009,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00018563122499999998,
            "cvar5_improvement": 0.029308652667755647,
            "drawdown_improvement": 0.256315615268284,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00040785415,
            "cvar5_improvement": 0.02575931913958562,
            "drawdown_improvement": 0.24514803450785796,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00025456765,
            "cvar5_improvement": 0.030477294935594344,
            "drawdown_improvement": 0.25928441913259703,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00038330867499999997,
            "cvar5_improvement": 0.026812412982841476,
            "drawdown_improvement": 0.24806985273514343,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00018921532499999999,
            "cvar5_improvement": 0.030457081763461333,
            "drawdown_improvement": 0.2595349162311024,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000323046925,
            "cvar5_improvement": 0.02848310766337355,
            "drawdown_improvement": 0.25315546231031677,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000275169225,
            "cvar5_improvement": 0.029142632175953073,
            "drawdown_improvement": 0.25525682534758276,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023589972500000003,
            "cvar5_improvement": 0.030616107801025878,
            "drawdown_improvement": 0.25981809394604743,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000323046925,
            "cvar5_improvement": 0.02848310766337355,
            "drawdown_improvement": 0.25315546231031677,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00026348775,
            "cvar5_improvement": 0.028180922537104115,
            "drawdown_improvement": 0.2528762596442694,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023589972500000003,
            "cvar5_improvement": 0.030616107801025878,
            "drawdown_improvement": 0.25981809394604743,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000299969975,
            "cvar5_improvement": 0.028720762311781396,
            "drawdown_improvement": 0.2540681357314404,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000377265675,
            "cvar5_improvement": 0.026263457898688284,
            "drawdown_improvement": 0.2465332337438613,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000275169225,
            "cvar5_improvement": 0.029142632175953073,
            "drawdown_improvement": 0.25525682534758276,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000149998125,
            "cvar5_improvement": 0.03166280520955293,
            "drawdown_improvement": 0.2631197015476756,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00018563122499999998,
            "cvar5_improvement": 0.029308652667755647,
            "drawdown_improvement": 0.256315615268284,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032224325000000003,
            "cvar5_improvement": 0.027033038859998738,
            "drawdown_improvement": 0.24928261173460453,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00015077362499999998,
            "cvar5_improvement": 0.03164528571734049,
            "drawdown_improvement": 0.26305276702371544,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00027520155,
            "cvar5_improvement": 0.02913315508014952,
            "drawdown_improvement": 0.2552086243402376,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000187664325,
            "cvar5_improvement": 0.030491743681733484,
            "drawdown_improvement": 0.25966688599362475,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023589972500000003,
            "cvar5_improvement": 0.030616107801025878,
            "drawdown_improvement": 0.25981809394604743,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00025456765,
            "cvar5_improvement": 0.030477294935594344,
            "drawdown_improvement": 0.25928441913259703,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000299969975,
            "cvar5_improvement": 0.028720762311781396,
            "drawdown_improvement": 0.2540681357314404,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00040785415,
            "cvar5_improvement": 0.02575931913958562,
            "drawdown_improvement": 0.24514803450785796,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00025685385,
            "cvar5_improvement": 0.02835832683498927,
            "drawdown_improvement": 0.25345297537720535,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000227657025,
            "cvar5_improvement": 0.029283257257645485,
            "drawdown_improvement": 0.25607122503378477,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000227657025,
            "cvar5_improvement": 0.029283257257645485,
            "drawdown_improvement": 0.25607122503378477,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00018761242500000001,
            "cvar5_improvement": 0.029265059875413908,
            "drawdown_improvement": 0.25615077489238547,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021545835,
            "cvar5_improvement": 0.030886383620845007,
            "drawdown_improvement": 0.2605931651726682,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00040785415,
            "cvar5_improvement": 0.02575931913958562,
            "drawdown_improvement": 0.24514803450785796,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023589972500000003,
            "cvar5_improvement": 0.030616107801025878,
            "drawdown_improvement": 0.25981809394604743,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0001898122,
            "cvar5_improvement": 0.030008942871633176,
            "drawdown_improvement": 0.2582321532514512,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023589972500000003,
            "cvar5_improvement": 0.030616107801025878,
            "drawdown_improvement": 0.25981809394604743,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0003575777,
            "cvar5_improvement": 0.027108220792216725,
            "drawdown_improvement": 0.2492031265407379,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00038330867499999997,
            "cvar5_improvement": 0.026812412982841476,
            "drawdown_improvement": 0.24806985273514343,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000227657025,
            "cvar5_improvement": 0.029283257257645485,
            "drawdown_improvement": 0.25607122503378477,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00015785107499999998,
            "cvar5_improvement": 0.030176257790207175,
            "drawdown_improvement": 0.25883223758141893,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000160016925,
            "cvar5_improvement": 0.030128317720531875,
            "drawdown_improvement": 0.2586503464673454,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00025456765,
            "cvar5_improvement": 0.030477294935594344,
            "drawdown_improvement": 0.25928441913259703,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021545835,
            "cvar5_improvement": 0.030886383620845007,
            "drawdown_improvement": 0.2605931651726682,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021545835,
            "cvar5_improvement": 0.030886383620845007,
            "drawdown_improvement": 0.2605931651726682,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00023768989999999998,
            "cvar5_improvement": 0.02934941835905365,
            "drawdown_improvement": 0.2561307902141852,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00027520155,
            "cvar5_improvement": 0.02913315508014952,
            "drawdown_improvement": 0.2552086243402376,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021595335,
            "cvar5_improvement": 0.030871261091549494,
            "drawdown_improvement": 0.26053142190375245,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000225491175,
            "cvar5_improvement": 0.029331197327320785,
            "drawdown_improvement": 0.2562531161478583,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021461295,
            "cvar5_improvement": 0.029587073007461495,
            "drawdown_improvement": 0.25704346363530883,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00015785107499999998,
            "cvar5_improvement": 0.030176257790207175,
            "drawdown_improvement": 0.25883223758141893,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000186117725,
            "cvar5_improvement": 0.03092764362389796,
            "drawdown_improvement": 0.2608478973105285,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000102451425,
            "cvar5_improvement": 0.03194571352206626,
            "drawdown_improvement": 0.26398630086359814,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00038330867499999997,
            "cvar5_improvement": 0.026812412982841476,
            "drawdown_improvement": 0.24806985273514343,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00043696082500000003,
            "cvar5_improvement": 0.025427595269670155,
            "drawdown_improvement": 0.24387875798478606,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.0003575777,
            "cvar5_improvement": 0.027108220792216725,
            "drawdown_improvement": 0.2492031265407379,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00022721890000000001,
            "cvar5_improvement": 0.02885016952657306,
            "drawdown_improvement": 0.25481131443864335,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021545835,
            "cvar5_improvement": 0.030886383620845007,
            "drawdown_improvement": 0.2605931651726682,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00014750342499999998,
            "cvar5_improvement": 0.03132160977985311,
            "drawdown_improvement": 0.2620949000816839,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000299969975,
            "cvar5_improvement": 0.028720762311781396,
            "drawdown_improvement": 0.2540681357314404,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00015077362499999998,
            "cvar5_improvement": 0.03164528571734049,
            "drawdown_improvement": 0.26305276702371544,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00027520155,
            "cvar5_improvement": 0.02913315508014952,
            "drawdown_improvement": 0.2552086243402376,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00022745260000000002,
            "cvar5_improvement": 0.028855769835771417,
            "drawdown_improvement": 0.2548504014877556,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000275169225,
            "cvar5_improvement": 0.029142632175953073,
            "drawdown_improvement": 0.25525682534758276,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021545835,
            "cvar5_improvement": 0.030886383620845007,
            "drawdown_improvement": 0.2605931651726682,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000282584825,
            "cvar5_improvement": 0.02806251902561402,
            "drawdown_improvement": 0.2523197015716109,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000225491175,
            "cvar5_improvement": 0.029331197327320785,
            "drawdown_improvement": 0.2562531161478583,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00043696082500000003,
            "cvar5_improvement": 0.025427595269670155,
            "drawdown_improvement": 0.24387875798478606,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00025685385,
            "cvar5_improvement": 0.02835832683498927,
            "drawdown_improvement": 0.25345297537720535,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00040785415,
            "cvar5_improvement": 0.02575931913958562,
            "drawdown_improvement": 0.24514803450785796,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032817645,
            "cvar5_improvement": 0.027605663792998874,
            "drawdown_improvement": 0.2506005526512881,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00032817645,
            "cvar5_improvement": 0.027605663792998874,
            "drawdown_improvement": 0.2506005526512881,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000225491175,
            "cvar5_improvement": 0.029331197327320785,
            "drawdown_improvement": 0.2562531161478583,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00021461295,
            "cvar5_improvement": 0.029587073007461495,
            "drawdown_improvement": 0.25704346363530883,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.00016744980000000002,
            "cvar5_improvement": 0.031066456489329493,
            "drawdown_improvement": 0.26138157212397883,
            "exposure_ratio": 0.08134920634920635,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            "cost_drag": 0.000377265675,
            "cvar5_improvement": 0.026263457898688284,
            "drawdown_improvement": 0.2465332337438613,
            "exposure_ratio": 0.125,
            "family": "trend_only",
            "positive_subperiod_share": 1.0,
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
            ],
            [
              "atr_stop_multiple"
            ],
            [
              "cooldown_sessions"
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
