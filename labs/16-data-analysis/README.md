# Lab 16 — Data & Analysis

**Module:** 16 — Data & Analysis Track

## Goal

Practice turning a CSV into real answers using only the standard library: read the rows,
sum and average the numbers, group by product, and find the best seller.

## Your task

Open **`analysis.py`**. It has five functions with `# TODO` markers. Complete each one so
it does what its description says. Don't change the function names or their inputs — the
tests rely on them. Each row is a dict like `{"product": "Widget", "amount": "30.00"}`,
and remember the `"amount"` is **text** until you convert it with `float(...)`.

1. `load_rows(path)` — read the CSV with `csv.DictReader` and return a list of dicts.
2. `total_sales(rows)` — return the sum of all amounts (a float).
3. `average_sale(rows)` — return the average amount with `statistics.mean` (a float).
4. `sales_by_product(rows)` — return a dict mapping product → its total amount.
5. `top_product(rows)` — return the product name with the highest total.

The tests load the saved `sales.csv` from this folder, so they run instantly and offline.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/16-data-analysis/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `analysis.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `analysis_solution.py` as a last resort.
