# Practice

本編を読んだ後、`exercises.py`の`TODO`を自分で実装します。最初は
`solutions.py`を見ずに考え、20〜30分試しても進めない場合だけ、対応する関数を
一つずつ確認してください。

## Workflow

1. `practice/exercises.py`の対象関数を実装する。
2. `python -m unittest tests/test_exercises.py -v`を実行する。
3. failure messageを読み、期待値と実際の値を比べる。
4. 全テスト成功後に`practice/solutions.py`と比較する。
5. 実装の違いを「正誤」だけでなく、読みやすさとedge caseで評価する。

`tests/test_exercises.py`は最初は失敗します。それが正常です。練習を開始するまでは、
完成教材全体の確認には`tests/test_solutions.py`を使います。
