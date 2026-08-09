# Chapter 05: Engineering Practice

モデルが一度動くだけでは開発完了ではありません。テスト、debug、入力検証、性能計測を
使って、変更に耐えられるコードへ近づけます。

## Lessons

1. `01_testing_tensors.py` — unittestとTensor比較
2. `02_debugging_shapes.py` — shape検証と明確な例外
3. `03_custom_dataset.py` — 独自Dataset
4. `04_inference_and_profiling.py` — inference_modeとprofiler

## Completion criteria

- 浮動小数点Tensorを適切な許容誤差で比較できる。
- shape errorを層の奥ではなく入力境界で発見できる。
- Datasetの責務を説明し、自作できる。
- 推論時にgradient記録を止める理由を説明できる。
