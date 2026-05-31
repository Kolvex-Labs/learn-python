# Module 00 — Setup & Your First Program

## What you'll learn

- What Python is and what "running a program" actually means
- How to run Python three ways: a script, the interactive REPL, and the lab tests
- How to write and run your very first program
- How to read a tiny error message without panicking

> Before this module, finish **`SETUP.md`** in the course root. It installs Python and
> your virtual environment. This module assumes that's done and your Terminal prompt
> shows `(.venv)`.

---

## The concept

**Python is a language for giving a computer instructions.** You write those
instructions as plain text in a file, and a program called the *Python interpreter*
reads your file from top to bottom and does what it says.

That's the whole idea. You write steps; Python performs them in order.

A few words you'll see constantly:

- **Code** — the instructions you write.
- **Script** — a file full of code (ends in `.py`), like `hello.py`.
- **Run** — to hand your script to Python so it does what the code says.
- **Output** — what your program prints out or produces.
- **The interpreter** — Python itself, the thing that runs your code. You started it in
  setup; the command is `python`.

Think of a recipe card. The card (your script) lists steps. The cook (Python) reads
each step in order and does it. If a step is unclear, the cook stops and tells you
which line confused them — that's an *error message*, and it's helpful, not scary.

---

## Show me

### 1. The REPL — try one line at a time

The REPL is an interactive Python prompt. It's perfect for quick experiments. Start it:

```bash
python
```

You'll see `>>>`. Type this and press Enter:

```python
>>> print("Hello, world!")
Hello, world!
```

`print(...)` tells Python to show something. Try a little math:

```python
>>> 12 * 4
48
>>> 7 + 3
10
```

Leave the REPL when you're done:

```python
>>> exit()
```

### 2. A script — save it and run it

The REPL forgets everything when you close it. Real programs live in files. In your
editor, create a file called `hello.py` in the course folder with these two lines:

```python
print("Hello, world!")
print("I am learning Python.")
```

Save it. Then in Terminal (with `(.venv)` showing, from `~/Code/python-course`):

```bash
python hello.py
```

Expected output:

```
Hello, world!
I am learning Python.
```

You just wrote and ran a program. Python read `hello.py` top to bottom and did each
line in order.

### 3. Comments — notes Python ignores

A `#` starts a comment. Python skips everything after it on that line. Comments are
notes for humans:

```python
# This is a note. Python ignores it.
print("Comments don't run.")  # you can put one at the end of a line too
```

---

## Common mistakes

- **Forgetting to activate the venv.** If `python` or `pytest` says "command not found"
  or behaves oddly, your prompt probably doesn't show `(.venv)`. Run
  `source .venv/bin/activate` from the course folder first.
- **Smart quotes instead of straight quotes.** If you copy text from a document, you
  might get `"curly"` quotes. Python needs straight ones: `"like this"`. Editors like
  VS Code use straight quotes automatically — type the code yourself.
- **Running from the wrong folder.** `python hello.py` only works if `hello.py` is in
  the folder your Terminal is in. Use `cd ~/Code/python-course` first.

### Reading your first error on purpose

Make a typo so you can see what an error looks like. Put this in a file and run it:

```python
prnt("oops")
```

Python responds:

```
NameError: name 'prnt' is not defined
```

Read it bottom to top: the last line names the problem (`prnt` isn't a real thing),
and Python even points at the line. The fix: spell it `print`. Errors are Python telling
you exactly where it got confused. You'll get very comfortable with them.

---

## Try it

There's no graded lab for this module — your "lab" is getting `hello.py` to print both
lines. Once it does, you're ready.

If you want the tutor agent to confirm you're set up, ask it: *"Check my Python setup."*

---

## Check yourself

**Q1.** What does the Python interpreter do?
- A) Designs the look of your program
- B) Reads your code and performs each instruction in order
- C) Saves your files to the cloud
- D) Connects your computer to the internet

**Q2.** Which command runs a script named `hello.py`?
- A) `run hello.py`
- B) `python hello.py`
- C) `hello.py python`
- D) `open hello.py`

**Q3.** What does `print("Hi")` do?
- A) Sends "Hi" to a printer
- B) Saves "Hi" to a file
- C) Shows `Hi` as output
- D) Nothing, it's a comment

**Q4.** What happens to text after a `#` on a line?
- A) Python runs it twice
- B) Python ignores it
- C) Python prints it in red
- D) It causes an error

**Q5.** Your prompt does **not** show `(.venv)` and `pytest` says "command not found".
What's the most likely fix?
- A) Reinstall macOS
- B) Run `source .venv/bin/activate` in the course folder
- C) Rename your file
- D) Restart the computer

**Q6.** What is the REPL best used for?
- A) Storing programs permanently
- B) Trying out single lines of code interactively
- C) Editing images
- D) Installing Python

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** The interpreter reads your instructions and carries them out in order.

**Q2 — B.** `python hello.py` hands the file to the Python interpreter to run.

**Q3 — C.** `print(...)` displays its contents as output in the Terminal.

**Q4 — B.** Everything after `#` on a line is a comment, which Python ignores.

**Q5 — B.** No `(.venv)` means the virtual environment isn't active. Activate it from
the course folder. (See SETUP.md, Step 4.)

**Q6 — B.** The REPL runs one line at a time and forgets when closed — ideal for quick
experiments, not for saving real programs.
