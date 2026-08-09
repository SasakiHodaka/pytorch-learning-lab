"""Create tensors and inspect their metadata."""

import torch

scalar = torch.tensor(7)
vector = torch.tensor([1.0, 2.0, 3.0])
matrix = torch.tensor([[1, 2, 3], [4, 5, 6]])

for name, value in [("scalar", scalar), ("vector", vector), ("matrix", matrix)]:
    print(f"\n{name}:\n{value}")
    print(f"shape={value.shape}, ndim={value.ndim}")
    print(f"dtype={value.dtype}, device={value.device}")

zeros = torch.zeros((2, 3))
ones = torch.ones((2, 3))
random_values = torch.rand((2, 3), generator=torch.Generator().manual_seed(0))

print(zeros)
print(ones)
print(random_values)

assert scalar.shape == torch.Size([])
assert vector.shape == (3,)
assert matrix.shape == (2, 3)
assert matrix.dtype == torch.int64
