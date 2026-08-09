"""Use gradient clipping and a learning-rate scheduler deliberately."""

import torch
from torch import nn

torch.manual_seed(0)
model = nn.Linear(2, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.2)
scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=2, gamma=0.5)
features = torch.randn(16, 2)
targets = features.sum(dim=1, keepdim=True)

learning_rates: list[float] = []
for epoch in range(5):
    loss = nn.functional.mse_loss(model(features), targets)
    optimizer.zero_grad()
    loss.backward()
    gradient_norm = nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()
    learning_rates.append(optimizer.param_groups[0]["lr"])
    scheduler.step()
    print(
        f"epoch={epoch}, loss={loss.item():.4f}, "
        f"gradient_norm={gradient_norm:.3f}, lr={learning_rates[-1]:.3f}"
    )

assert learning_rates == [0.2, 0.2, 0.1, 0.1, 0.05]
