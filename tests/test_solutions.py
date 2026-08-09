"""Tests proving that the reference solutions satisfy the exercise contract."""

import unittest

import torch
from torch import nn

from practice import solutions


class PythonMeanTests(unittest.TestCase):
    def test_mean(self) -> None:
        self.assertEqual(solutions.python_mean([1.0, 2.0, 3.0]), 2.0)

    def test_empty(self) -> None:
        with self.assertRaises(ValueError):
            solutions.python_mean([])


class TensorExerciseTests(unittest.TestCase):
    def test_normalize_rows(self) -> None:
        values = torch.tensor([[1.0, 3.0], [2.0, 2.0]])
        actual = solutions.normalize_rows(values)
        expected = torch.tensor([[0.25, 0.75], [0.5, 0.5]])
        torch.testing.assert_close(actual, expected)

    def test_gradient(self) -> None:
        actual = solutions.squared_error_gradient(weight=2.0, x=3.0, target=10.0)
        self.assertEqual(actual, -24.0)


class ModelExerciseTests(unittest.TestCase):
    def test_model_shape_and_layers(self) -> None:
        model = solutions.make_classifier(3, 5, 2)
        self.assertIsInstance(model[0], nn.Linear)
        self.assertIsInstance(model[1], nn.ReLU)
        self.assertEqual(model(torch.ones(4, 3)).shape, (4, 2))

    def test_accuracy(self) -> None:
        logits = torch.tensor([[3.0, 1.0], [0.0, 2.0], [4.0, 1.0]])
        targets = torch.tensor([0, 1, 1])
        self.assertAlmostEqual(solutions.classification_accuracy(logits, targets), 2 / 3)


if __name__ == "__main__":
    unittest.main()
