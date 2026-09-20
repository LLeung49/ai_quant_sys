# 风险调整后 ETF 样本外验证决策报告

## 决策

- 结论：`diagnostic_complete`
- 建议：Diagnostic research only; no authorization.
- 阻断项：无

## 策略与买入持有比较

| 指标 | 策略 | 买入持有 | 差异（策略－买入持有） |
| --- | ---: | ---: | ---: |
| annual_return | 0.026068 | 0.106942 | -0.080874 |
| sharpe | 0.297663 | 0.356353 | -0.058689 |
| Sortino | 0.330925 | 0.577005 | -0.246079 |
| calmar | 0.238016 | 0.289695 | -0.051679 |
| cvar5 | -0.013408 | -0.037859 | 0.024451 |
| max_drawdown | -0.109522 | -0.369155 | 0.259632 |
| turnover | 16.153857 | 3.035067 | 13.118790 |
| total_cost | 824.893250 | 159.899700 | 664.993550 |

## OOS 分布

{
  "window_count": 4,
  "win_rate": 0.25,
  "median_excess_return": -0.000725454299999817,
  "best_excess_return": 0.15779478079999987,
  "worst_excess_return": -0.23043547289999977
}

## 执行、换手与成本

{
  "strategy": {
    "invested_sessions": 226,
    "cash_sessions": 278,
    "exposure_ratio": 0.44841269841269843,
    "turnover": 16.153856553902244,
    "total_cost": 824.89325,
    "cost_drag": 0.0082489325
  },
  "buy_and_hold": {
    "invested_sessions": 500,
    "cash_sessions": 4,
    "exposure_ratio": 0.9920634920634921,
    "turnover": 3.035066837769012,
    "total_cost": 159.8997,
    "cost_drag": 0.001598997
  }
}

## 数据边界、配置与训练曲面

