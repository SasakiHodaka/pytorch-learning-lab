# Learning Progress

実行回数ではなく、コードを読解・変更・実装できる度合いを記録します。

## Scale

- `0`: 未理解または未着手
- `1`: 補助があれば説明できる
- `2`: 自力で読解し、小さな変更を検証できる
- `3`: edge caseを発見し、テストと実装を追加できる

Lesson完了はLevel 2以上です。各行のEvidenceには、説明ノート、テスト、コミットなど
第三者が確認できる根拠を記入します。

## Progress table

| Chapter | Read | Change | Build | Evidence | Status |
| --- | ---: | ---: | ---: | --- | --- |
| 00 Python Foundations | 0 | 0 | 0 | — | Not started |
| 01 Tensor Fundamentals | 0 | 0 | 0 | — | Not started |
| 02 Autograd and Optimization | 0 | 0 | 0 | — | Not started |
| 03 Neural Networks | 0 | 0 | 0 | — | Not started |
| 04 Data and Training | 0 | 0 | 0 | — | Not started |
| 05 Engineering Practice | 0 | 0 | 0 | — | Not started |
| 06 Advanced Development | 0 | 0 | 0 | — | Not started |
| 07 Internals and OSS | 0 | 0 | 0 | — | Not started |

## Session log template

```markdown
### YYYY-MM-DD — Lesson

- Reading target:
- Responsibility:
- Input/output/data flow:
- Contract inferred from tests:
- Change prediction:
- Observed result:
- Implementation decision:
- Remaining question:
- Verification command:
- Commit:
```

## Program completion

- [ ] 初見のPython関数を、呼び出し元とテストを含めて説明できる。
- [ ] 初見のPyTorchコードで、主要Tensorのshapeを追跡できる。
- [ ] failureから原因仮説を立て、調査範囲を絞れる。
- [ ] 既存設計を保ちながら、小さな機能変更とテストを追加できる。
- [ ] 複数moduleからなる学習pipelineを読解・変更できる。
- [ ] PyTorch本体のAPIから実装と公式テストを探せる。
- [ ] 最小再現、回帰テスト、修正を含むPRを準備できる。
