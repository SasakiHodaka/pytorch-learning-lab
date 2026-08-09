"""Functions give a name to reusable behavior."""


def calculate_mean(values: list[float]) -> float:
    """Return the arithmetic mean of a non-empty list."""
    return sum(values) / len(values)


def describe_epoch(epoch: int, loss: float) -> str:
    """Build a readable training message."""
    return f"epoch={epoch}, loss={loss:.3f}"


losses = [0.9, 0.6, 0.3]
mean_loss = calculate_mean(losses)
message = describe_epoch(epoch=3, loss=losses[-1])

print(mean_loss)
print(message)

# Type hints help readers and tools, but Python still executes the function.
assert calculate_mean([2.0, 4.0]) == 3.0
assert message == "epoch=3, loss=0.300"
