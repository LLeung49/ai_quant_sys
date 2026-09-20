# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`diagnostic_complete`
- 建议：Diagnostic research only; no authorization.
- 阻断项：无

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.008128 | 0.136579 | -0.128451 |
| sharpe | 0.111788 | 0.721402 | -0.609613 |
| Sortino | 0.125099 | 0.985714 | -0.860615 |
| calmar | 0.096852 | 0.802067 | -0.705215 |
| cvar5 | -0.011228 | -0.026753 | 0.015525 |
| max_drawdown | -0.083920 | -0.170284 | 0.086364 |
| turnover | 21.452580 | 3.997072 | 17.455509 |
| total_cost | 1093.832180 | 199.407930 | 894.424250 |

## OOS 分布

{
  "window_count": 5,
  "win_rate": 0.0,
  "median_excess_return": -0.031977420600000306,
  "best_excess_return": -0.01192907859999981,
  "worst_excess_return": -0.14117198809999987
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 472,
    "cash_sessions": 158,
    "exposure_ratio": 0.7492063492063492,
    "turnover": 21.45258049652135,
    "total_cost": 1093.83218,
    "cost_drag": 0.010938321800000001
  },
  "buy_and_hold": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 3.997071902300532,
    "total_cost": 199.40793,
    "cost_drag": 0.0019940793
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-17",
  "config_hashes": [
    "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
    "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
    "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
    "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03"
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
            0.07608750970000026,
            0.02887670620000014,
            0.01722870710000006,
            0.08630498020000009
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
            0.03139534850000017,
            0.02597923990000009,
            0.08117076860000012
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
            0.031751209800000194,
            0.034833937300000124,
            0.07596012530000015
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
            0.026077795000000237,
            0.043922701200000164,
            0.07042747310000018
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
            0.024001611700000147,
            0.013623100300000029,
            0.08921831250000008
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
            0.020739065700000177,
            0.018299815800000032,
            0.08706925890000011
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
            0.017433894300000224,
            0.02328816170000004,
            0.08489866080000014
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
            0.018900183700000236,
            0.027911097900000043,
            0.08261963640000015
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
            0.023699126500000143,
            0.013060801500000031,
            0.08949139440000009
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
            0.01996258760000017,
            0.01676252970000004,
            0.08761542270000011
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
            0.012434133700000198,
            0.020377198200000043,
            0.08571790650000014
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
            0.012067311900000204,
            0.02388308620000005,
            0.08363340880000016
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
            0.023795155300000145,
            0.011354070300000029,
            0.09044387780000007
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
            0.02016264760000017,
            0.01319926010000003,
            0.08934714140000008
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
            0.012730222500000199,
            0.015095434600000034,
            0.0885281619000001
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
            0.012467431900000202,
            0.016924991700000037,
            0.08722103010000011
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
            0.026060945700000115,
            0.012189199100000027,
            0.09198844770000007
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
            0.024517747500000114,
            0.014585848700000025,
            0.09233418270000007
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
            0.022120331600000112,
            0.016982498300000027,
            0.0927010150000001
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
            0.016927199400000113,
            0.019414917900000026,
            0.0930548842000001
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
            0.02437676330000012,
            0.010088953200000026,
            0.09317551510000006
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
            0.020555804900000123,
            0.010518193200000026,
            0.09456085160000008
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
            0.01673484650000013,
            0.010947433200000026,
            0.09591308650000009
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
            0.012687701600000132,
            0.011376673200000026,
            0.0972984230000001
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
            0.024328777700000127,
            0.010088953200000026,
            0.09189032150000007
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
            0.020459833700000138,
            0.010518193200000026,
            0.09189032150000007
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
            0.016590889700000146,
            0.010947433200000026,
            0.09189032150000007
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
            0.012495759200000156,
            0.011376673200000026,
            0.09189032150000007
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
            0.025836579600000117,
            0.010088953200000026,
            0.09189032150000007
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
            0.023467185600000117,
            0.010518193200000026,
            0.09189032150000007
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
            0.021097791600000117,
            0.010947433200000026,
            0.09189032150000007
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
            0.018539200000000117,
            0.011376673200000026,
            0.09189032150000007
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
            0.026793292500000118,
            0.010088953200000026,
            0.09189032150000007
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
            0.025467585300000116,
            0.010518193200000026,
            0.09189032150000007
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
            0.024141878100000118,
            0.010947433200000026,
            0.09189032150000007
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
            0.022548251300000117,
            0.011376673200000026,
            0.09189032150000007
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
            0.026221464100000116,
            0.009849025200000026,
            0.09189032150000007
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
            0.024271944100000116,
            0.010038337200000027,
            0.09189032150000007
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
            0.022322424100000116,
            0.010227649200000025,
            0.09189032150000007
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
            0.020183706500000117,
            0.010432737200000026,
            0.09189032150000007
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
            0.026313249700000117,
            0.009709713200000025,
            0.09189032150000007
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
            0.024378777700000118,
            0.009709713200000025,
            0.09189032150000007
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
            0.022444305700000118,
            0.009709713200000025,
            0.09189032150000007
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
            0.02050983370000012,
            0.009709713200000025,
            0.09189032150000007
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
            0.05300962040000001,
            0.01722870710000006,
            0.08630498020000009,
            -0.005372334099999801
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
            0.05788853510000003,
            0.02597923990000009,
            0.08117076860000012,
            -0.0027737355999997693
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
            0.06091329190000004,
            0.034833937300000124,
            0.07596012530000015,
            -0.006897506099999767
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
            0.058177187500000074,
            0.043922701200000164,
            0.07042747310000018,
            -0.010884525299999788
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
            0.046790603000000014,
            0.013623100300000029,
            0.08921831250000008,
            -0.008682761399999817
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
            0.04399270380000003,
            0.018299815800000032,
            0.08706925890000011,
            -0.0072840980999997924
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
            0.042151371400000075,
            0.02328816170000004,
            0.08489866080000014,
            -0.008589328999999795
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
            0.04428594420000008,
            0.027911097900000043,
            0.08261963640000015,
            -0.017987100599999823
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
            0.046554853000000014,
            0.013060801500000031,
            0.08949139440000009,
            -0.00687881349999981
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
            0.04325240020000003,
            0.01676252970000004,
            0.08761542270000011,
            -0.003559296899999777
          ],
          "positive_window_share": 0.75
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
            0.03704730910000005,
            0.020377198200000043,
            0.08571790650000014,
            -0.005787999699999779
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
            0.03775012360000004,
            0.02388308620000005,
            0.08363340880000016,
            -0.0146789888999998
          ],
          "positive_window_share": 0.75
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
            0.046650881800000016,
            0.011354070300000029,
            0.09044387780000007,
            -0.009021284599999832
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
            0.04345246020000003,
            0.01319926010000003,
            0.08934714140000008,
            -0.00818826189999982
          ],
          "positive_window_share": 0.75
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
            0.037351400300000046,
            0.015095434600000034,
            0.0885281619000001,
            -0.00714800129999981
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
            0.03800703700000004,
            0.016924991700000037,
            0.08722103010000011,
            -0.011820456199999801
          ],
          "positive_window_share": 0.75
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
            0.047964669,
            0.012189199100000027,
            0.09198844770000007,
            -0.010423381099999834
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
            0.0459321089,
            0.014585848700000025,
            0.09233418270000007,
            -0.011204721299999824
          ],
          "positive_window_share": 0.75
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
            0.0441969683,
            0.016982498300000027,
            0.0927010150000001,
            -0.011929078599999816
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
            0.038514474199999996,
            0.019414917900000026,
            0.0930548842000001,
            -0.012636202799999807
          ],
          "positive_window_share": 0.75
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
            0.0462017646,
            0.010088953200000026,
            0.09317551510000006,
            -0.009431429799999834
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
            0.04215461970000001,
            0.010518193200000026,
            0.09456085160000008,
            -0.009082534499999826
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
            0.03833366130000001,
            0.010947433200000026,
            0.09591308650000009,
            -0.00869065209999982
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
            0.03419428970000001,
            0.011376673200000026,
            0.0972984230000001,
            -0.008341756799999813
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
            0.046153779000000006,
            0.010088953200000026,
            0.09189032150000007,
            -0.00877362719999984
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
            0.04205864850000002,
            0.010518193200000026,
            0.09189032150000007,
            -0.007723942199999841
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
            0.03818970450000003,
            0.010947433200000026,
            0.09189032150000007,
            -0.00674214429999984
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
            0.03399834850000004,
            0.011376673200000026,
            0.09189032150000007,
            -0.0056924592999998405
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
            0.047653329,
            0.010088953200000026,
            0.09189032150000007,
            -0.008143816199999836
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
            0.0450947374,
            0.010518193200000026,
            0.09189032150000007,
            -0.0065142126999998325
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
            0.042725343400000004,
            0.010947433200000026,
            0.09189032150000007,
            -0.004852711299999828
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
            0.0401667518,
            0.011376673200000026,
            0.09189032150000007,
            -0.0031732152999998237
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
            0.0486970158,
            0.010088953200000026,
            0.09189032150000007,
            -0.009675341599999842
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
            0.047182111,
            0.010518193200000026,
            0.09189032150000007,
            -0.009577370999999842
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
            0.0458564038,
            0.010947433200000026,
            0.09189032150000007,
            -0.009472402499999841
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
            0.044262777,
            0.011376673200000026,
            0.09189032150000007,
            -0.009374431899999841
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
            0.048073202999999995,
            0.009849025200000026,
            0.09189032150000007,
            -0.009227475999999837
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
            0.0459344854,
            0.010038337200000027,
            0.09189032150000007,
            -0.008681639799999832
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
            0.0439849654,
            0.010227649200000025,
            0.09189032150000007,
            -0.008096815299999827
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
            0.0418462478,
            0.010432737200000026,
            0.09189032150000007,
            -0.007550979099999824
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
            0.048138251,
            0.009709713200000025,
            0.09189032150000007,
            -0.009227475999999837
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
            0.046203779,
            0.009709713200000025,
            0.09189032150000007,
            -0.008681639799999832
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
            0.044108101,
            0.009709713200000025,
            0.09189032150000007,
            -0.008096815299999827
          ],
          "positive_window_share": 0.75
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
            0.042173629000000004,
            0.009709713200000025,
            0.09189032150000007,
            -0.007550979099999824
          ],
          "positive_window_share": 0.75
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
            0.010067105399999913,
            0.08630498020000009,
            -0.005372334099999801,
            -0.11030661689999988
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
            0.015098994099999923,
            0.08117076860000012,
            -0.0027737355999997693,
            -0.10173746489999985
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
            0.01904260059999993,
            0.07596012530000015,
            -0.006897506099999767,
            -0.09371752879999984
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
            0.02386146739999994,
            0.07042747310000018,
            -0.010884525299999788,
            -0.1123104162999998
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
            0.010019356599999907,
            0.08921831250000008,
            -0.008682761399999817,
            -0.11206985929999985
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
            0.014335642699999911,
            0.08706925890000011,
            -0.0072840980999997924,
            -0.10569160199999983
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
            0.018537009599999918,
            0.08489866080000014,
            -0.008589328999999795,
            -0.1005719255999998
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
            0.02217381889999992,
            0.08261963640000015,
            -0.017987100599999823,
            -0.11069508619999975
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
            0.009218139799999903,
            0.08949139440000009,
            -0.00687881349999981,
            -0.11595765909999986
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
            0.012150591999999905,
            0.08761542270000011,
            -0.003559296899999777,
            -0.11426424479999986
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
            0.014555898299999905,
            0.08571790650000014,
            -0.005787999699999779,
            -0.11318254389999982
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
            0.017347135499999902,
            0.08363340880000016,
            -0.0146789888999998,
            -0.12761743099999978
          ],
          "positive_window_share": 0.5
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
            0.007707565799999906,
            0.09044387780000007,
            -0.009021284599999832,
            -0.11453993179999988
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
            0.00903939959999991,
            0.08934714140000008,
            -0.00818826189999982,
            -0.11079376429999988
          ],
          "positive_window_share": 0.5
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
            0.01042211809999991,
            0.0885281619000001,
            -0.00714800129999981,
            -0.10778586869999988
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
            0.011491316499999914,
            0.08722103010000011,
            -0.011820456199999801,
            -0.12050879359999986
          ],
          "positive_window_share": 0.5
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
            0.008542694599999904,
            0.09198844770000007,
            -0.010423381099999834,
            -0.11426906599999989
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
            0.010425988199999904,
            0.09233418270000007,
            -0.011204721299999824,
            -0.11073193459999989
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
            0.012492018099999905,
            0.0927010150000001,
            -0.011929078599999816,
            -0.1078456765999999
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
            0.014368293699999904,
            0.0930548842000001,
            -0.012636202799999807,
            -0.12045073569999987
          ],
          "positive_window_share": 0.5
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
            0.006717214199999904,
            0.09317551510000006,
            -0.009431429799999834,
            -0.11538638739999987
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
            0.006561076599999904,
            0.09456085160000008,
            -0.009082534499999826,
            -0.11334936689999989
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
            0.006404838999999904,
            0.09591308650000009,
            -0.00869065209999982,
            -0.11187741979999988
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
            0.006199911599999904,
            0.0972984230000001,
            -0.008341756799999813,
            -0.12582438679999985
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
            0.007350591799999903,
            0.09189032150000007,
            -0.00877362719999984,
            -0.11501783309999988
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
            0.007779831799999904,
            0.09189032150000007,
            -0.007723942199999841,
            -0.11149983589999987
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
            0.008209071799999903,
            0.09189032150000007,
            -0.00674214429999984,
            -0.10951757199999988
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
            0.008638311799999904,
            0.09189032150000007,
            -0.0056924592999998405,
            -0.12268928519999986
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
            0.007350591799999903,
            0.09189032150000007,
            -0.008143816199999836,
            -0.11471892279999987
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
            0.007779831799999904,
            0.09189032150000007,
            -0.0065142126999998325,
            -0.11090201529999988
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
            0.008209071799999903,
            0.09189032150000007,
            -0.004852711299999828,
            -0.10827054609999988
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
            0.008638311799999904,
            0.09189032150000007,
            -0.0031732152999998237,
            -0.12149364399999986
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
            0.007350591799999903,
            0.09189032150000007,
            -0.009675341599999842,
            -0.10974044339999989
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
            0.007779831799999904,
            0.09189032150000007,
            -0.009577370999999842,
            -0.10148911279999989
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
            0.008209071799999903,
            0.09189032150000007,
            -0.009472402499999841,
            -0.0931633269999999
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
            0.008638311799999904,
            0.09189032150000007,
            -0.009374431899999841,
            -0.0845879944999999
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
            0.007110663799999904,
            0.09189032150000007,
            -0.009227475999999837,
            -0.11182381059999989
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
            0.007299975799999903,
            0.09189032150000007,
            -0.008681639799999832,
            -0.10572144419999989
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
            0.007489287799999904,
            0.09189032150000007,
            -0.008096815299999827,
            -0.0997872624999999
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
            0.007678599799999904,
            0.09189032150000007,
            -0.007550979099999824,
            -0.0936418107999999
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
            0.006971351799999904,
            0.09189032150000007,
            -0.009227475999999837,
            -0.11602108249999989
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
            0.006971351799999904,
            0.09189032150000007,
            -0.008681639799999832,
            -0.11419386419999988
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
            0.006971351799999904,
            0.09189032150000007,
            -0.008096815299999827,
            -0.11238664169999987
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
            0.006971351799999904,
            0.09189032150000007,
            -0.007550979099999824,
            -0.11037181529999988
          ],
          "positive_window_share": 0.5
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
            0.10470664130000015,
            -0.005372334099999801,
            -0.11030661689999988,
            -0.12045710749999988
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
            0.09887753280000018,
            -0.0027737355999997693,
            -0.10173746489999985,
            -0.13984512869999988
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
            0.09300854520000022,
            -0.006897506099999767,
            -0.09371752879999984,
            -0.14117198809999984
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
            0.08823023160000025,
            -0.010884525299999788,
            -0.1123104162999998,
            -0.1373049601999998
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
            0.10770091970000013,
            -0.008682761399999817,
            -0.11206985929999985,
            -0.10328481819999989
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
            0.10456684250000016,
            -0.0072840980999997924,
            -0.10569160199999983,
            -0.12154624159999987
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
            0.10160501860000018,
            -0.008589328999999795,
            -0.1005719255999998,
            -0.12440924279999988
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
            0.09871973470000021,
            -0.017987100599999823,
            -0.11069508619999975,
            -0.11862834959999985
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
            0.10824708350000013,
            -0.00687881349999981,
            -0.11595765909999986,
            -0.10082735169999991
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
            0.10565917010000016,
            -0.003559296899999777,
            -0.11426424479999986,
            -0.1220868160999999
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
            0.10310415830000018,
            -0.005787999699999779,
            -0.11318254389999982,
            -0.12680405769999992
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
            0.1007063672000002,
            -0.0146789888999998,
            -0.12761743099999978,
            -0.12352964399999991
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
            0.11004181250000011,
            -0.009021284599999832,
            -0.11453993179999988,
            -0.09655823649999992
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
            0.10975888520000013,
            -0.00818826189999982,
            -0.11079376429999988,
            -0.11494822809999992
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
            0.10919643240000015,
            -0.00714800129999981,
            -0.10778586869999988,
            -0.12302382699999996
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
            0.10863397960000015,
            -0.011820456199999801,
            -0.12050879359999986,
            -0.12209007599999996
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
            0.11121748000000012,
            -0.010423381099999834,
            -0.11426906599999989,
            -0.09337612899999993
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
            0.11196539050000014,
            -0.011204721299999824,
            -0.11073193459999989,
            -0.10644034189999993
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
            0.11287321890000016,
            -0.011929078599999816,
            -0.1078456765999999,
            -0.11901702939999995
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
            0.11348095560000016,
            -0.012636202799999807,
            -0.12045073569999987,
            -0.11873208369999996
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
            0.11156623190000012,
            -0.009431429799999834,
            -0.11538638739999987,
            -0.09067693899999993
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
            0.11266289430000015,
            -0.009082534499999826,
            -0.11334936689999989,
            -0.1005927315999999
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
            0.11375843460000015,
            -0.00869065209999982,
            -0.11187741979999988,
            -0.11139422159999993
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
            0.11485795780000017,
            -0.008341756799999813,
            -0.12582438679999985,
            -0.11443600779999996
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
            0.11009090780000011,
            -0.00877362719999984,
            -0.11501783309999988,
            -0.08814730179999994
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
            0.10947207230000013,
            -0.007723942199999841,
            -0.11149983589999987,
            -0.09607267549999993
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
            0.10899341060000013,
            -0.00674214429999984,
            -0.10951757199999988,
            -0.10469923069999992
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
            0.10851362680000014,
            -0.0056924592999998405,
            -0.12268928519999986,
            -0.11148989189999996
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
            0.11079014490000011,
            -0.008143816199999836,
            -0.11471892279999987,
            -0.08919297299999993
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
            0.11079014490000011,
            -0.0065142126999998325,
            -0.11090201529999988,
            -0.09882586109999991
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
            0.11079014490000011,
            -0.004852711299999828,
            -0.10827054609999988,
            -0.10850809949999989
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
            0.11079014490000011,
            -0.0031732152999998237,
            -0.12149364399999986,
            -0.11587022409999992
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
            0.11079014490000011,
            -0.009675341599999842,
            -0.10974044339999989,
            -0.08757945719999993
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
            0.11079014490000011,
            -0.009577370999999842,
            -0.10148911279999989,
            -0.09553784779999994
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
            0.11079014490000011,
            -0.009472402499999841,
            -0.0931633269999999,
            -0.10349623839999993
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
            0.11079014490000011,
            -0.009374431899999841,
            -0.0845879944999999,
            -0.11134021839999997
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
            0.11079014490000011,
            -0.009227475999999837,
            -0.11182381059999989,
            -0.08618687509999992
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
            0.11079014490000011,
            -0.008681639799999832,
            -0.10572144419999989,
            -0.09271069619999991
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
            0.11079014490000011,
            -0.008096815299999827,
            -0.0997872624999999,
            -0.09923451729999991
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
            0.11079014490000011,
            -0.007550979099999824,
            -0.0936418107999999,
            -0.1080172155999999
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
            0.11079014490000011,
            -0.009227475999999837,
            -0.11602108249999989,
            -0.08668269509999993
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
            0.11079014490000011,
            -0.008681639799999832,
            -0.11419386419999988,
            -0.09374533829999994
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
            0.11079014490000011,
            -0.008096815299999827,
            -0.11238664169999987,
            -0.10080798149999994
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
            0.11079014490000011,
            -0.007550979099999824,
            -0.11037181529999988,
            -0.10769531219999993
          ],
          "positive_window_share": 0.25
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
            -0.030470088999999815,
            -0.11030661689999988,
            -0.12045710749999988,
            -0.023144561599999995
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
            -0.024845918599999784,
            -0.10173746489999985,
            -0.13984512869999988,
            -0.012195804099999936
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
            -0.01926492949999975,
            -0.09371752879999984,
            -0.14117198809999984,
            -0.013100445899999827
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
            -0.015960217099999716,
            -0.1123104162999998,
            -0.1373049601999998,
            -0.019185385999999926
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
            -0.032150223999999825,
            -0.11206985929999985,
            -0.10328481819999989,
            -0.030610385100000026
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
            -0.0288523365999998,
            -0.10569160199999983,
            -0.12154624159999987,
            -0.023756537599999992
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
            -0.025570544799999772,
            -0.1005719255999998,
            -0.12440924279999988,
            -0.01666797339999996
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
            -0.02203712169999975,
            -0.11069508619999975,
            -0.11862834959999985,
            -0.025135983399999968
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
            -0.031272592599999816,
            -0.11595765909999986,
            -0.10082735169999991,
            -0.03292804610000002
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
            -0.026820145199999784,
            -0.11426424479999986,
            -0.1220868160999999,
            -0.02879571019999998
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
            -0.02242226759999975,
            -0.11318254389999982,
            -0.12680405769999992,
            -0.024691520799999943
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
            -0.017953407999999716,
            -0.12761743099999978,
            -0.12352964399999991,
            -0.02429439159999997
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
            -0.033487626099999834,
            -0.11453993179999988,
            -0.09655823649999992,
            -0.031918847700000044
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
            -0.031758518999999825,
            -0.11079376429999988,
            -0.11494822809999992,
            -0.026926051300000024
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
            -0.029988377399999815,
            -0.10778586869999988,
            -0.12302382699999996,
            -0.02190095670000001
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
            -0.028119810199999807,
            -0.12050879359999986,
            -0.12209007599999996,
            -0.016806383199999993
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
            -0.03423072419999983,
            -0.11426906599999989,
            -0.09337612899999993,
            -0.03006064150000003
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
            -0.03311836619999982,
            -0.11073193459999989,
            -0.10644034189999993,
            -0.023069252900000004
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
            -0.032039236499999804,
            -0.1078456765999999,
            -0.11901702939999995,
            -0.016057298099999975
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
            -0.031066138599999793,
            -0.12045073569999987,
            -0.11873208369999996,
            -0.00920204129999995
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
            -0.033353350099999846,
            -0.11538638739999987,
            -0.09067693899999993,
            -0.031271234600000045
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
            -0.03146391709999984,
            -0.11334936689999989,
            -0.1005927315999999,
            -0.025708231600000027
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
            -0.029713544199999845,
            -0.11187741979999988,
            -0.11139422159999993,
            -0.020399652000000008
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
            -0.027873403699999844,
            -0.12582438679999985,
            -0.11443600779999996,
            -0.015121490899999993
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
            -0.03500873109999984,
            -0.11501783309999988,
            -0.08814730179999994,
            -0.030841363600000046
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
            -0.03500873109999984,
            -0.11149983589999987,
            -0.09607267549999993,
            -0.024854315200000036
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
            -0.03500873109999984,
            -0.10951757199999988,
            -0.10469923069999992,
            -0.019024064800000025
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
            -0.03500873109999984,
            -0.12268928519999986,
            -0.11148989189999996,
            -0.013316032700000015
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
            -0.03500873109999984,
            -0.11471892279999987,
            -0.08919297299999993,
            -0.03358052660000005
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
            -0.03500873109999984,
            -0.11090201529999988,
            -0.09882586109999991,
            -0.030633411000000044
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
            -0.03500873109999984,
            -0.10827054609999988,
            -0.10850809949999989,
            -0.02787123990000004
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
            -0.03500873109999984,
            -0.12149364399999986,
            -0.11587022409999992,
            -0.024972937000000032
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
            -0.03500873109999984,
            -0.10974044339999989,
            -0.08757945719999993,
            -0.035181703900000055
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
            -0.03500873109999984,
            -0.10148911279999989,
            -0.09553784779999994,
            -0.034152940000000055
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
            -0.03500873109999984,
            -0.0931633269999999,
            -0.10349623839999993,
            -0.033075263400000054
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
            -0.03500873109999984,
            -0.0845879944999999,
            -0.11134021839999997,
            -0.031977420600000056
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
            -0.03500873109999984,
            -0.11182381059999989,
            -0.08618687509999992,
            -0.035181703900000055
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
            -0.03500873109999984,
            -0.10572144419999989,
            -0.09271069619999991,
            -0.034152940000000055
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
            -0.03500873109999984,
            -0.0997872624999999,
            -0.09923451729999991,
            -0.033075263400000054
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
            -0.03500873109999984,
            -0.0936418107999999,
            -0.1080172155999999,
            -0.031977420600000056
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
            -0.03500873109999984,
            -0.11602108249999989,
            -0.08668269509999993,
            -0.03466078760000005
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
            -0.03500873109999984,
            -0.11419386419999988,
            -0.09374533829999994,
            -0.032956299100000044
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
            -0.03500873109999984,
            -0.11238664169999987,
            -0.10080798149999994,
            -0.03123164440000004
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
            -0.03500873109999984,
            -0.11037181529999988,
            -0.10769531219999993,
            -0.029527155900000036
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
    "data_fingerprint": "0f72892e4cbdd079ecd08b1f0683192eaabdf5f63c1c8f3003bc39c512ed00d0",
    "run_mode": "research_diagnostic",
    "research_only": true,
    "activation_eligible": false,
    "shadow_run_eligible": false,
    "trading_authorized": false,
    "target": {
      "exposure_id": "csi_300",
      "stock_code": "510300.SH",
      "sub_layer": "broad_domestic_core",
      "scope": "formal"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
        "config": {
          "grid": {
            "step_pct": 0.03,
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
        "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
        "config": {
          "grid": {
            "step_pct": 0.02,
            "unit_pct": 0.1,
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
        "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
        "config": {
          "grid": {
            "step_pct": 0.01,
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
        "window_id": "wf_003",
        "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
        "config": {
          "grid": {
            "step_pct": 0.055,
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
        "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
        "config": {
          "grid": {
            "step_pct": 0.01,
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
    "profile_id": "grid_core",
    "profile_hash": "53e04e2ebcde6b11cecadf28bd776455bbc733ecf2d4f5a2eececcacc0d3ff45",
    "execution_windows": [
      {
        "window_id": "wf_000",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.03,
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
          "strategy_id": "grid_only",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.03,
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
          "policy_id": "grid_only",
          "spec_hash": "76adce12b09bfe825c73cf50c006ec179585c9aee673e2e83e67f1c5981b518c"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "be4db87a692a0bb4ed6ef5dfcebf112c5d92a4e4c082a336b8db4ef72d91a676",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.01112061171559775,
              "annual_volatility": 0.11784407713839432,
              "sharpe": 0.0943671670705849,
              "sortino": 0.20842217257349835,
              "calmar": 0.13066638383601578,
              "worst_126_session_return": 0.005500804500000456,
              "cvar5": -0.012247951491541564,
              "win_rate": 0.456,
              "payoff_ratio": 1.1862209069265377,
              "profit_factor": 1.0244635105274644,
              "turnover": 0.957530378429847,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9999549098196394,
              "max_drawdown": -0.08510690652887387,
              "recovery_sessions": 1,
              "total_cost": 39.91955
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "79df819a696c97c255c29c17f41eef648ac383ff3c038e642e5d9b909be09568",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.00493666290966166,
              "annual_volatility": 0.058959383504344556,
              "sharpe": 0.08372989363597892,
              "sortino": 0.18281087097827586,
              "calmar": 0.11294234009809394,
              "worst_126_session_return": 0.002445702900000235,
              "cvar5": -0.00613170164245382,
              "win_rate": 0.456,
              "payoff_ratio": 1.1966439873966566,
              "profit_factor": 1.0180404071882,
              "turnover": 0.5561630265493653,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.1621877142857143,
              "max_drawdown": -0.04370958584153661,
              "recovery_sessions": 1,
              "total_cost": 122.02971
            }
          }
        ]
      },
      {
        "window_id": "wf_001",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.02,
            "unit_pct": 0.1,
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
          "strategy_id": "grid_only",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.02,
              "unit_pct": 0.1,
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
          "policy_id": "grid_only",
          "spec_hash": "43b75f8c69b01a9522560ff0d7f5970a14ced682825a1561dbcb8f602df9c132"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.37750125028994863,
              "annual_volatility": 0.285878753780145,
              "sharpe": 1.3204942490419065,
              "sortino": 1.885955770743272,
              "calmar": 2.7637619214791456,
              "worst_126_session_return": 0.17217930199999998,
              "cvar5": -0.03710662739499071,
              "win_rate": 0.512,
              "payoff_ratio": 1.1905244762022895,
              "profit_factor": 1.3136821806370091,
              "turnover": 0.8723409118517654,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.998976930792377,
              "max_drawdown": -0.13658964158819897,
              "recovery_sessions": 2,
              "total_cost": 39.8698
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.18927685694187701,
              "annual_volatility": 0.14484161813659668,
              "sharpe": 1.3067850206104057,
              "sortino": 1.8945591858317357,
              "calmar": 2.6981221439887015,
              "worst_126_session_return": 0.0897898079000019,
              "cvar5": -0.01868399814019774,
              "win_rate": 0.512,
              "payoff_ratio": 1.2554817610957199,
              "profit_factor": 1.3172267657397716,
              "turnover": 0.6680782338839331,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.13041945454545456,
              "max_drawdown": -0.07015133001431295,
              "recovery_sessions": 2,
              "total_cost": 186.51921
            }
          }
        ]
      },
      {
        "window_id": "wf_002",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.01,
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
          "strategy_id": "grid_only",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.01,
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
          "policy_id": "grid_only",
          "spec_hash": "83eb2b7ff8d9c9a904e19fa816256b02e29384c4678b3a53d4d56ba589516540"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "e514a3071015233ca07b6d6c60aa09c39ee5aca8d19f7b3bbc962a03125df884",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.2840456053372127,
              "annual_volatility": 0.1495190488812094,
              "sharpe": 1.8997285460455449,
              "sortino": 1.8652210358077557,
              "calmar": 2.829925749761357,
              "worst_126_session_return": 0.13203368399999915,
              "cvar5": -0.024215119388543965,
              "win_rate": 0.56,
              "payoff_ratio": 1.0615461095911916,
              "profit_factor": 1.4290043782958348,
              "turnover": 0.9848624250321056,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.999156626506024,
              "max_drawdown": -0.10037210529681417,
              "recovery_sessions": 1,
              "total_cost": 39.8316
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "ce2c5fcb7f407337d8f2d9b70eb71cc489669ea71269ca40cdad1b89d7c5e77e",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.13515538953726414,
              "annual_volatility": 0.07498533596798045,
              "sharpe": 1.8024242712598761,
              "sortino": 1.772497269800916,
              "calmar": 2.6454436546220554,
              "worst_126_session_return": 0.06490087589999982,
              "cvar5": -0.012151527752390165,
              "win_rate": 0.56,
              "payoff_ratio": 1.0567611387398639,
              "profit_factor": 1.4225630713805864,
              "turnover": 0.5804752099391987,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.19458233333333333,
              "max_drawdown": -0.0510898764753972,
              "recovery_sessions": 1,
              "total_cost": 107.51241
            }
          }
        ]
      },
      {
        "window_id": "wf_003",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.055,
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
          "strategy_id": "grid_only",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.055,
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
          "policy_id": "grid_only",
          "spec_hash": "ff3c8b8009674e161ec585b69bae2c64d03400335691c3635b15338e80801dd3"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "5340ab168fbcf227c1344283d5ada8eb15bc7ed0ff2f5dfa512d91f0370979f8",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.0972034117901377,
              "annual_volatility": 0.14851381727060442,
              "sharpe": 0.6545075305217228,
              "sortino": 1.04245352000917,
              "calmar": 1.5026933291920253,
              "worst_126_session_return": 0.04708925999999902,
              "cvar5": -0.02125396629574357,
              "win_rate": 0.544,
              "payoff_ratio": 0.9389329700777486,
              "profit_factor": 1.1201305607945071,
              "turnover": 0.9429914657285958,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.999398194583751,
              "max_drawdown": -0.0646861271703405,
              "recovery_sessions": 1,
              "total_cost": 39.874
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "7d098022e1fb1d01c3955075a7e2e647a75d81f1612309b663747d9ae5eb2f8b",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.04842929543224006,
              "annual_volatility": 0.07444039389601431,
              "sharpe": 0.6505781726503339,
              "sortino": 1.0390373581362886,
              "calmar": 1.4748302761166496,
              "worst_126_session_return": 0.023736220599998248,
              "cvar5": -0.01065399231676665,
              "win_rate": 0.544,
              "payoff_ratio": 0.9348582907003337,
              "profit_factor": 1.1152695397828543,
              "turnover": 0.5762470740957483,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.1777794,
              "max_drawdown": -0.03283719911131633,
              "recovery_sessions": 1,
              "total_cost": 117.77794
            }
          }
        ]
      },
      {
        "window_id": "wf_004",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.01,
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
          "strategy_id": "grid_only",
          "version": "1",
          "config": {
            "grid": {
              "step_pct": 0.01,
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
          "policy_id": "grid_only",
          "spec_hash": "83eb2b7ff8d9c9a904e19fa816256b02e29384c4678b3a53d4d56ba589516540"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "e514a3071015233ca07b6d6c60aa09c39ee5aca8d19f7b3bbc962a03125df884",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.029455874683836147,
              "annual_volatility": 0.19983187085957774,
              "sharpe": -0.1474032873591763,
              "sortino": -0.21188062779522784,
              "calmar": -0.2644523341339672,
              "worst_126_session_return": -0.014721129799999955,
              "cvar5": -0.030115061564563412,
              "win_rate": 0.48,
              "payoff_ratio": 1.0415192869339944,
              "profit_factor": 0.9919231304133281,
              "turnover": 0.9662235569027248,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9992965931863727,
              "max_drawdown": -0.111384438259162,
              "recovery_sessions": 13,
              "total_cost": 39.91298
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "ce2c5fcb7f407337d8f2d9b70eb71cc489669ea71269ca40cdad1b89d7c5e77e",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.013679136875917486,
              "annual_volatility": 0.10005038234551278,
              "sharpe": -0.13672248476450716,
              "sortino": -0.19641479131179587,
              "calmar": -0.23825960192455173,
              "worst_126_session_return": -0.006808836299999177,
              "cvar5": -0.015112743942727769,
              "win_rate": 0.48,
              "payoff_ratio": 1.0350262211766776,
              "profit_factor": 0.9857392582635026,
              "turnover": 0.5963244981980205,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.16530572727272727,
              "max_drawdown": -0.05741274125123896,
              "recovery_sessions": 13,
              "total_cost": 128.18363
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
      "experiment_id": "round2-csi300-20260917",
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
        "profile_id": "grid_core",
        "required_evidence": [
          "execution",
          "integrated_oos",
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
          "policy_id": "grid_only",
          "strategy_id": "grid_only",
          "version": "1"
        },
        "version": "1"
      },
      "profile_hash": "53e04e2ebcde6b11cecadf28bd776455bbc733ecf2d4f5a2eececcacc0d3ff45",
      "start_date": "2021-01-01",
      "target_codes": [
        "510300.SH"
      ]
    },
    "experiment_hash": "17b7b5e0ace9e9a974f808732c9a2ea200e13c17d72cbe93497eef934c99aa06",
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
            "provenance_hash": "be4db87a692a0bb4ed6ef5dfcebf112c5d92a4e4c082a336b8db4ef72d91a676",
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
            "provenance_hash": "79df819a696c97c255c29c17f41eef648ac383ff3c038e642e5d9b909be09568",
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
            "cost_drag": 0.001315707225,
            "cvar5_improvement": 0.015017026999579325,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20443588512829686,
            "sortino_excess": 0.27978957798372184,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001455375125,
            "cvar5_improvement": 0.01468937535852401,
            "drawdown_improvement": 0.10765027998238363,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23587266707026028,
            "sortino_excess": 0.14796810131352459,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0018682278,
            "cvar5_improvement": 0.015137563163640927,
            "drawdown_improvement": 0.10794511812186397,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2668053008124632,
            "sortino_excess": 0.22697257118642086,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012822441000000001,
            "cvar5_improvement": 0.014776283437281896,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1644691073245843,
            "sortino_excess": 0.2925309928321398,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0028248358,
            "cvar5_improvement": 0.013780106484481186,
            "drawdown_improvement": 0.10285802916618306,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.14067866469102422,
            "sortino_excess": 0.6213677965981013,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001384912275,
            "cvar5_improvement": 0.014742776627018278,
            "drawdown_improvement": 0.10950830062703726,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.14767206073692113,
            "sortino_excess": 0.27971263984560935,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017468033,
            "cvar5_improvement": 0.014922097153562462,
            "drawdown_improvement": 0.10888439200851599,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19636723319635524,
            "sortino_excess": 0.2262593556456315,
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
            "cost_drag": 0.0013326292000000002,
            "cvar5_improvement": 0.014887656042623907,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2270027578670214,
            "sortino_excess": 0.22717427729996523,
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
            "cost_drag": 0.0012611370499999999,
            "cvar5_improvement": 0.015012415907424595,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.22453029771989874,
            "sortino_excess": 0.23512600201305264,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001293356325,
            "cvar5_improvement": 0.014888128933282733,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18379989866022042,
            "sortino_excess": 0.2747849299007109,
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
            "cost_drag": 0.0015266600750000001,
            "cvar5_improvement": 0.01488618116094828,
            "drawdown_improvement": 0.10958972105060089,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11867787763276579,
            "sortino_excess": 0.3372694292727816,
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
            "cost_drag": 0.0012537956750000002,
            "cvar5_improvement": 0.014888486226302528,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18479273370116556,
            "sortino_excess": 0.2708589319453789,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002628228725,
            "cvar5_improvement": 0.01417553655511706,
            "drawdown_improvement": 0.10584822742420502,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19390915066157924,
            "sortino_excess": 0.484286164785947,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015863849999999998,
            "cvar5_improvement": 0.014927367401247208,
            "drawdown_improvement": 0.10937118983682828,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11147957390068938,
            "sortino_excess": 0.3498270490036777,
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
            "cost_drag": 0.002197252,
            "cvar5_improvement": 0.015104452053935546,
            "drawdown_improvement": 0.10903061114167259,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27969082919330523,
            "sortino_excess": 0.26700153202111143,
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
            "cost_drag": 0.0030560065750000003,
            "cvar5_improvement": 0.013522198219370687,
            "drawdown_improvement": 0.09950784611872038,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.07593590341239709,
            "sortino_excess": 0.7663976651994946,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001351378675,
            "cvar5_improvement": 0.014949378205081599,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2653282870415937,
            "sortino_excess": 0.19180738673233136,
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
            "cost_drag": 0.00146717755,
            "cvar5_improvement": 0.014715986528133228,
            "drawdown_improvement": 0.10829671417120781,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1653820784661909,
            "sortino_excess": 0.23184122793045983,
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
            "cost_drag": 0.0013045758749999998,
            "cvar5_improvement": 0.014950003482377825,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18930112811231137,
            "sortino_excess": 0.28666797842568126,
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
            "cost_drag": 0.00125746295,
            "cvar5_improvement": 0.01495047553476735,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2057868088649528,
            "sortino_excess": 0.2517410031713465,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001636110175,
            "cvar5_improvement": 0.014838892528035564,
            "drawdown_improvement": 0.1095074279188886,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.17889814913213192,
            "sortino_excess": 0.25404408139466733,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015659653,
            "cvar5_improvement": 0.014928248185878876,
            "drawdown_improvement": 0.10890007176596433,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.17576717880377857,
            "sortino_excess": 0.28126859208927146,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024694968750000003,
            "cvar5_improvement": 0.014483939464329184,
            "drawdown_improvement": 0.10791092611845149,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1850891842380443,
            "sortino_excess": 0.35695061573471965,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.00180321045,
            "cvar5_improvement": 0.015106935700554311,
            "drawdown_improvement": 0.10936569221536813,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.22275919263355995,
            "sortino_excess": 0.2613416667894166,
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
            "cost_drag": 0.001282279425,
            "cvar5_improvement": 0.014776179138623464,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.15999156924966454,
            "sortino_excess": 0.3010464829359072,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0018092679750000003,
            "cvar5_improvement": 0.015147181273156013,
            "drawdown_improvement": 0.1089178397923515,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3174541187244258,
            "sortino_excess": 0.16386214026082405,
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
            "cost_drag": 0.0023225332,
            "cvar5_improvement": 0.015080012009378543,
            "drawdown_improvement": 0.10785867284032527,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18504032712810076,
            "sortino_excess": 0.3663444251703714,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013145509749999998,
            "cvar5_improvement": 0.014810680029982967,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18447074908714922,
            "sortino_excess": 0.2689286064850289,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00209972675,
            "cvar5_improvement": 0.015078799661613984,
            "drawdown_improvement": 0.11013292329122751,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.28577968995630804,
            "sortino_excess": 0.2575984617231128,
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
            "cost_drag": 0.0013150641,
            "cvar5_improvement": 0.01501629996514961,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3752488638683223,
            "sortino_excess": 0.08483152752092213,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001351497625,
            "cvar5_improvement": 0.014950003482377825,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20824132776226892,
            "sortino_excess": 0.2644790958204944,
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
            "cost_drag": 0.0013152402000000001,
            "cvar5_improvement": 0.015017026999579325,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.30855519090293687,
            "sortino_excess": 0.17380014749077705,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001293430875,
            "cvar5_improvement": 0.014888128933282733,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1742974195099241,
            "sortino_excess": 0.29286989189718216,
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
            "cost_drag": 0.001807567075,
            "cvar5_improvement": 0.014892353614136794,
            "drawdown_improvement": 0.1079405904071705,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2540990467345848,
            "sortino_excess": 0.15735393816463097,
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
            "cost_drag": 0.001314382675,
            "cvar5_improvement": 0.0148110608057949,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16656880642608363,
            "sortino_excess": 0.2925507038231451,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00183035225,
            "cvar5_improvement": 0.014804244240073011,
            "drawdown_improvement": 0.10663279285080243,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27236907496366686,
            "sortino_excess": 0.15046639574561216,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001426756675,
            "cvar5_improvement": 0.014734106027668082,
            "drawdown_improvement": 0.10886196643821308,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1532554759723291,
            "sortino_excess": 0.2534668678636905,
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
            "cost_drag": 0.0013044621,
            "cvar5_improvement": 0.014950003482377825,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2039331143642748,
            "sortino_excess": 0.25871405628930133,
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
            "cost_drag": 0.0013161797250000001,
            "cvar5_improvement": 0.015017026999579325,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2235306820474895,
            "sortino_excess": 0.24320341317003258,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001721804775,
            "cvar5_improvement": 0.01494792549674243,
            "drawdown_improvement": 0.10969828681091762,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18687224259378274,
            "sortino_excess": 0.26956589458576463,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001250121575,
            "cvar5_improvement": 0.014776466581194903,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16447683238433328,
            "sortino_excess": 0.29143561931511053,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001332603475,
            "cvar5_improvement": 0.014888128933282733,
            "drawdown_improvement": 0.11014623172751334,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19011506437738748,
            "sortino_excess": 0.2752527510961998,
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
            "cost_drag": 0.001465513475,
            "cvar5_improvement": 0.014829645948516679,
            "drawdown_improvement": 0.10985940372509184,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1359957943000587,
            "sortino_excess": 0.313636713076353,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020277920749999997,
            "cvar5_improvement": 0.014922040050260965,
            "drawdown_improvement": 0.11002432985052041,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.21413791899357687,
            "sortino_excess": 0.26783032724378864,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.0024597915114345165,
          "execution_cost": 145.92741,
          "grid_return": -0.012592390966939867,
          "reconciliation_error": 6.938893903907228e-18,
          "transition_return": 0.0,
          "trend_return": 0.0
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
            "cost_drag": 0.0015863849999999998,
            "cvar5_improvement": 0.014927367401247208,
            "drawdown_improvement": 0.10937118983682828,
            "exposure_ratio": 0.5496031746031746,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11147957390068938,
            "sortino_excess": 0.3498270490036777,
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
          "policy_id": "grid_only",
          "spec_hash": "76adce12b09bfe825c73cf50c006ec179585c9aee673e2e83e67f1c5981b518c",
          "strategy_id": "grid_only",
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
            "provenance_hash": "ad96060e0acdbd7d60fb870e3232884fa580658da2888cfebb9f99956bf8f0e6",
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
            "provenance_hash": "8b2bac349c450898c8323f53d9294ff1bca46a32b24858cf044f59f48f6c9c43",
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
            "cost_drag": 0.0012196378,
            "cvar5_improvement": 0.010480043407592074,
            "drawdown_improvement": 0.08724576881153562,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.07124831451374922,
            "sortino_excess": 0.31971085328079385,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001329315475,
            "cvar5_improvement": 0.010429436663842884,
            "drawdown_improvement": 0.08638962775022133,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.005773713094598773,
            "sortino_excess": 0.2854077327753829,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001790065325,
            "cvar5_improvement": 0.01103850560778188,
            "drawdown_improvement": 0.08573914241445432,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.04759881981088346,
            "sortino_excess": 0.31257913736789406,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001185954325,
            "cvar5_improvement": 0.010222116372202217,
            "drawdown_improvement": 0.08584908602345631,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.053387495209715405,
            "sortino_excess": 0.33552496850138364,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00279401065,
            "cvar5_improvement": 0.010150652379342201,
            "drawdown_improvement": 0.08542404274786417,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.24631618444246267,
            "sortino_excess": 0.8479585887827266,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001249521975,
            "cvar5_improvement": 0.010233860682041327,
            "drawdown_improvement": 0.08606111612571982,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0247553343239277,
            "sortino_excess": 0.33020129293861633,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016515727999999999,
            "cvar5_improvement": 0.01070909923422103,
            "drawdown_improvement": 0.08745550364527288,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0009693541058767019,
            "sortino_excess": 0.35735276536072413,
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
            "cost_drag": 0.0012096675,
            "cvar5_improvement": 0.010339378455741977,
            "drawdown_improvement": 0.0872285463258996,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08664926153641979,
            "sortino_excess": 0.30088697151592614,
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
            "cost_drag": 0.0011648016,
            "cvar5_improvement": 0.010477370705375863,
            "drawdown_improvement": 0.08726281392992222,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08718612314996194,
            "sortino_excess": 0.3000728810806973,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001197346675,
            "cvar5_improvement": 0.01032735875894911,
            "drawdown_improvement": 0.086308060848205,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06245663497979976,
            "sortino_excess": 0.32767647631223584,
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
            "cost_drag": 0.001405368,
            "cvar5_improvement": 0.010539200554193929,
            "drawdown_improvement": 0.08728966400130225,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.017889750181675018,
            "sortino_excess": 0.3750406999376009,
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
            "cost_drag": 0.001157179275,
            "cvar5_improvement": 0.010312961898006543,
            "drawdown_improvement": 0.086308060848205,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06457514347953651,
            "sortino_excess": 0.32475688999045776,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00274477075,
            "cvar5_improvement": 0.010245082224771565,
            "drawdown_improvement": 0.08630796902933324,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.22181486641803133,
            "sortino_excess": 0.7620805903529451,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014593719999999998,
            "cvar5_improvement": 0.010628896002678013,
            "drawdown_improvement": 0.08733485956229617,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.04509969717763104,
            "sortino_excess": 0.39094593354294216,
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
            "cost_drag": 0.002170006525,
            "cvar5_improvement": 0.01066848082452013,
            "drawdown_improvement": 0.08620541653631245,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.06053041330759745,
            "sortino_excess": 0.4819283584860299,
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
            "cost_drag": 0.002915013625,
            "cvar5_improvement": 0.010142659207455018,
            "drawdown_improvement": 0.08409031207849693,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.23868317472244432,
            "sortino_excess": 0.9170241318886405,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012213940250000001,
            "cvar5_improvement": 0.010412534453739894,
            "drawdown_improvement": 0.08724881800587514,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.10891375420321892,
            "sortino_excess": 0.2753599898141874,
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
            "cost_drag": 0.001302340525,
            "cvar5_improvement": 0.010384177634691261,
            "drawdown_improvement": 0.08661036734556685,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.0014138128152264631,
            "sortino_excess": 0.30381501974149405,
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
            "cost_drag": 0.00120853375,
            "cvar5_improvement": 0.010411601762685458,
            "drawdown_improvement": 0.08678777288565429,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06164370979931887,
            "sortino_excess": 0.33132865696851344,
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
            "cost_drag": 0.00116114265,
            "cvar5_improvement": 0.010413460223190294,
            "drawdown_improvement": 0.08680121981840111,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0759912903658117,
            "sortino_excess": 0.3130653475032392,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001547086425,
            "cvar5_improvement": 0.01044947907467505,
            "drawdown_improvement": 0.08682387808860773,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.02919454455764839,
            "sortino_excess": 0.34509152685274475,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001486204375,
            "cvar5_improvement": 0.01071812947866306,
            "drawdown_improvement": 0.08717098965502745,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.021557203152884175,
            "sortino_excess": 0.36790385936811326,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024639793499999997,
            "cvar5_improvement": 0.010236433237737447,
            "drawdown_improvement": 0.08668336506906368,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.07027471172210387,
            "sortino_excess": 0.5290313197291417,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.0018064588249999999,
            "cvar5_improvement": 0.01075002585291901,
            "drawdown_improvement": 0.0868056962678041,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.08431969911454291,
            "sortino_excess": 0.49402303479856075,
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
            "cost_drag": 0.001185985525,
            "cvar5_improvement": 0.010221645198301483,
            "drawdown_improvement": 0.08584431509340107,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.049905695405691945,
            "sortino_excess": 0.3397639596747981,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001828869225,
            "cvar5_improvement": 0.010945550013085443,
            "drawdown_improvement": 0.08654224428681723,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.04565117229671986,
            "sortino_excess": 0.4264099002336093,
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
            "cost_drag": 0.002193078275,
            "cvar5_improvement": 0.01066754597818635,
            "drawdown_improvement": 0.08516410270834568,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.030970634239773087,
            "sortino_excess": 0.38617666626166697,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001198366125,
            "cvar5_improvement": 0.010235059054061,
            "drawdown_improvement": 0.08630712048891287,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0651394895999457,
            "sortino_excess": 0.3228942085379366,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00207955265,
            "cvar5_improvement": 0.010607676741772723,
            "drawdown_improvement": 0.08703936815913607,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.03791684526436306,
            "sortino_excess": 0.44211784137114757,
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
            "cost_drag": 0.001233001775,
            "cvar5_improvement": 0.010479084206738681,
            "drawdown_improvement": 0.0872586086746707,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1350147761850996,
            "sortino_excess": 0.2419951922766014,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00122187605,
            "cvar5_improvement": 0.010415054210856357,
            "drawdown_improvement": 0.08726642699312362,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.040588492503469506,
            "sortino_excess": 0.3716905778229627,
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
            "cost_drag": 0.00123333995,
            "cvar5_improvement": 0.010482327296829658,
            "drawdown_improvement": 0.08728202584890676,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.03772599936288366,
            "sortino_excess": 0.3737459746709213,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0011974090749999999,
            "cvar5_improvement": 0.010326436458383464,
            "drawdown_improvement": 0.08629889698481927,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.055732975188773945,
            "sortino_excess": 0.33620189593449595,
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
            "cost_drag": 0.0017067238750000002,
            "cvar5_improvement": 0.010901765531750549,
            "drawdown_improvement": 0.08725269978685471,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.004136396551112392,
            "sortino_excess": 0.33111032300974647,
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
            "cost_drag": 0.001198525875,
            "cvar5_improvement": 0.010235936347656427,
            "drawdown_improvement": 0.0863135555315935,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.044853334596901766,
            "sortino_excess": 0.352452155614551,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017638220999999998,
            "cvar5_improvement": 0.010980121824264439,
            "drawdown_improvement": 0.086609825491032,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.03599554071471489,
            "sortino_excess": 0.27365037076758436,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012761902499999998,
            "cvar5_improvement": 0.010325929140792087,
            "drawdown_improvement": 0.08678522842737313,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.008918953900679927,
            "sortino_excess": 0.31745707862830774,
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
            "cost_drag": 0.00120844255,
            "cvar5_improvement": 0.010412985027941496,
            "drawdown_improvement": 0.08680121981840111,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0708693486017129,
            "sortino_excess": 0.3189995570812179,
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
            "cost_drag": 0.0012201408999999999,
            "cvar5_improvement": 0.010481870411645056,
            "drawdown_improvement": 0.08726281392992222,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08210466019315805,
            "sortino_excess": 0.3041569405639117,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0016736639,
            "cvar5_improvement": 0.010495483703973352,
            "drawdown_improvement": 0.08697920705997328,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.003058817099164876,
            "sortino_excess": 0.40355308677627244,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0011535203250000001,
            "cvar5_improvement": 0.01020686895499974,
            "drawdown_improvement": 0.08584908602345631,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.05482820997015963,
            "sortino_excess": 0.33332900334080096,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012107129,
            "cvar5_improvement": 0.010338097063554375,
            "drawdown_improvement": 0.08722832764891386,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.04396033724805531,
            "sortino_excess": 0.36265102062503185,
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
            "cost_drag": 0.0013502390750000002,
            "cvar5_improvement": 0.010352815170246363,
            "drawdown_improvement": 0.08631547470314607,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.013171763262920647,
            "sortino_excess": 0.35536496095841824,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00188990915,
            "cvar5_improvement": 0.010416300378686159,
            "drawdown_improvement": 0.08668136180835098,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.017033041179895153,
            "sortino_excess": 0.3744267911996585,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.059559500904708684,
          "execution_cost": 243.59428,
          "grid_return": -0.05970807321497143,
          "reconciliation_error": 2.7755575615628914e-17,
          "transition_return": 0.0,
          "trend_return": 0.0
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
            "cost_drag": 0.0018064588249999999,
            "cvar5_improvement": 0.01075002585291901,
            "drawdown_improvement": 0.0868056962678041,
            "exposure_ratio": 0.5813492063492064,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.08431969911454291,
            "sortino_excess": 0.49402303479856075,
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
          "policy_id": "grid_only",
          "spec_hash": "43b75f8c69b01a9522560ff0d7f5970a14ced682825a1561dbcb8f602df9c132",
          "strategy_id": "grid_only",
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
            "provenance_hash": "e514a3071015233ca07b6d6c60aa09c39ee5aca8d19f7b3bbc962a03125df884",
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
            "provenance_hash": "ce2c5fcb7f407337d8f2d9b70eb71cc489669ea71269ca40cdad1b89d7c5e77e",
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
            "cost_drag": 0.001581627775,
            "cvar5_improvement": 0.012255153921332598,
            "drawdown_improvement": 0.07485564600623792,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.31895032257113826,
            "sortino_excess": -0.047338905918128615,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00164713175,
            "cvar5_improvement": 0.012680274991057616,
            "drawdown_improvement": 0.07107097160157258,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.30204771041847644,
            "sortino_excess": -0.16128470282211216,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0021613984,
            "cvar5_improvement": 0.012583321507007725,
            "drawdown_improvement": 0.06949439288685971,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.43939795281995964,
            "sortino_excess": -0.32772940180850524,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014027548250000002,
            "cvar5_improvement": 0.011623942585621827,
            "drawdown_improvement": 0.06795264676518897,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4675309578603618,
            "sortino_excess": -0.3298465495574307,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00306200675,
            "cvar5_improvement": 0.012806673392926122,
            "drawdown_improvement": 0.0737573510665614,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1338837878122885,
            "sortino_excess": 0.13217119114182418,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015667014749999998,
            "cvar5_improvement": 0.011672195433118463,
            "drawdown_improvement": 0.06888730681322136,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4345411185551097,
            "sortino_excess": -0.3283911162571109,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019333008,
            "cvar5_improvement": 0.01233635581037052,
            "drawdown_improvement": 0.07366439912020642,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.35675823478300106,
            "sortino_excess": -0.2193495538162356,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015405857,
            "cvar5_improvement": 0.01215029089477276,
            "drawdown_improvement": 0.07367659435243284,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41028196802223565,
            "sortino_excess": -0.2172098223340801,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001387209775,
            "cvar5_improvement": 0.012558791305217702,
            "drawdown_improvement": 0.07253446948240402,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.40776992144982405,
            "sortino_excess": -0.1475698523239929,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014081261750000002,
            "cvar5_improvement": 0.012011339400072743,
            "drawdown_improvement": 0.07023334071078818,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.42291412249607224,
            "sortino_excess": -0.23267711027201557,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00169605075,
            "cvar5_improvement": 0.01236742133940453,
            "drawdown_improvement": 0.07335773144448002,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.35549011697731386,
            "sortino_excess": -0.21521313443875148,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001385637175,
            "cvar5_improvement": 0.011896676684456093,
            "drawdown_improvement": 0.06956851026434319,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4616933706507851,
            "sortino_excess": -0.30199319475421016,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00294653895,
            "cvar5_improvement": 0.012346476427027468,
            "drawdown_improvement": 0.07290544296891552,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20230019941190466,
            "sortino_excess": 0.009017115007969208,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001760860025,
            "cvar5_improvement": 0.0128333044699005,
            "drawdown_improvement": 0.0747363299860658,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27340197714137754,
            "sortino_excess": -0.0738374629500321,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00257032555,
            "cvar5_improvement": 0.012533942252614436,
            "drawdown_improvement": 0.07267230916177134,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20325270509561397,
            "sortino_excess": 0.023981188681027915,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003041929775,
            "cvar5_improvement": 0.013036537612333157,
            "drawdown_improvement": 0.07314346764556987,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.22533650935164914,
            "sortino_excess": 0.02207684841804175,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00156976025,
            "cvar5_improvement": 0.012578608457015462,
            "drawdown_improvement": 0.07426704892644478,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.35937191157847986,
            "sortino_excess": -0.09852074149955231,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016622161,
            "cvar5_improvement": 0.012473353066074555,
            "drawdown_improvement": 0.07143841317023472,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2899939272959933,
            "sortino_excess": -0.11901276053590493,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00155026355,
            "cvar5_improvement": 0.01202402877568864,
            "drawdown_improvement": 0.07379198634313344,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3701459474034392,
            "sortino_excess": -0.1630618289638151,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001386625425,
            "cvar5_improvement": 0.01223805705134449,
            "drawdown_improvement": 0.071655767968555,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4354101013791793,
            "sortino_excess": -0.22986144819538146,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018181227000000002,
            "cvar5_improvement": 0.011797104124091854,
            "drawdown_improvement": 0.069904037532142,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4456982273779911,
            "sortino_excess": -0.33632503042735046,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00176261965,
            "cvar5_improvement": 0.013123353101330813,
            "drawdown_improvement": 0.07506393451380428,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.28131203172391384,
            "sortino_excess": -0.08326259708847497,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00267214585,
            "cvar5_improvement": 0.011823709579919689,
            "drawdown_improvement": 0.07016209684459618,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.37952142295698205,
            "sortino_excess": -0.22891893764468885,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.00211781125,
            "cvar5_improvement": 0.012104706415660652,
            "drawdown_improvement": 0.07173482004714204,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.29859295307042216,
            "sortino_excess": -0.12665531904889135,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001489647425,
            "cvar5_improvement": 0.01150729130310236,
            "drawdown_improvement": 0.0683891518504044,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.46522502745862393,
            "sortino_excess": -0.3396090630647755,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0022088642,
            "cvar5_improvement": 0.012444072321230232,
            "drawdown_improvement": 0.07092267791846224,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.26652058774895615,
            "sortino_excess": -0.08598559669364736,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002583862375,
            "cvar5_improvement": 0.01264854326901354,
            "drawdown_improvement": 0.07173570564165532,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3529343795339206,
            "sortino_excess": -0.1781577380432911,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015125662500000002,
            "cvar5_improvement": 0.011687425019547979,
            "drawdown_improvement": 0.06962908458775571,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.46470670776846,
            "sortino_excess": -0.3255280101904648,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002407129125,
            "cvar5_improvement": 0.012179285846958455,
            "drawdown_improvement": 0.07324377450243794,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2868185783903535,
            "sortino_excess": -0.1070385931955992,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015354573,
            "cvar5_improvement": 0.012823414036804315,
            "drawdown_improvement": 0.07482845426695856,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3878632766988916,
            "sortino_excess": -0.13480680619176663,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001569895525,
            "cvar5_improvement": 0.01258693791096093,
            "drawdown_improvement": 0.07436921182163778,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3303391370613127,
            "sortino_excess": -0.053113373847469475,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001535736,
            "cvar5_improvement": 0.012827816171894083,
            "drawdown_improvement": 0.07486548862608436,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3493361867081987,
            "sortino_excess": -0.07876133839360525,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015202621249999998,
            "cvar5_improvement": 0.011751409500346624,
            "drawdown_improvement": 0.07114310168880006,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4195276349843206,
            "sortino_excess": -0.26139205231610196,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020473270000000003,
            "cvar5_improvement": 0.012828497945974357,
            "drawdown_improvement": 0.07477333666808178,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2575299678149169,
            "sortino_excess": -0.07308744692202697,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015126359249999998,
            "cvar5_improvement": 0.011688422678290367,
            "drawdown_improvement": 0.06970224070915096,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4569513964499921,
            "sortino_excess": -0.3138054067541055,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020866553,
            "cvar5_improvement": 0.013135679647083828,
            "drawdown_improvement": 0.07430094219053315,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.35041664448726206,
            "sortino_excess": -0.21826946506535183,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016149228,
            "cvar5_improvement": 0.012082170592188735,
            "drawdown_improvement": 0.07175594081495384,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3593061487291341,
            "sortino_excess": -0.2298584874591024,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001414296625,
            "cvar5_improvement": 0.012403956695464777,
            "drawdown_improvement": 0.07207629678154864,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3757331738640101,
            "sortino_excess": -0.10729016142559805,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014196466499999999,
            "cvar5_improvement": 0.012770560624351607,
            "drawdown_improvement": 0.07254504790017519,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3273647770971939,
            "sortino_excess": 0.032678772884968045,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0019654141,
            "cvar5_improvement": 0.011717939364207525,
            "drawdown_improvement": 0.06979495086694193,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4224741185835026,
            "sortino_excess": -0.2909772488148398,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013846508,
            "cvar5_improvement": 0.011570039967019458,
            "drawdown_improvement": 0.0676106261174505,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.48576025966362507,
            "sortino_excess": -0.35864657298376074,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015414481750000001,
            "cvar5_improvement": 0.01214945795098804,
            "drawdown_improvement": 0.07368368918795482,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3941048306282182,
            "sortino_excess": -0.19177785729000268,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016315057000000001,
            "cvar5_improvement": 0.011817225049623004,
            "drawdown_improvement": 0.06937960407683008,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.43674365169486684,
            "sortino_excess": -0.32910942575275803,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0021974174,
            "cvar5_improvement": 0.01173821195430671,
            "drawdown_improvement": 0.07023693424315233,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41733465517146967,
            "sortino_excess": -0.29253532483591316,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.0620661230082496,
          "execution_cost": 188.03041,
          "grid_return": -0.07623813019633233,
          "reconciliation_error": 0.0,
          "transition_return": 0.0,
          "trend_return": 0.0
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
            "cost_drag": 0.00306200675,
            "cvar5_improvement": 0.012806673392926122,
            "drawdown_improvement": 0.0737573510665614,
            "exposure_ratio": 0.5734126984126984,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1338837878122885,
            "sortino_excess": 0.13217119114182418,
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
          "policy_id": "grid_only",
          "spec_hash": "83eb2b7ff8d9c9a904e19fa816256b02e29384c4678b3a53d4d56ba589516540",
          "strategy_id": "grid_only",
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
            "provenance_hash": "5340ab168fbcf227c1344283d5ada8eb15bc7ed0ff2f5dfa512d91f0370979f8",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "7d098022e1fb1d01c3955075a7e2e647a75d81f1612309b663747d9ae5eb2f8b",
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
            "cost_drag": 0.0015146813,
            "cvar5_improvement": 0.01443604090320147,
            "drawdown_improvement": 0.08088879873605598,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3846288449869675,
            "sortino_excess": -0.2691793470060711,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015473547249999998,
            "cvar5_improvement": 0.015208991709204322,
            "drawdown_improvement": 0.07733755535032799,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.39173674984714074,
            "sortino_excess": -0.3199210941633069,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0019429805000000001,
            "cvar5_improvement": 0.014751362089156367,
            "drawdown_improvement": 0.07449405440467138,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7136061021781879,
            "sortino_excess": -0.7176791676183716,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001340810525,
            "cvar5_improvement": 0.013593651088222261,
            "drawdown_improvement": 0.07398579949500703,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3265695439829869,
            "sortino_excess": -0.2823156195829637,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027724257749999997,
            "cvar5_improvement": 0.014925380550346132,
            "drawdown_improvement": 0.07748429080593747,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5847909607877885,
            "sortino_excess": -0.4463258874110569,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015139374,
            "cvar5_improvement": 0.013795130272947853,
            "drawdown_improvement": 0.07499767956996284,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3216407399935136,
            "sortino_excess": -0.30033315574062647,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017753986,
            "cvar5_improvement": 0.014592213880842125,
            "drawdown_improvement": 0.07890758958297334,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.43640548724350603,
            "sortino_excess": -0.42948211647920026,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015274016499999999,
            "cvar5_improvement": 0.01438393635302714,
            "drawdown_improvement": 0.0794237818381088,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.32722169775782856,
            "sortino_excess": -0.2496629293221958,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013477967499999999,
            "cvar5_improvement": 0.014740012458965213,
            "drawdown_improvement": 0.07856762221222208,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4233185779297589,
            "sortino_excess": -0.3073763215921301,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00135396515,
            "cvar5_improvement": 0.014080566828798047,
            "drawdown_improvement": 0.07626649344060624,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.32219191767021405,
            "sortino_excess": -0.24759948009011268,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00160495815,
            "cvar5_improvement": 0.014556588005753813,
            "drawdown_improvement": 0.0789250727196357,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.39127403215745227,
            "sortino_excess": -0.3700949765926567,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001331230675,
            "cvar5_improvement": 0.013965935769898083,
            "drawdown_improvement": 0.07560166299416124,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.36813067091997437,
            "sortino_excess": -0.3227115925801673,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027320054249999996,
            "cvar5_improvement": 0.01458549789868025,
            "drawdown_improvement": 0.07727515887434463,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.604040742887763,
            "sortino_excess": -0.5350617505490297,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00164094775,
            "cvar5_improvement": 0.015123792041773151,
            "drawdown_improvement": 0.08004104770097153,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4507257671559285,
            "sortino_excess": -0.3762443025729417,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002326176025,
            "cvar5_improvement": 0.014832873952873424,
            "drawdown_improvement": 0.07803268994837492,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4994676240293959,
            "sortino_excess": -0.4227062408665313,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002671223875,
            "cvar5_improvement": 0.015107735943844302,
            "drawdown_improvement": 0.07716110936440113,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6756434507376639,
            "sortino_excess": -0.5686635477722823,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015724404249999999,
            "cvar5_improvement": 0.01490125401403009,
            "drawdown_improvement": 0.07989459312208658,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34455002255350364,
            "sortino_excess": -0.21577819243221455,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00159077105,
            "cvar5_improvement": 0.014896992999069159,
            "drawdown_improvement": 0.07766149395563171,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3475195995543264,
            "sortino_excess": -0.2640019747584552,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001503512075,
            "cvar5_improvement": 0.01416710002464252,
            "drawdown_improvement": 0.0798251390729515,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3602216625897218,
            "sortino_excess": -0.3000452468694974,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013398797250000001,
            "cvar5_improvement": 0.014381417738246157,
            "drawdown_improvement": 0.07768892069837305,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.39339127609973024,
            "sortino_excess": -0.31957820122446245,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016974664250000002,
            "cvar5_improvement": 0.013923278243905596,
            "drawdown_improvement": 0.07555787007144496,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.36061864518148534,
            "sortino_excess": -0.36259361422149505,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001605572975,
            "cvar5_improvement": 0.015477334423708827,
            "drawdown_improvement": 0.08049170440540801,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.47713219304907867,
            "sortino_excess": -0.39360362433508145,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002648660625,
            "cvar5_improvement": 0.014088422358385555,
            "drawdown_improvement": 0.07548725976634088,
            "exposure_ratio": 0.6468253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.536912193599783,
            "sortino_excess": -0.5473411445924167,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.0019973532499999998,
            "cvar5_improvement": 0.01427862775383062,
            "drawdown_improvement": 0.07676494918960733,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4992381150588741,
            "sortino_excess": -0.4708589735687301,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00142758065,
            "cvar5_improvement": 0.013505673685942946,
            "drawdown_improvement": 0.07442230458022245,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.33502810935041444,
            "sortino_excess": -0.30786401830886995,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0020356670750000003,
            "cvar5_improvement": 0.014620869741138373,
            "drawdown_improvement": 0.07563843361531783,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5426337860504998,
            "sortino_excess": -0.49226764766867737,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022835067500000003,
            "cvar5_improvement": 0.014963117336660187,
            "drawdown_improvement": 0.07767839629981463,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6289786311077561,
            "sortino_excess": -0.5853749544476148,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014830198999999998,
            "cvar5_improvement": 0.013751973104857429,
            "drawdown_improvement": 0.07553095233134652,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.33346983502529537,
            "sortino_excess": -0.2888520259943401,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002267331125,
            "cvar5_improvement": 0.014481434187229136,
            "drawdown_improvement": 0.07830885570831367,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5054495471555158,
            "sortino_excess": -0.4809382279766816,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001526308725,
            "cvar5_improvement": 0.015210744547946126,
            "drawdown_improvement": 0.08033607469945592,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4391747833242315,
            "sortino_excess": -0.319271080353942,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015231093250000001,
            "cvar5_improvement": 0.01472970911023921,
            "drawdown_improvement": 0.08040236455145583,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3661351159851299,
            "sortino_excess": -0.24192610263316047,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00146879095,
            "cvar5_improvement": 0.015008356485383545,
            "drawdown_improvement": 0.08089864135590241,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4581674975830884,
            "sortino_excess": -0.347162731501091,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014658529999999998,
            "cvar5_improvement": 0.013856777551991653,
            "drawdown_improvement": 0.07717625441861811,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3438994264916992,
            "sortino_excess": -0.31086412320858875,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001824872475,
            "cvar5_improvement": 0.015117838094715966,
            "drawdown_improvement": 0.08003967836873793,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.43441749702775245,
            "sortino_excess": -0.3680629092502454,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014504480999999998,
            "cvar5_improvement": 0.013686311465773102,
            "drawdown_improvement": 0.07573539343896901,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3388939421542615,
            "sortino_excess": -0.29866289627559695,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018083928750000002,
            "cvar5_improvement": 0.015425110175524453,
            "drawdown_improvement": 0.07993124039644137,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5259637693389637,
            "sortino_excess": -0.49587154008803624,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015647410000000001,
            "cvar5_improvement": 0.014373144758243375,
            "drawdown_improvement": 0.07794039597098765,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.31730511465630296,
            "sortino_excess": -0.28000735834386453,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001367918875,
            "cvar5_improvement": 0.014547317382366445,
            "drawdown_improvement": 0.0781094495113667,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3229018844039644,
            "sortino_excess": -0.1896291813661285,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013530214749999999,
            "cvar5_improvement": 0.014951781778099119,
            "drawdown_improvement": 0.07857820062999324,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3527428822551325,
            "sortino_excess": -0.14069163642800728,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001884741525,
            "cvar5_improvement": 0.013832570216610357,
            "drawdown_improvement": 0.07538240496950244,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3925208492019534,
            "sortino_excess": -0.39022157894028364,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013225835000000002,
            "cvar5_improvement": 0.013539768066812197,
            "drawdown_improvement": 0.07364377884726855,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34832361797020334,
            "sortino_excess": -0.31462417713460267,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001486792375,
            "cvar5_improvement": 0.014254599449398256,
            "drawdown_improvement": 0.07971684191777287,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34599387927978575,
            "sortino_excess": -0.27548248379634965,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00154608035,
            "cvar5_improvement": 0.013879262853543683,
            "drawdown_improvement": 0.07521009412772209,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3538895746646727,
            "sortino_excess": -0.3460745684950659,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002117186125,
            "cvar5_improvement": 0.013922848814014163,
            "drawdown_improvement": 0.07585188693771683,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41173622890937855,
            "sortino_excess": -0.4260073325424908,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.030576217252622946,
          "execution_cost": 106.61606,
          "grid_return": -0.004893853266719194,
          "reconciliation_error": 0.0,
          "transition_return": 0.0,
          "trend_return": 0.0
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.0013530214749999999,
            "cvar5_improvement": 0.014951781778099119,
            "drawdown_improvement": 0.07857820062999324,
            "exposure_ratio": 0.6587301587301587,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3527428822551325,
            "sortino_excess": -0.14069163642800728,
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
              "unit_pct": 0.2
            },
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
          "policy_id": "grid_only",
          "spec_hash": "ff3c8b8009674e161ec585b69bae2c64d03400335691c3635b15338e80801dd3",
          "strategy_id": "grid_only",
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
            "provenance_hash": "e514a3071015233ca07b6d6c60aa09c39ee5aca8d19f7b3bbc962a03125df884",
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
            "provenance_hash": "ce2c5fcb7f407337d8f2d9b70eb71cc489669ea71269ca40cdad1b89d7c5e77e",
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
            "cost_drag": 0.001424828525,
            "cvar5_improvement": 0.014020728054327098,
            "drawdown_improvement": 0.055097925661109465,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.61142117260037,
            "sortino_excess": -0.8081677723018691,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001390059675,
            "cvar5_improvement": 0.015261814281004354,
            "drawdown_improvement": 0.05631946911845806,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.537113545881001,
            "sortino_excess": -0.6433409098121827,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001873456025,
            "cvar5_improvement": 0.014875926322501528,
            "drawdown_improvement": 0.05637885913674201,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6018560025058829,
            "sortino_excess": -0.7858271864452435,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00124926755,
            "cvar5_improvement": 0.012829712208586109,
            "drawdown_improvement": 0.047955400467109416,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5980214911406543,
            "sortino_excess": -0.883484328535348,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00288971045,
            "cvar5_improvement": 0.015525477545764443,
            "drawdown_improvement": 0.06285122713749766,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4067670834281405,
            "sortino_excess": -0.33458242422239715,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00139671515,
            "cvar5_improvement": 0.013173082991751659,
            "drawdown_improvement": 0.04991856732428229,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5776230197774472,
            "sortino_excess": -0.850024926794171,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016726280500000002,
            "cvar5_improvement": 0.014147356699902455,
            "drawdown_improvement": 0.05495611829526886,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6754425092385599,
            "sortino_excess": -0.9608448808504422,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014221268,
            "cvar5_improvement": 0.013963436396467374,
            "drawdown_improvement": 0.05440087340615443,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5176524398141287,
            "sortino_excess": -0.7310809670375646,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001257991,
            "cvar5_improvement": 0.014327663765769253,
            "drawdown_improvement": 0.05277779779014877,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6548178606025923,
            "sortino_excess": -0.8490793072882014,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00126294025,
            "cvar5_improvement": 0.01342263607348688,
            "drawdown_improvement": 0.050509265728863245,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5864968938155231,
            "sortino_excess": -0.8388947827892852,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001542711275,
            "cvar5_improvement": 0.014201143894000498,
            "drawdown_improvement": 0.0547973641334602,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.568531606790587,
            "sortino_excess": -0.7810717750168312,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00124029555,
            "cvar5_improvement": 0.013310848184949223,
            "drawdown_improvement": 0.049854306646547886,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6240757194664786,
            "sortino_excess": -0.900031965016264,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00290856645,
            "cvar5_improvement": 0.014916619972440204,
            "drawdown_improvement": 0.05965588016692838,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5852464837487292,
            "sortino_excess": -0.6867973413340014,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015807975249999997,
            "cvar5_improvement": 0.0150183541166073,
            "drawdown_improvement": 0.057467593091893476,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5592729787228675,
            "sortino_excess": -0.6583069546678082,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002370659025,
            "cvar5_improvement": 0.015031928661439972,
            "drawdown_improvement": 0.05884245436290514,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4696190872040287,
            "sortino_excess": -0.6306453010803152,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027444822749999997,
            "cvar5_improvement": 0.015808410851842876,
            "drawdown_improvement": 0.06347388615065322,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4477134100560287,
            "sortino_excess": -0.3859055405446149,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001458887025,
            "cvar5_improvement": 0.014701722943372816,
            "drawdown_improvement": 0.055889910218711925,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4850150568399612,
            "sortino_excess": -0.623404802897485,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001446696775,
            "cvar5_improvement": 0.014774400235206306,
            "drawdown_improvement": 0.05544412040840288,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5344404483084253,
            "sortino_excess": -0.6597767780258259,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00141262735,
            "cvar5_improvement": 0.013622368089668352,
            "drawdown_improvement": 0.05432323261671823,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6009640926418219,
            "sortino_excess": -0.8565199524953644,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00124998705,
            "cvar5_improvement": 0.01383460593589049,
            "drawdown_improvement": 0.052165046020850814,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6373203286740927,
            "sortino_excess": -0.8791813193622502,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016003979,
            "cvar5_improvement": 0.013236294623500636,
            "drawdown_improvement": 0.04997228719706695,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6235716346837813,
            "sortino_excess": -0.9350410246499856,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015464871999999999,
            "cvar5_improvement": 0.015515127231537505,
            "drawdown_improvement": 0.05902237881530753,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5037778643354991,
            "sortino_excess": -0.5686097115628381,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002764831125,
            "cvar5_improvement": 0.013896930510400552,
            "drawdown_improvement": 0.05296701875294085,
            "exposure_ratio": 0.7242063492063492,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6848165027398158,
            "sortino_excess": -0.9675750727581012,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.00190021645,
            "cvar5_improvement": 0.014022950173221771,
            "drawdown_improvement": 0.05431253035178146,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.7216250925250285,
            "sortino_excess": -0.9850776249212492,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013360712749999999,
            "cvar5_improvement": 0.012742205980207527,
            "drawdown_improvement": 0.04839667648238008,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6018405929762988,
            "sortino_excess": -0.9011656450434256,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001991584875,
            "cvar5_improvement": 0.014540334476950051,
            "drawdown_improvement": 0.0557805630737398,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6540277520709914,
            "sortino_excess": -0.8447530136768981,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022398726,
            "cvar5_improvement": 0.015251644407178817,
            "drawdown_improvement": 0.06032534150910471,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4700608132188884,
            "sortino_excess": -0.6759641234183802,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013845447749999999,
            "cvar5_improvement": 0.013089290828399316,
            "drawdown_improvement": 0.04982846740095842,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.570571042762909,
            "sortino_excess": -0.840984080053974,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002257666825,
            "cvar5_improvement": 0.01443471027132314,
            "drawdown_improvement": 0.05678860275095726,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.617773611706241,
            "sortino_excess": -0.8557227411840564,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014064726,
            "cvar5_improvement": 0.015181002183805673,
            "drawdown_improvement": 0.05687815732186882,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5304698986355194,
            "sortino_excess": -0.6633560231945388,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001431391525,
            "cvar5_improvement": 0.014336892959128086,
            "drawdown_improvement": 0.05441817067696625,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6138220257677749,
            "sortino_excess": -0.8004860877058524,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013776214250000001,
            "cvar5_improvement": 0.014798552304296109,
            "drawdown_improvement": 0.055635985549655376,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6959508238291521,
            "sortino_excess": -0.8792279035453354,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013748953,
            "cvar5_improvement": 0.013199769097246133,
            "drawdown_improvement": 0.05142819057026085,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5983396508814596,
            "sortino_excess": -0.8860571968884083,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001714744825,
            "cvar5_improvement": 0.014895985330480074,
            "drawdown_improvement": 0.0583203843791196,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6441277509314963,
            "sortino_excess": -0.8460729286770088,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013592757499999999,
            "cvar5_improvement": 0.012951404365285931,
            "drawdown_improvement": 0.049239183550051274,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6083875698182885,
            "sortino_excess": -0.8979054064813774,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001704253125,
            "cvar5_improvement": 0.015384912379263751,
            "drawdown_improvement": 0.05997549544348474,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5978254884671056,
            "sortino_excess": -0.7945486762348803,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014340491750000001,
            "cvar5_improvement": 0.014033578508615793,
            "drawdown_improvement": 0.05413172230689128,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5404245225365085,
            "sortino_excess": -0.7525085293276477,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00127693095,
            "cvar5_improvement": 0.014001202182136237,
            "drawdown_improvement": 0.05259409612238661,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5798130259047115,
            "sortino_excess": -0.7712278072800514,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0012630319,
            "cvar5_improvement": 0.014534641925171768,
            "drawdown_improvement": 0.052770282436660126,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6022795729197973,
            "sortino_excess": -0.7131487134735439,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00179814975,
            "cvar5_improvement": 0.01325757906483331,
            "drawdown_improvement": 0.05000721343814632,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6439962078397353,
            "sortino_excess": -0.957789967453619,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00123156145,
            "cvar5_improvement": 0.012769907783675241,
            "drawdown_improvement": 0.04761847344813028,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6164566235410767,
            "sortino_excess": -0.9103582486398198,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001394992,
            "cvar5_improvement": 0.013691301845560425,
            "drawdown_improvement": 0.05303674590839075,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6036066925562636,
            "sortino_excess": -0.8552008040278678,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00148287755,
            "cvar5_improvement": 0.01323871607838482,
            "drawdown_improvement": 0.04989545882806615,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5914221248823308,
            "sortino_excess": -0.8701028183029322,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002103809025,
            "cvar5_improvement": 0.01348495857581114,
            "drawdown_improvement": 0.05132390707121129,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6167434978316312,
            "sortino_excess": -0.9306541434940458,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.0485695345747693,
          "execution_cost": 409.66402,
          "grid_return": 0.01914817536362779,
          "reconciliation_error": 0.0,
          "transition_return": 0.0,
          "trend_return": 0.0
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
            "cost_drag": 0.00288971045,
            "cvar5_improvement": 0.015525477545764443,
            "drawdown_improvement": 0.06285122713749766,
            "exposure_ratio": 0.7361111111111112,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4067670834281405,
            "sortino_excess": -0.33458242422239715,
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
          "policy_id": "grid_only",
          "spec_hash": "83eb2b7ff8d9c9a904e19fa816256b02e29384c4678b3a53d4d56ba589516540",
          "strategy_id": "grid_only",
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
      "policy_id": "grid_only",
      "strategy_id": "grid_only",
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
        "event_date": "2024-02-20",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 14700,
        "raw_price": 3.3840149
      },
      {
        "event_date": "2024-02-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 4300,
        "raw_price": 3.4859539
      },
      {
        "event_date": "2024-03-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 4200,
        "raw_price": 3.5839245
      },
      {
        "event_date": "2024-06-12",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 6200,
        "raw_price": 3.5429368
      },
      {
        "event_date": "2024-07-12",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 14500,
        "raw_price": 3.5120533
      },
      {
        "event_date": "2024-07-25",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 14500,
        "raw_price": 3.4629608000000003
      },
      {
        "event_date": "2024-08-01",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 14400,
        "raw_price": 3.5030505999999995
      },
      {
        "event_date": "2024-08-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 4400,
        "raw_price": 3.3970187999999997
      },
      {
        "event_date": "2024-08-15",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 18800,
        "raw_price": 3.3639905000000003
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 43600,
        "traded_value": "151113.7205199999928000"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 2,
        "shares": 8500,
        "traded_value": "30042.0846700"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 39500,
        "traded_value": "135422.1611600000099900"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 4400,
        "traded_value": "14946.8827199999986800"
      }
    },
    "invested_sessions": 94,
    "cash_sessions": 32,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_001",
    "trade_points": [
      {
        "event_date": "2024-09-25",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 14300,
        "raw_price": 3.4900466999999997
      },
      {
        "event_date": "2024-09-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2700,
        "raw_price": 3.6988900000000005
      },
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2600,
        "raw_price": 4.0057979
      },
      {
        "event_date": "2024-10-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2400,
        "raw_price": 4.6546031999999995
      },
      {
        "event_date": "2024-10-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 2500,
        "raw_price": 4.2862855
      },
      {
        "event_date": "2024-10-10",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 9100,
        "raw_price": 4.068779
      },
      {
        "event_date": "2024-10-11",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 13200,
        "raw_price": 4.0582171
      },
      {
        "event_date": "2024-10-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 2600,
        "raw_price": 3.9881961
      },
      {
        "event_date": "2024-10-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 2600,
        "raw_price": 3.931179
      },
      {
        "event_date": "2024-10-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2600,
        "raw_price": 4.0157949
      },
      {
        "event_date": "2024-11-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2600,
        "raw_price": 4.1357589
      },
      {
        "event_date": "2024-11-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2600,
        "raw_price": 4.2807154
      },
      {
        "event_date": "2024-11-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 2600,
        "raw_price": 4.1532456
      },
      {
        "event_date": "2024-11-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 2600,
        "raw_price": 4.0722213
      },
      {
        "event_date": "2024-11-25",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 15800,
        "raw_price": 3.9538135000000003
      },
      {
        "event_date": "2024-12-09",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 13200,
        "raw_price": 4.0552162
      },
      {
        "event_date": "2025-01-03",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 13200,
        "raw_price": 3.9078273
      },
      {
        "event_date": "2025-01-27",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 13300,
        "raw_price": 3.9371807999999997
      },
      {
        "event_date": "2025-02-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 2600,
        "raw_price": 4.007797300000001
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 4,
        "shares": 54000,
        "traded_value": "209369.4920099999917200"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 7,
        "shares": 18100,
        "traded_value": "74317.2981200000027500"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 5,
        "shares": 12900,
        "traded_value": "52692.3029500"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 38100,
        "traded_value": "151079.4625600000047400"
      }
    },
    "invested_sessions": 76,
    "cash_sessions": 50,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_002",
    "trade_points": [
      {
        "event_date": "2025-03-07",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 12300,
        "raw_price": 4.041212
      },
      {
        "event_date": "2025-03-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3600,
        "raw_price": 4.116764600000001
      },
      {
        "event_date": "2025-03-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3700,
        "raw_price": 4.064218899999999
      },
      {
        "event_date": "2025-03-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3700,
        "raw_price": 4.0102027
      },
      {
        "event_date": "2025-04-07",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 16100,
        "raw_price": 3.79886
      },
      {
        "event_date": "2025-04-28",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 12400,
        "raw_price": 3.8841649
      },
      {
        "event_date": "2025-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3700,
        "raw_price": 3.9168246000000004
      },
      {
        "event_date": "2025-05-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3600,
        "raw_price": 4.0097967
      },
      {
        "event_date": "2025-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3600,
        "raw_price": 3.9661894999999996
      },
      {
        "event_date": "2025-06-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3600,
        "raw_price": 3.9968006000000003
      },
      {
        "event_date": "2025-06-19",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 5100,
        "raw_price": 3.8968306000000004
      },
      {
        "event_date": "2025-06-24",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 12400,
        "raw_price": 3.8971687999999998
      },
      {
        "event_date": "2025-06-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3700,
        "raw_price": 3.9378183
      },
      {
        "event_date": "2025-06-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3600,
        "raw_price": 3.9938015000000004
      },
      {
        "event_date": "2025-07-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3600,
        "raw_price": 4.0467856
      },
      {
        "event_date": "2025-07-18",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-21",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-22",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-23",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-24",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-25",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-28",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-29",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-30",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-31",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-01",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-04",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-05",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-06",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-08",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-12",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-15",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-18",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-19",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-20",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-21",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-22",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-25",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-26",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-27",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-28",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-08-29",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-09-01",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-09-02",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-09-03",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 37100,
        "traded_value": "146195.4454799999975200"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 7,
        "shares": 25400,
        "traded_value": "101652.3951300000076000"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 3,
        "shares": 11000,
        "traded_value": "44153.6421199999948600"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 21200,
        "traded_value": "81035.4820600000020400"
      }
    },
    "invested_sessions": 106,
    "cash_sessions": 20,
    "rejected_order_count": 34
  },
  {
    "window_id": "wf_003",
    "trade_points": [
      {
        "event_date": "2025-09-05",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 11200,
        "raw_price": 4.451335
      },
      {
        "event_date": "2025-09-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 4300,
        "raw_price": 4.6755968999999995
      },
      {
        "event_date": "2025-11-24",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 6900,
        "raw_price": 4.5776262999999995
      },
      {
        "event_date": "2025-12-08",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10800,
        "raw_price": 4.712413300000001
      },
      {
        "event_date": "2026-01-20",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 10800,
        "raw_price": 4.7335795
      },
      {
        "event_date": "2026-01-21",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10800,
        "raw_price": 4.710412699999999
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 32800,
        "traded_value": "151621.472800000000000"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 1,
        "shares": 4300,
        "traded_value": "20105.0666699999978500"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 17700,
        "traded_value": "82708.2800699999965500"
      }
    },
    "invested_sessions": 114,
    "cash_sessions": 12,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_004",
    "trade_points": [
      {
        "event_date": "2026-04-09",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10900,
        "raw_price": 4.5743719
      },
      {
        "event_date": "2026-04-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3200,
        "raw_price": 4.6276113
      },
      {
        "event_date": "2026-04-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3200,
        "raw_price": 4.7305804
      },
      {
        "event_date": "2026-04-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.818554000000001
      },
      {
        "event_date": "2026-04-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3200,
        "raw_price": 4.7564265
      },
      {
        "event_date": "2026-04-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.828551
      },
      {
        "event_date": "2026-05-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-08",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-12",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-15",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-18",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-05-22",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 1500,
        "raw_price": 4.8265516
      },
      {
        "event_date": "2026-05-25",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10400,
        "raw_price": 4.881463999999999
      },
      {
        "event_date": "2026-05-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.9105264
      },
      {
        "event_date": "2026-05-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.9615111
      },
      {
        "event_date": "2026-06-02",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.8684601
      },
      {
        "event_date": "2026-06-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.9365186
      },
      {
        "event_date": "2026-06-08",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.791437
      },
      {
        "event_date": "2026-06-09",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 7300,
        "raw_price": 4.762570800000001
      },
      {
        "event_date": "2026-06-16",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10300,
        "raw_price": 4.921476
      },
      {
        "event_date": "2026-06-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 4.9815051
      },
      {
        "event_date": "2026-06-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 5.0774763
      },
      {
        "event_date": "2026-06-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.9304787
      },
      {
        "event_date": "2026-06-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 5.0064976
      },
      {
        "event_date": "2026-06-29",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.8984691
      },
      {
        "event_date": "2026-06-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.9455159
      },
      {
        "event_date": "2026-07-01",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3000,
        "raw_price": 5.007497300000001
      },
      {
        "event_date": "2026-07-03",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 1400,
        "raw_price": 4.828551
      },
      {
        "event_date": "2026-07-10",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10400,
        "raw_price": 4.9194754
      },
      {
        "event_date": "2026-07-13",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.803440599999999
      },
      {
        "event_date": "2026-07-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.721416
      },
      {
        "event_date": "2026-07-20",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 16600,
        "raw_price": 4.628611
      },
      {
        "event_date": "2026-08-10",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 10400,
        "raw_price": 4.7564265
      },
      {
        "event_date": "2026-08-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.6714009999999995
      },
      {
        "event_date": "2026-08-26",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.6163845
      },
      {
        "event_date": "2026-08-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 3100,
        "raw_price": 4.6825948
      },
      {
        "event_date": "2026-09-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 3100,
        "raw_price": 4.6323893
      },
      {
        "event_date": "2026-09-14",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 16600,
        "raw_price": 4.5496347
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 5,
        "shares": 52400,
        "traded_value": "251948.461869999989600"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 13,
        "shares": 40100,
        "traded_value": "195824.834920000006100"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 10,
        "shares": 31100,
        "traded_value": "148315.5813299999953500"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 5,
        "shares": 43400,
        "traded_value": "201125.444260000007300"
      }
    },
    "invested_sessions": 82,
    "cash_sessions": 44,
    "rejected_order_count": 8
  }
]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

### wf_000

Largest absolute contributor: grid_return (-0.01259239).
Next research action: Study grid spacing, sizing and stop/cooldown behavior on training windows.

### wf_001

Largest absolute contributor: grid_return (-0.05970807).
Next research action: Study grid spacing, sizing and stop/cooldown behavior on training windows.

### wf_002

Largest absolute contributor: grid_return (-0.07623813).
Next research action: Study grid spacing, sizing and stop/cooldown behavior on training windows.

### wf_003

Largest absolute contributor: cash_opportunity_cost (-0.03057622).
Next research action: Study cash exposure and re-entry timing on training windows.

### wf_004

Largest absolute contributor: cash_opportunity_cost (-0.04856953).
Next research action: Study cash exposure and re-entry timing on training windows.

Research evidence only; no broker action is authorized.
