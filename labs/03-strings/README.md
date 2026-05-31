# Lab 03 — Strings

**Module:** 03 — Strings in Depth

## Goal

Practice indexing, slicing, `len()`, and the common string methods.

## Your task

Open **`strings.py`**. It has five functions with `# TODO` markers. Complete each one so
it does what its description says. Don't change the function names or their inputs — the
tests rely on them.

1. `shout(text)` — return the text in upper case with a `"!"` added.
   (e.g. `shout("hi")` → `"HI!"`)
2. `initials(full_name)` — return the uppercase first letter of each word, joined.
   (e.g. `initials("ada lovelace")` → `"AL"`)
3. `last_char(text)` — return the last character. Hint: `text[-1]`.
   (e.g. `last_char("hello")` → `"o"`)
4. `count_letter(text, letter)` — return how many times `letter` appears in `text`.
   (e.g. `count_letter("banana", "a")` → `3`)
5. `is_palindrome(text)` — return `True` if the text reads the same forwards and
   backwards, ignoring case.
   (e.g. `is_palindrome("Level")` → `True`, `is_palindrome("hello")` → `False`)

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/03-strings/
```

- **Green** → all five work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix
  `strings.py` and run again.

## Stuck?

Ask the tutor agent for a hint, or open `strings_solution.py` as a last resort.
