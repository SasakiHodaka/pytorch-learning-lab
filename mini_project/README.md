# Capstone: Structured Training Project

単一scriptから卒業し、責務ごとに分割した小さな分類projectです。外部datasetは不要です。
白紙から書き直すのではなく、既存applicationを読み、変更要求の影響範囲を判断し、
module境界を保ったまま修正するための読解教材として使用します。

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

## Reading order

1. `train.py`でapplicationの入口と呼び出し順を確認する。
2. `config.py`で外部から変更できる値を確認する。
3. `data.py`で入力とtargetの生成過程を追跡する。
4. `model.py`でTensor shapeの変化を追跡する。
5. `engine.py`で学習と評価の状態変更を分離する。
6. `tests/test_mini_project.py`で保証されている契約を確認する。

## Change protocol

変更前に次を記録します。

- 要求を満たすために変わる責務
- 変更候補fileと理由
- 変えてはいけない公開API
- 追加または変更するテスト
- 予想される副作用

実装後は予想と実際の差を記録し、一つの要求を一つのコミットにします。

## Development exercises

1. hidden sizeを変え、parameter数とaccuracyを比較する。
2. SGDをAdamへ変更し、同じseedでloss推移を比較する。
3. model入力shapeの異常系testを追加する。
4. checkpointへoptimizer stateとepochを追加し、学習再開を実装する。
5. synthetic dataを実datasetへ置き換える前に、data leakageの可能性を列挙する。
