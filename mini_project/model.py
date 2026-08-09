"""Model definition for the capstone project."""

import torch
from torch import nn


class Classifier(nn.Module):
    def __init__(self, hidden_features: int, classes: int = 2) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, hidden_features),
            nn.ReLU(),
            nn.Linear(hidden_features, classes),
        )

    def forward(self, features: torch.Tensor) -> torch.Tensor:
        if features.ndim != 2 or features.shape[1] != 2:
            raise ValueError(f"expected shape [batch, 2], got {tuple(features.shape)}")
        return self.network(features)
