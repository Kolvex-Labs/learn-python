"""Lab 09 — Errors & Exceptions: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def safe_int(text):
    """Return int(text), or None if it cannot be converted."""
    try:
        return int(text)
    except ValueError:
        return None


def divide(a, b):
    """Return a / b, but raise ValueError("cannot divide by zero") when b == 0."""
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b


def get_item(items, index):
    """Return items[index], or None if the index is out of range."""
    try:
        return items[index]
    except IndexError:
        return None


def parse_or_default(text, default):
    """Return int(text) if possible, otherwise return `default`."""
    try:
        return int(text)
    except ValueError:
        return default
