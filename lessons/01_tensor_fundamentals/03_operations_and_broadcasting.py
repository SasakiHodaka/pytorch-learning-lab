"""Compare element-wise operations, matrix multiplication, and broadcasting."""

import torch

x = torch.tensor([1.0, 2.0, 3.0])
y = torch.tensor([10.0, 20.0, 30.0])
print(f"addition: {x + y}")
print(f"element-wise multiplication: {x * y}")

left = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
right = torch.tensor([[5.0, 6.0], [7.0, 8.0]])
matrix_product = left @ right
print(f"matrix multiplication:\n{matrix_product}")

# A shape (3,) vector is reused for every row of the (2, 3) matrix.
batch = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
bias = torch.tensor([0.1, 0.2, 0.3])
broadcast_result = batch + bias
print(f"broadcast result:\n{broadcast_result}")

assert torch.equal(x * y, torch.tensor([10.0, 40.0, 90.0]))
assert torch.equal(matrix_product, torch.tensor([[19.0, 22.0], [43.0, 50.0]]))
assert broadcast_result.shape == batch.shape
