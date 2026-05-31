"""Lab 16 — Data & Analysis: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""
import csv
import statistics


def load_rows(path):
    """Read the CSV at `path` and return a list of dicts, one per data row."""
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def total_sales(rows):
    """Return the sum of float(row["amount"]) over all rows (a float)."""
    return sum(float(row["amount"]) for row in rows)


def average_sale(rows):
    """Return statistics.mean of the amounts (a float)."""
    amounts = [float(row["amount"]) for row in rows]
    return statistics.mean(amounts)


def sales_by_product(rows):
    """Return a dict mapping each product name -> its total amount (a float)."""
    totals = {}
    for row in rows:
        product = row["product"]
        amount = float(row["amount"])
        totals[product] = totals.get(product, 0) + amount
    return totals


def top_product(rows):
    """Return the product name with the highest total amount."""
    totals = sales_by_product(rows)
    return max(totals, key=totals.get)
