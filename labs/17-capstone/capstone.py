"""Lab 17 — Capstone Project.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/17-capstone/` to check your work.

This ties the whole part together: fetch (here, load from a JSON file), process the
records, and write a CSV report. Each order is a dict shaped like:
    {"id": 1, "category": "books", "amount": 12.99}
JSON keeps number types, so "amount" is already a float. No text conversion needed.
"""
import csv
import json


def load_orders(path):
    """Load the JSON file at `path` and return the list of order dicts."""
    # TODO: open(path), json.load(f), and return the result.
    raise NotImplementedError("Complete load_orders()")


def total_by_category(orders):
    """Return a dict mapping each category -> the total amount for that category (float)."""
    # TODO: walk the orders, adding each order["amount"] into a dict keyed by
    #       order["category"]. Hint: totals.get(category, 0) + order["amount"].
    raise NotImplementedError("Complete total_by_category()")


def summary(orders):
    """Return a dict with:
        "count"      -> the number of orders (int)
        "total"      -> the sum of all amounts (float)
        "categories" -> a sorted list of the distinct category names
    """
    # TODO: build and return that dict. For categories, collect a set of
    #       order["category"] values and wrap it in sorted(...).
    raise NotImplementedError("Complete summary()")


def write_report(path, orders):
    """Write a CSV at `path` with header `category,total` and one row per category
    (categories sorted alphabetically) with its total amount. Return the number of
    category rows written (not counting the header)."""
    # TODO: compute totals with total_by_category. Open(path, "w", newline=""),
    #       make a csv.writer, write the header row ["category", "total"], then for
    #       each category in sorted(totals) write [category, totals[category]].
    #       Return how many category rows you wrote.
    raise NotImplementedError("Complete write_report()")
