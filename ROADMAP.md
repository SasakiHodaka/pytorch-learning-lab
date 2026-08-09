# Roadmap: Beginner to PyTorch Contributor

## 1. Goal and definition of success

このプロジェクトの最終目標は、PyTorchを使ったモデルを作れるだけでなく、
PyTorch本体のIssueを再現・調査し、実装修正と回帰テストをPull Requestとして提出し、
Maintainerのレビューに対応できる状態になることです。

最終的な成功条件は次の通りです。

- PyTorchの主要概念を、自分の言葉と実行可能なコードで説明できる。
- 学んだAPIについて、関連する公式実装と公式テストを探せる。
- バグ報告から最小再現コード、原因仮説、修正、回帰テストを作成できる。
- PyTorchのContribution Guide、Issue、CI、レビューの手順に従える。
- PyTorch本体へコードとテストを含むPRを提出し、レビューへ継続対応する。
- 最終到達目標として、PRのMaintainer承認とMergeを目指す。

MergeはMaintainerの判断やプロジェクト状況にも依存するため、学習上の必須成果は
「品質のあるPRを提出し、レビュー対応できること」、最終成果は「Merge」と区別します。

## 2. Learning principles

各テーマは次のサイクルで学びます。

```text
概念を説明する
  ↓
小さなコードで使う
  ↓
出力を予想して実験する
  ↓
正常系・境界値・異常系をテストする
  ↓
公式ドキュメントを確認する
  ↓
PyTorch本体の実装とテストを読む
  ↓
学習ノートへ根拠と疑問を残す
```

先に大量のファイルを作らず、一つのLessonを理解・検証してから次へ進みます。
各Phaseの完了条件を満たすまでは、次のPhaseを「完了」としません。

## 3. Phase roadmap

### Phase 0: Foundation

目的: 再現可能で安全な学習環境とGit運用を整える。

学ぶこと:

- Python仮想環境、依存関係、CPU/GPUとdevice
- Gitのstatus、diff、add、commit、branch、remote
- 小さく意味のあるコミットとREADMEの更新

成果物:

- `requirements.txt`
- `.gitignore`
- `README.md`
- `ROADMAP.md`

完了条件:

- 新しい環境でセットアップ手順を再現できる。
- 意図したファイルだけをコミットできる。
- リポジトリの目的、現在地、次の作業をREADMEから判断できる。

状態: **完了**

### Phase 1: Tensor fundamentals

目的: Tensorを「AI用の魔法」ではなく、形状・型・配置を持つ数値データとして理解する。

予定Lesson:

1. `01_tensor_basics.py` — 生成、shape、dtype、device
2. `02_tensor_operations.py` — indexing、reshape、broadcasting、集約
3. `03_matrix_operations.py` — dot product、matrix multiplication、次元の整合性
4. `04_numpy_interop.py` — NumPy変換、copy、共有メモリ

完了条件:

- scalar、vector、matrix、高次元Tensorを区別できる。
- shape、dtype、deviceが計算へ与える影響を説明できる。
- 要素積と行列積の違いを、shapeを使って説明できる。
- broadcastingの成功例と失敗例を予測できる。
- NumPyとの共有メモリとcopyの違いを実験で示せる。

### Phase 2: Autograd and optimization

目的: 学習を「Lossから勾配を計算し、Parameterを更新する処理」として理解する。

予定Lesson:

1. `05_autograd_basics.py` — `requires_grad`、計算グラフ、leaf Tensor
2. `06_backward_and_gradients.py` — `backward()`、勾配蓄積、`zero_grad`
3. `07_linear_regression.py` — 予測、Loss、勾配、手動更新
4. `08_optimizer_basics.py` — SGDと`optimizer.step()`

完了条件:

- forward、loss、backward、parameter updateを順に説明できる。
- 微分値と`.grad`の対応を手計算で確認できる。
- 勾配が蓄積する理由とリセットが必要な理由を説明できる。
- autogradを使わない更新とOptimizerによる更新を比較できる。

### Phase 3: Neural networks and training

