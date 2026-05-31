# Lab 04 — Conditionals

**Module:** 04 — Making Decisions

## Goal

Practice `if` / `elif` / `else` chains and getting the order of conditions right.

## Your task

Open **`conditionals.py`**. It has four functions with `# TODO` markers. Complete each
one so it does what its description says. Don't change the function names or their inputs
— the tests rely on them.

1. `grade(score)` — return `"A"` if `score >= 90`, `"B"` if `>= 80`, `"C"` if `>= 70`,
   `"D"` if `>= 60`, otherwise `"F"`.
   (e.g. `grade(95)` → `"A"`, `grade(72)` → `"C"`)
2. `sign(n)` — return `"positive"`, `"negative"`, or `"zero"`.
   (e.g. `sign(5)` → `"positive"`, `sign(0)` → `"zero"`)
3. `fizzbuzz(n)` — return `"FizzBuzz"` if `n` is divisible by 15, `"Fizz"` if by 3,
   `"Buzz"` if by 5, otherwise `str(n)`.
   (e.g. `fizzbuzz(15)` → `"FizzBuzz"`, `fizzbuzz(7)` → `"7"`)
4. `ticket_price(age)` — return `5` if `age < 13`, `7` if `age >= 65`, otherwise `10`.
   (e.g. `ticket_price(10)` → `5`, `ticket_price(70)` → `7`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/04-conditionals/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `conditionals.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `conditionals_solution.py` as a last resort.
