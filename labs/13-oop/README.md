# Lab 13 — OOP

**Module:** 13 — Object-Oriented Programming

## Goal

Practice writing classes: storing data with `__init__` and `self`, and adding methods
that act on that data.

## Your task

Open **`shapes.py`**. It has two classes with `# TODO` markers. Complete each method so it
does what its description says. Don't change the class names, method names, or their inputs
— the tests rely on them.

1. `Rectangle(width, height)` — store `width` and `height`.
   - `area()` returns `width * height`.
   - `perimeter()` returns `2 * (width + height)`.
2. `BankAccount(balance=0)` — store the starting `balance` (default 0).
   - `deposit(amount)` adds to the balance.
   - `withdraw(amount)` subtracts from the balance, but raises
     `ValueError("insufficient funds")` if `amount` is more than the balance.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/13-oop/
```

- **Green** → both classes work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the test and what it expected. Fix `shapes.py` and
  run again.

## Stuck?

Ask the tutor agent for a hint, or open `shapes_solution.py` as a last resort.
