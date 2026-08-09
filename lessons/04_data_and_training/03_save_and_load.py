"""Save model state and reproduce predictions after loading it."""

from pathlib import Path
from tempfile import TemporaryDirectory

import torch
from torch import nn


def create_model() -> nn.Module:
    return nn.Linear(2, 1)


torch.manual_seed(0)
model = create_model()
inputs = torch.tensor([[1.0, 2.0]])
expected = model(inputs).detach()

with TemporaryDirectory() as temporary_directory:
    checkpoint_path = Path(temporary_directory) / "model.pt"
    torch.save(model.state_dict(), checkpoint_path)

    restored_model = create_model()
    state = torch.load(checkpoint_path, weights_only=True)
    restored_model.load_state_dict(state)
    actual = restored_model(inputs).detach()

print(f"before save: {expected}")
print(f"after load:  {actual}")
assert torch.equal(actual, expected)
