"""Lab 04 — Making Decisions: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def grade(score):
    """Return a letter grade for the score.

    A if score >= 90, B if >= 80, C if >= 70, D if >= 60, otherwise F.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def sign(n):
    """Return 'positive', 'negative', or 'zero' for the number n."""
    if n > 0:
        return "positive"
    elif n < 0:
        return "negative"
    else:
        return "zero"


def fizzbuzz(n):
    """Return 'FizzBuzz' if n is divisible by 15, 'Fizz' if by 3, 'Buzz' if by 5,
    otherwise the number as a string (str(n)).
    """
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)


def ticket_price(age):
    """Return the ticket price for the given age.

    5 if age < 13, 7 if age >= 65, otherwise 10.
    """
    if age < 13:
        return 5
    elif age >= 65:
        return 7
    else:
        return 10
