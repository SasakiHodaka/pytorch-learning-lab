# Chapter 06: Advanced Development

ここまでの部品を実案件に近い判断へつなげます。画像batchを扱うCNN、train/validation
分割、学習率調整、gradient clippingを学び、最後にcapstone projectを実行します。

## Lessons

1. `01_convolutional_network.py` — image shapeとCNN
2. `02_validation_and_metrics.py` — validationとconfusion matrix
3. `03_training_controls.py` — schedulerとgradient clipping
4. [`../../mini_project/`](../../mini_project/) — 分割されたtraining application

## Completion criteria

- `[batch, channel, height, width]`を各CNN層で追跡できる。
- training dataとvalidation dataを分ける理由を説明できる。
- accuracyだけでは見えないclass別の誤りを確認できる。
- scheduler、gradient clipping、checkpointを目的に応じて使える。
- model、data、engine、CLI、testを分離したprojectを変更できる。
