"""Lab 06 — Lists & Tuples: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def largest(numbers):
    """Return the largest number in the list, or None if the list is empty."""
    if not numbers:
        return None
    return max(numbers)


def evens(numbers):
    """Return a list of only the even numbers, in their original order."""
    return [n for n in numbers if n % 2 == 0]


def reverse_list(items):
    """Return a NEW list with the items reversed. Do not change the input list."""
    return items[::-1]


def second_item(items):
    """Return the item at index 1 (the second item)."""
    return items[1]


def total_and_count(numbers):
    """Return a tuple (sum_of_numbers, how_many_numbers)."""
    return (sum(numbers), len(numbers))
