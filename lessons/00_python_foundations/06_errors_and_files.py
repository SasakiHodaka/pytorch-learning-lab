"""Read errors and use files without hiding failures."""

from pathlib import Path


def safe_divide(numerator: float, denominator: float) -> float | None:
    """Return None when division is impossible."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        print("denominator must not be zero")
        return None


print(safe_divide(6.0, 2.0))
print(safe_divide(6.0, 0.0))

this_file = Path(__file__)
text = this_file.read_text(encoding="utf-8")
print(this_file.name)
print(f"characters in this lesson: {len(text)}")

assert safe_divide(6.0, 2.0) == 3.0
assert safe_divide(6.0, 0.0) is None
assert "safe_divide" in text
