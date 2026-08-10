# Chapter 03: Neural Networks

`nn.Module`はparameterと計算をまとめるPyTorchモデルの基本単位です。この章では
層、活性化関数、lossを分解して理解した後、小さな分類器を作ります。

## Lessons

1. `01_module_and_parameters.py` — Module、forward、Parameter
2. `02_activation_and_loss.py` — ReLU、logits、CrossEntropyLoss
3. `03_binary_classifier.py` — 非線形な分類モデル

## Reading missions

- `__init__`で登録されたmoduleとparameterを列挙する。
- `forward`を通るTensorのshapeを層ごとに追跡する。
- logits、target、loss、predictionが作られる行を特定する。
- modelの呼び出しが`forward`へつながることを説明する。

## Change missions

- hidden sizeを変更し、影響するweightと出力shapeを予測する。
- 活性化関数を変更し、変わる処理と変わらないAPIを区別する。
- 入力feature数を誤らせ、エラーの発生箇所と原因を説明する。

## Build mission

`practice.make_classifier`を実装します。テストから必要な入力shapeと出力shapeを読み、
`Linear -> ReLU -> Linear`の各層の責務を説明します。

## Completion criteria

- 初見の`nn.Module`の構造とforwardデータフローを説明できる。
- logits、確率、prediction、target、lossをコード上で区別できる。
- architecture変更の影響をparameterとshapeで追跡できる。
- 既存のshape契約を満たすmodelを実装できる。
