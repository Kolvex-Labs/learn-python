"""Lab 03 — Strings in Depth.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/03-strings/` to check your work.
"""


def shout(text):
    """Return text in upper case with a '!' added. Example: 'hi' -> 'HI!'."""
    # TODO: uppercase the text with .upper() and add "!" on the end.
    raise NotImplementedError("Complete shout()")


def initials(full_name):
    """Return the uppercase first letter of each word, joined.

    Example: 'ada lovelace' -> 'AL'.
    """
    # TODO: split full_name into words, take the first letter of each,
    #       uppercase them, and join them into one string.
    raise NotImplementedError("Complete initials()")


def last_char(text):
    """Return the last character of text."""
    # TODO: use negative indexing to return text[-1].
    raise NotImplementedError("Complete last_char()")


def count_letter(text, letter):
    """Return how many times `letter` appears in `text`."""
    # TODO: use the .count(...) method.
    raise NotImplementedError("Complete count_letter()")


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards (case-insensitive).

    Example: 'Level' -> True, 'hello' -> False.
    """
    # TODO: lowercase the text, then compare it to its reverse (text[::-1]).
    raise NotImplementedError("Complete is_palindrome()")
