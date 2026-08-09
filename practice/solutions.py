"""Reference solutions for practice/exercises.py."""

import torch
from torch import nn


def python_mean(values: list[float]) -> float:
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def normalize_rows(values: torch.Tensor) -> torch.Tensor:
    if values.ndim != 2:
        raise ValueError("values must be a 2D tensor")
    row_sums = values.sum(dim=1, keepdim=True)
    if torch.any(row_sums == 0):
        raise ValueError("every row sum must be non-zero")
    return values / row_sums


def squared_error_gradient(weight: float, x: float, target: float) -> float:
    weight_tensor = torch.tensor(weight, requires_grad=True)
    prediction = weight_tensor * x
    loss = (prediction - target) ** 2
    loss.backward()
    return weight_tensor.grad.item()


def make_classifier(input_features: int, hidden_features: int, classes: int) -> nn.Module:
    return nn.Sequential(
        nn.Linear(input_features, hidden_features),
        nn.ReLU(),
        nn.Linear(hidden_features, classes),
    )


def classification_accuracy(logits: torch.Tensor, targets: torch.Tensor) -> float:
    if logits.ndim != 2:
        raise ValueError("logits must have shape [samples, classes]")
    if targets.ndim != 1 or len(logits) != len(targets):
        raise ValueError("targets must have shape [samples]")
    predictions = logits.argmax(dim=1)
    return (predictions == targets).float().mean().item()
