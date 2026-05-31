"""Lab 11 — Modules, Packages & the Standard Library.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/11-modules/` to check your work.

Each function uses a module from the standard library. Add the imports you need at the
top of this file.
"""


def circle_area(r):
    """Return the area of a circle with radius `r` (math.pi * r ** 2)."""
    # TODO: import math at the top of the file, then return math.pi * r ** 2.
    raise NotImplementedError("Complete circle_area()")


def mean(numbers):
    """Return the average of `numbers` using statistics.mean."""
    # TODO: import statistics, then return statistics.mean(numbers).
    raise NotImplementedError("Complete mean()")


def most_common(items):
    """Return the single most common value in `items`."""
    # TODO: use collections.Counter. Counter(items).most_common(1) returns a list
    # like [(value, count)] — return just the value.
    raise NotImplementedError("Complete most_common()")


def pick(items, seed):
    """Return a deterministically chosen item from `items` using the given seed.

    Use random.Random(seed).choice(items) so the same seed always picks the same item.
    """
    # TODO: import random, then return random.Random(seed).choice(items).
    raise NotImplementedError("Complete pick()")
