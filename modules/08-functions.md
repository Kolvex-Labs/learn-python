# Module 08 — Functions

## What you'll learn

- How to define your own function with `def` and call it
- The difference between `return` and `print`
- Default parameter values and keyword arguments
- How `*args` and `**kwargs` let a function take any number of inputs
- The difference between local and global scope, plus what a docstring is

---

## The concept

A **function** is a named block of code you can run whenever you want. You write the
steps once, give them a name, and then "call" that name to run them again and again. You
have already been calling functions: `print(...)`, `len(...)`, and `int(...)` are all
functions.

You make your own with `def` (short for "define"):

```python
def greet():
    print("Hello!")
```

That block says "when someone calls `greet`, print Hello!". Nothing happens until you
**call** it by writing its name with parentheses:

```python
greet()    # Hello!
```

Most functions need information to work with. You list the names they expect inside the
parentheses. Those names are **parameters**:

```python
def greet(name):
    print(f"Hello, {name}!")
```

When you call the function, the actual values you hand it are **arguments**:

```python
greet("Sam")    # "Sam" is the argument; name is the parameter
```

So a **parameter** is the name in the definition, and an **argument** is the real value
you pass in. Same slot, two names depending on where you're standing.

### return vs print

`print` shows something on the screen. `return` hands a value back to the code that
called the function, so it can be stored or used. They are not the same.

```python
def add(a, b):
    return a + b

total = add(2, 3)    # total now holds 5
print(total)         # 5
```

If `add` used `print(a + b)` instead of `return`, you'd see `5` on screen but `total`
would be `None`, because the function gave nothing back. **Use `return` when you want a
result you can keep working with.**

---

## Show me

### Default parameter values

A parameter can have a default, used when the caller doesn't supply that argument:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Sam"))               # Hello, Sam!
print(greet("Sam", "Welcome"))    # Welcome, Sam!
```

Because `greeting` has a default, you can leave it out.

### Keyword arguments

You can pass arguments by name, in any order. These are **keyword arguments**:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="Sam", greeting="Hi"))    # Hi, Sam!
print(greet(greeting="Hi", name="Sam"))    # Hi, Sam!   (order doesn't matter)
```

### `*args`: any number of positional arguments

Sometimes you don't know how many values the caller will pass. `*args` gathers them all
into a tuple:

```python
def add_all(*numbers):
    return sum(numbers)

print(add_all(1, 2, 3))      # 6
print(add_all(10, 20))       # 30
print(add_all())             # 0   (empty, sum is 0)
```

The `*` is what does the gathering. The name `numbers` is up to you.

### `**kwargs`: any number of keyword arguments

`**kwargs` gathers extra keyword arguments into a dict:

```python
def build_profile(name, **details):
    profile = {"name": name}
    for key, value in details.items():
        profile[key] = value
    return profile

print(build_profile("Sam", age=9, city="Reno"))
# {'name': 'Sam', 'age': 9, 'city': 'Reno'}
```

### Local vs global scope

A variable made *inside* a function lives only there. This is its **scope**. Code outside
can't see it:

```python
def f():
    secret = 42        # local to f
    return secret

print(f())             # 42
print(secret)          # NameError: name 'secret' is not defined
```

A variable made at the top level of your file is **global** and can be read inside
functions. Keep functions simple by passing values in as arguments rather than reaching
out to globals.

### Docstrings

A **docstring** is a string right under `def` that explains what the function does. Tools
and people read it:

```python
def square(n):
    """Return n multiplied by itself."""
    return n * n
```

---

## Common mistakes

- **Using `print` when you need `return`.** `print` only shows a value; it doesn't hand
  one back. If you call a print-only function and try to store the result, you get
  `None`. Use `return` for any value you want to reuse.
- **Forgetting the parentheses when calling.** `greet` by itself refers to the function
  but doesn't run it. You must write `greet()` to actually call it.
- **Putting a default that can change in the wrong spot.** Parameters with defaults must
  come *after* ones without: `def f(a, b=1)` is fine, but `def f(a=1, b)` raises a
  `SyntaxError`. Required parameters first, defaults last.

---

## Try it

Open **`labs/08-functions/`** and read its `README.md`. You'll complete the functions in
`functions.py`, then run:

```bash
pytest labs/08-functions/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What keyword defines a function?
- A) `func`
- B) `def`
- C) `function`
- D) `define`

**Q2.** In `def greet(name):`, what is `name`?
- A) An argument
- B) A parameter
- C) A return value
- D) A docstring

**Q3.** What's the key difference between `return` and `print`?
- A) Nothing, they're the same
- B) `return` hands a value back to the caller; `print` only displays it
- C) `print` is faster
- D) `return` shows text in color

**Q4.** Given `def greet(name, greeting="Hello"):`, what does `greet("Sam")` return?
- A) `"Sam, Hello!"`
- B) `"Hello, Sam!"`
- C) `"Hello!"`
- D) An error

**Q5.** What does `*numbers` collect the positional arguments into?
- A) A list
- B) A dict
- C) A tuple
- D) A string

**Q6.** What does `**details` collect keyword arguments into?
- A) A list
- B) A tuple
- C) A set
- D) A dict

**Q7.** A variable created inside a function is...
- A) Global, visible everywhere
- B) Local, visible only inside that function
- C) Saved to a file
- D) Deleted immediately

**Q8.** What is a docstring?
- A) A comment that Python runs
- B) A string just under `def` that describes the function
- C) The function's return value
- D) A type of error

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** `def` defines a function.

**Q2 — B.** `name` in the definition is a parameter. The value you pass when calling is
the argument.

**Q3 — B.** `return` hands a value back so the caller can use it; `print` only shows it.

**Q4 — B.** `greeting` defaults to `"Hello"`, so the result is `"Hello, Sam!"`.

**Q5 — C.** `*args` gathers positional arguments into a tuple.

**Q6 — D.** `**kwargs` gathers keyword arguments into a dict.

**Q7 — B.** Variables made inside a function are local to it and can't be seen outside.

**Q8 — B.** A docstring is the string right under `def` that documents the function.
