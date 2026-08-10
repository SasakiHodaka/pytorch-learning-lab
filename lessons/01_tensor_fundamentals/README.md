# Chapter 01: Tensor Fundamentals

Tensorは、形状・データ型・計算装置を持つ多次元の数値配列です。モデルへの入力、
parameter、予測、loss、gradientはTensorとして表現されます。

## Lessons

1. `01_create_and_inspect.py` — 作成、shape、dtype、device
2. `02_index_and_reshape.py` — indexing、slicing、reshape
3. `03_operations_and_broadcasting.py` — 要素演算、行列積、broadcasting
4. `04_numpy_and_devices.py` — NumPyとの共有、copy、device移動

## Reading missions

- 各Tensorの生成箇所と`shape`、`dtype`、`device`を一覧にする。
- indexing、reshape、transposeの前後でshapeを追跡する。
- `*`と`@`の入力・出力shapeから、演算の意味を判定する。
- NumPyとTensorの一方を変更したとき、共有された値が変わる箇所を特定する。

## Change missions

- 入力shapeを一つだけ変え、成功する演算と失敗する演算を予測する。
- broadcastingへ新しい次元を加え、どの軸が拡張されるか説明する。
- viewをcopyへ変更し、変更伝播の違いをテストする。

## Build mission

`practice.normalize_rows`を実装します。行合計のshapeとbroadcastingをコード実行前に
説明し、元のshapeが保たれるテストを通します。

## Completion criteria

- 初見のTensorコードで主要なshape、dtype、deviceを追跡できる。
- 要素積、行列積、broadcastingをコードとshapeから判別できる。
- viewとcopy、CPUとacceleratorの影響範囲を説明・検証できる。
- shapeを保つTensor関数とテストを追加できる。
