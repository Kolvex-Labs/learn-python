"""Lab 02 — Operators & Expressions: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def rectangle_area(w, h):
    """Return the area of a rectangle with width w and height h."""
    return w * h


def is_even(n):
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


def average(a, b, c):
    """Return the average of a, b, and c as a float."""
    return (a + b + c) / 3


def can_vote(age):
    """Return True if age is 18 or older, False otherwise."""
    return age >= 18


def seconds_to_minutes(total_seconds):
    """Return a tuple (minutes, seconds) for the given total_seconds.

    Example: 130 -> (2, 10).
    """
    minutes = total_seconds // 60
    seconds = total_seconds % 60
    return (minutes, seconds)
