# Lab 17 — Capstone Project

**Module:** 17 — Capstone Project

## Goal

Build the whole pipeline end to end: load order records, total them by category,
summarize the dataset, and write a clean CSV report. This is the biggest lab and it ties
the automation, web/API, and data tracks together.

## Your task

Open **`capstone.py`**. It has four functions with `# TODO` markers. Complete each one so
it does what its description says. Don't change the function names or their inputs — the
tests rely on them. Each order is a dict like `{"id": 1, "category": "books", "amount": 12.99}`,
and because it comes from JSON the `"amount"` is already a `float`.

1. `load_orders(path)` — load the JSON file and return the list of order dicts.
2. `total_by_category(orders)` — return a dict mapping category → its total amount.
3. `summary(orders)` — return a dict with `"count"` (int), `"total"` (float), and
   `"categories"` (a sorted list of the distinct category names).
4. `write_report(path, orders)` — write a CSV with header `category,total` and one row per
   category (sorted alphabetically). Return the number of category rows written.

The read tests load the saved `orders.json` from this folder; the write test uses a
temporary folder. Everything runs offline.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/17-capstone/
```

- **Green** → all four work, and you've finished the course. Tick it off in `PROGRESS.md`.
- **Red** → read the message; it names the function and what it expected. Fix
  `capstone.py` and run again.

Want to see the pipeline hit a real API? If you're online, run
`python labs/17-capstone/live_demo.py`. It's optional and not graded.

## Stuck?

Ask the tutor agent for a hint, or open `capstone_solution.py` as a last resort.
