"""Lab 01 — Variables: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def greeting(name):
    """Return a greeting like 'Hello, Sam!' for the given name."""
    return f"Hello, {name}!"


def to_int(text):
    """Convert a numeric string like '42' to the integer 42 and return it."""
    return int(text)


def add_one(text):
    """Given a numeric string like '7', return the integer one larger (8)."""
    return int(text) + 1


def describe(name, age):
    """Return '<name> is <age> years old.'"""
    return f"{name} is {age} years old."
