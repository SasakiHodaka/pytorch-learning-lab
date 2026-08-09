"""Run these tests while implementing practice/exercises.py."""

import unittest

import torch

from practice import exercises


class ExerciseTests(unittest.TestCase):
    def test_python_mean(self) -> None:
        self.assertEqual(exercises.python_mean([2.0, 4.0]), 3.0)

    def test_normalize_rows(self) -> None:
        actual = exercises.normalize_rows(torch.tensor([[1.0, 1.0], [1.0, 3.0]]))
        torch.testing.assert_close(actual, torch.tensor([[0.5, 0.5], [0.25, 0.75]]))

    def test_gradient(self) -> None:
        self.assertEqual(exercises.squared_error_gradient(2.0, 3.0, 10.0), -24.0)

    def test_classifier(self) -> None:
        model = exercises.make_classifier(2, 4, 3)
        self.assertEqual(model(torch.ones(5, 2)).shape, (5, 3))

    def test_accuracy(self) -> None:
        logits = torch.tensor([[2.0, 1.0], [0.0, 3.0]])
        targets = torch.tensor([0, 1])
        self.assertEqual(exercises.classification_accuracy(logits, targets), 1.0)


if __name__ == "__main__":
    unittest.main()
