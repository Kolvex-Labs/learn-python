"""Lab 04 — Making Decisions.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/04-conditionals/` to check your work.
"""


def grade(score):
    """Return a letter grade for the score.

    A if score >= 90, B if >= 80, C if >= 70, D if >= 60, otherwise F.
    """
    # TODO: use an if / elif / else chain. Put the highest cutoff first.
    raise NotImplementedError("Complete grade()")


def sign(n):
    """Return 'positive', 'negative', or 'zero' for the number n."""
    # TODO: check n > 0, n < 0, and otherwise return 'zero'.
    raise NotImplementedError("Complete sign()")


def fizzbuzz(n):
    """Return 'FizzBuzz' if n is divisible by 15, 'Fizz' if by 3, 'Buzz' if by 5,
    otherwise the number as a string (str(n)).
    """
    # TODO: check divisibility by 15 first, then 3, then 5, else str(n).
    raise NotImplementedError("Complete fizzbuzz()")


def ticket_price(age):
    """Return the ticket price for the given age.

    5 if age < 13, 7 if age >= 65, otherwise 10.
    """
    # TODO: use an if / elif / else chain to return the right price.
    raise NotImplementedError("Complete ticket_price()")
