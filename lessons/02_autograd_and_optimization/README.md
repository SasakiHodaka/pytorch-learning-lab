# Chapter 02: Autograd and Optimization

モデル学習は、予測、loss計算、微分、parameter更新の繰り返しです。この章では
自動微分を手計算と照合し、最後にOptimizerへつなげます。

## Lessons

1. `01_computation_graph.py` — 計算グラフとgradient
2. `02_gradient_accumulation.py` — 勾配蓄積とzeroing
3. `03_linear_regression.py` — 手動更新とOptimizer

## Completion criteria

- `.grad`が何を表すか説明できる。
- `backward()`前後と`zero_grad()`の必要性を説明できる。
- 一つのparameterをlossに基づいて更新できる。
