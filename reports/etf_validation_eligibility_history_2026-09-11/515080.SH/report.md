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
            true
          ],
          "oos_returns": [
            0.028316633700000034,
            -0.0037831566999999133,
            -0.04251632649999995,
            0.005556200999999952
          ],
          "positive_window_share": 0.5
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
            0.01834362500000004,
            -0.0006749549999998973,
            -0.03797322789999995,
            -0.0006845897000000434
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.008261671200000046,
            0.002264214400000117,
            -0.03329896299999994,
            -0.007019244500000035
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "da28e066148553678760b45c21a54f0f815cb41838c646423fedd4acd0c69f0d",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.001759591499999949,
            0.005164792100000131,
            -0.02882293239999993,
            -0.013359539000000031
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "90d6ff7ed79e50c4dddaaed58adbfdc177b6bf9b378de9d013c1d4240154e606",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011654187799999938,
            0.008030363500000144,
            -0.024358159499999924,
            -0.019597696000000026
          ],
          "positive_window_share": 0.25
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
            0.03612101330000005,
            0.003174894600000134,
            -0.05211304859999993,
            0.009091704000000016
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
            0.03282070380000006,
            0.007888307600000147,
            -0.04412175809999992,
            0.0028302078000000223
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.030261057000000063,
            0.010805872200000163,
            -0.03590157619999991,
            -0.0035486355999999712
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "77bd9770c8d5ec308e8b7fd0fadfa8fbf6cead744a6e15323ae2a4260b80ad42",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.02041623300000007,
            0.013783743000000178,
            -0.031409953299999904,
            -0.009811084399999968
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0664477e5295e0bc1c74559f720de476589a1201e90ca5c2c2645acf217e5a1e",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.010374435300000075,
            0.016691139600000193,
            -0.026930240699999893,
            -0.016099276599999962
          ],
          "positive_window_share": 0.5
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
            0.038279917200000055,
            0.010052776800000118,
            -0.06249137669999991,
            0.012677480200000082
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
            0.028143081400000058,
            0.013082463300000128,
            -0.05803513939999991,
            0.006340674400000086
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
            0.030651156800000086,
            0.01695169370000021,
            -0.049329910999999886,
            3.384010000009527e-05
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "77c0310211df78935d4962e65b3e258ba298c8d9fd368ecda7590f2158d215b1",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.031137801700000082,
            0.022418896400000225,
            -0.03873102179999988,
            -0.0062911298999999005
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2b1ca3a349c41d3e74f6ea219a4c0fe30f94bd0c8d69053d8a263b0a0abd2acc",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.021250807600000088,
            0.025469448900000236,
            -0.03177378599999988,
            -0.012717230799999896
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c952cae7bd45116005f8eb31266d51ce6c128f513baffac095de4b6cb97384f6",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.03703243200000002,
            -0.00423554869999993,
            -0.06821363259999991,
            0.01646349310000015
          ],
          "positive_window_share": 0.5
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
            0.038568160500000066,
            0.020433187200000157,
            -0.06559897809999989,
            0.009938772100000154
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
            0.028513799600000077,
            0.023464803700000172,
            -0.059057787099999884,
            0.0035790935000001613
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2542c5a0c6a70a2692a3038a43bcea945893d0495b2c1713e03b0f9afdf6620a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.03549990600000011,
            0.02767932280000027,
            -0.04667443919999986,
            -0.002785423199999835
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c1f8d05174940de5abab81e70dbabad9d91d52b696bb409bdd2ab6d799a45da8",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.025323447600000118,
            0.030789582000000284,
            -0.03926930829999986,
            -0.009050265999999828
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e43174b66cae18536744c3921b38ea3b06411d2aafef1ba96738db80f17ae80b",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.02338157990000004,
            -0.0035888716999999334,
            -0.03914297139999996,
            0.004189145199999907
          ],
          "positive_window_share": 0.5
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
            0.013362029600000044,
            -0.0005080752999999209,
            -0.03446248179999996,
            -0.0020234624000000853
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0032451001000000507,
            0.0024044849000000937,
            -0.029915481299999953,
            -0.008380509800000081
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "222df6d8f13727d94d27e59090092450a9d1437210027cc7ba1e9ed6e9669731",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.006602761899999941,
            0.00527952050000011,
            -0.025246448299999946,
            -0.014708968800000076
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1955c130371fbd273746ee973f8ff228037a1edbf3c4f5811acb4c15e0cf6dda",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.016548786299999937,
            0.008204625300000126,
            -0.020788196899999938,
            -0.021027690600000065
          ],
          "positive_window_share": 0.25
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
            0.03294504820000005,
            0.0045000109000000905,
            -0.04288742319999995,
            0.005816651499999926
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "259b394408833371c897a4a9317235e9c836670ca8171b17b53da30eb4a6a0c9",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.029899460400000064,
            0.007626360300000103,
            -0.03659158669999995,
            -0.0005249426000000675
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.019770533900000067,
            0.01063401640000012,
            -0.029252388299999935,
            -0.006803129300000061
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "183a91bd23a755b7e87e0ab603de83e23b8219e506dd76397e078a1cf902c167",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.009817056200000073,
            0.013649109600000136,
            -0.024771913999999926,
            -0.013116117900000057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "260012ec18d23eb314b1bd71c33087541eee3662ea1fdbc37c0ba619bcac2dbb",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            4.004000000792929e-07,
            0.016540765000000148,
            -0.020284102699999917,
            -0.019447818400000046
          ],
          "positive_window_share": 0.5
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
            0.03459082280000008,
            0.004200667000000085,
            -0.05000424749999993,
            0.007383360999999948
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
            0.02444174500000009,
            0.007137644700000098,
            -0.04523909889999993,
            0.0010256216999999547
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.025827503400000076,
            0.018752478800000142,
            -0.03525050989999992,
            -0.005251986500000038
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0c65d2ef761411d63b3e7d181c2d998d0df2dcf703efd602be2fad87e1da59dc",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.026502854200000092,
            0.02193822170000016,
            -0.02816749239999992,
            -0.01162991900000003
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3c50ec6e404a0402a3f98be24cad12d2a6bb4f1a9ce1917679cbf45896f6efd0",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.016525838500000098,
            0.024928684700000172,
            -0.023463000699999913,
            -0.01794096290000003
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "13140adfdb638ee59aee50db7ac7a68bf94b4aeb3cd69660a93f3b3954d57fc0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.030562821600000047,
            -0.0052589768999999585,
            -0.05546936499999993,
            0.009169383199999968
          ],
          "positive_window_share": 0.5
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
            0.03357874110000011,
            0.01235001530000011,
            -0.04884956459999991,
            0.002573845199999973
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.023633231600000117,
            0.015457758900000129,
            -0.044276274299999904,
            -0.003700725500000019
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "80899914e7291fc258eeddf6520efbf7fe1b0287b99fc96d0a62841279df7425",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.028851065700000095,
            0.03014582990000018,
            -0.032478546699999895,
            -0.009998874800000015
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4769bcc53bde368b7006c19ea230e03bc28764d38036f94954f64cec059dcb85",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.018946189300000103,
            0.0332618422000002,
            -0.026125116099999898,
            -0.016382649000000006
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f6d7509f3f5c1634fea76f4dd53e98841aa76151e5c756d7dfd55b79d67dc8f8",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.01805568290000002,
            -0.005778201999999937,
            -0.03866230889999998,
            0.0036318925999999016
          ],
          "positive_window_share": 0.5
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
            0.007915139500000026,
            -0.0027715526999999227,
            -0.033989921999999964,
            -0.002631979500000093
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0019929715999999695,
            0.00017378420000009262,
            -0.02938483739999996,
            -0.008899757600000086
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9b285843c53cb0e98fbb611366f677a98327b135bad0b9ffb777bf5f8f2ea648",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011836415299999965,
            0.003050944400000106,
            -0.024762190899999956,
            -0.01522012360000008
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3b113e92d617b95e71b3d485144a8bf07623fdd5476c359cde7bf0af5e60b9ba",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.021634804199999955,
            0.005942357900000122,
            -0.02030774099999995,
            -0.021548406900000074
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "eec8e6bf15537c408060e82aa9252bc11c299b5ededb53194b719629a246267c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.028806296300000013,
            -0.0002009489999999156,
            -0.04049717319999997,
            0.004340164299999914
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1fb848b69f408dc3ba8d7bd85ebc85edda0535045ed94aad7ab28c6599beaf4d",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.01867666190000002,
            0.002738720400000099,
            -0.03339248019999996,
            -0.0019505688000000798
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.008699576900000026,
            0.005798089600000111,
            -0.028542370199999955,
            -0.008223246900000074
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4734c020226fa7443033daa844967e4699044f02fbfcdd5f6005cd5984d5532d",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.001262079999999964,
            0.008742017800000126,
            -0.023986308699999948,
            -0.014508418800000068
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e062b42fc995eb71bc33d23b0a1a7171cd43966949db71673235e334018a8b9f",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011131541099999961,
            0.011648998800000143,
            -0.01952041789999994,
            -0.020887768500000063
          ],
          "positive_window_share": 0.25
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
            0.03712267490000001,
            0.005350282400000104,
            -0.04828541919999994,
            0.005000179599999929
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a7e68e5035096e8601e3fc70bed10c2f2d51007849d3f7759c8601c0d59a51de",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.02688919240000002,
            0.00832111180000012,
            -0.043630856199999936,
            -0.001289983600000065
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.019571491400000023,
            0.011441649000000133,
            -0.031704019799999955,
            -0.0075181877000000605
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9f72db2d6091f70ef6f2c28a733136150b7d98312604e238d2900953d4d65ab4",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.00939734070000003,
            0.014357385900000148,
            -0.02335154449999994,
            -0.013901500000000053
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1b7e2c5e7b5958dc5a4167102c649e3905f2a20047667578f26da46fe53ae2b2",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0005155849999999643,
            0.017368223500000165,
            -0.018757558799999935,
            -0.020205039800000046
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4fc55be6dc74c3f50156a7e114ea4978acdb95ed567f20d6bbf0c18ba03b48c2",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.043541675800000006,
            -0.003755428099999958,
            -0.05382051319999994,
            0.005681175999999941
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c828166e74ca3a3a5edaf08d9a9cc9318061f12eaf8a971288d9fe9aa94f0002",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.036882829100000014,
            0.013937646100000142,
            -0.04657954069999992,
            -0.0005879517000000507
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.02667690470000002,
            0.017031324600000158,
            -0.04209145579999991,
            -0.006878592400000046
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d6dfb2a62a2c81350ef9e449a06dc69ac134a1e3741a97bf3776f014a02b7bde",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.02021997730000003,
            0.019975488900000168,
            -0.027770961999999948,
            -0.01317715470000004
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4e1a984b1c95dcc573ae3ac61d76713bc6516583278750a0006153bff7d9df6a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.010209100900000035,
            0.023092642200000183,
            -0.023268299899999942,
            -0.019501668100000036
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "589b9e99b2cc99c9bf11c7d143c4316f35fae491362d7df2a95b2a38cea057ef",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.011727906900000026,
            -0.005563175899999941,
            -0.037777663899999966,
            0.0029740077999998935
          ],
          "positive_window_share": 0.5
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
            0.0017870753000000308,
            -0.0025179552999999265,
            -0.032956202199999965,
            -0.0033106028000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.008071066399999959,
            0.0004212141000000877,
            -0.028429932799999953,
            -0.009595483300000096
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "61a86f69f97281212bca1d76dff4959aded7bc8ae179fd65e9a35b51766efe9a",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01796775369999995,
            0.003298574300000103,
            -0.02378655609999995,
            -0.01591584930000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "266908ce86922ef9e2da585eb6b06dc860b8cc72327a6b50d62c098f123fd428",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.02774313569999995,
            0.006163945700000117,
            -0.019331207099999942,
            -0.022244132600000077
          ],
          "positive_window_share": 0.25
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
            0.015788568300000035,
            0.00024307620000007732,
            -0.03616340889999996,
            0.002862440899999902
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "deba15173d77c901d382e9f5272229ae1cba6daa2726b4bb6ce9634e86a14da7",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.00570090390000004,
            0.0032878834000000905,
            -0.03146102979999995,
            -0.003422169700000092
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.004095355499999953,
            0.006199277800000107,
            -0.02679111979999994,
            -0.009711950200000083
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a43d42200543c8fee6ecea4bd84917ea1bcf540d535e043f6a521a06832f55f1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.013984215099999947,
            0.009208186500000121,
            -0.022202282599999935,
            -0.016030286100000082
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e2cff1ab7f737919236ab95a7fedc68c273418b1b4245a5f6ac6c54916c93f70",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.023760581199999936,
            0.012182247400000134,
            -0.017676236999999928,
            -0.022358569400000076
          ],
          "positive_window_share": 0.25
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
            0.01979024740000004,
            0.005982895700000095,
            -0.03839900339999995,
            0.0027494341999999075
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "5a17506ad28bbda515701fea8e5e9ce9e4f8bde66bd49b5febd4aad94e2a76b2",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.009759451200000047,
            0.008928732600000107,
            -0.03364585869999995,
            -0.003536236600000086
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -2.5966399999945156e-05,
            0.012071332500000125,
            -0.025153161799999928,
            -0.00982831710000008
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ddadfe8a500e58a2d963639c48ce323fa3bb67b8504429063f208814804f1af2",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.010015274699999938,
            0.01499321770000014,
            -0.020535217999999918,
            -0.016146753000000076
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b54f48b12b36135d832f2f0ecb43d61a4941bcf07a971027a9accc6831847aea",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.019728774399999933,
            0.018068935800000154,
            -0.016011646399999913,
            -0.022471566400000066
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d726ac15f78e72d7171a62d66dcf57ed06bd6d2e3d2d36113bbde161c0666e27",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.023501368600000034,
            -0.0026817502999999313,
            -0.04913478839999994,
            0.0026360371999999133
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3b8400990f65f2f5c0b5d93d3ebecb37df16eedcd649695660efe4d79ce973b7",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.013886092800000055,
            0.014799835200000128,
            -0.033357157899999934,
            -0.0036527035000000797
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0038768751000000587,
            0.017914476700000143,
            -0.02869536509999993,
            -0.00991884850000007
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a8b1e9c488ff9b024597f84b549df68bca23d0664c4df78a57248136fcff3c3c",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.006060496499999936,
            0.020931286500000156,
            -0.018901371699999905,
            -0.01626118980000007
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "45451ae22fd54f5fcc4a8c83f4e0e0fcc2755c40142cb91352153ea353ce96a3",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01594551279999993,
            0.02397681510000017,
            -0.0143879162999999,
            -0.02258600320000006
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e5da6823593cc26f966c1b236eb2179524508f51ac24bb8ecc1ae9cf0512a2d2",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.012198441800000018,
            -0.005098133899999951,
            -0.03933642299999998,
            0.0030880612999998856
          ],
          "positive_window_share": 0.5
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
            0.0022585943000000205,
            -0.002119893199999938,
            -0.03463400489999997,
            -0.003196549300000108
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.007633388899999968,
            0.0008952534000000768,
            -0.029973918199999967,
            -0.009481159900000098
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "961cfe76def7b11fe2351283e3ebd181a0c11106d5a65042f1ccade8bdfaaa3b",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01749163469999996,
            0.003804990300000092,
            -0.02550469649999996,
            -0.015798925900000094
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "17c7279512899f3a91bea351e1b53d236bffc52f4a909e0f96befb2127ba1987",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.027266916699999963,
            0.0066671763000001084,
            -0.020998002999999953,
            -0.022127209200000088
          ],
          "positive_window_share": 0.25
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
            0.016693186000000013,
            0.001132157500000057,
            -0.039511953999999974,
            0.0030405478999998847
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c732a62eeaa84162fc5a884fcc09486a2b9ee5c9039b8d9a0d76f72351d048d6",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.006688243300000021,
            0.004086142100000072,
            -0.034725892499999966,
            -0.0032440627000001054
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0032037398999999744,
            0.007106856200000084,
            -0.030111912999999962,
            -0.009528673300000103
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5a60d04000e8a42a7ef2a4dfd58e04047fee6e55af55b1d752e8f78c30a7fad1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.013128165299999967,
            0.0101096974000001,
            -0.025543599099999953,
            -0.01584643930000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "5d600521d8ec100f51d0d336c6543e9781171444d584310acb517b6041a05a64",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.02293508879999996,
            0.013016678400000117,
            -0.02110990229999995,
            -0.022174722600000085
          ],
          "positive_window_share": 0.25
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
            0.02108899350000001,
            0.007229638900000064,
            -0.039614280499999974,
            0.002991594699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "819c03065fc9ba17502a28de6a63d327816c6d8cb8388251104604e1a045d6c4",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.011081166400000016,
            0.010284029700000079,
            -0.03493669599999996,
            -0.0032915761000001063
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0011630427000000262,
            0.013398315600000089,
            -0.030372540699999957,
            -0.0095761867000001
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d6b5f0adf9731cb102e277bd3fb3c7f60594548d2231a497b32c94673cd0b667",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.008766899299999971,
            0.016419557400000107,
            -0.02569993909999995,
            -0.015893952700000095
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "757cb14275a89bc4c9e5a29a7520d973e34a22ebd3401c538b8a321442b8fd5b",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01863835039999996,
            0.019439292300000122,
            -0.021265833299999946,
            -0.022220796200000087
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b6449162a482e7a08f99c096b1423ca1e879ffa87022184dd0cff292e8213cf6",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.020550903600000007,
            -0.002157226499999946,
            -0.04580667709999996,
            0.002944081299999887
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4948e389709741f3f9c362d58fe2624e794f41e6d5ef2b7968b00962535749d6",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.015379118000000015,
            0.016551460100000085,
            -0.03519722369999996,
            -0.0033390895000001072
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0054820216000000185,
            0.0195929542000001,
            -0.030453426199999953,
            -0.009623700100000097
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2b8cce8c37110946254601751fec91e8b1a3052ace950c33d369bc1269f4e54c",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.004503285799999972,
            0.02269124220000011,
            -0.025948114699999948,
            -0.015941466100000093
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d8d5c98b26ff14e3212cd6294dddc02b69e28e1725828e71a010ae9c00e64f87",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.014206801399999969,
            0.025782043600000127,
            -0.021471826899999942,
            -0.022268309600000084
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9b0ed793b8789210beddbfe561da3142bf989c157269bda13aa9d2e732098470",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.012802623000000013,
            -0.008201998999999951,
            -0.038856216899999976,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0028627755000000185,
            -0.005294906299999937,
            -0.03415379879999997,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.00702920769999997,
            -0.0023554368999999208,
            -0.029493712099999965,
            -0.0093836465000001
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "3cc7b53f43c230cbc0bbe5e407576b80e5c3c8401dd8cf82ff397d5c07f70d48",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.016897456499999963,
            0.000517123300000092,
            -0.02501194519999996,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b313af62bdd5d8e3e6b7fef4e167294ef0b09dc0cc58c92f6913a9a1385bd71c",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.026706779999999958,
            0.0034086368000001074,
            -0.020524794799999954,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c043be32382e64bdbba090ec810f1ccf50a09fe8648fc8a3408bbd2ab9ac73c6",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.01791955380000001,
            -0.005408250899999944,
            -0.038588996599999974,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.007817903200000014,
            -0.0025011581999999297,
            -0.033822478199999964,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0019953774999999785,
            0.0005241547000000846,
            -0.02920849869999996,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7c2b3fc2dbedd2b079ebdeca8887a83fb588fd2a1d89ed4f35c2ff52d779728b",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011953744399999973,
            0.003400747400000098,
            -0.024627639599999956,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2893c794a262dfeeb1d55eb234d4bbc50613e92208bd8509d365e79e48e8e243",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.021736729399999967,
            0.006298128400000113,
            -0.020213485899999946,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7826433e193e4ac82cc351ff0995a6b514018d7da192d993bd018af86f9827f0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.022850843,
            -0.0025671034999999384,
            -0.03826111699999997,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "8cbfd1cd2d9316edcb8d2b295fa7dd39a4888c1b6c1a9fd7cd02af0f71389581",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.012833012900000006,
            0.00037873340000007735,
            -0.033590530399999964,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.002925908700000014,
            0.003317802800000092,
            -0.029026375099999956,
            -0.0093836465000001
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "77548bc87ab8ee39a946a4bb2c139e0addd6da3a1b8a8eb663acbcf366d946f3",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.007009219699999979,
            0.006313415700000106,
            -0.02434132619999995,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "23c50db9ddba5ebfe44269566b665b6b65bbdf61def5dfe671d025e6d5a010b1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.016835809799999976,
            0.009219996700000122,
            -0.019926763499999944,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.021917482100000007,
            0.00022664460000006853,
            -0.041513063499999954,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "812af4d1fa0b091fb7419ff0da1d71ce91fe65a0a3224bbcf41431dcebd0b08d",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0177531511,
            0.0032144689000000864,
            -0.03342085199999996,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.007838049300000007,
            0.006197294400000098,
            -0.028684052399999955,
            -0.0093836465000001
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cbe67dbd8ea3ade52ec52ba1d9625b2a6f87d9e55ccafd9a64fd847a889053cc",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0021024970999999892,
            0.009149051200000115,
            -0.024166293599999947,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "461c154a7e2353f2283c499ac85775b992b924de41d0fec46d9f06b5172f7142",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011913023599999982,
            0.012103520800000132,
            -0.019709548899999943,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "f06c82a4eeb01c2ca1b3775d507f3fdf523eac9e7bd4f72ae421cb474e7f3e8d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.010745959400000019,
            -0.007283274699999941,
            -0.037748875599999974,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0007722704000000247,
            -0.0042766253999999265,
            -0.033039566499999964,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.009119712799999971,
            -0.0013636651999999125,
            -0.028325114199999963,
            -0.0093836465000001
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "9b49243fc490f86a5308087d28dcd0c8743ca5e9e7f2f9f5645275731e7a26ee",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.019011600099999963,
            0.001535304200000101,
            -0.023833733599999955,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "46f84d8aed1026e2d80d880921222dcafc41aee81ce7ffb4371076fddea389b7",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.02886605839999995,
            0.004400308500000116,
            -0.01938353649999995,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a742864c7a1208b39c7fae284c174b8dd0af4d1de90c2fad405dab24d97015e9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.013318335800000015,
            -0.0035038223999999223,
            -0.03625885859999997,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0033446468000000174,
            -0.00044901819999990794,
            -0.03155493099999997,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0065473363999999715,
            0.0024635420000001067,
            -0.026897708099999956,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0be1879f481ad47d63cb1e9e3839ecd1e8b8a47f13b42f9c203ebdd2d8b36c92",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.016437423699999967,
            0.005372311400000121,
            -0.022278061599999947,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cd527804e36527d86170dc60b7b5297223c9325a141bce31c0379910247fe5f4",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.026289181999999967,
            0.008336872300000134,
            -0.017790665099999943,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01589071220000001,
            0.0003237848000000945,
            -0.034812760499999956,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "18fc14e280c2cfd24eb7a861ce0ea745639459e640b134c7b93c1eee85bd3f1a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.005917023200000017,
            0.00333660160000011,
            -0.030111208699999954,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.003974959999999979,
            0.0063172584000001225,
            -0.02544117949999995,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "64e3052ef8fa0319a7c2533e42c13b53422f82ad86eb68d7701d663c462fd129",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01386534729999997,
            0.009299975200000136,
            -0.020874436599999942,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8088cc365f89e6679290e380387e1324139d60bed3aa5ee409fd03ee528e9a99",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.023746647099999962,
            0.012248343600000152,
            -0.016340713799999934,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01857590640000001,
            0.00414522450000011,
            -0.040140296799999954,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2ea28b5fd16155856db1a6aaf045c7c6a38ceefbc42b4e51cb92f1e5a3291080",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.008523241100000013,
            0.007158041300000126,
            -0.028745191699999947,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0014025835999999792,
            0.01021164550000014,
            -0.02388286229999994,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8e9ceaba7690e6d3faceede615245b6d1a7554518ab91ac3b377c4df97f4c0a3",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011293270899999971,
            0.013127282400000159,
            -0.019428830199999934,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "fb7cf5a396194be308efbdd959d12d7a0c48b1193d5a2caac5caa3adc4c65a92",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.021172670699999965,
            0.01618500740000017,
            -0.014866787299999927,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "318930da62df7a9a4b135893117f29e6080cdee95f09a82d0197d3413840c2a1",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.010745959400000019,
            -0.007003358699999945,
            -0.035852050199999985,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0007722704000000247,
            -0.00399670939999993,
            -0.03119730669999998,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.009119712799999971,
            -0.0010837491999999144,
            -0.026479054399999973,
            -0.0093836465000001
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "71cb3c31412438e23d4b9bff35ae94c701cf15c333086d98008bcf43077b98f0",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.019011600099999963,
            0.0018152202000000991,
            -0.021911212999999964,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "65e02eee14f0acb0a825dacbe164cfa06365c84cde2b215e2174efcc30cf82c1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.02886605839999995,
            0.004680224500000114,
            -0.017457791299999956,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a10c8020a0773c04afed2636a58bedf090d4fbf98ff1d3b60925e0ea4e097776",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.013318335800000015,
            -0.0029439903999999295,
            -0.03273824049999999,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c3738ae7a721e173bf76984f66c2f685bc435209fd4dab537ffc550a62a23d7b",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0033446468000000174,
            6.882640000008267e-05,
            -0.02790784819999998,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0065473363999999715,
            0.0030638483000000986,
            -0.023213359399999973,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "19d00bceaeaee45b90711aedc56891ccd0aec187c04e0c1df0557f9894ba521c",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.016437423699999967,
            0.005940141000000114,
            -0.01859416049999997,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "56cb7fb31d203469a3f1c85e5c30ae6f448173b6cf02c6203dc31a8c63b6dd5c",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.026289181999999967,
            0.008904701900000127,
            -0.01406056069999996,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01589071220000001,
            0.0011715304000000822,
            -0.029433865799999993,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "25d46927d3049e38377b2aab3cdec3957e2a5adf6b1a27fe97889bc46891180e",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.005917023200000017,
            0.004184347200000098,
            -0.024711481299999984,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.003974959999999979,
            0.007173001600000114,
            -0.019988401199999978,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "daa598de199db4f2abe5d43ad5487cc9e98f006ac89533dc04afd523606d5df7",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01386534729999997,
            0.010155718400000128,
            -0.01540786219999997,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0752a8b6c7a878a88b448142929f6a9f3be2c1ed8c4201bee06a7d6faa25ea99",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.023746647099999962,
            0.013061999400000145,
            -0.010812496799999967,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01857590640000001,
            0.005230898700000097,
            -0.03446688589999998,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bd323451f9997167020ef8b4d4563d57e755f853e5a756382be5fefaf5d43de9",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.008523241100000013,
            0.008293700500000112,
            -0.02153855839999999,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0014025835999999792,
            0.011355302300000127,
            -0.01665870589999998,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6b5bf2db39c7a5312bb922ccbb7f79eb56adc7b97c17b591d33d8da2a6250bc1",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011293270899999971,
            0.01430341590000014,
            -0.012118803699999972,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "edcf6df73115739f59495a635a2f6e95889a072a90f65715f3683de0279b6036",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.021172670699999965,
            0.017369138500000155,
            -0.007485999099999967,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "89ad7adcecda2efcf8cbd6a6401ed3e6ed96b851083accd850f6a0c518aa15b3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.010745959400000019,
            -0.007003358699999945,
            -0.03528122149999999,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0007722704000000247,
            -0.00399670939999993,
            -0.03062647799999998,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.009119712799999971,
            -0.0010837491999999144,
            -0.025988222399999976,
            -0.0093836465000001
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "8d2fb7a3cdb517396e8b9acf88ea220280c39c0d59402311d007504ddef79d5c",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.019011600099999963,
            0.0018152202000000991,
            -0.02126968609999997,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e2c8bb705339dcc5463a443085ff18111efcc79131fc23f37b0689f00224e812",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.02886605839999995,
            0.004680224500000114,
            -0.016879964699999958,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e63647ca2002739cec51718c1fc3233e1fa1a415c34c193d001a7c1cd59f7a79",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.013318335800000015,
            -0.0029439903999999295,
            -0.0315254849,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "8d4112ab3315d7d1ddc27a4d870f5e4b35afd1d22a3825b4b4fafb3f73ad8f3b",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0033446468000000174,
            6.882640000008267e-05,
            -0.02675919289999999,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0065473363999999715,
            0.0030638483000000986,
            -0.02216579449999998,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1421bd391e699bf7e3db84dd519ed0f9abd810d6436050bef6fa5aac1639def6",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.016437423699999967,
            0.005940141000000114,
            -0.017508606999999975,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d6db03d900f41c0c72fa21236bdcea5a570191d0749630206087c435ff3a8898",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.026289181999999967,
            0.008904701900000127,
            -0.012920741599999966,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01589071220000001,
            0.0011715304000000822,
            -0.0277073839,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a01c832be39f3c46cd5b376ca93ac9936e7882bf59f762681abd6bb6e5fae186",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.005917023200000017,
            0.004184347200000098,
            -0.023020988599999997,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.003974959999999979,
            0.007173001600000114,
            -0.01826092079999999,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b66db6d06efa7d1e620ced97604377222cfc7a690e9e12414f834e4ae2dde28d",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01386534729999997,
            0.010155718400000128,
            -0.01358645629999998,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "290d66f51c3334521564ebbf587b2c8f96dd3feca2c2d788144f482ee2e0e5c3",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.023746647099999962,
            0.013061999400000145,
            -0.008988124799999976,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01857590640000001,
            0.005230898700000097,
            -0.03220556449999999,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "26296eafe932dd4ff9512c67b6adb54a054d9512ee6fe088c015bb6b30ae16ef",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.008523241100000013,
            0.008293700500000112,
            -0.019088174200000002,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0014025835999999792,
            0.011355302300000127,
            -0.014458035999999994,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "20c920b02310daf4b859f8b813f29af3b4d257da9ba48b2d64b95f4328dde275",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011293270899999971,
            0.01430341590000014,
            -0.009726139799999992,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4b29dc52dae93fa89372642c660f99eeca7df753f4baaa1174e66a58541fe27d",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.021172670699999965,
            0.017369138500000155,
            -0.005129645099999983,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ca6aa7709729328d94aa19e8129a8ec3f86ce1d32039e064fb623fbb8f1ac58e",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.01026760110000002,
            -0.007003358699999945,
            -0.03528122149999999,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0003267695000000251,
            -0.00399670939999993,
            -0.03062647799999998,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.009565213699999964,
            -0.0010837491999999144,
            -0.025988222399999976,
            -0.0093836465000001
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "dcaf4f81927c472859f6300f1b7ac9cec525bb1864c151d3d4070612ae8e5df4",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01942775949999996,
            0.0018152202000000991,
            -0.02126968609999997,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "eb49287bc547c6e506f3aadb7eda6b7daada828a03319fcee65cf5fdd3c3fd6a",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.029237282999999947,
            0.004680224500000114,
            -0.016879964699999958,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "8001ce7a61e6bbc527399ec1395b7cefc4fdc1a06d706c582a8a9beb5ebe3b02",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.012514588300000021,
            -0.0029439903999999295,
            -0.0315254849,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "268cf23cf0dce23398307940260e0cecf8d96d17daf5edc865eaaa770f936901",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0025737567000000267,
            6.882640000008267e-05,
            -0.02675919289999999,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.007318226499999969,
            0.0030638483000000986,
            -0.02216579449999998,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1543bfd39152b539b9476475cdaa1d411c13d91f416cbff3ba8211a1b4f61a45",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.01718127229999996,
            0.005940141000000114,
            -0.017508606999999975,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "11a928c621365eb7f902d7635a77ce6899022428a591ed6644c79dd42f8bf607",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.026957638399999956,
            0.008904701900000127,
            -0.012920741599999966,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.014795417000000022,
            0.0011715304000000822,
            -0.0277073839,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a71457d47e5c1fa6cd81dc8bc2295e36bc60f4d0e12fac791b33187fe27c62b3",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.004821728000000025,
            0.004184347200000098,
            -0.023020988599999997,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.005037397799999968,
            0.007173001600000114,
            -0.01826092079999999,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "04c0ca5fbcf902e5b9afe76b36a90ca3ad2104030989324ad9d294df660cfa89",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.014934685099999963,
            0.010155718400000128,
            -0.01358645629999998,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "64ca51cf505764cc7dcd808efa152085d9373da22f33c6e151902050d8ddf2c4",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.024711151199999948,
            0.013061999400000145,
            -0.008988124799999976,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01700954680000002,
            0.005230898700000097,
            -0.03220556449999999,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6c762a7a83d430eb4aae46bc3b939d9320278f039a0d1733b209ae55c6e64f75",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.007068715200000027,
            0.008293700500000112,
            -0.019088174200000002,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0027904105999999665,
            0.011355302300000127,
            -0.014458035999999994,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a6346dd7e1804c75cf8dd0eb15ee8b4c4797741b2f0c1cb674ef99891c3fa9e9",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.012688197899999962,
            0.01430341590000014,
            -0.009726139799999992,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d3c336ea2c30970cb838c9559f28ef5afffee91fabd06beb0c1839e49256766d",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.022464463999999955,
            0.017369138500000155,
            -0.005129645099999983,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a38ca9017ee7323d6ca2fa38e717ced6f522427e0f6ce2d771d4ec8eeb087dcf",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.011400911200000016,
            -0.006543496699999948,
            -0.03561510629999998,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
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
            0.0014610637000000218,
            -0.0034718668999999328,
            -0.03086927059999997,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.008430919499999967,
            -0.0005589066999999205,
            -0.026215118599999965,
            -0.0093836465000001
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "4db6c5d5762841c37dc4de1bc30a10cd0e27c01bfab964bf6c8365bcc5313082",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.018323006799999965,
            0.0023400627000000965,
            -0.02163666249999996,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ffcbf75f862ff7b602b47b861df9fc8a853843804e38aef1f90875d90a3822e7",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.028098288799999954,
            0.005237443700000111,
            -0.017175243199999954,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b3b9838498a218b2c75976ab65e15e6c8076bb286d1ea658b3fbbf8b7e944b0b",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.014798891500000015,
            -0.0018943053999999383,
            -0.032235805699999974,
            0.003185574699999888
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9aab49f04c34ce9b0218247ceb595fe069b32faa5bdcebea8b02ec4761a1c832",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.004825202500000021,
            0.0011185114000000773,
            -0.02746996459999997,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0050667806999999745,
            0.004063548300000091,
            -0.022816012599999963,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6a052b308f6ab167426ab2a7e99b79c37ceafef5132f04f03ebf5c5e3dece9d5",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.014956867999999963,
            0.007037298200000108,
            -0.018155378099999953,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "081a8609b5d2788de7dedead3776df8fed29be1556ee3ac5015b21181e073d7f",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.024763891499999954,
            0.010001759100000122,
            -0.01366686689999995,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.01816303030000001,
            0.0026960729000000717,
            -0.028729611099999972,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c3a2b9e6812b3f6ca0f3a545088ae9cbf0150071f297f84c671e4ca96a08d7fb",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.008189341300000017,
            0.005708889700000087,
            -0.024070658599999965,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0017364833999999746,
            0.008745016300000102,
            -0.01928112789999996,
            -0.0093836465000001
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0cad56c70b53c6f45b92078a0eb03bb554e4515d6c3eca9cc7cee91426f915e9",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.011627170699999967,
            0.011792613600000116,
            -0.014661279899999949,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9e3707d9ca4dd26f414d299f19d60bc43cbdbf2bf2b6da6219c626e1973457ae",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.021429594199999964,
            0.01469899460000013,
            -0.010092642099999945,
            -0.022031135600000085
          ],
          "positive_window_share": 0.25
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
            0.021527169100000007,
            0.007280283700000084,
            -0.025384870699999968,
            0.003185574699999888
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e4fc4425fef1519fb6942a195045717cd0d7d9196af4d4bbd9def08121347069",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.011553480100000013,
            0.010390657700000097,
            -0.020554929299999962,
            -0.0030990359000001057
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.001627655400000018,
            0.013467055000000113,
            -0.015761589599999952,
            -0.0093836465000001
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "40da851baa2cf49bf7ef0a57c4209c8c76198f9c0a177a116a76f059fcdf01bf",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.008263231899999973,
            0.01648014910000013,
            -0.011096955099999944,
            -0.01570285230000009
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b846a0a7e4c43066dab6457e533f7c7c435e82ee1372dd35cc746ba1dbbf7394",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.018097696899999967,
            0.01949578670000014,
            -0.006592743899999941,
            -0.022031135600000085
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
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05539749529999997,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "adbca544282724c5a7a2958f71250737af4685caeb95879a42bc97e6fba41fa0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05539749529999997,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e731b06b6b8a57905247003db6fe52b6b03c796f946f86db5ff1d9a78d7bc936",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05539749529999997,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "46f7afbe4f52f52cf8832a43b79598af956b8e0d3541d6425464a97964d756c0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0efce7b04e5e193de8d96ae22d700309b50d9ec1b26b72a73c3a1a9f6769501d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1b03d2707a07fe802f1760263c82b3d4b8342a455e2139542829ce33055346c3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cc26b8dbf9aabc5a954cdba7f15445f6906c516ab4ca332c472c7970122b880a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "de68c4ccc59411bff11772363170338b6761dbd0f39bd7fc8c794de5cfd5259e",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b3ab56d68fdcaada002d2614a264764fe445837a7212d9cef39fd0934e9a098b",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c3b3386f66538a319e0467b3a0b591520efa06cc1ee02fe2bfe05a4bfdea1895",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "8bf92734c3d2ba8e6c3dd7f599c5b43e34620f9479e5c24f9b34ccbe045b4947",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cf9cde26dba3c73a5567f30c5d5a03c684d25c008ef9fb3ad24b61ff1e53e962",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0c441452555d21094fcf63b740acffe7a9176260632649cedf006f78d5c922dc",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05539749529999997,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "23d1e52eeccaf4bc0cb8853853c2be63a69dd7762b18d7289741c7e7f37b98f9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05539749529999997,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a5c471fd8ef46b803b80689400b2fc0c30d0ff6a0d4e6a27deb9881f27514916",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05539749529999997,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "37ce18ea991b11a33fd546c75664f8cafed609d4a7311f44011f1ac689f5ecbe",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c4ecea34d33f8e9ff517190ef1639a0078c204de4df752764eafe9f1f8ec39cd",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c4d5b093333d5f925ed448b6d6d3817b80258f4b6df0402ff62d7ff6e5de0d90",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ddcf08c0eb422a69906267785f04df8ddf6ada327f9f7dbfc623ef071dcdcb28",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "548bde01f4ae3b39c455be93505eda30b321c79668d9f8acde7f81aac0feefc0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b1ce106b9791d9b2313e33ad5d36230eb1a10a96118d83ef7b6350514a957bd9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bd61e6ffa991468a6062bf4047742d76be80658e74f9212ae8482ed6d90027cf",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9fcab2c463797c9b28ee01148cc476784bb2473b84bf8f2ae68c546f3cb9c946",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.056828087699999946,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "61609ced85a7068bb6b227a8778db35ac30701765ed24a2d414765a7965417f9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1a8b7c2b566250e4974b9accd1eb288e0b1c3b9ece047603707261bce302dd08",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055663244999999965,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "07a6da34a90c5c24e8cfdef1b9c07e2ff039d51fce0b917d7a4ba2527844daa4",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055663244999999965,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "441990e611d4bfed0a753adb7d990a66af9681ccb20bb032d058f3e3bf793c67",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055663244999999965,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d00659d885e156983f250b8d53e6c117947d0afc46d076fdcf1e024dacb4145d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bc6f099a3c49e384ab643559ec0ec44d65d442396a1dc177bb4c7181ac52ae54",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055972657799999964,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "492d3075b7505d752fc4569124324cf50ec4e1e12399bff92d72a757be0abcea",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055972657799999964,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ebab91384cb73c29a059a5f61ee4cb1db962fd86e95224f09308839b0f4f4a7d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055972657799999964,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4266ee5cc6a9ac907f421389ef9cf425c951ac9475f81729c7ed50f0150b1b7d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6a23f24486bb79be48113d97b10bbba4ac19f7ddef0e43e81ec8d1dc67ff9092",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055972657799999964,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "be75d5c8e26860196c89f31b797698e558e2c7568cb1a802d2a09507366516ca",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055972657799999964,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9a5ffaf7d90c7cd06362d27f96a11d349d1b8f1dd81f180cf81cb93f13789ea5",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055972657799999964,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "fc714e5166dab9d576b2cca6b8263c9609f4ba786bf9b50769aa593b8e6c47d5",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.055606002800000005,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1a1d82ea59c99bfe7ac50c54c249f33eecaf9e8d07e4abf76bdd391e3652f99b",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05779928639999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "915b629158bae600eedb793e1b7461db1bca2642934e70e963373d51bb0eec9d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05779928639999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "505ad729a6207cc8be7b2d3fe972a46ba111f58eeaa7b3b530a2cfa2e1d371ac",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05779928639999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "59b014959d6ca4769d4753c652daf0ccb38e962e5c3d4d3ea42fec5bd2a2a57a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e77bf2a8d1f196188c97d7cfc708d2f57c96d69e508253e83cf169f5c4d6c81c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "add329e8e27ecebe1d584cb1f14ba572d35710aea60476ca8ccbc31431672993",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c8d96d02fef2052aa1b5b4f37d053341689597b833962dea2b09040dda9cd81d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "64e8b768141ab52605621addcd48eb9cc31b1ffcd58858b53f7d3015b5511af3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9a8031973c8ec766ac9566a91c4f700fd8d2a7712f8f4e3641c67b8135e77bca",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4a09e9f42c304e0c0f941aa4fb00cfc45f473ebaa326e8c08008a0a2a91e8d4c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c54abf54583ce691431dbb42312227a0d225834bfc9a325757243da770f414aa",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "387050649e85b36d7c6e999764671f946e30e8f6587f959815efda2fee8967c9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05779928639999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6d0b27b35b089a17eb96ff6e8962cf760fda88c3a3d4da56f20518c119a22fea",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05779928639999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "7e25e305550d53d8dd69c7eeb54c0b6e13240426682cf97ea575590254e15a8f",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05779928639999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "09c907ccffba9c79389da45ffbc273ef56ff552a01e37bb47bf4b4f538584933",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "330e9079a8741ac5ed4d998877d62b08834a5251908efa8b14fa9b09f101662a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "eadf7cacdbca92462104fbb663d7c89152d0846f8079544838f53c144e80b383",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2c75c42046ef3a6d0f0febae245bcf1a0d429394847dcdc593062e759c731b73",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bdfeea35c79ba78c3054cc430396a6f0454ffcb4c0eefca49e78830b92de5ccc",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3d16b6890afaf109d0c4451863565fe56cb71dd1454039aa22d95648f62fe42d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e22018ff8811c7b7c47fb6ee98be4a18af5dd760741f1521c9a5e5246a5dcead",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4c5dbff3038888fbc8ba660d551023c7213bc3c92e7d698161e4831ddb927e16",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.059921800599999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f985f1617e9bb77ea62699fce58cc6011e56a4fb40c9d3565f854b8ed05f5e4c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1a0ba2f00044f420ffb20d85ffd3b630915c4f0587b631a9e61e8fc68b943b2c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05834478999999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ae2f1ec1405653fbbf289a5f020fe4b9ab1365648959be0631bcd1db772eadad",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05834478999999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "50aeca7dbe7571cfa0dd145f2032d40a70a44efb66da2450d2ac21fc20d8ac95",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.05834478999999993,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "02ed4b871a3ac2dc98111f5f7dba62b21c61af723cae0b25f7d3fa568b6642e4",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "13e36312d75235095a99fb4673caba20941b36b205e0f88c729e7bc1900c423e",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.058744448199999924,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9755e4a2985929b24476e74975b3281dcf102f99fc184339e833c99c9365e566",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.058744448199999924,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a2606ff0dd53e64bdaed4879ebef55587c576527665e09aaceec8068c023f1fa",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.058744448199999924,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0a073f60f2b4e958cf7bb14f680436f06eb26b748c281a78271005a1011caa57",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "42105ee5fa31f194122fe24f85377d35b1afea27da9bbed7fe4efa1b04df9b81",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.058744448199999924,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b4a19d9ee57a1ed883fc45f2d940417ba33b9bcd8854935c3d9ed02a29df5c44",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.058744448199999924,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a05a3729a4575c24923de713a0ba59f30f2cfd21472905bb9a557e2e85fe5392",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.058744448199999924,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cd978ede184d59c0797473a5f7cf0173d393d3398a9aa841a8dc97ea58a53cb5",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0583545212,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c1144d55f4b001966183229609c62f71533195749e340dc147b58b34996d34b1",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.060198887399999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b7aa686834fba404e57ce646e62ea5ae9ce6b33df36f634aa733cced8430673f",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.060198887399999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b7c893047999c7d6c75f8da734604fb8e463ffc56e36cbccd00fa3732bfff73c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.060198887399999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c2faa48b20285145059a9507df7fb128457be7916c87597372a667e3535514da",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "376261879bb3a98cb9d9f885ebc4606248424ee5623184ed545ba758deb3d361",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1c9aaeaf1c01aaa86bd6f9b2a9def8c7f55b76815b48c037012df2db186a7ad9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "53ae75468006b31323bf7c8217cd72f20b714d1c350e56945d1b7cb891a67f57",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "dcbdfc7b407f6dae2709dbf78aaa01157de1752506623e224a3c54d9dcbd44cc",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d1a7f1bab43c17c56cf770ea8414ee06ce61b60f10d4a20f8959f14d48824bba",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bfc4d87ac49a11a984a17ee8bc2a235c4905e425284c08722bc83a3787c3da0f",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "90e95eca032bfe50e881261b29e392fa034ba82c6ca75e51bb44c3dd72c9275c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ec4085c7e24702acce52ee2a5997e551a4978c5f8741df94c163d6422bc23f7c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "696913cb4f51a33bf3935b51da3b38e1dcd6d1a97557ef171529553b4d7bfbf7",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.060198887399999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f403091f4d2bc6ab744045f21d94ccd7cdb6bb69adac3cb07ebeb46eaf36f684",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.060198887399999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6fc8e2eef32a9bbeedf4d1623087ba3891701d13c78d22843cdf57a1c9bb12be",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.060198887399999894,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c2209a5b405bac286c73284d9fc581c16a425d179dcff71abdeaa8710254fe0f",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "52db97a65a1d4ad3cfa5799f59629bcab32d4cb9e84027e5ec07afc0fc759dea",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "520cb3507a916dc9d9f2fa51dacd4e7c3511bbf9eee1fcdf03da237bb9f07e11",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "74615fd57e7c943c143fd077540a3361517eb745a26477811b844f682456d219",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e9e04869e6239071f9dd8cce64bab3d8eeb7ca305ff95b34978dc8aedbbd705c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "13a36acfc6269b30b569bb601b5e16abcb027c50365afdcb43ae693eeb166958",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d576233a8b8830e3532da4d368e8f230e4de74243f423ae4693135f0662ad5a3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "44cb7392c928f53c521015a2cd2d0d65ae8766b2261ffc6f5861bc3196ad086f",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06248258079999986,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b5ae512c057c4cca149fc22aa5ab060d43221cfcfb62184e6b988b8670e045e0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ec7cbbe41821b4534745fc5abe749c3fa818c012a03773917d564783155e3c9b",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0610145427999999,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cd308639566094e1248179f35cda2c75f4b3f108d88965087b313c6e2c18ad0c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0610145427999999,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "45fc69735e2a6498f6345128fd7d46a7e5ad7bc5aa540c5fe68355a5a078e402",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.0610145427999999,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ce25616a08a3a713d3baa8fbe9c681a24d2d0ae6253ec78d562b4a0e52cefb9e",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f3b1956a637c63c935fb3bb6eb3e713d0e7881edf280d7cd43341778f5d206ec",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06132745559999989,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4ef5f2e60b0a12f9c3dfdfc50ff212dda872ca3811ba7eb1a418cd635500ee86",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06132745559999989,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f38dda51d631dae80a08a0027a6f82f3f06d6328bca9e8c207522a8316d0a562",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06132745559999989,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "5bf8412a3fe2565df7fe2ecd3cf0bf8ef854466aaaa317215f6937328ff3ab18",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1b8a1433cd25010fb5c550b3665e973d63467cfe7baa46e828f42e0e3914c235",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06132745559999989,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6c62868387b90bf0e5d50a007eb97dff2c5f410ac777bb74e949f24ca4545cd4",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06132745559999989,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bf18cc0ff8f31c28dd27bd53bea9a4b8740f08d9cba11a3a14cacc6d1091b9ef",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06132745559999989,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f08a6c33adf0cb5410922ccb5eb4e34f92024956a5c0332e80e647bee7cb2a01",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.061103039600000006,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3de7c13e774d534c952c8462bc02d4706ba6c2da63098dcc633d9891959119c9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.062455745799999865,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "161dbc35e812294ca418d3a491ac83452d7dae568d1e5be10421ee4e19fdab27",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.062455745799999865,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1e3c5a3a25ba0ff260f82888076b19bd3e2497627e62d17545f54d5382b673a9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.062455745799999865,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b9bc2fd53b37952d0fa31d7ee6c7abb2df29fc0c936f761b0b4d5de89d3b3c65",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1424ccb6f148503ef949aaec1c140dfeedf287a16154036803144b75c5de03c2",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a164ba23ba9524e034fe07bfe24aea3b27db569bc592dca70655d980b21fcdd3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "fd3352c6d16146fc47234c6239e5393864ac990b33c70cd0570d7c36192d1a49",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "7ec3d94889c6256057b589f9a9349e6f11c29591facbfc6dd184ffe7dc58d8de",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d352ec1510356ccb70944864be43f48121546077644fccd6d3b4ebe46472fbb3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "42881131aa958b37001b7427d92d5475137405fe28d79f77e10b24316f77ab3c",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ed0dd236355b7a8d9f42cd954e2aba0cca2d130aeb2e511c8145e52b3b5c9229",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a7e3098ae1d238b85a68bf710352484a836546f125d4abdecafda4bd5b6ce8e1",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9b43cfb13d4e03c1d855e2b81d3146f84cdd7f6155194208cff59649e4fafedd",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.062455745799999865,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "275334c7d66460505e7c71e7f1bc8e971d6b44f3af26a6b8dba212d744d4d00a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.062455745799999865,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0dee04873a3ddf671052ea481c0d968718285776ddcfc900e5af011213ad542b",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.062455745799999865,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "8538b7affe3bb97a027406cdbf0ee82edbf2a14cf9b0164e0f3b16e518dcce49",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "05063fd72167d3a3a2da97e7c8c63023ebe7fe845967932f2a3a68b2d9023574",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "707d5fac1ebe3f88df9b8bca06082ec5f029dbaaa67f900f17bdbb99418ae959",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "12643fc27869a63bcca87e3e38c0aae6f7825f6728622759920ecebf182931d1",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2d4e420f979f519ab7261ed8c86ca8308618af6e63b56f5476e2d2fce0fd8a14",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "76c2fdbf72a6ee26af1f5ea026eca75afdfcee1086f79c917047a7c7ab3c01ed",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bcaf1067a4e98787b432db5b6681a208b9eea62150fe336c1090df3b4f678dfc",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b54d6a3fa555012188e6f740379a78f0dd22cd68864cae4eb9e915ce67e8baaa",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06458901119999984,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "17c9c940096d43a773c4905d1982dc3a9c901fae82b8de14cfb27f6844ce84c0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0165967a82c576ce3dbbcae3a03db3d0b9766a1b6ba0de5459235753d980e642",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "091fbd2cc185b592a8e7b80f30e3e73fb8f3034ef10dcb197ae208d1892901d3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "17dbff0a23e5d013e2d4b110485364f1d520f1dd5b5b79ea9cec2328e6048ff9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a7d1bc64be18eec70f804ccb675f4de3265988e1f7041b8dac11721a645fbccd",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "81f56cf56a5de341c5d98c82cf7d5803225386e334d2d1d583526e9c4ea5e855",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "512697187c6fe64646e9ff21e491e8e481880ebae3fbd0e5138c76ee036ec1d5",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "673a28cda6786a76d77f41b3d518b2dc00aa5c1482c95959af2c5318831043bd",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "64e6f60cccaa85fd39f8b1fa74bc32547aeab8eb0fc0ea90356ebdca81ab94da",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "f20359ca6d891690d890c115b86a566a971340c2017016139abfe828870ecff8",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "891e4aac1326376aff627803dcff3b5d016adb3f7c1d241c033375b50f4f5659",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4bfb9404f1e53fa2d8ba993a154c73bc83122dfdb210429965cadb5122d6cb5d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.06370019559999987,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "443522543e3e8dd041a7ffeee4af344efccc3ec16395b525bc91265308a4d846",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0388718755,
            -0.019340616,
            -0.063851558,
            0.022377599999999866
          ],
          "positive_window_share": 0.5
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
        "515080.SH"
      ]
    },
    "experiment_hash": "e113e53a07ecafd1ad052db70d361bc762d0b4acc91aa0225e6eac57d5a2a695",
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
            "cost_drag": 0.001178279575,
            "cvar5_improvement": 0.019327339150945522,
            "drawdown_improvement": 0.09937772336001344,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.022653484541373614,
            "sortino_excess": -0.1153033698425002,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00158517795,
            "cvar5_improvement": 0.020061810968435064,
            "drawdown_improvement": 0.10431911817050307,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.44770288052733903,
            "sortino_excess": 0.5435723096026435,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018351761999999998,
            "cvar5_improvement": 0.014093111642278089,
            "drawdown_improvement": 0.07101050786095664,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.14799644947391577,
            "sortino_excess": -0.20199104652574087,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001096090675,
            "cvar5_improvement": 0.01944057478437961,
            "drawdown_improvement": 0.09942641670563643,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14987510611955263,
            "sortino_excess": 0.2409950721051808,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.004051092975,
            "cvar5_improvement": 0.01322523853251518,
            "drawdown_improvement": 0.06991097162141002,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.06030561451588971,
            "sortino_excess": -0.22778340564173577,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020729273999999997,
            "cvar5_improvement": 0.012276968554292916,
            "drawdown_improvement": 0.061731132594018245,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1941390935057879,
            "sortino_excess": -0.2745354357163836,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020626411,
            "cvar5_improvement": 0.011865204761904714,
            "drawdown_improvement": 0.058991439267676665,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.25806696725327694,
            "sortino_excess": -0.37863426855235927,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00232087925,
            "cvar5_improvement": 0.01832334548619682,
            "drawdown_improvement": 0.09465692587430738,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.11386166893792682,
            "sortino_excess": 0.13477008391841638,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00289733745,
            "cvar5_improvement": 0.01832209046584503,
            "drawdown_improvement": 0.09613420241035134,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21811135663617592,
            "sortino_excess": 0.5577382351010265,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001851613925,
            "cvar5_improvement": 0.013686325265848648,
            "drawdown_improvement": 0.068425072640559,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.28887504629981986,
            "sortino_excess": -0.43343132255968086,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00312494125,
            "cvar5_improvement": 0.015315810648204472,
            "drawdown_improvement": 0.08158748689244316,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24608892087149542,
            "sortino_excess": 0.2684733802041798,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017870297,
            "cvar5_improvement": 0.013989588508550286,
            "drawdown_improvement": 0.07039696514093718,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.13656136756385406,
            "sortino_excess": -0.2033050049155272,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00147282065,
            "cvar5_improvement": 0.01720901391924111,
            "drawdown_improvement": 0.08655601119301762,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3071790613101249,
            "sortino_excess": -0.46044287053751365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001541848325,
            "cvar5_improvement": 0.016143533323104024,
            "drawdown_improvement": 0.08312407116346324,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.031073871837304312,
            "sortino_excess": 0.06461008854488462,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0021015608,
            "cvar5_improvement": 0.011923721493364759,
            "drawdown_improvement": 0.059380960029110724,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2644958819843193,
            "sortino_excess": -0.3765231647107591,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018871416500000002,
            "cvar5_improvement": 0.019576592399742715,
            "drawdown_improvement": 0.10302627783155777,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.0556942999285049,
            "sortino_excess": -0.031422155866841744,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001793542875,
            "cvar5_improvement": 0.01377678923583298,
            "drawdown_improvement": 0.06907274793990603,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.24399669180001893,
            "sortino_excess": -0.3442816684692563,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001822005025,
            "cvar5_improvement": 0.013757671964261167,
            "drawdown_improvement": 0.06888862434997403,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.24484338210323292,
            "sortino_excess": -0.34595943305362015,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001695946175,
            "cvar5_improvement": 0.01602519329297625,
            "drawdown_improvement": 0.08377972033528086,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.11604540300870866,
            "sortino_excess": -0.24305441868091401,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002234845525,
            "cvar5_improvement": 0.011703959863844643,
            "drawdown_improvement": 0.05784124847880867,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3435616162140831,
            "sortino_excess": -0.5060706887757852,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0029568239,
            "cvar5_improvement": 0.014950089551783955,
            "drawdown_improvement": 0.0781526773343324,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.015473580533422335,
            "sortino_excess": -0.10497159685940441,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0020995621,
            "cvar5_improvement": 0.017126395569091988,
            "drawdown_improvement": 0.08939088398007936,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2408955108618002,
            "sortino_excess": 0.317974630054935,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001392512325,
            "cvar5_improvement": 0.017576046630692364,
            "drawdown_improvement": 0.08961062789438257,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.12451221447954824,
            "sortino_excess": -0.2355034819667274,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0030183695,
            "cvar5_improvement": 0.012298527577406043,
            "drawdown_improvement": 0.062173213692901436,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2758143133035488,
            "sortino_excess": -0.43002993349627483,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017931812500000001,
            "cvar5_improvement": 0.013778454879480729,
            "drawdown_improvement": 0.0690828518300877,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2517369525464337,
            "sortino_excess": -0.35675412967880643,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0027085974,
            "cvar5_improvement": 0.01348145492988555,
            "drawdown_improvement": 0.06988932006968149,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.025498826380805528,
            "sortino_excess": -0.14194579241296582,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001544315325,
            "cvar5_improvement": 0.015257164947182489,
            "drawdown_improvement": 0.07630152034789867,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.32411115459479484,
            "sortino_excess": -0.46024347650898534,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003466412475,
            "cvar5_improvement": 0.01678232986093364,
            "drawdown_improvement": 0.08924691519799596,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21482443042812738,
            "sortino_excess": 0.1908661791120482,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00185627405,
            "cvar5_improvement": 0.01818345023359757,
            "drawdown_improvement": 0.09369738971883557,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.02301275795085249,
            "sortino_excess": -0.08123070018372261,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016093581750000001,
            "cvar5_improvement": 0.015278127469298667,
            "drawdown_improvement": 0.07667984559847232,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.35916726339120636,
            "sortino_excess": -0.5224701070082293,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00180531915,
            "cvar5_improvement": 0.014363538439535778,
            "drawdown_improvement": 0.07349500440327514,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.0442519188627426,
            "sortino_excess": -0.046973447363244186,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001345620725,
            "cvar5_improvement": 0.019542710945203483,
            "drawdown_improvement": 0.1011519822720999,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2279623912811018,
            "sortino_excess": 0.12755518312548453,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002742772,
            "cvar5_improvement": 0.01413009706740224,
            "drawdown_improvement": 0.07170943500927557,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.25439720081458783,
            "sortino_excess": -0.40435190142528665,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019291443000000001,
            "cvar5_improvement": 0.015915937084408,
            "drawdown_improvement": 0.07979363976084489,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17595772097083748,
            "sortino_excess": -0.28206742732908474,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002203035425,
            "cvar5_improvement": 0.012208072090958139,
            "drawdown_improvement": 0.06262595022931577,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.26344969829187614,
            "sortino_excess": -0.4119654103969643,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.004009015775,
            "cvar5_improvement": 0.01572803441394762,
            "drawdown_improvement": 0.08490594892188874,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.39561404973765996,
            "sortino_excess": 0.4385380172441249,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002434534525,
            "cvar5_improvement": 0.018265816481413413,
            "drawdown_improvement": 0.09523307767352857,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21108046632907884,
            "sortino_excess": 0.21913823246782274,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013216440750000002,
            "cvar5_improvement": 0.017700721281133383,
            "drawdown_improvement": 0.09055576984344305,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.034336233834570795,
            "sortino_excess": -0.03368416732476601,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001587394625,
            "cvar5_improvement": 0.015519953041979017,
            "drawdown_improvement": 0.07800070345379032,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2682685770649434,
            "sortino_excess": -0.40811183677600926,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0032275463,
            "cvar5_improvement": 0.01323855207782241,
            "drawdown_improvement": 0.06922799224860329,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08113899276880931,
            "sortino_excess": -0.1926094099031795,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013271745000000001,
            "cvar5_improvement": 0.017906912256719063,
            "drawdown_improvement": 0.09282668495705468,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14870233289032214,
            "sortino_excess": 0.23239773871307598,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0023912397999999997,
            "cvar5_improvement": 0.011777086879963608,
            "drawdown_improvement": 0.05786587529957268,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3370985186233548,
            "sortino_excess": -0.49184624808866356,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013432688,
            "cvar5_improvement": 0.017440650516261886,
            "drawdown_improvement": 0.08814909796367326,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.16775001603179363,
            "sortino_excess": -0.22629780119581788,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011417434500000001,
            "cvar5_improvement": 0.019569765161865142,
            "drawdown_improvement": 0.10025171682313941,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.191080061886772,
            "sortino_excess": 0.3085226957810431,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002179663,
            "cvar5_improvement": 0.01192319095301271,
            "drawdown_improvement": 0.06011915246588406,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3179278510287109,
            "sortino_excess": -0.4747567718765204,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020733344,
            "cvar5_improvement": 0.012277747639464334,
            "drawdown_improvement": 0.06173221791179942,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1824733615303093,
            "sortino_excess": -0.2546808119380968,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00424029745,
            "cvar5_improvement": 0.013777948483774843,
            "drawdown_improvement": 0.07425092918186066,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13623276202340978,
            "sortino_excess": 0.005102970919834332,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002084513475,
            "cvar5_improvement": 0.014585191130104294,
            "drawdown_improvement": 0.07553127053877809,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.0020243887357875023,
            "sortino_excess": -0.06732781557116788,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015299887999999998,
            "cvar5_improvement": 0.016083981239611682,
            "drawdown_improvement": 0.08189827609404743,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.047044681865600124,
            "sortino_excess": 0.075034231952372,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001414343675,
            "cvar5_improvement": 0.017713395907332254,
            "drawdown_improvement": 0.09154207319826108,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.00783749420399471,
            "sortino_excess": -0.09638077637883849,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001097826075,
            "cvar5_improvement": 0.01896601918693097,
            "drawdown_improvement": 0.09586728757493593,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2815750045695501,
            "sortino_excess": -0.39428114945109,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00226210485,
            "cvar5_improvement": 0.017802020709828826,
            "drawdown_improvement": 0.09092317159968902,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.16653056190614673,
            "sortino_excess": -0.2977975673497343,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0025140059250000004,
            "cvar5_improvement": 0.01210716804610035,
            "drawdown_improvement": 0.05999526997355226,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.30890303000283564,
            "sortino_excess": -0.46920529859377913,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001827840725,
            "cvar5_improvement": 0.018017986111435767,
            "drawdown_improvement": 0.09346681468531873,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.30817049421122034,
            "sortino_excess": 0.3390439258163408,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0033937174750000004,
            "cvar5_improvement": 0.01369263923552455,
            "drawdown_improvement": 0.07283619815261222,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1278510105923243,
            "sortino_excess": 0.09642871596310285,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018773900499999998,
            "cvar5_improvement": 0.013440943041848669,
            "drawdown_improvement": 0.0671010357600475,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.36524264853828964,
            "sortino_excess": -0.5297874406367175,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001557562175,
            "cvar5_improvement": 0.015592623635474825,
            "drawdown_improvement": 0.07845491818304376,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2150546174467733,
            "sortino_excess": -0.30026207796664933,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001793329925,
            "cvar5_improvement": 0.014265950360681257,
            "drawdown_improvement": 0.07231023492123803,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.030837466280157266,
            "sortino_excess": -0.04592289847277273,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017317248749999998,
            "cvar5_improvement": 0.015758734555732238,
            "drawdown_improvement": 0.07964593205933801,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.20174616074202556,
            "sortino_excess": -0.3267461669634516,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00272021655,
            "cvar5_improvement": 0.01979193733011796,
            "drawdown_improvement": 0.10329497133875185,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2773278471058007,
            "sortino_excess": 0.2908805215031971,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0016260286250000002,
            "cvar5_improvement": 0.017292835068718544,
            "drawdown_improvement": 0.0866170129906702,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.29269706539180074,
            "sortino_excess": -0.43192176066141347,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002643261675,
            "cvar5_improvement": 0.012955261355565698,
            "drawdown_improvement": 0.06638296773311339,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.014750459851748499,
            "sortino_excess": -0.06557490568410432,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00142229965,
            "cvar5_improvement": 0.0174019785724215,
            "drawdown_improvement": 0.0889140481311958,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2565892976687609,
            "sortino_excess": -0.4041599423972817,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022279042,
            "cvar5_improvement": 0.012486532321768199,
            "drawdown_improvement": 0.06497251188697084,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2052292317317564,
            "sortino_excess": -0.34584901058690753,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00151783025,
            "cvar5_improvement": 0.015527694046928896,
            "drawdown_improvement": 0.07804618751065714,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.20632550279509104,
            "sortino_excess": -0.30273608444963074,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0021159628750000003,
            "cvar5_improvement": 0.011545468948627314,
            "drawdown_improvement": 0.05701204437705412,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3607691489746363,
            "sortino_excess": -0.5231247809186602,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0023345548,
            "cvar5_improvement": 0.014716770699729532,
            "drawdown_improvement": 0.07465406165213292,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1347734132949646,
            "sortino_excess": -0.2704123148105635,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0035007907750000005,
            "cvar5_improvement": 0.014122127136569781,
            "drawdown_improvement": 0.07521499226705924,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.29578330499312144,
            "sortino_excess": 0.37357803937031225,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00160379115,
            "cvar5_improvement": 0.017993432866244732,
            "drawdown_improvement": 0.09384355126884325,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.24852888046134713,
            "sortino_excess": 0.14887789865006318,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020756856,
            "cvar5_improvement": 0.012582411956889281,
            "drawdown_improvement": 0.06395966476525167,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.09547669559689553,
            "sortino_excess": -0.12566452532351993,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003520428025,
            "cvar5_improvement": 0.016530763081691362,
            "drawdown_improvement": 0.08736204410752016,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13196317340217928,
            "sortino_excess": -0.015060815492355564,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017814721,
            "cvar5_improvement": 0.013384700578637474,
            "drawdown_improvement": 0.06655284391471009,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3300393734349693,
            "sortino_excess": -0.4764565810725323,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00316007195,
            "cvar5_improvement": 0.018412340584511366,
            "drawdown_improvement": 0.0981474616860224,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.655504605640822,
            "sortino_excess": 1.395673767378914,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0027534136,
            "cvar5_improvement": 0.013868599979204472,
            "drawdown_improvement": 0.07334534502269544,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.10430275061066503,
            "sortino_excess": 0.03758438771580713,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011013181750000002,
            "cvar5_improvement": 0.019572584159448694,
            "drawdown_improvement": 0.10075633460484615,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3825347258577985,
            "sortino_excess": 0.5914072431792489,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00148487975,
            "cvar5_improvement": 0.019972576880475774,
            "drawdown_improvement": 0.10213344685730127,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16740654146591202,
            "sortino_excess": 0.1517781180123827,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002680408,
            "cvar5_improvement": 0.019859292477491623,
            "drawdown_improvement": 0.10436877352689775,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.6195860325451937,
            "sortino_excess": 1.3312338445417258,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013948487499999998,
            "cvar5_improvement": 0.017116601079553952,
            "drawdown_improvement": 0.0863571725320397,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.35105237731566796,
            "sortino_excess": -0.5131550522010745,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00177594965,
            "cvar5_improvement": 0.016103021927634874,
            "drawdown_improvement": 0.08243349538972894,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.059436168207516876,
            "sortino_excess": -0.14347348536096202,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002071901475,
            "cvar5_improvement": 0.011946099364378232,
            "drawdown_improvement": 0.05955798863852382,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.27107419068577676,
            "sortino_excess": -0.38651343057868137,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0014128386499999998,
            "cvar5_improvement": 0.019122093199327023,
            "drawdown_improvement": 0.09636878254975956,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.25565832402003397,
            "sortino_excess": -0.3847410688260782,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00174808525,
            "cvar5_improvement": 0.01789729384100508,
            "drawdown_improvement": 0.09151278107172833,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.0648262548311038,
            "sortino_excess": 0.06234940054250318,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00199473395,
            "cvar5_improvement": 0.01393859636308925,
            "drawdown_improvement": 0.0700844764213999,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23608331932462015,
            "sortino_excess": -0.37163741408170325,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011084990249999999,
            "cvar5_improvement": 0.019472543530338088,
            "drawdown_improvement": 0.10036766488237511,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13058983509087213,
            "sortino_excess": 0.20930538761545434,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0022713662,
            "cvar5_improvement": 0.01211134925137391,
            "drawdown_improvement": 0.060551368632855374,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.260673969995303,
            "sortino_excess": -0.403876898125179,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027862359249999995,
            "cvar5_improvement": 0.01693112791570696,
            "drawdown_improvement": 0.08891915641840911,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2943153061686799,
            "sortino_excess": 0.3639809798965705,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002109753575,
            "cvar5_improvement": 0.013613382310760785,
            "drawdown_improvement": 0.06736778252287376,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3277720603389751,
            "sortino_excess": -0.4789053945987849,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00336412995,
            "cvar5_improvement": 0.01703998848441944,
            "drawdown_improvement": 0.09073687945883044,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3381800832100492,
            "sortino_excess": 0.82997308099045,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002110710425,
            "cvar5_improvement": 0.012258693956775294,
            "drawdown_improvement": 0.06149386761934658,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.18320778196156307,
            "sortino_excess": -0.25659724401634254,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001872772625,
            "cvar5_improvement": 0.013970865998314255,
            "drawdown_improvement": 0.07031958674841712,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2178998789176686,
            "sortino_excess": -0.34756524659430277,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001609239275,
            "cvar5_improvement": 0.01580135693546584,
            "drawdown_improvement": 0.07994320687609366,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.18124654643506066,
            "sortino_excess": -0.303521432944978,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002073297575,
            "cvar5_improvement": 0.011584835276423311,
            "drawdown_improvement": 0.05735099676706559,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3451565617311946,
            "sortino_excess": -0.4930365207172648,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016666849,
            "cvar5_improvement": 0.01584061724039159,
            "drawdown_improvement": 0.08160254435340977,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2057179904416922,
            "sortino_excess": -0.3463567722926919,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001781807425,
            "cvar5_improvement": 0.013696569728987982,
            "drawdown_improvement": 0.06848852891573964,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23657870349436355,
            "sortino_excess": -0.34719711838927314,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001804985125,
            "cvar5_improvement": 0.014360785299585,
            "drawdown_improvement": 0.07348346527967181,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.06270385670615775,
            "sortino_excess": -0.07976196932783478,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015362388,
            "cvar5_improvement": 0.015915175948657923,
            "drawdown_improvement": 0.08088597782568072,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.0952515240794718,
            "sortino_excess": -0.12106615700830473,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013690559749999999,
            "cvar5_improvement": 0.017868271685439842,
            "drawdown_improvement": 0.09246545748641657,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.14404141950508448,
            "sortino_excess": 0.2236894093569263,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0024885981250000002,
            "cvar5_improvement": 0.0184488186174812,
            "drawdown_improvement": 0.0975220419292663,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.42683092279042617,
            "sortino_excess": 0.546244684568418,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001792218675,
            "cvar5_improvement": 0.013428826738257547,
            "drawdown_improvement": 0.06686128220038368,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.33769936529266764,
            "sortino_excess": -0.48108882124349484,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002312029275,
            "cvar5_improvement": 0.012488591377721767,
            "drawdown_improvement": 0.06326674694049514,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.16679096018528408,
            "sortino_excess": -0.28343548891797243,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015239177499999999,
            "cvar5_improvement": 0.01581528162605896,
            "drawdown_improvement": 0.0799762095933764,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08373331929675476,
            "sortino_excess": -0.1236419282059287,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019296030000000002,
            "cvar5_improvement": 0.014034786726617685,
            "drawdown_improvement": 0.07217658560650436,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23880750817398805,
            "sortino_excess": -0.3829135760314061,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0037826228000000005,
            "cvar5_improvement": 0.01488302322679813,
            "drawdown_improvement": 0.07859772955605457,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.016413630150506772,
            "sortino_excess": -0.14486981077934788,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003991720775,
            "cvar5_improvement": 0.015244404931434984,
            "drawdown_improvement": 0.08240568968807785,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.23740423138638256,
            "sortino_excess": 0.12783032354820836,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001236808075,
            "cvar5_improvement": 0.019380378717097198,
            "drawdown_improvement": 0.10036721448161806,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.041857132081910026,
            "sortino_excess": -0.1569041441087285,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001841174475,
            "cvar5_improvement": 0.015448797464432798,
            "drawdown_improvement": 0.0769297422975018,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.31498870201192825,
            "sortino_excess": -0.4624904045265723,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001820895,
            "cvar5_improvement": 0.016340039545660857,
            "drawdown_improvement": 0.08499612112295904,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.09994015498532521,
            "sortino_excess": 0.04098527734953786,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019009796000000001,
            "cvar5_improvement": 0.013749544928068597,
            "drawdown_improvement": 0.06964787385937543,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.30463485030112014,
            "sortino_excess": -0.45868775791966726,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011304354499999999,
            "cvar5_improvement": 0.019245404580247014,
            "drawdown_improvement": 0.09789518700540298,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08499899369009911,
            "sortino_excess": -0.10112600395357302,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0021491456,
            "cvar5_improvement": 0.01213762714367449,
            "drawdown_improvement": 0.060790770740233285,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.24297496046722064,
            "sortino_excess": -0.37845677597830385,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00325048885,
            "cvar5_improvement": 0.015529227206513892,
            "drawdown_improvement": 0.08337089086252822,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4291015947422928,
            "sortino_excess": 0.5089106975280605,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00147917435,
            "cvar5_improvement": 0.017777939613146335,
            "drawdown_improvement": 0.09279564814357824,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.03131101554892199,
            "sortino_excess": -0.14466003267816982,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00314493785,
            "cvar5_improvement": 0.01608427581249164,
            "drawdown_improvement": 0.08208429576662624,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22036086411211186,
            "sortino_excess": -0.40060090985852004,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001559376375,
            "cvar5_improvement": 0.01786187692091605,
            "drawdown_improvement": 0.09205825356186967,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.0435139388825809,
            "sortino_excess": -0.020867105562645843,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001310552775,
            "cvar5_improvement": 0.01712409756352144,
            "drawdown_improvement": 0.08611611978997213,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.31161987948701664,
            "sortino_excess": -0.44040563696489343,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010978689,
            "cvar5_improvement": 0.018966393528267126,
            "drawdown_improvement": 0.09586955360021543,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2734856351615733,
            "sortino_excess": -0.38073415710362424,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011954479,
            "cvar5_improvement": 0.019436162721658705,
            "drawdown_improvement": 0.09948910546480796,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.010655628257322886,
            "sortino_excess": -0.10250438442311327,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001141505175,
            "cvar5_improvement": 0.019377850960540444,
            "drawdown_improvement": 0.09974675424624424,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.03337265447559379,
            "sortino_excess": -0.033774675598454235,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0031639920999999996,
            "cvar5_improvement": 0.018174064291463832,
            "drawdown_improvement": 0.09561299322347447,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.18943900011222503,
            "sortino_excess": 0.07248049053013489,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001450562375,
            "cvar5_improvement": 0.017621414421520796,
            "drawdown_improvement": 0.09116717399281477,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.14869192491725094,
            "sortino_excess": -0.280905528632168,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00179258695,
            "cvar5_improvement": 0.013427835132228023,
            "drawdown_improvement": 0.06685222680434041,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.33329334286301937,
            "sortino_excess": -0.4742945702417736,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001316296275,
            "cvar5_improvement": 0.017455900301378866,
            "drawdown_improvement": 0.08834054638061994,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1662713675013866,
            "sortino_excess": -0.22328905873132954,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018950251250000002,
            "cvar5_improvement": 0.01420315538097561,
            "drawdown_improvement": 0.07223273684876363,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.14375181224775896,
            "sortino_excess": -0.25871898370119273,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012983848000000001,
            "cvar5_improvement": 0.017080866092712674,
            "drawdown_improvement": 0.08580468003969427,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2995533602852867,
            "sortino_excess": -0.4324337437538577,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0036830273249999997,
            "cvar5_improvement": 0.012434638920005165,
            "drawdown_improvement": 0.06317401500551481,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2782624016048771,
            "sortino_excess": -0.4582612823061587,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.002073595025,
            "cvar5_improvement": 0.016459364510638473,
            "drawdown_improvement": 0.08415198165756482,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.07269842583567465,
            "sortino_excess": -0.19804147431557492,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001954174075,
            "cvar5_improvement": 0.01353429318711446,
            "drawdown_improvement": 0.0673012757488532,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3361888469970017,
            "sortino_excess": -0.49661140429178224,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015246901,
            "cvar5_improvement": 0.015268696696584186,
            "drawdown_improvement": 0.07641197600384877,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3235409880939694,
            "sortino_excess": -0.45921110868467896,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001303929025,
            "cvar5_improvement": 0.01737107546832908,
            "drawdown_improvement": 0.08772043929990808,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.15694101958229545,
            "sortino_excess": -0.22941269607049533,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001182111925,
            "cvar5_improvement": 0.018949211497305354,
            "drawdown_improvement": 0.09609762893905693,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3323431726849311,
            "sortino_excess": -0.4923028044836281,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002233303725,
            "cvar5_improvement": 0.0139371450248751,
            "drawdown_improvement": 0.06951026668661575,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2940801969081147,
            "sortino_excess": -0.452007753124397,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018345778250000002,
            "cvar5_improvement": 0.013389846637311085,
            "drawdown_improvement": 0.06653729682824033,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.35578627556327014,
            "sortino_excess": -0.5162573962854178,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0021293741499999997,
            "cvar5_improvement": 0.01685181226752784,
            "drawdown_improvement": 0.08794215146777987,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.12364570913083063,
            "sortino_excess": 0.06879891467140553,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020632017,
            "cvar5_improvement": 0.012158404474831398,
            "drawdown_improvement": 0.060896996177853435,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1737639488566486,
            "sortino_excess": -0.2590885509684602,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00244043685,
            "cvar5_improvement": 0.0151981503175323,
            "drawdown_improvement": 0.07928821570338798,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.04875162946967919,
            "sortino_excess": -0.04742365595495712,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0029273942750000005,
            "cvar5_improvement": 0.01787748595938721,
            "drawdown_improvement": 0.09166508075016536,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1626686476578732,
            "sortino_excess": -0.34144931358459407,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013217709,
            "cvar5_improvement": 0.01770105664755101,
            "drawdown_improvement": 0.09057808900445777,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.014984043197148411,
            "sortino_excess": 0.0008644079099831836,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011029374749999999,
            "cvar5_improvement": 0.01926016449300341,
            "drawdown_improvement": 0.09810640719514935,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.10001224631946237,
            "sortino_excess": -0.12828589253671915,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00108563665,
            "cvar5_improvement": 0.018917500536180756,
            "drawdown_improvement": 0.09551962803427619,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.26807005546973456,
            "sortino_excess": -0.38723336512908185,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0021942567,
            "cvar5_improvement": 0.014099409037564393,
            "drawdown_improvement": 0.07025328904239625,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.21528245163046683,
            "sortino_excess": -0.3346125803604385,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027061097,
            "cvar5_improvement": 0.01691842943648588,
            "drawdown_improvement": 0.08851367890914855,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.19235090477131278,
            "sortino_excess": 0.26210747786841754,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018485509000000001,
            "cvar5_improvement": 0.014343115338485434,
            "drawdown_improvement": 0.0731497204746194,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.04628875408261207,
            "sortino_excess": -0.05121486328470251,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010994839,
            "cvar5_improvement": 0.019600604512381888,
            "drawdown_improvement": 0.10061832336671964,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16393654711437416,
            "sortino_excess": 0.26154244395584436,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013560947000000002,
            "cvar5_improvement": 0.017685300767922452,
            "drawdown_improvement": 0.090306075481221,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.017960821604411814,
            "sortino_excess": -0.004706857204724163,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011578,
            "cvar5_improvement": 0.019184105093406692,
            "drawdown_improvement": 0.09747398058791859,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1766435142808354,
            "sortino_excess": -0.2993300601973379,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001800491275,
            "cvar5_improvement": 0.018488931750155115,
            "drawdown_improvement": 0.09533800950081445,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.1663348332005804,
            "sortino_excess": 0.19961095863939068,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0023710502500000003,
            "cvar5_improvement": 0.014671327988841427,
            "drawdown_improvement": 0.07595497014612132,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.06322194335727327,
            "sortino_excess": 0.047185641858093014,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011083695,
            "cvar5_improvement": 0.019471545755506636,
            "drawdown_improvement": 0.10036285495110503,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.10375144699167665,
            "sortino_excess": 0.16117819317309076,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00156539205,
            "cvar5_improvement": 0.01523024638378086,
            "drawdown_improvement": 0.07608476675327164,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3487831525394479,
            "sortino_excess": -0.5069606801864593,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026938492000000004,
            "cvar5_improvement": 0.016621988116815152,
            "drawdown_improvement": 0.0869709206104104,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.08276672264606001,
            "sortino_excess": 0.02842072315761507,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016317191,
            "cvar5_improvement": 0.015970629116211714,
            "drawdown_improvement": 0.08184366502952406,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08798716866676165,
            "sortino_excess": -0.19120924924836855,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002158125775,
            "cvar5_improvement": 0.011608225918771656,
            "drawdown_improvement": 0.057618683210980265,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.36818483697704874,
            "sortino_excess": -0.5335743139834822,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0010907686,
            "cvar5_improvement": 0.01920451140947021,
            "drawdown_improvement": 0.09747231290211084,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.06986269653742216,
            "sortino_excess": -0.0988586840168825,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002556620225,
            "cvar5_improvement": 0.012708123839895408,
            "drawdown_improvement": 0.06358915938936988,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1352698035037055,
            "sortino_excess": -0.2300369119720195,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012220870500000002,
            "cvar5_improvement": 0.01943721964256814,
            "drawdown_improvement": 0.09950454218168886,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.13934987555336456,
            "sortino_excess": -0.28348747668708185,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017993417500000001,
            "cvar5_improvement": 0.01411283463480773,
            "drawdown_improvement": 0.07127519924383477,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.14665898675360478,
            "sortino_excess": -0.19918982372853236,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015356089,
            "cvar5_improvement": 0.015917774001544763,
            "drawdown_improvement": 0.08090959634866807,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.11041059231417683,
            "sortino_excess": -0.14739171301724266,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020643047999999997,
            "cvar5_improvement": 0.01244641489952518,
            "drawdown_improvement": 0.06279591591428152,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08469945322381084,
            "sortino_excess": -0.12868479581403477,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015415157999999999,
            "cvar5_improvement": 0.01614606494632253,
            "drawdown_improvement": 0.08313167873615138,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.011129696861105709,
            "sortino_excess": 0.029360010909828455,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002152785525,
            "cvar5_improvement": 0.01984564438172303,
            "drawdown_improvement": 0.10307904109878277,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.3567211543148398,
            "sortino_excess": 0.41528608722185706,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013267705499999999,
            "cvar5_improvement": 0.017905648958531403,
            "drawdown_improvement": 0.09281750434395347,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.11987578816068595,
            "sortino_excess": 0.18109094698285208,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00153058965,
            "cvar5_improvement": 0.015610520894404109,
            "drawdown_improvement": 0.07864604949537324,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.21403283719459804,
            "sortino_excess": -0.2981069364841232,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001209137125,
            "cvar5_improvement": 0.019212943109712402,
            "drawdown_improvement": 0.09856354260577846,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1985576285619274,
            "sortino_excess": -0.33917527648220713,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00424199355,
            "cvar5_improvement": 0.01431708930882156,
            "drawdown_improvement": 0.07702380975921785,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.2559612752895891,
            "sortino_excess": 0.22508966155230414,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002016385575,
            "cvar5_improvement": 0.016187084247814662,
            "drawdown_improvement": 0.08275136598963106,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.009375435102186302,
            "sortino_excess": -0.0552772416822013,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001302373025,
            "cvar5_improvement": 0.019380865576452536,
            "drawdown_improvement": 0.09916199570580872,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.03869690036159221,
            "sortino_excess": -0.11814582979350338,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013162101000000002,
            "cvar5_improvement": 0.017454961109362566,
            "drawdown_improvement": 0.08833503986448002,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17898951080016012,
            "sortino_excess": -0.2453716025050911,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00130947325,
            "cvar5_improvement": 0.01764294564730018,
            "drawdown_improvement": 0.08963346021019053,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.001981997079243125,
            "sortino_excess": 0.002680297644137547,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015243981,
            "cvar5_improvement": 0.015271223994216607,
            "drawdown_improvement": 0.07642710886423135,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3274736482818421,
            "sortino_excess": -0.4650309733526662,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013302208250000002,
            "cvar5_improvement": 0.01710995520446584,
            "drawdown_improvement": 0.08600855732049487,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.30634404315434516,
            "sortino_excess": -0.4320219632447807,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002047322825,
            "cvar5_improvement": 0.01638237139488972,
            "drawdown_improvement": 0.08430174591429443,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.13027250404451957,
            "sortino_excess": 0.15511329072508326,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001515749825,
            "cvar5_improvement": 0.01758985376864293,
            "drawdown_improvement": 0.0893450017970231,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.14553840584111727,
            "sortino_excess": -0.25374416994444327,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001637699375,
            "cvar5_improvement": 0.015575892209970334,
            "drawdown_improvement": 0.07924952591459203,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2850302561737134,
            "sortino_excess": -0.43611660863128177,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018808616749999999,
            "cvar5_improvement": 0.01868494155152684,
            "drawdown_improvement": 0.09802433680015904,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4715036088313361,
            "sortino_excess": 0.5743971527202042,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00210495655,
            "cvar5_improvement": 0.019882115896731518,
            "drawdown_improvement": 0.10388841857641556,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.4050401724593095,
            "sortino_excess": 0.5111269545367373,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002374921425,
            "cvar5_improvement": 0.019393349811084985,
            "drawdown_improvement": 0.10205054386290688,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.03625391301627556,
            "sortino_excess": 0.07421588252026257,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001117708475,
            "cvar5_improvement": 0.018952182112737966,
            "drawdown_improvement": 0.09575055430967702,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.27493678811463906,
            "sortino_excess": -0.38303691571750975,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0019585053249999997,
            "cvar5_improvement": 0.01425694334407194,
            "drawdown_improvement": 0.07435110733769756,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.16965434186370246,
            "sortino_excess": -0.30492661782104713,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00157034825,
            "cvar5_improvement": 0.015898001356799016,
            "drawdown_improvement": 0.08062256137892335,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.09705936118958253,
            "sortino_excess": -0.1247440864160618,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002132634975,
            "cvar5_improvement": 0.011853322239399128,
            "drawdown_improvement": 0.058893309270158706,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3030712281733742,
            "sortino_excess": -0.451453823484927,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001583305075,
            "cvar5_improvement": 0.01612561418506691,
            "drawdown_improvement": 0.0827799790603265,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.028214275709369685,
            "sortino_excess": 0.05889589237420048,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017551860499999997,
            "cvar5_improvement": 0.017607991645177436,
            "drawdown_improvement": 0.08878402307863331,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23808134079063611,
            "sortino_excess": -0.3895590960689974,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001969552975,
            "cvar5_improvement": 0.015771069629739,
            "drawdown_improvement": 0.07909513939425913,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.27277397025846095,
            "sortino_excess": -0.428472410437182,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002120883925,
            "cvar5_improvement": 0.012562695430020827,
            "drawdown_improvement": 0.06364043407370393,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.09669012427418755,
            "sortino_excess": -0.1286260459919478,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015120052,
            "cvar5_improvement": 0.015229414653885068,
            "drawdown_improvement": 0.07613963417504008,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.31813839486563056,
            "sortino_excess": -0.45920609006436264,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020394158,
            "cvar5_improvement": 0.014311819416363784,
            "drawdown_improvement": 0.07282874791424698,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.12275658474951634,
            "sortino_excess": -0.22512767234094336,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020724466999999997,
            "cvar5_improvement": 0.011944702466062754,
            "drawdown_improvement": 0.0595461503880029,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.26415887179445574,
            "sortino_excess": -0.3754271310773434,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011428228249999999,
            "cvar5_improvement": 0.019444704746360463,
            "drawdown_improvement": 0.10009519265448624,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.12551835025807223,
            "sortino_excess": 0.20027604910028476,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00248852,
            "cvar5_improvement": 0.01551437016231949,
            "drawdown_improvement": 0.08277185622915315,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.21297067658953,
            "sortino_excess": 0.20562689630965822,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013456406000000001,
            "cvar5_improvement": 0.01956956135557742,
            "drawdown_improvement": 0.09995064837791268,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.10620608815275542,
            "sortino_excess": -0.11528343438683011,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0023538309500000004,
            "cvar5_improvement": 0.012838941878883976,
            "drawdown_improvement": 0.06603714910948982,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.06290744521781133,
            "sortino_excess": -0.1489064814715286,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.003408175075,
            "cvar5_improvement": 0.014264395843813822,
            "drawdown_improvement": 0.07268013284094782,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2563156100488072,
            "sortino_excess": -0.4368768062065439,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017989432249999999,
            "cvar5_improvement": 0.014113536516658656,
            "drawdown_improvement": 0.07128072270326952,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1599542311351752,
            "sortino_excess": -0.22249552521201685,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00149768825,
            "cvar5_improvement": 0.01941959534584187,
            "drawdown_improvement": 0.0993037592663121,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.014252239220247764,
            "sortino_excess": -0.017377497296843708,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0018131268,
            "cvar5_improvement": 0.01342269180861807,
            "drawdown_improvement": 0.06674921556964566,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3338136850606583,
            "sortino_excess": -0.4751086404047991,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002282614375,
            "cvar5_improvement": 0.014467155418726577,
            "drawdown_improvement": 0.07306753501576227,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08647292732058937,
            "sortino_excess": -0.16306961050157234,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001530230875,
            "cvar5_improvement": 0.015613497758595427,
            "drawdown_improvement": 0.07865829299572485,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2228121632489451,
            "sortino_excess": -0.31254184921394695,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0017109604250000001,
            "cvar5_improvement": 0.017696971485278146,
            "drawdown_improvement": 0.08948853589314754,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.10952051563315746,
            "sortino_excess": -0.19104853134505298,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0026080395500000003,
            "cvar5_improvement": 0.012916913480315123,
            "drawdown_improvement": 0.0650802890638357,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.1769139900225176,
            "sortino_excess": -0.31929677508520604,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0015334639000000002,
            "cvar5_improvement": 0.01955640097718251,
            "drawdown_improvement": 0.10084923624707487,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.28335692267452817,
            "sortino_excess": 0.3080309131468826,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002073340925,
            "cvar5_improvement": 0.011585738652266642,
            "drawdown_improvement": 0.05735635101836689,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3416292986488686,
            "sortino_excess": -0.4877605221206569,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002471892425,
            "cvar5_improvement": 0.0122789019926699,
            "drawdown_improvement": 0.06073404089537626,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2418807434160043,
            "sortino_excess": -0.36987268482889835,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002048386875,
            "cvar5_improvement": 0.019557667707104466,
            "drawdown_improvement": 0.10040783360874447,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.07142974559365065,
            "sortino_excess": -0.17797804372968612,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001314814225,
            "cvar5_improvement": 0.01786493566978399,
            "drawdown_improvement": 0.09159746939730146,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16823645949578164,
            "sortino_excess": 0.2664002612305133,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0012598708250000001,
            "cvar5_improvement": 0.019041554910674736,
            "drawdown_improvement": 0.09629547431647811,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.2720333908788399,
            "sortino_excess": -0.41656096376141144,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0011032485750000001,
            "cvar5_improvement": 0.0192602547820561,
            "drawdown_improvement": 0.09809513207225357,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.08225607208910218,
            "sortino_excess": -0.09612023258124722,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016874107750000002,
            "cvar5_improvement": 0.01537257791769291,
            "drawdown_improvement": 0.07687981916716707,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.32400520471212624,
            "sortino_excess": -0.48129952961839695,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002094147075,
            "cvar5_improvement": 0.011586543356799562,
            "drawdown_improvement": 0.05726461321033094,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3418628708818512,
            "sortino_excess": -0.4883344285979998,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0020750241,
            "cvar5_improvement": 0.0125838501388892,
            "drawdown_improvement": 0.0639489475457177,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.11071690374620569,
            "sortino_excess": -0.15197213871104412,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001601772775,
            "cvar5_improvement": 0.019844187668145722,
            "drawdown_improvement": 0.10280342018030392,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.16679547695812186,
            "sortino_excess": 0.1410858591917675,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001137761425,
            "cvar5_improvement": 0.018920319416369222,
            "drawdown_improvement": 0.0955250582690744,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.31856074020393454,
            "sortino_excess": -0.4703674795893664,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0027137694999999997,
            "cvar5_improvement": 0.019526026784719472,
            "drawdown_improvement": 0.10057102206148547,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.05638856772718932,
            "sortino_excess": -0.22907171348364372,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001541591225,
            "cvar5_improvement": 0.019434866260304436,
            "drawdown_improvement": 0.09858394593745931,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17551605628842948,
            "sortino_excess": -0.32129340552992824,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00109965355,
            "cvar5_improvement": 0.019603181401256504,
            "drawdown_improvement": 0.10064137386709168,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": 0.20060353838867323,
            "sortino_excess": 0.3242891610624101,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.002165753925,
            "cvar5_improvement": 0.012422156189144787,
            "drawdown_improvement": 0.0627073667600132,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.17940936309789918,
            "sortino_excess": -0.3016601448723242,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.0013105956,
            "cvar5_improvement": 0.01712460659776587,
            "drawdown_improvement": 0.0861191962326476,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.30557407608005727,
            "sortino_excess": -0.43064655448004885,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00137119195,
            "cvar5_improvement": 0.01736227569496341,
            "drawdown_improvement": 0.08769206702976082,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.23520292174208543,
            "sortino_excess": -0.3682400983235059,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.001350596725,
            "cvar5_improvement": 0.017080752402165732,
            "drawdown_improvement": 0.08577252922958242,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3384502169633109,
            "sortino_excess": -0.4941197015281609,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024782089000000003,
            "cvar5_improvement": 0.01596039962789384,
            "drawdown_improvement": 0.08131873789817848,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.22277434953720665,
            "sortino_excess": -0.3665446276991404,
            "stable": false
          },
          {
            "config": {
              "cost": {
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
            "cost_drag": 0.00206266335,
            "cvar5_improvement": 0.011543506038348281,
            "drawdown_improvement": 0.05705460206085844,
            "exposure_ratio": 0.7123015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct",
              "fixed_initial_pct"
            ],
            "sharpe_excess": -0.3382293119532032,
            "sortino_excess": -0.4886295587073426,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010270375,
            "cvar5_improvement": 0.023962121187088486,
            "drawdown_improvement": 0.12238727930606522,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000104016325,
            "cvar5_improvement": 0.023957196277583033,
            "drawdown_improvement": 0.12235868728253682,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022882895,
            "cvar5_improvement": 0.023252711234900893,
            "drawdown_improvement": 0.11853029167479606,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00015050455,
            "cvar5_improvement": 0.023698157285797536,
            "drawdown_improvement": 0.12093919672626793,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022882895,
            "cvar5_improvement": 0.023252711234900893,
            "drawdown_improvement": 0.11853029167479606,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00014359,
            "cvar5_improvement": 0.02372400594988429,
            "drawdown_improvement": 0.1210886528614577,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001462141,
            "cvar5_improvement": 0.023714314216290115,
            "drawdown_improvement": 0.12103264777071243,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010270375,
            "cvar5_improvement": 0.023962121187088486,
            "drawdown_improvement": 0.12238727930606522,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001907564,
            "cvar5_improvement": 0.02346688723055918,
            "drawdown_improvement": 0.1196844321081639,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022882895,
            "cvar5_improvement": 0.023252711234900893,
            "drawdown_improvement": 0.11853029167479606,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000104016325,
            "cvar5_improvement": 0.023957196277583033,
            "drawdown_improvement": 0.12235868728253682,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000104016325,
            "cvar5_improvement": 0.023957196277583033,
            "drawdown_improvement": 0.12235868728253682,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022882895,
            "cvar5_improvement": 0.023252711234900893,
            "drawdown_improvement": 0.11853029167479606,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001462141,
            "cvar5_improvement": 0.023714314216290115,
            "drawdown_improvement": 0.12103264777071243,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022882895,
            "cvar5_improvement": 0.023252711234900893,
            "drawdown_improvement": 0.11853029167479606,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00015050455,
            "cvar5_improvement": 0.023698157285797536,
            "drawdown_improvement": 0.12093919672626793,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010270375,
            "cvar5_improvement": 0.023962121187088486,
            "drawdown_improvement": 0.12238727930606522,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018452819999999998,
            "cvar5_improvement": 0.02348690589839113,
            "drawdown_improvement": 0.1198005470099204,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010805695,
            "cvar5_improvement": 0.02394211442523277,
            "drawdown_improvement": 0.122271094209991,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001907564,
            "cvar5_improvement": 0.02346688723055918,
            "drawdown_improvement": 0.1196844321081639,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001462141,
            "cvar5_improvement": 0.023714314216290115,
            "drawdown_improvement": 0.12103264777071243,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00014359,
            "cvar5_improvement": 0.02372400594988429,
            "drawdown_improvement": 0.1210886528614577,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018911435,
            "cvar5_improvement": 0.02347259816881227,
            "drawdown_improvement": 0.1197176128741341,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010805695,
            "cvar5_improvement": 0.02394211442523277,
            "drawdown_improvement": 0.122271094209991,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001907564,
            "cvar5_improvement": 0.02346688723055918,
            "drawdown_improvement": 0.1196844321081639,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001462141,
            "cvar5_improvement": 0.023714314216290115,
            "drawdown_improvement": 0.12103264777071243,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018911435,
            "cvar5_improvement": 0.02347259816881227,
            "drawdown_improvement": 0.1197176128741341,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001462141,
            "cvar5_improvement": 0.023714314216290115,
            "drawdown_improvement": 0.12103264777071243,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001462141,
            "cvar5_improvement": 0.023714314216290115,
            "drawdown_improvement": 0.12103264777071243,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00015050455,
            "cvar5_improvement": 0.023698157285797536,
            "drawdown_improvement": 0.12093919672626793,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010805695,
            "cvar5_improvement": 0.02394211442523277,
            "drawdown_improvement": 0.122271094209991,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022882895,
            "cvar5_improvement": 0.023252711234900893,
            "drawdown_improvement": 0.11853029167479606,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00015050455,
            "cvar5_improvement": 0.023698157285797536,
            "drawdown_improvement": 0.12093919672626793,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00015050455,
            "cvar5_improvement": 0.023698157285797536,
            "drawdown_improvement": 0.12093919672626793,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000104016325,
            "cvar5_improvement": 0.023957196277583033,
            "drawdown_improvement": 0.12235868728253682,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000104016325,
            "cvar5_improvement": 0.023957196277583033,
            "drawdown_improvement": 0.12235868728253682,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00014359,
            "cvar5_improvement": 0.02372400594988429,
            "drawdown_improvement": 0.1210886528614577,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00015050455,
            "cvar5_improvement": 0.023698157285797536,
            "drawdown_improvement": 0.12093919672626793,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018911435,
            "cvar5_improvement": 0.02347259816881227,
            "drawdown_improvement": 0.1197176128741341,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018911435,
            "cvar5_improvement": 0.02347259816881227,
            "drawdown_improvement": 0.1197176128741341,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 8.5282e-05,
            "cvar5_improvement": 0.02370169905356856,
            "drawdown_improvement": 0.12072005444832365,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010805695,
            "cvar5_improvement": 0.02394211442523277,
            "drawdown_improvement": 0.122271094209991,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010805695,
            "cvar5_improvement": 0.02394211442523277,
            "drawdown_improvement": 0.122271094209991,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001907564,
            "cvar5_improvement": 0.02346688723055918,
            "drawdown_improvement": 0.1196844321081639,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018911435,
            "cvar5_improvement": 0.02347259816881227,
            "drawdown_improvement": 0.1197176128741341,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018452819999999998,
            "cvar5_improvement": 0.02348690589839113,
            "drawdown_improvement": 0.1198005470099204,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002300377,
            "cvar5_improvement": 0.023372788044015106,
            "drawdown_improvement": 0.11913802844683274,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000134164425,
            "cvar5_improvement": 0.02388550069208683,
            "drawdown_improvement": 0.12194155436106846,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.000104016325,
            "cvar5_improvement": 0.023957196277583033,
            "drawdown_improvement": 0.12235868728253682,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018434265,
            "cvar5_improvement": 0.023612926034747978,
            "drawdown_improvement": 0.12044493957629285,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00010805695,
            "cvar5_improvement": 0.02394211442523277,
            "drawdown_improvement": 0.122271094209991,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018452819999999998,
            "cvar5_improvement": 0.02348690589839113,
            "drawdown_improvement": 0.1198005470099204,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 7.01524e-05,
            "cvar5_improvement": 0.02382620139686816,
            "drawdown_improvement": 0.12146372004832368,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00022944140000000002,
            "cvar5_improvement": 0.02324997751953118,
            "drawdown_improvement": 0.11851441447870406,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001907564,
            "cvar5_improvement": 0.02346688723055918,
            "drawdown_improvement": 0.1196844321081639,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0001907564,
            "cvar5_improvement": 0.02346688723055918,
            "drawdown_improvement": 0.1196844321081639,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00018911435,
            "cvar5_improvement": 0.02347259816881227,
            "drawdown_improvement": 0.1197176128741341,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 5.50228e-05,
            "cvar5_improvement": 0.02395054425424326,
            "drawdown_improvement": 0.12220738564832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 3.98932e-05,
            "cvar5_improvement": 0.0240747280694897,
            "drawdown_improvement": 0.12295105124832367,
            "exposure_ratio": 0.003968253968253968,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
            "screened_axes": [
              "risk_per_unit",
              "add_n",
              "max_units",
              "amount_ratio_min"
            ],
            "sharpe_excess": null,
            "sortino_excess": null,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.0002671453,
            "cvar5_improvement": 0.023161453839429247,
            "drawdown_improvement": 0.11800244858343922,
            "exposure_ratio": 0.025793650793650792,
            "family": "trend_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "unavailable_training_metrics:sortino_excess,sharpe_excess",
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
