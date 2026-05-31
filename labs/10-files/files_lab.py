"""Lab 10 — Files & the Filesystem.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/10-files/` to check your work.

Each function takes a `path` (a string or pathlib.Path). The tests pass a temporary
file path, so you never touch your real files.
"""


def write_lines(path, lines):
    """Write each string in `lines` as its own line in the file at `path`.

    Each line should end with a newline. Overwrite the file if it already exists.
    """
    # TODO: open `path` in write mode with `with open(...)`, then write each
    # item from `lines` followed by "\n".
    raise NotImplementedError("Complete write_lines()")


def read_lines(path):
    """Return a list of the file's lines with trailing newlines removed."""
    # TODO: open `path` in read mode, read the lines, and strip the trailing
    # newline from each. Return the resulting list of strings.
    raise NotImplementedError("Complete read_lines()")


def count_lines(path):
    """Return the number of lines in the file at `path`."""
    # TODO: count how many lines the file has and return that integer.
    raise NotImplementedError("Complete count_lines()")


def append_line(path, line):
    """Append `line` (followed by a newline) to the end of the file at `path`."""
    # TODO: open `path` in append mode and write `line` followed by "\n".
    raise NotImplementedError("Complete append_line()")
