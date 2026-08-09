"""Make deliberate choices about random seeds and devices."""

import torch


def make_values(seed: int, device: torch.device) -> torch.Tensor:
    torch.manual_seed(seed)
    return torch.rand(3).to(device)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
first = make_values(seed=42, device=device)
second = make_values(seed=42, device=device)

print(f"device={device}")
print(first)
print(second)

assert torch.equal(first, second)
assert first.device == device

# Reproducibility can also depend on hardware, algorithms, libraries, and versions.
