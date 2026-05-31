"""Lab 09 — Errors & Exceptions.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/09-errors/` to check your work.
"""


def safe_int(text):
    """Return int(text), or None if it cannot be converted."""
    # TODO: try to convert text to an int; catch ValueError and return None instead.
    raise NotImplementedError("Complete safe_int()")


def divide(a, b):
    """Return a / b, but raise ValueError("cannot divide by zero") when b == 0."""
    # TODO: if b is 0, raise ValueError("cannot divide by zero"); otherwise return a / b.
    raise NotImplementedError("Complete divide()")


def get_item(items, index):
    """Return items[index], or None if the index is out of range."""
    # TODO: try to return items[index]; catch IndexError and return None instead.
    raise NotImplementedError("Complete get_item()")


def parse_or_default(text, default):
    """Return int(text) if possible, otherwise return `default`."""
    # TODO: try to convert text to an int; on ValueError, return default.
    raise NotImplementedError("Complete parse_or_default()")
