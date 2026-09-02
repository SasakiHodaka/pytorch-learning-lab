# Issue investigation: pytorch/pytorch#195165

## Decision

`ContextVarVariable`の移行は学習用patchとして保持するが、PRにはしない。
別Contributorが2026-08-28に取得を明言しており、競合するため。

## Facts

- IssueはOpen。
- Labels: `good first issue`, `OSS contribution wanted`, `llm-amenable`, `triaged`。
- 目的は`VariableTracker.call_method`の分岐を宣言的な`tp_methods`へ移すこと。
- 最新mainでは`AutogradEngineVariable`と`OptimizerVariable`はすでに移行済み。
- `ContextVarVariable`には`get`, `set`, `reset`のimperative dispatchが残っていた。
- `test/dynamo/test_contextvars.py`に既存の正常系・引数エラー・graph breakテストがある。

## Local experiment

- Repository: `C:\Users\sasakihodaka\pytorch`
- Branch: `issue-195165-contextvar`
- Changed file: `torch/_dynamo/variables/misc.py`
- Change: `get`, `set`, `reset`を`tp_methods`に登録する試作

## Verification

Succeeded:

```powershell
python -m ruff check torch\_dynamo\variables\misc.py
git diff --check
```

Not yet runnable:

```powershell
python test\dynamo\test_contextvars.py -v
```

浅いsource checkoutが未ビルドのため、生成される`torch/version.py`がなくimport時に停止した。
したがって、このpatchをPR-readyとは判定しない。

## Learning

- IssueがOpenでも、コメントで作業宣言されていれば競合を避ける。
- Issue本文のチェックリストより最新mainが先に進んでいる場合がある。
- lint成功だけでは実行時の互換性を証明できない。
- PyTorchの`Method`はCPythonの`ml_flags`から引数規約を導出する。
