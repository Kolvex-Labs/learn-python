"""Lab 07 — Dictionaries & Sets.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/07-dicts-sets/` to check your work.
"""


def word_count(text):
    """Return a dict mapping each lowercased word -> how many times it appears.

    Split the text on whitespace.
    """
    # TODO: lowercase the text, split it into words, and count each word into a dict.
    raise NotImplementedError("Complete word_count()")


def get_or_default(d, key, default):
    """Return the value for key, or `default` if the key is missing."""
    # TODO: return d's value for key, falling back to default. Hint: .get(key, default)
    raise NotImplementedError("Complete get_or_default()")


def unique_sorted(items):
    """Return a sorted list of the distinct values in `items`."""
    # TODO: drop duplicates with set(...), then return them sorted.
    raise NotImplementedError("Complete unique_sorted()")


def merge(d1, d2):
    """Return a NEW dict with both dicts' pairs. On a conflict, d2 wins.

    Do not change d1 or d2.
    """
    # TODO: start from a copy of d1, then add d2's pairs on top so d2 wins.
    raise NotImplementedError("Complete merge()")


def count_unique(items):
    """Return the number of distinct values in `items`."""
    # TODO: return how many different values items contains.
    raise NotImplementedError("Complete count_unique()")
