"""Use autograd and compare its gradient with a hand calculation."""

import torch

x = torch.tensor(3.0)
weight = torch.tensor(2.0, requires_grad=True)
bias = torch.tensor(1.0, requires_grad=True)

prediction = weight * x + bias
target = torch.tensor(10.0)
loss = (prediction - target) ** 2
loss.backward()

print(f"prediction={prediction.item()}")
print(f"loss={loss.item()}")
print(f"d_loss/d_weight={weight.grad.item()}")
print(f"d_loss/d_bias={bias.grad.item()}")

# prediction=7, error=-3. d(error^2)/dw = 2*error*x = -18.
assert weight.grad.item() == -18.0
assert bias.grad.item() == -6.0
