"""Understand shared memory, copies, and device-aware code."""

import numpy as np
import torch

array = np.array([1.0, 2.0, 3.0], dtype=np.float32)
shared = torch.from_numpy(array)
copied = torch.tensor(array)

array[0] = 100.0
print(f"NumPy: {array}")
print(f"shared tensor: {shared}")
print(f"copied tensor: {copied}")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
on_device = copied.to(device)
back_on_cpu = on_device.cpu()
print(f"selected device: {device}")

assert shared[0].item() == 100.0
assert copied[0].item() == 1.0
assert back_on_cpu.device.type == "cpu"
