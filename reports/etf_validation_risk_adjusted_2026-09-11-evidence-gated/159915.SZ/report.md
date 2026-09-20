# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`do_not_trade`
- 建议：不交易，直至补齐并复核缺失或无效证据。
- 阻断项：oos_evidence

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.027696 | 0.074322 | -0.046626 |
| sharpe | 0.364421 | 0.231128 | 0.133293 |
| Sortino | 0.406988 | 0.362905 | 0.044083 |
| calmar | 0.216220 | 0.188462 | 0.027758 |
| cvar5 | -0.010572 | -0.037242 | 0.026670 |
| max_drawdown | -0.128092 | -0.394363 | 0.266271 |
| turnover | 16.078491 | 6.838001 | 9.240490 |
| total_cost | 724.026440 | 239.741560 | 484.284880 |

## OOS 分布

{
  "window_count": 6,
  "win_rate": 0.5,
  "median_excess_return": 0.08631951050294495,
  "best_excess_return": 0.12168371063100902,
  "worst_excess_return": -0.2321081495987789
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 240,
    "cash_sessions": 516,
    "exposure_ratio": 0.31746031746031744,
    "turnover": 16.078491258620762,
    "total_cost": 724.02644,
    "cost_drag": 0.0072402644
  },
  "buy_and_hold": {
    "invested_sessions": 756,
    "cash_sessions": 0,
    "exposure_ratio": 1.0,
    "turnover": 6.838000774779866,
    "total_cost": 239.74156,
    "cost_drag": 0.0023974155999999997
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-10",
  "config_hashes": [
    "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e"
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff22a96b188c46ff2579d35795ae13499b4e07c803d51709c0c77cd0f06cbec4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45be862309c4f4c129b8a2f1c191d5e43b14357d0c05c0e30add1a17830fc677",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5f35123201b6d26bf5d85ad095ecb0cb0bf4c146e0fb0a5fe58cd5005e6324a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f421e580e3a2cf5268f7ac5360cebc998b90c6f371e8f7e0d9e7758df323f6e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0822c7e6a7b7ce4715377e932c2eefe257e6132e8472f63693f0dd515bc5bc9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4fb82db85a6b8847c7476dd4de4939e500232caa43d14bce6062b8704a86a3f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dd1660e126f3641b21a6e2108102a529a0acdac36daa229ddab1555a29652859",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "70ebb8eca36c7ada727cf004aa381f67e40f8299c87e8f8055dea8b3fc3e3b35",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        }
      ]
    },
    {
      "window_id": "wf_001",
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff22a96b188c46ff2579d35795ae13499b4e07c803d51709c0c77cd0f06cbec4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45be862309c4f4c129b8a2f1c191d5e43b14357d0c05c0e30add1a17830fc677",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5f35123201b6d26bf5d85ad095ecb0cb0bf4c146e0fb0a5fe58cd5005e6324a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f421e580e3a2cf5268f7ac5360cebc998b90c6f371e8f7e0d9e7758df323f6e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0822c7e6a7b7ce4715377e932c2eefe257e6132e8472f63693f0dd515bc5bc9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4fb82db85a6b8847c7476dd4de4939e500232caa43d14bce6062b8704a86a3f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dd1660e126f3641b21a6e2108102a529a0acdac36daa229ddab1555a29652859",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "70ebb8eca36c7ada727cf004aa381f67e40f8299c87e8f8055dea8b3fc3e3b35",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        }
      ]
    },
    {
      "window_id": "wf_002",
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff22a96b188c46ff2579d35795ae13499b4e07c803d51709c0c77cd0f06cbec4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45be862309c4f4c129b8a2f1c191d5e43b14357d0c05c0e30add1a17830fc677",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5f35123201b6d26bf5d85ad095ecb0cb0bf4c146e0fb0a5fe58cd5005e6324a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f421e580e3a2cf5268f7ac5360cebc998b90c6f371e8f7e0d9e7758df323f6e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0822c7e6a7b7ce4715377e932c2eefe257e6132e8472f63693f0dd515bc5bc9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4fb82db85a6b8847c7476dd4de4939e500232caa43d14bce6062b8704a86a3f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dd1660e126f3641b21a6e2108102a529a0acdac36daa229ddab1555a29652859",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "70ebb8eca36c7ada727cf004aa381f67e40f8299c87e8f8055dea8b3fc3e3b35",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        }
      ]
    },
    {
      "window_id": "wf_003",
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff22a96b188c46ff2579d35795ae13499b4e07c803d51709c0c77cd0f06cbec4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45be862309c4f4c129b8a2f1c191d5e43b14357d0c05c0e30add1a17830fc677",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5f35123201b6d26bf5d85ad095ecb0cb0bf4c146e0fb0a5fe58cd5005e6324a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f421e580e3a2cf5268f7ac5360cebc998b90c6f371e8f7e0d9e7758df323f6e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0822c7e6a7b7ce4715377e932c2eefe257e6132e8472f63693f0dd515bc5bc9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4fb82db85a6b8847c7476dd4de4939e500232caa43d14bce6062b8704a86a3f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dd1660e126f3641b21a6e2108102a529a0acdac36daa229ddab1555a29652859",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "70ebb8eca36c7ada727cf004aa381f67e40f8299c87e8f8055dea8b3fc3e3b35",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        }
      ]
    },
    {
      "window_id": "wf_004",
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff22a96b188c46ff2579d35795ae13499b4e07c803d51709c0c77cd0f06cbec4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45be862309c4f4c129b8a2f1c191d5e43b14357d0c05c0e30add1a17830fc677",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5f35123201b6d26bf5d85ad095ecb0cb0bf4c146e0fb0a5fe58cd5005e6324a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f421e580e3a2cf5268f7ac5360cebc998b90c6f371e8f7e0d9e7758df323f6e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0822c7e6a7b7ce4715377e932c2eefe257e6132e8472f63693f0dd515bc5bc9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4fb82db85a6b8847c7476dd4de4939e500232caa43d14bce6062b8704a86a3f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dd1660e126f3641b21a6e2108102a529a0acdac36daa229ddab1555a29652859",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "70ebb8eca36c7ada727cf004aa381f67e40f8299c87e8f8055dea8b3fc3e3b35",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        }
      ]
    },
    {
      "window_id": "wf_005",
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ff22a96b188c46ff2579d35795ae13499b4e07c803d51709c0c77cd0f06cbec4",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "45be862309c4f4c129b8a2f1c191d5e43b14357d0c05c0e30add1a17830fc677",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "5f35123201b6d26bf5d85ad095ecb0cb0bf4c146e0fb0a5fe58cd5005e6324a1",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "f421e580e3a2cf5268f7ac5360cebc998b90c6f371e8f7e0d9e7758df323f6e8",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0822c7e6a7b7ce4715377e932c2eefe257e6132e8472f63693f0dd515bc5bc9a",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c4fb82db85a6b8847c7476dd4de4939e500232caa43d14bce6062b8704a86a3f",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
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
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "dd1660e126f3641b21a6e2108102a529a0acdac36daa229ddab1555a29652859",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "70ebb8eca36c7ada727cf004aa381f67e40f8299c87e8f8055dea8b3fc3e3b35",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "0cfcbe081e9b2c5730afa931b5cc48131bf1e93593e74d28136c8d17a5ea3386",
          "positive_windows": [
            true,
            true,
            true,
            true
          ],
          "oos_returns": [
            0.0,
            0.0,
            0.0,
            0.0
          ],
          "positive_window_share": 1.0
        }
      ]
    }
  ],
  "run_manifest": {
    "schema_version": 1,
    "runner": "run_instrument_validation",
    "source_provider": "ValidationMarketDataProvider",
    "data_cutoff": "2026-09-10",
    "requested_start": "2021-01-04",
    "data_fingerprint": "98bdafa6fe46236976edcad28376261edf65400584e6ecd2a5f958075edae34d",
    "target": {
      "exposure_id": "chinext",
      "stock_code": "159915.SZ",
      "sub_layer": "broad_domestic_growth",
      "scope": "formal"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e",
        "config": {
          "grid": {
            "step_pct": 0.035,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.6,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.5,
            "risk_per_unit": 0.005,
            "add_n": 0.75,
            "max_units": 3,
            "require_macd_bullish": true,
            "amount_ratio_min": 1.2
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      },
      {
        "window_id": "wf_001",
        "config_hash": "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e",
        "config": {
          "grid": {
            "step_pct": 0.035,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.6,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.5,
            "risk_per_unit": 0.005,
            "add_n": 0.75,
            "max_units": 3,
            "require_macd_bullish": true,
            "amount_ratio_min": 1.2
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      },
      {
        "window_id": "wf_002",
        "config_hash": "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e",
        "config": {
          "grid": {
            "step_pct": 0.035,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.6,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.5,
            "risk_per_unit": 0.005,
            "add_n": 0.75,
            "max_units": 3,
            "require_macd_bullish": true,
            "amount_ratio_min": 1.2
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      },
      {
        "window_id": "wf_003",
        "config_hash": "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e",
        "config": {
          "grid": {
            "step_pct": 0.035,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.6,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.5,
            "risk_per_unit": 0.005,
            "add_n": 0.75,
            "max_units": 3,
            "require_macd_bullish": true,
            "amount_ratio_min": 1.2
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      },
      {
        "window_id": "wf_004",
        "config_hash": "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e",
        "config": {
          "grid": {
            "step_pct": 0.035,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.6,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.5,
            "risk_per_unit": 0.005,
            "add_n": 0.75,
            "max_units": 3,
            "require_macd_bullish": true,
            "amount_ratio_min": 1.2
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      },
      {
        "window_id": "wf_005",
        "config_hash": "9537534e5869fb3247914cc6bb4996bcb943033038e221f74e4af0e1d929cf7e",
        "config": {
          "grid": {
            "step_pct": 0.035,
            "unit_pct": 0.1,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.6,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.5,
            "risk_per_unit": 0.005,
            "add_n": 0.75,
            "max_units": 3,
            "require_macd_bullish": true,
            "amount_ratio_min": 1.2
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        }
      }
    ],
    "screened_axes": {
      "grid": [
        "step_pct",
        "unit_pct",
        "fixed_initial_pct",
        "atr_stop_multiple",
        "cooldown_sessions"
      ],
      "trend": [
        "risk_per_unit",
        "add_n",
        "max_units",
        "amount_ratio_min",
        "stop_n",
        "require_macd_bullish"
      ]
    }
  }
}

## 事件归因

[
  {
    "window_id": "wf_000",
    "trade_points": [
      {
        "event_date": "2023-07-14",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 27400,
        "raw_price": 2.1846552
      },
      {
        "event_date": "2023-07-25",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 27400,
        "raw_price": 2.1223631000000003
      },
      {
        "event_date": "2023-07-31",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 27100,
        "raw_price": 2.1726516
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 2,
        "shares": 54500,
        "traded_value": "118738.4108400"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 1,
        "shares": 27400,
        "traded_value": "58152.7489400000082200"
      }
    },
    "invested_sessions": 14,
    "cash_sessions": 112,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_001",
    "trade_points": [
      {
        "event_date": "2023-08-11",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 27400,
        "raw_price": 2.1876561
      },
      {
        "event_date": "2023-08-16",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 27400,
        "raw_price": 2.0843745
      },
      {
        "event_date": "2023-10-13",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 29800,
        "raw_price": 1.9545861999999998
      },
      {
        "event_date": "2023-10-23",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 29800,
        "raw_price": 1.8444465
      },
      {
        "event_date": "2023-11-20",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 29100,
        "raw_price": 1.9345801999999999
      },
      {
        "event_date": "2023-12-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 4900,
        "raw_price": 1.8545562
      },
      {
        "event_date": "2023-12-06",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 34000,
        "raw_price": 1.8174546
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 86300,
        "traded_value": "174484.7297199999911300"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 91200,
        "traded_value": "173869.8234000"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 4900,
        "traded_value": "9087.3253800"
      }
    },
    "invested_sessions": 21,
    "cash_sessions": 105,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_002",
    "trade_points": [
      {
        "event_date": "2024-04-29",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33600,
        "raw_price": 1.780534
      },
      {
        "event_date": "2024-05-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 5500,
        "raw_price": 1.8504447
      },
      {
        "event_date": "2024-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 5600,
        "raw_price": 1.7845351999999999
      },
      {
        "event_date": "2024-06-11",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 33700,
        "raw_price": 1.7344795000000002
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 33600,
        "traded_value": "59825.942400"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 1,
        "shares": 5500,
        "traded_value": "10177.4458500"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 5600,
        "traded_value": "9993.3971199999994400"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 1,
        "shares": 33700,
        "traded_value": "58451.9591500000067400"
      }
    },
    "invested_sessions": 27,
    "cash_sessions": 99,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_003",
    "trade_points": [
      {
        "event_date": "2024-09-20",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 39500,
        "raw_price": 1.5164548
      },
      {
        "event_date": "2024-09-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 6400,
        "raw_price": 1.6205137
      },
      {
        "event_date": "2024-09-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 6200,
        "raw_price": 1.7124861000000002
      },
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 24100,
        "raw_price": 1.9994
      },
      {
        "event_date": "2024-10-25",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 2800,
        "raw_price": 2.1463558999999997
      },
      {
        "event_date": "2025-01-27",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33100,
        "raw_price": 2.0866257999999998
      },
      {
        "event_date": "2025-02-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 5400,
        "raw_price": 2.1973406
      },
      {
        "event_date": "2025-02-25",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 25400,
        "raw_price": 2.1883433
      },
      {
        "event_date": "2025-03-03",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 2300,
        "raw_price": 2.1323601
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 2,
        "shares": 72600,
        "traded_value": "128967.2785799999933800"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 3,
        "shares": 18000,
        "traded_value": "32854.3407400000012400"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 2,
        "shares": 49500,
        "traded_value": "103769.4598200"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 2,
        "shares": 5100,
        "traded_value": "10914.2247499999991600"
      }
    },
    "invested_sessions": 39,
    "cash_sessions": 87,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_004",
    "trade_points": [
      {
        "event_date": "2025-03-17",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 27400,
        "raw_price": 2.1886564
      },
      {
        "event_date": "2025-03-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 4600,
        "raw_price": 2.1126336
      },
      {
        "event_date": "2025-04-01",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 32000,
        "raw_price": 2.0663799000000003
      },
      {
        "event_date": "2025-05-30",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 29200,
        "raw_price": 1.980594
      },
      {
        "event_date": "2025-06-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 4700,
        "raw_price": 2.1083673000000003
      },
      {
        "event_date": "2025-07-07",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 21700,
        "raw_price": 2.1253622
      },
      {
        "event_date": "2025-08-04",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 2800,
        "raw_price": 2.2843145000000002
      },
      {
        "event_date": "2025-08-14",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 5100,
        "raw_price": 2.4737419
      },
      {
        "event_date": "2025-08-18",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4100,
        "raw_price": 2.520756
      },
      {
        "event_date": "2025-08-19",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 3400,
        "raw_price": 2.5757725000000002
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 2,
        "shares": 56600,
        "traded_value": "117802.5301600"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 4600,
        "traded_value": "9718.1145600"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 1,
        "shares": 32000,
        "traded_value": "66124.1568000000096000"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 1,
        "shares": 4700,
        "traded_value": "9909.3263100000014100"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 21700,
        "traded_value": "46120.3597400"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 2800,
        "traded_value": "6396.0806000000005600"
      },
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 5100,
        "traded_value": "12616.0836900"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 2,
        "shares": 7500,
        "traded_value": "19092.7261000000006800"
      }
    },
    "invested_sessions": 72,
    "cash_sessions": 54,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_005",
    "trade_points": [
      {
        "event_date": "2025-09-12",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 2300,
        "raw_price": 3.010903
      },
      {
        "event_date": "2025-09-18",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 2200,
        "raw_price": 3.1159345000000003
      },
      {
        "event_date": "2025-09-23",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 4500,
        "raw_price": 3.1140655
      },
      {
        "event_date": "2025-11-12",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 19400,
        "raw_price": 3.0959285000000003
      },
      {
        "event_date": "2025-11-24",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 19400,
        "raw_price": 2.9241224999999997
      },
      {
        "event_date": "2025-12-08",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 18700,
        "raw_price": 3.1019303
      },
      {
        "event_date": "2025-12-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 3.209037
      },
      {
        "event_date": "2026-01-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 3.3709884
      },
      {
        "event_date": "2026-01-15",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 11100,
        "raw_price": 3.3050082
      },
      {
        "event_date": "2026-01-21",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 1600,
        "raw_price": 3.2420271
      },
      {
        "event_date": "2026-02-10",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 18100,
        "raw_price": 3.3279981
      },
      {
        "event_date": "2026-03-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3000,
        "raw_price": 3.1919573
      },
      {
        "event_date": "2026-03-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 3.338998
      }
    ],
    "by_reason": {
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 2300,
        "traded_value": "6925.076900"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 1,
        "shares": 2200,
        "traded_value": "6855.0559000000006600"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 2,
        "shares": 6100,
        "traded_value": "19200.5381100"
      },
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 56200,
        "traded_value": "178303.8751200000058200"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 1,
        "shares": 19400,
        "traded_value": "56727.9764999999941800"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 3,
        "shares": 9000,
        "traded_value": "29757.0702000"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 11100,
        "traded_value": "36685.5910200"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 3000,
        "traded_value": "9575.8719000"
      }
    },
    "invested_sessions": 67,
    "cash_sessions": 59,
    "rejected_order_count": 0
  }
]
