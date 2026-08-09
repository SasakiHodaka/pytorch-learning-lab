"""Deterministic synthetic data and DataLoaders."""

import torch
from torch.utils.data import DataLoader, TensorDataset, random_split

from mini_project.config import TrainingConfig


def create_loaders(config: TrainingConfig) -> tuple[DataLoader, DataLoader]:
    generator = torch.Generator().manual_seed(config.seed)
    features = torch.randn(config.samples, 2, generator=generator)
    targets = (features[:, 0] ** 2 + features[:, 1] > 0.5).long()
    dataset = TensorDataset(features, targets)

    validation_size = int(len(dataset) * config.validation_fraction)
    training_size = len(dataset) - validation_size
    training_data, validation_data = random_split(
        dataset, [training_size, validation_size], generator=generator
    )
    training_loader = DataLoader(
        training_data, batch_size=config.batch_size, shuffle=True, generator=generator
    )
    validation_loader = DataLoader(
        validation_data, batch_size=config.batch_size, shuffle=False
    )
    return training_loader, validation_loader
