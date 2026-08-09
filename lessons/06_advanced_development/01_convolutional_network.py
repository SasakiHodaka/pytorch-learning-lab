"""Follow image shapes through a convolutional neural network."""

import torch
from torch import nn


class TinyCnn(nn.Module):
    def __init__(self, classes: int = 3) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 4, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(4, 8, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d((1, 1)),
        )
        self.classifier = nn.Linear(8, classes)

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        features = self.features(images)
        flattened = torch.flatten(features, start_dim=1)
        return self.classifier(flattened)


model = TinyCnn(classes=3)
images = torch.randn(5, 1, 28, 28)  # batch, channel, height, width
logits = model(images)

print(f"input shape: {images.shape}")
print(f"logit shape: {logits.shape}")
assert logits.shape == (5, 3)
