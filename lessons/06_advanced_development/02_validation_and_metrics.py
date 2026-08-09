"""Measure class-specific mistakes with a confusion matrix."""

import torch


def confusion_matrix(
    predictions: torch.Tensor, targets: torch.Tensor, classes: int
) -> torch.Tensor:
    matrix = torch.zeros((classes, classes), dtype=torch.int64)
    for target, prediction in zip(targets, predictions, strict=True):
        matrix[target, prediction] += 1
    return matrix


targets = torch.tensor([0, 0, 1, 1, 2, 2])
predictions = torch.tensor([0, 1, 1, 1, 0, 2])
matrix = confusion_matrix(predictions, targets, classes=3)
accuracy = (predictions == targets).float().mean().item()

print(f"accuracy={accuracy:.3f}")
print("rows=true class, columns=predicted class")
print(matrix)

assert matrix.sum().item() == len(targets)
assert torch.equal(matrix.diag(), torch.tensor([1, 2, 1]))
