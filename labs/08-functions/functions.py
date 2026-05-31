"""Lab 08 — Functions.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/08-functions/` to check your work.
"""


def greet(name, greeting="Hello"):
    """Return f"{greeting}, {name}!" using the given greeting (default "Hello")."""
    # TODO: return the greeting, the name, and an exclamation mark in an f-string.
    raise NotImplementedError("Complete greet()")


def add_all(*numbers):
    """Return the sum of all the numbers passed (0 if none are passed)."""
    # TODO: sum up every number gathered by *numbers and return it.
    raise NotImplementedError("Complete add_all()")


def apply_discount(price, percent=10):
    """Return price reduced by `percent` percent, as a float.

    apply_discount(100) -> 90.0
    """
    # TODO: subtract percent% of price from price and return the result.
    raise NotImplementedError("Complete apply_discount()")


def build_profile(name, **details):
    """Return a dict starting with {"name": name} plus every extra keyword."""
    # TODO: start a dict with the name, then add each extra keyword from details.
    raise NotImplementedError("Complete build_profile()")


def repeat(text, times=2):
    """Return the string `text` repeated `times` times."""
    # TODO: return text repeated times times. Hint: a string times an int repeats it.
    raise NotImplementedError("Complete repeat()")
