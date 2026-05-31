"""Lab 17 — Capstone Project: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""
import csv
import json


def load_orders(path):
    """Load the JSON file at `path` and return the list of order dicts."""
    with open(path) as f:
        return json.load(f)


def total_by_category(orders):
    """Return a dict mapping each category -> the total amount for that category (float)."""
    totals = {}
    for order in orders:
        category = order["category"]
        totals[category] = totals.get(category, 0) + order["amount"]
    return totals


def summary(orders):
    """Return count, total, and a sorted list of distinct categories."""
    return {
        "count": len(orders),
        "total": sum(order["amount"] for order in orders),
        "categories": sorted({order["category"] for order in orders}),
    }


def write_report(path, orders):
    """Write a CSV at `path` with header `category,total` and one row per category
    (sorted alphabetically). Return the number of category rows written."""
    totals = total_by_category(orders)
    rows_written = 0
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["category", "total"])
        for category in sorted(totals):
            writer.writerow([category, totals[category]])
            rows_written += 1
    return rows_written
