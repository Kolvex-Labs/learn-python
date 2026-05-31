# Module 14 — Automation Track

## What you'll learn

- How to look at the files inside a folder with `pathlib`
- How to make folders, move files, and rename files from code
- How to organize a messy folder by file type, the way a person would by hand
- Why sorting your results makes a script behave the same way every time

---

## The concept

**Automation means writing code to do the boring, repetitive jobs you'd otherwise do by
hand.** Dragging 200 downloaded files into folders. Renaming photos one by one.
Cleaning up a folder every Friday. A short script does it in a blink, the same way each
time, without getting bored or making a typo.

Python gives you three tools for this, and you'll use them together:

- **`pathlib`** — the modern way to talk about files and folders. A `Path` is just an
  object that points at a place on disk, like `Path("downloads/report.txt")`. You ask
  the path questions ("what's your name?", "are you a file?") and it answers.
- **`os`** — older, lower-level helpers for the operating system. You'll mostly reach
  for `pathlib` instead, but `os` is worth knowing exists.
- **`shutil`** — short for "shell utilities". It does the heavier file jobs like moving
  and copying.

A few words you'll see:

- **Path** — an object pointing at a file or folder. `Path("notes.txt")`.
- **Suffix** — the file extension, *with* the dot: `report.txt` has suffix `.txt`.
- **Top-level** — directly inside a folder, not buried in a subfolder.
- **`iterdir`** — "iterate the directory", meaning loop over everything inside a folder.

Think of a folder as a drawer full of loose papers. `iterdir` is you flipping through
them one at a time. `mkdir` is labeling a new drawer. `shutil.move` is dropping a paper
into the right drawer. That's the whole job.

### Why sorting matters

When you ask a folder for its contents, the operating system can hand them back in any
order. On your Mac today it might be alphabetical. On a server tomorrow it might not be.
If your script depends on the order, it will behave differently in different places, and
that is a nightmare to debug.

The fix is simple. **Sort your results before you use them.** Then your script does the
exact same thing every single time, everywhere. Tests love this too, because they can
predict the answer.

---

## Show me

### Looking inside a folder

```python
from pathlib import Path

folder = Path("downloads")

for item in sorted(folder.iterdir()):
    print(item.name)
# notes.txt
# photo.jpg
# report.txt
```

`folder.iterdir()` gives you every item directly inside `downloads`. Wrapping it in
`sorted(...)` puts them in a predictable order. `item.name` is just the filename, with
no folder in front.

### Finding only the files you want

A `Path` knows its own suffix (the extension, with the dot):

```python
from pathlib import Path

report = Path("downloads/report.txt")
print(report.suffix)   # .txt
print(report.name)     # report.txt
print(report.stem)     # report
```

So to collect every `.txt` file directly in a folder, sorted:

```python
from pathlib import Path

folder = Path("downloads")
texts = sorted(p for p in folder.iterdir() if p.is_file() and p.suffix == ".txt")
print(texts)
# [PosixPath('downloads/notes.txt'), PosixPath('downloads/report.txt')]
```

`p.is_file()` skips subfolders, so you only keep actual files.

### Making a folder and moving a file into it

```python
import shutil
from pathlib import Path

folder = Path("downloads")
subfolder = folder / "txt"        # the / builds a new path: downloads/txt
subfolder.mkdir(exist_ok=True)    # make it; exist_ok=True means "fine if it's already there"

source = folder / "report.txt"
shutil.move(str(source), str(subfolder / "report.txt"))
# report.txt now lives in downloads/txt/
```

Two things to notice. The `/` operator joins paths, so `folder / "txt"` means
`downloads/txt`. And `mkdir(exist_ok=True)` won't crash if the folder already exists,
which matters when you organize many files into the same subfolder.

### Renaming a file

```python
from pathlib import Path

old = Path("downloads/IMG_5523.jpg")
new = old.with_name("vacation_1.jpg")   # same folder, new name
old.rename(new)
```

`with_name(...)` keeps the file in the same folder but swaps the filename. `old.rename(new)`
does the actual rename on disk.

---

## Common mistakes

- **Forgetting to skip subfolders.** `folder.iterdir()` returns folders too, not just
  files. If you try to read or move a folder as if it were a file, things break. Guard
  with `if p.is_file()`.
- **Depending on the folder's order.** Without `sorted(...)`, the order your files come
  back in can change between computers, so your renamed files end up numbered
  differently. Always sort first when the order matters.
- **`mkdir` crashing on an existing folder.** Plain `subfolder.mkdir()` raises an error if
  the folder is already there. When you're organizing many files into the same `txt`
  folder, only the first one would succeed. Use `mkdir(exist_ok=True)`.

---

## Try it

Open **`labs/14-automation/`** and read its `README.md`. You'll complete the functions in
`automation.py`, then run:

```bash
pytest labs/14-automation/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What does `folder.iterdir()` give you?
- A) Only the `.txt` files in the folder
- B) Every item directly inside the folder, files and subfolders alike
- C) The folder's name as text
- D) A single combined string of all filenames

**Q2.** For the path `Path("photos/beach.jpg")`, what is its `.suffix`?
- A) `beach`
- B) `jpg`
- C) `.jpg`
- D) `photos`

**Q3.** Why should you wrap `folder.iterdir()` in `sorted(...)`?
- A) It makes the script run faster
- B) So results come back in the same predictable order every time
- C) It deletes duplicate files
- D) It is required or Python crashes

**Q4.** What does `folder / "txt"` produce?
- A) The division of two numbers
- B) A new path pointing at the `txt` subfolder inside `folder`
- C) An error, because you can't divide a path
- D) The text `"folder/txt"` with no special meaning

**Q5.** Why use `mkdir(exist_ok=True)` instead of plain `mkdir()`?
- A) It makes the folder hidden
- B) It won't raise an error if the folder already exists
- C) It creates the folder faster
- D) It deletes the folder first

**Q6.** Which check keeps you from treating a subfolder like a file?
- A) `p.is_file()`
- B) `p.sorted()`
- C) `p.exists() == False`
- D) `p.name()`

**Q7.** What does `shutil.move` do?
- A) Renames a file in place only
- B) Moves a file from one location to another
- C) Copies a file and keeps both
- D) Reads a file's contents

**Q8.** For `Path("downloads/report.txt")`, what is `.stem`?
- A) `report.txt`
- B) `report`
- C) `.txt`
- D) `downloads`

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** `iterdir()` yields every item directly inside the folder, including
subfolders, so you usually filter with `is_file()`.

**Q2 — C.** `.suffix` includes the dot, so it's `.jpg`. Without the dot you'd use `.suffix[1:]`.

**Q3 — B.** Folder order isn't guaranteed by the operating system. Sorting makes your
script deterministic everywhere.

**Q4 — B.** The `/` operator on a `Path` joins paths, giving `folder/txt`.

**Q5 — B.** `exist_ok=True` makes `mkdir` quietly succeed if the folder already exists,
which matters when many files share one destination folder.

**Q6 — A.** `p.is_file()` is `True` only for actual files, so it filters out subfolders.

**Q7 — B.** `shutil.move` relocates a file from a source path to a destination path.

**Q8 — B.** `.stem` is the name without the suffix, so `report`. `.name` would keep the
`.txt`.
</content>
</invoke>
