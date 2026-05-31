"""Lab 12 — Working with Data Formats: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""
import csv
import json


def to_json(obj):
    """Return `obj` converted to a JSON string."""
    return json.dumps(obj)


def from_json(text):
    """Return the Python object described by the JSON string `text`."""
    return json.loads(text)


def write_csv(path, header, rows):
    """Write a CSV file at `path`: `header` as the first row, then each list in `rows`."""
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in rows:
            writer.writerow(row)


def read_csv(path):
    """Return a list of dicts, one per data row, keyed by the header."""
    with open(path, "r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)
