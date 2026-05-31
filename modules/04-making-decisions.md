# Module 04 — Making Decisions

## What you'll learn

- How to run code only when a condition is true, using `if`
- How to add more branches with `elif` and a fallback with `else`
- How to build conditions from comparisons and `and` / `or` / `not`
- Which values count as "false" even though they aren't `False` (truthiness)
- The `match` statement for picking among fixed options (Python 3.10+)

---

## The concept

So far your programs run every line, top to bottom. **Decisions** let a program choose:
do this *only if* something is true. The tool is the **`if` statement`**.

### if

```python
age = 20
if age >= 18:
    print("You can vote.")
```

Read it as: "if `age >= 18` is true, run the indented line." The part after `if` is the
**condition** — an expression that is `True` or `False`. The indented block under it is
the **body**, and it only runs when the condition is true.

Two rules of shape:

- The line ends with a colon `:`.
- The body is **indented** (four spaces). Indentation is how Python knows which lines
  belong to the `if`. Get it wrong and Python complains.

### else: the fallback

`else` runs when the `if` condition is false:

```python
age = 12
if age >= 18:
    print("You can vote.")
else:
    print("Too young to vote.")
```

Exactly one of the two blocks runs, never both.

### elif: more branches

`elif` ("else if") lets you check another condition when the earlier ones were false.
You can chain as many as you like:

```python
score = 75
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D or below")
```

Python checks the conditions top to bottom and runs the **first** one that's true, then
skips the rest. Order matters: put the strictest condition first. This is exactly the
pattern you'll use for the `grade` function in the lab.

### Conditions can combine

A condition is just an expression that's `True` or `False`, so you can use the
comparison and boolean operators from Module 02:

```python
if age >= 13 and age < 65:
    print("Standard ticket.")
```

### Truthiness: values that count as false

Python lets you use *any* value as a condition. Most values count as "true," but a few
count as "false" even though they aren't the word `False`. These **falsy** values are:

- `0` (the number zero)
- `""` (the empty string)
- `[]` (the empty list)
- `None` (a special "nothing" value)

Everything else is **truthy**. This lets you write natural checks:

```python
name = ""
if name:
    print(f"Hello, {name}")
else:
    print("No name given.")     # this runs, because "" is falsy
```

### match: choosing among fixed options

When you're comparing one value against several exact possibilities, `match` can read
more cleanly than a long `elif` chain. It needs **Python 3.10 or newer**:

```python
command = "start"
match command:
    case "start":
        print("Starting up.")
    case "stop":
        print("Shutting down.")
    case _:
        print("Unknown command.")   # _ is the catch-all, like else
```

Each `case` is one option. The underscore `_` matches anything that didn't match above.
You can always write the same logic with `if`/`elif`/`else`; `match` is just tidier for
this shape.

---

## Show me

### A simple if / else

```python
temperature = 35
if temperature > 30:
    print("It's hot.")    # this runs
else:
    print("Not too hot.")
```

### An elif chain (first true wins)

```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"      # 85 >= 80 is the first true one, so grade is "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)         # B
```

### Truthiness

```python
items = []
if items:
    print("There are items.")
else:
    print("The list is empty.")   # this runs, [] is falsy
```

### match

```python
day = "Sat"
match day:
    case "Sat":
        print("Weekend!")   # this runs
    case "Sun":
        print("Weekend!")
    case _:
        print("Weekday.")
```

---

## Common mistakes

- **Forgetting the colon or the indentation.** Every `if`, `elif`, and `else` line ends
  with `:`, and its body must be indented. `if x > 0 print("yes")` is an error; you need
  the colon and a new indented line.
- **Wrong order in an elif chain.** If you check `score >= 70` before `score >= 90`,
  every high score matches the first test and you never reach the `A`. Put the strictest
  condition first.
- **Using `=` instead of `==` in a condition.** `if age = 18:` is an error. To compare,
  use `==`: `if age == 18:`.

---

## Try it

Open **`labs/04-conditionals/`** and read its `README.md`. You'll complete the functions
in `conditionals.py`, then run:

```bash
pytest labs/04-conditionals/
```

Make it green before moving on.

---

## Check yourself

**Q1.** When does the body of an `if` statement run?
- A) Always
- B) Only when the condition is `True`
- C) Only when the condition is `False`
- D) Never

**Q2.** In an `if` / `elif` / `elif` / `else` chain, how many blocks run?
- A) All of them
- B) Exactly one
- C) None
- D) At least two

**Q3.** What does `elif` mean?
- A) "end if"
- B) "else if" — check another condition when the earlier ones were false
- C) "error if"
- D) A typo for `else`

**Q4.** Which of these values is **falsy**?
- A) `1`
- B) `"hi"`
- C) `""`
- D) `[1, 2]`

**Q5.** What ends every `if` line in Python?
- A) A semicolon `;`
- B) A colon `:`
- C) A period `.`
- D) Nothing

**Q6.** Given `score = 95`, which grade does this print?
```python
if score >= 70:
    print("C")
elif score >= 90:
    print("A")
```
- A) `A`
- B) `C`
- C) Both
- D) Nothing

**Q7.** What does the `_` case do in a `match` statement?
- A) Causes an error
- B) Matches nothing
- C) Matches anything that didn't match an earlier case (like `else`)
- D) Repeats the first case

**Q8.** Which minimum Python version does `match` need?
- A) 3.6
- B) 3.8
- C) 3.10
- D) 2.7

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** The indented body runs only when the condition evaluates to `True`.

**Q2 — B.** Python runs the first block whose condition is true, then skips the rest, so
exactly one block runs (the `else` counts as the fallback).

**Q3 — B.** `elif` is "else if": a new condition checked only when all the earlier ones
were false.

**Q4 — C.** The empty string `""` is falsy, along with `0`, `[]`, and `None`. The others
are truthy.

**Q5 — B.** Every `if`, `elif`, and `else` header ends with a colon.

**Q6 — B.** Conditions are checked top to bottom, and `score >= 70` is true first, so it
prints `C` and never reaches the `elif`. That's why order matters: the strict test must
come first.

**Q7 — C.** The underscore is the catch-all case, the `match` version of `else`.

**Q8 — C.** The `match` statement was added in Python 3.10.
