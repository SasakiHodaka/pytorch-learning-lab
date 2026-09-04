# Resume here

最終更新: 2026-09-04

PCやCodexからログアウトした後は、PowerShellで次を実行する。

```powershell
cd C:\Users\sasakihodaka\pytorch-learning-lab
git status
git log -2 --oneline
```

## Current state

- 学習・調査記録はGitへコミット済み。
- PyTorchのclean開発worktreeは`C:\Users\sasakihodaka\pytorch-dev`。
- branchは`env-prep`、基点は`b45272bf18dd1448d0f7d4a351ec96c0e1f7ed90`。
- Python 3.12.7 venv、開発dependency、MKL、Visual C++、全submoduleを準備済み。
- CPU-only buildとeditable installが完了済み。
- `torch 2.15.0a0+gitb45272b`のimportとCPU Tensor演算を確認済み。
- 2026-09-04に`actionable`と`good first issue`の新着25件ずつを再監査済み。小規模なCPU候補は既存PRまたは作業宣言と競合していた。
- `C:\Users\sasakihodaka\pytorch`の`issue-195165-contextvar`には未コミットの学習用patchがある。
- Issue #195165は他Contributorと競合するため、そのpatchを本家へ提出しない。

## First action

新着Issueを再監査する。

```powershell
cd C:\Users\sasakihodaka\pytorch-learning-lab
powershell -ExecutionPolicy Bypass -File tools\audit_pytorch_issues.ps1 -MaxIssues 25
powershell -ExecutionPolicy Bypass -File tools\audit_pytorch_issues.ps1 -MaxIssues 25 -Label "good first issue"
```

Open PR、assignee、作業宣言のないCPUで再現可能なIssueだけを候補にする。
Issueコメント、fork作成、PR作成などGitHubを書き換える操作は、内容を本人が確認してから行う。

## GitHub authentication

認証状態を確認する。

```powershell
gh auth status
```

現在は`SasakiHodaka`として認証済み。無効になった場合は、tokenをファイルへ記録せず次で再認証する。

```powershell
gh auth login -h github.com -p https -w
```

認証後、保存済みcommitをGitHubにも退避する。

```powershell
git push origin main
```
