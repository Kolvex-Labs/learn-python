"""Lab 08 — Functions: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def greet(name, greeting="Hello"):
    """Return f"{greeting}, {name}!" using the given greeting (default "Hello")."""
    return f"{greeting}, {name}!"


def add_all(*numbers):
    """Return the sum of all the numbers passed (0 if none are passed)."""
    return sum(numbers)


def apply_discount(price, percent=10):
    """Return price reduced by `percent` percent, as a float.

    apply_discount(100) -> 90.0
    """
    return price - price * (percent / 100)


def build_profile(name, **details):
    """Return a dict starting with {"name": name} plus every extra keyword."""
    profile = {"name": name}
    for key, value in details.items():
        profile[key] = value
    return profile


def repeat(text, times=2):
    """Return the string `text` repeated `times` times."""
    return text * times
