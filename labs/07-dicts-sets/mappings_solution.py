"""Lab 07 — Dictionaries & Sets: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def word_count(text):
    """Return a dict mapping each lowercased word -> how many times it appears.

    Split the text on whitespace.
    """
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts


def get_or_default(d, key, default):
    """Return the value for key, or `default` if the key is missing."""
    return d.get(key, default)


def unique_sorted(items):
    """Return a sorted list of the distinct values in `items`."""
    return sorted(set(items))


def merge(d1, d2):
    """Return a NEW dict with both dicts' pairs. On a conflict, d2 wins.

    Do not change d1 or d2.
    """
    result = dict(d1)
    result.update(d2)
    return result


def count_unique(items):
    """Return the number of distinct values in `items`."""
    return len(set(items))
