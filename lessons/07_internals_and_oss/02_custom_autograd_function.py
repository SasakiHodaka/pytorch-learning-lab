"""Implement and numerically check a custom backward formula."""

import torch


class Cube(torch.autograd.Function):
    @staticmethod
    def forward(ctx: object, value: torch.Tensor) -> torch.Tensor:
        ctx.save_for_backward(value)  # type: ignore[attr-defined]
        return value**3

    @staticmethod
    def backward(ctx: object, grad_output: torch.Tensor) -> tuple[torch.Tensor]:
        (value,) = ctx.saved_tensors  # type: ignore[attr-defined]
        return (grad_output * 3 * value**2,)


value = torch.tensor([2.0], dtype=torch.double, requires_grad=True)
result = Cube.apply(value)
result.backward()

print(f"result={result.item()}")
print(f"gradient={value.grad.item()}")
assert value.grad.item() == 12.0

# gradcheck compares backward against a finite-difference approximation.
candidate = torch.randn(3, dtype=torch.double, requires_grad=True)
assert torch.autograd.gradcheck(Cube.apply, (candidate,))
