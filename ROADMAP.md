# Roadmap: Code Reader to PyTorch Contributor

## Goal

最終目標は、PyTorchコードを使えるだけでなく、未知のコードを読み、変更の影響を判断し、
テストを伴う安全な修正を作り、PyTorch本体へのPull Requestを準備できることです。

能力の優先順位は次の通りです。

1. 既存コードを根拠付きで読む
2. 影響範囲を予測して安全に変更する
3. 分解した仕様からコードを書く

具体的な5段階の学習方法と評価尺度は[Education Program](lessons/README.md)を参照します。

## Stage 0: Python code reading

教材: [`lessons/00_python_foundations`](lessons/00_python_foundations/)

読む対象:

- 値、型、式、変数
- 分岐、loop、関数
- collection、class、例外、file操作

能力ゲート:

- 初見の短い関数について、入力から戻り値までを追跡できる。
- 実行される分岐とloop回数を具体的な入力で説明できる。
- tracebackから、自作コード内の原因候補を見つけられる。
- テストから`python_mean`の正常系と異常系を読み、自力実装できる。

## Stage 1: Tensor data-flow reading

教材: [`lessons/01_tensor_fundamentals`](lessons/01_tensor_fundamentals/)

読む対象:

- Tensor生成、shape、dtype、device
- indexing、reshape、transpose
- 要素演算、行列積、broadcasting
- NumPyとの共有、copy、device移動

能力ゲート:

- 初見のTensor処理について、各行のshapeを追跡できる。
- 演算が成功する条件とshape errorの原因を説明できる。
- viewとcopyの変更伝播をテストで示せる。
- `normalize_rows`をshape契約を保って実装できる。

## Stage 2: Autograd and optimization reading

教材: [`lessons/02_autograd_and_optimization`](lessons/02_autograd_and_optimization/)

読む対象:

- 計算グラフ、leaf Tensor、gradient
- gradient蓄積と初期化
- forward、loss、backward、parameter update
- 手動更新とOptimizer

能力ゲート:

- 学習loopを責務ごとに分解できる。
- `.grad`が作られ、蓄積され、消去される箇所を特定できる。
- learning rate変更の影響を予測して検証できる。
- `squared_error_gradient`をautogradで実装できる。

## Stage 3: Model architecture reading

教材: [`lessons/03_neural_networks`](lessons/03_neural_networks/)

読む対象:

- `nn.Module`、parameter、`__init__`、`forward`
- activation、logits、prediction、loss
- 小さな分類model

能力ゲート:

- model構造とforwardのデータフローを説明できる。
- 各層の入力・出力shapeとparameter shapeを追跡できる。
- architecture変更で影響する層とテストを事前に列挙できる。
- 指定shapeを満たす`make_classifier`を実装できる。

## Stage 4: Training pipeline reading

教材: [`lessons/04_data_and_training`](lessons/04_data_and_training/)

読む対象:

- Dataset、DataLoader、sample、batch
- trainingとevaluation
- checkpoint、seed、device

能力ゲート:

- dataからmetricまで複数関数をまたぐ流れを追跡できる。
- trainingとevaluationの状態変更を区別できる。
- batch sizeやcheckpoint項目の変更影響を説明できる。
- `classification_accuracy`をTensor操作で実装できる。

## Stage 5: Failure and test reading

教材: [`lessons/05_engineering_practice`](lessons/05_engineering_practice/)

読む対象:

- unittest、Tensor比較、正常系・境界値・異常系
- traceback、shape検証、例外message
- Dataset契約、inference mode、profiler

能力ゲート:

- failureを期待、実際、位置、原因仮説へ分解できる。
- 既存テストが保証していないedge caseを発見できる。
- 修正前に失敗する回帰テストを書ける。
- 仮説を一つずつ検証し、必要最小限の修正を作れる。

## Stage 6: Multi-module application reading

教材:

- [`lessons/06_advanced_development`](lessons/06_advanced_development/)
- [`mini_project`](mini_project/)

読む対象:

- CNN、validation、class別metric
- scheduler、gradient clipping
- config、data、model、engine、CLI、testの依存関係

能力ゲート:

- 複数moduleの呼び出しとデータフローを図示できる。
- 機能要求から変更候補fileとテストを事前に列挙できる。
- 公開APIと責務境界を保って機能を追加できる。
- 複数fileの変更を、一つの目的を持つコミットへまとめられる。

## Stage 7: PyTorch internals and OSS contribution

教材: [`lessons/07_internals_and_oss`](lessons/07_internals_and_oss/)

読む対象:

- 公開Python API、実装file、dispatcher、C++/ATen
- 公式テスト、Issue、Contribution Guide
- custom autograd、gradcheck

能力ゲート:

- 公開APIから関連実装と公式テストを探せる。
- 巨大なcodebaseで目的に必要な範囲だけを読める。
- Issueの事実、原因仮説、判断、未確認事項を分離できる。
- 最小再現、回帰テスト、最小修正を含むPRを準備できる。

## Session workflow

1回の学習では一つの読解対象だけを扱います。

```text
Survey → Trace → Contract → Change → Build → Review → Commit
```

記録には最低限、次を含めます。

- 読んだ責務とデータフロー
- テストから抽出した契約
- 変更前の影響予測
- 実際の検証結果
- 予測との差と原因
- 実行したコマンド
- コミットhash

進捗は[`PROGRESS.md`](PROGRESS.md)へRead・Change・Buildを分けて記録します。

## Definition of program completion

- 未知のコードを、名前の印象ではなく定義・呼び出し・テストを根拠に説明できる。
- 変更前に影響範囲を予測し、テストで予測を検証できる。
- failureから調査範囲を絞り、原因仮説を段階的に検証できる。
- 既存設計へ合わせた実装と回帰テストを書ける。
- 自分の変更を第三者が再現・レビューできる形で説明できる。
- PyTorch本体へ品質のあるPRを提出し、reviewへ対応できる。

MergeはMaintainerの判断にも依存します。必須成果はPR-readyな品質とレビュー対応能力、
最終的な挑戦目標はMaintainer承認とMergeです。
