# Module 09 — Errors & Exceptions

## What you'll learn

- What a traceback is and how to read it from the bottom up
- The common exceptions you'll meet and what each one means
- How to catch an error with `try` / `except` so your program keeps going
- How `else` and `finally` round out a `try` block
- How to raise your own error with `raise`

---

## The concept

When Python hits a problem it can't handle, it stops and reports an **exception**: an
error with a name and a message. You've already met a few. An exception isn't a bug in
Python; it's Python telling you something went wrong and exactly where.

The report Python prints is called a **traceback**. It can look scary, but it's just a
trail showing how Python got to the problem. **Read it from the bottom up.** The last
line is the most useful: it names the exception and describes it.

```
Traceback (most recent call last):
  File "app.py", line 3, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero
```

The bottom line says `ZeroDivisionError: division by zero`. That's your answer: you
divided by zero on line 3. Start at the bottom, then look up only if you need more
context.

### Common exceptions

You'll see these again and again:

| Exception | Happens when... | Example |
|-----------|-----------------|---------|
| `ValueError` | the value is the wrong *kind* for the operation | `int("hello")` |
| `TypeError` | the *type* is wrong | `"a" + 5` |
| `IndexError` | a list index is out of range | `[1, 2][5]` |
| `KeyError` | a dict key doesn't exist | `{"a": 1}["b"]` |
| `ZeroDivisionError` | you divide by zero | `10 / 0` |

Knowing the name tells you what to fix.

---

## Show me

### try / except: catch a problem and keep going

A `try` block holds code that might fail. The `except` block runs only if that failure
happens, instead of crashing the program:

```python
try:
    number = int("hello")
except ValueError:
    number = 0

print(number)    # 0
```

Python tries `int("hello")`, which raises `ValueError`. The `except ValueError` catches
it and sets `number = 0`. The program keeps running.

### Catch a *specific* exception

Name the exception you expect. That way you don't accidentally hide a different problem:

```python
try:
    value = my_list[index]
except IndexError:
    value = None
```

This catches an out-of-range index but lets other, unexpected errors surface normally.
Catching the specific exception is better than a bare `except:` that swallows everything.

### try / except / else / finally

- `else` runs if the `try` block had **no** error.
- `finally` runs **no matter what**, error or not. It's for cleanup.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print(f"result is {result}")    # result is 5.0
finally:
    print("done")                   # done
```

With no error, you'll see `result is 5.0` then `done`. If the division had failed, you'd
see the error message then `done`. `finally` always runs.

### Raising your own error

Sometimes *your* code should refuse bad input. You signal that with `raise`, choosing the
exception type and message:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b

divide(10, 0)    # ValueError: cannot divide by zero
```

`raise` stops the function and reports the exception, just like a built-in one would. The
caller can then catch it with `try` / `except` if they choose.

---

## Common mistakes

- **Panicking at the traceback instead of reading the bottom line.** The last line names
  the exact problem. Read bottom-up; the rest is just the path Python took to get there.
- **Catching everything with a bare `except:`.** `except:` hides real bugs because it
  swallows every error, even ones you didn't expect. Catch the specific type, like
  `except ValueError:`, so surprises still show up.
- **Forgetting that `int("12.5")` raises `ValueError`.** Only whole-number text converts
  cleanly with `int`. `int("12.5")` fails. Wrap the conversion in `try` / `except
  ValueError` when the text might not be a clean integer.

---

## Try it

Open **`labs/09-errors/`** and read its `README.md`. You'll complete the functions in
`errors.py`, then run:

```bash
pytest labs/09-errors/
```

Make it green before moving on.

---

## Check yourself

**Q1.** When reading a traceback, which line is usually the most useful?
- A) The first line
- B) The middle line
- C) The last (bottom) line
- D) None of them

**Q2.** Which exception does `int("hello")` raise?
- A) `TypeError`
- B) `ValueError`
- C) `KeyError`
- D) `IndexError`

**Q3.** Which exception does `{"a": 1}["b"]` raise?
- A) `IndexError`
- B) `ValueError`
- C) `KeyError`
- D) `ZeroDivisionError`

**Q4.** What does `10 / 0` raise?
- A) `ValueError`
- B) `ZeroDivisionError`
- C) `TypeError`
- D) Nothing, it returns 0

**Q5.** In a `try` block, when does the `except` block run?
- A) Always
- B) Only if the `try` block raises a matching exception
- C) Only if the `try` block succeeds
- D) Never

**Q6.** When does a `finally` block run?
- A) Only on success
- B) Only on error
- C) No matter what, error or not
- D) Only if there's no `except`

**Q7.** What does `raise ValueError("nope")` do?
- A) Prints "nope" and continues
- B) Stops and reports a `ValueError` with the message "nope"
- C) Returns "nope"
- D) Nothing

**Q8.** Why prefer `except ValueError:` over a bare `except:`?
- A) It's shorter
- B) It catches more errors
- C) It catches only the error you expect, so other bugs still surface
- D) It runs faster

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — C.** Read tracebacks bottom-up; the last line names the exception and its message.

**Q2 — B.** `int("hello")` can't become a number, so it raises `ValueError`.

**Q3 — C.** Looking up a missing dict key raises `KeyError`.

**Q4 — B.** Dividing by zero raises `ZeroDivisionError`.

**Q5 — B.** `except` runs only when the `try` block raises a matching exception.

**Q6 — C.** `finally` always runs, whether or not an error happened. It's for cleanup.

**Q7 — B.** `raise` stops execution and reports the chosen exception and message.

**Q8 — C.** Catching the specific exception leaves unexpected errors visible instead of
silently swallowing them.
