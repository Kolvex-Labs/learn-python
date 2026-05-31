# Module 01 — Variables, Types & Printing

## What you'll learn

- How to store a value in a variable and use it later
- The four everyday data types: text, whole numbers, decimals, and true/false
- How to combine values into messages with f-strings
- How to ask the user for input — and why it always arrives as text

---

## The concept

A **variable** is a name for a value. You put a value in it, and later you use the name
to get the value back. Think of it as a labeled box: you write `age` on the box, drop
`30` inside, and from then on saying `age` means `30`.

You create a variable with `=`, the **assignment** sign:

```python
age = 30
name = "Alex"
```

Read `=` as "gets" — *age gets 30*. It is **not** the "equals" from math; it means
"store the value on the right into the name on the left."

Every value has a **type** — what kind of thing it is. The four you'll use constantly:

| Type | Means | Example |
|------|-------|---------|
| `str` | text ("string" of characters) | `"hello"`, `"Alex"` |
| `int` | whole number | `30`, `-7`, `0` |
| `float` | number with a decimal point | `19.99`, `3.0` |
| `bool` | true or false | `True`, `False` |

Text always goes in quotes: `"hello"`. Numbers never do: `30`, not `"30"`. That
quote is the difference between the number thirty and the two-character text "30" — and
Python treats them very differently.

You can check a value's type with `type(...)`:

```python
type("hello")   # <class 'str'>
type(30)        # <class 'int'>
type(19.99)     # <class 'float'>
type(True)      # <class 'bool'>
```

---

## Show me

### Storing and using variables

```python
name = "Alex"
age = 30

print(name)        # Alex
print(age)         # 30
```

### f-strings: building messages

To drop a variable into a sentence, put an `f` before the opening quote and wrap the
variable in `{curly braces}`. This is an **f-string** ("formatted string"):

```python
name = "Alex"
age = 30

print(f"My name is {name} and I am {age}.")
# My name is Alex and I am 30.
```

Without the `f`, the braces are just literal text — a classic beginner trip-up:

```python
print("My name is {name}.")    # My name is {name}.   <- not what you want
print(f"My name is {name}.")   # My name is Alex.     <- correct
```

### Reassigning

A variable can change. The latest assignment wins:

```python
score = 10
score = 25
print(score)   # 25
```

### Getting input from the user

`input(...)` shows a prompt and waits for the user to type. **Whatever they type comes
back as a `str`**, even if it looks like a number:

```python
age_text = input("How old are you? ")   # user types 30
print(type(age_text))                   # <class 'str'>  <- text, not a number!
```

To do math with it, **convert** it to a number with `int(...)` or `float(...)`:

```python
age = int(age_text)     # now it's the number 30
print(age + 1)          # 31
```

Going the other way, `str(...)` turns a number into text.

---

## Common mistakes

- **Forgetting the `f`.** `print("Hi {name}")` prints the literal `{name}`. You need
  `print(f"Hi {name}")`. If your braces show up in the output, you forgot the `f`.
- **Treating `input()` as a number.** `input()` always returns text. `input("n? ") + 1`
  crashes because you can't add a number to text. Convert first: `int(input("n? ")) + 1`.
- **Quoting numbers you want to do math with.** `"30" + "5"` gives `"305"` (text glued
  together), not `35`. Drop the quotes for real numbers.

---

## Try it

Open **`labs/01-variables/`** and read its `README.md`. You'll complete the functions in
`variables.py`, then run:

```bash
pytest labs/01-variables/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What does `=` do in `x = 5`?
- A) Tests whether x equals 5
- B) Stores the value 5 in the variable x
- C) Prints 5
- D) Creates an error

**Q2.** What is the type of `"30"`?
- A) `int`
- B) `float`
- C) `str`
- D) `bool`

**Q3.** What does this print?
```python
name = "Sam"
print(f"Hi {name}")
```
- A) `Hi {name}`
- B) `Hi Sam`
- C) `f"Hi Sam"`
- D) `Hi name`

**Q4.** What does `input("Age? ")` return when the user types `25`?
- A) The number `25` as an `int`
- B) The text `"25"` as a `str`
- C) `True`
- D) An error

**Q5.** What does `"5" + "2"` produce?
- A) `7`
- B) `"7"`
- C) `"52"`
- D) An error

**Q6.** Which line correctly turns the text `"19"` into the number 19?
- A) `int("19")`
- B) `str(19)`
- C) `"19".number()`
- D) `float "19"`

**Q7.** After these lines, what does `print(score)` show?
```python
score = 10
score = 25
```
- A) `10`
- B) `25`
- C) `35`
- D) `1025`

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** `=` is assignment: it stores the value on the right into the name on the
left. (A comparison would use `==`, which you'll meet in Module 02.)

**Q2 — C.** The quotes make it a string. `30` without quotes would be an `int`.

**Q3 — B.** The `f` prefix turns `{name}` into the variable's value, `Sam`.

**Q4 — B.** `input()` always returns a `str`, even when the text looks like a number.

**Q5 — C.** With strings, `+` joins them end to end, giving `"52"`. Numbers would add.

**Q6 — A.** `int("19")` converts text to a whole number. `str(19)` does the reverse.

**Q7 — B.** Reassignment replaces the old value; the most recent one (`25`) wins.
