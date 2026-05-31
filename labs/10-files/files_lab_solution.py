"""Lab 10 — Files & the Filesystem: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""


def write_lines(path, lines):
    """Write each string in `lines` as its own line in the file at `path`."""
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def read_lines(path):
    """Return a list of the file's lines with trailing newlines removed."""
    with open(path, "r") as f:
        return [line.rstrip("\n") for line in f]


def count_lines(path):
    """Return the number of lines in the file at `path`."""
    with open(path, "r") as f:
        return len(f.readlines())


def append_line(path, line):
    """Append `line` (followed by a newline) to the end of the file at `path`."""
    with open(path, "a") as f:
        f.write(line + "\n")
