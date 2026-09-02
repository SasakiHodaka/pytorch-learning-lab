# Resume here

最終更新: 2026-09-02

PCやCodexからログアウトした後は、PowerShellで次を実行する。

```powershell
cd C:\Users\sasakihodaka\pytorch-learning-lab
git status
git log -2 --oneline
```

## Current state

- 学習・調査記録はGitへコミット済み。
- PyTorchのclean開発worktreeは`C:\Users\sasakihodaka\pytorch-dev`。
- branchは`env-prep`、基点は`580b06aeb5aa20cb5b78e79751c7467e7a845d94`。
- Python 3.12.7 venv、開発dependency、MKL、Visual C++、全submoduleを準備済み。
- CPU-only初回buildは580個のobjectと複数のlibraryを生成したところで時間上限により中断。
- build成果物は`pytorch-dev\build`に残っているため、最初からやり直さない。
- `C:\Users\sasakihodaka\pytorch`の`issue-195165-contextvar`には未コミットの学習用patchがある。
- Issue #195165は他Contributorと競合するため、そのpatchを本家へ提出しない。

## First action

初回buildを差分から再開する。

```powershell
cd C:\Users\sasakihodaka\pytorch-learning-lab
powershell -ExecutionPolicy Bypass -File tools\build_pytorch_cpu.ps1
powershell -ExecutionPolicy Bypass -File tools\verify_pytorch_dev.ps1
```

`build_pytorch_cpu.ps1`がVisual C++とCPU-only用の一時環境変数を毎回設定するため、
PowerShellを閉じた後も手動で環境変数を復元する必要はない。

## After the build passes

```powershell
powershell -ExecutionPolicy Bypass -File tools\audit_pytorch_issues.ps1 -MaxIssues 25
```

Open PR、assignee、作業宣言のないCPUで再現可能なIssueだけを候補にする。
Issueコメント、fork作成、PR作成などGitHubを書き換える操作は、内容を本人が確認してから行う。

## GitHub authentication

認証状態を確認する。

```powershell
gh auth status
```

無効なら、tokenをファイルへ記録せず次で再認証する。

```powershell
gh auth login -h github.com -p https -w
```

認証後、保存済みcommitをGitHubにも退避する。

```powershell
git push origin main
```
