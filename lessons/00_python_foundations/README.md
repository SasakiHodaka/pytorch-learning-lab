# Chapter 00: Python Foundations

PyTorchはPythonから操作します。この章では文法の暗記ではなく、短いPythonコードから
名前、データフロー、分岐、繰り返し、例外を読み取る力を作ります。

## Lessons

1. `01_values_and_variables.py` — 値、変数、型、演算
2. `02_conditions_and_loops.py` — 条件分岐と繰り返し
3. `03_functions.py` — 関数、引数、戻り値、型ヒント
4. `04_collections.py` — list、tuple、dict、enumerate
5. `05_classes.py` — class、instance、method
6. `06_errors_and_files.py` — 例外、path、ファイル

## Run

```powershell
python lessons/00_python_foundations/01_values_and_variables.py
```

## Reading missions

- 代入の右辺から左辺へ、値と型がどう結び付くか追跡する。
- `if`と`for`について、実行される行とされない行を特定する。
- 関数の呼び出しから戻り値までを、引数の具体値で追跡する。
- list、tuple、dict、classについて、値の所有者と変更箇所を区別する。
- tracebackを下から読み、例外が発生した最初の自作コードを探す。

## Change missions

- 変数を一つ変更し、その値が使われる出力とassertを特定する。
- 条件を一つ追加し、既存の入力で処理経路が変わらないことを確認する。
- 正常入力の動作を保ったまま、不正入力へ`ValueError`を追加する。

## Build mission

`practice.python_mean`を実装します。先にテストから正常系と空listの契約を読み取り、
疑似コードを書いてから実装します。

## Completion criteria

- 初見の短い関数について、入力から戻り値までを自力で追跡できる。
- 分岐とloopの実行経路を具体的な入力で説明できる。
- テストから正常系、境界値、異常系の仕様を抽出できる。
- 既存動作を保ちながら、小さな関数と例外処理を追加できる。