目的: `nn.Module`を使って、再現可能な学習・評価ループを構築する。

予定Lesson:

1. `09_nn_module.py` — Module、Parameter、forward
2. `10_activation_and_loss.py` — Linear、ReLU、損失関数
3. `11_training_loop.py` — train/eval、epoch、metric
4. `12_dataset_dataloader.py` — Dataset、DataLoader、batch
5. `13_classification.py` — 分類モデルの学習と評価
6. `14_model_save_load.py` — `state_dict`、保存、再開、推論

完了条件:

- モデル、Loss、Optimizer、DataLoaderの責務を説明できる。
- 学習と評価で挙動を切り替える理由を説明できる。
- seedを設定し、学習結果と環境情報を記録できる。
- 過学習、データリーク、accuracyだけに依存する危険を理解する。
- 保存済みweightを読み込み、同じ入力に推論できる。

### Phase 4: Testing and engineering quality

目的: 動くだけのコードから、変更を安全に検証できるコードへ進む。

学ぶこと:

- pytest、assert、fixture、parameterize
- 正常系、境界値、異常系、回帰テスト
- 例外型とエラーメッセージ
- 型ヒント、lint、再現性、最小依存

予定構成:

```text
08_testing/
└─ examples/
tests/
├─ test_tensor_basics.py
├─ test_tensor_operations.py
└─ test_training_loop.py
```

完了条件:

- バグを再現する「修正前には失敗するテスト」を書ける。
- 実装詳細ではなく、公開された動作をテストできる。
- edge caseを列挙し、どれをテスト対象にするか説明できる。
- テスト、lint、実行手順を一つずつ再現できる。

### Phase 5: PyTorch internals and source reading

目的: Python APIから、実装、dispatcher、ATen、autograd、テストへの経路を追う。

学ぶこと:

- `torch/`のPython frontend
- `torch/csrc/`のPython/C++境界
- `aten/src/ATen/`とnative operators
- dispatcherとoperator registrationの概観
- `torch/autograd`と`torch/csrc/autograd`
- `test/`配下の公式テスト

予定構成:

```text
07_pytorch_internals/
09_source_reading/
├─ linear.md
├─ relu.md
└─ tensor_operation.md
```

各source-reading noteには次を記録します。

- 公開APIと最小使用例
- 入力、出力、edge case
- Python側の入口
- C++/ATen側の実装候補
- 関連する公式テスト
- 調査時点のPyTorch commit hash
- 未解決の疑問

完了条件:

- 一つの公開APIから関連実装とテストを見つけられる。
- Pythonだけの変更とC++ buildが必要な変更を区別できる。
- 読んだコードを断定しすぎず、根拠となるpathとcommitを示せる。

### Phase 6: Contribution environment

目的: `pytorch/pytorch`をForkし、対象を絞った開発とテストを行えるようにする。

手順:

1. 公式Guideと`CONTRIBUTING.md`を最新状態で読む。
2. GitHub上でForkし、`origin`と`upstream`を設定する。
3. 公式が案内する開発方法を選び、環境情報を記録する。
4. 変更対象に近い既存テストを一つ実行する。
5. 小さなローカル変更で、テストが失敗・成功する流れを確認する。
6. lintと対象テストの実行方法を記録する。

ゲート:

- Forkとupstream同期を自力で行える。
- 対象テストを一件指定して実行できる。
- Buildが必要な変更の所要時間と環境制約を把握している。
- PyTorch本体とlearning-labの変更を混同しない。

### Phase 7: Issue selection and investigation

目的: 解決可能で合意された課題を選び、コードを書く前に問題を正確に定義する。

Issue選定基準:

- Maintainerが`actionable`と判断している。
- 他のContributorが作業中ではないことを確認できる。
- 期待動作と実際の動作を説明できる。
- 最小再現が作れる、または既存テストから再現できる。
- 初回貢献として変更範囲と検証コストが現実的である。
- ドキュメントだけでなく、可能なら実装修正とテスト追加を含められる。

調査テンプレート:

