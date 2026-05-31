"""Lab 13 — Object-Oriented Programming.

Complete the two classes below. Replace each `raise NotImplementedError(...)` line with
your code. Run `pytest labs/13-oop/` to check your work.
"""


class Rectangle:
    """A rectangle with a width and a height."""

    def __init__(self, width, height):
        """Store `width` and `height` on the instance."""
        # TODO: save width and height as attributes with self.width = ... etc.
        raise NotImplementedError("Complete Rectangle.__init__()")

    def area(self):
        """Return the area: width * height."""
        # TODO: return self.width * self.height.
        raise NotImplementedError("Complete Rectangle.area()")

    def perimeter(self):
        """Return the perimeter: 2 * (width + height)."""
        # TODO: return 2 * (self.width + self.height).
        raise NotImplementedError("Complete Rectangle.perimeter()")


class BankAccount:
    """A bank account that tracks a balance."""

    def __init__(self, balance=0):
        """Store the starting `balance` on the instance (defaults to 0)."""
        # TODO: save balance as self.balance.
        raise NotImplementedError("Complete BankAccount.__init__()")

    def deposit(self, amount):
        """Add `amount` to the balance."""
        # TODO: increase self.balance by amount.
        raise NotImplementedError("Complete BankAccount.deposit()")

    def withdraw(self, amount):
        """Subtract `amount` from the balance.

        Raise ValueError("insufficient funds") if `amount` is greater than the balance.
        """
        # TODO: if amount > self.balance, raise ValueError("insufficient funds").
        # Otherwise subtract amount from self.balance.
        raise NotImplementedError("Complete BankAccount.withdraw()")
