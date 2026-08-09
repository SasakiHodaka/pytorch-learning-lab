"""Define an nn.Module and inspect its parameters."""

import torch
from torch import nn


class TinyRegressor(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.linear = nn.Linear(in_features=2, out_features=1)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.linear(inputs)


torch.manual_seed(0)
model = TinyRegressor()
inputs = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
outputs = model(inputs)  # Call the module; do not call forward directly.

print(model)
print(outputs)
for name, parameter in model.named_parameters():
    print(f"{name}: shape={parameter.shape}, requires_grad={parameter.requires_grad}")

assert outputs.shape == (2, 1)
assert model.linear.weight.shape == (1, 2)
assert model.linear.bias.shape == (1,)
