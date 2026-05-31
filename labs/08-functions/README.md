# Lab 08 — Functions

**Module:** 08 — Functions

## Goal

Practice writing functions with defaults, keyword arguments, `*args`, and `**kwargs`,
and returning values instead of printing them.

## Your task

Open **`functions.py`**. It has five functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `greet(name, greeting="Hello")` — return `"{greeting}, {name}!"`.
   (e.g. `greet("Sam")` → `"Hello, Sam!"`; `greet("Sam", "Hi")` → `"Hi, Sam!"`)
2. `add_all(*numbers)` — return the sum of every number passed (0 if none).
   (e.g. `add_all(1, 2, 3)` → `6`; `add_all()` → `0`)
3. `apply_discount(price, percent=10)` — return the price reduced by `percent` percent,
   as a float. (e.g. `apply_discount(100)` → `90.0`)
4. `build_profile(name, **details)` — return a dict starting with `{"name": name}` plus
   every extra keyword. (e.g. `build_profile("Sam", age=9)` → `{"name": "Sam", "age": 9}`)
5. `repeat(text, times=2)` — return `text` repeated `times` times.
   (e.g. `repeat("ab")` → `"abab"`; `repeat("x", 3)` → `"xxx"`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/08-functions/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `functions.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `functions_solution.py` as a last resort.
