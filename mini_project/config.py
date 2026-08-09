"""Typed configuration for the capstone project."""

from dataclasses import dataclass
import torch


@dataclass(frozen=True)
class TrainingConfig:
    seed: int = 42
    samples: int = 400
    batch_size: int = 32
    hidden_features: int = 16
    epochs: int = 10
    learning_rate: float = 0.1
    validation_fraction: float = 0.2

    @property
    def device(self) -> torch.device:
        return torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def validate(self) -> None:
        if self.samples < 10:
            raise ValueError("samples must be at least 10")
        if self.batch_size < 1 or self.epochs < 1:
            raise ValueError("batch_size and epochs must be positive")
        if not 0 < self.validation_fraction < 1:
            raise ValueError("validation_fraction must be between 0 and 1")
