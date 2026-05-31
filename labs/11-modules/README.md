# Lab 11 — Modules

**Module:** 11 — Modules, Packages & the Standard Library

## Goal

Practice importing from the standard library: `math`, `statistics`, `collections`, and
`random`.

## Your task

Open **`toolbox.py`**. It has four functions with `# TODO` markers. Add the imports you
need at the top, then complete each function. Don't change the function names or their
inputs — the tests rely on them.

1. `circle_area(r)` — return `math.pi * r ** 2`.
2. `mean(numbers)` — return the average using `statistics.mean`.
3. `most_common(items)` — return the single most common value, using
   `collections.Counter`.
4. `pick(items, seed)` — return a deterministic choice using
   `random.Random(seed).choice(items)`.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/11-modules/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `toolbox.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `toolbox_solution.py` as a last resort.
