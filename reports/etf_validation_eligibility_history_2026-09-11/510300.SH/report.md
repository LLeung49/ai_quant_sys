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
            0.08531787610000016,
            0.04410736100000001,
            0.011810525799999855,
            0.1266534825000001
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
            0.08082345650000022,
            0.04838446420000001,
            0.010926812599999884,
            0.11555605260000013
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
            0.07608750970000026,
            0.05300962040000001,
            0.010067105399999913,
            0.10470664130000015
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
            0.0709070265000003,
            0.05741775290000001,
            0.009303342999999941,
            0.09332759060000018
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
            0.06543896280000036,
            0.06201600910000002,
            0.00870780639999997,
            0.0825107499000002
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
            0.07503872800000018,
            0.04777487360000003,
            0.016245219499999866,
            0.12102175020000014
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
            0.06805025630000022,
            0.05326807890000003,
            0.015674068199999894,
            0.10968175110000017
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
            0.06315461880000027,
            0.05788853510000003,
            0.015098994099999923,
            0.09887753280000018
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
            0.06014969650000031,
            0.06229656760000003,
            0.014041580699999952,
            0.0874459891000002
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
            0.05610585570000037,
            0.06689492380000003,
            0.013064814099999978,
            0.07678211400000023
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
            0.0698716995000002,
            0.05356414180000006,
            0.021113653499999874,
            0.11500557460000019
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
            0.06477944060000024,
            0.05776042300000006,
            0.020139529899999904,
            0.10367110350000021
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
            0.05521927510000029,
            0.06091329190000004,
            0.01904260059999993,
            0.09300854520000022
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
            0.04695297960000033,
            0.060759688000000034,
            0.01835059399999996,
            0.08239280110000025
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "2b1ca3a349c41d3e74f6ea219a4c0fe30f94bd0c8d69053d8a263b0a0abd2acc",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.04243637290000038,
            0.05638400870000003,
            0.017684749299999986,
            0.07241043530000026
          ],
          "positive_window_share": 1.0
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
            0.07074757620000022,
            0.06311489130000006,
            0.02140140019999981,
            0.10890945910000022
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
            0.05636974190000027,
            0.06287407250000009,
            0.024456920799999914,
            0.09793711170000025
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
            0.05195889510000031,
            0.058177187500000074,
            0.02386146739999994,
            0.08823023160000025
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
            0.04051484420000036,
            0.053389598100000074,
            0.023384824199999966,
            0.07836451760000027
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c1f8d05174940de5abab81e70dbabad9d91d52b696bb409bdd2ab6d799a45da8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.03838093750000038,
            0.04875444190000007,
            0.023814255399999998,
            0.07186601200000026
          ],
          "positive_window_share": 1.0
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
            0.08952312140000016,
            0.037167233600000016,
            0.01161012139999985,
            0.12982675850000008
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
            0.0857350003000002,
            0.042163346800000015,
            0.010909244499999879,
            0.11843958920000011
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
            0.08083969790000024,
            0.046790603000000014,
            0.010019356599999907,
            0.10770091970000013
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
            0.07581283850000028,
            0.05120093550000002,
            0.009443230499999936,
            0.09666862030000016
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
            0.07033514770000032,
            0.05543073470000002,
            0.008721768999999964,
            0.08551145680000018
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
            0.08444910080000018,
            0.03505787660000005,
            0.015463589999999854,
            0.12687251300000013
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
            0.07765464760000024,
            0.03893495120000004,
            0.014926663899999883,
            0.11568426560000014
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
            0.07230484330000027,
            0.04399270380000003,
            0.014335642699999911,
            0.10456684250000016
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
            0.06842600610000031,
            0.048403036300000035,
            0.01390199409999994,
            0.09340681300000019
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
            0.06509487390000038,
            0.05263283550000004,
            0.012704989699999968,
            0.0825726578000002
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
            0.08380923680000021,
            0.035912159000000055,
            0.01982714399999986,
            0.12375783930000014
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
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
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
            0.0693021659000003,
            0.042151371400000075,
            0.018537009599999918,
            0.10160501860000018
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
            0.06151745130000034,
            0.04539813490000005,
            0.017411673399999945,
            0.0906088878000002
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
            0.05584119680000038,
            0.04901902730000006,
            0.016591143399999973,
            0.07977249910000023
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
            0.08991134960000023,
            0.04297214820000006,
            0.015120198799999861,
            0.12079399380000017
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
            0.07486137380000027,
            0.03989250450000008,
            0.02338217579999989,
            0.10950628770000018
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
            0.07020183990000031,
            0.04428594420000008,
            0.02217381889999992,
            0.09871973470000021
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
            0.05861764220000036,
            0.0438775492000001,
            0.021652039099999947,
            0.08750761220000024
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
            0.0535282974000004,
            0.0479976782000001,
            0.021044741799999975,
            0.07817663530000024
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
            0.09331358960000019,
            0.03685276160000001,
            0.010644953799999846,
            0.13037292230000008
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
            0.08818465160000023,
            0.04184887480000002,
            0.009925191399999875,
            0.11898575300000011
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
            0.08328934920000028,
            0.046554853000000014,
            0.009218139799999903,
            0.10824708350000013
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
            0.07811586600000033,
            0.05096518550000002,
            0.008459977399999933,
            0.09721478410000016
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
            0.07263787520000037,
            0.05519498470000002,
            0.0077385158999999605,
            0.08598908080000019
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
            0.08626562680000019,
            0.03156440560000003,
            0.013477917999999846,
            0.1279076917000001
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
            0.08174649080000025,
            0.03862514400000003,
            0.012940991899999876,
            0.11663754150000014
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
            0.07923050890000029,
            0.04325240020000003,
            0.012150591999999905,
            0.10565917010000016
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
            0.07639343480000038,
            0.04774145470000003,
            0.011253505599999932,
            0.09449914060000018
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
            0.07107315930000041,
            0.05197125390000003,
            0.01023273539999996,
            0.0835411191000002
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
            0.08483951930000021,
            0.03077110780000003,
            0.016329876499999847,
            0.12527828530000013
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
            0.07985053930000025,
            0.036030396400000025,
            0.015648826399999875,
            0.11426706100000016
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
            0.07196958040000029,
            0.03704730910000005,
            0.014555898299999905,
            0.10310415830000018
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
            0.06782677290000036,
            0.04464394040000005,
            0.013800635899999933,
            0.0922800808000002
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
            0.06248904010000041,
            0.049235631000000044,
            0.01316294219999996,
            0.08114206030000022
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
            0.08789906570000022,
            0.03069339110000004,
            0.018984389699999847,
            0.12299965530000015
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
            0.07608711820000028,
            0.03283969800000004,
            0.018244223399999874,
            0.11171194920000017
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
            0.07154417260000032,
            0.03775012360000004,
            0.017347135499999902,
            0.1007063672000002
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
            0.06236687590000036,
            0.03696636790000006,
            0.01699719529999993,
            0.08969226740000022
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
            0.0571375731000004,
            0.040844315200000064,
            0.01599224039999996,
            0.07985713930000023
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
            0.09333858700000014,
            0.036948790400000014,
            0.009298330599999849,
            0.13245608130000008
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
            0.08791814140000019,
            0.041944903600000014,
            0.008761404499999877,
            0.12110191360000011
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
            0.08331434660000023,
            0.046650881800000016,
            0.007707565799999906,
            0.11004181250000011
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
            0.07784535580000028,
            0.05106121430000002,
            0.0069442033999999354,
            0.09903983390000015
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
            0.07264947260000032,
            0.055291013500000014,
            0.006222841899999963,
            0.08792645350000017
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
            0.09090770320000016,
            0.031764465600000034,
            0.010634864399999852,
            0.13197816560000009
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
            0.0857787652000002,
            0.03882520400000003,
            0.00993398749999988,
            0.1205159592000001
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
            0.08131062840000025,
            0.04345246020000003,
            0.00903939959999991,
            0.10975888520000013
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
            0.07584123760000029,
            0.047941514700000035,
            0.008594651899999937,
            0.09861723280000016
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
            0.07037640560000033,
            0.05217131390000003,
            0.007873290399999965,
            0.08747217290000019
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
            0.08523082180000016,
            0.03107519900000003,
            0.011843816499999854,
            0.1315532429000001
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
            0.08010458290000022,
            0.03633448760000003,
            0.011276417999999882,
            0.12022781030000013
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
            0.07888780340000026,
            0.037351400300000046,
            0.01042211809999991,
            0.10919643240000015
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
            0.0737099202000003,
            0.04494803160000005,
            0.00962134459999994,
            0.09805478000000017
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
            0.06837218740000034,
            0.04953972220000005,
            0.008899983099999969,
            0.0869500421000002
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
            0.08201825040000019,
            0.03110151350000004,
            0.011349021499999857,
            0.1310002901000001
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
            0.07670225200000022,
            0.03324782040000004,
            0.012556849099999885,
            0.11961236450000012
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
            0.07207902800000027,
            0.03800703700000004,
            0.011491316499999914,
            0.10863397960000015
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
            0.07170580200000032,
            0.037652320000000065,
            0.010910390399999942,
            0.09737201750000017
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
            0.06650878960000035,
            0.04124443520000007,
            0.01036799529999997,
            0.08644058230000021
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
            0.09367948470000015,
            0.0382625776,
            0.010133459399999847,
            0.13353139700000008
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
            0.08825903910000019,
            0.0433374128,
            0.009596533299999875,
            0.12231740310000011
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
            0.08365524430000024,
            0.047964669,
            0.008542694599999904,
            0.11121748000000012
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
            0.07818625350000027,
            0.0523750015,
            0.007966568499999932,
            0.10021970140000015
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
            0.07299037030000033,
            0.0566048007,
            0.007245106999999961,
            0.08906220780000017
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
            0.09158949860000015,
            0.036230017499999996,
            0.012021452999999845,
            0.13439215450000008
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
            0.08646056060000021,
            0.0412261307,
            0.011320576099999875,
            0.12309097980000011
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
            0.08183347150000025,
            0.0459321089,
            0.010425988199999904,
            0.11196539050000014
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
            0.07636408070000028,
            0.05034244139999999,
            0.009853162099999932,
            0.10096718980000016
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
            0.07102721030000034,
            0.0545722406,
            0.00913320059999996,
            0.08981081830000018
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
            0.08523082180000016,
            0.0316051535,
            0.013867058599999846,
            0.1351657312000001
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
            0.08010458290000022,
            0.0368644421,
            0.013163481699999875,
            0.12375519570000013
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
            0.07987950580000025,
            0.0441969683,
            0.012492018099999905,
            0.11287321890000016
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
            0.0747016226000003,
            0.04868602279999999,
            0.011736355699999933,
            0.10157492650000018
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
            0.06936388980000034,
            0.052915822,
            0.01102119419999996,
            0.0903858534000002
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
            0.08201825040000019,
            0.03448890440000005,
            0.015626871399999846,
            0.1358863149000001
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
            0.07670225200000022,
            0.033887218,
            0.015082545299999875,
            0.12452397240000014
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
            0.07207902800000027,
            0.038514474199999996,
            0.014368293699999904,
            0.11348095560000016
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
            0.07303840210000032,
            0.04657474069999999,
            0.013612631299999933,
            0.10218266320000019
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
            0.06784138970000037,
            0.0508832619,
            0.01294315779999996,
            0.09099359010000022
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
            0.09446025040000017,
            0.0365783952,
            0.008144028199999846,
            0.13388014890000008
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
            0.0890398048000002,
            0.0415745084,
            0.007424265799999875,
            0.12266615500000011
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
            0.08443601000000026,
            0.0462017646,
            0.006717214199999904,
            0.11156623190000012
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
            0.0789670192000003,
            0.0506120971,
            0.005954251799999932,
            0.10052646590000015
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
            0.07357369510000034,
            0.0548418963,
            0.00523289029999996,
            0.08931733760000017
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
            0.09295408910000019,
            0.03253125030000001,
            0.007992590599999846,
            0.1351246459000001
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
            0.08782515110000025,
            0.03752736350000001,
            0.007272828199999875,
            0.12377047820000012
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
            0.08335701430000028,
            0.04215461970000001,
            0.006561076599999904,
            0.11266289430000015
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
            0.07788762350000034,
            0.04656495220000001,
            0.0057981141999999325,
            0.10148295450000017
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
            0.07255075310000036,
            0.050794751400000004,
            0.00507675269999996,
            0.0904147000000002
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
            0.08632249420000021,
            0.02871029190000001,
            0.007609926899999846,
            0.13621796350000012
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
            0.08119325620000024,
            0.03370640510000001,
            0.007070300799999875,
            0.12483643900000013
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
            0.08218381430000032,
            0.03833366130000001,
            0.006404838999999904,
            0.11375843460000015
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
            0.07700593110000037,
            0.042651767100000015,
            0.005641876599999932,
            0.10257919480000018
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
            0.0716681983000004,
            0.04688156630000001,
            0.00492051509999996,
            0.0913384870000002
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
            0.08201825040000019,
            0.029140028600000013,
            0.007458489299999846,
            0.13732228670000013
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
            0.07815381640000027,
            0.029567033500000013,
            0.006914163199999875,
            0.12592495660000014
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
            0.07353059240000032,
            0.03419428970000001,
            0.006199911599999904,
            0.11485795780000017
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
            0.07612347630000041,
            0.038604622200000015,
            0.005436949199999932,
            0.10353568340000019
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
            0.07092646390000044,
            0.04283442140000002,
            0.00476437749999996,
            0.09229497560000022
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
            0.09605487480000016,
            0.03653040960000001,
            0.008774705799999847,
            0.13240482480000007
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
            0.0909259368000002,
            0.04152652280000001,
            0.008054943399999875,
            0.1211908309000001
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
            0.08603063440000025,
            0.046153779000000006,
            0.007350591799999903,
            0.11009090780000011
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
            0.08085685120000029,
            0.05056411150000001,
            0.006589729399999932,
            0.09904013620000014
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
            0.07537016040000033,
            0.05479391070000001,
            0.0058221669999999615,
            0.08797404250000017
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
            0.09652526590000018,
            0.03243527910000002,
            0.009203945799999846,
            0.13193096310000008
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
            0.09139632790000023,
            0.03743139230000002,
            0.008484183399999875,
            0.1205767954000001
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
            0.08650102550000027,
            0.04205864850000002,
            0.007779831799999904,
            0.10947207230000013
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
            0.08146750030000031,
            0.04646898100000002,
            0.007018969399999932,
            0.09842130070000014
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
            0.07598950950000036,
            0.050698780200000015,
            0.0062514069999999615,
            0.08735520700000017
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
            0.09143875780000017,
            0.028566335100000027,
            0.009633185799999847,
            0.13131692760000008
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
            0.08644977780000021,
            0.033562448300000026,
            0.008913423399999875,
            0.11996025990000012
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
            0.08729473160000029,
            0.03818970450000003,
            0.008209071799999903,
            0.10899341060000013
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
            0.08213483230000033,
            0.04250381150000003,
            0.007448209399999932,
            0.09794221690000016
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
            0.07679709950000038,
            0.046733610700000025,
            0.0066806469999999615,
            0.08687724530000018
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
            0.08895951680000014,
            0.029140028600000013,
            0.010062425799999846,
            0.13070289210000008
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
            0.08513017380000022,
            0.02937109230000004,
            0.009342663399999875,
            0.11944859660000012
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
            0.08020488040000026,
            0.03399834850000004,
            0.008638311799999904,
            0.10851362680000014
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
            0.08292853840000036,
            0.03840868100000004,
            0.007877449399999932,
            0.09732338140000016
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
            0.0774644315000004,
            0.04263848020000004,
            0.0071098869999999615,
            0.08622570820000018
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
            0.09625881360000013,
            0.038029959599999996,
            0.008774705799999847,
            0.13306886030000006
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
            0.09112987560000019,
            0.043026072799999995,
            0.008054943399999875,
            0.1218548664000001
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
            0.08645950570000022,
            0.047653329,
            0.007350591799999903,
            0.11079014490000011
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
            0.08106039000000026,
            0.0520636615,
            0.006589729399999932,
            0.09974167330000014
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
            0.07557359920000031,
            0.0562934607,
            0.0058221669999999615,
            0.08864287800000016
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
            0.09735501690000013,
            0.035471368,
            0.009203945799999846,
            0.13306886030000006
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
            0.09222607890000017,
            0.0404674812,
            0.008484183399999875,
            0.1218548664000001
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
            0.08733077650000022,
            0.0450947374,
            0.007779831799999904,
            0.11079014490000011
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
            0.08229725130000026,
            0.049505069900000004,
            0.007018969399999932,
            0.09974167330000014
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
            0.07681926050000032,
            0.0537348691,
            0.0062514069999999615,
            0.08864287800000016
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
            0.09180164890000014,
            0.033101974,
            0.009633185799999847,
            0.13306886030000006
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
            0.08681266890000018,
            0.0380980872,
            0.008913423399999875,
            0.1218548664000001
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
            0.08855335390000023,
            0.042725343400000004,
            0.008209071799999903,
            0.11079014490000011
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
            0.08339345460000026,
            0.0471356759,
            0.007448209399999932,
            0.09974167330000014
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
            0.07805572180000031,
            0.0513654751,
            0.0066806469999999615,
            0.08864287800000016
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
            0.08895951680000014,
            0.030989473599999998,
            0.010062425799999846,
            0.13306886030000006
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
            0.08558403760000018,
            0.0355394956,
            0.009342663399999875,
            0.1218548664000001
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
            0.08068873520000022,
            0.0401667518,
            0.008638311799999904,
            0.11079014490000011
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
            0.08461603200000027,
            0.0445770843,
            0.007877449399999932,
            0.09974167330000014
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
            0.07915192510000031,
            0.048806883499999995,
            0.0071098869999999615,
            0.08864287800000016
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
            0.09580944620000013,
            0.0389949244,
            0.008774705799999847,
            0.13306886030000006
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
            0.09068050820000018,
            0.0440697596,
            0.008054943399999875,
            0.1218548664000001
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
            0.08578520580000022,
            0.0486970158,
            0.007350591799999903,
            0.11079014490000011
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
            0.08061142260000026,
            0.053107348299999996,
            0.006589729399999932,
            0.09974167330000014
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
            0.07512473180000032,
            0.057337147500000005,
            0.0058221669999999615,
            0.08864287800000016
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
            0.09618533340000013,
            0.0374800196,
            0.009203945799999846,
            0.13306886030000006
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
            0.09105639540000018,
            0.0424761328,
            0.008484183399999875,
            0.1218548664000001
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
            0.08624706720000022,
            0.047182111,
            0.007779831799999904,
            0.11079014490000011
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
            0.08107358400000027,
            0.0515924435,
            0.007018969399999932,
            0.09974167330000014
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
            0.07559589320000032,
            0.0558222427,
            0.0062514069999999615,
            0.08864287800000016
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
            0.09664719480000014,
            0.0361543124,
            0.009633185799999847,
            0.13306886030000006
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
            0.09151825680000018,
            0.0411504256,
            0.008913423399999875,
            0.1218548664000001
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
            0.08662295440000023,
            0.0458564038,
            0.008209071799999903,
            0.11079014490000011
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
            0.08144947120000026,
            0.0502667363,
            0.007448209399999932,
            0.09974167330000014
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
            0.0760577546000003,
            0.0544965355,
            0.0066806469999999615,
            0.08864287800000016
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
            0.09144277160000014,
            0.030989473599999998,
            0.010062425799999846,
            0.13306886030000006
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
            0.09189414400000018,
            0.0396355208,
            0.009342663399999875,
            0.1218548664000001
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
            0.08708481580000023,
            0.044262777,
            0.008638311799999904,
            0.11079014490000011
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
            0.08191133260000028,
            0.048751831499999995,
            0.007877449399999932,
            0.09974167330000014
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
            0.07643364180000031,
            0.052981630700000004,
            0.0071098869999999615,
            0.08864287800000016
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
            0.09615034390000013,
            0.0384498336,
            0.008534777799999846,
            0.13306886030000006
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
            0.09102140590000019,
            0.043445946799999996,
            0.007815015399999875,
            0.1218548664000001
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
            0.08612610350000022,
            0.048073202999999995,
            0.007110663799999904,
            0.11079014490000011
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
            0.08095232030000027,
            0.0524835355,
            0.006349801399999933,
            0.09974167330000014
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
            0.07546562950000031,
            0.0567133347,
            0.005582238999999961,
            0.08864287800000016
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
            0.09686712880000013,
            0.036311116,
            0.008724089799999847,
            0.13306886030000006
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
            0.09173819080000017,
            0.041307229200000004,
            0.008004327399999876,
            0.1218548664000001
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
            0.08692886260000023,
            0.0459344854,
            0.007299975799999903,
            0.11079014490000011
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
            0.08175537940000027,
            0.0503448179,
            0.0065391133999999325,
            0.09974167330000014
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
            0.07627768860000031,
            0.0545746171,
            0.005771550999999962,
            0.08864287800000016
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
            0.09766988790000014,
            0.0343348584,
            0.008913401799999845,
            0.13306886030000006
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
            0.09254094990000018,
            0.0393577092,
            0.008193639399999874,
            0.1218548664000001
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
            0.08764564750000023,
            0.0439849654,
            0.007489287799999904,
            0.11079014490000011
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
            0.08247216430000026,
            0.048395297899999995,
            0.006728425399999932,
            0.09974167330000014
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
            0.0770804477000003,
            0.052625097100000004,
            0.005960862999999961,
            0.08864287800000016
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
            0.09144277160000014,
            0.030989473599999998,
            0.009102713799999846,
            0.13306886030000006
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
            0.09325773480000019,
            0.0372189916,
            0.008382951399999875,
            0.1218548664000001
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
            0.08844840660000022,
            0.0418462478,
            0.007678599799999904,
            0.11079014490000011
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
            0.08327492340000027,
            0.0462565803,
            0.006917737399999933,
            0.09974167330000014
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
            0.0776382803000003,
            0.0504863795,
            0.006150174999999962,
            0.08864287800000016
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
            0.09609536040000013,
            0.0385148816,
            0.008395465799999845,
            0.13306886030000006
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
            0.09096642240000018,
            0.0435109948,
            0.007675703399999874,
            0.1218548664000001
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
            0.08607112000000022,
            0.048138251,
            0.006971351799999904,
            0.11079014490000011
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
            0.08089733680000027,
            0.052548583499999996,
            0.006210489399999933,
            0.09974167330000014
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
            0.0754106460000003,
            0.056778382700000005,
            0.005442926999999961,
            0.08864287800000016
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
            0.09675216330000014,
            0.0365804096,
            0.008395465799999845,
            0.13306886030000006
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
            0.09162322530000018,
            0.0415765228,
            0.007675703399999874,
            0.1218548664000001
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
            0.08681889560000022,
            0.046203779,
            0.006971351799999904,
            0.11079014490000011
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
            0.08164541240000027,
            0.0506141115,
            0.006210489399999933,
            0.09974167330000014
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
            0.07616772160000032,
            0.0548439107,
            0.005442926999999961,
            0.08864287800000016
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
            0.09749993890000014,
            0.0344847316,
            0.008395465799999845,
            0.13306886030000006
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
            0.09237100090000018,
            0.0394808448,
            0.007675703399999874,
            0.1218548664000001
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
            0.08747569850000023,
            0.044108101,
            0.006971351799999904,
            0.11079014490000011
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
            0.08230221530000027,
            0.0485184335,
            0.006210489399999933,
            0.09974167330000014
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
            0.07691549720000032,
            0.052748232699999995,
            0.005442926999999961,
            0.08864287800000016
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
            0.09121284060000014,
            0.0325502596,
            0.008395465799999845,
            0.13306886030000006
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
            0.09302780380000018,
            0.0375463728,
            0.007675703399999874,
            0.1218548664000001
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
            0.08822347410000023,
            0.042173629000000004,
            0.006971351799999904,
            0.11079014490000011
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
            0.08304999090000027,
            0.0465839615,
            0.006210489399999933,
            0.09974167330000014
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
            0.07741334780000031,
            0.0508137607,
            0.005442926999999961,
            0.08864287800000016
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9d664e42f27aebc329cd49abcbde343fb1387af1a9f1e283a7df2b7720569a0b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
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
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e8b7fcf3c2ad7e14ca5c309d4ceea34c37377a944d4e994eec2a8d8c3e9ca776",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a67e3cc74965886bce10ad473e4d8bcf742d60206923755ca556662199841790",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "a5efd00fb61d9b2a1ac35aba15b83ae9e0a19fed8a321553463582b8c2af4d5b",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
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
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f20ba2653807ceb72f7ef55682a53e713c7e7387f3283a836fa7144d92d2d1c9",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.07895621600000025,
            0.04113445870000006,
            0.019427095399999886,
            0.11268601850000015
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
            0.11622306339999999,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.11622306339999999,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.11622306339999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.11622306339999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.11883706790000001,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.11883706790000001,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.11883706790000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.11883706790000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1194989559,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.1194989559,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.1194989559,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1194989559,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.11622306339999999,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.11622306339999999,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.11622306339999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.11622306339999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1184079392,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.1184079392,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.1184079392,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1184079392,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1186977156,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.1186977156,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.1186977156,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1186977156,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.115735611,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.115735611,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.115735611,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.115735611,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1168404691,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.1168404691,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.1168404691,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1168404691,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1168404691,
            0.0253068358,
            0.007482631199999758,
            0.1673710158
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
            0.1168404691,
            0.0253068358,
            0.010118808699999758,
            0.1673710158
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
            0.1168404691,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1168404691,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1230496846,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1230496846,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1230496846,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1230496846,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1273175534,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1273175534,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1273175534,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1273175534,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1284540334,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1284540334,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1284540334,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1284540334,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1230496846,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1230496846,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1230496846,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1230496846,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1265583257,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1265583257,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1265583257,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1265583257,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1270746197,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1270746197,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1270746197,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1270746197,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1218844165,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1218844165,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1218844165,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1218844165,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1237444818,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1237444818,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1237444818,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1237444818,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1237444818,
            0.024604538199999998,
            0.004845006599999758,
            0.1673710158
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
            0.1237444818,
            0.024604538199999998,
            0.010118808699999758,
            0.1673710158
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
            0.1237444818,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1237444818,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1295979161,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.1295979161,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.1295979161,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1295979161,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.13455232220000002,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.13455232220000002,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.13455232220000002,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.13455232220000002,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1359152982,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.1359152982,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.1359152982,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1359152982,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1295979161,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.1295979161,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.1295979161,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1295979161,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1335950351,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.1335950351,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.1335950351,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1335950351,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1342137879,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.1342137879,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.1342137879,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1342137879,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.12791218570000001,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.12791218570000001,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.12791218570000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.12791218570000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.12996885390000001,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.12996885390000001,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.12996885390000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.12996885390000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.12996885390000001,
            0.023931503,
            0.0023088290999997577,
            0.1673710158
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
            0.12996885390000001,
            0.023931503,
            0.010118808699999758,
            0.1673710158
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
            0.12996885390000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.12996885390000001,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "3de7c13e774d534c952c8462bc02d4706ba6c2da63098dcc633d9891959119c9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13623417399999999,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.13623417399999999,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.13623417399999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.13623417399999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "1424ccb6f148503ef949aaec1c140dfeedf287a16154036803144b75c5de03c2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14123430380000002,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.14123430380000002,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.14123430380000002,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.14123430380000002,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "d352ec1510356ccb70944864be43f48121546077644fccd6d3b4ebe46472fbb3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1425973798,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.1425973798,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.1425973798,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1425973798,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "9b43cfb13d4e03c1d855e2b81d3146f84cdd7f6155194208cff59649e4fafedd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13623417399999999,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.13623417399999999,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.13623417399999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.13623417399999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "05063fd72167d3a3a2da97e7c8c63023ebe7fe845967932f2a3a68b2d9023574",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1402909272,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.1402909272,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.1402909272,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1402909272,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "76c2fdbf72a6ee26af1f5ea026eca75afdfcee1086f79c917047a7c7ab3c01ed",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14090968,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.14090968,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.14090968,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.14090968,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0165967a82c576ce3dbbcae3a03db3d0b9766a1b6ba0de5459235753d980e642",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1340609912,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.1340609912,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.1340609912,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.1340609912,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "81f56cf56a5de341c5d98c82cf7d5803225386e334d2d1d583526e9c4ea5e855",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13603265009999999,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.13603265009999999,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.13603265009999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.13603265009999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f20359ca6d891690d890c115b86a566a971340c2017016139abfe828870ecff8",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13603265009999999,
            0.0232292054,
            -0.0003287955000002424,
            0.1673710158
          ],
          "positive_window_share": 0.75
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
            0.13603265009999999,
            0.0232292054,
            0.010118808699999758,
            0.1673710158
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
            0.13603265009999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
            0.13603265009999999,
            0.026029871,
            0.010118808699999758,
            0.1673710158
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
        "510300.SH"
      ]
    },
    "experiment_hash": "1fd9093c4bc0ff6020c7397b3d9b80f4b446f016d8fdb6fd6e6d9e3d1f7e45a6",
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
            "cost_drag": 0.0008489211,
            "cvar5_improvement": 0.018467957298539343,
            "drawdown_improvement": 0.1410093399818579,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.021185780778108537,
            "sortino_excess": 0.4050173952257579,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012805254500000002,
            "cvar5_improvement": 0.018357671179489343,
            "drawdown_improvement": 0.13893084516674206,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.12924698265095189,
            "sortino_excess": 0.5950785037750881,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00130108245,
            "cvar5_improvement": 0.013875523683464414,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23399671674323486,
            "sortino_excess": 0.6213225859600192,
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
            "cost_drag": 0.0007687235250000001,
            "cvar5_improvement": 0.018578085045724547,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.17381548106258868,
            "sortino_excess": 0.558954089429704,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0028612957749999997,
            "cvar5_improvement": 0.011205394198892063,
            "drawdown_improvement": 0.09554037086306938,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21360513963654992,
            "sortino_excess": 0.7239163265553246,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015407921999999999,
            "cvar5_improvement": 0.012306980508003534,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23654058809038833,
            "sortino_excess": 0.6284082527138224,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00144311335,
            "cvar5_improvement": 0.01220082884274325,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25028122520243923,
            "sortino_excess": 0.6302409011000946,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
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
            "cost_drag": 0.0023510984250000003,
            "cvar5_improvement": 0.015327229524470805,
            "drawdown_improvement": 0.12177277493540314,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2285661415615901,
            "sortino_excess": 0.8657384267056625,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001358034825,
            "cvar5_improvement": 0.01376511468473933,
            "drawdown_improvement": 0.11064819993789554,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20754670210815424,
            "sortino_excess": 0.5964983511865488,
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
            "cost_drag": 0.002149685825,
            "cvar5_improvement": 0.013900587410993051,
            "drawdown_improvement": 0.10990255633115886,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.12258518476554378,
            "sortino_excess": 0.6339518883481325,
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
            "cost_drag": 0.0012537698000000001,
            "cvar5_improvement": 0.013876129943476641,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23050240375531886,
            "sortino_excess": 0.61543592357032,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011273756000000001,
            "cvar5_improvement": 0.016845113994442752,
            "drawdown_improvement": 0.13080946565323878,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2773369200993426,
            "sortino_excess": 0.6620789866358672,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0011269602999999999,
            "cvar5_improvement": 0.015516966835837868,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23059592652318803,
            "sortino_excess": 0.6383830115648932,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001483289,
            "cvar5_improvement": 0.01222586388608847,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2513327631899991,
            "sortino_excess": 0.6327951846570226,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014983000749999999,
            "cvar5_improvement": 0.018058039039628285,
            "drawdown_improvement": 0.13745955866111786,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3461699301495327,
            "sortino_excess": 0.8965536304940659,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012900551250000002,
            "cvar5_improvement": 0.013813907785063329,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.256271616773711,
            "sortino_excess": 0.6451097208297875,
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
            "cost_drag": 0.001289976675,
            "cvar5_improvement": 0.01381411830621038,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24696612674742197,
            "sortino_excess": 0.629516939956601,
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
            "cost_drag": 0.0013127848,
            "cvar5_improvement": 0.01499813723860001,
            "drawdown_improvement": 0.11758337630537796,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1364389039047886,
            "sortino_excess": 0.512853336833369,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016583512250000002,
            "cvar5_improvement": 0.01207188595566853,
            "drawdown_improvement": 0.10052906243260593,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.28153015337832576,
            "sortino_excess": 0.6605689767455256,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020720103,
            "cvar5_improvement": 0.013874447108079052,
            "drawdown_improvement": 0.11072973736546168,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16696869490956143,
            "sortino_excess": 0.6455893928154259,
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
            "cost_drag": 0.00168602295,
            "cvar5_improvement": 0.015324949774252656,
            "drawdown_improvement": 0.11817092437822227,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18181715452804437,
            "sortino_excess": 0.6276869102656348,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001000995325,
            "cvar5_improvement": 0.01690683453041062,
            "drawdown_improvement": 0.13068868724736268,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.06193953506741615,
            "sortino_excess": 0.469946334486332,
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
            "cost_drag": 0.0021656956249999997,
            "cvar5_improvement": 0.012206520833044843,
            "drawdown_improvement": 0.1007453128787428,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23104899375837257,
            "sortino_excess": 0.635520735823145,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013292317,
            "cvar5_improvement": 0.013814932341129594,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24259962631471468,
            "sortino_excess": 0.6294090202194348,
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
            "cost_drag": 0.002060054275,
            "cvar5_improvement": 0.012297958561556143,
            "drawdown_improvement": 0.09955633683450424,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2014074155940186,
            "sortino_excess": 0.6386495507004923,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001093193875,
            "cvar5_improvement": 0.015258959796423785,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2547251769642409,
            "sortino_excess": 0.6339365931100784,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002548544475,
            "cvar5_improvement": 0.013813408334786299,
            "drawdown_improvement": 0.11222882383615773,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.17473389489883967,
            "sortino_excess": 0.7818707571568507,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001423430625,
            "cvar5_improvement": 0.016936700189566875,
            "drawdown_improvement": 0.13014965766140696,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.169167487995169,
            "sortino_excess": 0.6175301142827736,
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
            "cost_drag": 0.0012166675,
            "cvar5_improvement": 0.015179364731790415,
            "drawdown_improvement": 0.12018769725801767,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25316825972953616,
            "sortino_excess": 0.6178240228148041,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001312650975,
            "cvar5_improvement": 0.013941157254184863,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23974553161142853,
            "sortino_excess": 0.6432510254346414,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010230314,
            "cvar5_improvement": 0.018378638480072346,
            "drawdown_improvement": 0.13988608215208836,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21239692946610916,
            "sortino_excess": 0.6488021270992296,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001974066475,
            "cvar5_improvement": 0.01377482007516132,
            "drawdown_improvement": 0.11073562127149697,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22401101176765445,
            "sortino_excess": 0.6336411969363429,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001530879325,
            "cvar5_improvement": 0.015351782441141649,
            "drawdown_improvement": 0.12033239561889356,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2520370710082895,
            "sortino_excess": 0.6352041338216773,
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
            "cost_drag": 0.0016952809999999999,
            "cvar5_improvement": 0.01193709727731429,
            "drawdown_improvement": 0.09832482583409913,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2355377161817903,
            "sortino_excess": 0.6036359861585405,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0029100266499999996,
            "cvar5_improvement": 0.012129758328343334,
            "drawdown_improvement": 0.09954782154487976,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.11853771269030572,
            "sortino_excess": 0.6801542891645237,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016605906,
            "cvar5_improvement": 0.016968505005595033,
            "drawdown_improvement": 0.1304232325588719,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.10332034915143143,
            "sortino_excess": 0.6081532293788291,
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
            "cost_drag": 0.0009664612,
            "cvar5_improvement": 0.01701266660527685,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.12876765254248043,
            "sortino_excess": 0.530015438369609,
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
            "cost_drag": 0.00117207815,
            "cvar5_improvement": 0.015337319625522964,
            "drawdown_improvement": 0.12077913188742825,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19023388132680086,
            "sortino_excess": 0.5835614944219667,
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
            "cost_drag": 0.00230013345,
            "cvar5_improvement": 0.012307059748827334,
            "drawdown_improvement": 0.10071721247791562,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1954410082911454,
            "sortino_excess": 0.6534123966006103,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000978174025,
            "cvar5_improvement": 0.017062687279042112,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21487716379164085,
            "sortino_excess": 0.625217491998033,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018115273,
            "cvar5_improvement": 0.012104020831963897,
            "drawdown_improvement": 0.10047862455204484,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2636677239407078,
            "sortino_excess": 0.6396928726509954,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009558192249999999,
            "cvar5_improvement": 0.016952126596370083,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22426951831083414,
            "sortino_excess": 0.6087670595564366,
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
            "cost_drag": 0.0007867678499999999,
            "cvar5_improvement": 0.018589600730446448,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.02573048851518878,
            "sortino_excess": 0.4011769930390327,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016449833749999998,
            "cvar5_improvement": 0.012014910531139289,
            "drawdown_improvement": 0.09918961296374659,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2485598596692314,
            "sortino_excess": 0.6144497042680435,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014945188999999999,
            "cvar5_improvement": 0.012306980508003534,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25304505927972915,
            "sortino_excess": 0.6466160920423241,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0028890811250000003,
            "cvar5_improvement": 0.011016351416047782,
            "drawdown_improvement": 0.09334898285887591,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1194568755535017,
            "sortino_excess": 0.6265833201043602,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00164736335,
            "cvar5_improvement": 0.01370167296405661,
            "drawdown_improvement": 0.10957719886290399,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3225219011498599,
            "sortino_excess": 0.7404013825686826,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001072072725,
            "cvar5_improvement": 0.015512467129568677,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20490008937481569,
            "sortino_excess": 0.5957190234460225,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010200911500000001,
            "cvar5_improvement": 0.01691638757021771,
            "drawdown_improvement": 0.13060428316364595,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.014330236593279547,
            "sortino_excess": 0.4146945834423539,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008256378499999999,
            "cvar5_improvement": 0.018459994313763873,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22331565667365705,
            "sortino_excess": 0.6024486993810478,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016379274750000002,
            "cvar5_improvement": 0.016905532096189314,
            "drawdown_improvement": 0.13089097101785913,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18575548728019714,
            "sortino_excess": 0.6216066312226397,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019136085249999999,
            "cvar5_improvement": 0.0122075836325162,
            "drawdown_improvement": 0.10041960284703308,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2530579161664215,
            "sortino_excess": 0.6412678864635528,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001446401175,
            "cvar5_improvement": 0.016709637965229625,
            "drawdown_improvement": 0.12789331994295539,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.17640309682884592,
            "sortino_excess": 0.5918161799040239,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002338256025,
            "cvar5_improvement": 0.012393890538088332,
            "drawdown_improvement": 0.10038448659904858,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13912001734087984,
            "sortino_excess": 0.6264313276163489,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001403264175,
            "cvar5_improvement": 0.013583766180952228,
            "drawdown_improvement": 0.1100660421394869,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2560204616375815,
            "sortino_excess": 0.6223277513269367,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0011046055,
            "cvar5_improvement": 0.01539080920444004,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2394530027817294,
            "sortino_excess": 0.623679281878054,
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
            "cost_drag": 0.0012574439,
            "cvar5_improvement": 0.013936828289272136,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21748407307522116,
            "sortino_excess": 0.6059728735385579,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013387329,
            "cvar5_improvement": 0.015298563017858133,
            "drawdown_improvement": 0.12040849830748795,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29532406264427147,
            "sortino_excess": 0.6944318875972089,
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
            "cost_drag": 0.00197007985,
            "cvar5_improvement": 0.01740672534651511,
            "drawdown_improvement": 0.135213041024925,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14273645869848478,
            "sortino_excess": 0.7657577296010063,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012788819,
            "cvar5_improvement": 0.016869996065426524,
            "drawdown_improvement": 0.13073084634343773,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24667942511225438,
            "sortino_excess": 0.6245921744225751,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002060022075,
            "cvar5_improvement": 0.012247801241924391,
            "drawdown_improvement": 0.09881840634275066,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21286009957349936,
            "sortino_excess": 0.5991293459949801,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001113517425,
            "cvar5_improvement": 0.016702846543805036,
            "drawdown_improvement": 0.12935735596427866,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22003883886758507,
            "sortino_excess": 0.5874216635618387,
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
            "cost_drag": 0.0017451630749999998,
            "cvar5_improvement": 0.011863624712912154,
            "drawdown_improvement": 0.09745995340693794,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2230434677315799,
            "sortino_excess": 0.59557820361595,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0010644298499999998,
            "cvar5_improvement": 0.015376412343497473,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23800880397141083,
            "sortino_excess": 0.6205740789433254,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001527152525,
            "cvar5_improvement": 0.01207737959484224,
            "drawdown_improvement": 0.10073678663175234,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24668368005495714,
            "sortino_excess": 0.6264602610364635,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00184233875,
            "cvar5_improvement": 0.013832148163783461,
            "drawdown_improvement": 0.10999856517206083,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23802274365307213,
            "sortino_excess": 0.6628738726770929,
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
            "cost_drag": 0.0024338845,
            "cvar5_improvement": 0.012415941463657936,
            "drawdown_improvement": 0.09943626253549886,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1596912828805486,
            "sortino_excess": 0.6592486293831034,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012262257499999999,
            "cvar5_improvement": 0.01678192906036359,
            "drawdown_improvement": 0.1290775571810817,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22457124263009673,
            "sortino_excess": 0.667371148684392,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015059633,
            "cvar5_improvement": 0.012372648115067808,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.244747150153096,
            "sortino_excess": 0.6447816383504062,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002368802475,
            "cvar5_improvement": 0.014341076254265991,
            "drawdown_improvement": 0.11561560933950324,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1657238280562414,
            "sortino_excess": 0.7327067962944106,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001246201925,
            "cvar5_improvement": 0.013640653650548767,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25892213214881465,
            "sortino_excess": 0.6362325772543599,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00261551095,
            "cvar5_improvement": 0.014654682451969173,
            "drawdown_improvement": 0.11797252421083751,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25230600872520736,
            "sortino_excess": 0.9603472817234204,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002081155675,
            "cvar5_improvement": 0.012395192149824704,
            "drawdown_improvement": 0.09911749871258574,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13591237601616507,
            "sortino_excess": 0.5601522920264705,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0007593661000000001,
            "cvar5_improvement": 0.018589600730446448,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.047733875294356604,
            "sortino_excess": 0.41884124250354754,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012800972250000002,
            "cvar5_improvement": 0.018158759859055233,
            "drawdown_improvement": 0.13773864193179547,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.27040143612815737,
            "sortino_excess": 0.703938224079648,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002195455325,
            "cvar5_improvement": 0.016779189355912077,
            "drawdown_improvement": 0.1314447777160032,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.234626558529824,
            "sortino_excess": 0.9443483527274609,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001066289175,
            "cvar5_improvement": 0.01676542070474307,
            "drawdown_improvement": 0.1302616391662789,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24113310513549585,
            "sortino_excess": 0.6038056965955833,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013987949,
            "cvar5_improvement": 0.015283193003354314,
            "drawdown_improvement": 0.120146217213662,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.31528633423257013,
            "sortino_excess": 0.7269350378462166,
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
            "cost_drag": 0.001522619025,
            "cvar5_improvement": 0.012243760390898894,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2473647250469983,
            "sortino_excess": 0.6322733525950219,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00112777535,
            "cvar5_improvement": 0.018447392734850885,
            "drawdown_improvement": 0.14104935854024675,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23407891624081145,
            "sortino_excess": 0.6079485649896804,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001360397975,
            "cvar5_improvement": 0.01684876330014298,
            "drawdown_improvement": 0.1290844403778033,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20225583664263738,
            "sortino_excess": 0.600750514807366,
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
            "cost_drag": 0.001523754175,
            "cvar5_improvement": 0.013735377848441524,
            "drawdown_improvement": 0.11027917846602944,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29316931334640317,
            "sortino_excess": 0.6869357689193369,
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
            "cost_drag": 0.00081583435,
            "cvar5_improvement": 0.018577976101668683,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20708674943252015,
            "sortino_excess": 0.6124452457064259,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017146052249999999,
            "cvar5_improvement": 0.01217850416864604,
            "drawdown_improvement": 0.10028113496034319,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29172892493603986,
            "sortino_excess": 0.682620257944801,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019305813000000001,
            "cvar5_improvement": 0.015406118716033016,
            "drawdown_improvement": 0.1194821345763395,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.143620810688842,
            "sortino_excess": 0.6621117583878897,
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
            "cost_drag": 0.001616570825,
            "cvar5_improvement": 0.013697452985221872,
            "drawdown_improvement": 0.11051237651399393,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2584804146933672,
            "sortino_excess": 0.6343059455655603,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027515272749999995,
            "cvar5_improvement": 0.013428121638479593,
            "drawdown_improvement": 0.10880957900522656,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20706388656351168,
            "sortino_excess": 0.8120189198435275,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001494401225,
            "cvar5_improvement": 0.012306980508003534,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2409007777936169,
            "sortino_excess": 0.6261962003026501,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00138420515,
            "cvar5_improvement": 0.01378592878893159,
            "drawdown_improvement": 0.11052845568415842,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1766782676587132,
            "sortino_excess": 0.5759869102241302,
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
            "cost_drag": 0.00119874305,
            "cvar5_improvement": 0.015354349279907873,
            "drawdown_improvement": 0.12065948859739409,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.15638389043175824,
            "sortino_excess": 0.5620883076970948,
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
            "cost_drag": 0.00150644645,
            "cvar5_improvement": 0.012099942638093827,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2595652229197809,
            "sortino_excess": 0.6383637884102611,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001315035375,
            "cvar5_improvement": 0.015077743263137336,
            "drawdown_improvement": 0.11850339123084372,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21787707319151733,
            "sortino_excess": 0.5914083494396817,
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
            "cost_drag": 0.001249801025,
            "cvar5_improvement": 0.01379273466013708,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2457295454672625,
            "sortino_excess": 0.6266735155624348,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001366662925,
            "cvar5_improvement": 0.013941157254184863,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2171822791653834,
            "sortino_excess": 0.6184338092796826,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00111582895,
            "cvar5_improvement": 0.015451368198643903,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2409432721382735,
            "sortino_excess": 0.6424843512955953,
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
            "cost_drag": 0.0009783366250000001,
            "cvar5_improvement": 0.017062687279042112,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1869790864272804,
            "sortino_excess": 0.5771699202499608,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018873872249999999,
            "cvar5_improvement": 0.016693922591048235,
            "drawdown_improvement": 0.1276448722204292,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22544116124771527,
            "sortino_excess": 0.7885550549274525,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001310859125,
            "cvar5_improvement": 0.013689766815127489,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25646136556563126,
            "sortino_excess": 0.6360497965368525,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001774782825,
            "cvar5_improvement": 0.012161058709990144,
            "drawdown_improvement": 0.09998715798542712,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30378602117144893,
            "sortino_excess": 0.710470399540502,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001068398625,
            "cvar5_improvement": 0.015451843393892703,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22001517813221144,
            "sortino_excess": 0.6072653246269933,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015030302749999998,
            "cvar5_improvement": 0.01350121564380653,
            "drawdown_improvement": 0.10833599739275743,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22847283402676483,
            "sortino_excess": 0.597975289044197,
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
            "cost_drag": 0.0026365142000000005,
            "cvar5_improvement": 0.012760802365335078,
            "drawdown_improvement": 0.10542826110848094,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19264272949572117,
            "sortino_excess": 0.7265274858968244,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002736207,
            "cvar5_improvement": 0.01234581600358364,
            "drawdown_improvement": 0.1027090492229597,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13937482724039185,
            "sortino_excess": 0.7107884419529451,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00096280355,
            "cvar5_improvement": 0.01818254859846186,
            "drawdown_improvement": 0.13877026743145562,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.08424444606443357,
            "sortino_excess": 0.47094267941422674,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001428821,
            "cvar5_improvement": 0.015288676292411891,
            "drawdown_improvement": 0.12063517251943365,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2553724775321339,
            "sortino_excess": 0.6311159637030064,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013802848000000001,
            "cvar5_improvement": 0.015265129430283278,
            "drawdown_improvement": 0.11939248420075055,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24091168101147672,
            "sortino_excess": 0.6594232243232867,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001453811575,
            "cvar5_improvement": 0.013573738736616594,
            "drawdown_improvement": 0.10916597714735449,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24214233116401201,
            "sortino_excess": 0.6069578565436619,
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
            "cost_drag": 0.00080492395,
            "cvar5_improvement": 0.01852777763797626,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20196709436799185,
            "sortino_excess": 0.5848940543956535,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00157782205,
            "cvar5_improvement": 0.012216135848800741,
            "drawdown_improvement": 0.10046265876399213,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19346613700507737,
            "sortino_excess": 0.5891205529200488,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002261762,
            "cvar5_improvement": 0.013839042724896574,
            "drawdown_improvement": 0.10854592454652778,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1355490728184099,
            "sortino_excess": 0.6711421139704733,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00115873025,
            "cvar5_improvement": 0.016524262380055454,
            "drawdown_improvement": 0.12760976591041548,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.09160898546442633,
            "sortino_excess": 0.4823980696244333,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002220003475,
            "cvar5_improvement": 0.014814873267819231,
            "drawdown_improvement": 0.11823430508641672,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20226063991692567,
            "sortino_excess": 0.6509382261904832,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001174797075,
            "cvar5_improvement": 0.016824081096681584,
            "drawdown_improvement": 0.12997941048030232,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23431392597815068,
            "sortino_excess": 0.6461237004630261,
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
            "cost_drag": 0.000976533125,
            "cvar5_improvement": 0.01687636588447186,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23999528201961118,
            "sortino_excess": 0.620140287145279,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0007932384999999999,
            "cvar5_improvement": 0.018452518449482955,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23748340197945728,
            "sortino_excess": 0.6186304033203198,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000962958925,
            "cvar5_improvement": 0.0180147948710776,
            "drawdown_improvement": 0.13786596810319704,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.09988783324222456,
            "sortino_excess": 0.49197237751863737,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008275068500000001,
            "cvar5_improvement": 0.01843674178186675,
            "drawdown_improvement": 0.14085584513198934,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.03282939690854204,
            "sortino_excess": 0.4114347657186437,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00219693405,
            "cvar5_improvement": 0.01588210721313494,
            "drawdown_improvement": 0.12547977007504105,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14622361185467905,
            "sortino_excess": 0.742130050540911,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011146224000000001,
            "cvar5_improvement": 0.01662531982971468,
            "drawdown_improvement": 0.12851762394550933,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13974634352212584,
            "sortino_excess": 0.512737131215116,
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
            "cost_drag": 0.001278679275,
            "cvar5_improvement": 0.013658120148237946,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26444345066751723,
            "sortino_excess": 0.6457823004057756,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000955578175,
            "cvar5_improvement": 0.016952126596370083,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23712927198495032,
            "sortino_excess": 0.6311428762921307,
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
            "cost_drag": 0.0014117101250000002,
            "cvar5_improvement": 0.013807623184338738,
            "drawdown_improvement": 0.11037378129288591,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14647831128193967,
            "sortino_excess": 0.5544708992127273,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000911975925,
            "cvar5_improvement": 0.016834434954945174,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24349709523105834,
            "sortino_excess": 0.6199102095552558,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002600340625,
            "cvar5_improvement": 0.011660071239599112,
            "drawdown_improvement": 0.09811598222714066,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22878545985351964,
            "sortino_excess": 0.6531965065463581,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0016170548750000001,
            "cvar5_improvement": 0.015395734289563121,
            "drawdown_improvement": 0.12012509435748228,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21170301087103244,
            "sortino_excess": 0.6478402621657016,
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
            "cost_drag": 0.00146334145,
            "cvar5_improvement": 0.013664654395718415,
            "drawdown_improvement": 0.11057387591755671,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.279235585822284,
            "sortino_excess": 0.6595087786415681,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0010932331,
            "cvar5_improvement": 0.015258855497765353,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26024348376366263,
            "sortino_excess": 0.6431536285716403,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009156431999999999,
            "cvar5_improvement": 0.016946664223878093,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.222666920900426,
            "sortino_excess": 0.60554962098255,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000916017,
            "cvar5_improvement": 0.018346853019502823,
            "drawdown_improvement": 0.1405358318396703,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2294108995213062,
            "sortino_excess": 0.586370158477185,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001721269425,
            "cvar5_improvement": 0.013777893885734105,
            "drawdown_improvement": 0.11042704686229654,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2502560152768142,
            "sortino_excess": 0.6397204976682167,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013312655999999999,
            "cvar5_improvement": 0.01367011686769623,
            "drawdown_improvement": 0.11080287432916805,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23947256116618776,
            "sortino_excess": 0.6200703232117631,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00162523615,
            "cvar5_improvement": 0.015402479273504743,
            "drawdown_improvement": 0.11931907722595586,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1215338477085304,
            "sortino_excess": 0.5609001459019158,
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
            "cost_drag": 0.00144708895,
            "cvar5_improvement": 0.012307712808654272,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23785378834285387,
            "sortino_excess": 0.6208579461910285,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018688651749999999,
            "cvar5_improvement": 0.013866733900444957,
            "drawdown_improvement": 0.10962349820220985,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18369552561113286,
            "sortino_excess": 0.6322798821246332,
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
            "cost_drag": 0.0020660262,
            "cvar5_improvement": 0.016368009978826245,
            "drawdown_improvement": 0.1282363605134162,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18223464477315438,
            "sortino_excess": 0.6563940757064217,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009667296249999999,
            "cvar5_improvement": 0.01701266660527685,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22714541720077583,
            "sortino_excess": 0.6312697881219578,
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
            "cost_drag": 0.0008441749249999999,
            "cvar5_improvement": 0.01852777763797626,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19558046662267162,
            "sortino_excess": 0.58902348514981,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0007610806499999999,
            "cvar5_improvement": 0.018443096552747226,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22794009258277037,
            "sortino_excess": 0.6017385746947732,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001719563425,
            "cvar5_improvement": 0.013778472453984208,
            "drawdown_improvement": 0.11016521676403873,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25923217937870646,
            "sortino_excess": 0.6431106284424656,
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
            "cost_drag": 0.00203938825,
            "cvar5_improvement": 0.01530847499920208,
            "drawdown_improvement": 0.11818513917195217,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23207374994158442,
            "sortino_excess": 0.7615120922225356,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001312494075,
            "cvar5_improvement": 0.013941157254184863,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2207851008738839,
            "sortino_excess": 0.6109082882593168,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0007866535500000001,
            "cvar5_improvement": 0.018589600730446448,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.00046561115460782426,
            "sortino_excess": 0.38971875188306343,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00096693145,
            "cvar5_improvement": 0.01701266660527685,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2070087123073886,
            "sortino_excess": 0.5960777981375047,
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
            "cost_drag": 0.0008703592000000001,
            "cvar5_improvement": 0.018460650460011316,
            "drawdown_improvement": 0.1411628348317265,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.12748930626279875,
            "sortino_excess": 0.5302216032247743,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014330169000000002,
            "cvar5_improvement": 0.01689658844935922,
            "drawdown_improvement": 0.12906743587059277,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18306869071232623,
            "sortino_excess": 0.6205243753027423,
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
            "cost_drag": 0.0018703402,
            "cvar5_improvement": 0.013768382299212067,
            "drawdown_improvement": 0.1084617861124842,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20011699517215498,
            "sortino_excess": 0.5905600449559598,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000815555425,
            "cvar5_improvement": 0.018577976101668683,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.06984320905779212,
            "sortino_excess": 0.47868916618234464,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001145244425,
            "cvar5_improvement": 0.015271206954191183,
            "drawdown_improvement": 0.1209338121453431,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2302644099644848,
            "sortino_excess": 0.6123450943365848,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018469646,
            "cvar5_improvement": 0.015448363040741037,
            "drawdown_improvement": 0.12081533629547306,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1333511630888579,
            "sortino_excess": 0.6284246179748735,
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
            "cost_drag": 0.0011706808,
            "cvar5_improvement": 0.015380494884605661,
            "drawdown_improvement": 0.12053956483424966,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.04929260644540414,
            "sortino_excess": 0.46319560434692353,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00159901785,
            "cvar5_improvement": 0.011985151287935602,
            "drawdown_improvement": 0.10000835059074079,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26055730176885017,
            "sortino_excess": 0.6277502261542609,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0007647479250000001,
            "cvar5_improvement": 0.01852291258745534,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20036318662445113,
            "sortino_excess": 0.5825084443623031,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020132389749999997,
            "cvar5_improvement": 0.01223870274552657,
            "drawdown_improvement": 0.09988418790304487,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25741308547748937,
            "sortino_excess": 0.6471943068572534,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010308874,
            "cvar5_improvement": 0.0182543170004287,
            "drawdown_improvement": 0.1389866156269541,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3295430216314637,
            "sortino_excess": 0.777825421313667,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013012001250000001,
            "cvar5_improvement": 0.013875523683464414,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24804116445872115,
            "sortino_excess": 0.6451599503612881,
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
            "cost_drag": 0.001162744175,
            "cvar5_improvement": 0.015451368198643903,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2192944532233908,
            "sortino_excess": 0.6182783780486213,
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
            "cost_drag": 0.0014507443,
            "cvar5_improvement": 0.012368483311011216,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22467247168658522,
            "sortino_excess": 0.6111707393048004,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00112648675,
            "cvar5_improvement": 0.015516966835837868,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1229468866498705,
            "sortino_excess": 0.5297268757814321,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001476452575,
            "cvar5_improvement": 0.01847334170777448,
            "drawdown_improvement": 0.14015343764310828,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.10017786701007841,
            "sortino_excess": 0.6238469894672953,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000977706925,
            "cvar5_improvement": 0.017062687279042112,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.08043650114063967,
            "sortino_excess": 0.4926764454007034,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00110468395,
            "cvar5_improvement": 0.01539080920444004,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25057425796320615,
            "sortino_excess": 0.6425048024756843,
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
            "cost_drag": 0.0009620787,
            "cvar5_improvement": 0.01827864046292855,
            "drawdown_improvement": 0.13967737328471416,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19516790805031403,
            "sortino_excess": 0.5662862450630852,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003005060975,
            "cvar5_improvement": 0.0110549570153687,
            "drawdown_improvement": 0.09220458840630641,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1122291697153403,
            "sortino_excess": 0.6195896610759253,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015857841250000002,
            "cvar5_improvement": 0.01535965779701889,
            "drawdown_improvement": 0.11943257584457542,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20507821825389136,
            "sortino_excess": 0.592628058669638,
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
            "cost_drag": 0.001034191775,
            "cvar5_improvement": 0.018420437836965047,
            "drawdown_improvement": 0.14080259867722256,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2987327736048118,
            "sortino_excess": 0.7105194467822418,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009950701999999999,
            "cvar5_improvement": 0.016952126596370083,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21821967185902225,
            "sortino_excess": 0.6105910904841576,
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
            "cost_drag": 0.0009196187999999999,
            "cvar5_improvement": 0.017013011109292153,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20213148804855147,
            "sortino_excess": 0.5894863888438766,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001125329825,
            "cvar5_improvement": 0.015293737164936788,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2523724398315977,
            "sortino_excess": 0.6334513440892218,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00094441405,
            "cvar5_improvement": 0.016847037879691665,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24486008510149773,
            "sortino_excess": 0.6226430143776381,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016008823999999998,
            "cvar5_improvement": 0.015273196135934714,
            "drawdown_improvement": 0.1182244562952573,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20138367895783532,
            "sortino_excess": 0.6028504997006783,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001185660875,
            "cvar5_improvement": 0.016846003053549885,
            "drawdown_improvement": 0.13043831288711177,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2967357285414822,
            "sortino_excess": 0.7082445872880998,
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
            "cost_drag": 0.00126657145,
            "cvar5_improvement": 0.015145061901571666,
            "drawdown_improvement": 0.11932275666848582,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23703216280505096,
            "sortino_excess": 0.6019539502239161,
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
            "cost_drag": 0.0015309754750000002,
            "cvar5_improvement": 0.016748283897263412,
            "drawdown_improvement": 0.1278009298498082,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14683739131877582,
            "sortino_excess": 0.6151918016300714,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015863779,
            "cvar5_improvement": 0.018319021365133522,
            "drawdown_improvement": 0.1388500420201168,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20014458419500272,
            "sortino_excess": 0.7575710318106835,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002305890975,
            "cvar5_improvement": 0.016059501203825818,
            "drawdown_improvement": 0.12754012128230055,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36989768235835196,
            "sortino_excess": 1.093526812893787,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000793518775,
            "cvar5_improvement": 0.01845257305334966,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2296861707127557,
            "sortino_excess": 0.605049011863328,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015542899,
            "cvar5_improvement": 0.013421257251066795,
            "drawdown_improvement": 0.1074237349506249,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21294003468057696,
            "sortino_excess": 0.5883476471913835,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001115711275,
            "cvar5_improvement": 0.015451368198643903,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22411049611633993,
            "sortino_excess": 0.6136149620393377,
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
            "cost_drag": 0.0015517467500000002,
            "cvar5_improvement": 0.012192654315373443,
            "drawdown_improvement": 0.10058211806028869,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21913802354680298,
            "sortino_excess": 0.6058668000250738,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0011271229,
            "cvar5_improvement": 0.015516966835837868,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20860071318787657,
            "sortino_excess": 0.6002426596198863,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001384354975,
            "cvar5_improvement": 0.016896771763070768,
            "drawdown_improvement": 0.13058220805156256,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.226460720157381,
            "sortino_excess": 0.6271876954250607,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0015346162999999998,
            "cvar5_improvement": 0.01534738432095165,
            "drawdown_improvement": 0.12056590488888472,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2430423751179553,
            "sortino_excess": 0.6371882437424468,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015057944749999998,
            "cvar5_improvement": 0.012372648115067808,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22758057496545742,
            "sortino_excess": 0.6160680945576165,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00106075575,
            "cvar5_improvement": 0.015243695561706988,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2536366551090877,
            "sortino_excess": 0.6316910098987765,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001584740775,
            "cvar5_improvement": 0.013716753646523033,
            "drawdown_improvement": 0.10998388097696676,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30827641368666137,
            "sortino_excess": 0.7101164995150091,
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
            "cost_drag": 0.0014833674500000001,
            "cvar5_improvement": 0.01222560576933931,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25938364207506087,
            "sortino_excess": 0.6461895294130768,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000815720575,
            "cvar5_improvement": 0.018577976101668683,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1791583767322423,
            "sortino_excess": 0.5646599881748182,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00190879605,
            "cvar5_improvement": 0.013834706709043538,
            "drawdown_improvement": 0.10846568555972605,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.11345290713063716,
            "sortino_excess": 0.5647647246932419,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011677038,
            "cvar5_improvement": 0.018127178566769223,
            "drawdown_improvement": 0.137795470014311,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1639673011480628,
            "sortino_excess": 0.5608028495773241,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018356228,
            "cvar5_improvement": 0.012153138691394935,
            "drawdown_improvement": 0.09969262071299731,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.31688165890356057,
            "sortino_excess": 0.7261377837156109,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002410794425,
            "cvar5_improvement": 0.013230510278651303,
            "drawdown_improvement": 0.10804859894511024,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21494531339234266,
            "sortino_excess": 0.6479035192979508,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001347469375,
            "cvar5_improvement": 0.013875523683464414,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22919155893066417,
            "sortino_excess": 0.6246367576665831,
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
            "cost_drag": 0.001186672975,
            "cvar5_improvement": 0.01845450368670439,
            "drawdown_improvement": 0.14019915658993298,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1768918103152151,
            "sortino_excess": 0.5608678414697517,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00127864005,
            "cvar5_improvement": 0.013658249005156659,
            "drawdown_improvement": 0.11093472920791397,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25981376183745314,
            "sortino_excess": 0.6381090000608961,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001822203575,
            "cvar5_improvement": 0.013803555579385651,
            "drawdown_improvement": 0.10961297438212037,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24987241356943846,
            "sortino_excess": 0.640914052357557,
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
            "cost_drag": 0.001143850025,
            "cvar5_improvement": 0.01539080920444004,
            "drawdown_improvement": 0.12106509713157035,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2327912171458045,
            "sortino_excess": 0.6233350231906344,
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
            "cost_drag": 0.0013774937,
            "cvar5_improvement": 0.016904464473221248,
            "drawdown_improvement": 0.13026641332543484,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2332968638038331,
            "sortino_excess": 0.6224615106769044,
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
            "cost_drag": 0.00203290575,
            "cvar5_improvement": 0.012267945023257893,
            "drawdown_improvement": 0.09998111625394007,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24340269033910045,
            "sortino_excess": 0.6582190524652736,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001208952625,
            "cvar5_improvement": 0.01832749388552324,
            "drawdown_improvement": 0.13898304258961927,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16223983799316427,
            "sortino_excess": 0.5706945593061082,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014742416,
            "cvar5_improvement": 0.01206829953744359,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26651347469798664,
            "sortino_excess": 0.6468404386784675,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001910426975,
            "cvar5_improvement": 0.012221568578904432,
            "drawdown_improvement": 0.10021316118943147,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26095772017790214,
            "sortino_excess": 0.6446358593177032,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00142241395,
            "cvar5_improvement": 0.018490277200127497,
            "drawdown_improvement": 0.14122599537137998,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13510632319165322,
            "sortino_excess": 0.5953735386339992,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009232860750000001,
            "cvar5_improvement": 0.017060247986499515,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1828942858209872,
            "sortino_excess": 0.5735998085011115,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009764929999999999,
            "cvar5_improvement": 0.018424810345899417,
            "drawdown_improvement": 0.14109295210405443,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2734845613802132,
            "sortino_excess": 0.6575313318992227,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0008046829,
            "cvar5_improvement": 0.01852777763797626,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21925671648038245,
            "sortino_excess": 0.6152115167494707,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012774507,
            "cvar5_improvement": 0.015261906731532906,
            "drawdown_improvement": 0.12070382422751877,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2785517821088845,
            "sortino_excess": 0.6590731236400237,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014742023749999998,
            "cvar5_improvement": 0.012068452146974152,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2625016000348914,
            "sortino_excess": 0.6402255383688302,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015593292750000001,
            "cvar5_improvement": 0.012372648115067808,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.22422009403675933,
            "sortino_excess": 0.6222499637106665,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00121956215,
            "cvar5_improvement": 0.018474015764912838,
            "drawdown_improvement": 0.14008594314868164,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.08456613978726635,
            "sortino_excess": 0.5261349199606578,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000845268925,
            "cvar5_improvement": 0.01843575168047379,
            "drawdown_improvement": 0.14128128943329266,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19242018808984668,
            "sortino_excess": 0.574653022410728,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001852661325,
            "cvar5_improvement": 0.017930143597813926,
            "drawdown_improvement": 0.138474066740564,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.15278703192351392,
            "sortino_excess": 0.6692021534920275,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012331658500000001,
            "cvar5_improvement": 0.01846527871027867,
            "drawdown_improvement": 0.1408669602965002,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20979011858781532,
            "sortino_excess": 0.6222895542938077,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0007868398500000001,
            "cvar5_improvement": 0.018589600730446448,
            "drawdown_improvement": 0.1414472831411156,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.04181940489937754,
            "sortino_excess": 0.4244857538280215,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00160434595,
            "cvar5_improvement": 0.01224011808569014,
            "drawdown_improvement": 0.1003433055900422,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16408881639039213,
            "sortino_excess": 0.5683883161135543,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0009444532749999999,
            "cvar5_improvement": 0.01684695794106468,
            "drawdown_improvement": 0.13116227299279679,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25173385936817666,
            "sortino_excess": 0.6341957415232896,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010217979249999998,
            "cvar5_improvement": 0.016889640565030714,
            "drawdown_improvement": 0.1308427996840898,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16737281414579275,
            "sortino_excess": 0.5644388013790709,
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
            "cost_drag": 0.0009961642,
            "cvar5_improvement": 0.016851783362608674,
            "drawdown_improvement": 0.13099628720774736,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21720469574017537,
            "sortino_excess": 0.5993528776842927,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001787578375,
            "cvar5_improvement": 0.015353469148887874,
            "drawdown_improvement": 0.12088396504538013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20785740878869147,
            "sortino_excess": 0.6267147611977405,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00144176425,
            "cvar5_improvement": 0.012048925924109537,
            "drawdown_improvement": 0.10090395194681454,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26175723189581235,
            "sortino_excess": 0.6386228367442448,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
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
                "atr_stop_multiple": 2.0,
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
            "config_hash": "9d664e42f27aebc329cd49abcbde343fb1387af1a9f1e283a7df2b7720569a0b",
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
            "stable": false
          },
          {
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
            "config_hash": "e8b7fcf3c2ad7e14ca5c309d4ceea34c37377a944d4e994eec2a8d8c3e9ca776",
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
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
            "config_hash": "a5efd00fb61d9b2a1ac35aba15b83ae9e0a19fed8a321553463582b8c2af4d5b",
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
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
                "cooldown_sessions": 0,
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
            "config_hash": "a67e3cc74965886bce10ad473e4d8bcf742d60206923755ca556662199841790",
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
            "stable": false
          },
          {
            "config": {
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
            "config_hash": "f20ba2653807ceb72f7ef55682a53e713c7e7387f3283a836fa7144d92d2d1c9",
            "cost_drag": 0.0017387755249999998,
            "cvar5_improvement": 0.01689433672023563,
            "drawdown_improvement": 0.12909225384686013,
            "exposure_ratio": 0.49404761904761907,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 0.2342167664080846,
            "sortino_excess": 0.7553016115287887,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00023461845,
            "cvar5_improvement": 0.02117435183364807,
            "drawdown_improvement": 0.16661490647723262,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.0944675e-05,
            "cvar5_improvement": 0.022632411137927987,
            "drawdown_improvement": 0.17184266370567558,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00027713445,
            "cvar5_improvement": 0.020864980562998896,
            "drawdown_improvement": 0.16596065692713702,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.365485e-05,
            "cvar5_improvement": 0.02279332514097201,
            "drawdown_improvement": 0.17198072917077678,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.0001472174,
            "cvar5_improvement": 0.021960627843859982,
            "drawdown_improvement": 0.1697875211517764,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 7.287765e-05,
            "cvar5_improvement": 0.0225725771069099,
            "drawdown_improvement": 0.1717927444757949,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010417835,
            "cvar5_improvement": 0.022441881893013473,
            "drawdown_improvement": 0.1713189346288554,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000114586125,
            "cvar5_improvement": 0.022572652625666115,
            "drawdown_improvement": 0.17117542586947246,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00010825530000000001,
            "cvar5_improvement": 0.02208988604351087,
            "drawdown_improvement": 0.17090133511256123,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000138335,
            "cvar5_improvement": 0.02243489845011731,
            "drawdown_improvement": 0.17088652980736493,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.000147567,
            "cvar5_improvement": 0.021889440651797577,
            "drawdown_improvement": 0.1703269380016808,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000262688725,
            "cvar5_improvement": 0.02123244617168482,
            "drawdown_improvement": 0.16713576035380598,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00018771207499999998,
            "cvar5_improvement": 0.02192787348303178,
            "drawdown_improvement": 0.16912146161838348,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.0002762903,
            "cvar5_improvement": 0.020805252693558787,
            "drawdown_improvement": 0.1659794098933941,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001504217,
            "cvar5_improvement": 0.0218517019649241,
            "drawdown_improvement": 0.1697076687125612,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.0001788788,
            "cvar5_improvement": 0.021756012729039337,
            "drawdown_improvement": 0.1699305819329423,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010505100000000001,
            "cvar5_improvement": 0.02219881192244675,
            "drawdown_improvement": 0.1709811875517764,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.0001544784,
            "cvar5_improvement": 0.022118402727946292,
            "drawdown_improvement": 0.16964519069520367,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00015641137499999998,
            "cvar5_improvement": 0.02205856869692821,
            "drawdown_improvement": 0.169595271465323,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.000113949225,
            "cvar5_improvement": 0.022599250018991043,
            "drawdown_improvement": 0.17119233400440392,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 9.8040625e-05,
            "cvar5_improvement": 0.02262897357209828,
            "drawdown_improvement": 0.1716749249737378,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000232422225,
            "cvar5_improvement": 0.02142266203793841,
            "drawdown_improvement": 0.16751210780976125,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00015981024999999998,
            "cvar5_improvement": 0.021893784432489852,
            "drawdown_improvement": 0.16990595143429776,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00010825530000000001,
            "cvar5_improvement": 0.02208988604351087,
            "drawdown_improvement": 0.17090133511256123,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000114586125,
            "cvar5_improvement": 0.022572652625666115,
            "drawdown_improvement": 0.17117542586947246,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 7.429175e-05,
            "cvar5_improvement": 0.022766727747647084,
            "drawdown_improvement": 0.17196382103584532,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.0001504217,
            "cvar5_improvement": 0.0218517019649241,
            "drawdown_improvement": 0.1697076687125612,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00010396737500000001,
            "cvar5_improvement": 0.022396576130894248,
            "drawdown_improvement": 0.17132277714635033,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000147567,
            "cvar5_improvement": 0.021889440651797577,
            "drawdown_improvement": 0.1703269380016808,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.0001875011,
            "cvar5_improvement": 0.021882567720912554,
            "drawdown_improvement": 0.16912530413587842,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00023130514999999998,
            "cvar5_improvement": 0.021307619098710956,
            "drawdown_improvement": 0.16753746491122776,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 5.453295e-05,
            "cvar5_improvement": 0.02282656727489845,
            "drawdown_improvement": 0.17226532983584533,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00015641137499999998,
            "cvar5_improvement": 0.02205856869692821,
            "drawdown_improvement": 0.169595271465323,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.0002134276,
            "cvar5_improvement": 0.021769381984623026,
            "drawdown_improvement": 0.16878872568956513,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00023782274999999999,
            "cvar5_improvement": 0.02106542595471219,
            "drawdown_improvement": 0.16653505403801744,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018771207499999998,
            "cvar5_improvement": 0.02192787348303178,
            "drawdown_improvement": 0.16912146161838348,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 7.8431525e-05,
            "cvar5_improvement": 0.02274145835087267,
            "drawdown_improvement": 0.17197497973562062,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00022012025,
            "cvar5_improvement": 0.02145887884832101,
            "drawdown_improvement": 0.16875797176896545,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 5.3896050000000004e-05,
            "cvar5_improvement": 0.02285316466822338,
            "drawdown_improvement": 0.1722822379707768,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000147886275,
            "cvar5_improvement": 0.021963206658565847,
            "drawdown_improvement": 0.17031708841399526,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00015660182499999998,
            "cvar5_improvement": 0.02199650101497705,
            "drawdown_improvement": 0.170396338876876,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 8.8002375e-05,
            "cvar5_improvement": 0.022415437829254335,
            "drawdown_improvement": 0.17140893441232252,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 5.453295e-05,
            "cvar5_improvement": 0.02282656727489845,
            "drawdown_improvement": 0.17226532983584533,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 9.819032500000001e-05,
            "cvar5_improvement": 0.0226816188236213,
            "drawdown_improvement": 0.1716734709356206,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00012979044999999998,
            "cvar5_improvement": 0.022236483725643623,
            "drawdown_improvement": 0.17098852698133726,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000147886275,
            "cvar5_improvement": 0.021963206658565847,
            "drawdown_improvement": 0.17031708841399526,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00012989387499999998,
            "cvar5_improvement": 0.022283390394604717,
            "drawdown_improvement": 0.17098619870003703,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000160927325,
            "cvar5_improvement": 0.022008827371717308,
            "drawdown_improvement": 0.16988059433283126,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 7.287765e-05,
            "cvar5_improvement": 0.0225725771069099,
            "drawdown_improvement": 0.1717927444757949,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.0944675e-05,
            "cvar5_improvement": 0.022632411137927987,
            "drawdown_improvement": 0.17184266370567558,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00019005267500000003,
            "cvar5_improvement": 0.02172502257997908,
            "drawdown_improvement": 0.16912342201399524,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000159882025,
            "cvar5_improvement": 0.021953175484087466,
            "drawdown_improvement": 0.1699041689829948,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000231376925,
            "cvar5_improvement": 0.021367010150308566,
            "drawdown_improvement": 0.16753568245992478,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00012521825,
            "cvar5_improvement": 0.022071673942003184,
            "drawdown_improvement": 0.17079804343429777,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.831400000000001e-05,
            "cvar5_improvement": 0.022715731533161303,
            "drawdown_improvement": 0.17197612174263952,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.287765e-05,
            "cvar5_improvement": 0.0225725771069099,
            "drawdown_improvement": 0.1717927444757949,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000126335325,
            "cvar5_improvement": 0.02218671688123064,
            "drawdown_improvement": 0.17077268633283127,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 9.886990000000001e-05,
            "cvar5_improvement": 0.02264705457895385,
            "drawdown_improvement": 0.17177174797644976,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000147886275,
            "cvar5_improvement": 0.021963206658565847,
            "drawdown_improvement": 0.17031708841399526,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010391045,
            "cvar5_improvement": 0.0223492337372796,
            "drawdown_improvement": 0.17132381029728366,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000147886275,
            "cvar5_improvement": 0.021963206658565847,
            "drawdown_improvement": 0.17031708841399526,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000196656675,
            "cvar5_improvement": 0.02156600591698843,
            "drawdown_improvement": 0.16808315904094062,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00013848470000000002,
            "cvar5_improvement": 0.02248754370164033,
            "drawdown_improvement": 0.17088507576924775,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.000160927325,
            "cvar5_improvement": 0.022008827371717308,
            "drawdown_improvement": 0.16988059433283126,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00010021085,
            "cvar5_improvement": 0.022452461180419204,
            "drawdown_improvement": 0.1711896612757949,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 9.0569775e-05,
            "cvar5_improvement": 0.022330060760280657,
            "drawdown_improvement": 0.17134373756401064,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.0001897334,
            "cvar5_improvement": 0.021651256573210806,
            "drawdown_improvement": 0.1691332716016808,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000125290025,
            "cvar5_improvement": 0.022131064993600798,
            "drawdown_improvement": 0.1707962609829948,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00030844625,
            "cvar5_improvement": 0.020731552640240656,
            "drawdown_improvement": 0.16556430085839852,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.287765e-05,
            "cvar5_improvement": 0.0225725771069099,
            "drawdown_improvement": 0.1717927444757949,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00014672285,
            "cvar5_improvement": 0.021829712782357468,
            "drawdown_improvement": 0.1703456909679379,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000277453725,
            "cvar5_improvement": 0.02093874656976717,
            "drawdown_improvement": 0.16595080733945147,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010825530000000001,
            "cvar5_improvement": 0.02208988604351087,
            "drawdown_improvement": 0.17090133511256123,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00019005267500000003,
            "cvar5_improvement": 0.02172502257997908,
            "drawdown_improvement": 0.16912342201399524,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 9.8809825e-05,
            "cvar5_improvement": 0.022620281317417675,
            "drawdown_improvement": 0.17177249191144434,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00015647425,
            "cvar5_improvement": 0.02193779664270608,
            "drawdown_improvement": 0.17040016098778735,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010021085,
            "cvar5_improvement": 0.022452461180419204,
            "drawdown_improvement": 0.1711896612757949,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00021332417499999998,
            "cvar5_improvement": 0.02172247531566193,
            "drawdown_improvement": 0.16879105397086536,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00013151154999999998,
            "cvar5_improvement": 0.022321765966522772,
            "drawdown_improvement": 0.1707158514288554,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 7.8431525e-05,
            "cvar5_improvement": 0.02274145835087267,
            "drawdown_improvement": 0.17197497973562062,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00015712364999999998,
            "cvar5_improvement": 0.022116367799152922,
            "drawdown_improvement": 0.17038544378133727,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00023782274999999999,
            "cvar5_improvement": 0.02106542595471219,
            "drawdown_improvement": 0.16653505403801744,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 9.886990000000001e-05,
            "cvar5_improvement": 0.02264705457895385,
            "drawdown_improvement": 0.17177174797644976,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010417835,
            "cvar5_improvement": 0.022441881893013473,
            "drawdown_improvement": 0.1713189346288554,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00018888925,
            "cvar5_improvement": 0.0215915287037707,
            "drawdown_improvement": 0.16915202456793788,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00010417835,
            "cvar5_improvement": 0.022441881893013473,
            "drawdown_improvement": 0.1713189346288554,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 5.453295e-05,
            "cvar5_improvement": 0.02282656727489845,
            "drawdown_improvement": 0.17226532983584533,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010505100000000001,
            "cvar5_improvement": 0.02219881192244675,
            "drawdown_improvement": 0.1709811875517764,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00017795385,
            "cvar5_improvement": 0.02169706292690778,
            "drawdown_improvement": 0.16995163816896547,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.429175e-05,
            "cvar5_improvement": 0.022766727747647084,
            "drawdown_improvement": 0.17196382103584532,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00013124365000000002,
            "cvar5_improvement": 0.022229117810788904,
            "drawdown_improvement": 0.17072072709728367,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 9.8277875e-05,
            "cvar5_improvement": 0.022512295211437286,
            "drawdown_improvement": 0.1712395805056756,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00015892307500000002,
            "cvar5_improvement": 0.022393139929721514,
            "drawdown_improvement": 0.17068184401007688,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.000158863,
            "cvar5_improvement": 0.02236636666818534,
            "drawdown_improvement": 0.17068258794507146,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00013151154999999998,
            "cvar5_improvement": 0.022321765966522772,
            "drawdown_improvement": 0.1707158514288554,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.0001788788,
            "cvar5_improvement": 0.021756012729039337,
            "drawdown_improvement": 0.1699305819329423,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00015660182499999998,
            "cvar5_improvement": 0.02199650101497705,
            "drawdown_improvement": 0.170396338876876,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000125161775,
            "cvar5_improvement": 0.022152171250767325,
            "drawdown_improvement": 0.17045164556401063,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 9.0569775e-05,
            "cvar5_improvement": 0.022330060760280657,
            "drawdown_improvement": 0.17134373756401064,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010825530000000001,
            "cvar5_improvement": 0.02208988604351087,
            "drawdown_improvement": 0.17090133511256123,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00013848470000000002,
            "cvar5_improvement": 0.02248754370164033,
            "drawdown_improvement": 0.17088507576924775,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.0002210452,
            "cvar5_improvement": 0.02151782865045257,
            "drawdown_improvement": 0.1687369155329423,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00011862870000000001,
            "cvar5_improvement": 0.022587215051702483,
            "drawdown_improvement": 0.17147023917644974,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00010396737500000001,
            "cvar5_improvement": 0.022396576130894248,
            "drawdown_improvement": 0.17132277714635033,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 9.819032500000001e-05,
            "cvar5_improvement": 0.0226816188236213,
            "drawdown_improvement": 0.1716734709356206,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000126335325,
            "cvar5_improvement": 0.02218671688123064,
            "drawdown_improvement": 0.17077268633283127,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00019106625000000002,
            "cvar5_improvement": 0.021759907133192747,
            "drawdown_improvement": 0.16950806898778734,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000196656675,
            "cvar5_improvement": 0.02156600591698843,
            "drawdown_improvement": 0.16808315904094062,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 9.0569775e-05,
            "cvar5_improvement": 0.022330060760280657,
            "drawdown_improvement": 0.17134373756401064,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 9.0569775e-05,
            "cvar5_improvement": 0.022330060760280657,
            "drawdown_improvement": 0.17134373756401064,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000118568625,
            "cvar5_improvement": 0.022560441790166308,
            "drawdown_improvement": 0.17147098311144432,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 9.807280000000001e-05,
            "cvar5_improvement": 0.022655892005909933,
            "drawdown_improvement": 0.1716746129426395,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.000138367175,
            "cvar5_improvement": 0.022461816883928964,
            "drawdown_improvement": 0.17088621777626664,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00012979044999999998,
            "cvar5_improvement": 0.022236483725643623,
            "drawdown_improvement": 0.17098852698133726,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00010391045,
            "cvar5_improvement": 0.0223492337372796,
            "drawdown_improvement": 0.17132381029728366,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.8281825e-05,
            "cvar5_improvement": 0.02268881309934965,
            "drawdown_improvement": 0.1719764337737378,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000122594375,
            "cvar5_improvement": 0.022237548319741004,
            "drawdown_improvement": 0.1705168424123225,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00010417835,
            "cvar5_improvement": 0.022441881893013473,
            "drawdown_improvement": 0.1713189346288554,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 8.8002375e-05,
            "cvar5_improvement": 0.022415437829254335,
            "drawdown_improvement": 0.17140893441232252,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 9.8809825e-05,
            "cvar5_improvement": 0.022620281317417675,
            "drawdown_improvement": 0.17177249191144434,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 5.3896050000000004e-05,
            "cvar5_improvement": 0.02285316466822338,
            "drawdown_improvement": 0.1722822379707768,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00026256115,
            "cvar5_improvement": 0.02117374179941385,
            "drawdown_improvement": 0.16713958246471733,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.0003075213,
            "cvar5_improvement": 0.020672602838109098,
            "drawdown_improvement": 0.16558535709442168,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000191193825,
            "cvar5_improvement": 0.021818611505463718,
            "drawdown_improvement": 0.16950424687687599,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00012521825,
            "cvar5_improvement": 0.022071673942003184,
            "drawdown_improvement": 0.17079804343429777,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.831400000000001e-05,
            "cvar5_improvement": 0.022715731533161303,
            "drawdown_improvement": 0.17197612174263952,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.8281825e-05,
            "cvar5_improvement": 0.02268881309934965,
            "drawdown_improvement": 0.1719764337737378,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000157227075,
            "cvar5_improvement": 0.02216327446811402,
            "drawdown_improvement": 0.17038311550003704,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 5.453295e-05,
            "cvar5_improvement": 0.02282656727489845,
            "drawdown_improvement": 0.17226532983584533,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000187444175,
            "cvar5_improvement": 0.02183522532729791,
            "drawdown_improvement": 0.16912633728681176,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.000125290025,
            "cvar5_improvement": 0.022131064993600798,
            "drawdown_improvement": 0.1707962609829948,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000131300575,
            "cvar5_improvement": 0.022276460204403548,
            "drawdown_improvement": 0.17071969394635034,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 7.8431525e-05,
            "cvar5_improvement": 0.02274145835087267,
            "drawdown_improvement": 0.17197497973562062,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00015647425,
            "cvar5_improvement": 0.02193779664270608,
            "drawdown_improvement": 0.17040016098778735,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000194089275,
            "cvar5_improvement": 0.021651382985962104,
            "drawdown_improvement": 0.1681483558892525,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.00017795385,
            "cvar5_improvement": 0.02169706292690778,
            "drawdown_improvement": 0.16995163816896547,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000126335325,
            "cvar5_improvement": 0.02218671688123064,
            "drawdown_improvement": 0.17077268633283127,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000277453725,
            "cvar5_improvement": 0.02093874656976717,
            "drawdown_improvement": 0.16595080733945147,
            "exposure_ratio": 0.06349206349206349,
            "family": "trend_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000126335325,
            "cvar5_improvement": 0.02218671688123064,
            "drawdown_improvement": 0.17077268633283127,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.000232422225,
            "cvar5_improvement": 0.02142266203793841,
            "drawdown_improvement": 0.16751210780976125,
            "exposure_ratio": 0.06349206349206349,
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
            "cost_drag": 0.000125161775,
            "cvar5_improvement": 0.022152171250767325,
            "drawdown_improvement": 0.17045164556401063,
            "exposure_ratio": 0.04365079365079365,
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
            "cost_drag": 0.00012989387499999998,
            "cvar5_improvement": 0.022283390394604717,
            "drawdown_improvement": 0.17098619870003703,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 7.8431525e-05,
            "cvar5_improvement": 0.02274145835087267,
            "drawdown_improvement": 0.17197497973562062,
            "exposure_ratio": 0.037698412698412696,
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
            "cost_drag": 0.00014672285,
            "cvar5_improvement": 0.021829712782357468,
            "drawdown_improvement": 0.1703456909679379,
            "exposure_ratio": 0.037698412698412696,
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
