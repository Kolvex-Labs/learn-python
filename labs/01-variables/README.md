# Lab 01 — Variables

**Module:** 01 — Variables, Types & Printing

## Goal

Practice storing values, converting between text and numbers, and building messages
with f-strings.

## Your task

Open **`variables.py`**. It has four functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `greeting(name)` — return the string `Hello, <name>!`
   (e.g. `greeting("Sam")` → `"Hello, Sam!"`)
2. `to_int(text)` — convert a string like `"42"` into the integer `42` and return it.
3. `add_one(text)` — given a string number like `"7"`, return the integer one larger
   (`8`). Hint: convert first, then add.
4. `describe(name, age)` — return `"<name> is <age> years old."`
   (e.g. `describe("Sam", 9)` → `"Sam is 9 years old."`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/01-variables/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `variables.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `variables_solution.py` as a last resort.
