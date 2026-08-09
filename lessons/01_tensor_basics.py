"""Lesson 01: Tensorの基本情報を確認する。

リポジトリのルートで次のコマンドを実行します。

    python lessons/01_tensor_basics.py
"""

# PyTorchの機能を、このファイルで使えるようにします。
import torch


# 1. 3個の数値を持つ、1次元のTensorを作ります。
numbers = torch.tensor([1.0, 2.0, 3.0])

# 2. Tensorそのものを表示します。
print("Tensor:")
print(numbers)

# 3. shapeは、Tensorが各方向にいくつの要素を持つかを表します。
print("\nShape:")
print(numbers.shape)

# 4. dtypeは、Tensorの数値を保存するデータ型です。
print("\nData type:")
print(numbers.dtype)

# 5. deviceは、Tensorがどの計算装置に置かれているかを表します。
print("\nDevice:")
print(numbers.device)
