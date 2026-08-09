"""Exercises: replace each NotImplementedError without changing the function API."""

import torch
from torch import nn


def python_mean(values: list[float]) -> float:
    """Return the mean and reject an empty list with ValueError."""
    raise NotImplementedError("TODO: Chapter 00")


def normalize_rows(values: torch.Tensor) -> torch.Tensor:
    """Divide every row by its sum while preserving the input shape."""
    raise NotImplementedError("TODO: Chapter 01")


def squared_error_gradient(weight: float, x: float, target: float) -> float:
    """Use autograd to return d((weight*x-target)^2)/d(weight)."""
    raise NotImplementedError("TODO: Chapter 02")


def make_classifier(input_features: int, hidden_features: int, classes: int) -> nn.Module:
    """Return Linear -> ReLU -> Linear with the requested dimensions."""
    raise NotImplementedError("TODO: Chapter 03")


def classification_accuracy(logits: torch.Tensor, targets: torch.Tensor) -> float:
    """Return the fraction of correctly predicted class indices."""
    raise NotImplementedError("TODO: Chapter 04")
