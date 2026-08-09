# Chapter 04: Data and Training

実際の開発では、データ準備、mini-batch学習、評価、checkpoint保存を分離します。
この章では再利用できる関数としてtraining pipelineを組み立てます。

## Lessons

1. `01_dataset_and_dataloader.py` — Dataset、shuffle、batch
2. `02_train_and_evaluate.py` — train/eval loopとmetric
3. `03_save_and_load.py` — state_dictとcheckpoint
4. `04_reproducibility_and_device.py` — seedとdevice

## Completion criteria

- sample、feature、target、batchを区別できる。
- trainingとevaluationで処理が異なる理由を説明できる。
- checkpointを読み込み、同じ予測を再現できる。
- seedを固定しても完全な再現が難しい場合を理解する。
