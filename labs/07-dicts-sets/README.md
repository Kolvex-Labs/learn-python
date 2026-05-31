# Lab 07 — Dictionaries & Sets

**Module:** 07 — Dictionaries & Sets

## Goal

Practice counting with dicts, looking up values safely, merging dicts without mutating
them, and using sets to find distinct values.

## Your task

Open **`mappings.py`**. It has five functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `word_count(text)` — return a dict mapping each lowercased word to its count (split
   on whitespace). (e.g. `word_count("the cat the dog")` → `{"the": 2, "cat": 1, "dog": 1}`)
2. `get_or_default(d, key, default)` — return `d[key]`, or `default` if the key is
   missing. (e.g. `get_or_default({"a": 1}, "b", 0)` → `0`)
3. `unique_sorted(items)` — return a sorted list of the distinct values.
   (e.g. `unique_sorted([3, 1, 2, 1])` → `[1, 2, 3]`)
4. `merge(d1, d2)` — return a **new** dict with both dicts' pairs; on a key conflict,
   `d2` wins. Don't change the inputs.
   (e.g. `merge({"a": 1, "b": 2}, {"b": 9})` → `{"a": 1, "b": 9}`)
5. `count_unique(items)` — return how many distinct values `items` has.
   (e.g. `count_unique([1, 1, 2, 3])` → `3`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/07-dicts-sets/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `mappings.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `mappings_solution.py` as a last resort.
