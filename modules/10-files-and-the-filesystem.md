# Module 10 — Files & the Filesystem

## What you'll learn

- How to open a file with `open()` and what the modes `r`, `w`, and `a` mean
- The `with open(...) as f:` pattern, and why it's the safe way to work with files
- How to read a file three ways: `read()`, `readlines()`, and looping over lines
- How to write to a file, and how newline characters (`\n`) actually work
- The basics of `pathlib.Path` for reading and writing files in one short line

---

## The concept

A **file** is data saved on disk so it survives after your program ends. Your variables
vanish when the program stops. A file stays. Reading a file pulls its contents into your
program; writing a file puts your program's data onto disk.

To work with a file, you first **open** it. `open()` gives you a *file object* — a handle
you use to read or write. When you're done, the file must be **closed** so the system
frees it and your writes are actually saved.

### Modes: what you plan to do with the file

When you open a file you pass a **mode**, a short string that says what you intend:

| Mode | Means | If the file exists | If it doesn't |
|------|-------|--------------------|---------------|
| `"r"` | read | reads it | error |
| `"w"` | write | **erases it first**, then writes | creates it |
| `"a"` | append | adds to the end | creates it |

The big one to respect is `"w"`. It wipes the file the moment you open it. If you want to
add to a file without destroying what's there, use `"a"`.

### The `with` pattern: open and auto-close

You *could* call `f.close()` yourself, but it's easy to forget, and if your code crashes
before reaching it, the file stays open. So Python gives you a cleaner way: the **`with`
statement**. It closes the file for you automatically, even if something goes wrong.

```python
with open("notes.txt", "r") as f:
    text = f.read()
# the file is closed here, automatically
```

Read it as: "open notes.txt as `f`, do the indented work, then close it." This is the
standard way to handle files. Use it every time.

### Reading: three ways

Once a file is open for reading, you have choices:

- `f.read()` — the **whole file** as one big string.
- `f.readlines()` — a **list of lines**, each line still carrying its `\n`.
- looping `for line in f:` — one line at a time, easy on memory for big files.

### Newlines: the invisible character

A text file is just characters. The thing that ends one line and starts the next is a
single character written `\n`, the **newline**. You usually don't see it, but it's there.
When you write lines yourself, *you* add the `\n`:

```python
f.write("first\n")
f.write("second\n")
```

That makes a file with two lines. Without the `\n`, both pieces land on the same line.

### pathlib: the modern, shorter way

`pathlib.Path` represents a file or folder path as an object with handy methods. For
simple read-and-write jobs it's shorter than `open()` and harder to get wrong:

```python
from pathlib import Path

p = Path("notes.txt")
p.write_text("hello\n")        # writes the whole string (creates/overwrites)
contents = p.read_text()       # reads the whole file as a string
p.exists()                     # True if the file is there, else False
```

`write_text` and `read_text` open, do the work, and close the file for you in one call.
Prefer `with open(...)` when you need line-by-line control, and `Path` for quick whole-file
reads and writes.

---

## Show me

### Writing a file, then reading it back

```python
with open("greeting.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")

with open("greeting.txt", "r") as f:
    print(f.read())
# Hello
# World
#
```

(The blank line at the end is the trailing `\n` after `World`.)

### Reading line by line

```python
with open("greeting.txt", "r") as f:
    for line in f:
        print(line.strip())
# Hello
# World
```

`line.strip()` removes the trailing `\n` (and any stray spaces) so the print is clean.

### Appending without erasing

```python
with open("greeting.txt", "a") as f:
    f.write("Again\n")

with open("greeting.txt", "r") as f:
    print(f.read())
# Hello
# World
# Again
#
```

The original two lines stayed; `"a"` added to the end.

### pathlib in one line each

```python
from pathlib import Path

p = Path("quick.txt")
p.write_text("one line\n")
print(p.read_text())     # one line
print(p.exists())        # True
```

---

## Common mistakes

- **Opening with `"w"` when you meant `"a"`.** `"w"` erases the file the instant you open
  it. If your saved data keeps disappearing, you probably used write mode where you wanted
  append mode. Use `"a"` to add to the end.
- **Forgetting the `\n`.** `f.write("a")` then `f.write("b")` gives one line, `ab`. To get
  separate lines, write `"a\n"` and `"b\n"`. The newline is your job.
- **Forgetting to close (so writes don't save).** If you open without `with` and never
  call `f.close()`, your writes may not reach the disk. Use `with open(...) as f:` and the
  closing is handled for you.

---

## Try it

Open **`labs/10-files/`** and read its `README.md`. You'll complete the functions in
`files_lab.py`, then run:

```bash
pytest labs/10-files/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What does opening a file in `"w"` mode do to an existing file?
- A) Adds to the end of it
- B) Erases its contents first, then writes
- C) Reads it
- D) Leaves it untouched and raises an error

**Q2.** Why is `with open(...) as f:` preferred over a plain `open()`?
- A) It runs faster
- B) It closes the file automatically, even if an error happens
- C) It encrypts the file
- D) It allows reading and writing at the same time

**Q3.** Which character marks the end of a line in a text file?
- A) `\t`
- B) `\n`
- C) `\end`
- D) A space

**Q4.** What does `f.readlines()` return?
- A) The whole file as one string
- B) A list of lines, each still ending in `\n`
- C) The number of lines
- D) The first line only

**Q5.** Which mode adds to the end of a file without erasing it?
- A) `"r"`
- B) `"w"`
- C) `"a"`
- D) `"x"`

**Q6.** What does `Path("notes.txt").read_text()` do?
- A) Returns the whole file contents as a string
- B) Returns a list of lines
- C) Deletes the file
- D) Checks whether the file exists

**Q7.** After `f.write("a")` then `f.write("b")` (no newlines), what's in the file?
- A) `a` and `b` on two lines
- B) `ab` on one line
- C) `a b`
- D) Nothing

**Q8.** What does `Path("notes.txt").exists()` return when the file is missing?
- A) `None`
- B) An error
- C) `False`
- D) `""`

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** `"w"` truncates (erases) the file the moment it opens, then writes fresh.
Use `"a"` if you want to keep what's there.

**Q2 — B.** `with` guarantees the file is closed when the block ends, even if your code
raises an error partway through.

**Q3 — B.** `\n`, the newline character, ends one line and starts the next.

**Q4 — B.** `readlines()` gives you a list of the lines, and each one still carries its
trailing `\n`.

**Q5 — C.** `"a"` is append mode: it adds to the end and creates the file if it's missing.

**Q6 — A.** `read_text()` opens the file, reads all of it into one string, and closes it.

**Q7 — B.** Without `\n`, the two writes land on the same line as `ab`. The newline is
something you add yourself.

**Q8 — C.** `exists()` returns the boolean `False` when the path isn't there (and `True`
when it is).
