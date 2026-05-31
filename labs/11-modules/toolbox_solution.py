"""Lab 11 — Modules, Packages & the Standard Library: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""
import math
import random
import statistics
from collections import Counter


def circle_area(r):
    """Return the area of a circle with radius `r` (math.pi * r ** 2)."""
    return math.pi * r ** 2


def mean(numbers):
    """Return the average of `numbers` using statistics.mean."""
    return statistics.mean(numbers)


def most_common(items):
    """Return the single most common value in `items`."""
    return Counter(items).most_common(1)[0][0]


def pick(items, seed):
    """Return a deterministically chosen item from `items` using the given seed."""
    return random.Random(seed).choice(items)
