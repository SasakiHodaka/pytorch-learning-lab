# Chapter 06: Advanced Development

ここまでの部品を実案件に近い判断へつなげます。画像batchを扱うCNN、train/validation
分割、学習率調整、gradient clippingを学び、最後にcapstone projectを実行します。

## Lessons

1. `01_convolutional_network.py` — image shapeとCNN
2. `02_validation_and_metrics.py` — validationとconfusion matrix
3. `03_training_controls.py` — schedulerとgradient clipping
4. [`../../mini_project/`](../../mini_project/) — 分割されたtraining application

## Reading missions

- CNN各層を通る`[batch, channel, height, width]`を追跡する。
- validation metricの集計単位と、class別情報が失われる箇所を探す。
- schedulerとgradient clippingが学習loopのどこへ介入するか特定する。
- mini projectのCLIからconfig、data、model、engineへの依存関係を図にする。

## Change missions

- CNNの一層を変更し、後続層へ必要な修正を事前に列挙する。
- metricを一つ追加し、計算、表示、テストへの影響範囲を追跡する。
- mini projectへ設定項目を一つ追加し、module境界を保って伝播させる。

## Build mission

mini projectへ小さな機能要求を追加します。コードを書く前に変更候補file、公開API、必要な
テストを列挙し、実装後に予測した影響範囲と実際の差を振り返ります。

## Completion criteria

- 複数moduleの依存関係とデータフローを図示できる。
- 要求から変更候補と影響範囲をコード編集前に列挙できる。
- 公開APIとmodule境界を保って機能を追加できる。
- 複数fileの変更をテスト付きの小さなコミットへまとめられる。
