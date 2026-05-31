# Lab 14 — Automation

**Module:** 14 — Automation Track

## Goal

Practice the real building blocks of a file-organizing script: listing files, moving them
into folders, and renaming them in bulk, all with predictable, sorted behavior.

## Your task

Open **`automation.py`**. It has three functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `find_files(folder, suffix)` — return a **sorted** list of `Path` objects for the
   top-level files whose name ends with `suffix` (e.g. `".txt"`). Skip subfolders.
2. `organize_by_extension(folder)` — move each top-level file into a subfolder named after
   its extension without the dot (`report.txt` → `folder/txt/report.txt`). Create
   subfolders as needed. Return a dict like `{"txt": 2, "jpg": 1}`.
3. `bulk_rename(folder, prefix)` — rename the top-level files (in sorted order by name) to
   `prefix_1`, `prefix_2`, ... keeping each file's original extension. Return how many
   you renamed.

The tests build a temporary folder for you with the `tmp_path` fixture, so your own files
are never touched.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/14-automation/
```

- **Green** → all three work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `automation.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `automation_solution.py` as a last resort.
