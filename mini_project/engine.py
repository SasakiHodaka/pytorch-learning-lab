"""Reusable training and evaluation loops."""

import torch
from torch import nn
from torch.utils.data import DataLoader


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
) -> float:
    model.train()
    total_loss = 0.0
    total_samples = 0
    for features, targets in loader:
        features, targets = features.to(device), targets.to(device)
        loss = nn.functional.cross_entropy(model(features), targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * len(features)
        total_samples += len(features)
    return total_loss / total_samples


def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> float:
    model.eval()
    correct = 0
    total = 0
    with torch.inference_mode():
        for features, targets in loader:
            features, targets = features.to(device), targets.to(device)
            predictions = model(features).argmax(dim=1)
            correct += (predictions == targets).sum().item()
            total += len(features)
    return correct / total
