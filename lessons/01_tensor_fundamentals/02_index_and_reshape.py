"""Select values and change the way a tensor is viewed."""

import torch

values = torch.arange(12).reshape(3, 4)
print(values)
print(f"first row: {values[0]}")
print(f"last column: {values[:, -1]}")
print(f"small block:\n{values[:2, 1:3]}")

flat = values.reshape(-1)
three_dimensions = values.reshape(2, 2, 3)
transposed = values.T

print(f"flat shape: {flat.shape}")
print(f"3D shape: {three_dimensions.shape}")
print(f"transposed shape: {transposed.shape}")

assert values[1, 2].item() == 6
assert flat.shape == (12,)
assert three_dimensions.numel() == values.numel()
assert transposed.shape == (4, 3)
