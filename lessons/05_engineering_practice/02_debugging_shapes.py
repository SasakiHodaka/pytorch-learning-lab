"""Validate inputs close to the public boundary."""

import torch
from torch import nn


class SafeClassifier(nn.Module):
    def __init__(self, input_features: int, classes: int) -> None:
        super().__init__()
        self.input_features = input_features
        self.linear = nn.Linear(input_features, classes)

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        if inputs.ndim != 2:
            raise ValueError(f"expected [batch, features], got shape {tuple(inputs.shape)}")
        if inputs.shape[1] != self.input_features:
            raise ValueError(
                f"expected {self.input_features} features, got {inputs.shape[1]}"
            )
        return self.linear(inputs)


model = SafeClassifier(input_features=3, classes=2)
valid = torch.ones(4, 3)
print(model(valid).shape)

try:
    model(torch.ones(4, 5))
except ValueError as error:
    print(f"helpful error: {error}")

assert model(valid).shape == (4, 2)
