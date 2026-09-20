# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`diagnostic_complete`
- 建议：Diagnostic research only; no authorization.
- 阻断项：无

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.016982 | 0.017417 | -0.000436 |
| sharpe | 0.297446 | 0.110765 | 0.186681 |
| Sortino | 0.318991 | 0.139929 | 0.179062 |
| calmar | 0.382946 | 0.111585 | 0.271361 |
| cvar5 | -0.008524 | -0.022059 | 0.013535 |
| max_drawdown | -0.044345 | -0.156089 | 0.111745 |
| turnover | 30.057821 | 4.817681 | 25.240140 |
| total_cost | 1504.177640 | 199.751400 | 1304.426240 |

## OOS 分布

{
  "window_count": 5,
  "win_rate": 0.6,
  "median_excess_return": 0.011127838200000406,
  "best_excess_return": 0.03281202669999994,
  "worst_excess_return": -0.037598883599999855
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 456,
    "cash_sessions": 174,
    "exposure_ratio": 0.7238095238095238,
    "turnover": 30.0578205724388,
    "total_cost": 1504.17764,
    "cost_drag": 0.015041776400000002
  },
  "buy_and_hold": {
    "invested_sessions": 625,
    "cash_sessions": 5,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 4.8176808208798905,
    "total_cost": 199.7514,
    "cost_drag": 0.0019975139999999997
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-17",
  "config_hashes": [
    "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
    "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61"
  ],
  "training_surface": [
    {
      "window_id": "wf_000",
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
            0.008261671200000046,
            -0.010628584099999781,
            -0.034757129499999914,
            -0.009258798699999973
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
            0.030261057000000063,
            -0.002903762699999736,
            -0.037104714499999886,
            -0.005729207699999905
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
            0.030651156800000086,
            -0.006789854199999751,
            -0.046838481899999874,
            -0.0022196104999998405
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.028513799600000077,
            -0.004863210599999768,
            -0.05454614569999985,
            0.0012752016000002267
          ],
          "positive_window_share": 0.5
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
            0.0032451001000000507,
            -0.010008142299999802,
            -0.03187526559999993,
            -0.01079385090000002
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
            0.019770533900000067,
            -0.0019167271999997772,
            -0.03158348199999993,
            -0.009319521099999999
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
            0.025827503400000076,
            -0.0008955085999997822,
            -0.037979651899999925,
            -0.007952018299999985
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
            0.023633231600000117,
            -0.008818981299999811,
            -0.041429834599999896,
            -0.006401569899999966
          ],
          "positive_window_share": 0.25
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
            -0.0019929715999999695,
            -0.012187635299999805,
            -0.03174664569999992,
            -0.011164933000000023
          ],
          "positive_window_share": 0.0
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
            0.008699576900000026,
            -0.006771767199999784,
            -0.03184463649999992,
            -0.010459873800000005
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
            0.019571491400000023,
            -0.0013984932999997618,
            -0.035907224099999926,
            -0.00982171829999999
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
            0.02667690470000002,
            -0.005011794499999783,
            -0.040899410399999905,
            -0.009097372999999978
          ],
          "positive_window_share": 0.25
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
            -0.008071066399999959,
            -0.011880063699999808,
            -0.030901869199999918,
            -0.010736061700000014
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
            -0.004095355499999953,
            -0.0061016500999997916,
            -0.0303020876999999,
            -0.009667447400000001
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
            -2.5966399999945156e-05,
            -0.00029601139999977516,
            -0.029889304099999882,
            -0.008548969299999983
          ],
          "positive_window_share": 0.0
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
            0.0038768751000000587,
            -0.0035967424999997985,
            -0.03440617169999988,
            -0.007394165199999966
          ],
          "positive_window_share": 0.25
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
            -0.007633388899999968,
            -0.013336032899999819,
            -0.03156941579999993,
            -0.011719574300000035
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
            -0.0032037398999999744,
            -0.00919711389999981,
            -0.03201702039999993,
            -0.011767087700000033
          ],
          "positive_window_share": 0.0
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
            0.0011630427000000262,
            -0.005028036999999805,
            -0.03236740039999993,
            -0.011814601100000037
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
            0.0054820216000000185,
            -0.0008860687999997993,
            -0.032618342999999925,
            -0.011862114500000034
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
            -0.013127151299999808,
            -0.030825288899999935,
            -0.011623500700000032
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
            -0.0019953774999999785,
            -0.008865674299999791,
            -0.030528299799999933,
            -0.011623500700000032
          ],
          "positive_window_share": 0.0
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
            0.002925908700000014,
            -0.0045157373999997735,
            -0.030169008599999932,
            -0.011623500700000032
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
            0.007838049300000007,
            -0.00032750779999975513,
            -0.029729823099999934,
            -0.011623500700000032
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
            -0.012456352599999814,
            -0.029621304299999932,
            -0.011623500700000032
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
            -0.0065473363999999715,
            -0.007482502899999804,
            -0.02781051059999993,
            -0.011623500700000032
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
            -0.003974959999999979,
            -0.002542842999999795,
            -0.02607716749999992,
            -0.011623500700000032
          ],
          "positive_window_share": 0.0
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
            0.002465209900000216,
            -0.02445337139999992,
            -0.011623500700000032
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
            -0.014672428399999823,
            -0.027814850699999942,
            -0.011623500700000032
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
            -0.0065473363999999715,
            -0.012040631699999818,
            -0.024407198299999947,
            -0.011623500700000032
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
            -0.003974959999999979,
            -0.009408834999999815,
            -0.020917301299999955,
            -0.011623500700000032
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
            -0.0014025835999999792,
            -0.006745878299999812,
            -0.017522194099999958,
            -0.011623500700000032
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
            -0.009119712799999971,
            -0.014434499799999822,
            -0.027345991399999933,
            -0.011623500700000032
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
            -0.0065473363999999715,
            -0.01156477449999982,
            -0.023413027299999934,
            -0.011623500700000032
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
            -0.003974959999999979,
            -0.008688881699999814,
            -0.019522719799999935,
            -0.011623500700000032
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
            -0.0014025835999999792,
            -0.005819156399999812,
            -0.015549867699999935,
            -0.011623500700000032
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
            -0.009565213699999964,
            -0.014197984299999822,
            -0.028275079499999932,
            -0.011623500700000032
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
            -0.007318226499999969,
            -0.011124320199999819,
            -0.025323920799999927,
            -0.011623500700000032
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
            -0.005037397799999968,
            -0.008044488599999814,
            -0.022327673199999922,
            -0.011623500700000032
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
            -0.0027904105999999665,
            -0.0049709244999998105,
            -0.01929019149999992,
            -0.011623500700000032
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
            -0.008430919499999967,
            -0.01356817329999982,
            -0.027618894499999942,
            -0.011623500700000032
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
            -0.0050667806999999745,
            -0.009793550199999812,
            -0.024110284999999947,
            -0.011623500700000032
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
            -0.0017364833999999746,
            -0.006025094599999805,
            -0.020582317699999957,
            -0.011623500700000032
          ],
          "positive_window_share": 0.0
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
            0.001627655400000018,
            -0.002153114299999797,
            -0.01691245399999996,
            -0.011623500700000032
          ],
          "positive_window_share": 0.25
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
            false,
            false,
            true
          ],
          "oos_returns": [
            0.002264214400000117,
            -0.034757129499999914,
            -0.009258798699999973,
            0.01546420790000009
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.010805872200000163,
            -0.037104714499999886,
            -0.005729207699999905,
            0.023120157200000113
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.01695169370000021,
            -0.046838481899999874,
            -0.0022196104999998405,
            0.0218803201000001
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.023464803700000172,
            -0.05454614569999985,
            0.0012752016000002267,
            0.014117575200000107
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0024044849000000937,
            -0.03187526559999993,
            -0.01079385090000002,
            0.015216565600000101
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.01063401640000012,
            -0.03158348199999993,
            -0.009319521099999999,
            0.02224709280000013
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.018752478800000142,
            -0.037979651899999925,
            -0.007952018299999985,
            0.020449137800000107
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.015457758900000129,
            -0.041429834599999896,
            -0.006401569899999966,
            0.01993879620000008
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.00017378420000009262,
            -0.03174664569999992,
            -0.011164933000000023,
            0.012604088700000078
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
            0.005798089600000111,
            -0.03184463649999992,
            -0.010459873800000005,
            0.016701309500000087
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.011441649000000133,
            -0.035907224099999926,
            -0.00982171829999999,
            0.0207797548000001
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.017031324600000158,
            -0.040899410399999905,
            -0.009097372999999978,
            0.020234496800000105
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0004212141000000877,
            -0.030901869199999918,
            -0.010736061700000014,
            0.010670737500000072
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.006199277800000107,
            -0.0303020876999999,
            -0.009667447400000001,
            0.012626151600000076
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.012071332500000125,
            -0.029889304099999882,
            -0.008548969299999983,
            0.014492155000000078
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.017914476700000143,
            -0.03440617169999988,
            -0.007394165199999966,
            0.016421340700000082
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0008952534000000768,
            -0.03156941579999993,
            -0.011719574300000035,
            0.011714249100000074
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.007106856200000084,
            -0.03201702039999993,
            -0.011767087700000033,
            0.014618458100000082
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.013398315600000089,
            -0.03236740039999993,
            -0.011814601100000037,
            0.01750889530000009
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0195929542000001,
            -0.032618342999999925,
            -0.011862114500000034,
            0.020431525000000096
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            false,
            false,
            false,
            true
          ],
          "oos_returns": [
            -0.0023554368999999208,
            -0.030825288899999935,
            -0.011623500700000032,
            0.009087508900000072
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0005241547000000846,
            -0.030528299799999933,
            -0.011623500700000032,
            0.009185305900000076
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.003317802800000092,
            -0.030169008599999932,
            -0.011623500700000032,
            0.009195907700000078
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.006197294400000098,
            -0.029729823099999934,
            -0.011623500700000032,
            0.009277619400000083
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            false,
            false,
            false,
            true
          ],
          "oos_returns": [
            -0.0013636651999999125,
            -0.029621304299999932,
            -0.011623500700000032,
            0.01023681420000008
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0024635420000001067,
            -0.02781051059999993,
            -0.011623500700000032,
            0.011352458100000087
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0063172584000001225,
            -0.02607716749999992,
            -0.011623500700000032,
            0.012573091800000099
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.01021164550000014,
            -0.02445337139999992,
            -0.011623500700000032,
            0.013685198900000108
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            false,
            false,
            false,
            true
          ],
          "oos_returns": [
            -0.0010837491999999144,
            -0.027814850699999942,
            -0.011623500700000032,
            0.01023681420000008
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0030638483000000986,
            -0.024407198299999947,
            -0.011623500700000032,
            0.011352458100000087
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.007173001600000114,
            -0.020917301299999955,
            -0.011623500700000032,
            0.012573091800000099
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.011355302300000127,
            -0.017522194099999958,
            -0.011623500700000032,
            0.013685198900000108
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            false,
            false,
            false,
            true
          ],
          "oos_returns": [
            -0.0010837491999999144,
            -0.027345991399999933,
            -0.011623500700000032,
            0.01023681420000008
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0030638483000000986,
            -0.023413027299999934,
            -0.011623500700000032,
            0.011352458100000087
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.007173001600000114,
            -0.019522719799999935,
            -0.011623500700000032,
            0.012573091800000099
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.011355302300000127,
            -0.015549867699999935,
            -0.011623500700000032,
            0.013685198900000108
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            false,
            false,
            false,
            true
          ],
          "oos_returns": [
            -0.0010837491999999144,
            -0.028275079499999932,
            -0.011623500700000032,
            0.010364775800000076
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0030638483000000986,
            -0.025323920799999927,
            -0.011623500700000032,
            0.011608381300000088
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.007173001600000114,
            -0.022327673199999922,
            -0.011623500700000032,
            0.012960975400000099
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.011355302300000127,
            -0.01929019149999992,
            -0.011623500700000032,
            0.014201044100000107
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            false,
            false,
            false,
            true
          ],
          "oos_returns": [
            -0.0005589066999999205,
            -0.027618894499999942,
            -0.011623500700000032,
            0.010488717300000071
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.004063548300000091,
            -0.024110284999999947,
            -0.011623500700000032,
            0.011992266100000076
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.008745016300000102,
            -0.020582317699999957,
            -0.011623500700000032,
            0.013492378100000077
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.013467055000000113,
            -0.01691245399999996,
            -0.011623500700000032,
            0.01497481190000008
          ],
          "positive_window_share": 0.5
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
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.03329896299999994,
            -0.009258798699999973,
            0.01546420790000009,
            -0.03294787779999982
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.03590157619999991,
            -0.005729207699999905,
            0.023120157200000113,
            -0.01847453459999973
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.049329910999999886,
            -0.0022196104999998405,
            0.0218803201000001,
            -0.003929821299999643
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            false,
            true,
            true,
            true
          ],
          "oos_returns": [
            -0.059057787099999884,
            0.0012752016000002267,
            0.014117575200000107,
            0.011127838200000448
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.029915481299999953,
            -0.01079385090000002,
            0.015216565600000101,
            -0.03306226269999986
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.029252388299999935,
            -0.009319521099999999,
            0.02224709280000013,
            -0.019536139699999816
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.03525050989999992,
            -0.007952018299999985,
            0.020449137800000107,
            -0.005948173399999774
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            false,
            false,
            true,
            true
          ],
          "oos_returns": [
            -0.044276274299999904,
            -0.006401569899999966,
            0.01993879620000008,
            0.007898222900000265
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02938483739999996,
            -0.011164933000000023,
            0.012604088700000078,
            -0.03685937229999987
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.028542370199999955,
            -0.010459873800000005,
            0.016701309500000087,
            -0.02760349079999984
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.031704019799999955,
            -0.00982171829999999,
            0.0207797548000001,
            -0.018548393199999805
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.04209145579999991,
            -0.009097372999999978,
            0.020234496800000105,
            -0.009211771199999774
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.028429932799999953,
            -0.010736061700000014,
            0.010670737500000072,
            -0.03753743949999988
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02679111979999994,
            -0.009667447400000001,
            0.012626151600000076,
            -0.029304852599999865
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.025153161799999928,
            -0.008548969299999983,
            0.014492155000000078,
            -0.02119048759999985
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02869536509999993,
            -0.007394165199999966,
            0.016421340700000082,
            -0.01303436089999983
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.029973918199999967,
            -0.011719574300000035,
            0.011714249100000074,
            -0.036278131499999894
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.030111912999999962,
            -0.011767087700000033,
            0.014618458100000082,
            -0.027072388299999892
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.030372540699999957,
            -0.011814601100000037,
            0.01750889530000009,
            -0.017805943699999886
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.030453426199999953,
            -0.011862114500000034,
            0.020431525000000096,
            -0.008528764299999884
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.029493712099999965,
            -0.011623500700000032,
            0.009087508900000072,
            -0.03644940139999989
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02920849869999996,
            -0.011623500700000032,
            0.009185305900000076,
            -0.027191429399999873
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.029026375099999956,
            -0.011623500700000032,
            0.009195907700000078,
            -0.018078333499999856
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.028684052399999955,
            -0.011623500700000032,
            0.009277619400000083,
            -0.008778192099999842
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.028325114199999963,
            -0.011623500700000032,
            0.01023681420000008,
            -0.0375998176999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.026897708099999956,
            -0.011623500700000032,
            0.011352458100000087,
            -0.029770205299999904
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02544117949999995,
            -0.011623500700000032,
            0.012573091800000099,
            -0.02198305489999991
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02388286229999994,
            -0.011623500700000032,
            0.013685198900000108,
            -0.014153442499999912
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.026479054399999973,
            -0.011623500700000032,
            0.01023681420000008,
            -0.0379290799999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.023213359399999973,
            -0.011623500700000032,
            0.011352458100000087,
            -0.030289371999999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.019988401199999978,
            -0.011623500700000032,
            0.012573091800000099,
            -0.022421309399999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.01665870589999998,
            -0.011623500700000032,
            0.013685198900000108,
            -0.014777254999999895
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.025988222399999976,
            -0.011623500700000032,
            0.01023681420000008,
            -0.0379290799999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02216579449999998,
            -0.011623500700000032,
            0.011352458100000087,
            -0.030289371999999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.01826092079999999,
            -0.011623500700000032,
            0.012573091800000099,
            -0.022421309399999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.014458035999999994,
            -0.011623500700000032,
            0.013685198900000108,
            -0.014777254999999895
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.025988222399999976,
            -0.011623500700000032,
            0.010364775800000076,
            -0.0379290799999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.02216579449999998,
            -0.011623500700000032,
            0.011608381300000088,
            -0.030289371999999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.01826092079999999,
            -0.011623500700000032,
            0.012960975400000099,
            -0.022421309399999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.014458035999999994,
            -0.011623500700000032,
            0.014201044100000107,
            -0.014777254999999895
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.026215118599999965,
            -0.011623500700000032,
            0.010488717300000071,
            -0.0379290799999999
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.022816012599999963,
            -0.011623500700000032,
            0.011992266100000076,
            -0.030289371999999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.01928112789999996,
            -0.011623500700000032,
            0.013492378100000077,
            -0.022421309399999898
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            false,
            false,
            true,
            false
          ],
          "oos_returns": [
            -0.015761589599999952,
            -0.011623500700000032,
            0.01497481190000008,
            -0.014777254999999895
          ],
          "positive_window_share": 0.25
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
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.007019244500000035,
            0.01546420790000009,
            -0.03294787779999982,
            -0.052956541999999815
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0035486355999999712,
            0.023120157200000113,
            -0.01847453459999973,
            -0.04526547939999982
          ],
          "positive_window_share": 0.25
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
            3.384010000009527e-05,
            0.0218803201000001,
            -0.003929821299999643,
            -0.04365377229999983
          ],
          "positive_window_share": 0.5
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
            0.0035790935000001613,
            0.014117575200000107,
            0.011127838200000448,
            -0.03759888359999981
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.008380509800000081,
            0.015216565600000101,
            -0.03306226269999986,
            -0.0556933186999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.006803129300000061,
            0.02224709280000013,
            -0.019536139699999816,
            -0.051840268799999804
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.005251986500000038,
            0.020449137800000107,
            -0.005948173399999774,
            -0.0480014146999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.003700725500000019,
            0.01993879620000008,
            0.007898222900000265,
            -0.04782570679999981
          ],
          "positive_window_share": 0.5
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
            -0.008899757600000086,
            0.012604088700000078,
            -0.03685937229999987,
            -0.053995749999999815
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.008223246900000074,
            0.016701309500000087,
            -0.02760349079999984,
            -0.048457906999999835
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0075181877000000605,
            0.0207797548000001,
            -0.018548393199999805,
            -0.04293164309999985
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.006878592400000046,
            0.020234496800000105,
            -0.009211771199999774,
            -0.04394204789999985
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
            -0.009595483300000096,
            0.010670737500000072,
            -0.03753743949999988,
            -0.053733813599999805
          ],
          "positive_window_share": 0.25
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
            -0.009711950200000083,
            0.012626151600000076,
            -0.029304852599999865,
            -0.04789905969999981
          ],
          "positive_window_share": 0.25
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
            -0.00982831710000008,
            0.014492155000000078,
            -0.02119048759999985,
            -0.04194573649999981
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.00991884850000007,
            0.016421340700000082,
            -0.01303436089999983,
            -0.03605258269999981
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
            -0.009481159900000098,
            0.011714249100000074,
            -0.036278131499999894,
            -0.057814870799999814
          ],
          "positive_window_share": 0.25
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
            -0.009528673300000103,
            0.014618458100000082,
            -0.027072388299999892,
            -0.05625782059999982
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0095761867000001,
            0.01750889530000009,
            -0.017805943699999886,
            -0.05468029399999983
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.009623700100000097,
            0.020431525000000096,
            -0.008528764299999884,
            -0.05312324379999984
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.009087508900000072,
            -0.03644940139999989,
            -0.059221433699999805
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
            -0.0093836465000001,
            0.009185305900000076,
            -0.027191429399999873,
            -0.0590934720999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.009195907700000078,
            -0.018078333499999856,
            -0.058965510499999804
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.009277619400000083,
            -0.008778192099999842,
            -0.0588375488999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.01023681420000008,
            -0.0375998176999999,
            -0.058849545299999806
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
            -0.0093836465000001,
            0.011352458100000087,
            -0.029770205299999904,
            -0.05833769889999982
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.012573091800000099,
            -0.02198305489999991,
            -0.057841847699999824
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.013685198900000108,
            -0.014153442499999912,
            -0.05733000129999983
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.01023681420000008,
            -0.0379290799999999,
            -0.05881855459999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.011352458100000087,
            -0.030289371999999898,
            -0.05827471779999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.012573091800000099,
            -0.022421309399999898,
            -0.05774787589999982
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.013685198900000108,
            -0.014777254999999895,
            -0.05722451549999983
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.01023681420000008,
            -0.0379290799999999,
            -0.05767189869999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.011352458100000087,
            -0.030289371999999898,
            -0.05601887729999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.012573091800000099,
            -0.022421309399999898,
            -0.05434537949999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.013685198900000108,
            -0.014777254999999895,
            -0.05263837429999982
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.010364775800000076,
            -0.0379290799999999,
            -0.05767189869999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.011608381300000088,
            -0.030289371999999898,
            -0.05601887729999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.012960975400000099,
            -0.022421309399999898,
            -0.05434537949999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.014201044100000107,
            -0.014777254999999895,
            -0.05263837429999982
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.010488717300000071,
            -0.0379290799999999,
            -0.05767189869999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.011992266100000076,
            -0.030289371999999898,
            -0.05601887729999981
          ],
          "positive_window_share": 0.25
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
            -0.0093836465000001,
            0.013492378100000077,
            -0.022421309399999898,
            -0.05434537949999981
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0093836465000001,
            0.01497481190000008,
            -0.014777254999999895,
            -0.05263837429999982
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
            true,
            false,
            false,
            false
          ],
          "oos_returns": [
            0.010464264900000162,
            -0.03294787779999982,
            -0.052956541999999815,
            -0.027290137299999948
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
            0.017033401800000195,
            -0.01847453459999973,
            -0.04526547939999982,
            -0.022162553599999923
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
            0.014668068000000183,
            -0.003929821299999643,
            -0.04365377229999983,
            -0.019047299999999875
          ],
          "positive_window_share": 0.25
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
            0.012062537600000162,
            0.011127838200000448,
            -0.03759888359999981,
            -0.024129818899999857
          ],
          "positive_window_share": 0.5
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
            0.011265854900000167,
            -0.03306226269999986,
            -0.0556933186999998,
            -0.03011529199999994
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
            0.0183397378000002,
            -0.019536139699999816,
            -0.051840268799999804,
            -0.02458978609999991
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
            0.016545367400000174,
            -0.005948173399999774,
            -0.0480014146999998,
            -0.019076409099999882
          ],
          "positive_window_share": 0.25
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
            0.01597559740000015,
            0.007898222900000265,
            -0.04782570679999981,
            -0.02232982729999988
          ],
          "positive_window_share": 0.5
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
            0.007943109100000147,
            -0.03685937229999987,
            -0.053995749999999815,
            -0.029133689799999973
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
            0.01121360650000016,
            -0.02760349079999984,
            -0.048457906999999835,
            -0.02298985549999998
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
            0.014312919500000174,
            -0.018548393199999805,
            -0.04293164309999985,
            -0.016732202799999984
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
            0.012951541100000186,
            -0.009211771199999774,
            -0.04394204789999985,
            -0.01053894189999999
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
            0.005853391000000138,
            -0.03753743949999988,
            -0.053733813599999805,
            -0.029996943699999966
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
            0.006477852800000142,
            -0.029304852599999865,
            -0.04789905969999981,
            -0.024720748999999966
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
            0.007294868500000145,
            -0.02119048759999985,
            -0.04194573649999981,
            -0.019449141799999965
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
            0.008008302700000147,
            -0.01303436089999983,
            -0.03605258269999981,
            -0.014113212499999965
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
            0.006573779100000142,
            -0.036278131499999894,
            -0.057814870799999814,
            -0.03216659719999996
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
            0.008083496700000147,
            -0.027072388299999892,
            -0.05625782059999982,
            -0.029205112199999952
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
            0.009605427100000154,
            -0.017805943699999886,
            -0.05468029399999983,
            -0.026307136099999948
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
            0.01107773780000016,
            -0.008528764299999884,
            -0.05312324379999984,
            -0.02333368499999994
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
            0.005199645700000137,
            -0.03644940139999989,
            -0.059221433699999805,
            -0.031608764599999964
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
            0.005278348400000139,
            -0.027191429399999873,
            -0.0590934720999998,
            -0.02812543619999996
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
            0.005376145400000143,
            -0.018078333499999856,
            -0.058965510499999804,
            -0.024588223999999957
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
            0.005386747200000146,
            -0.008778192099999842,
            -0.0588375488999998,
            -0.021093029499999954
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
            0.006352187800000145,
            -0.0375998176999999,
            -0.058849545299999806,
            -0.031305855499999966
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
            0.0074643949000001535,
            -0.029770205299999904,
            -0.05833769889999982,
            -0.027512620099999975
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
            0.008648039700000162,
            -0.02198305489999991,
            -0.057841847699999824,
            -0.023665500899999976
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
            0.009868673400000173,
            -0.014153442499999912,
            -0.05733000129999983,
            -0.01986039939999998
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
            0.006352187800000145,
            -0.0379290799999999,
            -0.05881855459999981,
            -0.030914972799999975
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
            0.0074643949000001535,
            -0.030289371999999898,
            -0.05827471779999981,
            -0.026687867599999984
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
            0.008648039700000162,
            -0.022421309399999898,
            -0.05774787589999982,
            -0.022394812499999993
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
            0.009868673400000173,
            -0.014777254999999895,
            -0.05722451549999983,
            -0.018113923500000004
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
            0.006352187800000145,
            -0.0379290799999999,
            -0.05767189869999981,
            -0.03181868659999997
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
            0.0074643949000001535,
            -0.030289371999999898,
            -0.05601887729999981,
            -0.028565930499999975
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
            0.008648039700000162,
            -0.022421309399999898,
            -0.05434537949999981,
            -0.025296065999999978
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
            0.009868673400000173,
            -0.014777254999999895,
            -0.05263837429999982,
            -0.022014235399999978
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
            0.006480149400000145,
            -0.0379290799999999,
            -0.05767189869999981,
            -0.03310362059999997
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
            0.007720318100000154,
            -0.030289371999999898,
            -0.05601887729999981,
            -0.031173802099999974
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
            0.009031924500000163,
            -0.022421309399999898,
            -0.05434537949999981,
            -0.029283369399999974
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
            0.010340094100000172,
            -0.014777254999999895,
            -0.05263837429999982,
            -0.02741453259999998
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
            0.006672091800000137,
            -0.0379290799999999,
            -0.05767189869999981,
            -0.03488307159999997
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
            0.008104202900000142,
            -0.030289371999999898,
            -0.05601887729999981,
            -0.03488307159999997
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
            0.009607751700000142,
            -0.022421309399999898,
            -0.05434537949999981,
            -0.03488307159999997
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
            0.011039862800000147,
            -0.014777254999999895,
            -0.05263837429999982,
            -0.03488307159999997
          ],
          "positive_window_share": 0.25
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
    "data_fingerprint": "dbe1d2a67bbf24d2e6b233d59ec5aeb83d26ea5d23dd543b8a5cd1763739a307",
    "run_mode": "research_diagnostic",
    "research_only": true,
    "activation_eligible": false,
    "shadow_run_eligible": false,
    "trading_authorized": false,
    "target": {
      "exposure_id": "csi_dividend",
      "stock_code": "515080.SH",
      "sub_layer": "defensive_dividend_etf",
      "scope": "formal"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
        "config": {
          "grid": {
            "step_pct": 0.01,
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
        "window_id": "wf_001",
        "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
        "config": {
          "grid": {
            "step_pct": 0.01,
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
        "window_id": "wf_002",
        "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
        "config": {
          "grid": {
            "step_pct": 0.01,
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
        "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
        "config": {
          "grid": {
            "step_pct": 0.01,
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
        "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
        "config": {
          "grid": {
            "step_pct": 0.015,
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
            "step_pct": 0.01,
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
              "step_pct": 0.01,
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
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.05906474155064645,
              "annual_volatility": 0.12027945796823028,
              "sharpe": -0.49106258498643524,
              "sortino": -0.7226369452431678,
              "calmar": -0.582499215541926,
              "worst_126_session_return": -0.02974744969999943,
              "cvar5": -0.017442761714884663,
              "win_rate": 0.464,
              "payoff_ratio": 0.9454928249585886,
              "profit_factor": 0.9294675228406464,
              "turnover": 0.986711089919292,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9984954954954954,
              "max_drawdown": -0.10139883449576115,
              "recovery_sessions": 1,
              "total_cost": 39.94497
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
            "validation_start": "2024-02-19",
            "validation_end": "2024-08-20",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.03341166538114615,
              "annual_volatility": 0.06024205360757253,
              "sharpe": -0.5546236122492717,
              "sortino": -0.808117047398304,
              "calmar": -0.6322094415674071,
              "worst_126_session_return": -0.0167151676000018,
              "cvar5": -0.008771386928373426,
              "win_rate": 0.464,
              "payoff_ratio": 0.9793453807584436,
              "profit_factor": 0.916161807806286,
              "turnover": 0.6108443508971437,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.06949720754716981,
              "max_drawdown": -0.05284904524410483,
              "recovery_sessions": 1,
              "total_cost": 283.41676
            }
          }
        ]
      },
      {
        "window_id": "wf_001",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.01,
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
              "step_pct": 0.01,
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
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.06890755696605422,
              "annual_volatility": 0.23355524824193227,
              "sharpe": 0.29503750176778354,
              "sortino": 0.39272410633252197,
              "calmar": 0.6539593740486608,
              "worst_126_session_return": 0.033606500199998335,
              "cvar5": -0.030748086705722655,
              "win_rate": 0.472,
              "payoff_ratio": 1.123692216224961,
              "profit_factor": 1.0868498484798803,
              "turnover": 0.9584028970177508,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.998996996996997,
              "max_drawdown": -0.10536978243686257,
              "recovery_sessions": 23,
              "total_cost": 39.94998
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
            "validation_start": "2024-08-21",
            "validation_end": "2025-03-04",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.03810572431961057,
              "annual_volatility": 0.1172206803920402,
              "sharpe": 0.3250768054934282,
              "sortino": 0.43615178236387225,
              "calmar": 0.6997840027824208,
              "worst_126_session_return": 0.018723541200000637,
              "cvar5": -0.015463723247222061,
              "win_rate": 0.472,
              "payoff_ratio": 1.1728810320212493,
              "profit_factor": 1.0812497013945892,
              "turnover": 0.6924230945393555,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.06438145454545455,
              "max_drawdown": -0.054453551621783114,
              "recovery_sessions": 23,
              "total_cost": 351.24588
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
              "step_pct": 0.01,
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
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.09989901020221614,
              "annual_volatility": 0.12893569719462258,
              "sharpe": 0.7747971459868335,
              "sortino": 0.6754988701593668,
              "calmar": 1.446092775144212,
              "worst_126_session_return": 0.04836450199999831,
              "cvar5": -0.021644158738771162,
              "win_rate": 0.576,
              "payoff_ratio": 0.7896247354169865,
              "profit_factor": 1.1844371031254797,
              "turnover": 0.9712957180213118,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.998978978978979,
              "max_drawdown": -0.0690820201299005,
              "recovery_sessions": 1,
              "total_cost": 39.9498
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
            "validation_start": "2025-03-05",
            "validation_end": "2025-09-03",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.045842688821312816,
              "annual_volatility": 0.0645200468254744,
              "sharpe": 0.7105185299278609,
              "sortino": 0.6268461739532405,
              "calmar": 1.311923872661973,
              "worst_126_session_return": 0.02248262049999994,
              "cvar5": -0.010843597636724803,
              "win_rate": 0.576,
              "payoff_ratio": 0.8094365381587227,
              "profit_factor": 1.1655886149485606,
              "turnover": 0.5934454827326571,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.07362428571428571,
              "max_drawdown": -0.03494310133124967,
              "recovery_sessions": 1,
              "total_cost": 263.03795
            }
          }
        ]
      },
      {
        "window_id": "wf_003",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.01,
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
              "step_pct": 0.01,
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
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.0818475865627395,
              "annual_volatility": 0.11914746118675354,
              "sharpe": 0.6869436054071714,
              "sortino": 0.9906898488367337,
              "calmar": 1.183754275338277,
              "worst_126_session_return": 0.039794367600000324,
              "cvar5": -0.017808038499318685,
              "win_rate": 0.536,
              "payoff_ratio": 0.9096293677323709,
              "profit_factor": 1.1286142155197936,
              "turnover": 0.9841210985886895,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 3.0003243243243243,
              "max_drawdown": -0.06914237884323604,
              "recovery_sessions": 1,
              "total_cost": 39.96324
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
            "validation_start": "2025-09-04",
            "validation_end": "2026-03-18",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.036831492074266725,
              "annual_volatility": 0.059605168680970495,
              "sharpe": 0.6179244667757399,
              "sortino": 0.8937698252133706,
              "calmar": 1.034583126515858,
              "worst_126_session_return": 0.01810309060000037,
              "cvar5": -0.00891963274406645,
              "win_rate": 0.536,
              "payoff_ratio": 0.8969154404383134,
              "profit_factor": 1.1128395279512406,
              "turnover": 0.6057059915935918,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.07316376,
              "max_drawdown": -0.035600321646751865,
              "recovery_sessions": 1,
              "total_cost": 268.29094
            }
          }
        ]
      },
      {
        "window_id": "wf_004",
        "profile_id": "grid_core",
        "execution_config": {
          "grid": {
            "step_pct": 0.015,
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
              "step_pct": 0.015,
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
          "spec_hash": "cc00abb09e1788472dcb337deebafcaaa2910da7ab66b37a1b48d613bdef69ea"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "3274e19422069735d2b29879bfd6d749ea2c0e1aef5687971ae4d05922309926",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.08858399074854784,
              "annual_volatility": 0.15639639629919672,
              "sharpe": -0.5664068536405453,
              "sortino": -0.8919892589737053,
              "calmar": -0.6230648100769278,
              "worst_126_session_return": -0.044967434099999926,
              "cvar5": -0.02064909112303694,
              "win_rate": 0.472,
              "payoff_ratio": 0.9666376912731148,
              "profit_factor": 0.9198648997598996,
              "turnover": 1.02884376843065,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.998339339339339,
              "max_drawdown": -0.142174600965846,
              "recovery_sessions": 7,
              "total_cost": 39.94341
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "34d1bbf0b5d64c261e0ab422e7dea8f250893e1a2af8fd493720da2286ef93a2",
            "validation_start": "2026-03-19",
            "validation_end": "2026-09-17",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.049112810439462584,
              "annual_volatility": 0.07825873235690053,
              "sharpe": -0.6275697159964542,
              "sortino": -0.9796261616477379,
              "calmar": -0.660873467086733,
              "worst_126_session_return": -0.024670662100000795,
              "cvar5": -0.01036328444074632,
              "win_rate": 0.472,
              "payoff_ratio": 0.9835349273852118,
              "profit_factor": 0.9066962611832421,
              "turnover": 0.6729628906980926,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.05758321739130434,
              "max_drawdown": -0.07431499808270714,
              "recovery_sessions": 7,
              "total_cost": 364.86621
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
      "experiment_id": "round2-dividend-20260917",
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
        "515080.SH"
      ]
    },
    "experiment_hash": "61a477ca27bcbffd8354b19491428ec2b3f460b86bf4dcbae341a10e10c1fe5b",
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
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
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
            "cost_drag": 0.001635634475,
            "cvar5_improvement": 0.0158690990974795,
            "drawdown_improvement": 0.08273256874910262,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2264971782832259,
            "sortino_excess": -0.29468131308505807,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00180355295,
            "cvar5_improvement": 0.015963514633383417,
            "drawdown_improvement": 0.08341629619721652,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2410473772436485,
            "sortino_excess": -0.41710878907687177,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002191775675,
            "cvar5_improvement": 0.01669344890417396,
            "drawdown_improvement": 0.08703297002744279,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19176177814431794,
            "sortino_excess": -0.46296316903442103,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016260519249999999,
            "cvar5_improvement": 0.014853087522356496,
            "drawdown_improvement": 0.07587331758364738,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5088202678617211,
            "sortino_excess": -0.6866322379706901,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034265548250000002,
            "cvar5_improvement": 0.016415149191884318,
            "drawdown_improvement": 0.08724260997520175,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2092057862865819,
            "sortino_excess": -0.46219464413503486,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001716894525,
            "cvar5_improvement": 0.014992207470491296,
            "drawdown_improvement": 0.07669922285544709,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5099177061461604,
            "sortino_excess": -0.6986054641372204,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00203524255,
            "cvar5_improvement": 0.015597614448637918,
            "drawdown_improvement": 0.07982486897792962,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3679466205715218,
            "sortino_excess": -0.5474469797323867,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001694820025,
            "cvar5_improvement": 0.015322418821842654,
            "drawdown_improvement": 0.07803349245077226,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41571228359866663,
            "sortino_excess": -0.5855949508092891,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001623710775,
            "cvar5_improvement": 0.015651362895654802,
            "drawdown_improvement": 0.08153287748197352,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20394263763432952,
            "sortino_excess": -0.27797244903326956,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001638849425,
            "cvar5_improvement": 0.015119872846475877,
            "drawdown_improvement": 0.07750634112175792,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4372951128351479,
            "sortino_excess": -0.5891981313892763,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00182509785,
            "cvar5_improvement": 0.015399710875507905,
            "drawdown_improvement": 0.07966016349779612,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4515722476354091,
            "sortino_excess": -0.6483581593737499,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001612386525,
            "cvar5_improvement": 0.015136175822375406,
            "drawdown_improvement": 0.07804530278700364,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.40265833877710644,
            "sortino_excess": -0.5461602415881044,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00362451435,
            "cvar5_improvement": 0.016343351642503706,
            "drawdown_improvement": 0.08637351031168206,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.10972461415807339,
            "sortino_excess": -0.3398078633134595,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001868356325,
            "cvar5_improvement": 0.01572965821659668,
            "drawdown_improvement": 0.0815650623310874,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3691195157494645,
            "sortino_excess": -0.5713669809273171,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002911526225,
            "cvar5_improvement": 0.016320803996104045,
            "drawdown_improvement": 0.087593491869937,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.14565743756723115,
            "sortino_excess": -0.3949798262067671,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00339769615,
            "cvar5_improvement": 0.016421543126677225,
            "drawdown_improvement": 0.08792229497058002,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23849719143368453,
            "sortino_excess": -0.47464072389031686,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001717475175,
            "cvar5_improvement": 0.01565441938259245,
            "drawdown_improvement": 0.07994153370609436,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3209394818752363,
            "sortino_excess": -0.48103645545822193,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001774691875,
            "cvar5_improvement": 0.015691267422770203,
            "drawdown_improvement": 0.08163441003788635,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3414242338665101,
            "sortino_excess": -0.5149008032263536,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016301229250000001,
            "cvar5_improvement": 0.01560907533139164,
            "drawdown_improvement": 0.08090142051023594,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.32416330432686635,
            "sortino_excess": -0.42044685828431094,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001617956475,
            "cvar5_improvement": 0.01540565545364568,
            "drawdown_improvement": 0.07998082980807103,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.30717663336314477,
            "sortino_excess": -0.41736412174061666,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001947872625,
            "cvar5_improvement": 0.015128716507135601,
            "drawdown_improvement": 0.076947754731466,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.48691079610938215,
            "sortino_excess": -0.6748553620861637,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019127335499999998,
            "cvar5_improvement": 0.015989796229783585,
            "drawdown_improvement": 0.08315921530426798,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27470313731120277,
            "sortino_excess": -0.4932391788542059,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00325156765,
            "cvar5_improvement": 0.015807223315701006,
            "drawdown_improvement": 0.08207329065263472,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41822203391075424,
            "sortino_excess": -0.632123985118431,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.002139782525,
            "cvar5_improvement": 0.016151694446461806,
            "drawdown_improvement": 0.08393881803655415,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3129264854663462,
            "sortino_excess": -0.5193832020137045,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00161903355,
            "cvar5_improvement": 0.014938437024899566,
            "drawdown_improvement": 0.07645098691847116,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.49891670422026774,
            "sortino_excess": -0.6667209289219571,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0021870934499999997,
            "cvar5_improvement": 0.016580599541722505,
            "drawdown_improvement": 0.08665262382008534,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16987505643197115,
            "sortino_excess": -0.41028205245733684,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002741895925,
            "cvar5_improvement": 0.016250973495546467,
            "drawdown_improvement": 0.08674534158332098,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2989586740996946,
            "sortino_excess": -0.5491983581089808,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001672824975,
            "cvar5_improvement": 0.014951924100904655,
            "drawdown_improvement": 0.07610482398180224,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5019613024803355,
            "sortino_excess": -0.6876241927676853,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002826906475,
            "cvar5_improvement": 0.01626064715333867,
            "drawdown_improvement": 0.0867365211703941,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1772850859620202,
            "sortino_excess": -0.3793019518481865,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001739668825,
            "cvar5_improvement": 0.01590959907111239,
            "drawdown_improvement": 0.08144695147729492,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.21632339562443142,
            "sortino_excess": -0.3785035545402773,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016297566249999999,
            "cvar5_improvement": 0.015613824064536225,
            "drawdown_improvement": 0.0809078159901453,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34414282990485984,
            "sortino_excess": -0.44982866111485587,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00163514655,
            "cvar5_improvement": 0.015875228814998928,
            "drawdown_improvement": 0.08273888980466268,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.25452889298536935,
            "sortino_excess": -0.3369505286305212,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016245170999999998,
            "cvar5_improvement": 0.015290264654910377,
            "drawdown_improvement": 0.07867665253541006,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4149301592116084,
            "sortino_excess": -0.5462253988772583,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0021221701749999998,
            "cvar5_improvement": 0.015861672229887876,
            "drawdown_improvement": 0.08185821791197845,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23149585413220755,
            "sortino_excess": -0.42744625850174767,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001618980525,
            "cvar5_improvement": 0.014940302266315476,
            "drawdown_improvement": 0.07644673222023154,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5051199716234631,
            "sortino_excess": -0.6750912284771327,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00213765845,
            "cvar5_improvement": 0.01591639716765544,
            "drawdown_improvement": 0.08247006048134073,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27073352157604785,
            "sortino_excess": -0.49574184948568234,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017455704499999998,
            "cvar5_improvement": 0.015354783463404801,
            "drawdown_improvement": 0.0792497088406166,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.43223310560409256,
            "sortino_excess": -0.6120076327071043,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00165112245,
            "cvar5_improvement": 0.015392154637048064,
            "drawdown_improvement": 0.07917848873800809,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.35968617734169567,
            "sortino_excess": -0.48191470888686516,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016641142,
            "cvar5_improvement": 0.01565758418910941,
            "drawdown_improvement": 0.08042660916198177,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27702237613138986,
            "sortino_excess": -0.36933086069402554,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002044153775,
            "cvar5_improvement": 0.015445609232933356,
            "drawdown_improvement": 0.07909702570428978,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4659472876501025,
            "sortino_excess": -0.6650667290649911,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001606729375,
            "cvar5_improvement": 0.014861721258196162,
            "drawdown_improvement": 0.07614175697842324,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4918101743380082,
            "sortino_excess": -0.6652784382737632,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00162427415,
            "cvar5_improvement": 0.015293885003728778,
            "drawdown_improvement": 0.07868312381794176,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.42807622629219694,
            "sortino_excess": -0.5651630224164873,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00178146035,
            "cvar5_improvement": 0.015022173949598323,
            "drawdown_improvement": 0.07689851238732079,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5205958360194913,
            "sortino_excess": -0.7173815944077884,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026051470499999997,
            "cvar5_improvement": 0.015615899976765405,
            "drawdown_improvement": 0.08131552130861033,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4236541874211217,
            "sortino_excess": -0.6197693923096673,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.004586228704420088,
          "execution_cost": 269.58745,
          "grid_return": 0.015780960537847763,
          "reconciliation_error": -8.673617379884035e-18,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.00339769615,
            "cvar5_improvement": 0.016421543126677225,
            "drawdown_improvement": 0.08792229497058002,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23849719143368453,
            "sortino_excess": -0.47464072389031686,
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
              "unit_pct": 0.2
            },
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
          "policy_id": "grid_only",
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be",
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
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
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
            "cost_drag": 0.001497967725,
            "cvar5_improvement": 0.011917749175975215,
            "drawdown_improvement": 0.07925345183844693,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14897319100628503,
            "sortino_excess": 0.18400536935485723,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001587603425,
            "cvar5_improvement": 0.011741210353122172,
            "drawdown_improvement": 0.07764067420767129,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08704176702537324,
            "sortino_excess": -0.23548334482301403,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002033491425,
            "cvar5_improvement": 0.01241683788726979,
            "drawdown_improvement": 0.08086550050719929,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2538975070389231,
            "sortino_excess": 0.36856493694853965,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001468139325,
            "cvar5_improvement": 0.010908336437336269,
            "drawdown_improvement": 0.07246204710903142,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18636045606269008,
            "sortino_excess": -0.3229742637439449,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0031470205750000002,
            "cvar5_improvement": 0.012101255808752256,
            "drawdown_improvement": 0.08141360315483304,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.22974347888290964,
            "sortino_excess": 0.2194874987999422,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001521180325,
            "cvar5_improvement": 0.010930024058231494,
            "drawdown_improvement": 0.07252970903820646,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.229824098547286,
            "sortino_excess": -0.39054344545898545,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018482773499999999,
            "cvar5_improvement": 0.011606555752754114,
            "drawdown_improvement": 0.07577782686668308,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.026618638007296788,
            "sortino_excess": -0.13529365832452026,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015435037249999998,
            "cvar5_improvement": 0.01123055222215227,
            "drawdown_improvement": 0.0743833175168642,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.12674881490785578,
            "sortino_excess": -0.25829592907081794,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001485272875,
            "cvar5_improvement": 0.011842528033945037,
            "drawdown_improvement": 0.07730415092902782,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.1571083623606676,
            "sortino_excess": 0.1945005637284522,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014740489,
            "cvar5_improvement": 0.011246077456905385,
            "drawdown_improvement": 0.07403510258415763,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09673401221292303,
            "sortino_excess": -0.1941377268951483,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001691199375,
            "cvar5_improvement": 0.011546412647808087,
            "drawdown_improvement": 0.07575624836730116,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.05480473754729252,
            "sortino_excess": -0.17875178565256608,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00147424375,
            "cvar5_improvement": 0.011234761817690531,
            "drawdown_improvement": 0.07403450291455316,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.07271710629680868,
            "sortino_excess": -0.16032801631835922,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003252474125,
            "cvar5_improvement": 0.012034570456037647,
            "drawdown_improvement": 0.08104126057556363,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.125329954481062,
            "sortino_excess": -0.002157617005940804,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017369485750000002,
            "cvar5_improvement": 0.011925854386265778,
            "drawdown_improvement": 0.07830414870213051,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.08743341295800526,
            "sortino_excess": 0.007562512590448628,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002535014325,
            "cvar5_improvement": 0.0124646465009762,
            "drawdown_improvement": 0.08216263637311788,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2672078929149838,
            "sortino_excess": 0.3566761793783108,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0032101422249999996,
            "cvar5_improvement": 0.012118684056038345,
            "drawdown_improvement": 0.08086590154254153,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.30158894137983305,
            "sortino_excess": 0.7930529514900155,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001565580425,
            "cvar5_improvement": 0.011521360610860565,
            "drawdown_improvement": 0.07619290972828124,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.04663670263600518,
            "sortino_excess": -0.1607311059111748,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001565200625,
            "cvar5_improvement": 0.011559036916927477,
            "drawdown_improvement": 0.07592643009087308,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.13972458194127924,
            "sortino_excess": -0.2946988337880035,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014920327,
            "cvar5_improvement": 0.011676316460117223,
            "drawdown_improvement": 0.07716357820178246,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.033343487803086144,
            "sortino_excess": 0.00997788147717471,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014796069249999998,
            "cvar5_improvement": 0.011557855616364549,
            "drawdown_improvement": 0.07567429246550642,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.03793044516799014,
            "sortino_excess": 0.00594618498419211,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00176649575,
            "cvar5_improvement": 0.01111150225385689,
            "drawdown_improvement": 0.07326688057576433,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16428824400354042,
            "sortino_excess": -0.31110594473706965,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017834955,
            "cvar5_improvement": 0.012194286784934108,
            "drawdown_improvement": 0.08074094710119117,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.24811572609773008,
            "sortino_excess": 0.20064856567623507,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0029088774,
            "cvar5_improvement": 0.011587327636852131,
            "drawdown_improvement": 0.07585523987800616,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.12939584705391372,
            "sortino_excess": -0.3068659948525789,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.001966028725,
            "cvar5_improvement": 0.011924122451018032,
            "drawdown_improvement": 0.07810069460253105,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.00899152664131174,
            "sortino_excess": -0.1143004016183296,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014808577,
            "cvar5_improvement": 0.010949516640293954,
            "drawdown_improvement": 0.07292619696470015,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.17655303754375248,
            "sortino_excess": -0.3037156889220156,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002014135575,
            "cvar5_improvement": 0.012240441516818756,
            "drawdown_improvement": 0.08084428983400055,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.1386173289546252,
            "sortino_excess": 0.1235594110744174,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002553213275,
            "cvar5_improvement": 0.012337424197594548,
            "drawdown_improvement": 0.08146019174879862,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2447253228795036,
            "sortino_excess": 0.33234638029638586,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001521664925,
            "cvar5_improvement": 0.01089644853046351,
            "drawdown_improvement": 0.072585274669562,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20166131031385565,
            "sortino_excess": -0.3515770370669282,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025114744,
            "cvar5_improvement": 0.012237875270159456,
            "drawdown_improvement": 0.08126811475882695,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.1321919712252829,
            "sortino_excess": 0.09713582371904653,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015877578499999998,
            "cvar5_improvement": 0.0117113021028265,
            "drawdown_improvement": 0.07796250737982122,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.03718118218305198,
            "sortino_excess": -0.057198596074329755,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001491928075,
            "cvar5_improvement": 0.011676141691296946,
            "drawdown_improvement": 0.07715710464750869,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.020771067331837575,
            "sortino_excess": -0.01110968272758378,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001497549325,
            "cvar5_improvement": 0.011917340396211843,
            "drawdown_improvement": 0.07925977289400699,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.13101249695114214,
            "sortino_excess": 0.15296005512847533,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001486806325,
            "cvar5_improvement": 0.01133118732543537,
            "drawdown_improvement": 0.07501109522262472,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0754666443486146,
            "sortino_excess": -0.15367601644010048,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019304474,
            "cvar5_improvement": 0.011927540122495103,
            "drawdown_improvement": 0.07831184266036578,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.13487192384816732,
            "sortino_excess": 0.09226747661915241,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014808225249999998,
            "cvar5_improvement": 0.010949066224300094,
            "drawdown_improvement": 0.072923487913996,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18054933271211543,
            "sortino_excess": -0.3097181776516828,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019548808,
            "cvar5_improvement": 0.01217789116798126,
            "drawdown_improvement": 0.07958383261143492,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.27847898373126906,
            "sortino_excess": 0.3182234735429612,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015433359,
            "cvar5_improvement": 0.0112730173745513,
            "drawdown_improvement": 0.07423249832597448,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18623953204669896,
            "sortino_excess": -0.3438334156542635,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014788001499999998,
            "cvar5_improvement": 0.011578737166282351,
            "drawdown_improvement": 0.0757075061684612,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.0012846504637501893,
            "sortino_excess": -0.0454952232991942,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001484837375,
            "cvar5_improvement": 0.01186113675140461,
            "drawdown_improvement": 0.07729618973261099,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.10574592747837018,
            "sortino_excess": 0.12079436420352693,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001869677375,
            "cvar5_improvement": 0.011331472794848519,
            "drawdown_improvement": 0.07436603379596535,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16079594668640101,
            "sortino_excess": -0.30857485854996936,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014686470750000001,
            "cvar5_improvement": 0.010901932661015495,
            "drawdown_improvement": 0.07245055418980714,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.17453845518158556,
            "sortino_excess": -0.3061246287942213,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001486599075,
            "cvar5_improvement": 0.011332161007470753,
            "drawdown_improvement": 0.07502037752330121,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08392150700260824,
            "sortino_excess": -0.16749728186240037,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001644622825,
            "cvar5_improvement": 0.01109175481581986,
            "drawdown_improvement": 0.07330663355741715,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.173643486686406,
            "sortino_excess": -0.3262260746958685,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002315767425,
            "cvar5_improvement": 0.011604486175317591,
            "drawdown_improvement": 0.0760295054053165,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11671045827944866,
            "sortino_excess": -0.2569918062803326,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.0192758935950959,
          "execution_cost": 485.36616,
          "grid_return": 0.01923445610852774,
          "reconciliation_error": 1.214306433183765e-17,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.0032101422249999996,
            "cvar5_improvement": 0.012118684056038345,
            "drawdown_improvement": 0.08086590154254153,
            "exposure_ratio": 0.7380952380952381,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.30158894137983305,
            "sortino_excess": 0.7930529514900155,
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
              "unit_pct": 0.2
            },
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
          "policy_id": "grid_only",
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
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
            "cost_drag": 0.001536178075,
            "cvar5_improvement": 0.01198989376513981,
            "drawdown_improvement": 0.06306556838669644,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.10072790236216365,
            "sortino_excess": -0.1403518963315398,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001744061325,
            "cvar5_improvement": 0.01197592433380099,
            "drawdown_improvement": 0.06513858098616876,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.26520138454145786,
            "sortino_excess": -0.42516270295476494,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002280055675,
            "cvar5_improvement": 0.011998349736092397,
            "drawdown_improvement": 0.06512698467639644,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.25220899577201733,
            "sortino_excess": -0.4290588002609132,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014917867000000002,
            "cvar5_improvement": 0.011057761586225599,
            "drawdown_improvement": 0.05620195726635385,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3752258651982814,
            "sortino_excess": -0.5197340587028366,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0035672855500000003,
            "cvar5_improvement": 0.011382279264941151,
            "drawdown_improvement": 0.0668758487731618,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2600569810550012,
            "sortino_excess": -0.4476777959590702,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015980562000000001,
            "cvar5_improvement": 0.01108039725975506,
            "drawdown_improvement": 0.05697344058622886,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4135213882293061,
            "sortino_excess": -0.5874124441963541,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001938096925,
            "cvar5_improvement": 0.01154142089781554,
            "drawdown_improvement": 0.06012591850714036,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.29106735276350443,
            "sortino_excess": -0.448461580233546,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015752688749999999,
            "cvar5_improvement": 0.011654266047881376,
            "drawdown_improvement": 0.0596660499860569,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.33493499853994874,
            "sortino_excess": -0.4944786167996785,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001523663225,
            "cvar5_improvement": 0.011912969602044124,
            "drawdown_improvement": 0.0611097825021171,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11864090325527928,
            "sortino_excess": -0.166570535700329,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015063513499999999,
            "cvar5_improvement": 0.011417901659931293,
            "drawdown_improvement": 0.05848472402297497,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2869290109873618,
            "sortino_excess": -0.39766881383362945,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017097625999999999,
            "cvar5_improvement": 0.01174931827882684,
            "drawdown_improvement": 0.060990713531674234,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.32252991238990125,
            "sortino_excess": -0.4951372033891205,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001493434675,
            "cvar5_improvement": 0.011326069684185269,
            "drawdown_improvement": 0.05753216762976071,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.29716065526928637,
            "sortino_excess": -0.4200162143210575,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0035258202,
            "cvar5_improvement": 0.011561492622760189,
            "drawdown_improvement": 0.06524292397711448,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20868858972148036,
            "sortino_excess": -0.4156859062583921,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017650774250000001,
            "cvar5_improvement": 0.012204992732461312,
            "drawdown_improvement": 0.06456574785801769,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.24086555899580137,
            "sortino_excess": -0.3978788236877837,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0027506708250000004,
            "cvar5_improvement": 0.012058464946223896,
            "drawdown_improvement": 0.07033751160946267,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18822993035780533,
            "sortino_excess": -0.3566075751029607,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0037128229,
            "cvar5_improvement": 0.011155084032784294,
            "drawdown_improvement": 0.0678169816388845,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3383711044819105,
            "sortino_excess": -0.4843338768193112,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016059407,
            "cvar5_improvement": 0.012119970022508128,
            "drawdown_improvement": 0.06259070868908409,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2639035536575141,
            "sortino_excess": -0.4128215447499106,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001695105275,
            "cvar5_improvement": 0.011786091145959316,
            "drawdown_improvement": 0.06321430520536495,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.315398954683089,
            "sortino_excess": -0.4854926097183134,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00152118965,
            "cvar5_improvement": 0.011746397388338053,
            "drawdown_improvement": 0.06079546397739363,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1953280503570058,
            "sortino_excess": -0.2695119993821836,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015084198499999998,
            "cvar5_improvement": 0.01163132319831697,
            "drawdown_improvement": 0.05933408373290505,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20869428252401878,
            "sortino_excess": -0.2971618860105756,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001830454,
            "cvar5_improvement": 0.011125365437756815,
            "drawdown_improvement": 0.05696171674175585,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.38173531500336527,
            "sortino_excess": -0.5465374970754368,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018207248749999999,
            "cvar5_improvement": 0.012549227462448406,
            "drawdown_improvement": 0.06808333650146944,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.14998572233911708,
            "sortino_excess": -0.2712703810638646,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0031203877750000004,
            "cvar5_improvement": 0.011408910733852886,
            "drawdown_improvement": 0.059334247570352466,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3613363985531731,
            "sortino_excess": -0.5671803584953842,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.0021663862,
            "cvar5_improvement": 0.011828954639130515,
            "drawdown_improvement": 0.06259234247814208,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2589985792172659,
            "sortino_excess": -0.43204218238420955,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014917771,
            "cvar5_improvement": 0.011057587913461642,
            "drawdown_improvement": 0.05620062570780043,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3764251695291,
            "sortino_excess": -0.5212528731028097,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002266874,
            "cvar5_improvement": 0.011937025359913204,
            "drawdown_improvement": 0.06599210496342695,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18839098295643542,
            "sortino_excess": -0.3657328350261999,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0028702361500000002,
            "cvar5_improvement": 0.012031116104486109,
            "drawdown_improvement": 0.06868468374527972,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19957562674967513,
            "sortino_excess": -0.31220087083900133,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001544434475,
            "cvar5_improvement": 0.01117847723614255,
            "drawdown_improvement": 0.05678288512025256,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3992636099674342,
            "sortino_excess": -0.5651514282471425,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026830189500000002,
            "cvar5_improvement": 0.012001258813284477,
            "drawdown_improvement": 0.06767070708760714,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18181097532693538,
            "sortino_excess": -0.35664413448655885,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001637431525,
            "cvar5_improvement": 0.01247103345265992,
            "drawdown_improvement": 0.06545868995475418,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.18875496547559292,
            "sortino_excess": -0.31823217473389903,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00152055975,
            "cvar5_improvement": 0.011748995441224893,
            "drawdown_improvement": 0.06081908250038098,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.21048711859171082,
            "sortino_excess": -0.29583755539112155,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015358455499999998,
            "cvar5_improvement": 0.011992425388358315,
            "drawdown_improvement": 0.06307317595938458,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.12067207733836226,
            "sortino_excess": -0.17560197396659596,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00150633215,
            "cvar5_improvement": 0.01141758172857354,
            "drawdown_improvement": 0.05848218390129084,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.28944130137716106,
            "sortino_excess": -0.40090036693948805,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020461458,
            "cvar5_improvement": 0.011707154514026465,
            "drawdown_improvement": 0.06334921189455972,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.20000156530924346,
            "sortino_excess": -0.35256748615808275,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014914851,
            "cvar5_improvement": 0.011060115211094063,
            "drawdown_improvement": 0.056215758568183005,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.38035782971697274,
            "sortino_excess": -0.5270727377707969,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020969175,
            "cvar5_improvement": 0.01177911851203794,
            "drawdown_improvement": 0.06525422181597582,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.16206673942903455,
            "sortino_excess": -0.31240282071798453,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016458106000000001,
            "cvar5_improvement": 0.011467739886697238,
            "drawdown_improvement": 0.060137372016116464,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3640048779183017,
            "sortino_excess": -0.5379247851912909,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015212187499999998,
            "cvar5_improvement": 0.011746845992985491,
            "drawdown_improvement": 0.06079911440007682,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19134141256385395,
            "sortino_excess": -0.26431854609538197,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015362167750000001,
            "cvar5_improvement": 0.011990451095609733,
            "drawdown_improvement": 0.06307017376484461,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09520397213440406,
            "sortino_excess": -0.13311079452076618,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002019543375,
            "cvar5_improvement": 0.01133556927070092,
            "drawdown_improvement": 0.05811073191707572,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3708347277355432,
            "sortino_excess": -0.5404907332765481,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001479275375,
            "cvar5_improvement": 0.011012742886351307,
            "drawdown_improvement": 0.05574087282786783,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3792671402405017,
            "sortino_excess": -0.5288326542726469,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015059733749999999,
            "cvar5_improvement": 0.011420558592764857,
            "drawdown_improvement": 0.05849442740164246,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2982206274315081,
            "sortino_excess": -0.41533527966931183,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016548736,
            "cvar5_improvement": 0.011247446231830402,
            "drawdown_improvement": 0.05744385236928673,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3966375419093453,
            "sortino_excess": -0.5723478274278178,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024452872,
            "cvar5_improvement": 0.011551244851715695,
            "drawdown_improvement": 0.060657389958489544,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34597504405060553,
            "sortino_excess": -0.5261670495350943,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.04571818720823475,
          "execution_cost": 314.63815999999997,
          "grid_return": 0.005321412522768969,
          "reconciliation_error": -6.938893903907228e-18,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.0037128229,
            "cvar5_improvement": 0.011155084032784294,
            "drawdown_improvement": 0.0678169816388845,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3383711044819105,
            "sortino_excess": -0.4843338768193112,
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
              "unit_pct": 0.2
            },
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
          "policy_id": "grid_only",
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be",
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
            "provenance_hash": "30363ae136b1cb4c2135fe506aa62f9c8de0d2d4fc96f90413f1b793fd4a8ed1",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "181d1ec02237faf0ed329cb0f2782c525e83448faf142cac290ea85b69917c90",
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
            "cost_drag": 0.0014737811,
            "cvar5_improvement": 0.012336943009785259,
            "drawdown_improvement": 0.048948005059920335,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.48171981997691643,
            "sortino_excess": -0.5495448675787462,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016357039,
            "cvar5_improvement": 0.012615986452778224,
            "drawdown_improvement": 0.05209876766320143,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5426728471743504,
            "sortino_excess": -0.5779496583192972,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00217649055,
            "cvar5_improvement": 0.01339436523448177,
            "drawdown_improvement": 0.055521684215762535,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.26981517038377717,
            "sortino_excess": -0.2904239597563162,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001442724225,
            "cvar5_improvement": 0.011548228547302725,
            "drawdown_improvement": 0.045085284430528394,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6480274805517022,
            "sortino_excess": -0.7303925590314527,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003508620225,
            "cvar5_improvement": 0.013343544350901359,
            "drawdown_improvement": 0.05809373745107471,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19189923482356708,
            "sortino_excess": -0.2120009360657689,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00152850505,
            "cvar5_improvement": 0.011635119688667572,
            "drawdown_improvement": 0.046115465713728404,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6673214871582874,
            "sortino_excess": -0.7489988876002254,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017529396,
            "cvar5_improvement": 0.012339197038161527,
            "drawdown_improvement": 0.04974259783378032,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5212459868697586,
            "sortino_excess": -0.6168916692439248,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014645350249999998,
            "cvar5_improvement": 0.012204601602017131,
            "drawdown_improvement": 0.04819173243112715,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.611859677824242,
            "sortino_excess": -0.6899704047200679,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00147387785,
            "cvar5_improvement": 0.012318112632378662,
            "drawdown_improvement": 0.048959509792487005,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4673479633362279,
            "sortino_excess": -0.5297461128226248,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014528905,
            "cvar5_improvement": 0.011822289345945244,
            "drawdown_improvement": 0.04636533790549541,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5937460605872509,
            "sortino_excess": -0.6779233828404069,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016203679,
            "cvar5_improvement": 0.01236427348538878,
            "drawdown_improvement": 0.04940128759039661,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5587114454314472,
            "sortino_excess": -0.6335202963459726,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014529193,
            "cvar5_improvement": 0.011811735615565372,
            "drawdown_improvement": 0.04636914570694936,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.58959407280434,
            "sortino_excess": -0.6719039112079903,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003436384975,
            "cvar5_improvement": 0.01301679864682027,
            "drawdown_improvement": 0.054757799373099575,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.29839579294262325,
            "sortino_excess": -0.35032553991350357,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016591441500000003,
            "cvar5_improvement": 0.012825869588664034,
            "drawdown_improvement": 0.0522595696823438,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.46859415277819966,
            "sortino_excess": -0.5153142264987794,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002548371075,
            "cvar5_improvement": 0.013438178292432467,
            "drawdown_improvement": 0.05928476231368976,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3157756018052456,
            "sortino_excess": -0.3222869708417976,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00375435605,
            "cvar5_improvement": 0.013485485300651651,
            "drawdown_improvement": 0.06082253704511709,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09611623936603562,
            "sortino_excess": -0.09331210665097106,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014743762000000002,
            "cvar5_improvement": 0.012662348332857102,
            "drawdown_improvement": 0.05041858222278792,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5572235320546595,
            "sortino_excess": -0.6199760948882906,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015999075750000001,
            "cvar5_improvement": 0.012344545771829321,
            "drawdown_improvement": 0.05090812702969105,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5867604242166176,
            "sortino_excess": -0.6488904604507986,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014630727749999999,
            "cvar5_improvement": 0.012093396044011866,
            "drawdown_improvement": 0.047685050103352944,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5390885484366443,
            "sortino_excess": -0.619437915461015,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014632512,
            "cvar5_improvement": 0.01207579711234288,
            "drawdown_improvement": 0.047677040718371255,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5289084775969686,
            "sortino_excess": -0.6052293265319337,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016852616,
            "cvar5_improvement": 0.01180642710436168,
            "drawdown_improvement": 0.04668603589416598,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6217643918788247,
            "sortino_excess": -0.7138864806963922,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016980576750000001,
            "cvar5_improvement": 0.013220974739483186,
            "drawdown_improvement": 0.05504352317850211,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3676791678960841,
            "sortino_excess": -0.3623044762828793,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003052875975,
            "cvar5_improvement": 0.012298615058767065,
            "drawdown_improvement": 0.04904723216111809,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.547128495979188,
            "sortino_excess": -0.6306363210778598,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.002010095675,
            "cvar5_improvement": 0.01268968113699775,
            "drawdown_improvement": 0.05118385839267528,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4690115098856972,
            "sortino_excess": -0.5519847952969796,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014427146250000002,
            "cvar5_improvement": 0.011548054874538768,
            "drawdown_improvement": 0.045083952871974975,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6492267848825208,
            "sortino_excess": -0.7319113734314258,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002127629175,
            "cvar5_improvement": 0.013094250084975473,
            "drawdown_improvement": 0.054820179048902934,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3114941438159106,
            "sortino_excess": -0.36510104986361347,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002664115175,
            "cvar5_improvement": 0.013745494085470156,
            "drawdown_improvement": 0.05931101667818975,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23009184279146705,
            "sortino_excess": -0.16987926155404415,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014545607000000002,
            "cvar5_improvement": 0.011733142602385102,
            "drawdown_improvement": 0.04599162352052347,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6590947755845341,
            "sortino_excess": -0.7398453414321746,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002458623125,
            "cvar5_improvement": 0.012936200082000226,
            "drawdown_improvement": 0.055355182560949234,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41164139882985173,
            "sortino_excess": -0.45469268797898077,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014844847249999998,
            "cvar5_improvement": 0.01308914276024786,
            "drawdown_improvement": 0.052616205575099245,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4972784710741003,
            "sortino_excess": -0.5281106376666854,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001462696875,
            "cvar5_improvement": 0.01215598051782867,
            "drawdown_improvement": 0.047685050103352944,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5687384716099267,
            "sortino_excess": -0.6423021080152735,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014733163999999998,
            "cvar5_improvement": 0.01242071087220285,
            "drawdown_improvement": 0.048948005059920335,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.521660745598486,
            "sortino_excess": -0.5803887883483954,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014528713,
            "cvar5_improvement": 0.011821969414587491,
            "drawdown_improvement": 0.04636279778381128,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5962583509770502,
            "sortino_excess": -0.6811549359462654,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018223584249999999,
            "cvar5_improvement": 0.012801496462932231,
            "drawdown_improvement": 0.052773142733808676,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.40470685398377604,
            "sortino_excess": -0.4894513180064043,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014426285999999998,
            "cvar5_improvement": 0.011566268921331104,
            "drawdown_improvement": 0.045083952871974975,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6591678881846458,
            "sortino_excess": -0.7395608153742845,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001890874725,
            "cvar5_improvement": 0.013171838312932973,
            "drawdown_improvement": 0.05575098067571296,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2701293127901424,
            "sortino_excess": -0.33295565851258235,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015635724,
            "cvar5_improvement": 0.012015728590088667,
            "drawdown_improvement": 0.04854794607483884,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6282054246625033,
            "sortino_excess": -0.7061777634422615,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014631018749999998,
            "cvar5_improvement": 0.012093844648659306,
            "drawdown_improvement": 0.04768870052603613,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5351019106434924,
            "sortino_excess": -0.6142444621742134,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014738198,
            "cvar5_improvement": 0.012337500340255183,
            "drawdown_improvement": 0.048952610438068506,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.47619588974915683,
            "sortino_excess": -0.5423037657679726,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001894709675,
            "cvar5_improvement": 0.01200307552769261,
            "drawdown_improvement": 0.04734668584167348,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6012947842456,
            "sortino_excess": -0.6913732895527176,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014429888500000002,
            "cvar5_improvement": 0.011540873891822883,
            "drawdown_improvement": 0.045070687034214435,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6465413259789697,
            "sortino_excess": -0.7281224658725969,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001452581425,
            "cvar5_improvement": 0.011864105106860798,
            "drawdown_improvement": 0.04636279778381128,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6159234364058841,
            "sortino_excess": -0.6962858952849591,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00158174015,
            "cvar5_improvement": 0.011836535607815212,
            "drawdown_improvement": 0.04658587749678628,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.6367326757638135,
            "sortino_excess": -0.7190720215511459,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002261393275,
            "cvar5_improvement": 0.012197079264991289,
            "drawdown_improvement": 0.049501964752876826,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5863213070613511,
            "sortino_excess": -0.6701290706925269,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.03180014095788847,
          "execution_cost": 265.24513,
          "grid_return": 0.005047938974613992,
          "reconciliation_error": -1.3877787807814457e-17,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.00375435605,
            "cvar5_improvement": 0.013485485300651651,
            "drawdown_improvement": 0.06082253704511709,
            "exposure_ratio": 0.7718253968253969,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09611623936603562,
            "sortino_excess": -0.09331210665097106,
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
              "unit_pct": 0.2
            },
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
          "policy_id": "grid_only",
          "spec_hash": "1ff299721961b2f7fc24a9abbe1034cb0bf525f17e7139dbd6661369e9ca69be",
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
            "provenance_hash": "3274e19422069735d2b29879bfd6d749ea2c0e1aef5687971ae4d05922309926",
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
            "provenance_hash": "34d1bbf0b5d64c261e0ab422e7dea8f250893e1a2af8fd493720da2286ef93a2",
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
            "cost_drag": 0.0014233178000000002,
            "cvar5_improvement": 0.011986152101831737,
            "drawdown_improvement": 0.04609814387814873,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2931290071988919,
            "sortino_excess": -0.3220024000433957,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015980257999999997,
            "cvar5_improvement": 0.012636669810989461,
            "drawdown_improvement": 0.050338776113006606,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3151485719943346,
            "sortino_excess": -0.2620197842681813,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00200732495,
            "cvar5_improvement": 0.013632474307030362,
            "drawdown_improvement": 0.05387062076043955,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.0804749240667068,
            "sortino_excess": 0.22180499879521526,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00136363245,
            "cvar5_improvement": 0.010967525343247578,
            "drawdown_improvement": 0.04222258782608174,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5705091433605659,
            "sortino_excess": -0.6269968780457913,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003205476375,
            "cvar5_improvement": 0.013595800507448134,
            "drawdown_improvement": 0.05371482103804484,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.005402239519002275,
            "sortino_excess": 0.008358329469670078,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014782584750000001,
            "cvar5_improvement": 0.011180311142505603,
            "drawdown_improvement": 0.04353326737498486,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5720189634470868,
            "sortino_excess": -0.6219376804990773,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016507221000000001,
            "cvar5_improvement": 0.012027561608574188,
            "drawdown_improvement": 0.047884207711248905,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3536644042125045,
            "sortino_excess": -0.39500481126934517,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001418552325,
            "cvar5_improvement": 0.011886884761639896,
            "drawdown_improvement": 0.046094269148101,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4717751160301808,
            "sortino_excess": -0.5036624393007085,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013822295,
            "cvar5_improvement": 0.01169936608055031,
            "drawdown_improvement": 0.04588751974758737,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4130023256746195,
            "sortino_excess": -0.4550658628021498,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013744533000000002,
            "cvar5_improvement": 0.011272599781181614,
            "drawdown_improvement": 0.04349775783323431,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.498843013988205,
            "sortino_excess": -0.5554303415134858,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001513476075,
            "cvar5_improvement": 0.011996446316330001,
            "drawdown_improvement": 0.047297566718853906,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4592939759021261,
            "sortino_excess": -0.49631272825008615,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013612994750000001,
            "cvar5_improvement": 0.011194910615059821,
            "drawdown_improvement": 0.04330939686118526,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5314131088238718,
            "sortino_excess": -0.5915685276223985,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003231561425,
            "cvar5_improvement": 0.012990821540217162,
            "drawdown_improvement": 0.05130117027009842,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1266026528338226,
            "sortino_excess": -0.13777251886006556,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015445066500000002,
            "cvar5_improvement": 0.012582131219748332,
            "drawdown_improvement": 0.050505170803808425,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34707576396277434,
            "sortino_excess": -0.342102059335705,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002462927425,
            "cvar5_improvement": 0.01360176508852672,
            "drawdown_improvement": 0.05524091023268318,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.03784272682197386,
            "sortino_excess": 0.007037879593066454,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0033366016500000002,
            "cvar5_improvement": 0.013774622447405455,
            "drawdown_improvement": 0.05546295108644628,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.06692140989860872,
            "sortino_excess": 0.05939199560716757,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001432610925,
            "cvar5_improvement": 0.012492628742870484,
            "drawdown_improvement": 0.0486545756482292,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.37062770396685696,
            "sortino_excess": -0.3656941623103127,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001557750625,
            "cvar5_improvement": 0.012211707543077946,
            "drawdown_improvement": 0.04917553979435568,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4069044183295153,
            "sortino_excess": -0.40549775050810466,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001408698775,
            "cvar5_improvement": 0.01167234967441093,
            "drawdown_improvement": 0.044807182637921744,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3847229499541094,
            "sortino_excess": -0.4294571804297892,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001371522175,
            "cvar5_improvement": 0.011459788745964277,
            "drawdown_improvement": 0.04462018620296346,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4725139355019763,
            "sortino_excess": -0.5276914194630077,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015944714250000001,
            "cvar5_improvement": 0.011346322146447893,
            "drawdown_improvement": 0.044350263942964735,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5115173285845165,
            "sortino_excess": -0.5668760637913879,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015762588,
            "cvar5_improvement": 0.013098098825427795,
            "drawdown_improvement": 0.053284702229282666,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.22117023701523825,
            "sortino_excess": -0.1433040480150396,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0029003430250000004,
            "cvar5_improvement": 0.012024038697124212,
            "drawdown_improvement": 0.046495528190144686,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41994289829770576,
            "sortino_excess": -0.46447444311996167,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.0018804316749999998,
            "cvar5_improvement": 0.012573523693409791,
            "drawdown_improvement": 0.04947184505657437,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2952224208402615,
            "sortino_excess": -0.30087144292734214,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00137988935,
            "cvar5_improvement": 0.010998976831362162,
            "drawdown_improvement": 0.04221946659458192,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5587586974765194,
            "sortino_excess": -0.6136232042512983,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001979099875,
            "cvar5_improvement": 0.013204896576042152,
            "drawdown_improvement": 0.053106905281602335,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.05866192659720927,
            "sortino_excess": 0.018959098658700824,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024596984249999998,
            "cvar5_improvement": 0.014088068337348821,
            "drawdown_improvement": 0.054460334178453584,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.01052822530239643,
            "sortino_excess": 0.0976669850637027,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00140427765,
            "cvar5_improvement": 0.011266269684438465,
            "drawdown_improvement": 0.043411236811748216,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5611076281961072,
            "sortino_excess": -0.6095429062866347,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002379134175,
            "cvar5_improvement": 0.012868793489555223,
            "drawdown_improvement": 0.052063402264033026,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.22905138283030313,
            "sortino_excess": -0.2178004311057758,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001446812425,
            "cvar5_improvement": 0.013069816378883072,
            "drawdown_improvement": 0.050888039701453974,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.260261766427356,
            "sortino_excess": -0.19470037720804012,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014212595,
            "cvar5_improvement": 0.011985060710881046,
            "drawdown_improvement": 0.045921043528794225,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.36858134513609164,
            "sortino_excess": -0.3700787192936188,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014357751250000002,
            "cvar5_improvement": 0.01240458919732195,
            "drawdown_improvement": 0.047219839186275064,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.26465724355623754,
            "sortino_excess": -0.2184243556302032,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013944661999999999,
            "cvar5_improvement": 0.011335391146075926,
            "drawdown_improvement": 0.0434915810061377,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.47443411691206244,
            "sortino_excess": -0.5276018028553309,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001707894325,
            "cvar5_improvement": 0.012612838979591257,
            "drawdown_improvement": 0.051088010332614425,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1675716887684237,
            "sortino_excess": -0.17785877283927,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013923748749999998,
            "cvar5_improvement": 0.011099042770598125,
            "drawdown_improvement": 0.0424900201389628,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5573289777145081,
            "sortino_excess": -0.6046385386009157,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017647333249999999,
            "cvar5_improvement": 0.01301386328917252,
            "drawdown_improvement": 0.054072019632811164,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.046745423520159465,
            "sortino_excess": 0.07104502280002817,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015175173,
            "cvar5_improvement": 0.01171707755782474,
            "drawdown_improvement": 0.04643266019575043,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4932333139673299,
            "sortino_excess": -0.5268037762713846,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001384803425,
            "cvar5_improvement": 0.01157725147859629,
            "drawdown_improvement": 0.04481626642138645,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4229526640335678,
            "sortino_excess": -0.47283572709784627,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001395786925,
            "cvar5_improvement": 0.011851620779192176,
            "drawdown_improvement": 0.04609256300439554,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34623163486869146,
            "sortino_excess": -0.38145590873096186,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.001784195725,
            "cvar5_improvement": 0.011641221623263226,
            "drawdown_improvement": 0.04529069237144512,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.49153145774637874,
            "sortino_excess": -0.5404408709196475,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0013510096000000002,
            "cvar5_improvement": 0.010924728889984095,
            "drawdown_improvement": 0.04202639045399886,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5860168623084023,
            "sortino_excess": -0.6441687468765886,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014066606,
            "cvar5_improvement": 0.011546666431454852,
            "drawdown_improvement": 0.04425339622639249,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4672970287470414,
            "sortino_excess": -0.499178106896618,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014827250750000002,
            "cvar5_improvement": 0.011343695641509537,
            "drawdown_improvement": 0.04399341028710352,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5574294278639906,
            "sortino_excess": -0.6106508109582071,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0021882746,
            "cvar5_improvement": 0.011848606223987021,
            "drawdown_improvement": 0.04699405087417877,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.47558299431253137,
            "sortino_excess": -0.5228017480804831,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": 0.019384494032918958,
          "execution_cost": 169.34074,
          "grid_return": 0.00864952401547265,
          "reconciliation_error": -1.0408340855860843e-17,
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
            "cost_drag": 0.0024596984249999998,
            "cvar5_improvement": 0.014088068337348821,
            "drawdown_improvement": 0.054460334178453584,
            "exposure_ratio": 0.751984126984127,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.01052822530239643,
            "sortino_excess": 0.0976669850637027,
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
          "policy_id": "grid_only",
          "spec_hash": "cc00abb09e1788472dcb337deebafcaaa2910da7ab66b37a1b48d613bdef69ea",
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
        "shares": 33300,
        "raw_price": 1.4974491
      },
      {
        "event_date": "2024-02-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13300,
        "raw_price": 1.5085473
      },
      {
        "event_date": "2024-02-23",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13100,
        "raw_price": 1.5335398
      },
      {
        "event_date": "2024-02-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13400,
        "raw_price": 1.4984494
      },
      {
        "event_date": "2024-03-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13300,
        "raw_price": 1.509547
      },
      {
        "event_date": "2024-03-06",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-03-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-03-08",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-03-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-03-12",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-03-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13400,
        "raw_price": 1.4964488
      },
      {
        "event_date": "2024-03-29",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 20400,
        "raw_price": 1.4745575000000002
      },
      {
        "event_date": "2024-04-02",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33500,
        "raw_price": 1.4964488
      },
      {
        "event_date": "2024-04-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13300,
        "raw_price": 1.5135458000000002
      },
      {
        "event_date": "2024-04-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13100,
        "raw_price": 1.5475356
      },
      {
        "event_date": "2024-04-18",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-04-19",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-04-22",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-04-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13300,
        "raw_price": 1.520456
      },
      {
        "event_date": "2024-05-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13200,
        "raw_price": 1.5355392
      },
      {
        "event_date": "2024-05-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-15",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-16",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-17",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-20",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-21",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-22",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-23",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-24",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-27",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-28",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-29",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-30",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-05-31",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-03",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-04",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-05",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-06",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-12",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-17",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2024-06-18",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 7200,
        "raw_price": 1.5285412999999999
      },
      {
        "event_date": "2024-07-02",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33000,
        "raw_price": 1.5354605
      },
      {
        "event_date": "2024-07-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13300,
        "raw_price": 1.5114532999999999
      },
      {
        "event_date": "2024-07-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13300,
        "raw_price": 1.4944482
      },
      {
        "event_date": "2024-07-23",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 59600,
        "raw_price": 1.4675596
      },
      {
        "event_date": "2024-08-16",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33700,
        "raw_price": 1.4564367999999999
      },
      {
        "event_date": "2024-08-20",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13400,
        "raw_price": 1.4675596
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 4,
        "shares": 133500,
        "traded_value": "199748.2064899999966300"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 7,
        "shares": 92700,
        "traded_value": "140567.3171500000026600"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 5,
        "shares": 66700,
        "traded_value": "100332.1906299999986700"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 87200,
        "traded_value": "128553.0225200000033600"
      }
    },
    "invested_sessions": 95,
    "cash_sessions": 31,
    "rejected_order_count": 33
  },
  {
    "window_id": "wf_001",
    "trade_points": [
      {
        "event_date": "2024-09-25",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 34600,
        "raw_price": 1.4434329
      },
      {
        "event_date": "2024-09-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13500,
        "raw_price": 1.5165449
      },
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13300,
        "raw_price": 1.5374610999999998
      },
      {
        "event_date": "2024-10-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12500,
        "raw_price": 1.779466
      },
      {
        "event_date": "2024-10-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13800,
        "raw_price": 1.5224566
      },
      {
        "event_date": "2024-10-10",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 35700,
        "raw_price": 1.5035488000000001
      },
      {
        "event_date": "2024-10-11",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33500,
        "raw_price": 1.5634689
      },
      {
        "event_date": "2024-10-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13500,
        "raw_price": 1.5364608
      },
      {
        "event_date": "2024-10-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13400,
        "raw_price": 1.5575326
      },
      {
        "event_date": "2024-10-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13600,
        "raw_price": 1.5234568999999998
      },
      {
        "event_date": "2024-10-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13500,
        "raw_price": 1.5535338
      },
      {
        "event_date": "2024-10-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13600,
        "raw_price": 1.5364608
      },
      {
        "event_date": "2024-10-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13500,
        "raw_price": 1.5515344000000002
      },
      {
        "event_date": "2024-10-30",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13700,
        "raw_price": 1.5254575
      },
      {
        "event_date": "2024-11-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13700,
        "raw_price": 1.5044511999999999
      },
      {
        "event_date": "2024-11-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13700,
        "raw_price": 1.5235428
      },
      {
        "event_date": "2024-11-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13600,
        "raw_price": 1.5525341
      },
      {
        "event_date": "2024-11-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13500,
        "raw_price": 1.5795260000000002
      },
      {
        "event_date": "2024-11-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13600,
        "raw_price": 1.5564668
      },
      {
        "event_date": "2024-11-13",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13700,
        "raw_price": 1.5374610999999998
      },
      {
        "event_date": "2024-11-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13700,
        "raw_price": 1.5284583999999999
      },
      {
        "event_date": "2024-11-19",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13700,
        "raw_price": 1.5465359
      },
      {
        "event_date": "2024-11-25",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13800,
        "raw_price": 1.5134538999999998
      },
      {
        "event_date": "2024-12-02",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13800,
        "raw_price": 1.5175446000000001
      },
      {
        "event_date": "2024-12-04",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13800,
        "raw_price": 1.5315404000000001
      },
      {
        "event_date": "2024-12-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13700,
        "raw_price": 1.5535338
      },
      {
        "event_date": "2024-12-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13600,
        "raw_price": 1.5705287
      },
      {
        "event_date": "2024-12-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13800,
        "raw_price": 1.5474640999999998
      },
      {
        "event_date": "2024-12-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13800,
        "raw_price": 1.5334598999999998
      },
      {
        "event_date": "2024-12-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13700,
        "raw_price": 1.5525341
      },
      {
        "event_date": "2025-01-03",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13900,
        "raw_price": 1.5314592999999999
      },
      {
        "event_date": "2025-01-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 14000,
        "raw_price": 1.5134538999999998
      },
      {
        "event_date": "2025-01-10",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 48400,
        "raw_price": 1.4925521000000002
      },
      {
        "event_date": "2025-02-05",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 34600,
        "raw_price": 1.5164548
      },
      {
        "event_date": "2025-02-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13900,
        "raw_price": 1.4874461
      },
      {
        "event_date": "2025-02-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13900,
        "raw_price": 1.5025491
      },
      {
        "event_date": "2025-02-21",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 14000,
        "raw_price": 1.4854455
      },
      {
        "event_date": "2025-02-28",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13900,
        "raw_price": 1.5015494
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 102700,
        "traded_value": "154788.3225700"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 16,
        "shares": 217300,
        "traded_value": "337750.8443400000081600"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 17,
        "shares": 233400,
        "traded_value": "355845.8217299999766700"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 84100,
        "traded_value": "125916.2138000000132500"
      }
    },
    "invested_sessions": 90,
    "cash_sessions": 36,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_002",
    "trade_points": [
      {
        "event_date": "2025-03-06",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33400,
        "raw_price": 1.4954485
      },
      {
        "event_date": "2025-03-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13200,
        "raw_price": 1.5175446000000001
      },
      {
        "event_date": "2025-03-18",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13100,
        "raw_price": 1.5355392
      },
      {
        "event_date": "2025-03-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13300,
        "raw_price": 1.5184554
      },
      {
        "event_date": "2025-04-01",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13300,
        "raw_price": 1.5044511999999999
      },
      {
        "event_date": "2025-04-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13300,
        "raw_price": 1.5165449
      },
      {
        "event_date": "2025-04-08",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 20400,
        "raw_price": 1.4345695
      },
      {
        "event_date": "2025-04-23",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33000,
        "raw_price": 1.5034508999999998
      },
      {
        "event_date": "2025-05-06",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13200,
        "raw_price": 1.4874461
      },
      {
        "event_date": "2025-05-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13200,
        "raw_price": 1.5015494
      },
      {
        "event_date": "2025-05-14",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13100,
        "raw_price": 1.5235428
      },
      {
        "event_date": "2025-05-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13000,
        "raw_price": 1.5405377
      },
      {
        "event_date": "2025-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13200,
        "raw_price": 1.5184554
      },
      {
        "event_date": "2025-06-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13100,
        "raw_price": 1.5355392
      },
      {
        "event_date": "2025-06-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 13200,
        "raw_price": 1.5154545
      },
      {
        "event_date": "2025-06-20",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 20200,
        "raw_price": 1.5055482
      },
      {
        "event_date": "2025-06-24",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 33000,
        "raw_price": 1.5174550999999998
      },
      {
        "event_date": "2025-06-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13100,
        "raw_price": 1.5325401
      },
      {
        "event_date": "2025-07-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13000,
        "raw_price": 1.5475356
      },
      {
        "event_date": "2025-07-08",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-09",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-10",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-15",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-07-16",
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
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 6900,
        "raw_price": 1.5655302000000002
      },
      {
        "event_date": "2025-08-06",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31800,
        "raw_price": 1.5884764
      },
      {
        "event_date": "2025-08-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12600,
        "raw_price": 1.6015194000000001
      },
      {
        "event_date": "2025-08-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12800,
        "raw_price": 1.5814743
      },
      {
        "event_date": "2025-08-22",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12700,
        "raw_price": 1.59952
      },
      {
        "event_date": "2025-08-28",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12800,
        "raw_price": 1.5824746
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 4,
        "shares": 131200,
        "traded_value": "200151.4274199999868000"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 11,
        "shares": 143400,
        "traded_value": "220925.9023400000025800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 7,
        "shares": 91800,
        "traded_value": "140385.1028999999986700"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 47500,
        "traded_value": "70479.4498200000013800"
      }
    },
    "invested_sessions": 109,
    "cash_sessions": 17,
    "rejected_order_count": 16
  },
  {
    "window_id": "wf_003",
    "trade_points": [
      {
        "event_date": "2025-09-10",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31400,
        "raw_price": 1.5874761
      },
      {
        "event_date": "2025-09-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12600,
        "raw_price": 1.5654694999999998
      },
      {
        "event_date": "2025-09-19",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 44000,
        "raw_price": 1.5385383
      },
      {
        "event_date": "2025-10-10",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31400,
        "raw_price": 1.5584674
      },
      {
        "event_date": "2025-10-13",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12500,
        "raw_price": 1.5575326
      },
      {
        "event_date": "2025-10-15",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12400,
        "raw_price": 1.5845245000000001
      },
      {
        "event_date": "2025-10-22",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-23",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-24",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-27",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-28",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-29",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-10-30",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-04",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-05",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-06",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-10",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-12",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-17",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-18",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-19",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-20",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-21",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-11-24",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 6500,
        "raw_price": 1.5845245000000001
      },
      {
        "event_date": "2025-12-29",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31700,
        "raw_price": 1.550465
      },
      {
        "event_date": "2026-01-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12600,
        "raw_price": 1.5685293
      },
      {
        "event_date": "2026-01-19",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12700,
        "raw_price": 1.5454634999999999
      },
      {
        "event_date": "2026-01-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12600,
        "raw_price": 1.5765269
      },
      {
        "event_date": "2026-01-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12500,
        "raw_price": 1.5985203000000001
      },
      {
        "event_date": "2026-01-30",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-02-03",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 6700,
        "raw_price": 1.5625311
      },
      {
        "event_date": "2026-02-05",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31100,
        "raw_price": 1.6014803
      },
      {
        "event_date": "2026-02-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12300,
        "raw_price": 1.6225131000000002
      },
      {
        "event_date": "2026-02-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12400,
        "raw_price": 1.6054815
      },
      {
        "event_date": "2026-02-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12300,
        "raw_price": 1.629511
      },
      {
        "event_date": "2026-03-03",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12200,
        "raw_price": 1.6605017000000002
      },
      {
        "event_date": "2026-03-11",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12300,
        "raw_price": 1.6394917
      },
      {
        "event_date": "2026-03-12",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12200,
        "raw_price": 1.6645005000000002
      },
      {
        "event_date": "2026-03-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 4,
        "shares": 125600,
        "traded_value": "197738.4037300"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 4,
        "shares": 50000,
        "traded_value": "79426.0206599999962100"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 57200,
        "traded_value": "88464.0528200000006500"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 9,
        "shares": 111600,
        "traded_value": "179291.3964400000098300"
      }
    },
    "invested_sessions": 86,
    "cash_sessions": 40,
    "rejected_order_count": 23
  },
  {
    "window_id": "wf_004",
    "trade_points": [
      {
        "event_date": "2026-04-17",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31200,
        "raw_price": 1.6004800000000001
      },
      {
        "event_date": "2026-04-29",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12300,
        "raw_price": 1.6255122
      },
      {
        "event_date": "2026-05-15",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12500,
        "raw_price": 1.5964788
      },
      {
        "event_date": "2026-05-19",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 31400,
        "raw_price": 1.5835248000000002
      },
      {
        "event_date": "2026-06-02",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 31000,
        "raw_price": 1.6084824
      },
      {
        "event_date": "2026-06-09",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 12500,
        "raw_price": 1.580474
      },
      {
        "event_date": "2026-06-17",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 43500,
        "raw_price": 1.5505347
      },
      {
        "event_date": "2026-07-15",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 32700,
        "raw_price": 1.4904469999999999
      },
      {
        "event_date": "2026-07-16",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 13000,
        "raw_price": 1.5115464
      },
      {
        "event_date": "2026-07-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 12800,
        "raw_price": 1.5325401
      },
      {
        "event_date": "2026-07-30",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-07-31",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-03",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-04",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-10",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-12",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-13",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-18",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-19",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-20",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-21",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-24",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-25",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-26",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-27",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-28",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-08-31",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-01",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-02",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-03",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-04",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-07",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-08",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-09",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-10",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-11",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-14",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-15",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-16",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2026-09-17",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 6900,
        "raw_price": 1.5445365
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 94900,
        "traded_value": "148535.5472999999998500"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 3,
        "shares": 38100,
        "traded_value": "59260.4165400"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 2,
        "shares": 25000,
        "traded_value": "39711.9100000"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 3,
        "shares": 81800,
        "traded_value": "127828.2400200000062800"
      }
    },
    "invested_sessions": 76,
    "cash_sessions": 50,
    "rejected_order_count": 31
  }
]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

### wf_000

Largest absolute contributor: grid_return (0.01578096).
Next research action: Study grid spacing, sizing and stop/cooldown behavior on training windows.

### wf_001

Largest absolute contributor: cash_opportunity_cost (-0.01927589).
Next research action: Study cash exposure and re-entry timing on training windows.

### wf_002

Largest absolute contributor: cash_opportunity_cost (-0.04571819).
Next research action: Study cash exposure and re-entry timing on training windows.

### wf_003

Largest absolute contributor: cash_opportunity_cost (-0.03180014).
Next research action: Study cash exposure and re-entry timing on training windows.

### wf_004

Largest absolute contributor: cash_opportunity_cost (0.01938449).
Next research action: Study cash exposure and re-entry timing on training windows.

Research evidence only; no broker action is authorized.
