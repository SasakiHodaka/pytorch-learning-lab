# Chapter 02: Autograd and Optimization

モデル学習は、予測、loss計算、微分、parameter更新の繰り返しです。この章では
自動微分を手計算と照合し、最後にOptimizerへつなげます。

## Lessons

1. `01_computation_graph.py` — 計算グラフとgradient
2. `02_gradient_accumulation.py` — 勾配蓄積とzeroing
3. `03_linear_regression.py` — 手動更新とOptimizer

## Reading missions

- leaf Tensorからlossまでの計算グラフを演算単位で追跡する。
- `backward()`の前後で`.grad`とparameterがどう変化するか記録する。
- 学習loopをforward、loss、backward、update、zeroingへ分解する。
- 手動更新とOptimizer版で、同じ責務を持つ行を対応付ける。

## Change missions

- `zero_grad()`を外した場合の2回目のgradientを予測・検証する。
- learning rateを一つ変更し、parameter更新量への影響を説明する。
- loss式を変更し、計算グラフとgradientへの影響を追跡する。

## Build mission

`practice.squared_error_gradient`を実装します。数式、Tensor演算、`.grad`の対応を説明し、
既存APIを変えずにテストを通します。

## Completion criteria

- 初見の学習loopを5つの責務に分解できる。
- `.grad`の発生源と蓄積箇所をコード上で特定できる。
- parameter更新式の変更影響を予測・検証できる。
- 自動微分を使う小さな関数をテスト付きで実装できる。