```text
Issue URL:
PyTorch commit:
Environment:
Expected behavior:
Actual behavior:
Minimal reproduction:
Suspected area:
Related tests:
Hypothesis:
Open questions:
```

予定構成:

```text
10_oss_practice/
├─ issue_analysis/
├─ reproductions/
└─ notes/
```

ゲート:

- Issueの言い換えではなく、自分で現象を再現できる。
- 原因と症状を区別し、仮説を検証する手順がある。
- Maintainerとの合意が必要な点を、実装前に質問できる。

### Phase 8: Fix, regression test, and Pull Request

目的: 最小で保守可能な修正を作り、第三者が検証できるPRとして提出する。

実装順序:

```text
Issue確認
  ↓
最小再現
  ↓
失敗する回帰テスト
  ↓
原因の特定
  ↓
必要最小限の修正
  ↓
対象テスト・関連テスト・lint
  ↓
self-review
  ↓
Pull Request
```

PR提出前チェック:

- Issueが`actionable`で、PRから参照されている。
- unrelatedな変更や生成ファイルが含まれていない。
- 修正前に失敗し、修正後に成功するテストがある。
- 変更理由、実装判断、検証コマンドを説明できる。
- 既存style、型、互換性、エラーメッセージを確認した。
- AI支援の有無にかかわらず、全行を本人が理解・検証した。
- Contribution Guideの最新要件を再確認した。

完了条件:

- PRを提出し、CI結果を読める。
- レビューコメントへ根拠を持って回答できる。
- 必要な修正を追加し、変更履歴を追跡できる。

### Phase 9: Review and merge

目的: Maintainerとのレビューを通じて変更品質を高め、Mergeを目指す。

行動原則:

- レビューを要望ではなく技術的フィードバックとして読む。
- 不明点は推測で直さず、理解した内容を確認する。
- 修正ごとに対象テストを再実行する。
- Scope拡大が必要ならIssue/PR上で合意を取る。
- Mergeされない場合も、技術的理由と学びを記録する。

到達状態:

1. **PR-ready contributor** — 品質のあるPRを提出しレビュー対応できる。
2. **Merged contributor** — PRがMaintainerに承認されMergeされる。
3. **Repeat contributor** — 同じ手順を別Issueでも再現できる。

## 4. Progress tracking

各LessonまたはIssue調査では、次の状態だけを使用します。

- `Not started`
- `In progress`
- `Blocked`（理由と解除条件を記録）
- `Completed`（完了条件と検証結果を記録）

READMEには現在地だけを表示し、詳細な学習記録は各Lessonまたはnoteへ残します。
ロードマップを変更した場合は、変更理由をコミットメッセージまたはPR本文に残します。

## 5. Planned repository structure

必要になった時点で段階的に作成します。

```text
pytorch-learning-lab/
├─ README.md
├─ ROADMAP.md
├─ requirements.txt
├─ 01_tensor_basics.py
├─ 02_tensor_operations.py
├─ ...
├─ 07_pytorch_internals/
├─ 08_testing/
├─ 09_source_reading/
├─ 10_oss_practice/
│  ├─ issue_analysis/
│  ├─ reproductions/
│  └─ notes/
└─ tests/
```

空のディレクトリや未着手Lessonは先に作らず、学習成果ができた時点で追加します。

## 6. Immediate next step

Phase 0の計画コミット後、`01_tensor_basics.py`を新しいコミットで作成します。
Lesson 01ではTensor生成、shape、dtype、deviceだけに集中し、理解確認後に演算へ進みます。

## 7. Official references

Contributionルールは変化するため、実際のIssue選定・PR提出時に必ず再確認します。

- [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html)
- [PyTorch repository](https://github.com/pytorch/pytorch)
- [The Ultimate Guide to PyTorch Contributions](https://github.com/pytorch/pytorch/wiki/The-Ultimate-Guide-to-PyTorch-Contributions)
- [PyTorch CONTRIBUTING.md](https://github.com/pytorch/pytorch/blob/main/CONTRIBUTING.md)
- [PyTorch contribution opportunities](https://github.com/pytorch/pytorch/contribute)
