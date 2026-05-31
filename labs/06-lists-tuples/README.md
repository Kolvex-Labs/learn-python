# Lab 06 — Lists & Tuples

**Module:** 06 — Lists & Tuples

## Goal

Practice working with lists: finding items, filtering, reversing without mutating,
indexing, and returning a tuple of results.

## Your task

Open **`sequences.py`**. It has five functions with `# TODO` markers. Complete each one
so it does what its description says. Don't change the function names or their inputs —
the tests rely on them.

1. `largest(numbers)` — return the largest number in the list, or `None` if the list is
   empty. (e.g. `largest([3, 7, 2])` → `7`; `largest([])` → `None`)
2. `evens(numbers)` — return a list of only the even numbers, in their original order.
   (e.g. `evens([1, 2, 3, 4])` → `[2, 4]`)
3. `reverse_list(items)` — return a **new** reversed list, leaving the input unchanged.
   (e.g. `reverse_list([1, 2, 3])` → `[3, 2, 1]`)
4. `second_item(items)` — return the item at index 1.
   (e.g. `second_item([10, 20, 30])` → `20`)
5. `total_and_count(numbers)` — return a tuple of `(sum, how_many)`.
   (e.g. `total_and_count([1, 2, 3])` → `(6, 3)`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/06-lists-tuples/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `sequences.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `sequences_solution.py` as a last resort.
