# Chapter 05: Engineering Practice

モデルが一度動くだけでは開発完了ではありません。テスト、debug、入力検証、性能計測を
使って、変更に耐えられるコードへ近づけます。

## Lessons

1. `01_testing_tensors.py` — unittestとTensor比較
2. `02_debugging_shapes.py` — shape検証と明確な例外
3. `03_custom_dataset.py` — 独自Dataset
4. `04_inference_and_profiling.py` — inference_modeとprofiler

## Reading missions

- テスト名から保証対象を推測し、実装のどの行に対応するか探す。
- failureを期待値、実際値、例外位置、原因仮説へ分解する。
- 入力検証がmodule内部ではなく境界に置かれる理由を説明する。
- profiler出力から、時間を使う演算と呼び出し関係を読む。

## Change missions

- 正常系テストを壊さず、境界値または異常系テストを一つ追加する。
- shape検証の条件を変更し、エラーメッセージの有用性を比較する。
- inference処理のgradient記録を切り替え、状態と性能差を観察する。

## Build mission

既存関数に対して「修正前には失敗するテスト」を先に追加し、必要最小限の修正で通します。
テストが実装詳細ではなく外部から見える契約を検証しているか説明します。

## Completion criteria

- テストとtracebackから、調査対象を少数の行へ絞り込める。
- 正常系、境界値、異常系で不足している契約を発見できる。
- failureの原因仮説を一つずつ検証できる。
- 回帰テストを先に書き、最小修正を実装できる。
