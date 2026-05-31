# Lab 05 — Loops

**Module:** 05 — Loops

## Goal

Practice `for` and `while` loops, `range()`, the accumulator pattern, and building lists.

## Your task

Open **`loops.py`**. It has five functions with `# TODO` markers. Complete each one so it
does what its description says. Don't change the function names or their inputs — the
tests rely on them.

1. `sum_to(n)` — return the sum of the whole numbers 1 through `n`.
   (e.g. `sum_to(5)` → `15`)
2. `count_vowels(text)` — return the number of vowels (a, e, i, o, u), ignoring case.
   (e.g. `count_vowels("hello")` → `2`)
3. `factorial(n)` — return `n!` (n factorial).
   (e.g. `factorial(0)` → `1`, `factorial(4)` → `24`)
4. `first_multiple(numbers, factor)` — return the first item in `numbers` divisible by
   `factor`, or `None` if none qualify.
   (e.g. `first_multiple([4, 9, 6, 7], 3)` → `9`)
5. `countdown(n)` — return a list `[n, n-1, ..., 1]`.
   (e.g. `countdown(5)` → `[5, 4, 3, 2, 1]`, `countdown(0)` → `[]`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/05-loops/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `loops.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `loops_solution.py` as a last resort.
