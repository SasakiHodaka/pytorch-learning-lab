"""Write focused tests with Python's built-in unittest."""

import unittest

import torch


def normalize(values: torch.Tensor) -> torch.Tensor:
    """Scale a non-constant 1D tensor to the range [0, 1]."""
    if values.ndim != 1:
        raise ValueError("values must be a 1D tensor")
    value_range = values.max() - values.min()
    if value_range == 0:
        raise ValueError("values must not all be equal")
    return (values - values.min()) / value_range


class NormalizeTests(unittest.TestCase):
    def test_normalizes_values(self) -> None:
        actual = normalize(torch.tensor([2.0, 4.0, 6.0]))
        expected = torch.tensor([0.0, 0.5, 1.0])
        torch.testing.assert_close(actual, expected)

    def test_rejects_matrix(self) -> None:
        with self.assertRaisesRegex(ValueError, "1D"):
            normalize(torch.ones(2, 2))

    def test_rejects_constant_values(self) -> None:
        with self.assertRaisesRegex(ValueError, "equal"):
            normalize(torch.ones(3))


if __name__ == "__main__":
    unittest.main()
