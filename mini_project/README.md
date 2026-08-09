# Capstone: Structured Training Project

単一scriptから卒業し、責務ごとに分割した小さな分類projectです。外部datasetは不要です。

```text
mini_project/
├─ config.py   # 学習設定
├─ data.py     # datasetとDataLoader
├─ model.py    # model定義
├─ engine.py   # train/evaluate処理
└─ train.py    # CLIと全体の組み立て
```

## Run

```powershell
python -m mini_project.train --epochs 10 --output artifacts/model.pt
```

`artifacts/`は生成物なのでGitへcommitしません。実行後はloss、validation accuracy、
checkpoint pathを確認してください。

## Development exercises

1. hidden sizeを変え、parameter数とaccuracyを比較する。
2. SGDをAdamへ変更し、同じseedでloss推移を比較する。
3. model入力shapeの異常系testを追加する。
4. checkpointへoptimizer stateとepochを追加し、学習再開を実装する。
5. synthetic dataを実datasetへ置き換える前に、data leakageの可能性を列挙する。
