"""Locate the installed Python implementation of a familiar API."""

import inspect

import torch
from torch import nn

source_file = inspect.getsourcefile(nn.Linear)
forward_source = inspect.getsource(nn.Linear.forward)

print(f"torch version: {torch.__version__}")
print(f"nn.Linear source file: {source_file}")
print("nn.Linear.forward source:")
print(forward_source)

assert source_file is not None
assert "linear" in forward_source

# Next investigation steps in pytorch/pytorch:
# 1. Find the functional call used by nn.Linear.forward.
# 2. Find tests that exercise Linear.
# 3. Record the repository commit hash used during the investigation.
