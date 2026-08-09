"""Load samples in mini-batches."""

import torch
from torch.utils.data import DataLoader, TensorDataset

features = torch.arange(20, dtype=torch.float32).reshape(10, 2)
targets = (features.sum(dim=1) > 18).long()
dataset = TensorDataset(features, targets)
loader = DataLoader(dataset, batch_size=4, shuffle=False)

print(f"samples: {len(dataset)}")
print(f"batches: {len(loader)}")

seen = 0
for batch_features, batch_targets in loader:
    print(batch_features.shape, batch_targets.shape)
    seen += batch_features.shape[0]

assert seen == len(dataset)
assert len(loader) == 3  # 4 + 4 + 2 samples
