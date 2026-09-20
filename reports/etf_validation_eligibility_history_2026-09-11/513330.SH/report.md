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
            false,
            true
          ],
          "oos_returns": [
            0.08633703520000009,
            0.11962079250000013,
            -0.08238751580000003,
            0.19936222900000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9f8d66390e22e841dbc879446df494747fe0e69404b4bb4c04c136d2b5046189",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07963476380000009,
            0.13457785660000016,
            -0.1007781603,
            0.19922438220000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07289744810000011,
            0.14969815040000015,
            -0.11900440689999998,
            0.19898233860000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "da28e066148553678760b45c21a54f0f815cb41838c646423fedd4acd0c69f0d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06600042150000013,
            0.16482997810000014,
            -0.1371047955,
            0.19866349530000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "90d6ff7ed79e50c4dddaaed58adbfdc177b6bf9b378de9d013c1d4240154e606",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.059101941900000135,
            0.18142200510000012,
            -0.15494792059999996,
            0.19828406590000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "43950e3f259617cc483404f6d6415d25f5b84e7eb334812843c5e9177958cce0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08641974940000006,
            0.12407525340000022,
            -0.08014294799999998,
            0.19669769800000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8bce2fd4652d535226e8dc035f7242084edc778cd386a1bba082c130a02ff6fd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09213146200000014,
            0.13906835320000022,
            -0.09847738759999997,
            0.19994286850000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08111732360000017,
            0.1593240356000002,
            -0.11676427689999994,
            0.20113021820000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "77bd9770c8d5ec308e8b7fd0fadfa8fbf6cead744a6e15323ae2a4260b80ad42",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08356821780000018,
            0.1811872426000002,
            -0.13481413819999993,
            0.20075003970000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0664477e5295e0bc1c74559f720de476589a1201e90ca5c2c2645acf217e5a1e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07648168720000018,
            0.2047222776000002,
            -0.15272325159999992,
            0.20034305780000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5132cd3db68e157dd3153cb3ae9792dee9a4b1c862130fd622636843c2b36730",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09186046280000007,
            0.13796329430000026,
            -0.07505882359999996,
            0.18908118810000007
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0a8f9b6084c1d444d5b9dacff3681205d0b72ae817079b8f300cb12517cbc6fc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08501562960000009,
            0.1601526071000003,
            -0.09352076499999994,
            0.18895578590000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08127430170000009,
            0.18375178240000029,
            -0.11455307129999989,
            0.1958696273000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "77c0310211df78935d4962e65b3e258ba298c8d9fd368ecda7590f2158d215b1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09299071110000019,
            0.19529295540000027,
            -0.13265692549999988,
            0.20088497270000008
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2b1ca3a349c41d3e74f6ea219a4c0fe30f94bd0c8d69053d8a263b0a0abd2acc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0857621981000002,
            0.1953729946000003,
            -0.15049181089999986,
            0.2004492008000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c952cae7bd45116005f8eb31266d51ce6c128f513baffac095de4b6cb97384f6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10237155910000009,
            0.23507718190000024,
            -0.08068041719999994,
            0.2069376113000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4deabe0573cbeae491a145f8e4d20f916f5c910661a4c80d8fc5167f3190b561",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09240471060000009,
            0.18532824660000036,
            -0.0905917272999999,
            0.18603409980000007
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0853855363000001,
            0.18540602780000034,
            -0.10886898819999988,
            0.18587482930000007
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2542c5a0c6a70a2692a3038a43bcea945893d0495b2c1713e03b0f9afdf6620a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08237093540000012,
            0.18549581150000033,
            -0.13056040719999984,
            0.19519928410000015
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c1f8d05174940de5abab81e70dbabad9d91d52b696bb409bdd2ab6d799a45da8",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06766377320000014,
            0.18883504850000035,
            -0.14528477169999984,
            0.19692728030000015
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e43174b66cae18536744c3921b38ea3b06411d2aafef1ba96738db80f17ae80b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08509411110000006,
            0.13094472190000012,
            -0.08120109370000005,
            0.200138746
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3986694fa6674e967c35c294ac4055fbd72f2cc3fda3b61e52db297456a13d8f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07848977470000008,
            0.1462965013000001,
            -0.09962323890000002,
            0.19996460580000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0716537233000001,
            0.1616613257000001,
            -0.1178657366,
            0.19975645700000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "222df6d8f13727d94d27e59090092450a9d1437210027cc7ba1e9ed6e9669731",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0648191154000001,
            0.1771347992000001,
            -0.13596774069999998,
            0.19937188400000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1955c130371fbd273746ee973f8ff228037a1edbf3c4f5811acb4c15e0cf6dda",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.05794455760000011,
            0.1925517477000001,
            -0.1538362743,
            0.1989903694
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bb96bcaf6239a8f480b471f3bd6f4f2edad305f90a5fe68ac611f0a7034ec535",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09974593990000011,
            0.14512325860000017,
            -0.07783613310000001,
            0.20142447330000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "259b394408833371c897a4a9317235e9c836670ca8171b17b53da30eb4a6a0c9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09481757120000012,
            0.1602891383000002,
            -0.09629301209999998,
            0.20260609970000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08809846080000013,
            0.1757296407000002,
            -0.11465816709999997,
            0.20237893580000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "183a91bd23a755b7e87e0ab603de83e23b8219e506dd76397e078a1cf902c167",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08113766720000014,
            0.19089467830000018,
            -0.13275450889999996,
            0.20200236970000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "260012ec18d23eb314b1bd71c33087541eee3662ea1fdbc37c0ba619bcac2dbb",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07402027270000014,
            0.20611520340000017,
            -0.15064108559999995,
            0.20151255800000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c848623e0be20099dc48e20d39b8cb65688053a8a496ec4aa885783422556572",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11907062330000014,
            0.19090118070000017,
            -0.07565798749999998,
            0.19803722050000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "08bb1f5360f9a1daa71255445b28f2b85a25bbf9afeafe227384fc93068725f1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11235418060000014,
            0.1743867555000002,
            -0.09409713189999996,
            0.19783891160000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10140816950000016,
            0.1895168832000002,
            -0.11141485279999992,
            0.20284303650000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0c65d2ef761411d63b3e7d181c2d998d0df2dcf703efd602be2fad87e1da59dc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09730914310000016,
            0.19857520040000023,
            -0.12959183159999993,
            0.20458333490000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3c50ec6e404a0402a3f98be24cad12d2a6bb4f1a9ce1917679cbf45896f6efd0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09012526840000018,
            0.20252715100000024,
            -0.1475048504999999,
            0.20414944250000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "13140adfdb638ee59aee50db7ac7a68bf94b4aeb3cd69660a93f3b3954d57fc0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10974148520000004,
            0.2107238444000002,
            -0.07551904499999995,
            0.2040966643000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6d151393122f9975d3a3fbbdfde74da7330ecc39667716a01b5d15571ac979f7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1290840116000002,
            0.2308626007000002,
            -0.09143406319999993,
            0.19791956440000008
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12208670130000018,
            0.2349109972000002,
            -0.10970341819999992,
            0.1976355462000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "80899914e7291fc258eeddf6520efbf7fe1b0287b99fc96d0a62841279df7425",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1095560729000002,
            0.2389547348000002,
            -0.1265474063999999,
            0.20440820230000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4769bcc53bde368b7006c19ea230e03bc28764d38036f94954f64cec059dcb85",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09153583120000021,
            0.2425379822000002,
            -0.14071296859999988,
            0.20615186990000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f6d7509f3f5c1634fea76f4dd53e98841aa76151e5c756d7dfd55b79d67dc8f8",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09573711020000007,
            0.1242962035000001,
            -0.07333409840000005,
            0.19912992350000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cff9859d4a5f2814140612668f4daacf34db624bbfeb4347eae64ec9f633685b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08897685960000008,
            0.1398047637000001,
            -0.09179069490000002,
            0.19898446560000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0822103440000001,
            0.1552663002000001,
            -0.1101994438,
            0.19878173310000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9b285843c53cb0e98fbb611366f677a98327b135bad0b9ffb777bf5f8f2ea648",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07526156060000011,
            0.1707962189000001,
            -0.1284984517,
            0.19848465210000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3b113e92d617b95e71b3d485144a8bf07623fdd5476c359cde7bf0af5e60b9ba",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06817788520000012,
            0.18630956770000012,
            -0.14648609569999999,
            0.19810263490000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "eec8e6bf15537c408060e82aa9252bc11c299b5ededb53194b719629a246267c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11367545260000009,
            0.1411517960000001,
            -0.06228926800000002,
            0.19913923870000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1fb848b69f408dc3ba8d7bd85ebc85edda0535045ed94aad7ab28c6599beaf4d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11585544860000012,
            0.14710987940000014,
            -0.0810101173,
            0.20035995360000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10882982000000013,
            0.16252996730000016,
            -0.09953467099999998,
            0.20020759080000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4734c020226fa7443033daa844967e4699044f02fbfcdd5f6005cd5984d5532d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10183523990000014,
            0.17796467350000017,
            -0.11788798569999996,
            0.19987121620000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e062b42fc995eb71bc33d23b0a1a7171cd43966949db71673235e334018a8b9f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09456494770000015,
            0.19340867990000016,
            -0.13606989199999994,
            0.19947309840000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0380f680c2ed4cb0751113688c497ae2ca73f1769aab860b0851287c65fe1fac",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13359138500000012,
            0.14532366270000013,
            -0.053528091300000004,
            0.19445697880000007
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a7e68e5035096e8601e3fc70bed10c2f2d51007849d3f7759c8601c0d59a51de",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12645404370000013,
            0.16458713390000013,
            -0.07232811779999998,
            0.19434044510000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12209781520000014,
            0.18445889100000012,
            -0.08885671409999994,
            0.19943688270000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9f72db2d6091f70ef6f2c28a733136150b7d98312604e238d2900953d4d65ab4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12866689980000018,
            0.1850604906000002,
            -0.10736882489999992,
            0.20124945950000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1b7e2c5e7b5958dc5a4167102c649e3905f2a20047667578f26da46fe53ae2b2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1212551251000002,
            0.2004982992000002,
            -0.12571797709999993,
            0.20087748280000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4fc55be6dc74c3f50156a7e114ea4978acdb95ed567f20d6bbf0c18ba03b48c2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1287406205,
            0.1466741451000001,
            -0.05287767489999999,
            0.19397025450000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c828166e74ca3a3a5edaf08d9a9cc9318061f12eaf8a971288d9fe9aa94f0002",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14821559340000015,
            0.17016579110000013,
            -0.062156190899999963,
            0.19314950900000008
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14095518770000018,
            0.18556467270000016,
            -0.08102797239999994,
            0.19295677230000008
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d6dfb2a62a2c81350ef9e449a06dc69ac134a1e3741a97bf3776f014a02b7bde",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1372790830000002,
            0.21238599010000017,
            -0.0968046109999999,
            0.19978914350000007
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4e1a984b1c95dcc573ae3ac61d76713bc6516583278750a0006153bff7d9df6a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12041005570000018,
            0.22795467710000017,
            -0.11261116309999988,
            0.19941145180000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "589b9e99b2cc99c9bf11c7d143c4316f35fae491362d7df2a95b2a38cea057ef",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09040754980000006,
            0.11826664260000011,
            -0.08257729470000005,
            0.20196531720000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "446dc1803e4c7a85e81fa0757a3f673cc8f49dc153680f00a73418f382fe40fc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08361045580000007,
            0.13378459060000011,
            -0.10105201630000003,
            0.20178556350000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07684493990000008,
            0.14920425300000012,
            -0.1192587793,
            0.20157683280000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "61a86f69f97281212bca1d76dff4959aded7bc8ae179fd65e9a35b51766efe9a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0698657568000001,
            0.16465073850000012,
            -0.1373926469,
            0.2012546573
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "266908ce86922ef9e2da585eb6b06dc860b8cc72327a6b50d62c098f123fd428",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06278072600000009,
            0.18018492850000012,
            -0.1552752174,
            0.2008525441
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "db3ce2343cab6d1650bea124ea4ff260409091058133b2b9bd6fe8a6fd2ff9a4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11176985530000007,
            0.1241440675000001,
            -0.08146789630000002,
            0.20607269220000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "deba15173d77c901d382e9f5272229ae1cba6daa2726b4bb6ce9634e86a14da7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10484408070000008,
            0.14293518430000013,
            -0.0998731566,
            0.2058692343
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09786547480000009,
            0.15003412250000017,
            -0.11820084619999997,
            0.2056625817
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a43d42200543c8fee6ecea4bd84917ea1bcf540d535e043f6a521a06832f55f1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09074622920000011,
            0.16543965020000018,
            -0.13629663359999997,
            0.20530900820000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e2cff1ab7f737919236ab95a7fedc68c273418b1b4245a5f6ac6c54916c93f70",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08342703310000012,
            0.18087101300000016,
            -0.15423615929999995,
            0.20485790630000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e15d48069bf09f9bb10971f06b1a917c4b07e6c1a074d0d1388e0185650d24cd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1299006416000001,
            0.12152742110000009,
            -0.09035431049999999,
            0.21012530700000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5a17506ad28bbda515701fea8e5e9ce9e4f8bde66bd49b5febd4aad94e2a76b2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12272745660000009,
            0.12457700230000016,
            -0.10878562539999997,
            0.20996627590000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11915142090000011,
            0.1581612777000001,
            -0.11720230389999996,
            0.20968711350000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11176938050000013,
            0.17878479910000014,
            -0.13536909629999994,
            0.20934173620000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b54f48b12b36135d832f2f0ecb43d61a4941bcf07a971027a9accc6831847aea",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10436182970000013,
            0.18151034890000023,
            -0.15333541949999993,
            0.20893346430000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d726ac15f78e72d7171a62d66dcf57ed06bd6d2e3d2d36113bbde161c0666e27",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13976257560000005,
            0.1311794559000001,
            -0.10179140899999997,
            0.21422160800000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3b8400990f65f2f5c0b5d93d3ebecb37df16eedcd649695660efe4d79ce973b7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14317567410000012,
            0.1379492341000001,
            -0.11104109809999994,
            0.21402986650000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13585732170000014,
            0.1531372628000001,
            -0.12922228179999992,
            0.21376533510000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a8b1e9c488ff9b024597f84b549df68bca23d0664c4df78a57248136fcff3c3c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13317843370000015,
            0.17676807600000016,
            -0.1345513465999999,
            0.21339903670000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "45451ae22fd54f5fcc4a8c83f4e0e0fcc2755c40142cb91352153ea353ce96a3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11643494600000015,
            0.19199149220000014,
            -0.14590297409999992,
            0.21293096400000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e5da6823593cc26f966c1b236eb2179524508f51ac24bb8ecc1ae9cf0512a2d2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09268443270000006,
            0.1250925212000001,
            -0.07783417840000006,
            0.2016142344
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0cbf63fff76abf8f86447fff223cc640736f864eaa9919c9dbc89d1c0d125adb",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08593977620000007,
            0.1408398840000001,
            -0.09626783680000003,
            0.20147749
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07909528820000009,
            0.1565538060000001,
            -0.11462094380000001,
            0.20127555800000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "961cfe76def7b11fe2351283e3ebd181a0c11106d5a65042f1ccade8bdfaaa3b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0720848989000001,
            0.17228365070000012,
            -0.1327699135,
            0.20095738610000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "17c7279512899f3a91bea351e1b53d236bffc52f4a909e0f96befb2127ba1987",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06501969090000011,
            0.1879923805000001,
            -0.1507180095,
            0.20058208300000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c2723042d21e0f63b5e375cfd0cc6b239d7d1319ce461a03c6a1a2ef7049a724",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11631646030000009,
            0.11743878820000009,
            -0.07211749360000004,
            0.20546243720000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c732a62eeaa84162fc5a884fcc09486a2b9ee5c9039b8d9a0d76f72351d048d6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1094727053000001,
            0.1397904250000001,
            -0.09060436890000002,
            0.20531278610000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1024783364000001,
            0.16432112790000014,
            -0.10909862220000001,
            0.20512703480000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5a60d04000e8a42a7ef2a4dfd58e04047fee6e55af55b1d752e8f78c30a7fad1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09529004620000012,
            0.18018677770000016,
            -0.12731761219999999,
            0.20480048020000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5d600521d8ec100f51d0d336c6543e9781171444d584310acb517b6041a05a64",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08808904210000013,
            0.19602515420000016,
            -0.14533056119999999,
            0.20440318510000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "21afa2e296937da975f586f16b52eb519be169e613d16ecd15cd50de513cdbcd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1358310556000001,
            0.1167456236000001,
            -0.06647436080000002,
            0.20926317110000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12611969580000013,
            0.1479983620000001,
            -0.10361148639999998,
            0.20890671060000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d6b5f0adf9731cb102e277bd3fb3c7f60594548d2231a497b32c94673cd0b667",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11884725230000015,
            0.17420444290000014,
            -0.12197457829999997,
            0.20862404020000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "757cb14275a89bc4c9e5a29a7520d973e34a22ebd3401c538b8a321442b8fd5b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11136644430000016,
            0.2037806805000002,
            -0.14010105579999996,
            0.20826358170000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b6449162a482e7a08f99c096b1423ca1e879ffa87022184dd0cff292e8213cf6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13955245300000002,
            0.1283423687000001,
            -0.08150465380000001,
            0.20307151540000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4948e389709741f3f9c362d58fe2624e794f41e6d5ef2b7968b00962535749d6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.15125215940000014,
            0.13177906680000012,
            -0.07976984789999998,
            0.21299048100000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14382306890000016,
            0.1469845698000001,
            -0.09828757959999997,
            0.21281577260000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2b8cce8c37110946254601751fec91e8b1a3052ace950c33d369bc1269f4e54c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14261671890000016,
            0.16318328140000013,
            -0.11672785369999995,
            0.21250149520000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d8d5c98b26ff14e3212cd6294dddc02b69e28e1725828e71a010ae9c00e64f87",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12573231450000016,
            0.17834079580000012,
            -0.13091540079999994,
            0.21211284050000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9b0ed793b8789210beddbfe561da3142bf989c157269bda13aa9d2e732098470",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08413933890000003,
            0.1227770102000001,
            -0.07609209320000007,
            0.19982000800000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "529b14ba63795fde28f27d0ddc49d26555b3ea64714f8b42d3e97419429806f3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07743482350000004,
            0.1384454549000001,
            -0.09462998670000004,
            0.1996891724
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07068176730000006,
            0.15404186780000012,
            -0.11292645240000003,
            0.1994916149
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3cc7b53f43c230cbc0bbe5e407576b80e5c3c8401dd8cf82ff397d5c07f70d48",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06380732590000007,
            0.1697655801000001,
            -0.1311046814,
            0.1991532157
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b313af62bdd5d8e3e6b7fef4e167294ef0b09dc0cc58c92f6913a9a1385bd71c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.056772668000000075,
            0.1853873377000001,
            -0.1490596602,
            0.1987877302
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c043be32382e64bdbba090ec810f1ccf50a09fe8648fc8a3408bbd2ab9ac73c6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09869017430000002,
            0.1286835797000001,
            -0.06865892520000005,
            0.20147392430000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "45fc5ff3ccb51fbcbd9cfe0f8880bfce401d63eea9bdb37ca7711e56fdfe51f1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09193826940000004,
            0.14365564850000015,
            -0.08728127860000003,
            0.20135598280000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08512239490000005,
            0.15934061120000015,
            -0.10569550180000001,
            0.20115852730000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7c2b3fc2dbedd2b079ebdeca8887a83fb588fd2a1d89ed4f35c2ff52d779728b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07801628360000006,
            0.17510078910000015,
            -0.12397370459999998,
            0.20083302220000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2893c794a262dfeeb1d55eb234d4bbc50613e92208bd8509d365e79e48e8e243",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07094607240000007,
            0.19081519590000015,
            -0.14203147779999997,
            0.2004675367
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7826433e193e4ac82cc351ff0995a6b514018d7da192d993bd018af86f9827f0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10894872290000002,
            0.12373662340000008,
            -0.06116203440000004,
            0.20312673890000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8cbfd1cd2d9316edcb8d2b295fa7dd39a4888c1b6c1a9fd7cd02af0f71389581",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10190592260000003,
            0.13831583090000016,
            -0.07986816960000001,
            0.20300989910000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09948118300000004,
            0.16547592820000012,
            -0.09842042609999999,
            0.20282523570000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "77548bc87ab8ee39a946a4bb2c139e0addd6da3a1b8a8eb663acbcf366d946f3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09237635610000006,
            0.18028336950000018,
            -0.11673848609999997,
            0.2024997306
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "23c50db9ddba5ebfe44269566b665b6b65bbdf61def5dfe671d025e6d5a010b1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08518298000000006,
            0.1961168281000002,
            -0.13492319869999997,
            0.20214724120000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8a8f91fb3f844ba6dfc5dfcf5bdbde75f84903dd70fbf2739c509a094fde215b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11196196330000001,
            0.12486441710000007,
            -0.05366222120000001,
            0.19760419430000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "812af4d1fa0b091fb7419ff0da1d71ce91fe65a0a3224bbcf41431dcebd0b08d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11511157110000003,
            0.1411633477000001,
            -0.0724339963,
            0.20466271370000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10791059250000004,
            0.15665829330000008,
            -0.09114322349999998,
            0.20447915200000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cbe67dbd8ea3ade52ec52ba1d9625b2a6f87d9e55ccafd9a64fd847a889053cc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10678195080000005,
            0.18685907800000015,
            -0.10958022109999996,
            0.20416654100000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "461c154a7e2353f2283c499ac85775b992b924de41d0fec46d9f06b5172f7142",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09948087330000006,
            0.20259308350000016,
            -0.12781017909999995,
            0.20381394960000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f06c82a4eeb01c2ca1b3775d507f3fdf523eac9e7bd4f72ae421cb474e7f3e8d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08535083070000003,
            0.1235459703000001,
            -0.07896472730000006,
            0.1980911457
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fde5f8993452adb198b2aebe545089a0c13eb1c9000759d5e47c483b81d0ca3b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07863417340000003,
            0.1392284192000001,
            -0.09742628140000005,
            0.1979603101
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07187211990000006,
            0.15483883630000012,
            -0.11570063510000003,
            0.19774985850000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9b49243fc490f86a5308087d28dcd0c8743ca5e9e7f2f9f5645275731e7a26ee",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06495769050000007,
            0.1705835549000001,
            -0.1338300832,
            0.1974114593
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "46f84d8aed1026e2d80d880921222dcafc41aee81ce7ffb4371076fddea389b7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.057985403000000074,
            0.18621931670000008,
            -0.1516893093,
            0.1970330797
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a742864c7a1208b39c7fae284c174b8dd0af4d1de90c2fad405dab24d97015e9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10118399470000003,
            0.1286835797000001,
            -0.07467424180000005,
            0.1979291958
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fd673b08ae5457fc2c262ed05bda3c5d6934808f9935cbade4c0d6172f79ad0f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09441368450000004,
            0.14521330410000013,
            -0.09314202650000003,
            0.19779836020000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08751368970000005,
            0.16092627520000014,
            -0.11143830950000001,
            0.19758790860000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0be1879f481ad47d63cb1e9e3839ecd1e8b8a47f13b42f9c203ebdd2d8b36c92",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08042605380000006,
            0.17673673870000015,
            -0.1296708997,
            0.19724950940000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cd527804e36527d86170dc60b7b5297223c9325a141bce31c0379910247fe5f4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07334957920000007,
            0.19247905390000014,
            -0.1475642197,
            0.19687112980000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "02951609451a1a3666f9e27a5c317b82fb9d83367c6c4907f4a9d530a074a829",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11194726670000002,
            0.12373662340000008,
            -0.07040835670000005,
            0.19776614420000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "18fc14e280c2cfd24eb7a861ce0ea745639459e640b134c7b93c1eee85bd3f1a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10481734700000003,
            0.14065645080000014,
            -0.08895732030000002,
            0.1976364103
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10319217970000004,
            0.16547592820000012,
            -0.1072779018,
            0.19742595870000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "64e3052ef8fa0319a7c2533e42c13b53422f82ad86eb68d7701d663c462fd129",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09607594540000006,
            0.18272201880000016,
            -0.12547399409999999,
            0.1970875595
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8088cc365f89e6679290e380387e1324139d60bed3aa5ee409fd03ee528e9a99",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08877186780000007,
            0.19860449210000017,
            -0.14341838819999997,
            0.19670917990000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8bcb1085f091f1ae946199c14e23c1ba1e975e65f06096e4aa24df9a5387bf01",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1159679395,
            0.12486441710000007,
            -0.07519098710000004,
            0.19760419430000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2ea28b5fd16155856db1a6aaf045c7c6a38ceefbc42b4e51cb92f1e5a3291080",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11904527790000002,
            0.1411633477000001,
            -0.08475737680000002,
            0.19747335870000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11181810710000004,
            0.15665829330000008,
            -0.10318182629999999,
            0.19726400880000003
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8e9ceaba7690e6d3faceede615245b6d1a7554518ab91ac3b377c4df97f4c0a3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11171620740000004,
            0.18685907800000015,
            -0.12141532959999998,
            0.19692560960000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fb7cf5a396194be308efbdd959d12d7a0c48b1193d5a2caac5caa3adc4c65a92",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10429860030000006,
            0.20259308350000016,
            -0.13937475949999997,
            0.19654723000000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "318930da62df7a9a4b135893117f29e6080cdee95f09a82d0197d3413840c2a1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08289926690000005,
            0.11940943480000007,
            -0.07895190510000008,
            0.1995340188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "824e648c83a8f7c5d611f1044280116ee112dafff48f1898aadbcdd7cc416908",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07607332690000007,
            0.1350234372000001,
            -0.09743268990000005,
            0.1994031832
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06928610610000008,
            0.15057290480000007,
            -0.11568643600000003,
            0.19920162689999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "71cb3c31412438e23d4b9bff35ae94c701cf15c333086d98008bcf43077b98f0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.062470767900000085,
            0.16618750780000008,
            -0.13379713880000002,
            0.1988632277
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "65e02eee14f0acb0a825dacbe164cfa06365c84cde2b215e2174efcc30cf82c1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.055407979700000096,
            0.18176472010000008,
            -0.1516966019,
            0.1984848481
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a10c8020a0773c04afed2636a58bedf090d4fbf98ff1d3b60925e0ea4e097776",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09601407540000007,
            0.12096061740000011,
            -0.07473332530000007,
            0.200814942
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c3738ae7a721e173bf76984f66c2f685bc435209fd4dab537ffc550a62a23d7b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08926892610000008,
            0.1365581813000001,
            -0.09322099620000004,
            0.20069300169999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0823003232000001,
            0.1521489885000001,
            -0.11150164970000002,
            0.2004914454
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "19d00bceaeaee45b90711aedc56891ccd0aec187c04e0c1df0557f9894ba521c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07533754290000011,
            0.16781559200000012,
            -0.12964185320000002,
            0.2001530462
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "56cb7fb31d203469a3f1c85e5c30ae6f448173b6cf02c6203dc31a8c63b6dd5c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06816075410000011,
            0.18343374330000012,
            -0.1475246745,
            0.1997835619
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "aa322358aee7ceed5d28526185f0ecc94c244a13c6344d41457546a6a739dfb8",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10920872810000008,
            0.12117539200000008,
            -0.07053649170000006,
            0.20210476049999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "25d46927d3049e38377b2aab3cdec3957e2a5adf6b1a27fe97889bc46891180e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1022979529000001,
            0.13805880470000012,
            -0.08904407000000004,
            0.2019828202
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0952418170000001,
            0.15370091180000012,
            -0.10736279330000002,
            0.20178126389999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "daa598de199db4f2abe5d43ad5487cc9e98f006ac89533dc04afd523606d5df7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08812078490000012,
            0.1693559972000001,
            -0.1255337326,
            0.20145175999999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0752a8b6c7a878a88b448142929f6a9f3be2c1ed8c4201bee06a7d6faa25ea99",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08079141340000014,
            0.1850065541000001,
            -0.1434628785,
            0.20108227569999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a6454c26597b01d0276b684c62019f613b394f2ff7eaaf890673936236e2a537",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09937969340000007,
            0.12144844220000006,
            -0.07649667560000006,
            0.2033856837
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bd323451f9997167020ef8b4d4563d57e755f853e5a756382be5fefaf5d43de9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11534260590000012,
            0.1377183815000001,
            -0.08491343960000004,
            0.20327263869999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10814320800000013,
            0.1531883346000001,
            -0.10330714370000002,
            0.2030710824
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6b5bf2db39c7a5312bb922ccbb7f79eb56adc7b97c17b591d33d8da2a6250bc1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10088351580000014,
            0.17081535400000014,
            -0.1215320076,
            0.2027415785
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "edcf6df73115739f59495a635a2f6e95889a072a90f65715f3683de0279b6036",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09530802700000014,
            0.18649337480000017,
            -0.1394658032,
            0.20238098949999997
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "89ad7adcecda2efcf8cbd6a6401ed3e6ed96b851083accd850f6a0c518aa15b3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08951369220000005,
            0.12118552110000008,
            -0.07869682320000007,
            0.1995340188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fbe5f873390f4fa9623ed2084060dd9b386dcb41caa2b71b95f0f2129cf57a56",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08276762330000006,
            0.13683007370000008,
            -0.09717336800000005,
            0.1994031832
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07602672700000007,
            0.15241259150000008,
            -0.11538661190000003,
            0.19920162689999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8d2fb7a3cdb517396e8b9acf88ea220280c39c0d59402311d007504ddef79d5c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06906603660000009,
            0.1680606447000001,
            -0.13350011560000002,
            0.1988632277
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e2c8bb705339dcc5463a443085ff18111efcc79131fc23f37b0689f00224e812",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.062030188600000105,
            0.18366840720000008,
            -0.1514117757,
            0.1984848481
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e63647ca2002739cec51718c1fc3233e1fa1a415c34c193d001a7c1cd59f7a79",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10955248190000008,
            0.1244780651000001,
            -0.07415792900000007,
            0.200814942
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8d4112ab3315d7d1ddc27a4d870f5e4b35afd1d22a3825b4b4fafb3f73ad8f3b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10267023170000009,
            0.1401367294000001,
            -0.09264098280000005,
            0.20069300169999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0957454496000001,
            0.15578863700000012,
            -0.11090305860000003,
            0.2004914454
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1421bd391e699bf7e3db84dd519ed0f9abd810d6436050bef6fa5aac1639def6",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08855612990000011,
            0.1715250409000001,
            -0.129124919,
            0.2001530462
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d6db03d900f41c0c72fa21236bdcea5a570191d0749630206087c435ff3a8898",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08139132490000012,
            0.1872065926000001,
            -0.1470094219,
            0.1997835619
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5a99c08a7ed7f5f806cf0a005980f33c6f44c53c9af3ff9ec74ea537e9ac3156",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12976619970000008,
            0.12117539200000008,
            -0.06968226080000006,
            0.20210476049999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a01c832be39f3c46cd5b376ca93ac9936e7882bf59f762681abd6bb6e5fae186",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12278316340000012,
            0.14339398930000014,
            -0.08817966260000004,
            0.2019828202
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11565648470000012,
            0.15912774700000012,
            -0.10655276000000002,
            0.20178126389999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b66db6d06efa7d1e620ced97604377222cfc7a690e9e12414f834e4ae2dde28d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10831282960000013,
            0.17489325810000012,
            -0.1247130443,
            0.20145175999999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "290d66f51c3334521564ebbf587b2c8f96dd3feca2c2d788144f482ee2e0e5c3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10090862580000014,
            0.19064676560000013,
            -0.1427017006,
            0.20108227569999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fa155e38f105769756379f1664a8105153b41ea206f3fa703f1dea61f6e2fc4a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11602577420000004,
            0.12144844220000006,
            -0.07954871580000006,
            0.2033856837
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "26296eafe932dd4ff9512c67b6adb54a054d9512ee6fe088c015bb6b30ae16ef",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.14295023620000014,
            0.1377183815000001,
            -0.08388360590000005,
            0.20327263869999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.13569394920000014,
            0.1531883346000001,
            -0.10222808600000002,
            0.2030710824
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "20c920b02310daf4b859f8b813f29af3b4d257da9ba48b2d64b95f4328dde275",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12828551400000016,
            0.17816685180000014,
            -0.12043772330000001,
            0.2027415785
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4b29dc52dae93fa89372642c660f99eeca7df753f4baaa1174e66a58541fe27d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.12071372740000016,
            0.19399174850000017,
            -0.13839714649999998,
            0.20238098949999997
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ca6aa7709729328d94aa19e8129a8ec3f86ce1d32039e064fb623fbb8f1ac58e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08324080200000004,
            0.12169540350000008,
            -0.08017421610000008,
            0.1995340188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c4e015ead6169a716f5f5e9c559d43e096fc921f96389ef1a18f5749d64d333b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07641559050000006,
            0.13734995910000009,
            -0.09859623160000006,
            0.1994031832
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06968055530000007,
            0.15294748140000008,
            -0.11682706890000004,
            0.19920162689999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "dcaf4f81927c472859f6300f1b7ac9cec525bb1864c151d3d4070612ae8e5df4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06271910950000008,
            0.16860543760000007,
            -0.13488626130000003,
            0.1988632277
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "eb49287bc547c6e506f3aadb7eda6b7daada828a03319fcee65cf5fdd3c3fd6a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.055592245900000094,
            0.1842283046000001,
            -0.1527850957,
            0.1984848481
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8001ce7a61e6bbc527399ec1395b7cefc4fdc1a06d706c582a8a9beb5ebe3b02",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09662650990000006,
            0.1254928284000001,
            -0.07714746430000008,
            0.200814942
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "268cf23cf0dce23398307940260e0cecf8d96d17daf5edc865eaaa770f936901",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08963426050000006,
            0.1411765002000001,
            -0.09556958940000006,
            0.20069300169999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08266144870000008,
            0.1568534153000001,
            -0.11381216880000004,
            0.2004914454
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1543bfd39152b539b9476475cdaa1d411c13d91f416cbff3ba8211a1b4f61a45",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0755507988000001,
            0.1726148267000001,
            -0.13193356470000003,
            0.2001530462
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "11a928c621365eb7f902d7635a77ce6899022428a591ed6644c79dd42f8bf607",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0682570171000001,
            0.1883212859000001,
            -0.1498423697,
            0.1997835619
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d6db90ed5261d686d5775a7fe7c23cbce9b135bff6dee12a51a8f348722dcbcd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10991492550000007,
            0.12117539200000008,
            -0.07412046830000008,
            0.20210476049999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a71457d47e5c1fa6cd81dc8bc2295e36bc60f4d0e12fac791b33187fe27c62b3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10287090110000008,
            0.14490836140000013,
            -0.09257039170000006,
            0.2019828202
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09566709060000009,
            0.16071741220000013,
            -0.11087394160000004,
            0.20178126389999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "04c0ca5fbcf902e5b9afe76b36a90ca3ad2104030989324ad9d294df660cfa89",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0883791896000001,
            0.17652293530000013,
            -0.12895725310000003,
            0.20145175999999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "64ca51cf505764cc7dcd808efa152085d9373da22f33c6e151902050d8ddf2c4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.0808392333000001,
            0.19235173590000013,
            -0.1468859109,
            0.20108227569999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "26b18365a7e4237cc73053f1f6c404fdd94246aa4e16544ee34c6b1bfe516a85",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10526739570000004,
            0.12144844220000006,
            -0.07114022050000009,
            0.2033856837
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6c762a7a83d430eb4aae46bc3b939d9320278f039a0d1733b209ae55c6e64f75",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.11606633600000009,
            0.1377183815000001,
            -0.08960446620000005,
            0.20327263869999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1086446726000001,
            0.1531883346000001,
            -0.10795849500000004,
            0.2030710824
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a6346dd7e1804c75cf8dd0eb15ee8b4c4797741b2f0c1cb674ef99891c3fa9e9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10122484470000011,
            0.18032641740000016,
            -0.12605337250000004,
            0.2027415785
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d3c336ea2c30970cb838c9559f28ef5afffee91fabd06beb0c1839e49256766d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09357445800000012,
            0.19620132910000015,
            -0.14400203390000002,
            0.20238098949999997
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a38ca9017ee7323d6ca2fa38e717ced6f522427e0f6ce2d771d4ec8eeb087dcf",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07883757500000003,
            0.12240934710000007,
            -0.07855657230000007,
            0.1995340188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8f4a1199d5a21df79951d1f560023a1fa23122d88707a3f69ce4c077993f95e8",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07201236350000005,
            0.13803316400000007,
            -0.09705146900000004,
            0.1994031832
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06523248730000006,
            0.15370443790000007,
            -0.11528379690000003,
            0.19920162689999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4db6c5d5762841c37dc4de1bc30a10cd0e27c01bfab964bf6c8365bcc5313082",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.05827008610000007,
            0.16938039950000006,
            -0.13336364090000002,
            0.1988632277
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ffcbf75f862ff7b602b47b861df9fc8a853843804e38aef1f90875d90a3822e7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.051146167100000084,
            0.18505455240000007,
            -0.1512599767,
            0.1984848481
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b3b9838498a218b2c75976ab65e15e6c8076bb286d1ea658b3fbbf8b7e944b0b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08767094010000004,
            0.1268084114000001,
            -0.07389968040000006,
            0.200814942
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9aab49f04c34ce9b0218247ceb595fe069b32faa5bdcebea8b02ec4761a1c832",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08068497990000005,
            0.1425783694000001,
            -0.09233719500000004,
            0.20069300169999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07367361630000006,
            0.1583300466000001,
            -0.11060915970000001,
            0.2004914454
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6a052b308f6ab167426ab2a7e99b79c37ceafef5132f04f03ebf5c5e3dece9d5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06656671100000007,
            0.1741344709000001,
            -0.1287925453,
            0.2001530462
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "081a8609b5d2788de7dedead3776df8fed29be1556ee3ac5015b21181e073d7f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.05927061850000008,
            0.18986347790000008,
            -0.14669742589999998,
            0.1997835619
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "064c3f82e8595dcab77015ea88579873dec1e16e29d5a987e51204197ce9414d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09641330210000004,
            0.12034067250000008,
            -0.06919942910000006,
            0.20210476049999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c3a2b9e6812b3f6ca0f3a545088ae9cbf0150071f297f84c671e4ca96a08d7fb",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08932758130000004,
            0.1469766189000001,
            -0.08773934840000003,
            0.2019828202
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08213360460000006,
            0.1628276937000001,
            -0.10607017170000001,
            0.20178126389999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0cad56c70b53c6f45b92078a0eb03bb554e4515d6c3eca9cc7cee91426f915e9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07480755180000007,
            0.1787315156000001,
            -0.12422451409999999,
            0.20145175999999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9e3707d9ca4dd26f414d299f19d60bc43cbdbf2bf2b6da6219c626e1973457ae",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.06727362930000008,
            0.1946193339000001,
            -0.1422079526,
            0.20108227569999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4e816f70069fec6fbef680ba41095962ee77e9ff072ca18af5f553cdcfd997e2",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.10526739570000004,
            0.12034065100000006,
            -0.06458881190000004,
            0.2033856837
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e4fc4425fef1519fb6942a195045717cd0d7d9196af4d4bbd9def08121347069",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09792897700000004,
            0.1366085897000001,
            -0.08308344390000003,
            0.20327263869999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.09052079200000006,
            0.15207454160000008,
            -0.101480105,
            0.2030710824
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "40da851baa2cf49bf7ef0a57c4209c8c76198f9c0a177a116a76f059fcdf01bf",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08306261230000007,
            0.18317540760000012,
            -0.11965994709999998,
            0.2027415785
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b846a0a7e4c43066dab6457e533f7c7c435e82ee1372dd35cc746ba1dbbf7394",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.07538016300000008,
            0.19913634510000014,
            -0.13767923479999997,
            0.20238098949999997
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c1d8a606615698ddf47c3031611029291113243880ae1217cad057e45c700d20",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c50720a991912cf57e64843e363cd92942ce6eb32e71495fdf2d379aa22178ce",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "808b619229eb3831d151dbf64b022578c9b57e597e569a0ed8774173402d8b62",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "197cb980c6ca0e63ffc8281c85333c5035ed97c3bbda01e94aee39f0be2af570",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "645b39d903cbd22867ad10ccedf4d75d54bbf485460e27591d8057b79e20e92a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.1286549836000001,
            0.14532446900000015,
            -0.08516373320000001,
            0.20913895730000004
          ],
          "positive_window_share": 0.75
        }
      ],
      "trend": [
        {
          "config_hash": "1fec94aa0bead42b20075940b637e819472c020dce8613fa5a3c7aa21734fd06",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1999938459
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "adbca544282724c5a7a2958f71250737af4685caeb95879a42bc97e6fba41fa0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1999938459
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e731b06b6b8a57905247003db6fe52b6b03c796f946f86db5ff1d9a78d7bc936",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1999938459
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "46f7afbe4f52f52cf8832a43b79598af956b8e0d3541d6425464a97964d756c0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0efce7b04e5e193de8d96ae22d700309b50d9ec1b26b72a73c3a1a9f6769501d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1989344123
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1b03d2707a07fe802f1760263c82b3d4b8342a455e2139542829ce33055346c3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1989344123
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cc26b8dbf9aabc5a954cdba7f15445f6906c516ab4ca332c472c7970122b880a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1989344123
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "de68c4ccc59411bff11772363170338b6761dbd0f39bd7fc8c794de5cfd5259e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b3ab56d68fdcaada002d2614a264764fe445837a7212d9cef39fd0934e9a098b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1989344123
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c3b3386f66538a319e0467b3a0b591520efa06cc1ee02fe2bfe05a4bfdea1895",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1989344123
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8bf92734c3d2ba8e6c3dd7f599c5b43e34620f9479e5c24f9b34ccbe045b4947",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1989344123
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cf9cde26dba3c73a5567f30c5d5a03c684d25c008ef9fb3ad24b61ff1e53e962",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0c441452555d21094fcf63b740acffe7a9176260632649cedf006f78d5c922dc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1994093021
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "23d1e52eeccaf4bc0cb8853853c2be63a69dd7762b18d7289741c7e7f37b98f9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1994093021
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a5c471fd8ef46b803b80689400b2fc0c30d0ff6a0d4e6a27deb9881f27514916",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1994093021
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "37ce18ea991b11a33fd546c75664f8cafed609d4a7311f44011f1ac689f5ecbe",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c4ecea34d33f8e9ff517190ef1639a0078c204de4df752764eafe9f1f8ec39cd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988994389
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c4d5b093333d5f925ed448b6d6d3817b80258f4b6df0402ff62d7ff6e5de0d90",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988994389
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ddcf08c0eb422a69906267785f04df8ddf6ada327f9f7dbfc623ef071dcdcb28",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988994389
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "548bde01f4ae3b39c455be93505eda30b321c79668d9f8acde7f81aac0feefc0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b1ce106b9791d9b2313e33ad5d36230eb1a10a96118d83ef7b6350514a957bd9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988174966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bd61e6ffa991468a6062bf4047742d76be80658e74f9212ae8482ed6d90027cf",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988174966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9fcab2c463797c9b28ee01148cc476784bb2473b84bf8f2ae68c546f3cb9c946",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988174966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "61609ced85a7068bb6b227a8778db35ac30701765ed24a2d414765a7965417f9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1a8b7c2b566250e4974b9accd1eb288e0b1c3b9ece047603707261bce302dd08",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1994093021
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "07a6da34a90c5c24e8cfdef1b9c07e2ff039d51fce0b917d7a4ba2527844daa4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1994093021
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "441990e611d4bfed0a753adb7d990a66af9681ccb20bb032d058f3e3bf793c67",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1994093021
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d00659d885e156983f250b8d53e6c117947d0afc46d076fdcf1e024dacb4145d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bc6f099a3c49e384ab643559ec0ec44d65d442396a1dc177bb4c7181ac52ae54",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988994389
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "492d3075b7505d752fc4569124324cf50ec4e1e12399bff92d72a757be0abcea",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988994389
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ebab91384cb73c29a059a5f61ee4cb1db962fd86e95224f09308839b0f4f4a7d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988994389
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4266ee5cc6a9ac907f421389ef9cf425c951ac9475f81729c7ed50f0150b1b7d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6a23f24486bb79be48113d97b10bbba4ac19f7ddef0e43e81ec8d1dc67ff9092",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988174966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "be75d5c8e26860196c89f31b797698e558e2c7568cb1a802d2a09507366516ca",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988174966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9a5ffaf7d90c7cd06362d27f96a11d349d1b8f1dd81f180cf81cb93f13789ea5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06575185440000006,
            -0.026154181200000143,
            0.1988174966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fc714e5166dab9d576b2cca6b8263c9609f4ba786bf9b50769aa593b8e6c47d5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06986320680000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1a1d82ea59c99bfe7ac50c54c249f33eecaf9e8d07e4abf76bdd391e3652f99b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2017007797
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "915b629158bae600eedb793e1b7461db1bca2642934e70e963373d51bb0eec9d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2017007797
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "505ad729a6207cc8be7b2d3fe972a46ba111f58eeaa7b3b530a2cfa2e1d371ac",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2017007797
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "59b014959d6ca4769d4753c652daf0ccb38e962e5c3d4d3ea42fec5bd2a2a57a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e77bf2a8d1f196188c97d7cfc708d2f57c96d69e508253e83cf169f5c4d6c81c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1997959188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "add329e8e27ecebe1d584cb1f14ba572d35710aea60476ca8ccbc31431672993",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1997959188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c8d96d02fef2052aa1b5b4f37d053341689597b833962dea2b09040dda9cd81d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1997959188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "64e8b768141ab52605621addcd48eb9cc31b1ffcd58858b53f7d3015b5511af3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1997959188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9a8031973c8ec766ac9566a91c4f700fd8d2a7712f8f4e3641c67b8135e77bca",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1997959188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4a09e9f42c304e0c0f941aa4fb00cfc45f473ebaa326e8c08008a0a2a91e8d4c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1997959188
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c54abf54583ce691431dbb42312227a0d225834bfc9a325757243da770f414aa",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "387050649e85b36d7c6e999764671f946e30e8f6587f959815efda2fee8967c9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2005307938
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6d0b27b35b089a17eb96ff6e8962cf760fda88c3a3d4da56f20518c119a22fea",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2005307938
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7e25e305550d53d8dd69c7eeb54c0b6e13240426682cf97ea575590254e15a8f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2005307938
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "09c907ccffba9c79389da45ffbc273ef56ff552a01e37bb47bf4b4f538584933",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "330e9079a8741ac5ed4d998877d62b08834a5251908efa8b14fa9b09f101662a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.199492858
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "eadf7cacdbca92462104fbb663d7c89152d0846f8079544838f53c144e80b383",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.199492858
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2c75c42046ef3a6d0f0febae245bcf1a0d429394847dcdc593062e759c731b73",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.199492858
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bdfeea35c79ba78c3054cc430396a6f0454ffcb4c0eefca49e78830b92de5ccc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3d16b6890afaf109d0c4451863565fe56cb71dd1454039aa22d95648f62fe42d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1994382298
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e22018ff8811c7b7c47fb6ee98be4a18af5dd760741f1521c9a5e5246a5dcead",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1994382298
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4c5dbff3038888fbc8ba660d551023c7213bc3c92e7d698161e4831ddb927e16",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1994382298
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f985f1617e9bb77ea62699fce58cc6011e56a4fb40c9d3565f854b8ed05f5e4c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1a0ba2f00044f420ffb20d85ffd3b630915c4f0587b631a9e61e8fc68b943b2c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2005307938
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ae2f1ec1405653fbbf289a5f020fe4b9ab1365648959be0631bcd1db772eadad",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2005307938
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "50aeca7dbe7571cfa0dd145f2032d40a70a44efb66da2450d2ac21fc20d8ac95",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.2005307938
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "02ed4b871a3ac2dc98111f5f7dba62b21c61af723cae0b25f7d3fa568b6642e4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "13e36312d75235095a99fb4673caba20941b36b205e0f88c729e7bc1900c423e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.199492858
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9755e4a2985929b24476e74975b3281dcf102f99fc184339e833c99c9365e566",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.199492858
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a2606ff0dd53e64bdaed4879ebef55587c576527665e09aaceec8068c023f1fa",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.199492858
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0a073f60f2b4e958cf7bb14f680436f06eb26b748c281a78271005a1011caa57",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "42105ee5fa31f194122fe24f85377d35b1afea27da9bbed7fe4efa1b04df9b81",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1994382298
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b4a19d9ee57a1ed883fc45f2d940417ba33b9bcd8854935c3d9ed02a29df5c44",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1994382298
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a05a3729a4575c24923de713a0ba59f30f2cfd21472905bb9a557e2e85fe5392",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.060308650900000066,
            -0.026154181200000143,
            0.1994382298
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cd978ede184d59c0797473a5f7cf0173d393d3398a9aa841a8dc97ea58a53cb5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06832432840000006,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c1144d55f4b001966183229609c62f71533195749e340dc147b58b34996d34b1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2034086118
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b7aa686834fba404e57ce646e62ea5ae9ce6b33df36f634aa733cced8430673f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2034086118
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b7c893047999c7d6c75f8da734604fb8e463ffc56e36cbccd00fa3732bfff73c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2034086118
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c2faa48b20285145059a9507df7fb128457be7916c87597372a667e3535514da",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "376261879bb3a98cb9d9f885ebc4606248424ee5623184ed545ba758deb3d361",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2008114286
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1c9aaeaf1c01aaa86bd6f9b2a9def8c7f55b76815b48c037012df2db186a7ad9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2008114286
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "53ae75468006b31323bf7c8217cd72f20b714d1c350e56945d1b7cb891a67f57",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2008114286
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "dcbdfc7b407f6dae2709dbf78aaa01157de1752506623e224a3c54d9dcbd44cc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d1a7f1bab43c17c56cf770ea8414ee06ce61b60f10d4a20f8959f14d48824bba",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2008114286
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bfc4d87ac49a11a984a17ee8bc2a235c4905e425284c08722bc83a3787c3da0f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2008114286
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "90e95eca032bfe50e881261b29e392fa034ba82c6ca75e51bb44c3dd72c9275c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2008114286
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ec4085c7e24702acce52ee2a5997e551a4978c5f8741df94c163d6422bc23f7c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "696913cb4f51a33bf3935b51da3b38e1dcd6d1a97557ef171529553b4d7bfbf7",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2016340761
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f403091f4d2bc6ab744045f21d94ccd7cdb6bb69adac3cb07ebeb46eaf36f684",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2016340761
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6fc8e2eef32a9bbeedf4d1623087ba3891701d13c78d22843cdf57a1c9bb12be",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2016340761
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c2209a5b405bac286c73284d9fc581c16a425d179dcff71abdeaa8710254fe0f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "52db97a65a1d4ad3cfa5799f59629bcab32d4cb9e84027e5ec07afc0fc759dea",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "520cb3507a916dc9d9f2fa51dacd4e7c3511bbf9eee1fcdf03da237bb9f07e11",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "74615fd57e7c943c143fd077540a3361517eb745a26477811b844f682456d219",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e9e04869e6239071f9dd8cce64bab3d8eeb7ca305ff95b34978dc8aedbbd705c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "13a36acfc6269b30b569bb601b5e16abcb027c50365afdcb43ae693eeb166958",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d576233a8b8830e3532da4d368e8f230e4de74243f423ae4693135f0662ad5a3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "44cb7392c928f53c521015a2cd2d0d65ae8766b2261ffc6f5861bc3196ad086f",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b5ae512c057c4cca149fc22aa5ab060d43221cfcfb62184e6b988b8670e045e0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ec7cbbe41821b4534745fc5abe749c3fa818c012a03773917d564783155e3c9b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2016340761
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cd308639566094e1248179f35cda2c75f4b3f108d88965087b313c6e2c18ad0c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2016340761
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "45fc69735e2a6498f6345128fd7d46a7e5ad7bc5aa540c5fe68355a5a078e402",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2016340761
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ce25616a08a3a713d3baa8fbe9c681a24d2d0ae6253ec78d562b4a0e52cefb9e",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f3b1956a637c63c935fb3bb6eb3e713d0e7881edf280d7cd43341778f5d206ec",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4ef5f2e60b0a12f9c3dfdfc50ff212dda872ca3811ba7eb1a418cd635500ee86",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f38dda51d631dae80a08a0027a6f82f3f06d6328bca9e8c207522a8316d0a562",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5bf8412a3fe2565df7fe2ecd3cf0bf8ef854466aaaa317215f6937328ff3ab18",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1b8a1433cd25010fb5c550b3665e973d63467cfe7baa46e828f42e0e3914c235",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6c62868387b90bf0e5d50a007eb97dff2c5f410ac777bb74e949f24ca4545cd4",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bf18cc0ff8f31c28dd27bd53bea9a4b8740f08d9cba11a3a14cacc6d1091b9ef",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.05485842010000007,
            -0.026154181200000143,
            0.2001409053
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "f08a6c33adf0cb5410922ccb5eb4e34f92024956a5c0332e80e647bee7cb2a01",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06678545000000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2051294478
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "161dbc35e812294ca418d3a491ac83452d7dae568d1e5be10421ee4e19fdab27",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2051294478
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1e3c5a3a25ba0ff260f82888076b19bd3e2497627e62d17545f54d5382b673a9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2051294478
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b9bc2fd53b37952d0fa31d7ee6c7abb2df29fc0c936f761b0b4d5de89d3b3c65",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2019966405
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a164ba23ba9524e034fe07bfe24aea3b27db569bc592dca70655d980b21fcdd3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2019966405
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "fd3352c6d16146fc47234c6239e5393864ac990b33c70cd0570d7c36192d1a49",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2019966405
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7ec3d94889c6256057b589f9a9349e6f11c29591facbfc6dd184ffe7dc58d8de",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2019966405
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "42881131aa958b37001b7427d92d5475137405fe28d79f77e10b24316f77ab3c",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2019966405
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ed0dd236355b7a8d9f42cd954e2aba0cca2d130aeb2e511c8145e52b3b5c9229",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2019966405
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a7e3098ae1d238b85a68bf710352484a836546f125d4abdecafda4bd5b6ce8e1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2027603653
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "275334c7d66460505e7c71e7f1bc8e971d6b44f3af26a6b8dba212d744d4d00a",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2027603653
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0dee04873a3ddf671052ea481c0d968718285776ddcfc900e5af011213ad542b",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2027603653
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "8538b7affe3bb97a027406cdbf0ee82edbf2a14cf9b0164e0f3b16e518dcce49",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "707d5fac1ebe3f88df9b8bca06082ec5f029dbaaa67f900f17bdbb99418ae959",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "12643fc27869a63bcca87e3e38c0aae6f7825f6728622759920ecebf182931d1",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2d4e420f979f519ab7261ed8c86ca8308618af6e63b56f5476e2d2fce0fd8a14",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bcaf1067a4e98787b432db5b6681a208b9eea62150fe336c1090df3b4f678dfc",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b54d6a3fa555012188e6f740379a78f0dd22cd68864cae4eb9e915ce67e8baaa",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "17c9c940096d43a773c4905d1982dc3a9c901fae82b8de14cfb27f6844ce84c0",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2027603653
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "091fbd2cc185b592a8e7b80f30e3e73fb8f3034ef10dcb197ae208d1892901d3",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2027603653
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "17dbff0a23e5d013e2d4b110485364f1d520f1dd5b5b79ea9cec2328e6048ff9",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.2027603653
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a7d1bc64be18eec70f804ccb675f4de3265988e1f7041b8dac11721a645fbccd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "512697187c6fe64646e9ff21e491e8e481880ebae3fbd0e5138c76ee036ec1d5",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "673a28cda6786a76d77f41b3d518b2dc00aa5c1482c95959af2c5318831043bd",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "64e6f60cccaa85fd39f8b1fa74bc32547aeab8eb0fc0ea90356ebdca81ab94da",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "891e4aac1326376aff627803dcff3b5d016adb3f7c1d241c033375b50f4f5659",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4bfb9404f1e53fa2d8ba993a154c73bc83122dfdb210429965cadb5122d6cb5d",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.04946678990000007,
            -0.026154181200000143,
            0.20094853000000001
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "443522543e3e8dd041a7ffeee4af344efccc3ec16395b525bc91265308a4d846",
          "positive_windows": [
            true,
            true,
            false,
            true
          ],
          "oos_returns": [
            0.08969982,
            0.06524657160000007,
            -0.026154181200000143,
            0.1983878104
          ],
          "positive_window_share": 0.75
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
        "513330.SH"
      ]
    },
    "experiment_hash": "09cdb15d5967cc4e327076efa33b3658a84862d4c05cdc4793bcd54c12cb1ec1",
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
            "cost_drag": 0.0011314021,
            "cvar5_improvement": 0.035804752280420724,
            "drawdown_improvement": 0.2242970078507825,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6857630468606124,
            "sortino_excess": 1.2190673469287105,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020688377,
            "cvar5_improvement": 0.03508710776876046,
            "drawdown_improvement": 0.2204302608629929,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 1.0893940053439175,
            "sortino_excess": 2.214483977020983,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00147866355,
            "cvar5_improvement": 0.026176897557282978,
            "drawdown_improvement": 0.18129600619831382,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.46497411415305995,
            "sortino_excess": 0.8746786995902022,
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
            "cost_drag": 0.001020745,
            "cvar5_improvement": 0.035554874998589434,
            "drawdown_improvement": 0.2212179471226885,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6642487795777595,
            "sortino_excess": 1.1050140433370053,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00391612875,
            "cvar5_improvement": 0.01957806061006534,
            "drawdown_improvement": 0.15106195359196353,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3010315694711635,
            "sortino_excess": 0.5664839431252806,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001898230325,
            "cvar5_improvement": 0.02215709783890818,
            "drawdown_improvement": 0.16607720757155084,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.40169830019172587,
            "sortino_excess": 0.7776825449992578,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016042634,
            "cvar5_improvement": 0.022021754627407835,
            "drawdown_improvement": 0.16718930783707517,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.34416804930207434,
            "sortino_excess": 0.6603404707719236,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0030446425499999997,
            "cvar5_improvement": 0.028930343638997272,
            "drawdown_improvement": 0.19526603397890782,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5327212665612397,
            "sortino_excess": 0.9680982947519936,
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
            "cost_drag": 0.0033092571,
            "cvar5_improvement": 0.02644251677243557,
            "drawdown_improvement": 0.18450228009942313,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2050427507297672,
            "sortino_excess": 0.48335380259283467,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016542209500000002,
            "cvar5_improvement": 0.02606975757123295,
            "drawdown_improvement": 0.1838838890868383,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3925079739203897,
            "sortino_excess": 0.7799598414426713,
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
            "cost_drag": 0.0036893597999999995,
            "cvar5_improvement": 0.023118941474154116,
            "drawdown_improvement": 0.16927573136724303,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4722185772946495,
            "sortino_excess": 0.8678510737440636,
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
            "cost_drag": 0.001499993175,
            "cvar5_improvement": 0.02601038307443214,
            "drawdown_improvement": 0.1832341383131529,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.477666112441933,
            "sortino_excess": 0.8726824819906155,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00163374315,
            "cvar5_improvement": 0.03217471454878881,
            "drawdown_improvement": 0.2094099654874383,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4417958766062793,
            "sortino_excess": 0.8564995849889578,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014465014500000001,
            "cvar5_improvement": 0.030241437707501685,
            "drawdown_improvement": 0.1979136686816235,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7108786672680923,
            "sortino_excess": 1.2813657893771435,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015869477,
            "cvar5_improvement": 0.022193683185793442,
            "drawdown_improvement": 0.164992068345005,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3386196271300682,
            "sortino_excess": 0.6534481738988072,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0027358342749999997,
            "cvar5_improvement": 0.031522953289147275,
            "drawdown_improvement": 0.2072678452936378,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8824178383006989,
            "sortino_excess": 1.5961339875587992,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015119970000000002,
            "cvar5_improvement": 0.02584097622766213,
            "drawdown_improvement": 0.18051698255971835,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3917601945709385,
            "sortino_excess": 0.7427628280000387,
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
            "cost_drag": 0.00141954475,
            "cvar5_improvement": 0.025520014424139786,
            "drawdown_improvement": 0.17904083702605364,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.357329092308159,
            "sortino_excess": 0.6825775670450228,
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
            "cost_drag": 0.001619617925,
            "cvar5_improvement": 0.030017035882363007,
            "drawdown_improvement": 0.19925620949568904,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7377376618372828,
            "sortino_excess": 1.2826334300813813,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002095535275,
            "cvar5_improvement": 0.02211712469349869,
            "drawdown_improvement": 0.16656432699588067,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3381369988822593,
            "sortino_excess": 0.6492098138767461,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0032617699249999996,
            "cvar5_improvement": 0.02342960477219777,
            "drawdown_improvement": 0.169989989101433,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36389511621177983,
            "sortino_excess": 0.7031388291551668,
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
            "cost_drag": 0.0025636564249999997,
            "cvar5_improvement": 0.0292642357467754,
            "drawdown_improvement": 0.1941912661761145,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9374638755199995,
            "sortino_excess": 1.9676405437773696,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00135084955,
            "cvar5_improvement": 0.03271119825542717,
            "drawdown_improvement": 0.211879703593211,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5560689832463195,
            "sortino_excess": 1.0115749823300897,
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
            "cost_drag": 0.0029967214,
            "cvar5_improvement": 0.020216922659498933,
            "drawdown_improvement": 0.15821595938899624,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2528550375281089,
            "sortino_excess": 0.5067561135275921,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001627239525,
            "cvar5_improvement": 0.0249989775408622,
            "drawdown_improvement": 0.17824506601471343,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3372076691210078,
            "sortino_excess": 0.6534630442629884,
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
            "cost_drag": 0.0031488389999999996,
            "cvar5_improvement": 0.0228401111269005,
            "drawdown_improvement": 0.1669059136798612,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.634579357144757,
            "sortino_excess": 1.1382229520540357,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001201922825,
            "cvar5_improvement": 0.027966368479933976,
            "drawdown_improvement": 0.19105981479833925,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2666085923629199,
            "sortino_excess": 0.5126910610153275,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0037221614749999997,
            "cvar5_improvement": 0.024045231650038433,
            "drawdown_improvement": 0.17267643101291452,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2773581527429126,
            "sortino_excess": 0.5626989084675619,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002373530425,
            "cvar5_improvement": 0.031916167087811455,
            "drawdown_improvement": 0.20709252801546585,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6757730831206377,
            "sortino_excess": 1.1699863430964748,
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
            "cost_drag": 0.0014783721,
            "cvar5_improvement": 0.02830975371771613,
            "drawdown_improvement": 0.19327157116162955,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3125454692561897,
            "sortino_excess": 0.6036468741901858,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016627662499999999,
            "cvar5_improvement": 0.027205923519716145,
            "drawdown_improvement": 0.18510812446896135,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.663270384424128,
            "sortino_excess": 1.2022240034717948,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001652199125,
            "cvar5_improvement": 0.03582192258495632,
            "drawdown_improvement": 0.22121944900179047,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 1.1849081875088316,
            "sortino_excess": 2.576812674647927,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0028265570249999994,
            "cvar5_improvement": 0.023530123756371497,
            "drawdown_improvement": 0.17201083954194427,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25490667649805404,
            "sortino_excess": 0.5042426617886492,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0021827383,
            "cvar5_improvement": 0.02854372608184236,
            "drawdown_improvement": 0.19407521211796938,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5224029828003979,
            "sortino_excess": 0.9316835366230196,
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
            "cost_drag": 0.00204935885,
            "cvar5_improvement": 0.023671600273434276,
            "drawdown_improvement": 0.17325024057121707,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5430757727424991,
            "sortino_excess": 0.9797620427072739,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00428741555,
            "cvar5_improvement": 0.02085036221798194,
            "drawdown_improvement": 0.1599613040311213,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29701599098456427,
            "sortino_excess": 0.5907963188856613,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002956622225,
            "cvar5_improvement": 0.029784764326769776,
            "drawdown_improvement": 0.1981384453957467,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44115010626063167,
            "sortino_excess": 0.8085039732367805,
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
            "cost_drag": 0.0014349445499999998,
            "cvar5_improvement": 0.03196765502008893,
            "drawdown_improvement": 0.20799652924282663,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5581924866833025,
            "sortino_excess": 0.9862303460580896,
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
            "cost_drag": 0.0014959305,
            "cvar5_improvement": 0.029374198441344937,
            "drawdown_improvement": 0.19820443207832403,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.43261212784253916,
            "sortino_excess": 0.8424923894768108,
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
            "cost_drag": 0.003429584375,
            "cvar5_improvement": 0.020223810767906705,
            "drawdown_improvement": 0.1562696312333498,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3446396964972777,
            "sortino_excess": 0.6788699067513972,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013109088750000001,
            "cvar5_improvement": 0.03313643926489076,
            "drawdown_improvement": 0.2103205741705657,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8420669531519229,
            "sortino_excess": 1.3724503260779009,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022685762,
            "cvar5_improvement": 0.021333442222734693,
            "drawdown_improvement": 0.16392363401294344,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29281450866146447,
            "sortino_excess": 0.5689371591014204,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00112652825,
            "cvar5_improvement": 0.0321680292757107,
            "drawdown_improvement": 0.2078524635836013,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4394023039345445,
            "sortino_excess": 0.8189922878242467,
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
            "cost_drag": 0.001022496225,
            "cvar5_improvement": 0.035211859846101035,
            "drawdown_improvement": 0.21941420947635637,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6358850105792315,
            "sortino_excess": 1.3028783461607867,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019282397,
            "cvar5_improvement": 0.02269509752754593,
            "drawdown_improvement": 0.1694687171431342,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4096394811059517,
            "sortino_excess": 0.7883074349978774,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001749079875,
            "cvar5_improvement": 0.023418509012516887,
            "drawdown_improvement": 0.16942954324076234,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4770059513373798,
            "sortino_excess": 0.9070799435805728,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00418542585,
            "cvar5_improvement": 0.019303292288993478,
            "drawdown_improvement": 0.1499520634013759,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3278801752663809,
            "sortino_excess": 0.6012435807298353,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00230466105,
            "cvar5_improvement": 0.027667106457837647,
            "drawdown_improvement": 0.18384399371160726,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9325122085614441,
            "sortino_excess": 1.6388501017397017,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013472437500000002,
            "cvar5_improvement": 0.029678119308776594,
            "drawdown_improvement": 0.1951447061969476,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5776534514300523,
            "sortino_excess": 1.0475868778061301,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001334669625,
            "cvar5_improvement": 0.03296123454795695,
            "drawdown_improvement": 0.211409546386445,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6994796499247132,
            "sortino_excess": 1.2255594844522915,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00109211765,
            "cvar5_improvement": 0.034557384947843835,
            "drawdown_improvement": 0.21982658104326397,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30069907713601957,
            "sortino_excess": 0.5714548201254154,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0025234107749999997,
            "cvar5_improvement": 0.03026056172408091,
            "drawdown_improvement": 0.20047603682835857,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2789282230251076,
            "sortino_excess": 0.5488197587982725,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002540573475,
            "cvar5_improvement": 0.021367091521105677,
            "drawdown_improvement": 0.1628590195384724,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3108133248334243,
            "sortino_excess": 0.5867820814478647,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00218090235,
            "cvar5_improvement": 0.03090606310479799,
            "drawdown_improvement": 0.20200551330505814,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9251975532581482,
            "sortino_excess": 1.6048415032047787,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0038315686499999996,
            "cvar5_improvement": 0.02052384704246507,
            "drawdown_improvement": 0.15796857388997793,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4342810252845486,
            "sortino_excess": 0.8046606875769634,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001639211425,
            "cvar5_improvement": 0.024954227375445073,
            "drawdown_improvement": 0.17901857140829458,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29548967057893843,
            "sortino_excess": 0.5775845656607279,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00126078635,
            "cvar5_improvement": 0.028869273158186024,
            "drawdown_improvement": 0.19333768975473103,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3879766876677347,
            "sortino_excess": 0.7328141341811482,
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
            "cost_drag": 0.001565908675,
            "cvar5_improvement": 0.02659172127427191,
            "drawdown_improvement": 0.1828772261704067,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5961923869148923,
            "sortino_excess": 0.9999213110661951,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001956102275,
            "cvar5_improvement": 0.030138825343195626,
            "drawdown_improvement": 0.19730236090236167,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6992856490295422,
            "sortino_excess": 1.2603186041829777,
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
            "cost_drag": 0.0030613833,
            "cvar5_improvement": 0.030651020735152468,
            "drawdown_improvement": 0.2016506497381969,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1788638246635146,
            "sortino_excess": 0.3663828819847653,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018001731,
            "cvar5_improvement": 0.03140591741246192,
            "drawdown_improvement": 0.20667249180592667,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3571897684526215,
            "sortino_excess": 0.686166643537814,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002722464475,
            "cvar5_improvement": 0.02282161276654895,
            "drawdown_improvement": 0.16659010903835977,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7394238629223994,
            "sortino_excess": 1.3134073218010751,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001467915975,
            "cvar5_improvement": 0.03258232999799448,
            "drawdown_improvement": 0.21167951553580877,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5740391427757504,
            "sortino_excess": 1.0010673369680565,
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
            "cost_drag": 0.002067639675,
            "cvar5_improvement": 0.024142977484348335,
            "drawdown_improvement": 0.17446687605643366,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6902761510391853,
            "sortino_excess": 1.1657811159342342,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012743343500000001,
            "cvar5_improvement": 0.028676929856465805,
            "drawdown_improvement": 0.19538453893602992,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3966466644043096,
            "sortino_excess": 0.7395530322289602,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001725948975,
            "cvar5_improvement": 0.02166146575572376,
            "drawdown_improvement": 0.16515538107649724,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2658146194772553,
            "sortino_excess": 0.5396238122327349,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002675785525,
            "cvar5_improvement": 0.025568846530913996,
            "drawdown_improvement": 0.17914897026590132,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5110607789193923,
            "sortino_excess": 0.9318866432543566,
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
            "cost_drag": 0.0037358928249999995,
            "cvar5_improvement": 0.0217477730552196,
            "drawdown_improvement": 0.16070138079947302,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6561067802403576,
            "sortino_excess": 1.000097856642056,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001944606675,
            "cvar5_improvement": 0.032963762635973164,
            "drawdown_improvement": 0.2074208799945466,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 1.2073450230706475,
            "sortino_excess": 2.5852034031044253,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001824241775,
            "cvar5_improvement": 0.02409010456708004,
            "drawdown_improvement": 0.1720233447847123,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5954247149784999,
            "sortino_excess": 1.1135222833799074,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0036062463750000003,
            "cvar5_improvement": 0.02507544410520176,
            "drawdown_improvement": 0.1746274023091659,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24788222426858642,
            "sortino_excess": 0.4326003585291028,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013715533999999999,
            "cvar5_improvement": 0.024562449223222448,
            "drawdown_improvement": 0.17788595236640792,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26064810450161446,
            "sortino_excess": 0.5076972533913136,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003706739075,
            "cvar5_improvement": 0.025402934369652394,
            "drawdown_improvement": 0.18218323769735362,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.302567597981547,
            "sortino_excess": 0.6799214972031618,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003165816125,
            "cvar5_improvement": 0.02362238054312272,
            "drawdown_improvement": 0.17047158931335976,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.840097093923527,
            "sortino_excess": 1.5620961301372605,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001064841875,
            "cvar5_improvement": 0.03522506561309218,
            "drawdown_improvement": 0.219435825308118,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7136273579431304,
            "sortino_excess": 1.3361318824492046,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020119852,
            "cvar5_improvement": 0.03427291140498965,
            "drawdown_improvement": 0.21778214441853577,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 1.0152328797027774,
            "sortino_excess": 2.2793268982092436,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0031840411,
            "cvar5_improvement": 0.028918337185509707,
            "drawdown_improvement": 0.19589781920395077,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20073123483831146,
            "sortino_excess": 0.490786235813779,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001345955475,
            "cvar5_improvement": 0.03166470228575873,
            "drawdown_improvement": 0.20776133436874106,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.34287740298632996,
            "sortino_excess": 0.654195745081344,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001983501,
            "cvar5_improvement": 0.030455294236379975,
            "drawdown_improvement": 0.1971818979724312,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8293056382923951,
            "sortino_excess": 1.5646801445152527,
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
            "cost_drag": 0.0017962253,
            "cvar5_improvement": 0.021693178177330102,
            "drawdown_improvement": 0.16421258039675452,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3213579574415409,
            "sortino_excess": 0.628386719411623,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016665177750000001,
            "cvar5_improvement": 0.034693633414452786,
            "drawdown_improvement": 0.22113424571955448,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42299812426037103,
            "sortino_excess": 0.7921399514326399,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00215204415,
            "cvar5_improvement": 0.03050184384269618,
            "drawdown_improvement": 0.20155554945697973,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5915905817216905,
            "sortino_excess": 0.937630861591047,
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
            "cost_drag": 0.002113648525,
            "cvar5_improvement": 0.02693964643646592,
            "drawdown_improvement": 0.18428248848271317,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6047613960862117,
            "sortino_excess": 1.1550086811215918,
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
            "cost_drag": 0.00111004865,
            "cvar5_improvement": 0.0359435624559933,
            "drawdown_improvement": 0.22350433224085683,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8271852051535074,
            "sortino_excess": 1.3661017418698782,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00227686645,
            "cvar5_improvement": 0.02366369230578438,
            "drawdown_improvement": 0.17139790936329122,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5437366707914211,
            "sortino_excess": 1.059545277402726,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034675124,
            "cvar5_improvement": 0.025888067577774457,
            "drawdown_improvement": 0.1818454150064594,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4974874970324086,
            "sortino_excess": 0.9109404229147963,
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
            "cost_drag": 0.002098695075,
            "cvar5_improvement": 0.024676465440456572,
            "drawdown_improvement": 0.1780727493447454,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30376514341572447,
            "sortino_excess": 0.5825134835671301,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0038219702,
            "cvar5_improvement": 0.023138763560264435,
            "drawdown_improvement": 0.17157716416516477,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26398543563197174,
            "sortino_excess": 0.6008868195992256,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001642488,
            "cvar5_improvement": 0.02295410371012687,
            "drawdown_improvement": 0.1672259349411692,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4293190398867286,
            "sortino_excess": 0.8194576877242511,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017571891,
            "cvar5_improvement": 0.02684507561949402,
            "drawdown_improvement": 0.18646454274774205,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5271680244168062,
            "sortino_excess": 0.9643431523351427,
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
            "cost_drag": 0.0015112803,
            "cvar5_improvement": 0.029931226043571,
            "drawdown_improvement": 0.1993262692531062,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.590334089676217,
            "sortino_excess": 1.0522337231293521,
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
            "cost_drag": 0.0016945850000000002,
            "cvar5_improvement": 0.021017160208869422,
            "drawdown_improvement": 0.16237500043820466,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24588999064732203,
            "sortino_excess": 0.48996186801297137,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016390913,
            "cvar5_improvement": 0.029902433849098277,
            "drawdown_improvement": 0.1993262692531062,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.694236102028509,
            "sortino_excess": 1.156606935438349,
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
            "cost_drag": 0.0014341508,
            "cvar5_improvement": 0.025344541717730436,
            "drawdown_improvement": 0.18124896953928302,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3639540967641516,
            "sortino_excess": 0.6896060046902637,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018387113250000003,
            "cvar5_improvement": 0.025812583451189836,
            "drawdown_improvement": 0.1814282294359155,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5322106482250916,
            "sortino_excess": 0.9692478310385046,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014296376,
            "cvar5_improvement": 0.02988321630024501,
            "drawdown_improvement": 0.1976811790216835,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5938179697689276,
            "sortino_excess": 1.1029340276409139,
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
            "cost_drag": 0.001184599,
            "cvar5_improvement": 0.03253072274476438,
            "drawdown_improvement": 0.2072870686210364,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6848378954185619,
            "sortino_excess": 1.1090929001361596,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003099043125,
            "cvar5_improvement": 0.0288363070600304,
            "drawdown_improvement": 0.1954179801632948,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8634076376222843,
            "sortino_excess": 1.4201110928489264,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00152323035,
            "cvar5_improvement": 0.02436622833535239,
            "drawdown_improvement": 0.17639527139493927,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24809730318114537,
            "sortino_excess": 0.48954273492680034,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002463908825,
            "cvar5_improvement": 0.024630525619203016,
            "drawdown_improvement": 0.1718815895247866,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7859440093237726,
            "sortino_excess": 1.3572459840064288,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013404738750000002,
            "cvar5_improvement": 0.029327459228770756,
            "drawdown_improvement": 0.19625814284074808,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5360076297070322,
            "sortino_excess": 0.9373256726117585,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001885578975,
            "cvar5_improvement": 0.026821215932764278,
            "drawdown_improvement": 0.18646454274774205,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5995992926204008,
            "sortino_excess": 1.0414852234689644,
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
            "cost_drag": 0.0037659810249999997,
            "cvar5_improvement": 0.02229830345508614,
            "drawdown_improvement": 0.16242551436619848,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2870182145343224,
            "sortino_excess": 0.5074719212292161,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0040443930749999996,
            "cvar5_improvement": 0.02169286649400718,
            "drawdown_improvement": 0.16125878770153426,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36286895831577093,
            "sortino_excess": 0.6476730118815435,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012605588,
            "cvar5_improvement": 0.03572826183119057,
            "drawdown_improvement": 0.2242970078507825,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8638239522620919,
            "sortino_excess": 1.3703256324635342,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019355099,
            "cvar5_improvement": 0.028032162751573487,
            "drawdown_improvement": 0.19245123651258678,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.32306257688896417,
            "sortino_excess": 0.6300761090719851,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002079613575,
            "cvar5_improvement": 0.030235022633357478,
            "drawdown_improvement": 0.19529011329049967,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9668575277228869,
            "sortino_excess": 2.0561108847446863,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017609739249999999,
            "cvar5_improvement": 0.02598992024838108,
            "drawdown_improvement": 0.18353000972569894,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44176446909778355,
            "sortino_excess": 0.8378714397776876,
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
            "cost_drag": 0.0009923675,
            "cvar5_improvement": 0.035428217334896005,
            "drawdown_improvement": 0.22229236936022675,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5344328395218108,
            "sortino_excess": 0.9591836640007085,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019195336,
            "cvar5_improvement": 0.023704589265075023,
            "drawdown_improvement": 0.17325024057121707,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.48234117502838797,
            "sortino_excess": 0.9137736375936353,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0036791706,
            "cvar5_improvement": 0.02360956279981332,
            "drawdown_improvement": 0.17093161289192169,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7223816684465838,
            "sortino_excess": 1.1299944870081584,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014854124500000001,
            "cvar5_improvement": 0.03287013572845693,
            "drawdown_improvement": 0.211409546386445,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8752761129355549,
            "sortino_excess": 1.3736597736911889,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00313018895,
            "cvar5_improvement": 0.02624329021726724,
            "drawdown_improvement": 0.18057567046077042,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18534476557785,
            "sortino_excess": 0.33499934998998115,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
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
            "cost_drag": 0.00122650715,
            "cvar5_improvement": 0.031137396811761496,
            "drawdown_improvement": 0.2050882649240469,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.26900372359183095,
            "sortino_excess": 0.5182416918042517,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001012969275,
            "cvar5_improvement": 0.034977590870248765,
            "drawdown_improvement": 0.2210239506496939,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.35334104482028306,
            "sortino_excess": 0.6563175661793084,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001270483125,
            "cvar5_improvement": 0.03549359534076158,
            "drawdown_improvement": 0.2232454966035096,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8257330743561565,
            "sortino_excess": 1.5981757452776248,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00111868055,
            "cvar5_improvement": 0.03560369640845864,
            "drawdown_improvement": 0.2232454966035096,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6204619457198961,
            "sortino_excess": 1.3754017631592583,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0033147474750000005,
            "cvar5_improvement": 0.027814994384203,
            "drawdown_improvement": 0.18751658778105432,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25629797687660866,
            "sortino_excess": 0.4204293887525409,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00147920075,
            "cvar5_improvement": 0.032669476923602656,
            "drawdown_improvement": 0.21142543809948786,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.672087309437416,
            "sortino_excess": 1.1081020010630052,
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
            "cost_drag": 0.0014393731500000001,
            "cvar5_improvement": 0.024766365464509027,
            "drawdown_improvement": 0.17754311804691345,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.27305152781520386,
            "sortino_excess": 0.5261742976398218,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012203265,
            "cvar5_improvement": 0.03248152203242569,
            "drawdown_improvement": 0.20936451039968673,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.49722384229706973,
            "sortino_excess": 0.9303026436995092,
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
            "cost_drag": 0.00175518015,
            "cvar5_improvement": 0.02712403563661885,
            "drawdown_improvement": 0.1868991255788866,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6545843271626832,
            "sortino_excess": 1.0903046255833733,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001076261075,
            "cvar5_improvement": 0.03133242102361822,
            "drawdown_improvement": 0.20664413252536626,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.28730329734051435,
            "sortino_excess": 0.5440788402683883,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003424298425,
            "cvar5_improvement": 0.019668364102765235,
            "drawdown_improvement": 0.15308317339963268,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1964633505449551,
            "sortino_excess": 0.37783831253981137,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.002512144725,
            "cvar5_improvement": 0.028764387718322945,
            "drawdown_improvement": 0.19302446219847244,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.575296633772924,
            "sortino_excess": 1.0268291197445087,
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
            "cost_drag": 0.00192506595,
            "cvar5_improvement": 0.02545353601520564,
            "drawdown_improvement": 0.18062000932063177,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.35684856829655304,
            "sortino_excess": 0.6786716952270004,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001279738125,
            "cvar5_improvement": 0.028152481599625176,
            "drawdown_improvement": 0.19178799284935402,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2852691796917205,
            "sortino_excess": 0.5419966294494214,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011402825,
            "cvar5_improvement": 0.03202413154320439,
            "drawdown_improvement": 0.20953410178362672,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.45169046700816856,
            "sortino_excess": 0.8207544809337975,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001211505525,
            "cvar5_improvement": 0.03504120651391321,
            "drawdown_improvement": 0.22253191407041675,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4020442757936863,
            "sortino_excess": 0.7537813435469303,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002370576525,
            "cvar5_improvement": 0.02469844872322743,
            "drawdown_improvement": 0.17681519674222113,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3250012606957179,
            "sortino_excess": 0.6018465511025245,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015541661249999998,
            "cvar5_improvement": 0.025010551235785307,
            "drawdown_improvement": 0.1791937423126302,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.27068572577040656,
            "sortino_excess": 0.546524144683421,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0026041028,
            "cvar5_improvement": 0.02939140810572123,
            "drawdown_improvement": 0.1955687901524603,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8561642263935888,
            "sortino_excess": 1.575867252817231,
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
            "cost_drag": 0.0016662499249999998,
            "cvar5_improvement": 0.022708615940362064,
            "drawdown_improvement": 0.17008875629316855,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.43946852352541577,
            "sortino_excess": 0.8226671090044667,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00298331525,
            "cvar5_improvement": 0.02589508456839503,
            "drawdown_improvement": 0.18053809551923647,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.707209296597098,
            "sortino_excess": 1.2114837349825498,
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
            "cost_drag": 0.002991360925,
            "cvar5_improvement": 0.029580024597010125,
            "drawdown_improvement": 0.1948391833468138,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1876302085876741,
            "sortino_excess": 0.33248812550717427,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001293493925,
            "cvar5_improvement": 0.03300070093818107,
            "drawdown_improvement": 0.21082531531386076,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.705209408641355,
            "sortino_excess": 1.2483316244293854,
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
            "cost_drag": 0.001194744125,
            "cvar5_improvement": 0.034975743382993627,
            "drawdown_improvement": 0.22144785805525677,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.49288098735288893,
            "sortino_excess": 0.9069592628698389,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00094197935,
            "cvar5_improvement": 0.034736576469156094,
            "drawdown_improvement": 0.2213911124042237,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.325808969671191,
            "sortino_excess": 0.6055661462444825,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0023430079999999997,
            "cvar5_improvement": 0.02532817021780393,
            "drawdown_improvement": 0.18081816079702576,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.467213946065134,
            "sortino_excess": 0.874938917660304,
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
            "cost_drag": 0.0032171148749999996,
            "cvar5_improvement": 0.026302655360251167,
            "drawdown_improvement": 0.18307561443063392,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7654329407082174,
            "sortino_excess": 1.2429669291189067,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015377044750000003,
            "cvar5_improvement": 0.026571515501848428,
            "drawdown_improvement": 0.18212905201896137,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5780194275197718,
            "sortino_excess": 1.0354387680588828,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001121285575,
            "cvar5_improvement": 0.03478020123396288,
            "drawdown_improvement": 0.2186537354269925,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5516293147140016,
            "sortino_excess": 1.2478562699071845,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00118364875,
            "cvar5_improvement": 0.03253132429972989,
            "drawdown_improvement": 0.2085531255056039,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6068266876722156,
            "sortino_excess": 1.041106316547003,
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
            "cost_drag": 0.0011576894,
            "cvar5_improvement": 0.03571737227781348,
            "drawdown_improvement": 0.22466949697309246,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6075380203849965,
            "sortino_excess": 1.0482945051808599,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002249445275,
            "cvar5_improvement": 0.03230032762796125,
            "drawdown_improvement": 0.20794022051430605,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9130234166295679,
            "sortino_excess": 1.5908025388794227,
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
            "cost_drag": 0.0026185215500000004,
            "cvar5_improvement": 0.025380132334169248,
            "drawdown_improvement": 0.17770493380083338,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.833699797941587,
            "sortino_excess": 1.3735865331651311,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012134742750000002,
            "cvar5_improvement": 0.035175905104306945,
            "drawdown_improvement": 0.22062915230918564,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.681374869203213,
            "sortino_excess": 1.1733374566011356,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013942766,
            "cvar5_improvement": 0.02836666938990089,
            "drawdown_improvement": 0.19344670219877824,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.28193365791128594,
            "sortino_excess": 0.5650877262470599,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00309910395,
            "cvar5_improvement": 0.026630467434216494,
            "drawdown_improvement": 0.1839615381941157,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3936024756420978,
            "sortino_excess": 0.7431610789206066,
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
            "cost_drag": 0.001469675775,
            "cvar5_improvement": 0.0300720021331088,
            "drawdown_improvement": 0.19925620949568904,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.59702162952403,
            "sortino_excess": 1.161095102788474,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001810552575,
            "cvar5_improvement": 0.021609021393247274,
            "drawdown_improvement": 0.16498164137245608,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.28615752126676386,
            "sortino_excess": 0.5649923162821824,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001006418225,
            "cvar5_improvement": 0.03538332027047887,
            "drawdown_improvement": 0.22279165966475623,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5529446474001415,
            "sortino_excess": 0.9345091158209358,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00275151565,
            "cvar5_improvement": 0.022476958753024204,
            "drawdown_improvement": 0.16717936284794618,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5760506189136215,
            "sortino_excess": 1.000934965213126,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001573400675,
            "cvar5_improvement": 0.0345828153688815,
            "drawdown_improvement": 0.2164402509989544,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9289200883791202,
            "sortino_excess": 1.8761096758956528,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00158737065,
            "cvar5_improvement": 0.026665106897323272,
            "drawdown_improvement": 0.18353567824820186,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5231883622615168,
            "sortino_excess": 0.9859007922847838,
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
            "cost_drag": 0.00157302165,
            "cvar5_improvement": 0.028729768662543162,
            "drawdown_improvement": 0.19425283622568076,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.48136372920228243,
            "sortino_excess": 0.9011412169346548,
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
            "cost_drag": 0.0017310058000000001,
            "cvar5_improvement": 0.023357502555927376,
            "drawdown_improvement": 0.1702658189855073,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5405372575839867,
            "sortino_excess": 0.9592274840263758,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001576701175,
            "cvar5_improvement": 0.029145135853733586,
            "drawdown_improvement": 0.19421040768725423,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5960589800061364,
            "sortino_excess": 1.1274798893819176,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002757186825,
            "cvar5_improvement": 0.032865984030517145,
            "drawdown_improvement": 0.2125059160978513,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4984230738590464,
            "sortino_excess": 0.8928688768888964,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001439774875,
            "cvar5_improvement": 0.03212340881688776,
            "drawdown_improvement": 0.2065698191377312,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6942532201035593,
            "sortino_excess": 1.1814987025186612,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013542031500000003,
            "cvar5_improvement": 0.029157648505625973,
            "drawdown_improvement": 0.19483087288004214,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4317770812951151,
            "sortino_excess": 0.8124143039330546,
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
            "cost_drag": 0.001264383225,
            "cvar5_improvement": 0.035687224500477795,
            "drawdown_improvement": 0.22466949697309246,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7267239180393474,
            "sortino_excess": 1.1596358255323596,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.004355988925,
            "cvar5_improvement": 0.019176079779644323,
            "drawdown_improvement": 0.15104739559528643,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2686162265342121,
            "sortino_excess": 0.5340220026958389,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00224594445,
            "cvar5_improvement": 0.02866008115975775,
            "drawdown_improvement": 0.19234970012746028,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7518692624547538,
            "sortino_excess": 1.328575888290012,
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
            "cost_drag": 0.001549773475,
            "cvar5_improvement": 0.03601681563648018,
            "drawdown_improvement": 0.22308154435678937,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8807283902375201,
            "sortino_excess": 1.6031565996605255,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001330043275,
            "cvar5_improvement": 0.03164247950453238,
            "drawdown_improvement": 0.207029384838654,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4094559273385705,
            "sortino_excess": 0.7762142894326485,
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
            "cost_drag": 0.0012044035,
            "cvar5_improvement": 0.03256650339169882,
            "drawdown_improvement": 0.20893240110031594,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6270800904270777,
            "sortino_excess": 0.9971937836759336,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013607710500000002,
            "cvar5_improvement": 0.02773320535590432,
            "drawdown_improvement": 0.19061736185315967,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25461174182315144,
            "sortino_excess": 0.49646639468458936,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010694462,
            "cvar5_improvement": 0.031380945063266975,
            "drawdown_improvement": 0.20552453983535082,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2834210860834883,
            "sortino_excess": 0.5376906772302273,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0023176620499999996,
            "cvar5_improvement": 0.028146174362483824,
            "drawdown_improvement": 0.18981753552611447,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7888589479168286,
            "sortino_excess": 1.4957580248665474,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017371846249999998,
            "cvar5_improvement": 0.033136902346695765,
            "drawdown_improvement": 0.21041485221150324,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7743267552328563,
            "sortino_excess": 1.326230645376281,
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
            "cost_drag": 0.0016015636,
            "cvar5_improvement": 0.02931250287563269,
            "drawdown_improvement": 0.19788720688056344,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4931195090842271,
            "sortino_excess": 0.9128118310855946,
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
            "cost_drag": 0.00242814585,
            "cvar5_improvement": 0.032019999214682404,
            "drawdown_improvement": 0.20648513693005816,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 1.1182343553362515,
            "sortino_excess": 2.2410539507296017,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00263531225,
            "cvar5_improvement": 0.0326278788978216,
            "drawdown_improvement": 0.21199051362902943,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8271255985341308,
            "sortino_excess": 1.391911136153773,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002941087725,
            "cvar5_improvement": 0.031347657380712816,
            "drawdown_improvement": 0.20866680627936957,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9165603400038536,
            "sortino_excess": 1.7703865888828973,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00093506945,
            "cvar5_improvement": 0.034817942890211076,
            "drawdown_improvement": 0.22027081043439808,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.31934281236616446,
            "sortino_excess": 0.5965862284060379,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019054843249999998,
            "cvar5_improvement": 0.02709963191558782,
            "drawdown_improvement": 0.1868991255788866,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7678025518159348,
            "sortino_excess": 1.191178295472461,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013201152250000001,
            "cvar5_improvement": 0.029410688743088675,
            "drawdown_improvement": 0.19542408792168345,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5200005477486868,
            "sortino_excess": 0.9541032855357455,
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
            "cost_drag": 0.0018209357,
            "cvar5_improvement": 0.022784697944096877,
            "drawdown_improvement": 0.1698197055900312,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3686235658916464,
            "sortino_excess": 0.7399300970577847,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00132042285,
            "cvar5_improvement": 0.029612951717661026,
            "drawdown_improvement": 0.19490054326530137,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5901019145142067,
            "sortino_excess": 1.0677516028736784,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002072473,
            "cvar5_improvement": 0.03146046857972065,
            "drawdown_improvement": 0.20548301612675574,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3890649764184785,
            "sortino_excess": 0.7112949350199687,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002207088125,
            "cvar5_improvement": 0.028067116531599004,
            "drawdown_improvement": 0.19105145491379225,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.348841967635462,
            "sortino_excess": 0.6527228222271306,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001701385825,
            "cvar5_improvement": 0.02345002711751652,
            "drawdown_improvement": 0.16907157108471232,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5253922603381267,
            "sortino_excess": 0.9757258932022637,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012086327,
            "cvar5_improvement": 0.027939364015259566,
            "drawdown_improvement": 0.19215346275043163,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2695622116568636,
            "sortino_excess": 0.5179206138893503,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022022822250000003,
            "cvar5_improvement": 0.027595286294389287,
            "drawdown_improvement": 0.1847153229600468,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8085354536614944,
            "sortino_excess": 1.3595656659926618,
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
            "cost_drag": 0.0016783071250000001,
            "cvar5_improvement": 0.022532236549334478,
            "drawdown_improvement": 0.1664556708896553,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3674413936344742,
            "sortino_excess": 0.7021705610693216,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.000999919075,
            "cvar5_improvement": 0.03549281397753888,
            "drawdown_improvement": 0.2212179471226885,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6723090208582891,
            "sortino_excess": 1.100217196507347,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0030329201,
            "cvar5_improvement": 0.026425957469578622,
            "drawdown_improvement": 0.1819575770758334,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9611845046911041,
            "sortino_excess": 1.6918659224655224,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001962513875,
            "cvar5_improvement": 0.03330719652939033,
            "drawdown_improvement": 0.21338260193108424,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9476139957297285,
            "sortino_excess": 1.9316520322336215,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0024366839999999997,
            "cvar5_improvement": 0.024996574747313066,
            "drawdown_improvement": 0.17288046786322916,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8058366868493,
            "sortino_excess": 1.5278442573253839,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00329429665,
            "cvar5_improvement": 0.022921009465007337,
            "drawdown_improvement": 0.1665709606326049,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.187311946461442,
            "sortino_excess": 0.35037969491691207,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017326191249999998,
            "cvar5_improvement": 0.025431282414290796,
            "drawdown_improvement": 0.18012645132052216,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.432827553846193,
            "sortino_excess": 0.8274218205127023,
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
            "cost_drag": 0.001756141825,
            "cvar5_improvement": 0.03479519745709897,
            "drawdown_improvement": 0.21976536232142685,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7837858417404695,
            "sortino_excess": 1.3367406626005622,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001362693125,
            "cvar5_improvement": 0.024577274665037,
            "drawdown_improvement": 0.1768134337048487,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2581709074939006,
            "sortino_excess": 0.5032923058170424,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0024158666249999997,
            "cvar5_improvement": 0.025747886117014004,
            "drawdown_improvement": 0.17995523005222896,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.7215257273017583,
            "sortino_excess": 1.15480805693067,
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
            "cost_drag": 0.0014660446500000001,
            "cvar5_improvement": 0.028318200668752423,
            "drawdown_improvement": 0.1925316778049613,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.36382055951861325,
            "sortino_excess": 0.697892816135278,
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
            "cost_drag": 0.0019039858250000001,
            "cvar5_improvement": 0.03185362954181294,
            "drawdown_improvement": 0.20714571282501026,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6909284715773352,
            "sortino_excess": 1.1271993044368758,
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
            "cost_drag": 0.002843113,
            "cvar5_improvement": 0.02239349618583193,
            "drawdown_improvement": 0.16538736560645179,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4676941137528628,
            "sortino_excess": 0.8684254518393113,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018443067,
            "cvar5_improvement": 0.03423603714445331,
            "drawdown_improvement": 0.2170348065129929,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.9060158380763021,
            "sortino_excess": 1.5919307091563786,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00161090445,
            "cvar5_improvement": 0.021405786292160355,
            "drawdown_improvement": 0.16350274936179873,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2672357569309592,
            "sortino_excess": 0.5210358542560798,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002507873225,
            "cvar5_improvement": 0.022118956013347582,
            "drawdown_improvement": 0.16702593163448337,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4298474651532344,
            "sortino_excess": 0.8230935414553171,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002387950175,
            "cvar5_improvement": 0.03363120209355906,
            "drawdown_improvement": 0.215034871623662,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3109269965088238,
            "sortino_excess": 0.5954501301099779,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001212131125,
            "cvar5_improvement": 0.03261460447037039,
            "drawdown_improvement": 0.2072870686210364,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6755672254066343,
            "sortino_excess": 1.1133565399831857,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014998190249999998,
            "cvar5_improvement": 0.03553778632671985,
            "drawdown_improvement": 0.2233394974954719,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.545831444480593,
            "sortino_excess": 1.045613151834951,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010861815,
            "cvar5_improvement": 0.03573514445578876,
            "drawdown_improvement": 0.22380620651022676,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6170639602357464,
            "sortino_excess": 1.1333322540113864,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017671444,
            "cvar5_improvement": 0.028811258031618877,
            "drawdown_improvement": 0.19491993406255018,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3878993840396681,
            "sortino_excess": 0.7561096415820568,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001533995775,
            "cvar5_improvement": 0.021219145899687028,
            "drawdown_improvement": 0.16279268642216432,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25461414851375785,
            "sortino_excess": 0.5020544083978579,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001989924475,
            "cvar5_improvement": 0.022718519096731823,
            "drawdown_improvement": 0.1683047388910266,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4910184418375235,
            "sortino_excess": 0.9252957453256071,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002067516675,
            "cvar5_improvement": 0.035315024961711614,
            "drawdown_improvement": 0.22196448772142688,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.8922736349737347,
            "sortino_excess": 1.6108299768723435,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00112701665,
            "cvar5_improvement": 0.035099791294884435,
            "drawdown_improvement": 0.2227101839395764,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.348822936291894,
            "sortino_excess": 0.6880215894071595,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002853936275,
            "cvar5_improvement": 0.0327925488181039,
            "drawdown_improvement": 0.20931782500613574,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20019480081185265,
            "sortino_excess": 0.3335697371764618,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019385367999999999,
            "cvar5_improvement": 0.03479618023432669,
            "drawdown_improvement": 0.2201385942682543,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4638165112234547,
            "sortino_excess": 0.8279913397981606,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001035525425,
            "cvar5_improvement": 0.03577608138444381,
            "drawdown_improvement": 0.22247095487937923,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6297440586782209,
            "sortino_excess": 1.3571494369822124,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001916032925,
            "cvar5_improvement": 0.0241607858551913,
            "drawdown_improvement": 0.17446687605643366,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.5948074916478072,
            "sortino_excess": 1.0712330132890848,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011474434499999999,
            "cvar5_improvement": 0.03155926306086653,
            "drawdown_improvement": 0.2062714308540544,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30755393556369,
            "sortino_excess": 0.5771984001080577,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001361740925,
            "cvar5_improvement": 0.03261868710960129,
            "drawdown_improvement": 0.21167951553580877,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.497403715798441,
            "sortino_excess": 0.9164907704366342,
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
            "cost_drag": 0.001261666175,
            "cvar5_improvement": 0.03172623818937649,
            "drawdown_improvement": 0.2079379870765205,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3038302823645894,
            "sortino_excess": 0.6051476578048118,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00266137915,
            "cvar5_improvement": 0.026883831538432768,
            "drawdown_improvement": 0.18616442096057378,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2627276536629877,
            "sortino_excess": 0.5105067477045847,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001542673775,
            "cvar5_improvement": 0.021205826543204034,
            "drawdown_improvement": 0.16386601131401105,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.25683948585570143,
            "sortino_excess": 0.5060636083457191,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
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
            "config_hash": "c1d8a606615698ddf47c3031611029291113243880ae1217cad057e45c700d20",
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
            "stable": false
          },
          {
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
            "config_hash": "c50720a991912cf57e64843e363cd92942ce6eb32e71495fdf2d379aa22178ce",
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "atr_stop_multiple"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
            "stable": false
          },
          {
            "config": {
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
            "config_hash": "197cb980c6ca0e63ffc8281c85333c5035ed97c3bbda01e94aee39f0be2af570",
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
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
            "config_hash": "645b39d903cbd22867ad10ccedf4d75d54bbf485460e27591d8057b79e20e92a",
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
            "stable": false
          },
          {
            "config": {
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
            "config_hash": "808b619229eb3831d151dbf64b022578c9b57e597e569a0ed8774173402d8b62",
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001885652325,
            "cvar5_improvement": 0.032929985330279195,
            "drawdown_improvement": 0.20924636460742385,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "cooldown_sessions"
            ],
            "sharpe_excess": 1.0049349010349529,
            "sortino_excess": 1.8659249098407016,
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
            "cost_drag": 0.00017962299999999998,
            "cvar5_improvement": 0.04231200342723578,
            "drawdown_improvement": 0.25641776718148224,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "05063fd72167d3a3a2da97e7c8c63023ebe7fe845967932f2a3a68b2d9023574",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.00011987267499999999,
            "cvar5_improvement": 0.043885623866753834,
            "drawdown_improvement": 0.26207765293217866,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "091fbd2cc185b592a8e7b80f30e3e73fb8f3034ef10dcb197ae208d1892901d3",
            "cost_drag": 0.00017962299999999998,
            "cvar5_improvement": 0.04231200342723578,
            "drawdown_improvement": 0.25641776718148224,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "09c907ccffba9c79389da45ffbc273ef56ff552a01e37bb47bf4b4f538584933",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "0a073f60f2b4e958cf7bb14f680436f06eb26b748c281a78271005a1011caa57",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "0c441452555d21094fcf63b740acffe7a9176260632649cedf006f78d5c922dc",
            "cost_drag": 0.00011987267499999999,
            "cvar5_improvement": 0.043885623866753834,
            "drawdown_improvement": 0.26207765293217866,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "0dee04873a3ddf671052ea481c0d968718285776ddcfc900e5af011213ad542b",
            "cost_drag": 0.00017962299999999998,
            "cvar5_improvement": 0.04231200342723578,
            "drawdown_improvement": 0.25641776718148224,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "0efce7b04e5e193de8d96ae22d700309b50d9ec1b26b72a73c3a1a9f6769501d",
            "cost_drag": 0.000137095125,
            "cvar5_improvement": 0.043679649952058856,
            "drawdown_improvement": 0.26157465751841663,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "12643fc27869a63bcca87e3e38c0aae6f7825f6728622759920ecebf182931d1",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "13a36acfc6269b30b569bb601b5e16abcb027c50365afdcb43ae693eeb166958",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "13e36312d75235095a99fb4673caba20941b36b205e0f88c729e7bc1900c423e",
            "cost_drag": 0.000142784575,
            "cvar5_improvement": 0.043234581781619506,
            "drawdown_improvement": 0.2598764979372268,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "1424ccb6f148503ef949aaec1c140dfeedf287a16154036803144b75c5de03c2",
            "cost_drag": 0.0002065542,
            "cvar5_improvement": 0.04169039219623098,
            "drawdown_improvement": 0.25490375472541293,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.000181102375,
            "cvar5_improvement": 0.04224216217754055,
            "drawdown_improvement": 0.2562475045859335,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "17c9c940096d43a773c4905d1982dc3a9c901fae82b8de14cfb27f6844ce84c0",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "17dbff0a23e5d013e2d4b110485364f1d520f1dd5b5b79ea9cec2328e6048ff9",
            "cost_drag": 0.00017962299999999998,
            "cvar5_improvement": 0.04231200342723578,
            "drawdown_improvement": 0.25641776718148224,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1a0ba2f00044f420ffb20d85ffd3b630915c4f0587b631a9e61e8fc68b943b2c",
            "cost_drag": 0.000139800625,
            "cvar5_improvement": 0.043362147714146725,
            "drawdown_improvement": 0.2601878579650876,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "1a1d82ea59c99bfe7ac50c54c249f33eecaf9e8d07e4abf76bdd391e3652f99b",
            "cost_drag": 0.00014055415,
            "cvar5_improvement": 0.043325846563996455,
            "drawdown_improvement": 0.26009924159811115,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "1a8b7c2b566250e4974b9accd1eb288e0b1c3b9ece047603707261bce302dd08",
            "cost_drag": 0.00011987267499999999,
            "cvar5_improvement": 0.043885623866753834,
            "drawdown_improvement": 0.26207765293217866,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "1b03d2707a07fe802f1760263c82b3d4b8342a455e2139542829ce33055346c3",
            "cost_drag": 0.000137095125,
            "cvar5_improvement": 0.043679649952058856,
            "drawdown_improvement": 0.26157465751841663,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "1b8a1433cd25010fb5c550b3665e973d63467cfe7baa46e828f42e0e3914c235",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "1c9aaeaf1c01aaa86bd6f9b2a9def8c7f55b76815b48c037012df2db186a7ad9",
            "cost_drag": 0.000184199625,
            "cvar5_improvement": 0.04232078530133485,
            "drawdown_improvement": 0.25703762723603585,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "1e3c5a3a25ba0ff260f82888076b19bd3e2497627e62d17545f54d5382b673a9",
            "cost_drag": 0.000181102375,
            "cvar5_improvement": 0.04224216217754055,
            "drawdown_improvement": 0.2562475045859335,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "1fec94aa0bead42b20075940b637e819472c020dce8613fa5a3c7aa21734fd06",
            "cost_drag": 0.000120236725,
            "cvar5_improvement": 0.04386782705862499,
            "drawdown_improvement": 0.2620341790279067,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "23d1e52eeccaf4bc0cb8853853c2be63a69dd7762b18d7289741c7e7f37b98f9",
            "cost_drag": 0.00011987267499999999,
            "cvar5_improvement": 0.043885623866753834,
            "drawdown_improvement": 0.26207765293217866,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "275334c7d66460505e7c71e7f1bc8e971d6b44f3af26a6b8dba212d744d4d00a",
            "cost_drag": 0.00017962299999999998,
            "cvar5_improvement": 0.04231200342723578,
            "drawdown_improvement": 0.25641776718148224,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "2c75c42046ef3a6d0f0febae245bcf1a0d429394847dcdc593062e759c731b73",
            "cost_drag": 0.000142784575,
            "cvar5_improvement": 0.043234581781619506,
            "drawdown_improvement": 0.2598764979372268,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "2d4e420f979f519ab7261ed8c86ca8308618af6e63b56f5476e2d2fce0fd8a14",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "330e9079a8741ac5ed4d998877d62b08834a5251908efa8b14fa9b09f101662a",
            "cost_drag": 0.000142784575,
            "cvar5_improvement": 0.043234581781619506,
            "drawdown_improvement": 0.2598764979372268,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "376261879bb3a98cb9d9f885ebc4606248424ee5623184ed545ba758deb3d361",
            "cost_drag": 0.000184199625,
            "cvar5_improvement": 0.04232078530133485,
            "drawdown_improvement": 0.25703762723603585,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "37ce18ea991b11a33fd546c75664f8cafed609d4a7311f44011f1ac689f5ecbe",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "387050649e85b36d7c6e999764671f946e30e8f6587f959815efda2fee8967c9",
            "cost_drag": 0.000139800625,
            "cvar5_improvement": 0.043362147714146725,
            "drawdown_improvement": 0.2601878579650876,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "3d16b6890afaf109d0c4451863565fe56cb71dd1454039aa22d95648f62fe42d",
            "cost_drag": 0.000142941625,
            "cvar5_improvement": 0.043227867814776604,
            "drawdown_improvement": 0.2598601142713766,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "3de7c13e774d534c952c8462bc02d4706ba6c2da63098dcc633d9891959119c9",
            "cost_drag": 0.000181102375,
            "cvar5_improvement": 0.04224216217754055,
            "drawdown_improvement": 0.2562475045859335,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.000142941625,
            "cvar5_improvement": 0.043227867814776604,
            "drawdown_improvement": 0.2598601142713766,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "4266ee5cc6a9ac907f421389ef9cf425c951ac9475f81729c7ed50f0150b1b7d",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "42881131aa958b37001b7427d92d5475137405fe28d79f77e10b24316f77ab3c",
            "cost_drag": 0.0002065542,
            "cvar5_improvement": 0.04169039219623098,
            "drawdown_improvement": 0.25490375472541293,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "441990e611d4bfed0a753adb7d990a66af9681ccb20bb032d058f3e3bf793c67",
            "cost_drag": 0.00011987267499999999,
            "cvar5_improvement": 0.043885623866753834,
            "drawdown_improvement": 0.26207765293217866,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "443522543e3e8dd041a7ffeee4af344efccc3ec16395b525bc91265308a4d846",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "44cb7392c928f53c521015a2cd2d0d65ae8766b2261ffc6f5861bc3196ad086f",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "45fc69735e2a6498f6345128fd7d46a7e5ad7bc5aa540c5fe68355a5a078e402",
            "cost_drag": 0.00015978774999999998,
            "cvar5_improvement": 0.04283597299670135,
            "drawdown_improvement": 0.25829346492345107,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "46f7afbe4f52f52cf8832a43b79598af956b8e0d3541d6425464a97964d756c0",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "492d3075b7505d752fc4569124324cf50ec4e1e12399bff92d72a757be0abcea",
            "cost_drag": 0.000121338475,
            "cvar5_improvement": 0.04382278923635156,
            "drawdown_improvement": 0.261924172379563,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4a09e9f42c304e0c0f941aa4fb00cfc45f473ebaa326e8c08008a0a2a91e8d4c",
            "cost_drag": 0.00016101937499999998,
            "cvar5_improvement": 0.042983499770211805,
            "drawdown_improvement": 0.25926404572950057,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "4bfb9404f1e53fa2d8ba993a154c73bc83122dfdb210429965cadb5122d6cb5d",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "4c5dbff3038888fbc8ba660d551023c7213bc3c92e7d698161e4831ddb927e16",
            "cost_drag": 0.000142941625,
            "cvar5_improvement": 0.043227867814776604,
            "drawdown_improvement": 0.2598601142713766,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "4ef5f2e60b0a12f9c3dfdfc50ff212dda872ca3811ba7eb1a418cd635500ee86",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "505ad729a6207cc8be7b2d3fe972a46ba111f58eeaa7b3b530a2cfa2e1d371ac",
            "cost_drag": 0.00014055415,
            "cvar5_improvement": 0.043325846563996455,
            "drawdown_improvement": 0.26009924159811115,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "50aeca7dbe7571cfa0dd145f2032d40a70a44efb66da2450d2ac21fc20d8ac95",
            "cost_drag": 0.000139800625,
            "cvar5_improvement": 0.043362147714146725,
            "drawdown_improvement": 0.2601878579650876,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "512697187c6fe64646e9ff21e491e8e481880ebae3fbd0e5138c76ee036ec1d5",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "520cb3507a916dc9d9f2fa51dacd4e7c3511bbf9eee1fcdf03da237bb9f07e11",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "52db97a65a1d4ad3cfa5799f59629bcab32d4cb9e84027e5ec07afc0fc759dea",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "53ae75468006b31323bf7c8217cd72f20b714d1c350e56945d1b7cb891a67f57",
            "cost_drag": 0.000184199625,
            "cvar5_improvement": 0.04232078530133485,
            "drawdown_improvement": 0.25703762723603585,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "548bde01f4ae3b39c455be93505eda30b321c79668d9f8acde7f81aac0feefc0",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "59b014959d6ca4769d4753c652daf0ccb38e962e5c3d4d3ea42fec5bd2a2a57a",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "5bf8412a3fe2565df7fe2ecd3cf0bf8ef854466aaaa317215f6937328ff3ab18",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "61609ced85a7068bb6b227a8778db35ac30701765ed24a2d414765a7965417f9",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "64e6f60cccaa85fd39f8b1fa74bc32547aeab8eb0fc0ea90356ebdca81ab94da",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "64e8b768141ab52605621addcd48eb9cc31b1ffcd58858b53f7d3015b5511af3",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "673a28cda6786a76d77f41b3d518b2dc00aa5c1482c95959af2c5318831043bd",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "696913cb4f51a33bf3935b51da3b38e1dcd6d1a97557ef171529553b4d7bfbf7",
            "cost_drag": 0.00015978774999999998,
            "cvar5_improvement": 0.04283597299670135,
            "drawdown_improvement": 0.25829346492345107,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "6a23f24486bb79be48113d97b10bbba4ac19f7ddef0e43e81ec8d1dc67ff9092",
            "cost_drag": 0.00012157405,
            "cvar5_improvement": 0.04381269083990534,
            "drawdown_improvement": 0.2618995088916581,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "6c62868387b90bf0e5d50a007eb97dff2c5f410ac777bb74e949f24ca4545cd4",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "6d0b27b35b089a17eb96ff6e8962cf760fda88c3a3d4da56f20518c119a22fea",
            "cost_drag": 0.000139800625,
            "cvar5_improvement": 0.043362147714146725,
            "drawdown_improvement": 0.2601878579650876,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "6fc8e2eef32a9bbeedf4d1623087ba3891701d13c78d22843cdf57a1c9bb12be",
            "cost_drag": 0.00015978774999999998,
            "cvar5_improvement": 0.04283597299670135,
            "drawdown_improvement": 0.25829346492345107,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "707d5fac1ebe3f88df9b8bca06082ec5f029dbaaa67f900f17bdbb99418ae959",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "74615fd57e7c943c143fd077540a3361517eb745a26477811b844f682456d219",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "76c2fdbf72a6ee26af1f5ea026eca75afdfcee1086f79c917047a7c7ab3c01ed",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.000139800625,
            "cvar5_improvement": 0.043362147714146725,
            "drawdown_improvement": 0.2601878579650876,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "7ec3d94889c6256057b589f9a9349e6f11c29591facbfc6dd184ffe7dc58d8de",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "81f56cf56a5de341c5d98c82cf7d5803225386e334d2d1d583526e9c4ea5e855",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "891e4aac1326376aff627803dcff3b5d016adb3f7c1d241c033375b50f4f5659",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "8bf92734c3d2ba8e6c3dd7f599c5b43e34620f9479e5c24f9b34ccbe045b4947",
            "cost_drag": 0.000137095125,
            "cvar5_improvement": 0.043679649952058856,
            "drawdown_improvement": 0.26157465751841663,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "90e95eca032bfe50e881261b29e392fa034ba82c6ca75e51bb44c3dd72c9275c",
            "cost_drag": 0.000184199625,
            "cvar5_improvement": 0.04232078530133485,
            "drawdown_improvement": 0.25703762723603585,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "915b629158bae600eedb793e1b7461db1bca2642934e70e963373d51bb0eec9d",
            "cost_drag": 0.00014055415,
            "cvar5_improvement": 0.043325846563996455,
            "drawdown_improvement": 0.26009924159811115,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
            "cost_drag": 0.00016101937499999998,
            "cvar5_improvement": 0.042983499770211805,
            "drawdown_improvement": 0.25926404572950057,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9755e4a2985929b24476e74975b3281dcf102f99fc184339e833c99c9365e566",
            "cost_drag": 0.000142784575,
            "cvar5_improvement": 0.043234581781619506,
            "drawdown_improvement": 0.2598764979372268,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "9a5ffaf7d90c7cd06362d27f96a11d349d1b8f1dd81f180cf81cb93f13789ea5",
            "cost_drag": 0.00012157405,
            "cvar5_improvement": 0.04381269083990534,
            "drawdown_improvement": 0.2618995088916581,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "9a8031973c8ec766ac9566a91c4f700fd8d2a7712f8f4e3641c67b8135e77bca",
            "cost_drag": 0.00016101937499999998,
            "cvar5_improvement": 0.042983499770211805,
            "drawdown_improvement": 0.25926404572950057,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "9b43cfb13d4e03c1d855e2b81d3146f84cdd7f6155194208cff59649e4fafedd",
            "cost_drag": 0.00017962299999999998,
            "cvar5_improvement": 0.04231200342723578,
            "drawdown_improvement": 0.25641776718148224,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.00012157405,
            "cvar5_improvement": 0.04381269083990534,
            "drawdown_improvement": 0.2618995088916581,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a05a3729a4575c24923de713a0ba59f30f2cfd21472905bb9a557e2e85fe5392",
            "cost_drag": 0.000142941625,
            "cvar5_improvement": 0.043227867814776604,
            "drawdown_improvement": 0.2598601142713766,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "a164ba23ba9524e034fe07bfe24aea3b27db569bc592dca70655d980b21fcdd3",
            "cost_drag": 0.0002065542,
            "cvar5_improvement": 0.04169039219623098,
            "drawdown_improvement": 0.25490375472541293,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "a2606ff0dd53e64bdaed4879ebef55587c576527665e09aaceec8068c023f1fa",
            "cost_drag": 0.000142784575,
            "cvar5_improvement": 0.043234581781619506,
            "drawdown_improvement": 0.2598764979372268,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "a5c471fd8ef46b803b80689400b2fc0c30d0ff6a0d4e6a27deb9881f27514916",
            "cost_drag": 0.00011987267499999999,
            "cvar5_improvement": 0.043885623866753834,
            "drawdown_improvement": 0.26207765293217866,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "a7d1bc64be18eec70f804ccb675f4de3265988e1f7041b8dac11721a645fbccd",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "a7e3098ae1d238b85a68bf710352484a836546f125d4abdecafda4bd5b6ce8e1",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "adbca544282724c5a7a2958f71250737af4685caeb95879a42bc97e6fba41fa0",
            "cost_drag": 0.000120236725,
            "cvar5_improvement": 0.04386782705862499,
            "drawdown_improvement": 0.2620341790279067,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "add329e8e27ecebe1d584cb1f14ba572d35710aea60476ca8ccbc31431672993",
            "cost_drag": 0.00016101937499999998,
            "cvar5_improvement": 0.042983499770211805,
            "drawdown_improvement": 0.25926404572950057,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "ae2f1ec1405653fbbf289a5f020fe4b9ab1365648959be0631bcd1db772eadad",
            "cost_drag": 0.000139800625,
            "cvar5_improvement": 0.043362147714146725,
            "drawdown_improvement": 0.2601878579650876,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "b1ce106b9791d9b2313e33ad5d36230eb1a10a96118d83ef7b6350514a957bd9",
            "cost_drag": 0.00012157405,
            "cvar5_improvement": 0.04381269083990534,
            "drawdown_improvement": 0.2618995088916581,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "b3ab56d68fdcaada002d2614a264764fe445837a7212d9cef39fd0934e9a098b",
            "cost_drag": 0.000137095125,
            "cvar5_improvement": 0.043679649952058856,
            "drawdown_improvement": 0.26157465751841663,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "b4a19d9ee57a1ed883fc45f2d940417ba33b9bcd8854935c3d9ed02a29df5c44",
            "cost_drag": 0.000142941625,
            "cvar5_improvement": 0.043227867814776604,
            "drawdown_improvement": 0.2598601142713766,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "b54d6a3fa555012188e6f740379a78f0dd22cd68864cae4eb9e915ce67e8baaa",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "b5ae512c057c4cca149fc22aa5ab060d43221cfcfb62184e6b988b8670e045e0",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "b7aa686834fba404e57ce646e62ea5ae9ce6b33df36f634aa733cced8430673f",
            "cost_drag": 0.000160903825,
            "cvar5_improvement": 0.04278270319760261,
            "drawdown_improvement": 0.2581635135971236,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "b7c893047999c7d6c75f8da734604fb8e463ffc56e36cbccd00fa3732bfff73c",
            "cost_drag": 0.000160903825,
            "cvar5_improvement": 0.04278270319760261,
            "drawdown_improvement": 0.2581635135971236,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "b9bc2fd53b37952d0fa31d7ee6c7abb2df29fc0c936f761b0b4d5de89d3b3c65",
            "cost_drag": 4.38163e-05,
            "cvar5_improvement": 0.04386225487491784,
            "drawdown_improvement": 0.2616697375213337,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "bc6f099a3c49e384ab643559ec0ec44d65d442396a1dc177bb4c7181ac52ae54",
            "cost_drag": 0.000121338475,
            "cvar5_improvement": 0.04382278923635156,
            "drawdown_improvement": 0.261924172379563,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "bcaf1067a4e98787b432db5b6681a208b9eea62150fe336c1090df3b4f678dfc",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "bd61e6ffa991468a6062bf4047742d76be80658e74f9212ae8482ed6d90027cf",
            "cost_drag": 0.00012157405,
            "cvar5_improvement": 0.04381269083990534,
            "drawdown_improvement": 0.2618995088916581,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "bdfeea35c79ba78c3054cc430396a6f0454ffcb4c0eefca49e78830b92de5ccc",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "be75d5c8e26860196c89f31b797698e558e2c7568cb1a802d2a09507366516ca",
            "cost_drag": 0.00012157405,
            "cvar5_improvement": 0.04381269083990534,
            "drawdown_improvement": 0.2618995088916581,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "bf18cc0ff8f31c28dd27bd53bea9a4b8740f08d9cba11a3a14cacc6d1091b9ef",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "bfc4d87ac49a11a984a17ee8bc2a235c4905e425284c08722bc83a3787c3da0f",
            "cost_drag": 0.000184199625,
            "cvar5_improvement": 0.04232078530133485,
            "drawdown_improvement": 0.25703762723603585,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "c1144d55f4b001966183229609c62f71533195749e340dc147b58b34996d34b1",
            "cost_drag": 0.000160903825,
            "cvar5_improvement": 0.04278270319760261,
            "drawdown_improvement": 0.2581635135971236,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "c2209a5b405bac286c73284d9fc581c16a425d179dcff71abdeaa8710254fe0f",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.5,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "c2faa48b20285145059a9507df7fb128457be7916c87597372a667e3535514da",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "c3b3386f66538a319e0467b3a0b591520efa06cc1ee02fe2bfe05a4bfdea1895",
            "cost_drag": 0.000137095125,
            "cvar5_improvement": 0.043679649952058856,
            "drawdown_improvement": 0.26157465751841663,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "c4d5b093333d5f925ed448b6d6d3817b80258f4b6df0402ff62d7ff6e5de0d90",
            "cost_drag": 0.000121338475,
            "cvar5_improvement": 0.04382278923635156,
            "drawdown_improvement": 0.261924172379563,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "c4ecea34d33f8e9ff517190ef1639a0078c204de4df752764eafe9f1f8ec39cd",
            "cost_drag": 0.000121338475,
            "cvar5_improvement": 0.04382278923635156,
            "drawdown_improvement": 0.261924172379563,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c54abf54583ce691431dbb42312227a0d225834bfc9a325757243da770f414aa",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "c8d96d02fef2052aa1b5b4f37d053341689597b833962dea2b09040dda9cd81d",
            "cost_drag": 0.00016101937499999998,
            "cvar5_improvement": 0.042983499770211805,
            "drawdown_improvement": 0.25926404572950057,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "cc26b8dbf9aabc5a954cdba7f15445f6906c516ab4ca332c472c7970122b880a",
            "cost_drag": 0.000137095125,
            "cvar5_improvement": 0.043679649952058856,
            "drawdown_improvement": 0.26157465751841663,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "cd308639566094e1248179f35cda2c75f4b3f108d88965087b313c6e2c18ad0c",
            "cost_drag": 0.00015978774999999998,
            "cvar5_improvement": 0.04283597299670135,
            "drawdown_improvement": 0.25829346492345107,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "cd978ede184d59c0797473a5f7cf0173d393d3398a9aa841a8dc97ea58a53cb5",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "ce25616a08a3a713d3baa8fbe9c681a24d2d0ae6253ec78d562b4a0e52cefb9e",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "cf9cde26dba3c73a5567f30c5d5a03c684d25c008ef9fb3ad24b61ff1e53e962",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "d00659d885e156983f250b8d53e6c117947d0afc46d076fdcf1e024dacb4145d",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "d1a7f1bab43c17c56cf770ea8414ee06ce61b60f10d4a20f8959f14d48824bba",
            "cost_drag": 0.000184199625,
            "cvar5_improvement": 0.04232078530133485,
            "drawdown_improvement": 0.25703762723603585,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "d352ec1510356ccb70944864be43f48121546077644fccd6d3b4ebe46472fbb3",
            "cost_drag": 0.0002065542,
            "cvar5_improvement": 0.04169039219623098,
            "drawdown_improvement": 0.25490375472541293,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "dcbdfc7b407f6dae2709dbf78aaa01157de1752506623e224a3c54d9dcbd44cc",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "ddcf08c0eb422a69906267785f04df8ddf6ada327f9f7dbfc623ef071dcdcb28",
            "cost_drag": 0.000121338475,
            "cvar5_improvement": 0.04382278923635156,
            "drawdown_improvement": 0.261924172379563,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "de68c4ccc59411bff11772363170338b6761dbd0f39bd7fc8c794de5cfd5259e",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e22018ff8811c7b7c47fb6ee98be4a18af5dd760741f1521c9a5e5246a5dcead",
            "cost_drag": 0.000142941625,
            "cvar5_improvement": 0.043227867814776604,
            "drawdown_improvement": 0.2598601142713766,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "e731b06b6b8a57905247003db6fe52b6b03c796f946f86db5ff1d9a78d7bc936",
            "cost_drag": 0.000120236725,
            "cvar5_improvement": 0.04386782705862499,
            "drawdown_improvement": 0.2620341790279067,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": null,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "e77bf2a8d1f196188c97d7cfc708d2f57c96d69e508253e83cf169f5c4d6c81c",
            "cost_drag": 0.00016101937499999998,
            "cvar5_improvement": 0.042983499770211805,
            "drawdown_improvement": 0.25926404572950057,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "e9e04869e6239071f9dd8cce64bab3d8eeb7ca305ff95b34978dc8aedbbd705c",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "eadf7cacdbca92462104fbb663d7c89152d0846f8079544838f53c144e80b383",
            "cost_drag": 0.000142784575,
            "cvar5_improvement": 0.043234581781619506,
            "drawdown_improvement": 0.2598764979372268,
            "exposure_ratio": 0.09126984126984126,
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
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "ebab91384cb73c29a059a5f61ee4cb1db962fd86e95224f09308839b0f4f4a7d",
            "cost_drag": 0.000121338475,
            "cvar5_improvement": 0.04382278923635156,
            "drawdown_improvement": 0.261924172379563,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.5,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "ec4085c7e24702acce52ee2a5997e551a4978c5f8741df94c163d6422bc23f7c",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "ec7cbbe41821b4534745fc5abe749c3fa818c012a03773917d564783155e3c9b",
            "cost_drag": 0.00015978774999999998,
            "cvar5_improvement": 0.04283597299670135,
            "drawdown_improvement": 0.25829346492345107,
            "exposure_ratio": 0.09126984126984126,
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
                "amount_ratio_min": 1.2,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "ed0dd236355b7a8d9f42cd954e2aba0cca2d130aeb2e511c8145e52b3b5c9229",
            "cost_drag": 0.0002065542,
            "cvar5_improvement": 0.04169039219623098,
            "drawdown_improvement": 0.25490375472541293,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f08a6c33adf0cb5410922ccb5eb4e34f92024956a5c0332e80e647bee7cb2a01",
            "cost_drag": 3.90967e-05,
            "cvar5_improvement": 0.04399952547324767,
            "drawdown_improvement": 0.2622584945787419,
            "exposure_ratio": 0.017857142857142856,
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
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "f20359ca6d891690d890c115b86a566a971340c2017016139abfe828870ecff8",
            "cost_drag": 0.00018483182499999998,
            "cvar5_improvement": 0.04209052970604915,
            "drawdown_improvement": 0.25587798254870675,
            "exposure_ratio": 0.09126984126984126,
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
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f3b1956a637c63c935fb3bb6eb3e713d0e7881edf280d7cd43341778f5d206ec",
            "cost_drag": 0.00016408045,
            "cvar5_improvement": 0.04265295393341565,
            "drawdown_improvement": 0.25784708681861973,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 2,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0075,
                "stop_n": 2.0
              }
            },
            "config_hash": "f403091f4d2bc6ab744045f21d94ccd7cdb6bb69adac3cb07ebeb46eaf36f684",
            "cost_drag": 0.00015978774999999998,
            "cvar5_improvement": 0.04283597299670135,
            "drawdown_improvement": 0.25829346492345107,
            "exposure_ratio": 0.09126984126984126,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "config_hash": "f985f1617e9bb77ea62699fce58cc6011e56a4fb40c9d3565f854b8ed05f5e4c",
            "cost_drag": 3.43771e-05,
            "cvar5_improvement": 0.044136595840899025,
            "drawdown_improvement": 0.2628473297375703,
            "exposure_ratio": 0.017857142857142856,
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
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.0025,
                "stop_n": 2.0
              }
            },
            "config_hash": "fc714e5166dab9d576b2cca6b8263c9609f4ba786bf9b50769aa593b8e6c47d5",
            "cost_drag": 2.96575e-05,
            "cvar5_improvement": 0.04427346676606591,
            "drawdown_improvement": 0.26343624301336055,
            "exposure_ratio": 0.017857142857142856,
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
                "amount_ratio_min": 1.2,
                "max_units": 3,
                "require_macd_bullish": true,
                "risk_per_unit": 0.01,
                "stop_n": 2.0
              }
            },
            "config_hash": "fd3352c6d16146fc47234c6239e5393864ac990b33c70cd0570d7c36192d1a49",
            "cost_drag": 0.0002065542,
            "cvar5_improvement": 0.04169039219623098,
            "drawdown_improvement": 0.25490375472541293,
            "exposure_ratio": 0.09126984126984126,
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
