# Education Program

この教材は、既存コードを読んで意図と影響範囲を判断できる力を最優先にし、次に安全に
変更する力、最後に白紙から実装する力を育てます。暗記や写経ではなく、根拠を示して
コードを説明・変更できることを目標にします。

## Priority

```text
読む（50%） → 変更する（30%） → 書く（20%）
```

- **読む**: 目的、入力、出力、データフロー、分岐、例外、外部作用を追跡する。
- **変更する**: 影響を予測し、一度に一つだけ変更してテストする。
- **書く**: 要求を分解し、テスト可能な小さな処理として実装する。

比率は初期の目安です。後半では読解対象が大きくなり、変更と実装の難度も上がります。

## Five-pass lesson protocol

すべてのLessonを次の5段階で進めます。

### 1. Survey

実行前に、ファイル名、import、定義、呼び出し、assertを確認します。まだ細部へ入りません。

成果物: 「このファイルは何をするか」を2〜3文で説明する。

### 2. Trace

重要な変数について、入力から出力まで値・型・shapeの変化を追います。分岐、loop、例外、
状態変更には印を付けます。

成果物: 主要なデータフローを箇条書きまたは図で示す。

### 3. Contract

docstring、型ヒント、呼び出し元、テストから、コードが守るべき仕様を抽出します。

成果物: 正常系、境界値、異常系をそれぞれ最低1つ挙げる。

### 4. Change

値、条件、shape、関数のいずれか一つだけを変更します。変更前に影響を予想し、実行または
テストで確かめます。

成果物: 「予想、結果、差が出た理由」を記録する。

### 5. Build

最後に、同じ概念を使う小さな関数またはテストを自分で実装します。模範解答は成功後に
比較対象としてのみ使用します。

成果物: 実装、テスト、判断理由を含む小さなコミット。

## Curriculum

| Chapter | 読解対象 | 変更・実装の中心 |
| --- | --- | --- |
| [`00_python_foundations`](00_python_foundations/) | Pythonの値、制御、関数、データ構造 | 小さな関数と例外処理 |
| [`01_tensor_fundamentals`](01_tensor_fundamentals/) | Tensorの型・shape・演算 | shapeを保つ変換処理 |
| [`02_autograd_and_optimization`](02_autograd_and_optimization/) | 計算グラフと学習更新 | 勾配計算と線形回帰 |
| [`03_neural_networks`](03_neural_networks/) | `nn.Module`とforward | 小さな分類器 |
| [`04_data_and_training`](04_data_and_training/) | 学習pipelineのデータフロー | 評価・保存可能な学習loop |
| [`05_engineering_practice`](05_engineering_practice/) | テストとfailure | 境界検証とdebug |
| [`06_advanced_development`](06_advanced_development/) | 複数moduleの関係 | mini projectの仕様変更 |
| [`07_internals_and_oss`](07_internals_and_oss/) | PyTorch本体の実装とテスト | 最小再現・回帰テスト・PR準備 |

## Reading questions

コードを読むたびに、次へ答えます。

1. このコードの責務は何か。
2. 入力と出力の型・shape・意味は何か。
3. データはどこから来て、どこへ渡るか。
4. どの条件で処理経路が変わるか。
5. 失敗するとしたら、どの入力と行が候補か。
6. テストは何を保証し、何を保証していないか。
7. 一行変えた場合、影響はどこまで伝わるか。

## Evaluation rubric

各Lessonを0〜3で自己評価します。

| Level | 判定 |
| --- | --- |
| 0 | 説明を読んでも処理を追えない |
| 1 | 補助があれば出力と処理を説明できる |
| 2 | 自力で仕様を説明し、小さな変更を検証できる |
| 3 | edge caseを発見し、テストと実装を追加できる |

Level 2をLesson完了の基準とし、重要LessonはLevel 3を目指します。

## Git workflow

```powershell
git switch -c lesson/00-python-mean
git diff
python -m unittest tests.test_exercises -v
git add <学習したファイルだけ>
git commit -m "lesson: implement Python mean exercise"
```

一つのコミットには、一つの学習上の判断だけを含めます。
