"""Lab 05 — Loops.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/05-loops/` to check your work.
"""


def sum_to(n):
    """Return the sum of the whole numbers 1 through n. sum_to(5) -> 15."""
    # TODO: start a total at 0, loop over range(1, n + 1), add each number.
    raise NotImplementedError("Complete sum_to()")


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text, ignoring case."""
    # TODO: loop over the characters of text.lower() and count the vowels.
    raise NotImplementedError("Complete count_vowels()")


def factorial(n):
    """Return n! (n factorial). factorial(0) -> 1, factorial(4) -> 24."""
    # TODO: start a result at 1, multiply it by each number from 1 to n.
    raise NotImplementedError("Complete factorial()")


def first_multiple(numbers, factor):
    """Return the first item in `numbers` divisible by `factor`, or None if none qualify."""
    # TODO: loop over numbers; return the first one where num % factor == 0.
    #       If the loop finishes with no match, return None.
    raise NotImplementedError("Complete first_multiple()")


def countdown(n):
    """Return a list [n, n-1, ..., 1]. countdown(0) -> []."""
    # TODO: build a list counting down from n to 1. Hint: range(n, 0, -1).
    raise NotImplementedError("Complete countdown()")
