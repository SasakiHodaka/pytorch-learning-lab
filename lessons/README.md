# Lessons

Python未経験者が、基礎文法からPyTorchの内部調査とOSS貢献準備まで進むための
実行可能な教材です。必ずChapter 00から順に進めてください。

## Curriculum

| Chapter | 内容 | ファイル数 |
| --- | --- | ---: |
| [`00_python_foundations`](00_python_foundations/) | Python文法、関数、collection、class、例外 | 6 |
| [`01_tensor_fundamentals`](01_tensor_fundamentals/) | Tensor、shape、演算、NumPy、device | 4 |
| [`02_autograd_and_optimization`](02_autograd_and_optimization/) | 自動微分、勾配、最適化 | 3 |
| [`03_neural_networks`](03_neural_networks/) | nn.Module、loss、分類器 | 3 |
| [`04_data_and_training`](04_data_and_training/) | Dataset、学習・評価、保存、再現性 | 4 |
| [`05_engineering_practice`](05_engineering_practice/) | test、debug、独自Dataset、profiling | 4 |
| [`06_advanced_development`](06_advanced_development/) | CNN、validation、学習制御、capstone | 3 + project |
| [`07_internals_and_oss`](07_internals_and_oss/) | source調査、custom autograd、Issue、PR | 2 + templates |

## How to study

1. ChapterのREADMEで目的と完了条件を読む。
2. コードを上から一行ずつ読み、出力を予想する。
3. リポジトリのルートからファイルを実行する。
4. `assert`が何を確認しているか、自分の言葉で説明する。
5. 値やshapeを一つだけ変え、結果またはerrorを観察する。
6. Chapter完了後に[`practice/`](../practice/)の問題を解く。
7. [`PROGRESS.md`](../PROGRESS.md)へ理解度を記録する。

最初から暗記する必要はありません。errorは失敗ではなく、理解を深める観察対象です。

## Run examples

```powershell
python lessons/00_python_foundations/01_values_and_variables.py
python lessons/01_tensor_fundamentals/01_create_and_inspect.py
```

完成済みLessonをすべて検証する場合:

```powershell
python tools/run_all_lessons.py
python -m unittest tests/test_solutions.py -v
```

練習問題のテストは、`practice/exercises.py`を実装してから実行します。

```powershell
python -m unittest tests/test_exercises.py -v
```
