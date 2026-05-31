# Lab 10 — Files

**Module:** 10 — Files & the Filesystem

## Goal

Practice reading from and writing to files with the `with open(...) as f:` pattern,
including the write, read, and append modes.

## Your task

Open **`files_lab.py`**. It has four functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `write_lines(path, lines)` — write each string in `lines` as its own line (each ending
   in a newline). Overwrite the file if it already exists.
2. `read_lines(path)` — return a list of the file's lines with the trailing newlines
   removed.
3. `count_lines(path)` — return the number of lines in the file.
4. `append_line(path, line)` — add `line` (plus a newline) to the end of the file without
   erasing what's there.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/10-files/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `files_lab.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `files_lab_solution.py` as a last resort.
