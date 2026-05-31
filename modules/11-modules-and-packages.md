# Module 11 — Modules, Packages & the Standard Library

## What you'll learn

- How to bring in code from elsewhere with `import` and `from x import y`
- What the standard library is, and a tour of `math`, `random`, `statistics`, `collections`
- How to install third-party packages with `pip` from PyPI
- A recap of virtual environments and why they keep projects tidy
- How to split your own code into modules, and what `if __name__ == "__main__":` is for

---

## The concept

You don't have to write everything yourself. Other people have written useful code, and
Python lets you pull it in. A **module** is just a `.py` file full of code you can reuse.
A **package** is a folder of modules bundled together.

### Importing

The `import` statement brings a module's code into your program:

```python
import math
print(math.sqrt(9))    # 3.0
```

After `import math`, you reach inside it with a dot: `math.sqrt`, `math.pi`. The `math.`
part tells Python where the name lives.

If you only want one thing from a module, use `from ... import ...`:

```python
from math import sqrt
print(sqrt(9))         # 3.0  — no "math." needed now
```

Both are fine. `import math` keeps the name `math.sqrt`, which makes it obvious where
`sqrt` came from. `from math import sqrt` is shorter. Pick whichever reads more clearly.

### The standard library

The **standard library** is the big set of modules that ships *with* Python. Nothing to
install — just `import` and go. A few you'll reach for often:

- **`math`** — math functions and constants: `math.pi`, `math.sqrt(x)`, `math.floor(x)`.
- **`random`** — random choices: `random.choice(items)`, `random.randint(1, 6)`.
- **`statistics`** — averages and spread: `statistics.mean(nums)`, `statistics.median(nums)`.
- **`collections`** — handy data containers. `Counter` tallies how often things appear:

```python
from collections import Counter
votes = ["yes", "no", "yes", "yes"]
print(Counter(votes).most_common(1))   # [('yes', 3)]
```

### Third-party packages: pip and PyPI

Some code isn't in the standard library. It lives on **PyPI** (the Python Package Index),
a public library of packages anyone can publish. You install from it with **`pip`**, the
package installer that came with Python:

```bash
pip install requests
```

Now `import requests` works in your program. `requests` is a popular package for fetching
web pages — not part of Python itself, but one command away.

### Virtual environments (recap)

A **virtual environment** (the `.venv` you made in setup) is a private box of installed
packages for one project. When it's active (your prompt shows `(.venv)`), `pip install`
puts packages there, not into your whole system. So Project A can use one version of a
package and Project B another, with no clash. Activate it before you `pip install` or run
your code.

### Organizing your own code into modules

Your own files are modules too. If you write `tools.py`:

```python
# tools.py
def shout(text):
    return text.upper() + "!"
```

...another file in the same folder can use it:

```python
# main.py
import tools
print(tools.shout("hi"))    # HI!
```

Splitting code across files keeps each file short and focused.

### `if __name__ == "__main__":`

When Python runs a file directly, it sets a hidden variable `__name__` to the string
`"__main__"`. When the file is *imported* instead, `__name__` is the module's name. So
this guard means "only run this part when I'm run directly, not when I'm imported":

```python
def greet(name):
    return f"Hi, {name}"

if __name__ == "__main__":
    print(greet("world"))     # runs only when you do: python thisfile.py
```

Put your `greet` function above the guard so others can import and reuse it, and put the
"run it now" demo below the guard so it doesn't fire on import.

---

## Show me

### Using a few standard-library modules

```python
import math
import statistics
from collections import Counter

print(math.pi)                          # 3.141592653589793
print(statistics.mean([2, 4, 6]))       # 4
print(Counter("banana").most_common(1)) # [('a', 3)]
```

### Deterministic randomness with a seed

`random` is random — unless you give it a **seed**, a starting number that makes it
repeat the same sequence every time. Great for tests.

```python
import random

r = random.Random(42)
print(r.choice(["a", "b", "c"]))   # always the same pick for seed 42
```

### The main guard in action

```python
# area.py
import math

def circle_area(r):
    return math.pi * r ** 2

if __name__ == "__main__":
    print(circle_area(2))     # 12.566370614359172
```

Run `python area.py` and it prints. `import area` from another file and it stays quiet —
you just get the `circle_area` function to use.

---

## Common mistakes

- **Importing a name you didn't import.** `import math` then calling bare `sqrt(9)` fails
  with `NameError`. Either write `math.sqrt(9)`, or import it by name first:
  `from math import sqrt`.
- **Naming your file after a module.** If you name your own file `random.py` or `math.py`,
  Python imports *your* file instead of the real module, and things break in confusing
  ways. Give your files their own names, like `tools.py`.
- **Forgetting to activate the venv before `pip install`.** Without `(.venv)` showing, the
  package may install somewhere your project can't see, or system-wide. Activate first,
  then install.

---

## Try it

Open **`labs/11-modules/`** and read its `README.md`. You'll complete the functions in
`toolbox.py`, then run:

```bash
pytest labs/11-modules/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What is a module in Python?
- A) A type of error
- B) A `.py` file full of code you can reuse
- C) A web page
- D) A kind of variable

**Q2.** After `import math`, how do you call its `sqrt` function?
- A) `sqrt(9)`
- B) `math.sqrt(9)`
- C) `import sqrt(9)`
- D) `math->sqrt(9)`

**Q3.** What is the standard library?
- A) Packages you must install from PyPI
- B) The set of modules that ships with Python, ready to import
- C) A folder you create yourself
- D) Another name for pip

**Q4.** What does `pip install requests` do?
- A) Runs requests once
- B) Downloads and installs the `requests` package from PyPI
- C) Imports requests into the current file
- D) Deletes requests

**Q5.** Why use a virtual environment?
- A) To make code run faster
- B) To keep each project's installed packages separate
- C) To connect to the internet
- D) To format your code

**Q6.** What does `from collections import Counter` followed by
`Counter([1, 1, 2]).most_common(1)` give?
- A) `[(1, 2)]`
- B) `[(2, 1)]`
- C) `2`
- D) `[1, 1, 2]`

**Q7.** When does the code under `if __name__ == "__main__":` run?
- A) Only when the file is imported by another file
- B) Only when the file is run directly
- C) Never
- D) Every time, both on import and on direct run

**Q8.** Why does `random.Random(42).choice(items)` always return the same item?
- A) Because `choice` always picks the first item
- B) Because the fixed seed `42` makes the sequence repeatable
- C) Because lists are not random
- D) Because it caches the result

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** A module is a `.py` file of reusable code. A folder of modules is a package.

**Q2 — B.** After `import math`, you reach its contents with a dot: `math.sqrt(9)`.

**Q3 — B.** The standard library ships with Python — `import` it directly, no install
needed.

**Q4 — B.** `pip` fetches the package from PyPI and installs it into your environment so
you can import it.

**Q5 — B.** A virtual environment isolates one project's packages from another's, so
versions never clash.

**Q6 — A.** `1` appears twice, so `most_common(1)` returns `[(1, 2)]` — the value and its
count.

**Q7 — B.** `__name__` equals `"__main__"` only when the file is run directly, so the
guarded code runs then and not on import.

**Q8 — B.** A seed sets the starting point of the random sequence. The same seed gives the
same sequence every time, which makes the pick deterministic.
