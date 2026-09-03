# PyTorch Contribution Sprint

長期カリキュラムを順番に消化せず、短い周期で学習と本家調査を往復する。

## One-cycle workflow

```text
演習を1つ実装
  → テスト・lintを通す
  → 関連するPyTorch本体の実装とテストを読む
  → Openかつ競合のないactionable Issueを確認
  → 回帰テストと最小修正を作る
  → 自分で全変更を説明してからPRを出す
```

## 2026-09-02 sprint

- [x] `practice/exercises.py` のChapter 00–04演習を実装
- [x] 学習Repoの12 tests、Ruff、mypyを通過
- [x] 29 Lessonを一括実行
- [x] PyTorch本体を浅いcloneとして `C:\Users\sasakihodaka\pytorch` に取得
- [x] 最新のContributionルールを確認
- [x] `good first issue` のOpen状態と競合を確認
- [x] Issue #195165の`ContextVarVariable`をローカルで試作
- [x] Ruffとdiff検査を通過
- [x] GitHub CLIを`SasakiHodaka`として認証
- [x] `actionable` / `good first issue` / `better-engineering`を横断調査
- [x] 各候補のIssueコメントとOpen/Closed PRを確認
- [x] PyTorch本体のCPU-onlyビルド環境を構築
- [x] clean worktree、専用venv、開発dependency、MKL、全submoduleを準備
- [x] CPU-only初回buildを差分から完走
- [x] source checkoutのimportとCPU Tensor smoke testを実行
- [ ] 選定したIssueの本家対象テストを実行
- [ ] 未競合のactionable Issueを確保
- [ ] 回帰テスト付きのPRを提出

## Current constraints

- CPU-only初回buildとeditable installは完了。8並列で完走し、CPU Tensor smoke testも成功。
- GitHub CLIは`SasakiHodaka`として再認証済み。
- Issue #195165の`ContextVarVariable`は別Contributorが取得済み。試作を提出しない。
- 調査した有望候補には既存のOpen PRまたは作業宣言があり、重複PRを避けた。

## Next burst

1. 新着の`actionable` / `good first issue`を確認し、コメントと関連PRを先に調べる。
2. timelineにOpen PRがなくても、コメント内のPR番号と現行mainでの再現結果を確認する。
3. 競合がなければ、本人確認後にIssueへ対象を明記する。
4. 最小修正、対象テスト、Spin lint、self-reviewまで一気に実施する。

## Candidate audit on 2026-09-02

- `#195165`: 小項目は他Contributorが取得済み。
- `#194869`: 修正と回帰テストがmerge-bot経由で最新mainへ反映済み。
- `#194344`, `#193823`, `#192719`, `#191787`: Open PRあり。
- `#170798`, `#174177`, `#174183`, `#185647`: Open PRあり。
- `#188398`, `#158895`, `#116203`, `#177265`: Open PRあり。
- `#183036`: 最新mainの共有docstringは既に特定Optimizerに依存しない例へ更新済み。

## Candidate audit on 2026-09-03

- 最新100件の`actionable`と最新25件の`good first issue`を監査。
- `#174984`, `#155981`, `#166853`, `#155671`: コメント内に既存修正PRあり。
- `#159740`: 現行checkoutは既に専用のpinned-memoryエラーを返す。
- `#153327`: 現行checkoutは巨大な`upscale_factor`をoverflowとして検出済み。
- `#157547`, `#156075`, `#154226`, `#154077`: assignee、既存PR、作業宣言、または仕様議論あり。
- timelineにOpen PRがないだけでは未競合と断定できないため、コメントと再現確認を必須とする。
- 今回は重複なしの小規模なCPU候補を確保できなかった。
