# PyTorch Learning Lab

PyTorchを基礎から内部実装まで体系的に学び、最終的に
[`pytorch/pytorch`](https://github.com/pytorch/pytorch) 本体へコードとテストを
貢献することを目標にした実践リポジトリです。

## Mission

```text
PyTorchを使う
  ↓
動作原理と内部実装を理解する
  ↓
テストとIssue調査を身につける
  ↓
PyTorch本体へ修正と回帰テストを提出する
  ↓
レビュー対応を経てMergeを目指す
```

「学習」と「OSS貢献」を別々に扱いません。学んだAPIについて、動作を実験し、
テストを書き、公式実装を読むところまでを一つの学習単位とします。

## Current status

| 項目 | 状態 |
| --- | --- |
| リポジトリ作成 | 完了 |
| CPU版PyTorch環境定義 | 完了 |
| 学習・貢献ロードマップ | 完了 |
| 完成版カリキュラム | 完了 |
| 学習開始地点 | Chapter 00: Python Foundations |
| PyTorch本体への貢献 | 未着手 |

詳細なフェーズ、成果物、完了条件は[ROADMAP.md](ROADMAP.md)を参照してください。

教材コードは[`lessons/`](lessons/)にあります。Python未経験者は
[`lessons/00_python_foundations/`](lessons/00_python_foundations/)から始めます。
練習問題と模範解答は[`practice/`](practice/)、理解度は
[`PROGRESS.md`](PROGRESS.md)で確認できます。

完成済み教材の一括検証:

```powershell
python tools/run_all_lessons.py
python -m unittest tests/test_solutions.py -v
```

## Repository policy

- Lessonは番号順に追加し、一つのテーマに集中させる。
- 各Lessonに「目的」「実験」「確認問題」「完了条件」を持たせる。
- 学んだ機能は、可能な範囲で公式実装と公式テストまで追跡する。
- 実装変更にはテストを添え、変更理由をコミットメッセージに残す。
- 生成物、仮想環境、個人情報、認証情報はコミットしない。
- PyTorch本体へのIssueやPRは、公式の最新ルールを提出直前に再確認する。

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Official resources

- [PyTorch documentation](https://docs.pytorch.org/docs/stable/index.html)
- [PyTorch repository](https://github.com/pytorch/pytorch)
- [PyTorch Contributor Guide](https://github.com/pytorch/pytorch/wiki/The-Ultimate-Guide-to-PyTorch-Contributions)
- [PyTorch CONTRIBUTING.md](https://github.com/pytorch/pytorch/blob/main/CONTRIBUTING.md)
- [PyTorch contribution opportunities](https://github.com/pytorch/pytorch/contribute)
