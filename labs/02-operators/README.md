# Lab 02 — Operators

**Module:** 02 — Operators & Expressions

## Goal

Practice arithmetic operators, floor division and remainder, comparisons, and returning
a tuple.

## Your task

Open **`operators.py`**. It has five functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `rectangle_area(w, h)` — return the width times the height.
   (e.g. `rectangle_area(3, 4)` → `12`)
2. `is_even(n)` — return `True` when `n` is even, `False` otherwise. Hint: `n % 2 == 0`.
   (e.g. `is_even(4)` → `True`, `is_even(7)` → `False`)
3. `average(a, b, c)` — return the average of the three numbers as a float. Use `/`.
   (e.g. `average(3, 6, 9)` → `6.0`)
4. `can_vote(age)` — return `True` when `age` is 18 or older.
   (e.g. `can_vote(18)` → `True`, `can_vote(17)` → `False`)
5. `seconds_to_minutes(total_seconds)` — return a tuple `(minutes, seconds)` using `//`
   and `%`.
   (e.g. `seconds_to_minutes(130)` → `(2, 10)`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/02-operators/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `operators.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `operators_solution.py` as a last resort.
