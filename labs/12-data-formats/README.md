# Lab 12 — Data Formats

**Module:** 12 — Working with Data Formats

## Goal

Practice converting Python data to and from JSON, and writing and reading CSV files.

## Your task

Open **`dataio.py`**. It has four functions with `# TODO` markers. Add the imports you
need (`json`, `csv`) at the top, then complete each function. Don't change the function
names or their inputs — the tests rely on them.

1. `to_json(obj)` — return `obj` as a JSON string (`json.dumps`).
2. `from_json(text)` — return the Python object from a JSON string (`json.loads`).
3. `write_csv(path, header, rows)` — write a CSV file: `header` as the first row, then each
   list in `rows`. Open with `newline=""` and use `csv.writer`.
4. `read_csv(path)` — return a list of dicts, one per data row, keyed by the header
   (`csv.DictReader`).

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/12-data-formats/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `dataio.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `dataio_solution.py` as a last resort.
