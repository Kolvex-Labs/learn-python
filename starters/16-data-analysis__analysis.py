"""Lab 16 — Data & Analysis.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/16-data-analysis/` to check your work.

You'll read a small sales CSV and pull real numbers out of it, using only the standard
library (csv and statistics). Each row looks like {"product": "Widget", "amount": "30.00"}.
Remember: the "amount" comes in as TEXT, so convert it with float(...) before doing math.
"""
import csv
import statistics


def load_rows(path):
    """Read the CSV at `path` and return a list of dicts, one per data row,
    using csv.DictReader (so each row is keyed by the header columns)."""
    # TODO: open(path, newline="") , wrap it in csv.DictReader, and return list(reader).
    raise NotImplementedError("Complete load_rows()")


def total_sales(rows):
    """Return the sum of float(row["amount"]) over all rows (a float)."""
    # TODO: convert each row's "amount" to a float and sum them.
    raise NotImplementedError("Complete total_sales()")


def average_sale(rows):
    """Return statistics.mean of the amounts (a float)."""
    # TODO: build a list of float(row["amount"]) and return statistics.mean(...) of it.
    raise NotImplementedError("Complete average_sale()")


def sales_by_product(rows):
    """Return a dict mapping each product name -> its total amount (a float)."""
    # TODO: walk the rows, and for each one add float(row["amount"]) into a dict
    #       bucket keyed by row["product"]. Hint: totals.get(product, 0) + amount.
    raise NotImplementedError("Complete sales_by_product()")


def top_product(rows):
    """Return the product name with the highest total amount."""
    # TODO: build the per-product totals (you can reuse sales_by_product) and return
    #       max(totals, key=totals.get).
    raise NotImplementedError("Complete top_product()")
