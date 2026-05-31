# Lab 09 — Errors & Exceptions

**Module:** 09 — Errors & Exceptions

## Goal

Practice catching specific exceptions with `try` / `except`, returning safe fallbacks,
and raising your own error with `raise`.

## Your task

Open **`errors.py`**. It has four functions with `# TODO` markers. Complete each one so
it does what its description says. Don't change the function names or their inputs — the
tests rely on them.

1. `safe_int(text)` — return `int(text)`, or `None` if it can't convert (catch
   `ValueError`). (e.g. `safe_int("42")` → `42`; `safe_int("hi")` → `None`)
2. `divide(a, b)` — return `a / b`, but `raise ValueError("cannot divide by zero")` when
   `b == 0`. (e.g. `divide(10, 2)` → `5.0`; `divide(1, 0)` → raises `ValueError`)
3. `get_item(items, index)` — return `items[index]`, or `None` if the index is out of
   range (catch `IndexError`). (e.g. `get_item([10, 20], 5)` → `None`)
4. `parse_or_default(text, default)` — return `int(text)` if possible, otherwise return
   `default`. (e.g. `parse_or_default("hi", 0)` → `0`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/09-errors/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `errors.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `errors_solution.py` as a last resort.
