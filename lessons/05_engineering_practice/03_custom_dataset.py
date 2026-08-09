"""Create a Dataset that validates and transforms individual samples."""

import torch
from torch.utils.data import DataLoader, Dataset


class PointDataset(Dataset):
    def __init__(self, points: torch.Tensor, labels: torch.Tensor) -> None:
        if points.ndim != 2:
            raise ValueError("points must have shape [samples, features]")
        if len(points) != len(labels):
            raise ValueError("points and labels must contain the same number of samples")
        self.points = points.float()
        self.labels = labels.long()

    def __len__(self) -> int:
        return len(self.points)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        point = self.points[index]
        label = self.labels[index]
        return point, label


dataset = PointDataset(
    points=torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]]),
    labels=torch.tensor([0, 1, 1, 0]),
)
loader = DataLoader(dataset, batch_size=2, shuffle=False)

for points, labels in loader:
    print(points, labels)

assert len(dataset) == 4
assert dataset[0][0].dtype == torch.float32
assert dataset[0][1].dtype == torch.int64
