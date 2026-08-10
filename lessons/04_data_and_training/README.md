# Chapter 04: Data and Training

実際の開発では、データ準備、mini-batch学習、評価、checkpoint保存を分離します。
この章では再利用できる関数としてtraining pipelineを組み立てます。

## Lessons

1. `01_dataset_and_dataloader.py` — Dataset、shuffle、batch
2. `02_train_and_evaluate.py` — train/eval loopとmetric
3. `03_save_and_load.py` — state_dictとcheckpoint
4. `04_reproducibility_and_device.py` — seedとdevice

## Reading missions

- DatasetからDataLoader、model、loss、metricまでデータの流れを追跡する。
- sampleとbatchでfeature・targetのshapeがどう変わるか説明する。
- trainingとevaluationの共通処理と異なる処理を分類する。
- checkpointへ保存される状態と、保存されない実行時状態を区別する。

## Change missions

- batch sizeを変更し、iteration数とTensor shapeへの影響を予測する。
- evaluationから`inference_mode`を外し、変わる状態を調べる。
- checkpoint項目を一つ追加し、保存・復元の両方を変更する。

## Build mission

`practice.classification_accuracy`を実装します。logitsからpredictionを得る軸と、batch単位の
正解率へ集約する処理をテストから読み取ります。

## Completion criteria

- 複数関数にまたがるtraining pipelineのデータフローを説明できる。
- trainingとevaluationの状態変更をコード上で特定できる。
- 設定変更がiteration、shape、保存状態へ与える影響を検証できる。
- metric関数を既存のTensor契約に合わせて実装できる。