{
  "data_cutoff": "2026-09-17",
  "config_hashes": [
    "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
    "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
    "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
    "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e"
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
            true,
            true
          ],
          "oos_returns": [
            0.21342945690000006,
            -0.037387413500000015,
            0.05141810020000019,
            0.02505980930000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.2477965866000001,
            -0.034775014599999966,
            0.05400408760000029,
            0.03233939420000008
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.23961189820000012,
            -0.017469065299999892,
            0.059417424100000386,
            0.02276596960000012
          ],
          "positive_window_share": 0.75
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
            0.24436340610000012,
            -0.020771573799999853,
            0.06635919530000045,
            0.0011573509000000967
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19266828140000003,
            -0.03566186890000004,
            0.054410795900000114,
            0.03238938760000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.20519671930000002,
            -0.042333800200000014,
            0.05894742270000014,
            0.040375714200000086
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.201671973,
            -0.03482855549999999,
            0.06349925000000017,
            0.028266348100000102
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.20717252330000002,
            -0.02223758379999992,
            0.0679362996000002,
            0.01608527740000011
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19440971920000005,
            -0.02466800920000005,
            0.05590937370000013,
            0.022183974899999986
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.20836126710000008,
            -0.021111176800000034,
            0.06188379450000018,
            0.03091265880000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.2225973018000001,
            -0.01770109920000002,
            0.06774554240000022,
            0.03952027830000006
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.2327136917000001,
            -0.02327492099999997,
            0.07368794780000028,
            0.041173595600000105
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18622098270000004,
            -0.02043454000000005,
            0.0546807049000001,
            0.019675452599999966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19190388010000003,
            -0.012887638100000043,
            0.059077593300000106,
            0.025548002799999983
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19790631230000005,
            -0.00537690610000003,
            0.06341414640000012,
            0.031394822
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19182613850000008,
            -0.007000062899999979,
            0.06765413970000013,
            0.03143695800000002
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.17696429010000003,
            -0.023269864700000052,
            0.05696174070000008,
            0.016146846599999962
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.17329449260000007,
            -0.018682596400000043,
            0.06352931940000009,
            0.018077669799999977
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.16553032000000006,
            -0.014270875800000027,
            0.07002969490000009,
            0.01995997889999999
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.15841695600000008,
            -0.023580451600000017,
            0.07650608970000009,
            0.015755402199999966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18118834730000005,
            -0.01816417540000006,
            0.0564470747000001,
            0.017844918799999967
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18154620670000005,
            -0.00851667470000006,
            0.062313285800000104,
            0.021358276699999987
          ],
          "positive_window_share": 0.75
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
            0.17764808430000006,
            0.001163135099999945,
            0.06812258830000012,
            0.02482217720000001
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
            0.17751504880000007,
            0.010909304799999946,
            0.07395802450000012,
            0.022217238999999993
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18248081060000004,
            -0.019232469500000064,
            0.05736101980000011,
            0.020893920099999973
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18426764050000005,
            -0.010664869000000056,
            0.06411751750000012,
            0.0274924475
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18161515990000004,
            -0.0021660333000000573,
            0.07097697410000015,
            0.03419374990000003
          ],
          "positive_window_share": 0.75
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
            0.18288310790000006,
            0.006387275799999946,
            0.07780324430000016,
            0.030842080900000013
          ],
          "positive_window_share": 1.0
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18631593840000005,
            -0.02277142610000006,
            0.05578332660000011,
            0.021188641099999954
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19207754090000007,
            -0.017893618600000057,
            0.06098066190000014,
            0.02806187199999996
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19762991520000006,
            -0.01310906610000006,
            0.06615979370000016,
            0.03497633289999996
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19708139930000007,
            -0.008298152900000057,
            0.0713499253000002,
            0.041863977799999966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18512646160000004,
            -0.02314146020000006,
            0.05514899150000009,
            0.021188641099999954
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.18940455600000006,
            -0.01869630100000006,
            0.0596026431000001,
            0.02806187199999996
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19382975040000006,
            -0.014292019800000055,
            0.06402073490000011,
            0.03497633289999996
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.19211058570000006,
            -0.009691062000000056,
            0.06833744750000012,
            0.041863977799999966
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.17381552020000005,
            -0.02352729400000006,
            0.05772156760000009,
            0.01865793809999995
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.16646144930000004,
            -0.01966401640000006,
            0.06474425900000011,
            0.022856405099999956
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.15921943000000005,
            -0.015833529200000057,
            0.07180861980000011,
            0.027037159499999963
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.15272589370000003,
            -0.011966158800000057,
            0.07882434650000013,
            0.031218224999999968
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.17654087080000003,
            -0.02263804990000006,
            0.0546044995000001,
            0.019273821099999946
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.17218172660000003,
            -0.017867289700000066,
            0.058301777100000104,
            0.024102057299999945
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.16789887170000006,
            -0.013117232800000066,
            0.062030409100000114,
            0.028895860099999948
          ],
          "positive_window_share": 0.75
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            true,
            false,
            true,
            true
          ],
          "oos_returns": [
            0.16453949670000007,
            -0.008325525700000065,
            0.06566437090000013,
            0.03378215299999995
          ],
          "positive_window_share": 0.75
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
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.07241820109999994,
            0.05141810020000019,
            0.02505980930000002,
            -0.14093661139999988
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "4ba27c22874b9850f961a064b0c0cbec006c1e2e752fea8169985499d494e6d6",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.08266268979999991,
            0.05400408760000029,
            0.03233939420000008,
            -0.14648150669999982
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.07627699459999981,
            0.059417424100000386,
            0.02276596960000012,
            -0.14368339509999975
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.0769738158999998,
            0.06635919530000045,
            0.0011573509000000967,
            -0.15280829359999967
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ff4c177908f78482ba254405d5ee9378b5c7c63fe77102b4d0f56fa68a165555",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.07032664889999996,
            0.054410795900000114,
            0.03238938760000002,
            -0.12746531779999992
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac3b358b2e80557d5ba9620b510472a2109a6c52328ab769e429cd068464f5b6",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.08252250669999994,
            0.05894742270000014,
            0.040375714200000086,
            -0.12035033189999987
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "60e882c4a0702e0d30ea46270dffa260f60f745dd4a32acc9fdb1e1a63724c5a",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.0818829351999999,
            0.06349925000000017,
            0.028266348100000102,
            -0.11342843179999983
          ],
          "positive_window_share": 0.5
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
            -0.07542537939999983,
            0.0679362996000002,
            0.01608527740000011,
            -0.09484037799999978
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d00e7a413dc0c16a28bc70ddeb8ed350aba95d73b88409a428dae37317de70ab",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06009507949999996,
            0.05590937370000013,
            0.022183974899999986,
            -0.14977771539999993
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "928ff9246144538cdea5af2f6efde5b0355c71d0abf4f11f954532e7de8195ce",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06260983319999994,
            0.06188379450000018,
            0.03091265880000002,
            -0.1650246454999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "9dddf7f3ef757a9f18f5973a3ccd6687dea654db95fef784d949d02fe0b0b1d4",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06534729469999995,
            0.06774554240000022,
            0.03952027830000006,
            -0.18033422439999988
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.07396029649999988,
            0.07368794780000028,
            0.041173595600000105,
            -0.18419675509999983
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "795d4515ee57febfc68b17037832ce285e1c07a1a03cb8b0c584d4a2f05f48a1",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05602520549999996,
            0.0546807049000001,
            0.019675452599999966,
            -0.14326069509999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "236aa65a294576dabeaac13b57e2808511cc1d554b7e66a07c0f94bd058785d0",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05481002369999995,
            0.059077593300000106,
            0.025548002799999983,
            -0.15220943699999992
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c22fc03cd43444f15b9fa2dd23bf8602189645c775c284729fe85029e6278aa0",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05363847489999995,
            0.06341414640000012,
            0.031394822,
            -0.1617109513999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c694ca450c44b0dacd6d87c1d7ab2d6ee91d5aef8797f99ca0430ee15c9b6229",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.0611687462999999,
            0.06765413970000013,
            0.03143695800000002,
            -0.15919514549999988
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "e74ce674edaa94759d1e3c22d8c43922a1d508a2e32210d2851de073af103c10",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05872011739999997,
            0.05696174070000008,
            0.016146846599999962,
            -0.13838366489999993
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "41996ce3e781e343c04fe477e4151bad9651a096eb9cc56cab77a37ec868b692",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06037045739999996,
            0.06352931940000009,
            0.018077669799999977,
            -0.14277363429999992
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "562a0a941e6a597295ce7bb7c86c6656fb14da14b34806a39ab4ad923e5615f7",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.062172813999999944,
            0.07002969490000009,
            0.01995997889999999,
            -0.1475635874999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "7a7f7daceec6466e9fa6ede7cb8d5dd3835dc8f28a5c320307ce4b922cf162ae",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.07692098729999994,
            0.07650608970000009,
            0.015755402199999966,
            -0.14033653029999987
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05391061879999997,
            0.0564470747000001,
            0.017844918799999967,
            -0.15231442179999993
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c7607fa3377f5d7bd313e8cda5f431908f3677e29e9f7f7cf563e74dfbe744d1",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.050570452599999975,
            0.062313285800000104,
            0.021358276699999987,
            -0.17087882079999991
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.047303436599999964,
            0.06812258830000012,
            0.02482217720000001,
            -0.1807195091999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "154f190c593cef61c84037b4896c73d6edec942d651987a9a82419300110c76d",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.04403446499999996,
            0.07395802450000012,
            0.022217238999999993,
            -0.1915859143999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05487924039999998,
            0.05736101980000011,
            0.020893920099999973,
            -0.14596026239999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "260007e81996db708e0f60bf89f59c975331ae2ee41e0c73c0f0ad5b37b08064",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.052713287499999976,
            0.06411751750000012,
            0.0274924475,
            -0.15829613009999993
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "65a89d08421d9718b4d5d94154a5fbd388473d11abcc90846531fe6a35e69f67",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05052386009999996,
            0.07097697410000015,
            0.03419374990000003,
            -0.17022528719999994
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b0c85931f2fb0bd085e1c63c008a54df8336e8cfe9e6a0b704f73422a7459608",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.04833357919999997,
            0.07780324430000016,
            0.030842080900000013,
            -0.1907841946999999
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05828053219999998,
            0.05578332660000011,
            0.021188641099999954,
            -0.13498460919999994
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "dde17bdbb2efd257e236db81049bdd82ccd8407c5124cf5a18fef6cdd5d02c03",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05960792339999998,
            0.06098066190000014,
            0.02806187199999996,
            -0.13611087729999993
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "b78084f5ae17ca8e23076e38631dc7f558179058dab59d39f57c7365776caab9",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06093671129999997,
            0.06615979370000016,
            0.03497633289999996,
            -0.13778445739999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06229849349999996,
            0.0713499253000002,
            0.041863977799999966,
            -0.13837706219999993
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05767499119999998,
            0.05514899150000009,
            0.021188641099999954,
            -0.13380660519999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "bf26a9f270d4bdbd9d5604c0563fc4880c262e0cd82c324937f1dbc4f7d8c6bc",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.058483245599999976,
            0.0596026431000001,
            0.02806187199999996,
            -0.13407442909999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "6bf23257f219baaf0f6815e84907344eaf777106f445281d02103bb38096fa13",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05922988379999997,
            0.06402073490000011,
            0.03497633289999996,
            -0.13451883029999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "0f8f8b4cd1c09f2045d0160fbe14f5a75f2748c86767f302e8ddeb2c3aab837e",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06005723339999997,
            0.06833744750000012,
            0.041863977799999966,
            -0.14364753289999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05859065699999997,
            0.05772156760000009,
            0.01865793809999995,
            -0.13380660519999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "3e3aaa870da79fe388e0f5499d4a129f4b6c59a25e2961548c78263e4269df10",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06031447719999997,
            0.06474425900000011,
            0.022856405099999956,
            -0.13407442909999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cd21492cb520c0db2078f74ce5fcd788aed8129adeefb6e2796bb19fa3f4adb3",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06199277639999997,
            0.07180861980000011,
            0.027037159499999963,
            -0.13451883029999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "cf314bcdacfc470a9f2a63b4a35d7ff814c7d7399eb328a184039ab11568cd03",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.06373569179999997,
            0.07882434650000013,
            0.031218224999999968,
            -0.14364753289999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05705240099999998,
            0.0546044995000001,
            0.019273821099999946,
            -0.13380660519999996
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "46976a746afc445d6867c17f5ca795f32b9f1ffc7a5664fb767aebab14118380",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.057264777199999985,
            0.058301777100000104,
            0.024102057299999945,
            -0.13407442909999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "76a66eb3271a1346cfc7e2ff79f6a550dccc258fdcca3a03d4b82eed5b8cf59a",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05743452519999998,
            0.062030409100000114,
            0.028895860099999948,
            -0.13451883029999995
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "2cff3bff54bcad3695deb6c5c45e20262b5a02bb4d1b31cf41aa9465801dbd4a",
          "positive_windows": [
            false,
            true,
            true,
            false
          ],
          "oos_returns": [
            -0.05764720139999998,
            0.06566437090000013,
            0.03378215299999995,
            -0.14364753289999996
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
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0025187597999997424,
            0.02505980930000002,
            -0.14093661139999988,
            -0.14354338419999985
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
            -0.008662516699999664,
            0.03233939420000008,
            -0.14648150669999982,
            -0.1837351356999998
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "1f06fc3ec576c68de3d8e5583156febe08db82be723dbe24bf5392db1a7f65cd",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.00963004989999959,
            0.02276596960000012,
            -0.14368339509999975,
            -0.18714127329999974
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "63376a956e83a815918270479af18ab8fb5019bae65d97baabf0a96d55444f49",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.009326522799999529,
            0.0011573509000000967,
            -0.15280829359999967,
            -0.1684067057999996
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
            0.0028272422000002184,
            0.03238938760000002,
            -0.12746531779999992,
            -0.13716809119999993
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
            0.0012558969000002612,
            0.040375714200000086,
            -0.12035033189999987,
            -0.1540884414999999
          ],
          "positive_window_share": 0.5
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
            -0.0002560386999996972,
            0.028266348100000102,
            -0.11342843179999983,
            -0.16663506459999983
          ],
          "positive_window_share": 0.25
        },
        {
          "config_hash": "a543650991e385a828bf83ebe323ba2a8ab48da8f617c95c59457cd22277ec61",
          "positive_windows": [
            false,
            true,
            false,
            false
          ],
          "oos_returns": [
            -0.0019341450999996596,
            0.01608527740000011,
            -0.09484037799999978,
            -0.1650978282999998
          ],
          "positive_window_share": 0.25
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
            0.005661317500000207,
            0.022183974899999986,
            -0.14977771539999993,
            -0.13567717469999993
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
            0.006771009200000261,
            0.03091265880000002,
            -0.1650246454999999,
            -0.15263746859999988
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
            0.007942300100000299,
            0.03952027830000006,
            -0.18033422439999988,
            -0.16468597669999985
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
            0.009270687400000338,
            0.041173595600000105,
            -0.18419675509999983,
            -0.1578425708999998
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
            0.0051288583000001775,
            0.019675452599999966,
            -0.14326069509999995,
            -0.12580412609999997
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
            0.005486824400000187,
            0.025548002799999983,
            -0.15220943699999992,
            -0.13176240009999993
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
            0.005879864900000198,
            0.031394822,
            -0.1617109513999999,
            -0.14150289669999994
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
            0.0063255163000002085,
            0.03143695800000002,
            -0.15919514549999988,
            -0.1378309201999999
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
            0.008874178500000177,
            0.016146846599999962,
            -0.13838366489999993,
            -0.12444789979999996
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
            0.013013337900000185,
            0.018077669799999977,
            -0.14277363429999992,
            -0.11880731319999993
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
            0.017124834300000197,
            0.01995997889999999,
            -0.1475635874999999,
            -0.14139900759999996
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
            0.021233661700000205,
            0.015755402199999966,
            -0.14033653029999987,
            -0.14970885799999994
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
            0.008414603100000181,
            0.017844918799999967,
            -0.15231442179999993,
            -0.13949545149999998
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
            0.011856827300000206,
            0.021358276699999987,
            -0.17087882079999991,
            -0.14942098909999993
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
            0.015296689400000216,
            0.02482217720000001,
            -0.1807195091999999,
            -0.18187080999999994
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
            0.018790437700000245,
            0.022217238999999993,
            -0.1915859143999999,
            -0.1869159204999999
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
            0.009279573700000196,
            0.020893920099999973,
            -0.14596026239999996,
            -0.1353979268
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
            0.013709282300000222,
            0.0274924475,
            -0.15829613009999993,
            -0.14134178420000001
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
            0.018029788700000243,
            0.03419374990000003,
            -0.17022528719999994,
            -0.1701683632
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
            0.022398261500000273,
            0.030842080900000013,
            -0.1907841946999999,
            -0.17147498080000004
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
            0.013505224900000168,
            0.021188641099999954,
            -0.13498460919999994,
            -0.1338459949
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
            0.02218490130000017,
            0.02806187199999996,
            -0.13611087729999993,
            -0.15062106990000002
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
            0.030893841100000173,
            0.03497633289999996,
            -0.13778445739999995,
            -0.16858937910000002
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
            0.03962365580000017,
            0.041863977799999966,
            -0.13837706219999993,
            -0.16937474260000002
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
            0.0084000547000002,
            0.021188641099999954,
            -0.13380660519999996,
            -0.13555428369999997
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
            0.011895926200000226,
            0.02806187199999996,
            -0.13407442909999995,
            -0.15416617609999997
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
            0.015389633800000246,
            0.03497633289999996,
            -0.13451883029999995,
            -0.17328834919999997
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
            0.018952979000000272,
            0.041863977799999966,
            -0.14364753289999996,
            -0.18079458289999997
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
            0.010273912200000193,
            0.01865793809999995,
            -0.13380660519999996,
            -0.13573800469999997
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
            0.015561788100000223,
            0.022856405099999956,
            -0.13407442909999995,
            -0.14237678379999996
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
            0.021034299200000252,
            0.027037159499999963,
            -0.13451883029999995,
            -0.17328834919999997
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
            0.026487667400000275,
            0.031218224999999968,
            -0.14364753289999996,
            -0.18079458289999997
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
            0.008201931200000179,
            0.019273821099999946,
            -0.13380660519999996,
            -0.13217937329999999
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
            0.01124004640000019,
            0.024102057299999945,
            -0.13407442909999995,
            -0.13503693749999998
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
            0.014222052400000199,
            0.028895860099999948,
            -0.13451883029999995,
            -0.1600466739
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
            0.0171350791000002,
            0.03378215299999995,
            -0.14364753289999996,
            -0.17460692619999996
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
            true
          ],
          "oos_returns": [
            0.06636607209999985,
            -0.14093661139999988,
            -0.14354338419999985,
            0.01768456200000013
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
            0.0780907056999999,
            -0.14648150669999982,
            -0.1837351356999998,
            0.0357751269000002
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
            0.07198759609999993,
            -0.14368339509999975,
            -0.18714127329999974,
            0.04007114660000031
          ],
          "positive_window_share": 0.5
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
            0.05319195599999989,
            -0.15280829359999967,
            -0.1684067057999996,
            0.021153759800000255
          ],
          "positive_window_share": 0.5
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
            0.07373067589999985,
            -0.12746531779999992,
            -0.13716809119999993,
            0.012943390500000115
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
            0.08593829239999991,
            -0.12035033189999987,
            -0.1540884414999999,
            0.02528356620000017
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
            0.07710816419999991,
            -0.11342843179999983,
            -0.16663506459999983,
            0.03756114920000023
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
            0.0680362294999999,
            -0.09484037799999978,
            -0.1650978282999998,
            0.02991420950000025
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
            0.06189073949999983,
            -0.14977771539999993,
            -0.13567717469999993,
            0.016636725600000082
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
            0.07349452599999987,
            -0.1650246454999999,
            -0.15263746859999988,
            0.032304842000000104
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
            0.0850660912999999,
            -0.18033422439999988,
            -0.16468597669999985,
            0.04825520060000013
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
            0.08937129119999995,
            -0.18419675509999983,
            -0.1578425708999998,
            0.06422145450000015
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
            0.05923414259999981,
            -0.14326069509999995,
            -0.12580412609999997,
            0.008045830300000077
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
            0.06790411789999982,
            -0.15220943699999992,
            -0.13176240009999993,
            0.01466496340000009
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
            0.07649049399999984,
            -0.1617109513999999,
            -0.14150289669999994,
            0.012126461100000123
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
            0.07908646629999985,
            -0.15919514549999988,
            -0.1378309201999999,
            0.005432776200000116
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
            0.05550205009999981,
            -0.13838366489999993,
            -0.12444789979999996,
            0.004770260600000076
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
            0.06009700809999982,
            -0.14277363429999992,
            -0.11880731319999993,
            0.00781651840000009
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
            0.06455611559999982,
            -0.1475635874999999,
            -0.14139900759999996,
            0.010809766600000105
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
            0.0626637187999998,
            -0.14033653029999987,
            -0.14970885799999994,
            0.013911263800000118
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "20a225c8b4f7b1dbf23a6281ddefea729a454968ff707bcd45cec7519d6b1933",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.05602982279999981,
            -0.15231442179999993,
            -0.13949545149999998,
            0.007586693300000063
          ],
          "positive_window_share": 0.5
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
            0.06095423099999982,
            -0.17087882079999991,
            -0.14942098909999993,
            0.013457414200000064
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
            0.06574617909999983,
            -0.1807195091999999,
            -0.18187080999999994,
            0.019262867000000065
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
            0.06425076079999979,
            -0.1915859143999999,
            -0.1869159204999999,
            0.025191111600000066
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "ac22899e9617405640d32f4ea94925626d4ff8952dbc8d5acda5ffc217b263b5",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.059175551599999814,
            -0.14596026239999996,
            -0.1353979268,
            0.005783680800000057
          ],
          "positive_window_share": 0.5
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
            0.06733911049999983,
            -0.15829613009999993,
            -0.14134178420000001,
            0.009740179000000052
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
            0.07550598259999984,
            -0.17022528719999994,
            -0.1701683632,
            0.013745550400000046
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
            0.07330828029999982,
            -0.1907841946999999,
            -0.17147498080000004,
            0.01770012520000004
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "c3afbaa8629a17f9e075e8f41158433942f6e9f2ef346831553f5480549d54a7",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0582241597999998,
            -0.13498460919999994,
            -0.1338459949,
            0.0038326708000000565
          ],
          "positive_window_share": 0.5
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
            0.06535726739999981,
            -0.13611087729999993,
            -0.15062106990000002,
            0.0057953967000000505
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
            0.0725287455999998,
            -0.13778445739999995,
            -0.16858937910000002,
            0.0076541146000000445
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
            0.07971321469999981,
            -0.13837706219999993,
            -0.16937474260000002,
            0.009539517900000039
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "99b6d40d50073ff10c74eb62acc384f9811a82c4e00eb39ee822839d93d239b5",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.0582241597999998,
            -0.13380660519999996,
            -0.13555428369999997,
            0.004249333600000057
          ],
          "positive_window_share": 0.5
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
            0.06535726739999981,
            -0.13407442909999995,
            -0.15416617609999997,
            0.00655157640000005
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
            0.0725287455999998,
            -0.13451883029999995,
            -0.17328834919999997,
            0.008829956200000044
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
            0.07971321469999981,
            -0.14364753289999996,
            -0.18079458289999997,
            0.011151128700000039
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "1dbd81a06797a95bf524a061383ad8055a466926ebfd98fdc83bb09ea9722e6a",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.055623647999999803,
            -0.13380660519999996,
            -0.13573800469999997,
            0.004450215200000069
          ],
          "positive_window_share": 0.5
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
            0.05994047269999981,
            -0.13407442909999995,
            -0.14237678379999996,
            0.006940865600000076
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
            0.06431078809999982,
            -0.13451883029999995,
            -0.17328834919999997,
            0.009447641000000083
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
            0.06866339089999982,
            -0.14364753289999996,
            -0.18079458289999997,
            0.01188633680000009
          ],
          "positive_window_share": 0.5
        },
        {
          "config_hash": "d5fd8ca1850d97fc16771fcade6477228a22d1c3279a1ad789f69bc7001850c0",
          "positive_windows": [
            true,
            false,
            false,
            true
          ],
          "oos_returns": [
            0.056261001799999794,
            -0.13380660519999996,
            -0.13217937329999999,
            0.0017663853000000561
          ],
          "positive_window_share": 0.5
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
            0.061225537599999796,
            -0.13407442909999995,
            -0.13503693749999998,
            0.0015853821000000499
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
            0.0662563994999998,
            -0.13451883029999995,
            -0.1600466739,
            0.0013552642000000436
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
            0.07128754339999979,
            -0.14364753289999996,
            -0.17460692619999996,
            0.0010658123000000371
          ],
          "positive_window_share": 0.5
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
    "requested_start": "2021-06-01",
    "data_fingerprint": "f959b6c22cc84c648b21c325d1aafecebdbe0b55ac59db55f9c7031cf85d13e5",
    "run_mode": "research_diagnostic",
    "research_only": true,
    "activation_eligible": false,
    "shadow_run_eligible": false,
    "trading_authorized": false,
    "target": {
      "exposure_id": "hang_seng_tech",
      "stock_code": "513130.SH",
      "sub_layer": "broad_hk_offshore",
      "scope": "formal"
    },
    "selected_configs": [
      {
        "window_id": "wf_000",
        "config_hash": "68ba01cc5f3024790b7fc6f92f93ebea8627b919d60db7c8ffff5e7b697ac400",
        "config": {
          "grid": {
            "step_pct": 0.035,
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
      },
      {
        "window_id": "wf_002",
        "config_hash": "ba114a375a5d23a98d66aa984159766e18746bae30a020eb4780b379d0663e6e",
        "config": {
          "grid": {
            "step_pct": 0.045,
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
        "config_hash": "18c5a21197f2189444ba1135f516edecee9d9c93675fc7529ec8de19bac61906",
        "config": {
          "grid": {
            "step_pct": 0.02,
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
    "profile_id": "grid_plus_optional_trend",
    "profile_hash": "f4f9eb95055b94fd1694c9f43501573cd2e7eb3f2e5590104fa2a83fd6ebf8b1",
    "execution_windows": [
      {
        "window_id": "wf_000",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.035,
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
              "step_pct": 0.035,
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
          "spec_hash": "28627d8386160dd721756e14f3636aecb6e9961f596be112cfca94dfef9d9bfc"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "6c66f8ba5bc583b424b507fe1cd18b63a6152b38b84bed6d844a561fcdc19b58",
            "validation_start": "2024-07-11",
            "validation_end": "2025-01-14",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.38540859800855776,
              "annual_volatility": 0.3265238625659338,
              "sharpe": 1.1803382300450815,
              "sortino": 2.2256473407505055,
              "calmar": 3.018492743320517,
              "worst_126_session_return": 0.17551215000000076,
              "cvar5": -0.03769308951412664,
              "win_rate": 0.456,
              "payoff_ratio": 1.2541144658098842,
              "profit_factor": 1.2324918026062655,
              "turnover": 0.9169117834146594,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9985,
              "max_drawdown": -0.1276824663108469,
              "recovery_sessions": 1,
              "total_cost": 39.985
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "5261c5dea7109d46a9ed40ccb03770fb975dcd32d1d2218936cfd122c78aaae6",
            "validation_start": "2024-07-11",
            "validation_end": "2025-01-14",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.1885726768067597,
              "annual_volatility": 0.16412862233085118,
              "sharpe": 1.1489323076546276,
              "sortino": 2.1199106331108655,
              "calmar": 2.8428882220543397,
              "worst_126_session_return": 0.08946968419999957,
              "cvar5": -0.018917923016052125,
              "win_rate": 0.456,
              "payoff_ratio": 1.4206910546630762,
              "profit_factor": 1.2269604562999294,
              "turnover": 0.8940531487730518,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.05288977358490566,
              "max_drawdown": -0.06633137220938379,
              "recovery_sessions": 1,
              "total_cost": 558.03158
            }
          }
        ]
      },
      {
        "window_id": "wf_001",
        "profile_id": "grid_plus_optional_trend",
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
          "strategy_id": "full_adaptive",
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
          "policy_id": "full_adaptive",
          "spec_hash": "f147e06f02e959eb09abfe5f2df7a3435f9467aacefc6313f7f433d07aa9cb2c"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "3274e19422069735d2b29879bfd6d749ea2c0e1aef5687971ae4d05922309926",
            "validation_start": "2025-01-15",
            "validation_end": "2025-07-24",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.6605960307163599,
              "annual_volatility": 0.3405374611564198,
              "sharpe": 1.9398630284993135,
              "sortino": 2.523461022920332,
              "calmar": 2.765134935336079,
              "worst_126_session_return": 0.2860502384999999,
              "cvar5": -0.048897495925385524,
              "win_rate": 0.544,
              "payoff_ratio": 1.0344582326336744,
              "profit_factor": 1.3272294305488654,
              "turnover": 0.834829203149359,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9976149999999993,
              "max_drawdown": -0.2389019147942847,
              "recovery_sessions": 1,
              "total_cost": 39.97615
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "34d1bbf0b5d64c261e0ab422e7dea8f250893e1a2af8fd493720da2286ef93a2",
            "validation_start": "2025-01-15",
            "validation_end": "2025-07-24",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": 0.29972805174441075,
              "annual_volatility": 0.17022806820658518,
              "sharpe": 1.7607440118551256,
              "sortino": 2.3095171789506925,
              "calmar": 2.3827295950832985,
              "worst_126_session_return": 0.13887078039999912,
              "cvar5": -0.024384286556023205,
              "win_rate": 0.544,
              "payoff_ratio": 1.1052301834765885,
              "profit_factor": 1.3185202188843514,
              "turnover": 0.9213683101260017,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.05775611428571428,
              "max_drawdown": -0.12579188690269005,
              "recovery_sessions": 1,
              "total_cost": 555.32196
            }
          }
        ]
      },
      {
        "window_id": "wf_002",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.045,
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
              "step_pct": 0.045,
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
          "spec_hash": "086cbd2374346ce2c7640384b79196f1f3570b0abc2f963f57b291b5a7442f3f"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "5a033edf5204561c39eaf6f20f5ab6eda571dccd50c29e8f1c683008458aff75",
            "validation_start": "2025-07-25",
            "validation_end": "2026-01-28",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.0008057766786166987,
              "annual_volatility": 0.2365710219117061,
              "sharpe": -0.0034060666944974926,
              "sortino": -0.006927982071003039,
              "calmar": -0.004501219740688023,
              "worst_126_session_return": -0.00039977200000007596,
              "cvar5": -0.028286058757534538,
              "win_rate": 0.512,
              "payoff_ratio": 0.9064819835224833,
              "profit_factor": 1.0178043323761217,
              "turnover": 0.9928399266415426,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 2.9977199999999997,
              "max_drawdown": -0.1790129620496007,
              "recovery_sessions": 21,
              "total_cost": 39.977199999999996
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "9733c2a281f281e965fe222e9db2c963715e9dfd422676377f93b4684bd79563",
            "validation_start": "2025-07-25",
            "validation_end": "2026-01-28",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.004519117931165995,
              "annual_volatility": 0.11829770527534945,
              "sharpe": -0.03820123070559405,
              "sortino": -0.07387794785462481,
              "calmar": -0.047764529235417366,
              "worst_126_session_return": -0.002244184400000293,
              "cvar5": -0.014179042195642014,
              "win_rate": 0.512,
              "payoff_ratio": 0.9405061252651838,
              "profit_factor": 1.0032065336161962,
              "turnover": 0.8323128497761576,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.04507827027027027,
              "max_drawdown": -0.0946124248161766,
              "recovery_sessions": 21,
              "total_cost": 580.0184399999999
            }
          }
        ]
      },
      {
        "window_id": "wf_003",
        "profile_id": "grid_plus_optional_trend",
        "execution_config": {
          "grid": {
            "step_pct": 0.02,
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
              "step_pct": 0.02,
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
          "spec_hash": "9c108e826d19d3a1df9684732fc983644303865ee9ba6ab6865c0379b8058e73"
        },
        "benchmarks": [
          {
            "benchmark_id": "buy_and_hold",
            "version": "1",
            "rebalance_sessions": null,
            "target_weight": 1.0,
            "spec_hash": "3958c38c790b7737f3af03d4a690f2509833bfa7f847fbd3e06c6a8e5cafd0c3",
            "provenance_hash": "165c9e9ed44f0545d9d50565e682079538459046d73787e2fa6141b551f6db95",
            "validation_start": "2026-01-29",
            "validation_end": "2026-08-07",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.345262782246343,
              "annual_volatility": 0.28596470576322097,
              "sharpe": -1.20736152150266,
              "sortino": -2.11382387175025,
              "calmar": -1.2185002106810088,
              "worst_126_session_return": -0.18948061349999978,
              "cvar5": -0.03646337774993241,
              "win_rate": 0.456,
              "payoff_ratio": 0.8633879107319711,
              "profit_factor": 0.8067723100282352,
              "turnover": 1.2085563688372505,
              "minimum_commission_share": 0.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 3.000135135135135,
              "max_drawdown": -0.2833506134999999,
              "recovery_sessions": 126,
              "total_cost": 39.961349999999996
            }
          },
          {
            "benchmark_id": "fixed_half_hold",
            "version": "1",
            "rebalance_sessions": 1,
            "target_weight": 0.5,
            "spec_hash": "ac073b13dfd8fc5232bf30851ba89adea309c68abd84a01a15249842c1d2e597",
            "provenance_hash": "1a46865cdabfccfebc415ec626a9662b104fd95f3519d58e34e659c6578ac031",
            "validation_start": "2026-01-29",
            "validation_end": "2026-08-07",
            "nav_sessions": 126,
            "metrics": {
              "annual_return": -0.1930043558916238,
              "annual_volatility": 0.14299073901299927,
              "sharpe": -1.3497682243189035,
              "sortino": -2.234220884530181,
              "calmar": -1.2510478400308649,
              "worst_126_session_return": -0.10090588700000014,
              "cvar5": -0.018254797315113497,
              "win_rate": 0.456,
              "payoff_ratio": 0.9486745309720384,
              "profit_factor": 0.7952124744912674,
              "turnover": 0.9539236799357531,
              "minimum_commission_share": 1.0,
              "unfilled_share": 0.0,
              "slippage_degradation": 0.05046349514563107,
              "max_drawdown": -0.1542741609999999,
              "recovery_sessions": 126,
              "total_cost": 540.9887
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
      "experiment_id": "round2-hk-tech-20260917",
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
        "513130.SH"
      ]
    },
    "experiment_hash": "40265a573628354ea84457c005a255abb2b91a1ad58d3d25ff66fe6ca425665d",
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
            "provenance_hash": "6c66f8ba5bc583b424b507fe1cd18b63a6152b38b84bed6d844a561fcdc19b58",
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
            "provenance_hash": "5261c5dea7109d46a9ed40ccb03770fb975dcd32d1d2218936cfd122c78aaae6",
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
            "cost_drag": 0.002018794625,
            "cvar5_improvement": 0.024967102278450753,
            "drawdown_improvement": 0.17112546327779973,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5814868384431873,
            "sortino_excess": 1.2138340713020193,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0023203776,
            "cvar5_improvement": 0.025855681707317016,
            "drawdown_improvement": 0.17727234033257133,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5543814241002396,
            "sortino_excess": 1.0992203228081523,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0036492033499999996,
            "cvar5_improvement": 0.02210522030482996,
            "drawdown_improvement": 0.15867781228830957,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.6507132010596028,
            "sortino_excess": 1.3731183737126629,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015780988999999999,
            "cvar5_improvement": 0.024183812513478075,
            "drawdown_improvement": 0.1643267640528323,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.23769949522777536,
            "sortino_excess": 0.48164109163252594,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004914475225,
            "cvar5_improvement": 0.018755048075428556,
            "drawdown_improvement": 0.1508367686610866,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4958236064918097,
            "sortino_excess": 1.0534269422705618,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001972490525,
            "cvar5_improvement": 0.02445509320045088,
            "drawdown_improvement": 0.16565053561049162,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.28512950021888733,
            "sortino_excess": 0.6072648605446573,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026428223500000003,
            "cvar5_improvement": 0.024626216691591568,
            "drawdown_improvement": 0.16678047115589784,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4208969904937846,
            "sortino_excess": 0.9316887845828816,
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
            "cost_drag": 0.00211434775,
            "cvar5_improvement": 0.025227076800267347,
            "drawdown_improvement": 0.17189218739266435,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4405820160914078,
            "sortino_excess": 0.9190960968267988,
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
            "cost_drag": 0.00171665815,
            "cvar5_improvement": 0.025453944515523023,
            "drawdown_improvement": 0.17806792589370352,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.42856291297887067,
            "sortino_excess": 0.8211823332954546,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001634507625,
            "cvar5_improvement": 0.02501699239718002,
            "drawdown_improvement": 0.1685412803090942,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.286310239065466,
            "sortino_excess": 0.565901880228471,
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
            "cost_drag": 0.002293810525,
            "cvar5_improvement": 0.025003090413044916,
            "drawdown_improvement": 0.16972685547486333,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3386423461167666,
            "sortino_excess": 0.7351006382736065,
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
            "cost_drag": 0.0016339640500000001,
            "cvar5_improvement": 0.02481326603804397,
            "drawdown_improvement": 0.16906255222599428,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.30812649607685727,
            "sortino_excess": 0.6203478246588454,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004749768425,
            "cvar5_improvement": 0.020037652354736427,
            "drawdown_improvement": 0.1527485076158266,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.511251875641237,
            "sortino_excess": 1.134417797233827,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002433502375,
            "cvar5_improvement": 0.025280035928151222,
            "drawdown_improvement": 0.1733745010951388,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3888270897312503,
            "sortino_excess": 0.8416573337619996,
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
            "cost_drag": 0.0038920279749999997,
            "cvar5_improvement": 0.020861321235816105,
            "drawdown_improvement": 0.1518542543894386,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4226583854326357,
            "sortino_excess": 0.9292502555100932,
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
            "cost_drag": 0.00497693725,
            "cvar5_improvement": 0.018113646191373473,
            "drawdown_improvement": 0.1473787730707947,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4305136888509056,
            "sortino_excess": 0.9419683184123332,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002244569225,
            "cvar5_improvement": 0.025722595295921996,
            "drawdown_improvement": 0.17562213147130654,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5594259211044028,
            "sortino_excess": 1.144664968980285,
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
            "cost_drag": 0.00225503565,
            "cvar5_improvement": 0.025825798839858128,
            "drawdown_improvement": 0.17534623715572065,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4824930228329951,
            "sortino_excess": 0.9815306754322033,
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
            "cost_drag": 0.0019433322750000003,
            "cvar5_improvement": 0.024767048679957014,
            "drawdown_improvement": 0.16866656518349815,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5007859496653206,
            "sortino_excess": 1.0371120326942944,
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
            "cost_drag": 0.00168930485,
            "cvar5_improvement": 0.025217785053872087,
            "drawdown_improvement": 0.17356172704362915,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.36856540668223525,
            "sortino_excess": 0.7110939593131246,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002373881825,
            "cvar5_improvement": 0.024081374271735304,
            "drawdown_improvement": 0.16337700339619826,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.29706712339389535,
            "sortino_excess": 0.6420795956067034,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024575328,
            "cvar5_improvement": 0.024773701096796108,
            "drawdown_improvement": 0.17157476547796813,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.34087042765232944,
            "sortino_excess": 0.7428269923983675,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004082293650000001,
            "cvar5_improvement": 0.021794672406762004,
            "drawdown_improvement": 0.15484141066464552,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.34478847444838895,
            "sortino_excess": 0.8116159604628028,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.0030878959750000002,
            "cvar5_improvement": 0.023511370973725115,
            "drawdown_improvement": 0.1606417796278799,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4574031721629519,
            "sortino_excess": 1.027938997906922,
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
            "cost_drag": 0.001736373375,
            "cvar5_improvement": 0.023838071254407435,
            "drawdown_improvement": 0.16321574154999197,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.28794387577330594,
            "sortino_excess": 0.5944443813883237,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0034525260500000003,
            "cvar5_improvement": 0.022965041319563565,
            "drawdown_improvement": 0.1604822748748655,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5974585580040828,
            "sortino_excess": 1.2922183299793883,
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
            "cost_drag": 0.00405165275,
            "cvar5_improvement": 0.020017767744168483,
            "drawdown_improvement": 0.14940587102522454,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.42481343317930365,
            "sortino_excess": 0.9467924144668372,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001960711625,
            "cvar5_improvement": 0.024368703118925444,
            "drawdown_improvement": 0.16595520904979877,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.30756229114057104,
            "sortino_excess": 0.6463336575839459,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003687517875,
            "cvar5_improvement": 0.022052238511002145,
            "drawdown_improvement": 0.1564813196095169,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.45950256664299216,
            "sortino_excess": 1.0154856365832035,
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
            "cost_drag": 0.00230985465,
            "cvar5_improvement": 0.025779819054240774,
            "drawdown_improvement": 0.17765114461201073,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.6470668324080279,
            "sortino_excess": 1.313376688299009,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00203928795,
            "cvar5_improvement": 0.025381993190202422,
            "drawdown_improvement": 0.17136624961100597,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5291768343828083,
            "sortino_excess": 1.1296614663149473,
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
            "cost_drag": 0.0021302445,
            "cvar5_improvement": 0.02565891160325926,
            "drawdown_improvement": 0.17468100602462078,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.6224882180772326,
            "sortino_excess": 1.3042350307375028,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018393393499999999,
            "cvar5_improvement": 0.024507247772933935,
            "drawdown_improvement": 0.16625241914541383,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.39262419662382775,
            "sortino_excess": 0.8126151588413683,
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
            "cost_drag": 0.002913438225,
            "cvar5_improvement": 0.024552828471985234,
            "drawdown_improvement": 0.16912132042993747,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5498157508498566,
            "sortino_excess": 1.1612048527161716,
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
            "cost_drag": 0.0018021618749999998,
            "cvar5_improvement": 0.023972530643953802,
            "drawdown_improvement": 0.16410617147804735,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.29375045025222235,
            "sortino_excess": 0.620969634397721,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00298598855,
            "cvar5_improvement": 0.02412842023490866,
            "drawdown_improvement": 0.16848117900751242,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5556732141029181,
            "sortino_excess": 1.1291191677708532,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00212575825,
            "cvar5_improvement": 0.025378390584443557,
            "drawdown_improvement": 0.17126616504342002,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3924961904387493,
            "sortino_excess": 0.8233051975717911,
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
            "cost_drag": 0.00169111185,
            "cvar5_improvement": 0.025597344056714037,
            "drawdown_improvement": 0.17279079596257582,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3342233183494069,
            "sortino_excess": 0.6424818314495143,
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
            "cost_drag": 0.0017202052750000002,
            "cvar5_improvement": 0.02610770347396574,
            "drawdown_improvement": 0.17701166262597529,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.38109856294203076,
            "sortino_excess": 0.7460254182208983,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.002726517225,
            "cvar5_improvement": 0.023547411626803436,
            "drawdown_improvement": 0.16025145350911885,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.31622488455108333,
            "sortino_excess": 0.6968938710748664,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015787465,
            "cvar5_improvement": 0.02404936065975282,
            "drawdown_improvement": 0.16459844182978559,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2480474822928541,
            "sortino_excess": 0.5106147396949576,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019201678250000001,
            "cvar5_improvement": 0.02478618255262072,
            "drawdown_improvement": 0.1680701770639813,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4086731736917848,
            "sortino_excess": 0.875787440186939,
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
            "cost_drag": 0.0021060287,
            "cvar5_improvement": 0.024333042789915892,
            "drawdown_improvement": 0.16485108006185623,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.25946173838286457,
            "sortino_excess": 0.5674260191940002,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003285882875,
            "cvar5_improvement": 0.023111047574938016,
            "drawdown_improvement": 0.15819479654675145,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 0.75,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.33329424634874105,
            "sortino_excess": 0.7537021746903079,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.007612257557028063,
          "execution_cost": 191.56391,
          "grid_return": -0.0027068876770020324,
          "reconciliation_error": 2.7755575615628914e-17,
          "transition_return": -0.05003560618955994,
          "trend_return": -0.09524712922896897
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
            "cost_drag": 0.00225503565,
            "cvar5_improvement": 0.025825798839858128,
            "drawdown_improvement": 0.17534623715572065,
            "exposure_ratio": 0.6051587301587301,
            "family": "grid_only",
            "positive_subperiod_share": 1.0,
            "rejection_reason": null,
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4824930228329951,
            "sortino_excess": 0.9815306754322033,
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
          "policy_id": "full_adaptive",
          "spec_hash": "28627d8386160dd721756e14f3636aecb6e9961f596be112cfca94dfef9d9bfc",
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
            "cost_drag": 0.001903363225,
            "cvar5_improvement": 0.021855029104241933,
            "drawdown_improvement": 0.10698085786362355,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.34758776953038817,
            "sortino_excess": -0.464843707861918,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00226955695,
            "cvar5_improvement": 0.02140584965757881,
            "drawdown_improvement": 0.10727316473547727,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5548117020035064,
            "sortino_excess": -0.7452903844934464,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.003670405025,
            "cvar5_improvement": 0.01778902589470847,
            "drawdown_improvement": 0.08777620552450816,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.43283060696089054,
            "sortino_excess": -0.5306023287478072,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017167170999999998,
            "cvar5_improvement": 0.020749418571063237,
            "drawdown_improvement": 0.09583319808454221,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.48917336811641215,
            "sortino_excess": -0.7820508590400826,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004988776975,
            "cvar5_improvement": 0.016244795655137624,
            "drawdown_improvement": 0.08354245350684367,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.39509106116935144,
            "sortino_excess": -0.46803772588333864,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00208903975,
            "cvar5_improvement": 0.0206822213511728,
            "drawdown_improvement": 0.09610188293422522,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5392702015252804,
            "sortino_excess": -0.8548120269625786,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002816994125,
            "cvar5_improvement": 0.01995529602779007,
            "drawdown_improvement": 0.09495182539937844,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.47688419803391163,
            "sortino_excess": -0.7043791808391656,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002196891125,
            "cvar5_improvement": 0.021298457527944365,
            "drawdown_improvement": 0.10228334833525668,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.46127529533590345,
            "sortino_excess": -0.6967284504620854,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001752580575,
            "cvar5_improvement": 0.021934584681844005,
            "drawdown_improvement": 0.10984196508738558,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4063694844053031,
            "sortino_excess": -0.5715341587993581,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017660885250000001,
            "cvar5_improvement": 0.021617697427752998,
            "drawdown_improvement": 0.1004733972156785,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4352533699171556,
            "sortino_excess": -0.6563740558767557,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0024485536000000002,
            "cvar5_improvement": 0.020223800563742837,
            "drawdown_improvement": 0.09578604235651778,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4769798431055732,
            "sortino_excess": -0.6885615194818011,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00172762095,
            "cvar5_improvement": 0.02154066127873846,
            "drawdown_improvement": 0.10143304231751504,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.45466340912137815,
            "sortino_excess": -0.6964605124300602,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00488595665,
            "cvar5_improvement": 0.017289549446013148,
            "drawdown_improvement": 0.0839362438978811,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4251511198471819,
            "sortino_excess": -0.5361302324305743,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026449599,
            "cvar5_improvement": 0.02006277198486724,
            "drawdown_improvement": 0.09655743588796309,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4399324507432895,
            "sortino_excess": -0.5686736793634026,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0041082202,
            "cvar5_improvement": 0.018119743992576636,
            "drawdown_improvement": 0.08834144050436488,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.27455607538714943,
            "sortino_excess": -0.2585653242498813,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0052701688,
            "cvar5_improvement": 0.015234095218986816,
            "drawdown_improvement": 0.07806638319136722,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5145006481135348,
            "sortino_excess": -0.5954170542702021,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022158838,
            "cvar5_improvement": 0.021350505862111444,
            "drawdown_improvement": 0.10755883502740926,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4271339038815183,
            "sortino_excess": -0.608601765938281,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00222232305,
            "cvar5_improvement": 0.021708235594765996,
            "drawdown_improvement": 0.10813372111578845,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.532967794463383,
            "sortino_excess": -0.7642528087144648,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018981895500000002,
            "cvar5_improvement": 0.02190664807950865,
            "drawdown_improvement": 0.10448156938231906,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3659267903475707,
            "sortino_excess": -0.5151859255505118,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017700495499999999,
            "cvar5_improvement": 0.02192062721575831,
            "drawdown_improvement": 0.10661578684700132,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.40979223810186327,
            "sortino_excess": -0.5945382578671838,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00254221375,
            "cvar5_improvement": 0.020000848093303318,
            "drawdown_improvement": 0.09303291024272364,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5124544804535203,
            "sortino_excess": -0.8093688087908365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025352843999999998,
            "cvar5_improvement": 0.02011571799976839,
            "drawdown_improvement": 0.10089980794191619,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41194457212285884,
            "sortino_excess": -0.46471915814786524,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004200253725,
            "cvar5_improvement": 0.018774293641925455,
            "drawdown_improvement": 0.0868140726651064,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4891015904377454,
            "sortino_excess": -0.6880080174337998,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.0032445343250000003,
            "cvar5_improvement": 0.01925733992030606,
            "drawdown_improvement": 0.08652902228566728,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.47891734938935604,
            "sortino_excess": -0.6697537714986297,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001769018925,
            "cvar5_improvement": 0.020655362167007103,
            "drawdown_improvement": 0.09560746790129968,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4847381576114083,
            "sortino_excess": -0.7752195596595012,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0036149525749999997,
            "cvar5_improvement": 0.01844703732463583,
            "drawdown_improvement": 0.08430858487943388,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4454370271835814,
            "sortino_excess": -0.5748579327819936,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004198573075,
            "cvar5_improvement": 0.01798182086556241,
            "drawdown_improvement": 0.08629105240061477,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19988592778676384,
            "sortino_excess": -0.005209375430297314,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020574187,
            "cvar5_improvement": 0.020599992176420272,
            "drawdown_improvement": 0.0967000344365051,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4989197577907529,
            "sortino_excess": -0.7887282651645254,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0038762034,
            "cvar5_improvement": 0.01873478460121003,
            "drawdown_improvement": 0.08881729556098003,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.28354062155341864,
            "sortino_excess": -0.3277708856759309,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00226039015,
            "cvar5_improvement": 0.021066664515688442,
            "drawdown_improvement": 0.10651342550433834,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.49261577042531,
            "sortino_excess": -0.6612818993176761,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020585385,
            "cvar5_improvement": 0.0212162861718612,
            "drawdown_improvement": 0.09865536676139866,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3696741325296956,
            "sortino_excess": -0.5109841656280031,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002004941125,
            "cvar5_improvement": 0.021596003432693286,
            "drawdown_improvement": 0.10283150067046357,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.29642375018218836,
            "sortino_excess": -0.3541682835786115,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018333178749999999,
            "cvar5_improvement": 0.021548295204549303,
            "drawdown_improvement": 0.10002181734424773,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4264149806778933,
            "sortino_excess": -0.6458406139660263,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00309139245,
            "cvar5_improvement": 0.019628082451276882,
            "drawdown_improvement": 0.09544068785604759,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4453521995073905,
            "sortino_excess": -0.6065669377688199,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018655714,
            "cvar5_improvement": 0.020184248445931384,
            "drawdown_improvement": 0.09368407135379753,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4858917291066637,
            "sortino_excess": -0.7729180435485365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0030624765000000003,
            "cvar5_improvement": 0.019599294588716832,
            "drawdown_improvement": 0.09885569725565002,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.41701376651548955,
            "sortino_excess": -0.5277588206904983,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022337056999999997,
            "cvar5_improvement": 0.02144485441685301,
            "drawdown_improvement": 0.10113887783733033,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5486234716308369,
            "sortino_excess": -0.8363514641963887,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018159848249999998,
            "cvar5_improvement": 0.022028649072889928,
            "drawdown_improvement": 0.10520011873304325,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3786292929636167,
            "sortino_excess": -0.528337295409524,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001806191275,
            "cvar5_improvement": 0.02208368932441843,
            "drawdown_improvement": 0.10793558338654749,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3633131824229335,
            "sortino_excess": -0.4825081773162667,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00287413955,
            "cvar5_improvement": 0.019609809498862544,
            "drawdown_improvement": 0.08870748190801397,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5151143253450521,
            "sortino_excess": -0.7864820647786415,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016851993749999999,
            "cvar5_improvement": 0.020679521554199432,
            "drawdown_improvement": 0.09631879606298285,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4978074907209593,
            "sortino_excess": -0.7977550873517382,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001961594675,
            "cvar5_improvement": 0.020761231750799972,
            "drawdown_improvement": 0.0962096635576942,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.42783875175918634,
            "sortino_excess": -0.6457767341163508,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0022513267250000002,
            "cvar5_improvement": 0.020105140374190714,
            "drawdown_improvement": 0.09358806345596596,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.5128942404636165,
            "sortino_excess": -0.8035893258957538,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034669737750000003,
            "cvar5_improvement": 0.019628025707687617,
            "drawdown_improvement": 0.0898763011433133,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4059070974045612,
            "sortino_excess": -0.5798056193216694,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.013000799314851545,
          "execution_cost": 316.82344,
          "grid_return": -0.11721543429276227,
          "reconciliation_error": 5.551115123125783e-17,
          "transition_return": -0.023552757686466037,
          "trend_return": -0.06960002526744682
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
            "cost_drag": 0.004198573075,
            "cvar5_improvement": 0.01798182086556241,
            "drawdown_improvement": 0.08629105240061477,
            "exposure_ratio": 0.6448412698412699,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.19988592778676384,
            "sortino_excess": -0.005209375430297314,
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
          "policy_id": "full_adaptive",
          "spec_hash": "f147e06f02e959eb09abfe5f2df7a3435f9467aacefc6313f7f433d07aa9cb2c",
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
            "provenance_hash": "5a033edf5204561c39eaf6f20f5ab6eda571dccd50c29e8f1c683008458aff75",
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
            "provenance_hash": "9733c2a281f281e965fe222e9db2c963715e9dfd422676377f93b4684bd79563",
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
            "cost_drag": 0.0017773137499999998,
            "cvar5_improvement": 0.026681771709090713,
            "drawdown_improvement": 0.12711495386229743,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.06904791683503564,
            "sortino_excess": 0.4107729938832365,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00212906355,
            "cvar5_improvement": 0.02595564992009688,
            "drawdown_improvement": 0.12744086219132247,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.4283272287804023,
            "sortino_excess": -0.7181790212327823,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.00345003475,
            "cvar5_improvement": 0.02471657562746053,
            "drawdown_improvement": 0.12068642684763695,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.052034486281169134,
            "sortino_excess": 0.04079691886023859,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017039639,
            "cvar5_improvement": 0.02437169116548239,
            "drawdown_improvement": 0.11744226517790277,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.12008670655191976,
            "sortino_excess": -0.05417262079442138,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004755711175,
            "cvar5_improvement": 0.021511832072624585,
            "drawdown_improvement": 0.10698004463802471,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.2908205404460862,
            "sortino_excess": -0.5486061033398875,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00208961185,
            "cvar5_improvement": 0.024300290056075678,
            "drawdown_improvement": 0.11807497212573664,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.23247915079488568,
            "sortino_excess": -0.29860229165350516,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002901526475,
            "cvar5_improvement": 0.024554011618480594,
            "drawdown_improvement": 0.1175163547151882,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.023576308794577956,
            "sortino_excess": 0.22865559899788723,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002197820125,
            "cvar5_improvement": 0.02610220177934558,
            "drawdown_improvement": 0.1260738891338603,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.07820833247195545,
            "sortino_excess": 0.2742229082575105,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00162383075,
            "cvar5_improvement": 0.026745022089747487,
            "drawdown_improvement": 0.13333549592297428,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.0616498661844342,
            "sortino_excess": 0.10657114232572931,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017642789249999998,
            "cvar5_improvement": 0.02611373226697665,
            "drawdown_improvement": 0.12243350372530715,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.14871628039982604,
            "sortino_excess": 0.4936538625582065,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00255950895,
            "cvar5_improvement": 0.025150327646497408,
            "drawdown_improvement": 0.12091289588166668,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.10256129771373357,
            "sortino_excess": 0.41955701550503793,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001712839725,
            "cvar5_improvement": 0.025803138852537613,
            "drawdown_improvement": 0.12473277206682618,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.0232983113921263,
            "sortino_excess": 0.3651325156104453,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004640965225,
            "cvar5_improvement": 0.022746517568644185,
            "drawdown_improvement": 0.10985796361102015,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.22991164560726338,
            "sortino_excess": -0.473958920985603,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025879694749999997,
            "cvar5_improvement": 0.025455008476041027,
            "drawdown_improvement": 0.122732420357693,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.0443358100888015,
            "sortino_excess": 0.24175296291802587,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00372682075,
            "cvar5_improvement": 0.024453881387166154,
            "drawdown_improvement": 0.11682571233167038,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.05220626647890901,
            "sortino_excess": -0.062120686940010855,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.005051066825,
            "cvar5_improvement": 0.020632309185533253,
            "drawdown_improvement": 0.10120707096496481,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.3625234887392517,
            "sortino_excess": -0.5739472475048306,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00206205195,
            "cvar5_improvement": 0.026568226143978586,
            "drawdown_improvement": 0.13168940902902979,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.03638048520431394,
            "sortino_excess": 0.03904330800380376,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00209763715,
            "cvar5_improvement": 0.026182650665838945,
            "drawdown_improvement": 0.1285997935831644,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.329023568929614,
            "sortino_excess": -0.6021249439543742,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017908272,
            "cvar5_improvement": 0.02661136142591626,
            "drawdown_improvement": 0.12530089388118518,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.08793475472457307,
            "sortino_excess": 0.3648191897142977,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001662171925,
            "cvar5_improvement": 0.02659553475504799,
            "drawdown_improvement": 0.13000915544637068,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.028444392545136688,
            "sortino_excess": 0.2316205218951426,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002605901575,
            "cvar5_improvement": 0.023909805879717923,
            "drawdown_improvement": 0.11548359740106687,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.11456766802920842,
            "sortino_excess": -0.014542436779428097,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0025223551,
            "cvar5_improvement": 0.025863637386919706,
            "drawdown_improvement": 0.12863439034962001,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.03722979206075411,
            "sortino_excess": 0.2842659102260967,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004422010525,
            "cvar5_improvement": 0.023608362945872294,
            "drawdown_improvement": 0.11183048248580199,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.07629171854165097,
            "sortino_excess": -0.056529505174556446,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.003106385525,
            "cvar5_improvement": 0.024851773866055228,
            "drawdown_improvement": 0.11484727900644548,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.034376066709742595,
            "sortino_excess": -0.07205534906136102,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001769072275,
            "cvar5_improvement": 0.02443574430802028,
            "drawdown_improvement": 0.11789738671179653,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.08458548956257711,
            "sortino_excess": 0.051860668047836664,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0033736796749999996,
            "cvar5_improvement": 0.024852964938074353,
            "drawdown_improvement": 0.11521276449651033,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.09402064656492339,
            "sortino_excess": -0.09541252044181675,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0038035424999999998,
            "cvar5_improvement": 0.024315269440141965,
            "drawdown_improvement": 0.11261590385072898,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.25,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.03280154878660199,
            "sortino_excess": 0.12021552955620746,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00204644785,
            "cvar5_improvement": 0.02439436600173822,
            "drawdown_improvement": 0.11967811573306372,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.15265250953373657,
            "sortino_excess": -0.14483820747420162,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003588814575,
            "cvar5_improvement": 0.024771042209407998,
            "drawdown_improvement": 0.11797954034657088,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.06256960048125149,
            "sortino_excess": 0.046984303690910834,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0020819822750000002,
            "cvar5_improvement": 0.026513315718950263,
            "drawdown_improvement": 0.1315247049873504,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.12816303600741605,
            "sortino_excess": -0.02086614818548438,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001977189625,
            "cvar5_improvement": 0.026442801953195396,
            "drawdown_improvement": 0.12797855399159488,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.1386358198160306,
            "sortino_excess": 0.3499620502067541,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019070668,
            "cvar5_improvement": 0.02699361825966415,
            "drawdown_improvement": 0.13425225954642486,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.22780775663513161,
            "sortino_excess": 0.5711081919807507,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017589757500000001,
            "cvar5_improvement": 0.025951253147734367,
            "drawdown_improvement": 0.12157978918242929,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.0960136335963106,
            "sortino_excess": 0.31095101492924415,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0029693143,
            "cvar5_improvement": 0.02448418899114591,
            "drawdown_improvement": 0.11782458974416304,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.01325313413829813,
            "sortino_excess": 0.21017879011715124,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001890708525,
            "cvar5_improvement": 0.024244948144887757,
            "drawdown_improvement": 0.11883029549955695,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06754191452915737,
            "sortino_excess": 0.04267870593900851,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0029739218499999997,
            "cvar5_improvement": 0.02464181413185751,
            "drawdown_improvement": 0.12112978429082338,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.05667807289844411,
            "sortino_excess": 0.34978417844881676,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002256200475,
            "cvar5_improvement": 0.025739730766414313,
            "drawdown_improvement": 0.1224706802481288,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.13941282900265758,
            "sortino_excess": -0.24885375351598488,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0017079541999999999,
            "cvar5_improvement": 0.026869445856062553,
            "drawdown_improvement": 0.1265999933624784,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.07149649050663298,
            "sortino_excess": 0.32281989169767455,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00167907985,
            "cvar5_improvement": 0.027111985256547514,
            "drawdown_improvement": 0.12883372999172502,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.04685644508429193,
            "sortino_excess": 0.35524933584976287,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.003006173425,
            "cvar5_improvement": 0.02398891012661638,
            "drawdown_improvement": 0.11433925888498006,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1452580679772876,
            "sortino_excess": -0.10911596727293618,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016598305499999997,
            "cvar5_improvement": 0.024060864905405467,
            "drawdown_improvement": 0.11746127649925037,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.17767358387783616,
            "sortino_excess": -0.1903872210718403,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019133174750000002,
            "cvar5_improvement": 0.025661044758044503,
            "drawdown_improvement": 0.1234530801083018,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.13201947307630058,
            "sortino_excess": 0.2883407223110734,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0023204089,
            "cvar5_improvement": 0.02393057192619522,
            "drawdown_improvement": 0.11631398519536185,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.1418535703127347,
            "sortino_excess": -0.10919091400720479,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0035082188,
            "cvar5_improvement": 0.024334895352850737,
            "drawdown_improvement": 0.11606316931720359,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": -0.06714810426718655,
            "sortino_excess": 0.013771458413618543,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": -0.012418506758307336,
          "execution_cost": 157.22263,
          "grid_return": -0.054349972410142146,
          "reconciliation_error": -1.5612511283791264e-17,
          "transition_return": 0.012982814426223326,
          "trend_return": 0.040539867527067175
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
            "cost_drag": 0.0019070668,
            "cvar5_improvement": 0.02699361825966415,
            "drawdown_improvement": 0.13425225954642486,
            "exposure_ratio": 0.6805555555555556,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.22780775663513161,
            "sortino_excess": 0.5711081919807507,
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
          "policy_id": "full_adaptive",
          "spec_hash": "086cbd2374346ce2c7640384b79196f1f3570b0abc2f963f57b291b5a7442f3f",
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
            "provenance_hash": "165c9e9ed44f0545d9d50565e682079538459046d73787e2fa6141b551f6db95",
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
                "unit_pct": 0.2
              },
              "trend": {
                "add_n": 0.5,
                "amount_ratio_min": null,
                "max_units": 4,
                "require_macd_bullish": true,
                "risk_per_unit": 0.005,
                "stop_n": 2.0
              }
            },
            "provenance_hash": "1a46865cdabfccfebc415ec626a9662b104fd95f3519d58e34e659c6578ac031",
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
            "cost_drag": 0.0015275011000000002,
            "cvar5_improvement": 0.026256884003388357,
            "drawdown_improvement": 0.13152547119728142,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4157472826077126,
            "sortino_excess": 1.0266592613281473,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001920548625,
            "cvar5_improvement": 0.02540524433408653,
            "drawdown_improvement": 0.1297530287689214,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.07119558068174614,
            "sortino_excess": 0.12878983858530257,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.003339203075,
            "cvar5_improvement": 0.024988284833422643,
            "drawdown_improvement": 0.12666197920010833,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.6536959742887309,
            "sortino_excess": 1.2306527830542007,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015392446749999998,
            "cvar5_improvement": 0.023294260131126607,
            "drawdown_improvement": 0.11348829325895807,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.24480206361007845,
            "sortino_excess": 0.567819415049063,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004619289425,
            "cvar5_improvement": 0.022619354917099873,
            "drawdown_improvement": 0.1180265712722163,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3049141305253662,
            "sortino_excess": 0.2825168760151444,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019353973000000003,
            "cvar5_improvement": 0.023305748001457963,
            "drawdown_improvement": 0.11378812610730424,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.17158979269603147,
            "sortino_excess": 0.40516209717612106,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00275149695,
            "cvar5_improvement": 0.02411751497021773,
            "drawdown_improvement": 0.12163948118426121,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.46130807958428643,
            "sortino_excess": 0.9812754454412187,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019857142,
            "cvar5_improvement": 0.025440004683789947,
            "drawdown_improvement": 0.12328864926751948,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4747677165586936,
            "sortino_excess": 0.9823771466953404,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00145608385,
            "cvar5_improvement": 0.025675129877183407,
            "drawdown_improvement": 0.1270075340510271,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.29106053303041474,
            "sortino_excess": 0.7219444838199466,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00158452665,
            "cvar5_improvement": 0.025234479161119684,
            "drawdown_improvement": 0.12029893713484299,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5015861778538223,
            "sortino_excess": 1.1175435061536627,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00236916325,
            "cvar5_improvement": 0.02410148827898675,
            "drawdown_improvement": 0.11720899789621525,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5004843619384092,
            "sortino_excess": 1.1104514505199372,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001560669725,
            "cvar5_improvement": 0.024565852838037805,
            "drawdown_improvement": 0.11866302358080313,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3906550347847407,
            "sortino_excess": 1.0019976251783114,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00453476045,
            "cvar5_improvement": 0.023361916508745032,
            "drawdown_improvement": 0.11767141833870554,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.35523065675267707,
            "sortino_excess": 0.42770597942030747,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002383236225,
            "cvar5_improvement": 0.02434913346452047,
            "drawdown_improvement": 0.12075249120925816,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4499619987847786,
            "sortino_excess": 0.918043105698609,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00362610375,
            "cvar5_improvement": 0.024650341205899966,
            "drawdown_improvement": 0.12627714826976735,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.581822882439595,
            "sortino_excess": 0.905805638630715,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0047248789,
            "cvar5_improvement": 0.021228699611361337,
            "drawdown_improvement": 0.11200258219233267,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.11746961435799352,
            "sortino_excess": 0.012392569242842835,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00182358735,
            "cvar5_improvement": 0.0259695140866344,
            "drawdown_improvement": 0.13217605491311465,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3722654940950091,
            "sortino_excess": 0.7616282069826181,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0019078762750000002,
            "cvar5_improvement": 0.02563721153318496,
            "drawdown_improvement": 0.1284283667699921,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.1401269137558043,
            "sortino_excess": 0.2395760282697878,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001563177425,
            "cvar5_improvement": 0.02610405754848078,
            "drawdown_improvement": 0.12724582023618436,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4398927943172025,
            "sortino_excess": 0.991270581016952,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001502268125,
            "cvar5_improvement": 0.025466606230092118,
            "drawdown_improvement": 0.1238026034374739,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.38907047411151563,
            "sortino_excess": 0.8636211768295312,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002475520075,
            "cvar5_improvement": 0.023202412390950777,
            "drawdown_improvement": 0.11462571208841746,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.29128787912593684,
            "sortino_excess": 0.6838987566121246,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002302409425,
            "cvar5_improvement": 0.02485169770217182,
            "drawdown_improvement": 0.1286175973120727,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.44388426926490665,
            "sortino_excess": 0.9196508948004439,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.004336648375,
            "cvar5_improvement": 0.023569401772505022,
            "drawdown_improvement": 0.11287599745799051,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4005434415689628,
            "sortino_excess": 0.7335559210503675,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
                "transfer_fee_rate": 0.0
              },
              "grid": {
                "atr_stop_multiple": 3.0,
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
            "cost_drag": 0.002999244525,
            "cvar5_improvement": 0.024427035547109885,
            "drawdown_improvement": 0.11501009823262703,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4955020398335724,
            "sortino_excess": 0.8878214891123033,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001585406875,
            "cvar5_improvement": 0.02348447983873514,
            "drawdown_improvement": 0.11469834657136799,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.28362559028868606,
            "sortino_excess": 0.676271553997068,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0032642853,
            "cvar5_improvement": 0.024856296071691014,
            "drawdown_improvement": 0.11834444399027805,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.5252789719246739,
            "sortino_excess": 1.006601265284526,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.003499249825,
            "cvar5_improvement": 0.024745669104075982,
            "drawdown_improvement": 0.12402359815894723,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.551241094821395,
            "sortino_excess": 0.964665490100453,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018597972000000001,
            "cvar5_improvement": 0.02339970438564276,
            "drawdown_improvement": 0.11538776806870943,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2337334524854869,
            "sortino_excess": 0.5226776740132802,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034987867,
            "cvar5_improvement": 0.024736256633383878,
            "drawdown_improvement": 0.12099516976638483,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.642649778419157,
            "sortino_excess": 0.9842981722752108,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0018165005,
            "cvar5_improvement": 0.025979398516533407,
            "drawdown_improvement": 0.1337860797488162,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2843295505550697,
            "sortino_excess": 0.6869316418089502,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.001736052075,
            "cvar5_improvement": 0.025574497623670058,
            "drawdown_improvement": 0.12485408678704119,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4310021655653307,
            "sortino_excess": 0.8919700483063076,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00164307605,
            "cvar5_improvement": 0.026166269138243846,
            "drawdown_improvement": 0.13201332170318827,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.49396201666445716,
            "sortino_excess": 1.0556363115617526,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00155349835,
            "cvar5_improvement": 0.025319041777058276,
            "drawdown_improvement": 0.12095348055413027,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4549911930565227,
            "sortino_excess": 0.9387199843812601,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00278528125,
            "cvar5_improvement": 0.024194826891182745,
            "drawdown_improvement": 0.12536821308685847,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4318902292289671,
            "sortino_excess": 0.8834165608424659,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016942513750000002,
            "cvar5_improvement": 0.023142250973700387,
            "drawdown_improvement": 0.11393025170231097,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.28176468611221056,
            "sortino_excess": 0.6505057611949037,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0026532637999999997,
            "cvar5_improvement": 0.024559011970450066,
            "drawdown_improvement": 0.13171577866959375,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.42890924233731026,
            "sortino_excess": 0.910414440614944,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.002084099175,
            "cvar5_improvement": 0.02511861179011498,
            "drawdown_improvement": 0.11971685759519746,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2954197716753513,
            "sortino_excess": 0.5392821034094039,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0015129955999999998,
            "cvar5_improvement": 0.02610531599380856,
            "drawdown_improvement": 0.1262414363470871,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4149481695426156,
            "sortino_excess": 0.9455400228150508,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0014686550249999998,
            "cvar5_improvement": 0.02640003273982003,
            "drawdown_improvement": 0.1302822042150151,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.3831789239982725,
            "sortino_excess": 0.9704355800026018,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
                "slippage_bps": 3.0,
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
            "cost_drag": 0.0029031642499999996,
            "cvar5_improvement": 0.023079814225583833,
            "drawdown_improvement": 0.11153477031389991,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.30378044161515777,
            "sortino_excess": 0.6767536052668794,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.00151495585,
            "cvar5_improvement": 0.022786975806257048,
            "drawdown_improvement": 0.1115401166499915,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.19576923733952256,
            "sortino_excess": 0.44142402363861044,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0016946287749999998,
            "cvar5_improvement": 0.024760046489687576,
            "drawdown_improvement": 0.11941270958286992,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4522824817709386,
            "sortino_excess": 0.871788505832347,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0021446215,
            "cvar5_improvement": 0.022730484503411436,
            "drawdown_improvement": 0.11155096839956785,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.2468211183833056,
            "sortino_excess": 0.5585524232237026,
            "stable": false
          },
          {
            "config": {
              "cost": {
                "commission_rate": 0.0001,
                "minimum_commission": 5.0,
                "sell_tax_rate": 0.0,
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
            "cost_drag": 0.0034268936500000003,
            "cvar5_improvement": 0.023722255200031912,
            "drawdown_improvement": 0.11454781083381185,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.4113728549028586,
            "sortino_excess": 0.8347714697532288,
            "stable": false
          }
        ],
        "excess_attribution": {
          "cash_opportunity_cost": 0.12515994953518533,
          "execution_cost": 159.28327,
          "grid_return": 0.030256627288885306,
          "reconciliation_error": -2.7755575615628914e-17,
          "transition_return": 0.0032404718138600956,
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
                "unit_pct": 0.2
              },
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
            "cost_drag": 0.003339203075,
            "cvar5_improvement": 0.024988284833422643,
            "drawdown_improvement": 0.12666197920010833,
            "exposure_ratio": 0.7162698412698413,
            "family": "grid_only",
            "positive_subperiod_share": 0.5,
            "rejection_reason": "outside_stable_plateau",
            "screened_axes": [
              "step_pct",
              "unit_pct"
            ],
            "sharpe_excess": 0.6536959742887309,
            "sortino_excess": 1.2306527830542007,
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
          "policy_id": "full_adaptive",
          "spec_hash": "9c108e826d19d3a1df9684732fc983644303865ee9ba6ab6865c0379b8058e73",
          "strategy_id": "full_adaptive",
          "version": "1"
        },
        "window_id": "wf_003"
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
        "event_date": "2024-07-15",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 99900,
        "raw_price": 0.50015
      },
      {
        "event_date": "2024-07-22",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 30600,
        "raw_price": 0.47914369999999995
      },
      {
        "event_date": "2024-07-26",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 130500,
        "raw_price": 0.4628611
      },
      {
        "event_date": "2024-08-19",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 101800,
        "raw_price": 0.470141
      },
      {
        "event_date": "2024-09-20",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 30000,
        "raw_price": 0.4858542
      },
      {
        "event_date": "2024-09-25",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 28300,
        "raw_price": 0.5328401
      },
      {
        "event_date": "2024-09-27",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 28200,
        "raw_price": 0.5708287
      },
      {
        "event_date": "2024-09-30",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 16600,
        "raw_price": 0.6101829999999999
      },
      {
        "event_date": "2024-10-08",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 12800,
        "raw_price": 0.7022105999999999
      },
      {
        "event_date": "2024-10-09",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 44700,
        "raw_price": 0.6448065000000001
      },
      {
        "event_date": "2024-12-09",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 86500,
        "raw_price": 0.5971791
      },
      {
        "event_date": "2024-12-11",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 25400,
        "raw_price": 0.6208137
      },
      {
        "event_date": "2024-12-17",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 26200,
        "raw_price": 0.5931778999999999
      },
      {
        "event_date": "2025-01-08",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 87300,
        "raw_price": 0.5868239
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 288200,
        "traded_value": "149481.3309500"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 2,
        "shares": 56800,
        "traded_value": "30203.05819999999585000"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 217800,
        "traded_value": "111633.1000200"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 3,
        "shares": 83700,
        "traded_value": "45423.6688100"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 28200,
        "traded_value": "16097.3693400"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 2,
        "shares": 29400,
        "traded_value": "19117.3334799999970600"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 44700,
        "traded_value": "28822.8505500000044700"
      }
    },
    "invested_sessions": 60,
    "cash_sessions": 66,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_001",
    "trade_points": [
      {
        "event_date": "2025-01-17",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 84200,
        "raw_price": 0.5931778999999999
      },
      {
        "event_date": "2025-01-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 32900,
        "raw_price": 0.6218134000000001
      },
      {
        "event_date": "2025-01-23",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 33000,
        "raw_price": 0.6181854
      },
      {
        "event_date": "2025-01-24",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 33300,
        "raw_price": 0.6071821
      },
      {
        "event_date": "2025-01-27",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 33000,
        "raw_price": 0.6288113000000001
      },
      {
        "event_date": "2025-02-06",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 32200,
        "raw_price": 0.6588023000000001
      },
      {
        "event_date": "2025-02-07",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 31700,
        "raw_price": 0.6757972000000001
      },
      {
        "event_date": "2025-02-10",
        "kind": "rejected_order",
        "reason": "insufficient shares",
        "shares": null,
        "raw_price": null
      },
      {
        "event_date": "2025-02-11",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 6700,
        "raw_price": 0.709787
      },
      {
        "event_date": "2025-02-17",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 13800,
        "raw_price": 0.7472241
      },
      {
        "event_date": "2025-02-20",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 11400,
        "raw_price": 0.7532259
      },
      {
        "event_date": "2025-02-24",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 9600,
        "raw_price": 0.780234
      },
      {
        "event_date": "2025-03-04",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 48800,
        "raw_price": 0.7247825
      },
      {
        "event_date": "2025-05-13",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 73800,
        "raw_price": 0.7242172
      },
      {
        "event_date": "2025-05-14",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 29700,
        "raw_price": 0.7152145
      },
      {
        "event_date": "2025-05-20",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 29800,
        "raw_price": 0.7062118
      },
      {
        "event_date": "2025-05-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 16300,
        "raw_price": 0.6842052000000001
      },
      {
        "event_date": "2025-05-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 29900,
        "raw_price": 0.6967909
      },
      {
        "event_date": "2025-06-10",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 29700,
        "raw_price": 0.7227831
      },
      {
        "event_date": "2025-06-16",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 30200,
        "raw_price": 0.6942081999999999
      },
      {
        "event_date": "2025-06-20",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 120200,
        "raw_price": 0.6807957000000001
      },
      {
        "event_date": "2025-06-25",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 72600,
        "raw_price": 0.710213
      },
      {
        "event_date": "2025-07-04",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 29400,
        "raw_price": 0.6922075999999999
      },
      {
        "event_date": "2025-07-09",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 29200,
        "raw_price": 0.7037888
      },
      {
        "event_date": "2025-07-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 28900,
        "raw_price": 0.719784
      },
      {
        "event_date": "2025-07-21",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 28200,
        "raw_price": 0.7437768
      },
      {
        "event_date": "2025-07-24",
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
        "shares": 230600,
        "traded_value": "154954.2723399999915800"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 9,
        "shares": 275700,
        "traded_value": "188472.2413600000129800"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 7,
        "shares": 201700,
        "traded_value": "135374.8002599999956700"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 6700,
        "traded_value": "4755.572900"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 3,
        "shares": 34800,
        "traded_value": "26388.7142400"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 48800,
        "traded_value": "35369.3860000"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 1,
        "shares": 120200,
        "traded_value": "81831.6431400000120200"
      }
    },
    "invested_sessions": 75,
    "cash_sessions": 51,
    "rejected_order_count": 2
  },
  {
    "window_id": "wf_002",
    "trade_points": [
      {
        "event_date": "2025-08-07",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 67700,
        "raw_price": 0.7382213999999999
      },
      {
        "event_date": "2025-08-26",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 26500,
        "raw_price": 0.7707687000000001
      },
      {
        "event_date": "2025-09-17",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 25500,
        "raw_price": 0.8147555
      },
      {
        "event_date": "2025-09-22",
        "kind": "fill",
        "reason": "grid_to_trend_rebalance",
        "shares": 2400,
        "raw_price": 0.8307507
      },
      {
        "event_date": "2025-09-26",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 13000,
        "raw_price": 0.8392516999999999
      },
      {
        "event_date": "2025-10-09",
        "kind": "fill",
        "reason": "trend_add",
        "shares": 11800,
        "raw_price": 0.8672601
      },
      {
        "event_date": "2025-10-14",
        "kind": "fill",
        "reason": "trend_stop",
        "shares": 38100,
        "raw_price": 0.8207537
      },
      {
        "event_date": "2025-10-30",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 63300,
        "raw_price": 0.8152444999999999
      },
      {
        "event_date": "2025-11-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 26200,
        "raw_price": 0.7632289
      },
      {
        "event_date": "2025-11-18",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 89500,
        "raw_price": 0.7547735
      },
      {
        "event_date": "2026-01-26",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 66400,
        "raw_price": 0.7472241
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 197400,
        "traded_value": "151198.2458699999869000"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 2,
        "shares": 52000,
        "traded_value": "41201.6358000000026500"
      },
      "grid_to_trend_rebalance": {
        "reason": "grid_to_trend_rebalance",
        "fill_count": 1,
        "shares": 2400,
        "traded_value": "1993.8016800"
      },
      "trend_add": {
        "reason": "trend_add",
        "fill_count": 2,
        "shares": 24800,
        "traded_value": "21143.9412799999987000"
      },
      "trend_stop": {
        "reason": "trend_stop",
        "fill_count": 1,
        "shares": 38100,
        "traded_value": "31270.7159700"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 1,
        "shares": 26200,
        "traded_value": "19996.5971800"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 1,
        "shares": 89500,
        "traded_value": "67552.2282500"
      }
    },
    "invested_sessions": 58,
    "cash_sessions": 68,
    "rejected_order_count": 0
  },
  {
    "window_id": "wf_003",
    "trade_points": [
      {
        "event_date": "2026-04-28",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 80800,
        "raw_price": 0.6181854
      },
      {
        "event_date": "2026-05-08",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 31800,
        "raw_price": 0.6368089
      },
      {
        "event_date": "2026-05-18",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 32600,
        "raw_price": 0.6141842
      },
      {
        "event_date": "2026-05-22",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 81600,
        "raw_price": 0.6038188
      },
      {
        "event_date": "2026-06-03",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 77800,
        "raw_price": 0.6391917
      },
      {
        "event_date": "2026-06-05",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 31700,
        "raw_price": 0.6171850999999999
      },
      {
        "event_date": "2026-06-09",
        "kind": "fill",
        "reason": "grid_stop",
        "shares": 109500,
        "raw_price": 0.5928221
      },
      {
        "event_date": "2026-07-21",
        "kind": "fill",
        "reason": "grid_initialize",
        "shares": 80000,
        "raw_price": 0.5941782
      },
      {
        "event_date": "2026-07-27",
        "kind": "fill",
        "reason": "grid_buy",
        "shares": 32400,
        "raw_price": 0.5781734
      },
      {
        "event_date": "2026-07-30",
        "kind": "fill",
        "reason": "grid_sell",
        "shares": 31900,
        "raw_price": 0.6068179
      }
    ],
    "by_reason": {
      "grid_initialize": {
        "reason": "grid_initialize",
        "fill_count": 3,
        "shares": 238600,
        "traded_value": "147212.7505800"
      },
      "grid_sell": {
        "reason": "grid_sell",
        "fill_count": 2,
        "shares": 63700,
        "traded_value": "39608.0140300"
      },
      "grid_buy": {
        "reason": "grid_buy",
        "fill_count": 3,
        "shares": 96700,
        "traded_value": "58319.9907499999968300"
      },
      "grid_stop": {
        "reason": "grid_stop",
        "fill_count": 2,
        "shares": 191100,
        "traded_value": "114185.6340300"
      }
    },
    "invested_sessions": 33,
    "cash_sessions": 93,
    "rejected_order_count": 0
  }
]
## Excess return diagnostics

Contributions sum daily net excess returns; execution_cost is a separate currency diagnostic already embedded in NAV.

### wf_000

Largest absolute contributor: trend_return (-0.09524713).
Next research action: Study trend entry/exit filters and stop distances on training windows.

### wf_001

Largest absolute contributor: grid_return (-0.11721543).
Next research action: Study grid spacing, sizing and stop/cooldown behavior on training windows.

### wf_002

Largest absolute contributor: grid_return (-0.05434997).
Next research action: Study grid spacing, sizing and stop/cooldown behavior on training windows.

### wf_003

Largest absolute contributor: cash_opportunity_cost (0.12515995).
Next research action: Study cash exposure and re-entry timing on training windows.

Research evidence only; no broker action is authorized.
