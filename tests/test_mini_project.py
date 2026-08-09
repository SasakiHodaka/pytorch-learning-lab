"""Focused tests for the capstone project's public behavior."""

import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import torch

from mini_project.config import TrainingConfig
from mini_project.data import create_loaders
from mini_project.model import Classifier
from mini_project.train import run


class MiniProjectTests(unittest.TestCase):
    def test_loader_preserves_all_samples(self) -> None:
        config = TrainingConfig(samples=100)
        train_loader, validation_loader = create_loaders(config)
        self.assertEqual(len(train_loader.dataset) + len(validation_loader.dataset), 100)

    def test_model_validates_shape(self) -> None:
        model = Classifier(hidden_features=4)
        self.assertEqual(model(torch.ones(3, 2)).shape, (3, 2))
        with self.assertRaisesRegex(ValueError, "batch, 2"):
            model(torch.ones(3, 4))

    def test_short_training_creates_checkpoint(self) -> None:
        config = TrainingConfig(samples=120, epochs=4, hidden_features=8)
        with TemporaryDirectory() as directory:
            output = Path(directory) / "model.pt"
            accuracy = run(config, output)
            self.assertTrue(output.exists())
            self.assertGreaterEqual(accuracy, 0.65)


if __name__ == "__main__":
    unittest.main()
