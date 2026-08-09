"""Separate training from evaluation."""

import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset


def train_one_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    loss_function: nn.Module,
) -> float:
    model.train()
    total_loss = 0.0
    for features, targets in loader:
        logits = model(features)
        loss = loss_function(logits, targets)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * features.shape[0]
    return total_loss / len(loader.dataset)  # type: ignore[arg-type]


def evaluate(model: nn.Module, loader: DataLoader) -> float:
    model.eval()
    correct = 0
    with torch.no_grad():
        for features, targets in loader:
            correct += (model(features).argmax(dim=1) == targets).sum().item()
    return correct / len(loader.dataset)  # type: ignore[arg-type]


torch.manual_seed(0)
features = torch.randn(200, 2)
targets = (features[:, 0] + features[:, 1] > 0).long()
loader = DataLoader(TensorDataset(features, targets), batch_size=20, shuffle=True)
model = nn.Sequential(nn.Linear(2, 8), nn.ReLU(), nn.Linear(8, 2))
optimizer = torch.optim.SGD(model.parameters(), lr=0.2)
loss_function = nn.CrossEntropyLoss()

for epoch in range(15):
    mean_loss = train_one_epoch(model, loader, optimizer, loss_function)
    if epoch % 5 == 0:
        print(f"epoch={epoch}, loss={mean_loss:.4f}")

accuracy = evaluate(model, loader)
print(f"accuracy={accuracy:.3f}")
assert accuracy > 0.90
