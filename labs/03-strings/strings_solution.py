"""Lab 03 — Strings in Depth: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def shout(text):
    """Return text in upper case with a '!' added. Example: 'hi' -> 'HI!'."""
    return text.upper() + "!"


def initials(full_name):
    """Return the uppercase first letter of each word, joined.

    Example: 'ada lovelace' -> 'AL'.
    """
    letters = ""
    for word in full_name.split():
        letters = letters + word[0].upper()
    return letters


def last_char(text):
    """Return the last character of text."""
    return text[-1]


def count_letter(text, letter):
    """Return how many times `letter` appears in `text`."""
    return text.count(letter)


def is_palindrome(text):
    """Return True if text reads the same forwards and backwards (case-insensitive).

    Example: 'Level' -> True, 'hello' -> False.
    """
    lowered = text.lower()
    return lowered == lowered[::-1]
