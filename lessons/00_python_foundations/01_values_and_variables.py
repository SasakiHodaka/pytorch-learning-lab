"""Values, variables, types, and basic arithmetic."""

# = means "store the value on the right under the name on the left".
model_name = "tiny-classifier"
epochs = 3
learning_rate = 0.1
is_training = True

print(model_name)
print(epochs)
print(learning_rate)
print(is_training)

# type shows what kind of value a variable currently refers to.
print(type(model_name))       # str: text
print(type(epochs))           # int: whole number
print(type(learning_rate))    # float: decimal number
print(type(is_training))      # bool: True or False

# Python evaluates the right-hand side first.
examples_per_epoch = 8
total_examples = epochs * examples_per_epoch
average_loss = (0.9 + 0.6 + 0.3) / epochs

print(f"total examples: {total_examples}")
print(f"average loss: {average_loss:.2f}")

# Exercise: predict both results before running the file.
assert total_examples == 24
assert round(average_loss, 2) == 0.60
