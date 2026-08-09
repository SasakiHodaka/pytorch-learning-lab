"""Run inference without gradients and inspect CPU operations."""

import torch
from torch import nn

model = nn.Sequential(nn.Linear(4, 8), nn.ReLU(), nn.Linear(8, 2))
model.eval()
inputs = torch.randn(16, 4)

with torch.inference_mode():
    outputs = model(inputs)

with torch.profiler.profile(activities=[torch.profiler.ProfilerActivity.CPU]) as profile:
    with torch.inference_mode():
        model(inputs)

print(outputs.shape)
print(profile.key_averages().table(sort_by="self_cpu_time_total", row_limit=5))

assert outputs.shape == (16, 2)
assert not outputs.requires_grad
