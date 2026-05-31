"""Lab 13 — Object-Oriented Programming: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        """Store `width` and `height` on the instance."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area: width * height."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter: 2 * (width + height)."""
        return 2 * (self.width + self.height)


class BankAccount:
    """A bank account that tracks a balance."""

    def __init__(self, balance=0):
        """Store the starting `balance` on the instance (defaults to 0)."""
        self.balance = balance

    def deposit(self, amount):
        """Add `amount` to the balance."""
        self.balance += amount

    def withdraw(self, amount):
        """Subtract `amount` from the balance.

        Raise ValueError("insufficient funds") if `amount` is greater than the balance.
        """
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
