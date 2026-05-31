"""Lab 12 — Working with Data Formats.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/12-data-formats/` to check your work.

Add the imports you need (`json`, `csv`) at the top of this file.
"""


def to_json(obj):
    """Return `obj` converted to a JSON string."""
    # TODO: import json, then return json.dumps(obj).
    raise NotImplementedError("Complete to_json()")


def from_json(text):
    """Return the Python object described by the JSON string `text`."""
    # TODO: return json.loads(text).
    raise NotImplementedError("Complete from_json()")


def write_csv(path, header, rows):
    """Write a CSV file at `path`: `header` as the first row, then each list in `rows`.

    Open the file with newline="" and use csv.writer.
    """
    # TODO: import csv. Open `path` for writing with newline="", make a csv.writer,
    # writerow(header), then writerow each row in `rows`.
    raise NotImplementedError("Complete write_csv()")


def read_csv(path):
    """Return a list of dicts, one per data row, keyed by the header.

    Use csv.DictReader.
    """
    # TODO: open `path` for reading with newline="", make a csv.DictReader, and
    # return a list of the rows (each row is already a dict).
    raise NotImplementedError("Complete read_csv()")
