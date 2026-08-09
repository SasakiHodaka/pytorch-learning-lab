"""Turn logits into a supervised classification loss."""

import torch
from torch import nn

logits = torch.tensor([[2.0, 0.5], [0.1, 1.5]])
targets = torch.tensor([0, 1])

probabilities = torch.softmax(logits, dim=1)
predictions = logits.argmax(dim=1)
loss = nn.CrossEntropyLoss()(logits, targets)

print(f"logits:\n{logits}")
print(f"probabilities:\n{probabilities}")
print(f"predictions: {predictions}")
print(f"loss: {loss.item():.4f}")

# CrossEntropyLoss expects raw logits, not values already passed through softmax.
assert torch.allclose(probabilities.sum(dim=1), torch.ones(2))
assert torch.equal(predictions, targets)
assert loss.ndim == 0
