"""Fit y = 2x + 1 with a tiny linear model."""

import torch

torch.manual_seed(0)
x = torch.tensor([[0.0], [1.0], [2.0], [3.0]])
y = 2 * x + 1

model = torch.nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_function = torch.nn.MSELoss()

for epoch in range(100):
    prediction = model(x)
    loss = loss_function(prediction, y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 20 == 0:
        print(f"epoch={epoch:3d}, loss={loss.item():.6f}")

learned_weight = model.weight.item()
learned_bias = model.bias.item()
print(f"weight={learned_weight:.3f}, bias={learned_bias:.3f}")

assert abs(learned_weight - 2.0) < 0.05
assert abs(learned_bias - 1.0) < 0.05
