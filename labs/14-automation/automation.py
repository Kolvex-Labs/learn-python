"""Lab 14 — Automation.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/14-automation/` to check your work.

These functions work on a folder full of files. The tests build a temporary folder for
you, so you never touch your real files.
"""
import shutil
from pathlib import Path


def find_files(folder, suffix):
    """Return a SORTED list of Path objects for the top-level files in `folder`
    whose name ends with `suffix` (for example ".txt"). Skip subfolders."""
    # TODO: loop over folder.iterdir(), keep items that are files and end with suffix,
    #       and return them sorted. Hint: sorted(...) at the end.
    raise NotImplementedError("Complete find_files()")


def organize_by_extension(folder):
    """Move each top-level file into a subfolder named after its extension WITHOUT
    the dot (report.txt -> folder/txt/report.txt). Create subfolders as needed.
    Return a dict mapping {extension_without_dot: count of files moved there}."""
    # TODO: for each top-level file, work out its extension without the dot
    #       (Path.suffix gives ".txt"; drop the leading dot). Make folder/<ext>
    #       with mkdir(exist_ok=True), move the file in with shutil.move, and tally
    #       the count per extension in a dict. Process files in sorted order.
    raise NotImplementedError("Complete organize_by_extension()")


def bulk_rename(folder, prefix):
    """Rename the top-level files (processed in sorted order by name) to
    f"{prefix}_1", f"{prefix}_2", ... keeping each file's original extension.
    Return the count of files renamed."""
    # TODO: collect the top-level files sorted by name. Walk them with a counter
    #       starting at 1. Build the new name as f"{prefix}_{n}{file.suffix}" and
    #       rename with file.rename(file.with_name(new_name)). Return how many you renamed.
    raise NotImplementedError("Complete bulk_rename()")
