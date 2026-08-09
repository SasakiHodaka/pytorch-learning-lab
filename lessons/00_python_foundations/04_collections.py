"""Collections hold multiple related values."""

losses = [0.9, 0.6, 0.3]
losses.append(0.2)
print(losses[0])
print(losses[-1])

image_shape = (28, 28)
height, width = image_shape
print(f"height={height}, width={width}")

config = {"learning_rate": 0.1, "epochs": 4, "batch_size": 2}
print(config["learning_rate"])

for index, current_loss in enumerate(losses, start=1):
    print(f"step={index}, loss={current_loss}")

assert len(losses) == 4
assert image_shape == (height, width)
assert config["epochs"] == 4
