# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`diagnostic_complete`
- 建议：Diagnostic research only; no authorization.
- 阻断项：无

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.024409 | 0.393843 | -0.369435 |
| sharpe | 0.272572 | 0.986649 | -0.714077 |
| Sortino | 0.286811 | 1.681271 | -1.394460 |
| calmar | 0.271254 | 1.263890 | -0.992636 |
| cvar5 | -0.013568 | -0.050295 | 0.036727 |
| max_drawdown | -0.089984 | -0.311612 | 0.221628 |
| turnover | 14.077853 | 3.154018 | 10.923835 |
| total_cost | 715.793750 | 199.775650 | 516.018100 |

## OOS 分布

{
  "window_count": 5,
  "win_rate": 0.2,
  "median_excess_return": -0.13402521079999996,
  "best_excess_return": 0.013989420699999977,
  "worst_excess_return": -0.5241757316
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 267,
    "cash_sessions": 363,
    "exposure_ratio": 0.4238095238095238,
    "turnover": 14.077852717910282,
    "total_cost": 715.79375,
    "cost_drag": 0.0071579375
  },
  "buy_and_hold": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 3.1540175362717813,
    "total_cost": 199.77564999999998,
    "cost_drag": 0.0019977565
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-17",
  "config_hashes": [
    "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
    "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
    "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
    "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3"
  ],
  "training_surface": [
    {
      "window_id": "wf_000",
      "grid": [
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
            0.08385071100000005,
            0.045227795800000095,
            0.08479416590000013
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
            0.09283133870000009,
            0.04133218190000014,
            0.07492483660000016
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
            0.08703166470000001,
            0.03573073460000017,
            0.06630144950000019
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
            0.08936919000000004,
            0.0342122975000002,
            0.06000371760000023
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
            0.07791756900000002,
            0.04444059150000006,
            0.08938077010000012
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
            0.08024438560000004,
            0.05253931750000007,
            0.08369598450000015
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
            0.08134713359999995,
            0.04162914010000007,
            0.07804072090000017
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
            0.07649672099999996,
            0.04080948500000008,
            0.07236470190000019
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
            0.0783779131,
            0.040006073000000066,
            0.0906994531000001
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
            0.0809589926,
            0.04333460710000008,
            0.08622497490000011
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
            0.08343949199999999,
            0.0299328712000001,
            0.08180686670000012
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
            0.07910642449999997,
            0.025186781500000116,
            0.07731713040000013
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
            0.083148583,
            0.042959245400000054,
            0.0919540159000001
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
            0.090551728,
            0.04902603570000007,
            0.08866981010000013
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
            0.09790074569999999,
            0.054910196900000076,
            0.08541073050000014
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
            0.09847833539999998,
            0.046477224300000085,
            0.08212130440000015
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
            0.08065015,
            0.04372206030000005,
            0.0916405483000001
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
            0.0854357295,
            0.05046342920000006,
            0.08802652170000011
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
            0.0901291417,
            0.057179031100000076,
            0.08438561720000012
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
            0.09480959900000001,
            0.04826297650000008,
            0.08069102440000014
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
            0.0821215451,
            0.04065905370000006,
            0.09230974900000011
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
            0.08838694460000002,
            0.044056080700000076,
            0.08924213580000012
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
            0.09458581890000001,
            0.04748571140000009,
            0.08625569560000013
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
            0.1007976893,
            0.0424134327000001,
            0.08321751340000014
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
            0.0821215451,
            0.038884897200000046,
            0.0945732844000001
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
            0.08838694460000002,
            0.04046236410000005,
            0.09369012520000009
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
            0.09458581890000001,
            0.04210881030000006,
            0.09284140650000008
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
            0.1007976893,
            0.043740320700000064,
            0.0919562473000001
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
            0.08125563870000002,
            0.038884897200000046,
            0.0952620900000001
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
            0.08661722040000001,
            0.04046236410000005,
            0.0950203364000001
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
            0.09210309980000003,
            0.04210881030000006,
            0.09477392600000009
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
            0.09745940950000002,
            0.043740320700000064,
            0.09453207240000008
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
            0.0836840915,
            0.038974870200000046,
            0.09546597800000009
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
            0.09140875440000001,
            0.040644309500000045,
            0.09546597800000009
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
            0.0991644804,
            0.042380728700000043,
            0.09546597800000009
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
            0.1068215998,
            0.04405016800000004,
            0.09546597800000009
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
            0.08099324899999999,
            0.04118614690000005,
            0.09546597800000009
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
            0.08594128229999999,
            0.04522781460000005,
            0.09546597800000009
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
            0.09094678979999998,
            0.049190506000000044,
            0.09546597800000009
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
            0.09583493629999998,
            0.053153197400000046,
            0.09546597800000009
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
            0.08180061529999999,
            0.041733922800000045,
            0.09546597800000009
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
            0.08751120739999999,
            0.04629843360000005,
            0.09546597800000009
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
            0.09321511389999998,
            0.05086294440000005,
            0.09546597800000009
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
            0.09894391289999997,
            0.055334383100000044,
            0.09546597800000009
          ],
          "positive_window_share": 1.0
        }
      ],
      "trend": []
    },
    {
      "window_id": "wf_001",
      "grid": [
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09179274349999994,
            0.045227795800000095,
            0.08479416590000013,
            -0.015623708299999983
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09362049279999998,
            0.04133218190000014,
            0.07492483660000016,
            -0.018827687599999962
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.0937942169999999,
            0.03573073460000017,
            0.06630144950000019,
            -0.02202587509999994
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.0903313584999999,
            0.0342122975000002,
            0.06000371760000023,
            -0.024767801999999922
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09332821519999993,
            0.04444059150000006,
            0.08938077010000012,
            -0.010544130699999973
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09619207209999994,
            0.05253931750000007,
            0.08369598450000015,
            -0.008727462199999952
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09799463859999986,
            0.04162914010000007,
            0.07804072090000017,
            -0.007147647099999918
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09360913289999989,
            0.04080948500000008,
            0.07236470190000019,
            -0.004879915499999901
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09362578589999992,
            0.040006073000000066,
            0.0906994531000001,
            -0.007548522399999993
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09656519009999992,
            0.04333460710000008,
            0.08622497490000011,
            -0.003434924299999989
          ],
          "positive_window_share": 0.75
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
            0.09949488319999991,
            0.0299328712000001,
            0.08180686670000012,
            0.0006688887000000227
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
            0.09549356739999988,
            0.025186781500000116,
            0.07731713040000013,
            0.004893827500000031
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09540093089999992,
            0.042959245400000054,
            0.0919540159000001,
            -0.006446011999999987
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10017080109999991,
            0.04902603570000007,
            0.08866981010000013,
            -0.0011257491999999841
          ],
          "positive_window_share": 0.75
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
            0.1049686364999999,
            0.054910196900000076,
            0.08541073050000014,
            0.004163886100000028
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
            0.10279347559999988,
            0.046477224300000085,
            0.08212130440000015,
            0.009398223500000025
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09292907709999992,
            0.04372206030000005,
            0.0916405483000001,
            -0.006014141599999995
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09497709049999992,
            0.05046342920000006,
            0.08802652170000011,
            -0.000304244799999992
          ],
          "positive_window_share": 0.75
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
            0.09708872099999992,
            0.057179031100000076,
            0.08438561720000012,
            0.005363346200000008
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
            0.09918300649999992,
            0.04826297650000008,
            0.08069102440000014,
            0.011035327800000008
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09443048119999992,
            0.04065905370000006,
            0.09230974900000011,
            -0.009857107899999995
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09800990769999993,
            0.044056080700000076,
            0.08924213580000012,
            -0.0083482899
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10162700029999992,
            0.04748571140000009,
            0.08625569560000013,
            -0.006873722400000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10514951269999992,
            0.0424134327000001,
            0.08321751340000014,
            -0.0054278163999999934
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09443048119999992,
            0.038884897200000046,
            0.0945732844000001,
            -0.009857107899999995
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09800990769999993,
            0.04046236410000005,
            0.09369012520000009,
            -0.0083482899
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10162700029999992,
            0.04210881030000006,
            0.09284140650000008,
            -0.006873722400000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10514951269999992,
            0.043740320700000064,
            0.0919562473000001,
            -0.0054278163999999934
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09385235769999992,
            0.038884897200000046,
            0.0952620900000001,
            -0.009857107899999995
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09675138859999993,
            0.04046236410000005,
            0.0950203364000001,
            -0.0083482899
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09983028379999993,
            0.04210881030000006,
            0.09477392600000009,
            -0.006873722400000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10281300779999994,
            0.043740320700000064,
            0.09453207240000008,
            -0.0054278163999999934
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09455969599999992,
            0.038974870200000046,
            0.09546597800000009,
            -0.009857107899999995
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09805108349999991,
            0.040644309500000045,
            0.09546597800000009,
            -0.0083482899
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10169003529999993,
            0.042380728700000043,
            0.09546597800000009,
            -0.006873722400000004
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.10523301589999992,
            0.04405016800000004,
            0.09546597800000009,
            -0.0054278163999999934
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09226934189999991,
            0.04118614690000005,
            0.09546597800000009,
            -0.009070090199999992
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.0934689818999999,
            0.04522781460000005,
            0.09546597800000009,
            -0.0067550304000000005
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09472021499999989,
            0.049190506000000044,
            0.09546597800000009,
            -0.004461217199999992
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09594484749999987,
            0.053153197400000046,
            0.09546597800000009,
            -0.0022215097999999933
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09226934189999991,
            0.041733922800000045,
            0.09546597800000009,
            -0.007924374099999992
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.0934689818999999,
            0.04629843360000005,
            0.09546597800000009,
            -0.004432930099999996
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.09472021499999989,
            0.05086294440000005,
            0.09546597800000009,
            -0.001004298099999995
          ],
          "positive_window_share": 0.75
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
            0.09594484749999987,
            0.055334383100000044,
            0.09546597800000009,
            0.002405347200000005
          ],
          "positive_window_share": 1.0
        }
      ],
      "trend": []
    },
    {
      "window_id": "wf_002",
      "grid": [
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06810950320000016,
            0.08479416590000013,
            -0.015623708299999983,
            -0.3053267702999998
          ],
          "positive_window_share": 0.5
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
            0.06537318420000021,
            0.07492483660000016,
            -0.018827687599999962,
            -0.3048997546999997
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06094081570000025,
            0.06630144950000019,
            -0.02202587509999994,
            -0.3056050211999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06079079050000028,
            0.06000371760000023,
            -0.024767801999999922,
            -0.32658761299999944
          ],
          "positive_window_share": 0.5
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
            0.06529250030000011,
            0.08938077010000012,
            -0.010544130699999973,
            -0.30359766229999985
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
            0.07327524700000013,
            0.08369598450000015,
            -0.008727462199999952,
            -0.30152307969999975
          ],
          "positive_window_share": 0.5
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
            0.061844176600000134,
            0.07804072090000017,
            -0.007147647099999918,
            -0.3009180333999997
          ],
          "positive_window_share": 0.5
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
            0.06051326110000015,
            0.07236470190000019,
            -0.004879915499999901,
            -0.3203289338999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06214701960000012,
            0.0906994531000001,
            -0.007548522399999993,
            -0.31105721869999986
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
            0.06643561220000015,
            0.08622497490000011,
            -0.003434924299999989,
            -0.31748941899999983
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.053803675800000166,
            0.08180686670000012,
            0.0006688887000000227,
            -0.3248522825999999
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.049725638600000184,
            0.07731713040000013,
            0.004893827500000031,
            -0.3469170675999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0640987068000001,
            0.0919540159000001,
            -0.006446011999999987,
            -0.32508558249999986
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.07012785620000012,
            0.08866981010000013,
            -0.0011257491999999841,
            -0.34586365749999987
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.07630426510000013,
            0.08541073050000014,
            0.004163886100000028,
            -0.3704839767999999
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.06768034820000013,
            0.08212130440000015,
            0.009398223500000025,
            -0.41108917389999977
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0648785178000001,
            0.0916405483000001,
            -0.006014141599999995,
            -0.32268485069999986
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.07169511310000011,
            0.08802652170000011,
            -0.000304244799999992,
            -0.3413077535999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.07856850210000013,
            0.08438561720000012,
            0.005363346200000008,
            -0.3606460090999999
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.06951970370000013,
            0.08069102440000014,
            0.011035327800000008,
            -0.3985546232999998
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06174447710000011,
            0.09230974900000011,
            -0.009857107899999995,
            -0.3020664453999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06522775710000012,
            0.08924213580000012,
            -0.0083482899,
            -0.30024770679999985
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
            0.06873843510000013,
            0.08625569560000013,
            -0.006873722400000004,
            -0.29856750019999984
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
            0.06354105550000015,
            0.08321751340000014,
            -0.0054278163999999934,
            -0.2969812879999998
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0599238559000001,
            0.0945732844000001,
            -0.009857107899999995,
            -0.30007320049999986
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0615402111000001,
            0.09369012520000009,
            -0.0083482899,
            -0.2962478730999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06322544560000011,
            0.09284140650000008,
            -0.006873722400000004,
            -0.2928627075999998
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06489053860000012,
            0.0919562473000001,
            -0.0054278163999999934,
            -0.2896131546999998
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0599238559000001,
            0.0952620900000001,
            -0.009857107899999995,
            -0.2953615838999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0615402111000001,
            0.0950203364000001,
            -0.0083482899,
            -0.2870116142999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06322544560000011,
            0.09477392600000009,
            -0.006873722400000004,
            -0.2788737975999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06489053860000012,
            0.09453207240000008,
            -0.0054278163999999934,
            -0.27111432889999987
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.060015828300000094,
            0.09546597800000009,
            -0.009857107899999995,
            -0.2953615838999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.061739151400000095,
            0.09546597800000009,
            -0.0083482899,
            -0.2870116142999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0635033622000001,
            0.09546597800000009,
            -0.006873722400000004,
            -0.2788737975999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06522668530000009,
            0.09546597800000009,
            -0.0054278163999999934,
            -0.27111432889999987
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0622745834000001,
            0.09546597800000009,
            -0.009070090199999992,
            -0.2953615838999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06633094660000009,
            0.09546597800000009,
            -0.0067550304000000005,
            -0.2870116142999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0704663861000001,
            0.09546597800000009,
            -0.004461217199999992,
            -0.2788737975999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.07444387300000009,
            0.09546597800000009,
            -0.0022215097999999933,
            -0.27111432889999987
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0628415608000001,
            0.09546597800000009,
            -0.007924374099999992,
            -0.3002407100999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.06751383920000009,
            0.09546597800000009,
            -0.004432930099999996,
            -0.2969343090999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0721861176000001,
            0.09546597800000009,
            -0.001004298099999995,
            -0.2940023988999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            true,
            true,
            false
          ],
          "oos_returns": [
            0.0767599182000001,
            0.09546597800000009,
            0.002405347200000005,
            -0.29130566109999995
          ],
          "positive_window_share": 0.75
        }
      ],
      "trend": []
    },
    {
      "window_id": "wf_003",
      "grid": [
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.06894704340000019,
            -0.015623708299999983,
            -0.3053267702999998,
            -0.2150244396999999
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
            0.05495219380000024,
            -0.018827687599999962,
            -0.3048997546999997,
            -0.24611994479999988
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
            0.04236325600000029,
            -0.02202587509999994,
            -0.3056050211999996,
            -0.25083521199999986
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
            0.03270840270000033,
            -0.024767801999999922,
            -0.32658761299999944,
            -0.24495676499999985
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
            0.07601329870000018,
            -0.010544130699999973,
            -0.30359766229999985,
            -0.1878274141999999
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
            0.0686136800000002,
            -0.008727462199999952,
            -0.30152307969999975,
            -0.22822071369999986
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
            0.06141741800000022,
            -0.007147647099999918,
            -0.3009180333999997,
            -0.23036029669999986
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
            0.054007809200000256,
            -0.004879915499999901,
            -0.3203289338999996,
            -0.22227092769999987
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
            0.07775958920000017,
            -0.007548522399999993,
            -0.31105721869999986,
            -0.16178528109999993
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
            0.07201682300000017,
            -0.003434924299999989,
            -0.31748941899999983,
            -0.21190371849999992
          ],
          "positive_window_share": 0.25
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
            0.06629586480000019,
            0.0006688887000000227,
            -0.3248522825999999,
            -0.21365994309999992
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
            0.0605851316000002,
            0.004893827500000031,
            -0.3469170675999998,
            -0.20703997479999992
          ],
          "positive_window_share": 0.5
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
            0.07938786870000017,
            -0.006446011999999987,
            -0.32508558249999986,
            -0.15269009239999992
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
            0.07523283060000019,
            -0.0011257491999999841,
            -0.34586365749999987,
            -0.2049432797999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            true,
            false,
            false
          ],
          "oos_returns": [
            0.0710337161000002,
            0.004163886100000028,
            -0.3704839767999999,
            -0.2127540657999999
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
            0.06687376360000022,
            0.009398223500000025,
            -0.41108917389999977,
            -0.2163827587999999
          ],
          "positive_window_share": 0.5
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
            0.07909235190000016,
            -0.006014141599999995,
            -0.32268485069999986,
            -0.14187253219999996
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
            0.07451462360000016,
            -0.000304244799999992,
            -0.3413077535999999,
            -0.18441506299999993
          ],
          "positive_window_share": 0.25
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
            0.07005242590000019,
            0.005363346200000008,
            -0.3606460090999999,
            -0.20394622909999993
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
            0.0655099389000002,
            0.011035327800000008,
            -0.3985546232999998,
            -0.20606117739999993
          ],
          "positive_window_share": 0.5
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
            0.07973401230000016,
            -0.009857107899999995,
            -0.3020664453999999,
            -0.13363362289999994
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
            0.07583301900000017,
            -0.0083482899,
            -0.30024770679999985,
            -0.16600873769999994
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
            0.0718569664000002,
            -0.006873722400000004,
            -0.29856750019999984,
            -0.19942259079999994
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
            0.06800478640000021,
            -0.0054278163999999934,
            -0.2969812879999998,
            -0.1998069004999999
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
            0.08157898220000015,
            -0.009857107899999995,
            -0.30007320049999986,
            -0.13190761719999994
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
            0.07953659970000015,
            -0.0083482899,
            -0.2962478730999999,
            -0.16239539269999995
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
            0.07745061990000016,
            -0.006873722400000004,
            -0.2928627075999998,
            -0.19384873139999992
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
            0.07536474010000016,
            -0.0054278163999999934,
            -0.2896131546999998,
            -0.19449277669999993
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
            0.08261937140000014,
            -0.009857107899999995,
            -0.2953615838999999,
            -0.12907564779999994
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
            0.08147465790000016,
            -0.0083482899,
            -0.2870116142999999,
            -0.15710915979999993
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
            0.08035182460000015,
            -0.006873722400000004,
            -0.2788737975999999,
            -0.18607242649999992
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
            0.07915554860000015,
            -0.0054278163999999934,
            -0.27111432889999987,
            -0.1892975164999999
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
            0.08261937140000014,
            -0.009857107899999995,
            -0.2953615838999999,
            -0.12907564779999994
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
            0.08147465790000016,
            -0.0083482899,
            -0.2870116142999999,
            -0.15710915979999993
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
            0.08035182460000015,
            -0.006873722400000004,
            -0.2788737975999999,
            -0.18607242649999992
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
            0.07915554860000015,
            -0.0054278163999999934,
            -0.27111432889999987,
            -0.1892975164999999
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
            0.08261937140000014,
            -0.009070090199999992,
            -0.2953615838999999,
            -0.11959650209999995
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
            0.08147465790000016,
            -0.0067550304000000005,
            -0.2870116142999999,
            -0.13769779049999994
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
            0.08035182460000015,
            -0.004461217199999992,
            -0.2788737975999999,
            -0.15994676069999994
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
            0.07915554860000015,
            -0.0022215097999999933,
            -0.27111432889999987,
            -0.17586009119999993
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
            0.08282743380000016,
            -0.007924374099999992,
            -0.3002407100999999,
            -0.11959650209999995
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
            0.08185924000000017,
            -0.004432930099999996,
            -0.2969343090999999,
            -0.13769779049999994
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
            0.08085037680000015,
            -0.001004298099999995,
            -0.2940023988999999,
            -0.15994676069999994
          ],
          "positive_window_share": 0.25
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
            0.07991362570000016,
            0.002405347200000005,
            -0.29130566109999995,
            -0.17586009119999993
          ],
          "positive_window_share": 0.5
        }
      ],
      "trend": []
    },
    {
      "window_id": "wf_004",
      "grid": [
        {
          "config_hash": "815b8196c744b75fe4f851240badeee093c72d4372769ddc31ba9ac4888a5b95",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.030049612499999948,
            -0.3053267702999998,
            -0.2150244396999999,
            -0.0659837066999999
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.039448877099999904,
            -0.3048997546999997,
            -0.24611994479999988,
            -0.07450480309999985
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.04623547299999986,
            -0.3056050211999996,
            -0.25083521199999986,
            -0.09738077519999985
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.05222447519999984,
            -0.32658761299999944,
            -0.24495676499999985,
            -0.1126538019999998
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.024565890799999962,
            -0.30359766229999985,
            -0.1878274141999999,
            -0.07197333509999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.028908859799999923,
            -0.30152307969999975,
            -0.22822071369999986,
            -0.0886286184999999
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.03330684089999987,
            -0.3009180333999997,
            -0.23036029669999986,
            -0.11428973529999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.03507542819999984,
            -0.3203289338999996,
            -0.22227092769999987,
            -0.12382932259999989
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.020243433299999974,
            -0.31105721869999986,
            -0.16178528109999993,
            -0.08002540069999994
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02059131749999997,
            -0.31748941899999983,
            -0.21190371849999992,
            -0.09362011769999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.020974762499999952,
            -0.3248522825999999,
            -0.21365994309999992,
            -0.11072283439999994
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02135525769999992,
            -0.3469170675999998,
            -0.20703997479999992,
            -0.11871239989999995
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.019635830199999982,
            -0.32508558249999986,
            -0.15269009239999992,
            -0.08061889549999994
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.019416660399999966,
            -0.34586365749999987,
            -0.2049432797999999,
            -0.07978282189999991
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.01923305139999995,
            -0.3704839767999999,
            -0.2127540657999999,
            -0.11327593489999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.019055943499999922,
            -0.41108917389999977,
            -0.2163827587999999,
            -0.12711538819999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.019279936999999983,
            -0.32268485069999986,
            -0.14187253219999996,
            -0.07759342929999993
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.018599905499999972,
            -0.3413077535999999,
            -0.18441506299999993,
            -0.0737261452999999
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.018049864399999963,
            -0.3606460090999999,
            -0.20394622909999993,
            -0.0979315105999999
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.017550778599999955,
            -0.3985546232999998,
            -0.20606117739999993,
            -0.10881292019999993
          ],
          "positive_window_share": 0.0
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
            -0.02425443419999998,
            -0.3020664453999999,
            -0.13363362289999994,
            -0.07641164639999995
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.028904887299999973,
            -0.30024770679999985,
            -0.16600873769999994,
            -0.07173169749999991
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.03358281409999997,
            -0.29856750019999984,
            -0.19942259079999994,
            -0.09265524769999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.03823326719999995,
            -0.2969812879999998,
            -0.1998069004999999,
            -0.10365123159999994
          ],
          "positive_window_share": 0.0
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
            -0.021996006199999987,
            -0.30007320049999986,
            -0.13190761719999994,
            -0.07485295499999994
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.024456509799999984,
            -0.2962478730999999,
            -0.16239539269999995,
            -0.06857057939999993
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.026888046899999976,
            -0.2928627075999998,
            -0.19384873139999992,
            -0.07271266419999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02938661219999998,
            -0.2896131546999998,
            -0.19449277669999993,
            -0.08964587019999992
          ],
          "positive_window_share": 0.0
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
            -0.021996006199999987,
            -0.2953615838999999,
            -0.12907564779999994,
            -0.07338763229999995
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.024456509799999984,
            -0.2870116142999999,
            -0.15710915979999993,
            -0.06543859079999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.026888046899999976,
            -0.2788737975999999,
            -0.18607242649999992,
            -0.06826301419999992
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02938661219999998,
            -0.27111432889999987,
            -0.1892975164999999,
            -0.08656797769999994
          ],
          "positive_window_share": 0.0
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
            -0.021095649699999997,
            -0.2953615838999999,
            -0.12907564779999994,
            -0.07625491409999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02266389199999999,
            -0.2870116142999999,
            -0.15710915979999993,
            -0.07125259459999997
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.024232634299999986,
            -0.2788737975999999,
            -0.18607242649999992,
            -0.06646792899999997
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.025801276599999978,
            -0.27111432889999987,
            -0.1892975164999999,
            -0.07814858769999997
          ],
          "positive_window_share": 0.0
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
            -0.021095649699999997,
            -0.2953615838999999,
            -0.11959650209999995,
            -0.07679341739999997
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02266389199999999,
            -0.2870116142999999,
            -0.13769779049999994,
            -0.07244548229999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.024232634299999986,
            -0.2788737975999999,
            -0.15994676069999994,
            -0.06825328879999995
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.025801276599999978,
            -0.27111432889999987,
            -0.17586009119999993,
            -0.08045850909999996
          ],
          "positive_window_share": 0.0
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
            -0.021095649699999997,
            -0.3002407100999999,
            -0.11959650209999995,
            -0.07513891489999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.02266389199999999,
            -0.2969343090999999,
            -0.13769779049999994,
            -0.06915053139999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.024232634299999986,
            -0.2940023988999999,
            -0.15994676069999994,
            -0.06347889419999996
          ],
          "positive_window_share": 0.0
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            false,
            false,
            false,
            false
          ],
          "oos_returns": [
            -0.025801276599999978,
            -0.29130566109999995,
            -0.17586009119999993,
            -0.07412055529999995
          ],
          "positive_window_share": 0.0
        }
      ],
      "trend": []
    }
  ],
  "run_manifest": {
    "schema_version": 1,
    "runner": "run_instrument_validation",
    "source_provider": "ValidationMarketDataProvider",
    "data_cutoff": "2026-09-17",
    "requested_start": "2021-01-04",
    "data_fingerprint": "9ffa7241c7bf98aca18d0460a2fbc11c74366ce3d05a5d7319dcf65185890865",
    "run_mode": "research_diagnostic",
    "research_only": true,
    "activation_eligible": false,
    "shadow_run_eligible": false,
    "trading_authorized": false,
    "target": {
      "exposure_id": "star_50",
      "stock_code": "588000.SH",
      "sub_layer": "broad_domestic_growth",
      "scope": "formal"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
        "config": {
          "grid": {
            "step_pct": 0.05,
            "unit_pct": 0.15,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
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
        "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
        "config": {
          "grid": {
            "step_pct": 0.025,
            "unit_pct": 0.15,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
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
        "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
        "config": {
          "grid": {
            "step_pct": 0.06,
            "unit_pct": 0.2,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
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
        "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
        "config": {
          "grid": {
            "step_pct": 0.06,
            "unit_pct": 0.2,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
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
        "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
        "config": {
          "grid": {
            "step_pct": 0.055,
            "unit_pct": 0.15,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
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
        "unit_pct"
      ],
      "trend": []
    },
    "profile_id": "grid_plus_optional_trend",
    "profile_hash": "f4f9eb95055b94fd1694c9f43501573cd2e7eb3f2e5590104fa2a83fd6ebf8b1",
    "execution_windows": [
      {
        "window_id": "wf_000",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.05,
            "unit_pct": 0.15,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": {
          "strategy_id": "full_adaptive",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.05,
              "unit_pct": 0.15,
              "initial_model": "fixed",
              "fixed_initial_pct": 0.5,
              "max_grid_per_day": 1,
              "atr_stop_multiple": 3.0,
              "cooldown_sessions": 5
            },
            "trend": {
              "stop_n": 2.0,
              "risk_per_unit": 0.005,
              "add_n": 0.5,
              "max_units": 4,
              "require_macd_bullish": true,
              "amount_ratio_min": null
            },
            "cost": {
              "commission_rate": 0.0001,
              "minimum_commission": 5.0,
              "slippage_bps": 3.0,
              "sell_tax_rate": 0.0,
              "transfer_fee_rate": 0.0
            }
          },
          "policy_id": "full_adaptive",
          "spec_hash": "09b46762ef403fab4bd180b196f9f60138fded696ab47dfcec0b21f3af6e7e9a"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "1f13464049e52d8111a8b7b843cd0a40dcabaa7151d26e5e7251c22794569b23",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.15689018847790748,
              "annual_volatility": 0.23734028859578868,
              "sharpe": -0.6610347927279435,
              "sortino": -1.1525047999921503,
              "calmar": -0.9614544392759045,
              "worst_126_session_return": -0.08116785120000014,
              "cvar5": -0.031069641573995888,
              "win_rate": 0.464,
              "payoff_ratio": 0.9990220183598529,
              "profit_factor": 0.9053637041386168,
              "turnover": 1.0102829987758115,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.998512,
              "max_drawdown": -0.16318005520476397,
              "recovery_sessions": 3,
              "total_cost": 39.98512
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "6131e0381c28481b1fc86e59486e433d1800f68b0e2ae0f04770f49bd0008a96",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.08475286517870528,
              "annual_volatility": 0.1186828202019146,
              "sharpe": -0.7141123292698605,
              "sortino": -1.2233699445576183,
              "calmar": -0.9807925932590505,
              "worst_126_session_return": -0.042978235700000145,
              "cvar5": -0.015583738029473456,
              "win_rate": 0.464,
              "payoff_ratio": 1.031035640348019,
              "profit_factor": 0.8925383155251506,
              "turnover": 0.8091473650181449,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.04776944554455446,
              "max_drawdown": -0.08641262766583724,
              "recovery_sessions": 3,
              "total_cost": 529.12357
            }
          }
        ]
      },
      {
        "window_id": "wf_001",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.025,
            "unit_pct": 0.15,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": {
          "strategy_id": "full_adaptive",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.025,
              "unit_pct": 0.15,
              "initial_model": "fixed",
              "fixed_initial_pct": 0.5,
              "max_grid_per_day": 1,
              "atr_stop_multiple": 3.0,
              "cooldown_sessions": 5
            },
            "trend": {
              "stop_n": 2.0,
              "risk_per_unit": 0.005,
              "add_n": 0.5,
              "max_units": 4,
              "require_macd_bullish": true,
              "amount_ratio_min": null
            },
            "cost": {
              "commission_rate": 0.0001,
              "minimum_commission": 5.0,
              "slippage_bps": 3.0,
              "sell_tax_rate": 0.0,
              "transfer_fee_rate": 0.0
            }
          },
          "policy_id": "full_adaptive",
          "spec_hash": "44f728f89b5e3024f86c94e44518bfaf1ea28ce504fc285737af24991859864e"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "0811a7ce7defbd83af87c94638e3ef01257fc8a8046aef13efac63fb66ed6e5c",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 1.469027745770405,
              "annual_volatility": 0.5570574417772431,
              "sharpe": 2.637120762777354,
              "sortino": 6.3548688967785845,
              "calmar": 7.72093383342325,
              "worst_126_session_return": 0.5656884306000005,
              "cvar5": -0.0493030348918008,
              "win_rate": 0.488,
              "payoff_ratio": 1.550150528548891,
              "profit_factor": 1.5251481006690704,
              "turnover": 0.7421812645357772,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9996936936936938,
              "max_drawdown": -0.19026555303596981,
              "recovery_sessions": 7,
              "total_cost": 39.95694
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "ea302f29e0fe1f3b6e3584e43b20acfc27da62b195e6250719b19dbe267483ac",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.6485040003822111,
              "annual_volatility": 0.2865835545526817,
              "sharpe": 2.2628793246508456,
              "sortino": 5.614971046744961,
              "calmar": 6.592666092342389,
              "worst_126_session_return": 0.2813965028999994,
              "cvar5": -0.024628150285319783,
              "win_rate": 0.488,
              "payoff_ratio": 1.6131040538566146,
              "profit_factor": 1.5374898013320857,
              "turnover": 0.9940700982969817,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.06509205555555556,
              "max_drawdown": -0.09836748764441006,
              "recovery_sessions": 7,
              "total_cost": 575.14971
            }
          }
        ]
      },
      {
        "window_id": "wf_002",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.06,
            "unit_pct": 0.2,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": {
          "strategy_id": "full_adaptive",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.06,
              "unit_pct": 0.2,
              "initial_model": "fixed",
              "fixed_initial_pct": 0.5,
              "max_grid_per_day": 1,
              "atr_stop_multiple": 3.0,
              "cooldown_sessions": 5
            },
            "trend": {
              "stop_n": 2.0,
              "risk_per_unit": 0.005,
              "add_n": 0.5,
              "max_units": 4,
              "require_macd_bullish": true,
              "amount_ratio_min": null
            },
            "cost": {
              "commission_rate": 0.0001,
              "minimum_commission": 5.0,
              "slippage_bps": 3.0,
              "sell_tax_rate": 0.0,
              "transfer_fee_rate": 0.0
            }
          },
          "policy_id": "full_adaptive",
          "spec_hash": "67cf3d971b8b0764fbf7bb7a7ff2e309cedad7648cadc7c4ec8c1c5ab5dc53f9"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "e0c69661fe5bf2a4a6daad0383446692f4bfbaf78d66cf402ca517c24373c774",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.3939572967555829,
              "annual_volatility": 0.2784735891511731,
              "sharpe": 1.414702550272076,
              "sortino": 2.0386473580058486,
              "calmar": 2.2074411158445426,
              "worst_126_session_return": 0.17910455269999948,
              "cvar5": -0.033409190495883236,
              "win_rate": 0.504,
              "payoff_ratio": 1.252431101443798,
              "profit_factor": 1.3150526565159881,
              "turnover": 1.0559854064273158,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9984714714714715,
              "max_drawdown": -0.17846786214492483,
              "recovery_sessions": 1,
              "total_cost": 39.94473
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "c460ab0a8c4386b12527408fc386abbf68ffb20f7d67c008cde0f07c827cec1e",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.18194684397737504,
              "annual_volatility": 0.1395250608019236,
              "sharpe": 1.3040441834006826,
              "sortino": 1.8938821015602911,
              "calmar": 1.9558255520218226,
              "worst_126_session_return": 0.0864528551999999,
              "cvar5": -0.016746467734176835,
              "win_rate": 0.504,
              "payoff_ratio": 1.277020422603453,
              "profit_factor": 1.2976175261938312,
              "turnover": 0.7965327952156988,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.05336662068965518,
              "max_drawdown": -0.09302815570094614,
              "recovery_sessions": 1,
              "total_cost": 458.21448
            }
          }
        ]
      },
      {
        "window_id": "wf_003",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.06,
            "unit_pct": 0.2,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": {
          "strategy_id": "full_adaptive",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.06,
              "unit_pct": 0.2,
              "initial_model": "fixed",
              "fixed_initial_pct": 0.5,
              "max_grid_per_day": 1,
              "atr_stop_multiple": 3.0,
              "cooldown_sessions": 5
            },
            "trend": {
              "stop_n": 2.0,
              "risk_per_unit": 0.005,
              "add_n": 0.5,
              "max_units": 4,
              "require_macd_bullish": true,
              "amount_ratio_min": null
            },
            "cost": {
              "commission_rate": 0.0001,
              "minimum_commission": 5.0,
              "slippage_bps": 3.0,
              "sell_tax_rate": 0.0,
              "transfer_fee_rate": 0.0
            }
          },
          "policy_id": "full_adaptive",
          "spec_hash": "67cf3d971b8b0764fbf7bb7a7ff2e309cedad7648cadc7c4ec8c1c5ab5dc53f9"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "e0c69661fe5bf2a4a6daad0383446692f4bfbaf78d66cf402ca517c24373c774",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.27159941969063106,
              "annual_volatility": 0.29696935810269526,
              "sharpe": 0.9145705180691033,
              "sortino": 1.4028600929315111,
              "calmar": 1.6470767444410677,
              "worst_126_session_return": 0.12657749660000062,
              "cvar5": -0.04260296659573252,
              "win_rate": 0.52,
              "payoff_ratio": 1.060433593400413,
              "profit_factor": 1.1682742978140144,
              "turnover": 0.8683399628571316,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.999033033033033,
              "max_drawdown": -0.1648978534893939,
              "recovery_sessions": 1,
              "total_cost": 39.95034
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "c460ab0a8c4386b12527408fc386abbf68ffb20f7d67c008cde0f07c827cec1e",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.13060946039519128,
              "annual_volatility": 0.1487407113994201,
              "sharpe": 0.8781016250786904,
              "sortino": 1.3429567845514845,
              "calmar": 1.53192470471055,
              "worst_126_session_return": 0.06278336859999878,
              "cvar5": -0.021357941853171025,
              "win_rate": 0.52,
              "payoff_ratio": 1.0682407237801868,
              "profit_factor": 1.1572607840952023,
              "turnover": 0.8249099466430094,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.055339875000000004,
              "max_drawdown": -0.08525840727914191,
              "recovery_sessions": 1,
              "total_cost": 506.56314
            }
          }
        ]
      },
      {
        "window_id": "wf_004",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.055,
            "unit_pct": 0.15,
            "initial_model": "fixed",
            "fixed_initial_pct": 0.5,
            "max_grid_per_day": 1,
            "atr_stop_multiple": 3.0,
            "cooldown_sessions": 5
          },
          "trend": {
            "stop_n": 2.0,
            "risk_per_unit": 0.005,
            "add_n": 0.5,
            "max_units": 4,
            "require_macd_bullish": true,
            "amount_ratio_min": null
          },
          "cost": {
            "commission_rate": 0.0001,
            "minimum_commission": 5.0,
            "slippage_bps": 3.0,
            "sell_tax_rate": 0.0,
            "transfer_fee_rate": 0.0
          }
        },
        "reference_benchmark_id": "buy_and_hold",
        "strategy_spec": {
          "strategy_id": "full_adaptive",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.055,
              "unit_pct": 0.15,
              "initial_model": "fixed",
              "fixed_initial_pct": 0.5,
              "max_grid_per_day": 1,
              "atr_stop_multiple": 3.0,
              "cooldown_sessions": 5
            },
            "trend": {
              "stop_n": 2.0,
              "risk_per_unit": 0.005,
              "add_n": 0.5,
              "max_units": 4,
              "require_macd_bullish": true,
              "amount_ratio_min": null
            },
            "cost": {
              "commission_rate": 0.0001,
              "minimum_commission": 5.0,
              "slippage_bps": 3.0,
              "sell_tax_rate": 0.0,
              "transfer_fee_rate": 0.0
            }
          },
          "policy_id": "full_adaptive",
          "spec_hash": "da0f198549720c158e876cc7c2efbb0cbcd4cebfb225f5c37d7359a2334518ff"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "5d7b449757ca7dbd57c3ee5a4c95d62f78d6beedb2e17b443075ede73c27a8df",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.44103651107124,
              "annual_volatility": 0.5161893936556832,
              "sharpe": 0.8544083169702381,
              "sortino": 1.4471374144384623,
              "calmar": 1.4153379864115931,
              "worst_126_session_return": 0.19869261479999856,
              "cvar5": -0.06532219539411704,
              "win_rate": 0.536,
              "payoff_ratio": 0.9769747763055647,
              "profit_factor": 1.168880535937015,
              "turnover": 0.8017140036715475,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.997849849849849,
              "max_drawdown": -0.3116121486920811,
              "recovery_sessions": 13,
              "total_cost": 39.93852
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "826f1361061e7b08ab053867a00259ecc2d5c02ebdca1f254f98f4edd2c4dd89",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.2256354621480159,
              "annual_volatility": 0.2582088816290768,
              "sharpe": 0.8738485706783184,
              "sortino": 1.4731390650010097,
              "calmar": 1.3606442457199321,
              "worst_126_session_return": 0.10619074080000024,
              "cvar5": -0.03269279040307558,
              "win_rate": 0.536,
              "payoff_ratio": 0.9867180894165231,
              "profit_factor": 1.1598265261562641,
              "turnover": 1.1532943112642393,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.07238489719626168,
              "max_drawdown": -0.16582987276635974,
              "recovery_sessions": 13,
              "total_cost": 573.72592
            }
          }
        ]
      }
    ],
    "benchmark_specs": [
      {
        "benchmark_id": "buy_and_hold",
        "rebalance_sessions": null,
        "target_weight": 1.0,
        "version": "1"
      },
      {
        "benchmark_id": "fixed_half_hold",
        "rebalance_sessions": 1,
        "target_weight": 0.5,
        "version": "1"
      }
    ],
    "experiment": {
      "allowed_axes": {
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
        "unit_pct": [
          0.05,
          0.1,
          0.15,
          0.2
        ]
      },
      "as_of_date": "2026-09-17",
      "experiment_id": "round2-star50-20260917",
      "profile": {
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "version": "1"
          }
        ],
        "profile_id": "grid_plus_optional_trend",
        "required_evidence": [
          "execution",
          "integrated_oos",
          "mode_attribution",
          "provenance"
        ],
        "selection_families": [
          "grid_only"
        ],
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
        "version": "1"
      },
      "profile_hash": "f4f9eb95055b94fd1694c9f43501573cd2e7eb3f2e5590104fa2a83fd6ebf8b1",
      "start_date": "2021-01-01",
      "target_codes": [
        "588000.SH"
      ]
    },
    "experiment_hash": "c2fe1498a19696d9c4cacce76cbb199a97a2b3cf239541386b4b982c029c50bc",
    "experiment_windows": [
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "1f13464049e52d8111a8b7b843cd0a40dcabaa7151d26e5e7251c22794569b23",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "6131e0381c28481b1fc86e59486e433d1800f68b0e2ae0f04770f49bd0008a96",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
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
            "cost_drag": 0.00142555745,
            "cvar5_improvement": 0.02239466812433637,
            "drawdown_improvement": 0.2062009997868485,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.39670693737710017,
            "sortino_excess": 1.0253082081315605,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017122989999999998,
            "cvar5_improvement": 0.021893369467271228,
            "drawdown_improvement": 0.20136803223666647,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.26073238238446844,
            "sortino_excess": 0.811283726362289,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00207552935,
            "cvar5_improvement": 0.020951528200847107,
            "drawdown_improvement": 0.1939519447625434,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20612649567651392,
            "sortino_excess": 0.3574544865030159,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013170602500000002,
            "cvar5_improvement": 0.02043916423939324,
            "drawdown_improvement": 0.1979230299516726,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.13247248560125444,
            "sortino_excess": 0.7000749779197519,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003030225525,
            "cvar5_improvement": 0.02210027467561946,
            "drawdown_improvement": 0.197867434040969,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.08310118096994157,
            "sortino_excess": 0.6924179064870497,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001516720325,
            "cvar5_improvement": 0.02037261808140034,
            "drawdown_improvement": 0.19721833403184075,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.12425286169266374,
            "sortino_excess": 0.6786974672546985,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00199035585,
            "cvar5_improvement": 0.021551913789831775,
            "drawdown_improvement": 0.1982672412078747,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.257974476935547,
            "sortino_excess": 0.8026233556020201,
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
            "cost_drag": 0.00147686755,
            "cvar5_improvement": 0.02125072654771984,
            "drawdown_improvement": 0.19949306545708892,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.16296826238238676,
            "sortino_excess": 0.7018988151426475,
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
            "cost_drag": 0.0013262807,
            "cvar5_improvement": 0.022565696767384985,
            "drawdown_improvement": 0.20725980660753907,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4297105878129107,
            "sortino_excess": 1.1254973472964465,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00133480915,
            "cvar5_improvement": 0.021391417991073525,
            "drawdown_improvement": 0.20065408587529093,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.19912108394476716,
            "sortino_excess": 0.7940446583574896,
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
            "cost_drag": 0.0018212223499999998,
            "cvar5_improvement": 0.021760742811655617,
            "drawdown_improvement": 0.19961409756790854,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.24387939330185684,
            "sortino_excess": 0.8032586420731913,
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
            "cost_drag": 0.00130744415,
            "cvar5_improvement": 0.02149075407034709,
            "drawdown_improvement": 0.20121941670591484,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.23228947900410052,
            "sortino_excess": 0.8364753099807486,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034096595250000003,
            "cvar5_improvement": 0.022208420360021564,
            "drawdown_improvement": 0.20089527075927033,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.333627888466514,
            "sortino_excess": 0.9822099481386559,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018526609,
            "cvar5_improvement": 0.022067080896021527,
            "drawdown_improvement": 0.20179566517439007,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.25094887038841485,
            "sortino_excess": 0.8342566183024958,
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
                "unit_pct": 0.15
              },
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
            "cost_drag": 0.002312057825,
            "cvar5_improvement": 0.021420957249977186,
            "drawdown_improvement": 0.19535019016952349,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.03918145517020863,
            "sortino_excess": 0.47301660220534353,
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
            "cost_drag": 0.002968878475,
            "cvar5_improvement": 0.022043603585170823,
            "drawdown_improvement": 0.19668147608812303,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.15707912662006698,
            "sortino_excess": 0.8708217937767426,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001529699975,
            "cvar5_improvement": 0.02187194410113488,
            "drawdown_improvement": 0.2016643438741628,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.21335827834607024,
            "sortino_excess": 0.7399106748691047,
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
                "unit_pct": 0.15
              },
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
            "cost_drag": 0.001685402425,
            "cvar5_improvement": 0.02169337365575797,
            "drawdown_improvement": 0.20132621518676896,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.25334996619360184,
            "sortino_excess": 0.8176153346252639,
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
            "cost_drag": 0.001400191725,
            "cvar5_improvement": 0.022002790228910142,
            "drawdown_improvement": 0.2034240818795258,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3045509907635142,
            "sortino_excess": 0.915552323903223,
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
            "cost_drag": 0.001316839975,
            "cvar5_improvement": 0.022121421529504373,
            "drawdown_improvement": 0.2042440217126216,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3266290732168312,
            "sortino_excess": 0.974271068383864,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001830078825,
            "cvar5_improvement": 0.02072088472225658,
            "drawdown_improvement": 0.19667315195416374,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.15643345761960287,
            "sortino_excess": 0.7016938313059631,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018212656750000002,
            "cvar5_improvement": 0.022244425303662246,
            "drawdown_improvement": 0.2012317273402497,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.18809746474479597,
            "sortino_excess": 0.7556108504420361,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00304675815,
            "cvar5_improvement": 0.021623000103589574,
            "drawdown_improvement": 0.20181210460191798,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2050669877166761,
            "sortino_excess": 0.7879773211791041,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.00213816415,
            "cvar5_improvement": 0.021134187772992953,
            "drawdown_improvement": 0.19860222198441607,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.13564349625531924,
            "sortino_excess": 0.6545405258507991,
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
            "cost_drag": 0.0013496688,
            "cvar5_improvement": 0.02046653267985376,
            "drawdown_improvement": 0.19795156492196125,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14100450197213316,
            "sortino_excess": 0.7076102197240564,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00202797085,
            "cvar5_improvement": 0.021127175628054544,
            "drawdown_improvement": 0.196275582603826,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08739965735537752,
            "sortino_excess": 0.44895080356089934,
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
            "cost_drag": 0.00244744555,
            "cvar5_improvement": 0.02082622562320853,
            "drawdown_improvement": 0.19268505845134537,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06238739996683908,
            "sortino_excess": 0.46060743707436985,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014246255999999999,
            "cvar5_improvement": 0.020375047348572074,
            "drawdown_improvement": 0.19735809915458533,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.11485162306123504,
            "sortino_excess": 0.6620873823956259,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026057477749999998,
            "cvar5_improvement": 0.021447322654399546,
            "drawdown_improvement": 0.19806256634692196,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.20862239408719846,
            "sortino_excess": 0.6913497014421495,
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
            "cost_drag": 0.0015821435250000001,
            "cvar5_improvement": 0.02223768096837603,
            "drawdown_improvement": 0.20386641925716548,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2645964655216131,
            "sortino_excess": 0.779161588406985,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015787826000000001,
            "cvar5_improvement": 0.02182114679616615,
            "drawdown_improvement": 0.20196441631291098,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.26493903736677243,
            "sortino_excess": 0.8168146243876342,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.0016387142249999999,
            "cvar5_improvement": 0.022096254354231484,
            "drawdown_improvement": 0.20426241838228235,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.342153673716898,
            "sortino_excess": 0.8822183534632152,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013748174,
            "cvar5_improvement": 0.021395574077395233,
            "drawdown_improvement": 0.2006739351149913,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.21813669043200967,
            "sortino_excess": 0.806094480976787,
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
            "cost_drag": 0.0020336012,
            "cvar5_improvement": 0.02177106925003531,
            "drawdown_improvement": 0.19981812343833158,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2662692344989324,
            "sortino_excess": 0.8436270857139478,
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
                "unit_pct": 0.05
              },
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
            "cost_drag": 0.001458081625,
            "cvar5_improvement": 0.020357051678578583,
            "drawdown_improvement": 0.19746700875909126,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.12893382914360824,
            "sortino_excess": 0.6788326941073471,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00197563565,
            "cvar5_improvement": 0.021814213534168535,
            "drawdown_improvement": 0.1990361921802501,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.17289808648934696,
            "sortino_excess": 0.7344429674209121,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016004357500000001,
            "cvar5_improvement": 0.02124892044961887,
            "drawdown_improvement": 0.19924978909101218,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.18593015457071216,
            "sortino_excess": 0.7449069289206007,
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
            "cost_drag": 0.00135242005,
            "cvar5_improvement": 0.021979775980586903,
            "drawdown_improvement": 0.20340751783845998,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.27312805399755213,
            "sortino_excess": 0.9070190009463241,
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
            "cost_drag": 0.001369715975,
            "cvar5_improvement": 0.022367549670292072,
            "drawdown_improvement": 0.2061532320280376,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3524035281437059,
            "sortino_excess": 1.032448326600215,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00194729455,
            "cvar5_improvement": 0.020831076176236894,
            "drawdown_improvement": 0.19754276816802782,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.09280059041302624,
            "sortino_excess": 0.6152417248460574,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001297882275,
            "cvar5_improvement": 0.020484055975510927,
            "drawdown_improvement": 0.1982090172142877,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.1479833318985045,
            "sortino_excess": 0.7194657730125456,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015182664,
            "cvar5_improvement": 0.021238544389533275,
            "drawdown_improvement": 0.19970734583986702,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.19270307991041696,
            "sortino_excess": 0.7468785312721761,
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
            "cost_drag": 0.001695793025,
            "cvar5_improvement": 0.020820961816536875,
            "drawdown_improvement": 0.19736566099603706,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14887827717739824,
            "sortino_excess": 0.7023205995055942,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002356150675,
            "cvar5_improvement": 0.02107103269091446,
            "drawdown_improvement": 0.19708122911794185,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.13510630539303914,
            "sortino_excess": 0.639792133706859,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.02745219310321083,
          "execution_cost": 155.14305,
          "grid_return": 0.02727400036446369,
          "reconciliation_error": 3.469446951953614e-18,
          "transition_return": 0.0020651799156102824,
          "trend_return": 0.0010250896444069027
        },
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {
          "grid_only": [
            [
              "step_pct",
              "unit_pct"
            ]
          ]
        },
        "selected_scores": {
          "grid_only": {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001400191725,
            "cvar5_improvement": 0.022002790228910142,
            "drawdown_improvement": 0.2034240818795258,
            "exposure_ratio": 0.5079365079365079,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3045509907635142,
            "sortino_excess": 0.915552323903223,
            "stable": true
          }
        },
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
          "policy_id": "full_adaptive",
          "spec_hash": "09b46762ef403fab4bd180b196f9f60138fded696ab47dfcec0b21f3af6e7e9a",
          "strategy_id": "full_adaptive",
          "version": "1"
        },
        "window_id": "wf_000"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "0811a7ce7defbd83af87c94638e3ef01257fc8a8046aef13efac63fb66ed6e5c",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "ea302f29e0fe1f3b6e3584e43b20acfc27da62b195e6250719b19dbe267483ac",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
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
            "cost_drag": 0.00154785825,
            "cvar5_improvement": 0.020704258949657356,
            "drawdown_improvement": 0.14482093331013668,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09165428285396865,
            "sortino_excess": 0.36731955540266276,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017935340250000002,
            "cvar5_improvement": 0.020537586843997813,
            "drawdown_improvement": 0.1430903414516969,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.014674313567766883,
            "sortino_excess": 0.4908374156458547,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002309867925,
            "cvar5_improvement": 0.020224374973664215,
            "drawdown_improvement": 0.14007059822286452,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.13462340137976736,
            "sortino_excess": 0.3618961276087882,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001476100475,
            "cvar5_improvement": 0.01910194351063013,
            "drawdown_improvement": 0.13169382491365877,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.32926723059756857,
            "sortino_excess": 0.1883574785402492,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003540313125,
            "cvar5_improvement": 0.019165648059265784,
            "drawdown_improvement": 0.13231118521764243,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1750603689529622,
            "sortino_excess": 0.351578672903422,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001656150625,
            "cvar5_improvement": 0.019232168708831824,
            "drawdown_improvement": 0.13215250898518388,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2940779470171209,
            "sortino_excess": 0.2511956828799725,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020714702,
            "cvar5_improvement": 0.02017779000417573,
            "drawdown_improvement": 0.13810984505817794,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06129099038952597,
            "sortino_excess": 0.505403667914975,
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
            "cost_drag": 0.00159666785,
            "cvar5_improvement": 0.020015000941799692,
            "drawdown_improvement": 0.136676495742957,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.21895689561648884,
            "sortino_excess": 0.34321965696349144,
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
            "cost_drag": 0.001467555675,
            "cvar5_improvement": 0.020159016688389916,
            "drawdown_improvement": 0.1434051914521737,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09818909677737889,
            "sortino_excess": 0.5023758693415012,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014812585999999998,
            "cvar5_improvement": 0.019754265547214787,
            "drawdown_improvement": 0.1354756416034867,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2819547349288206,
            "sortino_excess": 0.2645631355952574,
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
            "cost_drag": 0.0019507454749999999,
            "cvar5_improvement": 0.020043331475971406,
            "drawdown_improvement": 0.13684835566942824,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.13927616698010467,
            "sortino_excess": 0.44953662607243927,
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
            "cost_drag": 0.001462828775,
            "cvar5_improvement": 0.019614926499856793,
            "drawdown_improvement": 0.13564980871000076,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.24828569622429247,
            "sortino_excess": 0.30672190861789406,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034657387,
            "cvar5_improvement": 0.019294007378610104,
            "drawdown_improvement": 0.13304070255104672,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.25411947315663946,
            "sortino_excess": 0.28462678932381985,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00206351575,
            "cvar5_improvement": 0.020437820244156794,
            "drawdown_improvement": 0.1413222360238212,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.00835042692515195,
            "sortino_excess": 0.5994146311730888,
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
                "unit_pct": 0.15
              },
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
            "cost_drag": 0.0027627314999999998,
            "cvar5_improvement": 0.020077057144743313,
            "drawdown_improvement": 0.14061265167743237,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.023157826746808746,
            "sortino_excess": 0.39192462083334567,
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
            "cost_drag": 0.0036568017250000005,
            "cvar5_improvement": 0.01864157269763366,
            "drawdown_improvement": 0.12934549004256915,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.21255100250711043,
            "sortino_excess": 0.3760996336517669,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016303209499999999,
            "cvar5_improvement": 0.02058414271010147,
            "drawdown_improvement": 0.1411133404978483,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11848880668147223,
            "sortino_excess": 0.4129246289988009,
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
                "unit_pct": 0.15
              },
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
            "cost_drag": 0.0017860234,
            "cvar5_improvement": 0.02040557226472456,
            "drawdown_improvement": 0.14077521181045446,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.07849711883394062,
            "sortino_excess": 0.49062928875496015,
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
            "cost_drag": 0.001534689725,
            "cvar5_improvement": 0.020477883140017018,
            "drawdown_improvement": 0.1405776813299009,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16935069098750938,
            "sortino_excess": 0.38505526765346,
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
            "cost_drag": 0.0014652348,
            "cvar5_improvement": 0.01998314159105669,
            "drawdown_improvement": 0.1395203573017494,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.17639262459519275,
            "sortino_excess": 0.4082000413847606,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019376495750000001,
            "cvar5_improvement": 0.019345595668820242,
            "drawdown_improvement": 0.13289853137788263,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23725307190979306,
            "sortino_excess": 0.30273666572834357,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002061360825,
            "cvar5_improvement": 0.020598323613213364,
            "drawdown_improvement": 0.14306439973487436,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.050507664818204706,
            "sortino_excess": 0.536935971313923,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0031156954,
            "cvar5_improvement": 0.019518145282127204,
            "drawdown_improvement": 0.13428058707571325,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2999178290111342,
            "sortino_excess": 0.1908738728423185,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.002191732675,
            "cvar5_improvement": 0.020028503107195065,
            "drawdown_improvement": 0.13875963871626426,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16503343238290075,
            "sortino_excess": 0.39904027468049397,
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
            "cost_drag": 0.00150858555,
            "cvar5_improvement": 0.019211433989899232,
            "drawdown_improvement": 0.13213504554553093,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3114503529478581,
            "sortino_excess": 0.2425112295756195,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002238567175,
            "cvar5_improvement": 0.02023146510596426,
            "drawdown_improvement": 0.13996388779083935,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.13737720296830652,
            "sortino_excess": 0.36361206460687695,
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
            "cost_drag": 0.00296159355,
            "cvar5_improvement": 0.019629089177326878,
            "drawdown_improvement": 0.13873235922415073,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.04852266664200698,
            "sortino_excess": 0.43927111865137575,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015640558999999998,
            "cvar5_improvement": 0.019234597976003562,
            "drawdown_improvement": 0.13229227410792846,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.30347918564854964,
            "sortino_excess": 0.23458559802089998,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0028179666500000003,
            "cvar5_improvement": 0.02000847358437214,
            "drawdown_improvement": 0.1392748215983587,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08209207735018186,
            "sortino_excess": 0.3881570074258854,
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
            "cost_drag": 0.0016633785500000003,
            "cvar5_improvement": 0.02088189834510262,
            "drawdown_improvement": 0.14558872847219592,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.010810230430622236,
            "sortino_excess": 0.45871527769055065,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016316202,
            "cvar5_improvement": 0.0203604394870884,
            "drawdown_improvement": 0.1394575051233021,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.21903495627853486,
            "sortino_excess": 0.3566350878394584,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.0016645485,
            "cvar5_improvement": 0.020588443144016345,
            "drawdown_improvement": 0.1433474105882388,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.15757133581134675,
            "sortino_excess": 0.3700780967749552,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00152142435,
            "cvar5_improvement": 0.019961809705705637,
            "drawdown_improvement": 0.13632093682846813,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.245370588428043,
            "sortino_excess": 0.34375306151500223,
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
            "cost_drag": 0.002207582125,
            "cvar5_improvement": 0.020591071433528094,
            "drawdown_improvement": 0.1430532856847912,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14193102656256879,
            "sortino_excess": 0.6514775191057249,
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
                "unit_pct": 0.05
              },
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
            "cost_drag": 0.0015653853749999999,
            "cvar5_improvement": 0.0191736859959661,
            "drawdown_improvement": 0.1317630724056882,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.32676911465811137,
            "sortino_excess": 0.14764804997987316,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002170387675,
            "cvar5_improvement": 0.020810755445382433,
            "drawdown_improvement": 0.14451962397522147,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14462328460529594,
            "sortino_excess": 0.6084090297365224,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00172023605,
            "cvar5_improvement": 0.020013194843698727,
            "drawdown_improvement": 0.13643321937688027,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19599500342816345,
            "sortino_excess": 0.3862277707414447,
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
            "cost_drag": 0.001486824175,
            "cvar5_improvement": 0.020190493745253637,
            "drawdown_improvement": 0.1392574961676345,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2277426362332616,
            "sortino_excess": 0.3452646535357859,
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
            "cost_drag": 0.0014923163500000002,
            "cvar5_improvement": 0.02043191138928134,
            "drawdown_improvement": 0.14306604496398098,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16621807896801283,
            "sortino_excess": 0.42255876878385124,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002034247225,
            "cvar5_improvement": 0.01961075064733957,
            "drawdown_improvement": 0.1339515265733323,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.29034348851131014,
            "sortino_excess": 0.23600646982409723,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014607274750000003,
            "cvar5_improvement": 0.019034072428057356,
            "drawdown_improvement": 0.13178251537424365,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.31263053412494857,
            "sortino_excess": 0.20916135563908353,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015982448250000001,
            "cvar5_improvement": 0.01988213651207931,
            "drawdown_improvement": 0.13556695798391788,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27757750558874367,
            "sortino_excess": 0.267123995419973,
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
            "cost_drag": 0.0018398086,
            "cvar5_improvement": 0.01927893700190055,
            "drawdown_improvement": 0.13230651411084277,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.26807248338579637,
            "sortino_excess": 0.27157694840949875,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025328331,
            "cvar5_improvement": 0.019665071248236188,
            "drawdown_improvement": 0.13419658552618993,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.256333850120006,
            "sortino_excess": 0.22289694084685677,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.19760980059256883,
          "execution_cost": 98.5301,
          "grid_return": -0.08391723657438065,
          "reconciliation_error": -5.551115123125783e-17,
          "transition_return": -0.18194118287024247,
          "trend_return": -0.015929512991155463
        },
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {
          "grid_only": [
            [
              "step_pct",
              "unit_pct"
            ]
          ]
        },
        "selected_scores": {
          "grid_only": {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002207582125,
            "cvar5_improvement": 0.020591071433528094,
            "drawdown_improvement": 0.1430532856847912,
            "exposure_ratio": 0.5099206349206349,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14193102656256879,
            "sortino_excess": 0.6514775191057249,
            "stable": true
          }
        },
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
          "policy_id": "full_adaptive",
          "spec_hash": "44f728f89b5e3024f86c94e44518bfaf1ea28ce504fc285737af24991859864e",
          "strategy_id": "full_adaptive",
          "version": "1"
        },
        "window_id": "wf_001"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "e0c69661fe5bf2a4a6daad0383446692f4bfbaf78d66cf402ca517c24373c774",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "c460ab0a8c4386b12527408fc386abbf68ffb20f7d67c008cde0f07c827cec1e",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
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
            "cost_drag": 0.0018825634750000001,
            "cvar5_improvement": 0.02317323857180166,
            "drawdown_improvement": 0.119926557854239,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5387564882052718,
            "sortino_excess": 0.5260093467752651,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00231882685,
            "cvar5_improvement": 0.02192810616620479,
            "drawdown_improvement": 0.11758568837925859,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6527547624444885,
            "sortino_excess": -0.10684289650766898,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0030110607500000003,
            "cvar5_improvement": 0.021668061239799478,
            "drawdown_improvement": 0.11054534442878752,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6721575658105122,
            "sortino_excess": -0.4276768705049291,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017804711499999999,
            "cvar5_improvement": 0.020349249558413655,
            "drawdown_improvement": 0.10516659549217697,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.784607539443861,
            "sortino_excess": -0.5334906793678831,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00459535075,
            "cvar5_improvement": 0.021222829960498492,
            "drawdown_improvement": 0.10865663089991365,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5489558593838741,
            "sortino_excess": 0.17188285711145868,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002024774775,
            "cvar5_improvement": 0.02013227354744889,
            "drawdown_improvement": 0.10487142019593701,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.8125830920988315,
            "sortino_excess": -0.645573482032219,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002502128075,
            "cvar5_improvement": 0.021528782153431292,
            "drawdown_improvement": 0.10926149330376583,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6852078543263426,
            "sortino_excess": -0.5050567859002667,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00189939965,
            "cvar5_improvement": 0.021350030797287384,
            "drawdown_improvement": 0.10818861781126721,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7586858629708565,
            "sortino_excess": -0.3473932649431583,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017927974,
            "cvar5_improvement": 0.02277032604677329,
            "drawdown_improvement": 0.12104174700013048,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.44117054503967446,
            "sortino_excess": 0.5525735015256095,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018126230000000002,
            "cvar5_improvement": 0.021598098223675963,
            "drawdown_improvement": 0.11029873049298744,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6884698110884326,
            "sortino_excess": -0.15853384607248971,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002366283875,
            "cvar5_improvement": 0.021751257152876527,
            "drawdown_improvement": 0.11122036678836952,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6620514080161094,
            "sortino_excess": -0.4068382499683191,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001748548475,
            "cvar5_improvement": 0.021464586410358213,
            "drawdown_improvement": 0.11050340306671566,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6774683184021839,
            "sortino_excess": -0.19082659322917322,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00418354835,
            "cvar5_improvement": 0.021263583933322915,
            "drawdown_improvement": 0.10843611225105423,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6312787771277959,
            "sortino_excess": -0.1276334455339943,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002522328875,
            "cvar5_improvement": 0.022359854720137715,
            "drawdown_improvement": 0.11688587243774348,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5336008122191209,
            "sortino_excess": -0.2716684532697351,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003785638725,
            "cvar5_improvement": 0.02183425622412742,
            "drawdown_improvement": 0.11437657175351243,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5137225096311169,
            "sortino_excess": 0.15594906587041651,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0048936697000000005,
            "cvar5_improvement": 0.02126589123468854,
            "drawdown_improvement": 0.1090706653838561,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5077966885430365,
            "sortino_excess": 0.24931900093641784,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019603374500000003,
            "cvar5_improvement": 0.022133140966752847,
            "drawdown_improvement": 0.11230006647253096,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6902873599577277,
            "sortino_excess": -0.07298726873790429,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00225921595,
            "cvar5_improvement": 0.0217915164544273,
            "drawdown_improvement": 0.11467620984838425,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6658489804386568,
            "sortino_excess": -0.2109576932600158,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018464879250000002,
            "cvar5_improvement": 0.0225453463294201,
            "drawdown_improvement": 0.11496111657055916,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6371503709264376,
            "sortino_excess": 0.19965424610644916,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001770093325,
            "cvar5_improvement": 0.02226802695555919,
            "drawdown_improvement": 0.11579531433674778,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.563918756113309,
            "sortino_excess": 0.2143406016383188,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002317910925,
            "cvar5_improvement": 0.020503344778466846,
            "drawdown_improvement": 0.10457881408611797,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7878963005605589,
            "sortino_excess": -0.6677287642290989,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002435334825,
            "cvar5_improvement": 0.022663535073218333,
            "drawdown_improvement": 0.11972724436022306,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6147800988544727,
            "sortino_excess": -0.5118767929890364,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0037223953500000006,
            "cvar5_improvement": 0.02090725868623475,
            "drawdown_improvement": 0.10607688334062115,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.728089862922712,
            "sortino_excess": -0.4866251989022172,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.002780632025,
            "cvar5_improvement": 0.021431199573374436,
            "drawdown_improvement": 0.10965491688507803,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6492138632841334,
            "sortino_excess": -0.40978354748458073,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00177991435,
            "cvar5_improvement": 0.02036457020679743,
            "drawdown_improvement": 0.10500237832597786,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.8015987559606156,
            "sortino_excess": -0.5547513987639543,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0029039058249999998,
            "cvar5_improvement": 0.021652328517022014,
            "drawdown_improvement": 0.11010379479637866,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6702427032900675,
            "sortino_excess": -0.36394254233187673,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004037664575,
            "cvar5_improvement": 0.021856788263564637,
            "drawdown_improvement": 0.11591984231614633,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4593055713949107,
            "sortino_excess": 0.2659976404917365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001841735,
            "cvar5_improvement": 0.020178343813506184,
            "drawdown_improvement": 0.10411722425555961,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.8175954871705282,
            "sortino_excess": -0.6099016249888684,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0035507705750000003,
            "cvar5_improvement": 0.02169214230557704,
            "drawdown_improvement": 0.11253661351440253,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5521890068571865,
            "sortino_excess": -0.10699825304151694,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002021239275,
            "cvar5_improvement": 0.022715042346256677,
            "drawdown_improvement": 0.11641303039188527,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.61351408477832,
            "sortino_excess": 0.1169133518991835,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001883480075,
            "cvar5_improvement": 0.02254474797353676,
            "drawdown_improvement": 0.11478601866881147,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6430030142373837,
            "sortino_excess": 0.1886247370904257,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00192782655,
            "cvar5_improvement": 0.023175499047549616,
            "drawdown_improvement": 0.11972466375435625,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5460513758158358,
            "sortino_excess": 0.5122127118678422,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001811636675,
            "cvar5_improvement": 0.021623933533076095,
            "drawdown_improvement": 0.10992946669766765,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7255478021875342,
            "sortino_excess": -0.20605167426364662,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00266046675,
            "cvar5_improvement": 0.022136205091654083,
            "drawdown_improvement": 0.11399116223977476,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5829955613615871,
            "sortino_excess": -0.4417093375127952,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00179987945,
            "cvar5_improvement": 0.020365228352711238,
            "drawdown_improvement": 0.10495036304179214,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.8037310848738382,
            "sortino_excess": -0.558551798716015,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002596517425,
            "cvar5_improvement": 0.02247630992571814,
            "drawdown_improvement": 0.11653321331402908,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.675425150230121,
            "sortino_excess": -0.7183466417579,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002141468925,
            "cvar5_improvement": 0.02124084391260023,
            "drawdown_improvement": 0.10972530776612921,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7453739199276532,
            "sortino_excess": -0.432717990562307,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018478556499999998,
            "cvar5_improvement": 0.0224747557679828,
            "drawdown_improvement": 0.115508905131357,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5773774441833734,
            "sortino_excess": 0.2758625193297477,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018844399000000002,
            "cvar5_improvement": 0.023039754629396475,
            "drawdown_improvement": 0.1206368640726177,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4557237525798479,
            "sortino_excess": 0.6263741011385467,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002543260075,
            "cvar5_improvement": 0.020651258268408766,
            "drawdown_improvement": 0.10507805339124651,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.776399758853374,
            "sortino_excess": -0.6257243243663522,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001729829325,
            "cvar5_improvement": 0.020282472851305078,
            "drawdown_improvement": 0.10526442437010591,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.778605494758525,
            "sortino_excess": -0.5486635656012055,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018400321500000002,
            "cvar5_improvement": 0.02162818544115951,
            "drawdown_improvement": 0.10983766146199375,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7295071342031051,
            "sortino_excess": -0.21348091243172135,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002212174525,
            "cvar5_improvement": 0.020588390787383202,
            "drawdown_improvement": 0.1055566517260822,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7767036784653877,
            "sortino_excess": -0.639861088834931,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0031520736249999997,
            "cvar5_improvement": 0.02079007329031996,
            "drawdown_improvement": 0.10635474404086126,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7431703284850099,
            "sortino_excess": -0.5347019334449621,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.00084408186778368,
          "execution_cost": 195.56581,
          "grid_return": 0.0018117515432506583,
          "reconciliation_error": 8.326672684688674e-17,
          "transition_return": 0.0012035267953259383,
          "trend_return": -0.13935053830981795
        },
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {
          "grid_only": [
            [
              "step_pct",
              "unit_pct"
            ]
          ]
        },
        "selected_scores": {
          "grid_only": {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017927974,
            "cvar5_improvement": 0.02277032604677329,
            "drawdown_improvement": 0.12104174700013048,
            "exposure_ratio": 0.5873015873015873,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.44117054503967446,
            "sortino_excess": 0.5525735015256095,
            "stable": false
          }
        },
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
          "policy_id": "full_adaptive",
          "spec_hash": "67cf3d971b8b0764fbf7bb7a7ff2e309cedad7648cadc7c4ec8c1c5ab5dc53f9",
          "strategy_id": "full_adaptive",
          "version": "1"
        },
        "window_id": "wf_002"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "e0c69661fe5bf2a4a6daad0383446692f4bfbaf78d66cf402ca517c24373c774",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "c460ab0a8c4386b12527408fc386abbf68ffb20f7d67c008cde0f07c827cec1e",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
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
            "cost_drag": 0.002030889875,
            "cvar5_improvement": 0.024356107598526258,
            "drawdown_improvement": 0.10508653798742473,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.3246041189037014,
            "sortino_excess": -0.5972876510232532,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024604162,
            "cvar5_improvement": 0.023235737584659043,
            "drawdown_improvement": 0.1026185003096137,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4964544973483391,
            "sortino_excess": -1.3057055970548155,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0032976324,
            "cvar5_improvement": 0.02287960175965463,
            "drawdown_improvement": 0.09395831062003407,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4544863652739408,
            "sortino_excess": -1.5597421607240989,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001917062775,
            "cvar5_improvement": 0.022310306102336353,
            "drawdown_improvement": 0.09713302127884985,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1273398044936498,
            "sortino_excess": -0.7459335026646639,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00489132465,
            "cvar5_improvement": 0.020889011798610288,
            "drawdown_improvement": 0.08244997139949567,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.6911249888988293,
            "sortino_excess": -1.2632570259313591,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00214215255,
            "cvar5_improvement": 0.022085036176038575,
            "drawdown_improvement": 0.09626646075557371,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.201537256106479,
            "sortino_excess": -0.9925515986379546,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026183255500000003,
            "cvar5_improvement": 0.02286169379448178,
            "drawdown_improvement": 0.09633379525158722,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.6030155100169452,
            "sortino_excess": -1.7905424823884217,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020491005749999998,
            "cvar5_improvement": 0.023063259555835852,
            "drawdown_improvement": 0.0978511336955663,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2800114220018628,
            "sortino_excess": -1.0567951576491288,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001939306425,
            "cvar5_improvement": 0.024087349979184665,
            "drawdown_improvement": 0.10646784969034867,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2064592064331245,
            "sortino_excess": -0.49514103401358717,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019710559,
            "cvar5_improvement": 0.023341814936154188,
            "drawdown_improvement": 0.10003594966424947,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1205793819814642,
            "sortino_excess": -0.5939991686619311,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002444471025,
            "cvar5_improvement": 0.023148103348691176,
            "drawdown_improvement": 0.09845473951044553,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4189180365346243,
            "sortino_excess": -1.4811699183475238,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001906809,
            "cvar5_improvement": 0.02320780956344647,
            "drawdown_improvement": 0.1003334158842849,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1160890530306025,
            "sortino_excess": -0.6310021021041528,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004416659900000001,
            "cvar5_improvement": 0.021437048196330914,
            "drawdown_improvement": 0.08583836802053652,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.8387543178498418,
            "sortino_excess": -1.625717501483495,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025607281,
            "cvar5_improvement": 0.023508280967123985,
            "drawdown_improvement": 0.10062378492565249,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.520570300300119,
            "sortino_excess": -1.642199117013932,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004124501375,
            "cvar5_improvement": 0.022704250666692315,
            "drawdown_improvement": 0.096285654876923,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.5764809819325858,
            "sortino_excess": -1.2758158165154403,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0052198059,
            "cvar5_improvement": 0.020497628312102275,
            "drawdown_improvement": 0.08036233081115302,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.5591417848672595,
            "sortino_excess": -1.1159315005697146,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00207924695,
            "cvar5_improvement": 0.023526037306617696,
            "drawdown_improvement": 0.09967323727514962,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4775180030438557,
            "sortino_excess": -1.2061460737646457,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002360573325,
            "cvar5_improvement": 0.02308802857317662,
            "drawdown_improvement": 0.10046867460713049,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.5485579761349402,
            "sortino_excess": -1.4545153057630982,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00200339205,
            "cvar5_improvement": 0.023939467442318993,
            "drawdown_improvement": 0.10240347247008541,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.3714034524018126,
            "sortino_excess": -0.8542822281815178,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019263818,
            "cvar5_improvement": 0.023733149977208663,
            "drawdown_improvement": 0.103409571552941,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1651136181195156,
            "sortino_excess": -0.5788669548968632,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002452566125,
            "cvar5_improvement": 0.02241587391649946,
            "drawdown_improvement": 0.09521585092106502,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2741228345894025,
            "sortino_excess": -1.2660458679088937,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025639950750000005,
            "cvar5_improvement": 0.0238154485709661,
            "drawdown_improvement": 0.10284547523948653,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.5431114936565251,
            "sortino_excess": -1.8123422519303942,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0039283303,
            "cvar5_improvement": 0.021673689716070928,
            "drawdown_improvement": 0.08970361443195932,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.7150689488137527,
            "sortino_excess": -1.8194714181447114,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.002941671275,
            "cvar5_improvement": 0.022630245872408736,
            "drawdown_improvement": 0.09418115281828249,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.6375640298236207,
            "sortino_excess": -1.7518866024421724,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019328536249999999,
            "cvar5_improvement": 0.022394271829103758,
            "drawdown_improvement": 0.09694446143384125,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1611170723263449,
            "sortino_excess": -0.8509736765183215,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.003163229625,
            "cvar5_improvement": 0.022855507354320796,
            "drawdown_improvement": 0.09404833134240245,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.5617728021452693,
            "sortino_excess": -1.6062286615245605,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00438260355,
            "cvar5_improvement": 0.02262348769602053,
            "drawdown_improvement": 0.09713673450448393,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4148100575752445,
            "sortino_excess": -1.0631818715983932,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001974597425,
            "cvar5_improvement": 0.022208626893025222,
            "drawdown_improvement": 0.09602267407739806,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1842655914533795,
            "sortino_excess": -0.9263334351915912,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0037822554750000003,
            "cvar5_improvement": 0.022693364052369637,
            "drawdown_improvement": 0.09557895030955782,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.717765577465264,
            "sortino_excess": -1.6485459998611156,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0021228635,
            "cvar5_improvement": 0.023866784946978248,
            "drawdown_improvement": 0.10146834412475236,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4232376277647134,
            "sortino_excess": -1.0438315392096869,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00200339205,
            "cvar5_improvement": 0.023939467442318993,
            "drawdown_improvement": 0.10240347247008541,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.3714034524018126,
            "sortino_excess": -0.8542822281815178,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002030889875,
            "cvar5_improvement": 0.024356107598526258,
            "drawdown_improvement": 0.10508653798742473,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.3246041189037014,
            "sortino_excess": -0.5972876510232532,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019904631,
            "cvar5_improvement": 0.023341814936154188,
            "drawdown_improvement": 0.09965359264188564,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2244472911362063,
            "sortino_excess": -0.8596662329234008,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027439716750000003,
            "cvar5_improvement": 0.023186945250277403,
            "drawdown_improvement": 0.09743790881416386,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.6195973850874195,
            "sortino_excess": -1.8633329786793147,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019328536249999999,
            "cvar5_improvement": 0.022394271829103758,
            "drawdown_improvement": 0.09694446143384125,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1611170723263449,
            "sortino_excess": -0.8509736765183215,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027245979749999996,
            "cvar5_improvement": 0.023479152696186098,
            "drawdown_improvement": 0.09860626014423501,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.6591719179408961,
            "sortino_excess": -2.083353021523068,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002274290425,
            "cvar5_improvement": 0.0227979524866432,
            "drawdown_improvement": 0.09835009452813845,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.321282581189893,
            "sortino_excess": -1.2164872491395378,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020040993,
            "cvar5_improvement": 0.023939467442318993,
            "drawdown_improvement": 0.10298341056742102,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1673730607156418,
            "sortino_excess": -0.508839459233899,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020312069,
            "cvar5_improvement": 0.02435611167005411,
            "drawdown_improvement": 0.10585857597872878,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2044224218131427,
            "sortino_excess": -0.40925802329262234,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002754719825,
            "cvar5_improvement": 0.02219348727369521,
            "drawdown_improvement": 0.0942030789781276,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.3046802450031239,
            "sortino_excess": -1.3281996845222348,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018661497,
            "cvar5_improvement": 0.02224567592906012,
            "drawdown_improvement": 0.09728578382146205,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1243529519255044,
            "sortino_excess": -0.7624313474744806,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019904631,
            "cvar5_improvement": 0.023341814936154188,
            "drawdown_improvement": 0.09965359264188564,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2244472911362063,
            "sortino_excess": -0.8596662329234008,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002299154725,
            "cvar5_improvement": 0.022503718003648133,
            "drawdown_improvement": 0.09628680413216065,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2163295564212078,
            "sortino_excess": -1.1131869594644663,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034428387,
            "cvar5_improvement": 0.02224451241063772,
            "drawdown_improvement": 0.09470036577467064,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4813129289015166,
            "sortino_excess": -1.5878500776792723,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": 0.022119326797903585,
          "execution_cost": 104.59175,
          "grid_return": -0.052988146930532366,
          "reconciliation_error": 6.938893903907228e-17,
          "transition_return": -0.011929237247010727,
          "trend_return": -0.05538027165306391
        },
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {
          "grid_only": [
            [
              "step_pct",
              "unit_pct"
            ]
          ]
        },
        "selected_scores": {
          "grid_only": {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001939306425,
            "cvar5_improvement": 0.024087349979184665,
            "drawdown_improvement": 0.10646784969034867,
            "exposure_ratio": 0.6607142857142857,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2064592064331245,
            "sortino_excess": -0.49514103401358717,
            "stable": false
          }
        },
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
          "policy_id": "full_adaptive",
          "spec_hash": "67cf3d971b8b0764fbf7bb7a7ff2e309cedad7648cadc7c4ec8c1c5ab5dc53f9",
          "strategy_id": "full_adaptive",
          "version": "1"
        },
        "window_id": "wf_003"
      },
      {
        "benchmark_specs": [
          {
            "benchmark_id": "buy_and_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "5d7b449757ca7dbd57c3ee5a4c95d62f78d6beedb2e17b443075ede73c27a8df",
            "rebalance_sessions": null,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "target_weight": 1.0,
            "version": "1"
          },
          {
            "benchmark_id": "fixed_half_hold",
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "provenance_hash": "826f1361061e7b08ab053867a00259ecc2d5c02ebdca1f254f98f4edd2c4dd89",
            "rebalance_sessions": 1,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "target_weight": 0.5,
            "version": "1"
          }
        ],
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
            "cost_drag": 0.00186627025,
            "cvar5_improvement": 0.026498017395971532,
            "drawdown_improvement": 0.08780911067438327,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6945099446341638,
            "sortino_excess": -0.07661735204294012,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00226151465,
            "cvar5_improvement": 0.025460395898274098,
            "drawdown_improvement": 0.08533938148864004,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.0304803241232694,
            "sortino_excess": -1.071389603083627,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002875767825,
            "cvar5_improvement": 0.025788206569485862,
            "drawdown_improvement": 0.08436329844016816,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.122141688469341,
            "sortino_excess": -1.515016804874569,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017951311000000002,
            "cvar5_improvement": 0.023695676111506237,
            "drawdown_improvement": 0.07717161679065834,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5635611423855867,
            "sortino_excess": -0.33483191072343993,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0045232131750000005,
            "cvar5_improvement": 0.02339866589509295,
            "drawdown_improvement": 0.07384428645236821,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1985278556434082,
            "sortino_excess": -1.0991134835677503,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00208563005,
            "cvar5_improvement": 0.02409399534590235,
            "drawdown_improvement": 0.07918829130411364,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6219148046314188,
            "sortino_excess": -0.5448280177573541,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025709477249999998,
            "cvar5_improvement": 0.02570600231496604,
            "drawdown_improvement": 0.08496871304853976,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.017250277121692,
            "sortino_excess": -1.3409924115102234,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001947681575,
            "cvar5_improvement": 0.02548529169134004,
            "drawdown_improvement": 0.08211974908207081,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6265725774492013,
            "sortino_excess": -0.43623646455405307,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018447388749999998,
            "cvar5_improvement": 0.02650163649860226,
            "drawdown_improvement": 0.08927099038865105,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6301641674788853,
            "sortino_excess": -0.014789605750223977,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018705376,
            "cvar5_improvement": 0.025354727737264847,
            "drawdown_improvement": 0.08197193092301322,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5109682014812068,
            "sortino_excess": -0.06310463426150936,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002352809675,
            "cvar5_improvement": 0.025981383898942244,
            "drawdown_improvement": 0.08751971168893319,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.8025210449823672,
            "sortino_excess": -0.9588827443110053,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001825473575,
            "cvar5_improvement": 0.02535152642695076,
            "drawdown_improvement": 0.0826667489040675,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5190243295173022,
            "sortino_excess": -0.11305008246562187,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00428993775,
            "cvar5_improvement": 0.024051034328635167,
            "drawdown_improvement": 0.07748702295350446,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.2095007999621108,
            "sortino_excess": -1.2487381122295882,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002354496125,
            "cvar5_improvement": 0.026209911156919834,
            "drawdown_improvement": 0.08789290979676351,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.0472252883861228,
            "sortino_excess": -1.3634029742510412,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0037255694,
            "cvar5_improvement": 0.02479389228521356,
            "drawdown_improvement": 0.08316424072885326,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.145832569734632,
            "sortino_excess": -1.0840233016185665,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004667006625,
            "cvar5_improvement": 0.023008753954338372,
            "drawdown_improvement": 0.07109134237555267,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1581048156906533,
            "sortino_excess": -1.1081172701273183,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019393803500000002,
            "cvar5_improvement": 0.025809442333006513,
            "drawdown_improvement": 0.08494827593989179,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.822445799357588,
            "sortino_excess": -0.63020748211122,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002229131025,
            "cvar5_improvement": 0.02547658351252201,
            "drawdown_improvement": 0.08565952532493251,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.0137920947527377,
            "sortino_excess": -1.1076868542204483,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001888039675,
            "cvar5_improvement": 0.02627433561234204,
            "drawdown_improvement": 0.08684680232223835,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6907554006991736,
            "sortino_excess": -0.2108020632364433,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00186951485,
            "cvar5_improvement": 0.02621990838601153,
            "drawdown_improvement": 0.08794930181910204,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5288997696709019,
            "sortino_excess": 0.023688847272987257,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002389442975,
            "cvar5_improvement": 0.02467527291904583,
            "drawdown_improvement": 0.07911235573603476,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.720494594308021,
            "sortino_excess": -0.8434707578458622,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022727177,
            "cvar5_improvement": 0.026296782410933986,
            "drawdown_improvement": 0.08822540191018213,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1525366512571387,
            "sortino_excess": -1.6400386228332808,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003995475125,
            "cvar5_improvement": 0.024150377396020155,
            "drawdown_improvement": 0.0764701463476076,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.0606875376124836,
            "sortino_excess": -1.266126281971785,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
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
            "cost_drag": 0.002766986,
            "cvar5_improvement": 0.02556112252219395,
            "drawdown_improvement": 0.08551817530685876,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1101704685720795,
            "sortino_excess": -1.4126026943306746,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017905417,
            "cvar5_improvement": 0.023778626713760728,
            "drawdown_improvement": 0.07717161679065834,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.589635795004359,
            "sortino_excess": -0.4302129881676428,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002809048475,
            "cvar5_improvement": 0.025727180563355424,
            "drawdown_improvement": 0.08517657424193137,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.1562438881789046,
            "sortino_excess": -1.4523682152465989,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0038997459250000002,
            "cvar5_improvement": 0.024537539865930963,
            "drawdown_improvement": 0.08247796738208257,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.0466250230788936,
            "sortino_excess": -0.9827472700650567,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018587875500000002,
            "cvar5_improvement": 0.023884126992289548,
            "drawdown_improvement": 0.0772069697692069,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6006901697330699,
            "sortino_excess": -0.47218637334488534,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0036241607499999996,
            "cvar5_improvement": 0.025023140275184628,
            "drawdown_improvement": 0.08401694106738897,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.133534769496315,
            "sortino_excess": -1.2397858301461295,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001915196275,
            "cvar5_improvement": 0.0259543234601989,
            "drawdown_improvement": 0.08433185364899495,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.862536947182683,
            "sortino_excess": -0.6306230660662733,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001898164125,
            "cvar5_improvement": 0.026120520946430185,
            "drawdown_improvement": 0.08690657939307897,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6880273110073887,
            "sortino_excess": -0.21273857916001288,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00186495165,
            "cvar5_improvement": 0.02627939956375908,
            "drawdown_improvement": 0.08694944793836781,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7369971536126555,
            "sortino_excess": -0.1296191783559919,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018614080000000002,
            "cvar5_improvement": 0.025426482190931174,
            "drawdown_improvement": 0.08197193092301322,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5969733456215944,
            "sortino_excess": -0.3067451757793708,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00249260005,
            "cvar5_improvement": 0.02590574056742959,
            "drawdown_improvement": 0.0841164456733609,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.255478378130511,
            "sortino_excess": -1.7312122926970581,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001836560375,
            "cvar5_improvement": 0.02403441327304081,
            "drawdown_improvement": 0.07786486018925512,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5704776328654441,
            "sortino_excess": -0.3837817725965125,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002425158925,
            "cvar5_improvement": 0.0259940891570106,
            "drawdown_improvement": 0.08319156363079577,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -1.4032227994241964,
            "sortino_excess": -2.060199503715011,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022406001500000004,
            "cvar5_improvement": 0.025351319720357153,
            "drawdown_improvement": 0.0858719482223467,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6786445038290246,
            "sortino_excess": -0.6615658327884246,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001925213175,
            "cvar5_improvement": 0.026215843199371567,
            "drawdown_improvement": 0.08684680232223835,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5153280319766426,
            "sortino_excess": 0.10482818251386344,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001910644275,
            "cvar5_improvement": 0.026498017395971532,
            "drawdown_improvement": 0.08780911067438327,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6079565462731924,
            "sortino_excess": 0.08464946505056614,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002645926275,
            "cvar5_improvement": 0.02474994673066326,
            "drawdown_improvement": 0.08067777502736409,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7281265752007875,
            "sortino_excess": -0.8657744277590926,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001760037025,
            "cvar5_improvement": 0.023696330542516936,
            "drawdown_improvement": 0.07752091847623085,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5672082461870772,
            "sortino_excess": -0.36070952901859693,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019160615,
            "cvar5_improvement": 0.025693874478556516,
            "drawdown_improvement": 0.08343743042291371,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5536389930251655,
            "sortino_excess": -0.20053031485881534,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022017801250000003,
            "cvar5_improvement": 0.024682597600515853,
            "drawdown_improvement": 0.08036551970678532,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6494791196751214,
            "sortino_excess": -0.6775814075294706,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003428918425,
            "cvar5_improvement": 0.02471992452376048,
            "drawdown_improvement": 0.08102303028573576,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.8362490161195464,
            "sortino_excess": -1.003373931514388,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.06805058460070076,
          "execution_cost": 161.96304,
          "grid_return": 0.022038952395328708,
          "reconciliation_error": 0.0,
          "transition_return": -0.0006004022852506841,
          "trend_return": -0.19415596756912398
        },
        "execution_cost_config": {
          "commission_rate": 0.0001,
          "minimum_commission": 5.0,
          "sell_tax_rate": 0.0,
          "slippage_bps": 3.0,
          "transfer_fee_rate": 0.0
        },
        "screened_axes": {
          "grid_only": [
            [
              "step_pct",
              "unit_pct"
            ]
          ]
        },
        "selected_scores": {
          "grid_only": {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001925213175,
            "cvar5_improvement": 0.026215843199371567,
            "drawdown_improvement": 0.08684680232223835,
            "exposure_ratio": 0.6567460317460317,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5153280319766426,
            "sortino_excess": 0.10482818251386344,
            "stable": false
          }
        },
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
          "policy_id": "full_adaptive",
          "spec_hash": "da0f198549720c158e876cc7c2efbb0cbcd4cebfb225f5c37d7359a2334518ff",
          "strategy_id": "full_adaptive",
          "version": "1"
        },
        "window_id": "wf_004"
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
    "trade_points": [
      {
        "event_date": "2024-02-28",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 10400,
        "raw_price": 0.8362508
      },
      {
        "event_date": "2024-03-04",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 9000,
        "raw_price": 0.8572571
      },
      {
        "event_date": "2024-03-22",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 19400,
        "raw_price": 0.8417474
      },
      {
        "event_date": "2024-04-29",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 63200,
        "raw_price": 0.790237
      },
      {
        "event_date": "2024-05-27",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 63200,
        "raw_price": 0.759772
      },
      {
        "event_date": "2024-06-05",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 62100,
        "raw_price": 0.7882364000000001
      },
      {
        "event_date": "2024-06-26",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 62100,
        "raw_price": 0.7507747
      },
      {
        "event_date": "2024-07-23",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 60800,
        "raw_price": 0.7862358
      },
      {
        "event_date": "2024-07-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 18700,
        "raw_price": 0.7432229
      },
      {
        "event_date": "2024-08-06",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 79500,
        "raw_price": 0.7467759
      }
    ],
    "by_reason": {
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 10400,
        "traded_value": "8697.0083200"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 1,
        "shares": 9000,
        "traded_value": "7715.3139000"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 19400,
        "traded_value": "16329.8995600"
      },
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 186100,
        "traded_value": "146695.5954800000062100"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 204800,
        "traded_value": "154009.3833200"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 18700,
        "traded_value": "13898.2682300"
      }
    },
    "invested_sessions": 58,
    "cash_sessions": 68,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_001",
    "trade_points": [
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 13200,
        "raw_price": 0.850255
      },
      {
        "event_date": "2024-10-08",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4800,
        "raw_price": 1.140342
      },
      {
        "event_date": "2024-10-11",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 18000,
        "raw_price": 0.9997
      },
      {
        "event_date": "2025-01-15",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 49100,
        "raw_price": 1.0313093
      },
      {
        "event_date": "2025-02-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 14400,
        "raw_price": 1.0666799
      },
      {
        "event_date": "2025-02-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 14200,
        "raw_price": 1.0926721
      },
      {
        "event_date": "2025-02-24",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13600,
        "raw_price": 1.1546535
      },
      {
        "event_date": "2025-02-26",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 1500,
        "raw_price": 1.1643492
      },
      {
        "event_date": "2025-02-27",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 8100,
        "raw_price": 1.1853555
      },
      {
        "event_date": "2025-03-04",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 16500,
        "raw_price": 1.1096670000000002
      }
    ],
    "by_reason": {
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 13200,
        "traded_value": "11223.366000"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 2,
        "shares": 12900,
        "traded_value": "15075.0211500"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 2,
        "shares": 34500,
        "traded_value": "36304.1055000000033000"
      },
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 49100,
        "traded_value": "50637.2866300"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 3,
        "shares": 42200,
        "traded_value": "46579.4219800"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 1500,
        "traded_value": "1746.5238000"
      }
    },
    "invested_sessions": 32,
    "cash_sessions": 94,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_002",
    "trade_points": [
      {
        "event_date": "2025-05-08",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 46400,
        "raw_price": 1.0773230999999999
      },
      {
        "event_date": "2025-05-29",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 46400,
        "raw_price": 1.0236928
      },
      {
        "event_date": "2025-06-06",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 46300,
        "raw_price": 1.0513153
      },
      {
        "event_date": "2025-06-23",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 46300,
        "raw_price": 1.0016994000000001
      },
      {
        "event_date": "2025-06-25",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 46100,
        "raw_price": 1.0323096
      },
      {
        "event_date": "2025-07-24",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 37500,
        "raw_price": 1.0716784000000001
      },
      {
        "event_date": "2025-07-25",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 15700,
        "raw_price": 1.0863258
      },
      {
        "event_date": "2025-07-28",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 11900,
        "raw_price": 1.1113332999999999
      },
      {
        "event_date": "2025-07-30",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 9500,
        "raw_price": 1.1223366000000001
      },
      {
        "event_date": "2025-08-04",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 45700,
        "raw_price": 1.0866739
      },
      {
        "event_date": "2025-08-15",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 13800,
        "raw_price": 1.1353404999999999
      },
      {
        "event_date": "2025-08-18",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 11200,
        "raw_price": 1.1713513
      },
      {
        "event_date": "2025-08-19",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 8900,
        "raw_price": 1.1813543
      },
      {
        "event_date": "2025-08-21",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 6900,
        "raw_price": 1.2093627
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 138800,
        "traded_value": "146253.1627899999953600"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 92700,
        "traded_value": "93878.0281400000046300"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 37500,
        "traded_value": "40187.9400000000037500"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 6,
        "shares": 64100,
        "traded_value": "72920.1694899999997600"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 45700,
        "traded_value": "49660.9972300"
      },
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 13800,
        "traded_value": "15667.6988999999986200"
      }
    },
    "invested_sessions": 68,
    "cash_sessions": 58,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_003",
    "trade_points": [
      {
        "event_date": "2025-09-18",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 5900,
        "raw_price": 1.4564367999999999
      },
      {
        "event_date": "2025-09-23",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4900,
        "raw_price": 1.4784434
      },
      {
        "event_date": "2025-09-25",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4300,
        "raw_price": 1.5244572
      },
      {
        "event_date": "2025-10-09",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4100,
        "raw_price": 1.6074821
      },
      {
        "event_date": "2025-10-15",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 19200,
        "raw_price": 1.4785563000000002
      },
      {
        "event_date": "2025-12-09",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 35200,
        "raw_price": 1.410423
      },
      {
        "event_date": "2026-01-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13500,
        "raw_price": 1.5165449
      },
      {
        "event_date": "2026-01-13",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 16600,
        "raw_price": 1.5935218000000002
      },
      {
        "event_date": "2026-01-22",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 6200,
        "raw_price": 1.6434929
      },
      {
        "event_date": "2026-01-30",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 11300,
        "raw_price": 1.5785263
      }
    ],
    "by_reason": {
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 1,
        "shares": 5900,
        "traded_value": "8592.9771199999994100"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 4,
        "shares": 19500,
        "traded_value": "30579.8712100"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 2,
        "shares": 30500,
        "traded_value": "46225.6281500000038400"
      },
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 1,
        "shares": 35200,
        "traded_value": "49646.889600"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 1,
        "shares": 13500,
        "traded_value": "20473.3561500"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 16600,
        "traded_value": "26452.4618800000033200"
      }
    },
    "invested_sessions": 49,
    "cash_sessions": 77,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_004",
    "trade_points": [
      {
        "event_date": "2026-04-15",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 6000,
        "raw_price": 1.4914473000000001
      },
      {
        "event_date": "2026-04-21",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 5900,
        "raw_price": 1.5234568999999998
      },
      {
        "event_date": "2026-04-28",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4900,
        "raw_price": 1.5794736999999999
      },
      {
        "event_date": "2026-05-06",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 4200,
        "raw_price": 1.7195157
      },
      {
        "event_date": "2026-06-01",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 21000,
        "raw_price": 1.8404477000000001
      },
      {
        "event_date": "2026-06-22",
        "kind": "fill",
        "reason": "trend_entry",
        "shares": 3300,
        "raw_price": 2.0266078
      },
      {
        "event_date": "2026-06-25",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 2900,
        "raw_price": 2.1146342
      },
      {
        "event_date": "2026-06-26",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 2700,
        "raw_price": 2.1426426
      },
      {
        "event_date": "2026-06-30",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 2500,
        "raw_price": 2.2576771
      },
      {
        "event_date": "2026-07-08",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 11400,
        "raw_price": 2.1413574
      },
      {
        "event_date": "2026-08-13",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 28500,
        "raw_price": 1.8565568000000001
      },
      {
        "event_date": "2026-08-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 8800,
        "raw_price": 1.7395217
      },
      {
        "event_date": "2026-09-07",
        "kind": "fill",
        "reason": "hard_stop",
        "shares": 37300,
        "raw_price": 1.6824951000000001
      },
      {
        "event_date": "2026-09-17",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 29500,
        "raw_price": 1.6985093999999998
      }
    ],
    "by_reason": {
      "trend_entry": {
        "reason": "trend_entry",
        "fill_count": 2,
        "shares": 9300,
        "traded_value": "15636.4895400000006000"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 6,
        "shares": 23100,
        "traded_value": "41511.5497299999983300"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 2,
        "shares": 32400,
        "traded_value": "63060.8760600000021000"
      },
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 2,
        "shares": 58000,
        "traded_value": "103017.8960999999969500"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 8800,
        "traded_value": "15307.7909600"
      },
      "hard_stop": {
        "reason": "hard_stop",
        "fill_count": 1,
        "shares": 37300,
        "traded_value": "62757.0672300000037300"
      }
    },
    "invested_sessions": 60,
    "cash_sessions": 66,
    "rejected_order_count": 0
  }
]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

### wf_000

Largest absolute contributor: cash_opportunity_cost (-0.02745219).
Next research action: Study cash exposure and re-entry timing on training windows.

### wf_001

Largest absolute contributor: cash_opportunity_cost (-0.19760980).
Next research action: Study cash exposure and re-entry timing on training windows.

### wf_002

Largest absolute contributor: trend_return (-0.13935054).
Next research action: Study trend entry/exit filters and stop distances on training windows.

### wf_003

Largest absolute contributor: trend_return (-0.05538027).
Next research action: Study trend entry/exit filters and stop distances on training windows.

### wf_004

Largest absolute contributor: trend_return (-0.19415597).
Next research action: Study trend entry/exit filters and stop distances on training windows.

Research evidence only; no broker action is authorized.
