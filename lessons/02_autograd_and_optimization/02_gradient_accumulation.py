"""Gradients accumulate until they are cleared."""

import torch

weight = torch.tensor(2.0, requires_grad=True)

first_loss = weight**2
first_loss.backward()
print(f"after first backward: {weight.grad.item()}")

second_loss = weight**2
second_loss.backward()
print(f"after second backward: {weight.grad.item()}")
assert weight.grad.item() == 8.0

weight.grad.zero_()
third_loss = weight**2
third_loss.backward()
print(f"after zero and backward: {weight.grad.item()}")
assert weight.grad.item() == 4.0
