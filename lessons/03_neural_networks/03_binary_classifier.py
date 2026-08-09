"""Train a small network to learn the XOR classification problem."""

import torch
from torch import nn


class XorClassifier(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(2, 8),
            nn.ReLU(),
            nn.Linear(8, 2),
        )

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        return self.network(inputs)


torch.manual_seed(0)
features = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
targets = torch.tensor([0, 1, 1, 0])
model = XorClassifier()
optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
loss_function = nn.CrossEntropyLoss()

for _ in range(300):
    logits = model(features)
    loss = loss_function(logits, targets)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

with torch.no_grad():
    predictions = model(features).argmax(dim=1)

print(f"predictions: {predictions}")
print(f"targets:     {targets}")
assert torch.equal(predictions, targets)
