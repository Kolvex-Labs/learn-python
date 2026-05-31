"""Lab 14 — Automation: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""
import shutil
from pathlib import Path


def find_files(folder, suffix):
    """Return a SORTED list of Path objects for the top-level files in `folder`
    whose name ends with `suffix` (for example ".txt"). Skip subfolders."""
    matches = [
        p for p in Path(folder).iterdir()
        if p.is_file() and p.name.endswith(suffix)
    ]
    return sorted(matches)


def organize_by_extension(folder):
    """Move each top-level file into a subfolder named after its extension WITHOUT
    the dot (report.txt -> folder/txt/report.txt). Create subfolders as needed.
    Return a dict mapping {extension_without_dot: count of files moved there}."""
    folder = Path(folder)
    counts = {}
    files = sorted(p for p in folder.iterdir() if p.is_file())
    for file in files:
        ext = file.suffix.lstrip(".")
        destination_dir = folder / ext
        destination_dir.mkdir(exist_ok=True)
        shutil.move(str(file), str(destination_dir / file.name))
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def bulk_rename(folder, prefix):
    """Rename the top-level files (processed in sorted order by name) to
    f"{prefix}_1", f"{prefix}_2", ... keeping each file's original extension.
    Return the count of files renamed."""
    folder = Path(folder)
    files = sorted((p for p in folder.iterdir() if p.is_file()), key=lambda p: p.name)
    count = 0
    for index, file in enumerate(files, start=1):
        new_name = f"{prefix}_{index}{file.suffix}"
        file.rename(file.with_name(new_name))
        count += 1
    return count
