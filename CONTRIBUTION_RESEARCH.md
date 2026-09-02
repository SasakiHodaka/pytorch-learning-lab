# PyTorch Contribution Research

調査日: 2026-09-02

## Mandatory contribution rules

PyTorch本体の`AGENTS.md`は`CLAUDE.md`を参照し、さらに`AI_POLICY.md`の遵守を必須としている。

- AIはGitHub上でIssue、PR、コメントを自律的に投稿しない。
- 投稿文面は、ユーザーが正確な内容を事前に確認・承認する。
- AI生成文は引用またはcode block内へ入れ、本人の説明を添える。
- AIが支援したコードは、本人が読んで理解してから提出する。
- 未完成または未確認のPRはDraftにする。
- PyTorch本体の一時ファイルは`agent_space/`だけに置く。
- lintはSpin経由で実行する。
- buildは`python -m pip install --no-build-isolation -v -e .`だけを使う。
- commitは本人が明示的に依頼した場合だけ作成する。

## Local repository state

- PyTorch source: `C:\Users\sasakihodaka\pytorch`
- Clone: shallow, blob filter enabled
- Current remote: upstreamの`pytorch/pytorch`だけ
- `origin/main`: 2026-09-02時点のGitHub mainへfetch済み
- Current branch: `issue-195165-contextvar`
- Local experiment: `torch/_dynamo/variables/misc.py`に未提出の変更あり
- Submodules: 未取得
- GitHub CLI: `SasakiHodaka`として認証済み
- GitHub fork: `SasakiHodaka/pytorch`は未作成

`ContextVarVariable`の変更は別Contributorと競合するため提出しない。学習用patchとしてのみ扱う。

## Windows environment audit

| Item | Result |
| --- | --- |
| OS | Windows / PowerShell |
| CPU | Intel Core i7-1165G7, 4 cores / 8 logical processors |
| RAM | 約16 GB |
| Free disk | 約85 GB（全submodule取得後） |
| Visual Studio | 2022 Community + C++ toolchain detected |
| Python | system 3.12.7; existing `.venv310` is 3.10.11 |
| Installed PyTorch | system 2.8.0 CPU; `.venv310` 2.9.1 CPU |
| Clean development worktree | `C:\Users\sasakihodaka\pytorch-dev`, branch `env-prep` |
| PyTorch venv | `pytorch-dev\.venv`, Python 3.12.7 |
| Build tools | CMake 4.4.3, Ninja 1.13.2 |
| Contributor tools | Spin 0.18, Lintrunner 0.13.1 |
| CPU math dependencies | MKL static/include 2024.2.0 + Intel OpenMP/TBB |
| Submodules | 53 recursive submodules initialized and commit-verified |

公式README上、source buildにはPython 3.10以上、C++20対応compiler、Visual Studio、10 GB以上、
初回30–60分が必要。現在のマシンではCPU-onlyかつ低並列が現実的。

CPU-only build設定は次のとおり。Visual Studioのローカライズ情報で
`Launch-VsDevShell.ps1`が失敗するため、`vcvars64.bat`の出力をPowerShellへ取り込む。

```powershell
$env:USE_CUDA = '0'
$env:USE_DISTRIBUTED = '0'
$env:USE_FLASH_ATTENTION = '0'
$env:USE_MEM_EFF_ATTENTION = '0'
$env:MAX_JOBS = '2'
python -m pip install --no-build-isolation -v -e .
```

初回buildはCMake configureとMSVC compileまで到達し、対話セッションの時間上限で安全に中断した。
`build`成果物は保持されており、次の公式editable-installを再実行すると差分から再開する。

```powershell
powershell -ExecutionPolicy Bypass -File tools\build_pytorch_cpu.ps1
powershell -ExecutionPolicy Bypass -File tools\verify_pytorch_dev.ps1
```

既定の`MAX_JOBS=2`は4 core / 約16 GBの端末でメモリと操作性を守るため。初回完了後の変更は
差分buildになる。検証scriptはimport元、version、CUDA無効、CPU Tensor演算を確認する。

`pyproject.toml`はWindowsでNinja generatorとMSVC `cl`を指定する。開発dependency groupには
SpinとCMakeが含まれ、CI pinはNinja 1.13.0、Lintrunner 0.13.0、Spin 0.17、CMake 3.31.6。

## Issue audit findings

IssueがOpenでも、次のいずれかなら新規PR候補から除外する。

1. コメントで別Contributorが作業を宣言している。
2. TimelineにOpen PRのcross-referenceがある。
3. 最新mainですでに修正されている。
4. Tracking Issueまたは`needs design`で、独立した受入条件がない。
5. 手元のCPU/Windows環境では再現・検証できない。

2026-09-02の監査では、最近のactionable 25件についてOpen PRなしは3件だけだった。

- `#194869`: merge-bot経由の修正と回帰テストが最新mainに存在する。
- `#191236`: staged rolloutのTracking Issue。
- `#183036`: 最新mainのdocstringはすでに特定Optimizerへ依存しない例になっている。

`better-engineering`群も22件監査した。候補に見えたものの判断は次のとおり。

- `#115614`: 2026-08-21に別Contributorが作業宣言。
- `#157547`: assigneeあり、`needs design`あり。
- `#151579`: 別Contributorが作業宣言。
- `#114935`: 最新mainでは対象fileの`print()`が0件。

## Read-only monitoring

[`tools/audit_pytorch_issues.ps1`](tools/audit_pytorch_issues.ps1)は、最新actionable Issueを取得し、
TimelineにあるOpen PRを照合する。GitHubへ書き込みは行わない。

```powershell
powershell -ExecutionPolicy Bypass -File tools\audit_pytorch_issues.ps1 -MaxIssues 25
```

優先する候補:

- `actionable`かつtriaged
- assigneeなし
- 作業宣言なし
- Open PR cross-referenceなし
- CPUで最小再現可能
- Pythonまたは限定的なC++変更
- 既存の対象テストが明確

## Ready-to-start procedure

1. 監査scriptで候補を抽出する。
2. Issue本文、全コメント、Timeline、関連するOpen/Closed PRを読む。
3. 最新mainで再現するか確認する。
4. APIから実装と既存テストを追跡する。
5. 事実、仮説、未確認事項、受入条件を記録する。
6. 投稿が必要なら、正確な文面を本人が確認してから実行する。
7. 本人が変更を理解できる小さなpatchと回帰テストを作る。
8. 対象テスト、関連テスト、Spin lintを実行する。
9. diffを本人が全行確認する。
10. 未完成ならDraft PR、完成済みなら通常PRの文面を本人が承認する。
