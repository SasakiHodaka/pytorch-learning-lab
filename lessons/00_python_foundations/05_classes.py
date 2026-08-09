"""Classes combine data and behavior."""


class RunningMean:
    """Track the mean of values received one at a time."""

    def __init__(self) -> None:
        self.total = 0.0
        self.count = 0

    def update(self, value: float) -> None:
        self.total += value
        self.count += 1

    def compute(self) -> float:
        if self.count == 0:
            raise ValueError("at least one value is required")
        return self.total / self.count


metric = RunningMean()
metric.update(0.9)
metric.update(0.3)
print(metric.total)
print(metric.count)
print(metric.compute())

assert metric.compute() == 0.6
