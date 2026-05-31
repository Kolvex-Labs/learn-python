"""Lab 05 — Loops: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def sum_to(n):
    """Return the sum of the whole numbers 1 through n. sum_to(5) -> 15."""
    total = 0
    for number in range(1, n + 1):
        total = total + number
    return total


def count_vowels(text):
    """Return the number of vowels (a, e, i, o, u) in text, ignoring case."""
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count = count + 1
    return count


def factorial(n):
    """Return n! (n factorial). factorial(0) -> 1, factorial(4) -> 24."""
    result = 1
    for number in range(1, n + 1):
        result = result * number
    return result


def first_multiple(numbers, factor):
    """Return the first item in `numbers` divisible by `factor`, or None if none qualify."""
    for number in numbers:
        if number % factor == 0:
            return number
    return None


def countdown(n):
    """Return a list [n, n-1, ..., 1]. countdown(0) -> []."""
    result = []
    for number in range(n, 0, -1):
        result.append(number)
    return result
