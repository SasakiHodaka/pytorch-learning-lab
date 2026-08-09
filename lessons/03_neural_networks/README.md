# Chapter 03: Neural Networks

`nn.Module`はparameterと計算をまとめるPyTorchモデルの基本単位です。この章では
層、活性化関数、lossを分解して理解した後、小さな分類器を作ります。

## Lessons

1. `01_module_and_parameters.py` — Module、forward、Parameter
2. `02_activation_and_loss.py` — ReLU、logits、CrossEntropyLoss
3. `03_binary_classifier.py` — 非線形な分類モデル

## Completion criteria

- `__init__`と`forward`の役割を説明できる。
- logitsと確率、predictionを区別できる。
- modelのparameterを列挙し、shapeを説明できる。
