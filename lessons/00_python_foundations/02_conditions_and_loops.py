"""Conditions decide; loops repeat."""

loss = 0.25

if loss < 0.3:
    print("loss is small")
else:
    print("keep training")

# range(3) produces 0, 1, 2. Python starts counting at zero.
for epoch in range(3):
    print(f"epoch index: {epoch}")

losses = [0.9, 0.6, 0.3]
total = 0.0

for current_loss in losses:
    total = total + current_loss

mean_loss = total / len(losses)
print(f"mean loss: {mean_loss:.2f}")

# A while loop continues while its condition is True.
countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1

assert mean_loss == 0.6
assert countdown == 0
