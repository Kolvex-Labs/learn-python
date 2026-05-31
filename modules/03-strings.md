# Module 03 — Strings in Depth

## What you'll learn

- How to reach individual characters with indexing, including from the end
- How to pull out a piece of a string with slicing
- How to measure a string's length with `len()`
- The everyday string methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`,
  `.split()`, `.count()`
- A quick recap of f-strings for building messages

---

## The concept

A **string** is text: a row of characters in order, like `"hello"`. Because the
characters sit in a fixed order, you can point at any one of them by its position.

### Indexing: reaching one character

Each character has an **index**, a position number. Python counts from **0**, not 1. So
the first character is at index `0`:

```
 h  e  l  l  o
 0  1  2  3  4
```

You grab a character with square brackets:

```python
text = "hello"
text[0]    # 'h'
text[1]    # 'e'
```

### Negative indexing: counting from the end

A negative index counts backward from the end. `-1` is the last character, `-2` the one
before it. This saves you from doing math to find the end:

```python
text = "hello"
text[-1]   # 'o'  <- last character
text[-2]   # 'l'
```

### Slicing: pulling out a piece

A **slice** grabs a range of characters. The form is `text[start:stop]`. It starts at
`start` and stops *just before* `stop` — the stop position is not included:

```python
text = "hello"
text[1:4]   # 'ell'   <- characters at index 1, 2, 3 (not 4)
text[:3]    # 'hel'   <- leave start blank to begin at 0
text[2:]    # 'llo'   <- leave stop blank to run to the end
```

The "stop is not included" rule trips everyone up at first. `text[1:4]` gives you three
characters, indices 1, 2, and 3. A useful check: the length of the slice is
`stop - start`.

### Length

`len(text)` tells you how many characters are in the string:

```python
len("hello")   # 5
len("")        # 0   <- the empty string has length 0
```

### Methods: actions a string can do

A **method** is a function attached to a value. You call it with a dot and parentheses:
`text.upper()`. Here are the ones you'll reach for constantly:

| Method | Does | Example | Result |
|--------|------|---------|--------|
| `.upper()` | make uppercase | `"hi".upper()` | `"HI"` |
| `.lower()` | make lowercase | `"HI".lower()` | `"hi"` |
| `.strip()` | trim spaces from both ends | `"  hi  ".strip()` | `"hi"` |
| `.replace(a, b)` | swap every `a` for `b` | `"aaa".replace("a", "b")` | `"bbb"` |
| `.split()` | break into a list of words | `"a b c".split()` | `["a", "b", "c"]` |
| `.count(x)` | how many times `x` appears | `"banana".count("a")` | `3` |

One thing to know: **strings never change in place.** A method like `.upper()` doesn't
edit the original; it *returns a new string*. So you keep the result:

```python
name = "mason"
name.upper()          # returns "MASON" but does NOT change name
print(name)           # mason   <- unchanged!
name = name.upper()   # now keep it
print(name)           # MASON
```

### f-strings recap

From Module 01: put `f` before the quote and wrap a value in `{braces}` to drop it into
text. Combine this with what's above:

```python
word = "hello"
print(f"{word} has {len(word)} letters and starts with {word[0]}.")
# hello has 5 letters and starts with h.
```

---

## Show me

### Indexing and slicing

```python
text = "Python"
print(text[0])      # P
print(text[-1])     # n
print(text[0:3])    # Pyt
print(text[3:])     # hon
print(len(text))    # 6
```

### Methods that transform text

```python
print("hello".upper())          # HELLO
print("LOUD".lower())           # loud
print("  spaces  ".strip())     # spaces
print("cat".replace("c", "b"))  # bat
```

### Splitting and counting

```python
print("ada lovelace".split())   # ['ada', 'lovelace']
print("banana".count("a"))      # 3
print("banana".count("na"))     # 2
```

### Building an initials string

```python
full_name = "ada lovelace"
words = full_name.split()       # ['ada', 'lovelace']
first = words[0][0]             # 'a'  <- first word, first letter
print(first.upper())            # A
```

---

## Common mistakes

- **Off-by-one with slicing.** `text[1:4]` does *not* include index 4. It gives indices
  1, 2, and 3. The stop number is where Python stops, not the last character it keeps.
- **Expecting a method to change the string.** `name.upper()` returns a new string and
  leaves `name` alone. You have to save it: `name = name.upper()`.
- **Reading an index that doesn't exist.** `"hi"[5]` crashes with an `IndexError`
  because there's no character at position 5. Valid indices for `"hi"` are 0 and 1 (and
  -1, -2).

---

## Try it

Open **`labs/03-strings/`** and read its `README.md`. You'll complete the functions in
`strings.py`, then run:

```bash
pytest labs/03-strings/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What does `"hello"[0]` return?
- A) `"e"`
- B) `"h"`
- C) `"o"`
- D) `1`

**Q2.** What does `"hello"[-1]` return?
- A) `"h"`
- B) `"l"`
- C) `"o"`
- D) An error

**Q3.** What does `"python"[1:4]` return?
- A) `"yth"`
- B) `"ytho"`
- C) `"pyth"`
- D) `" python"`

**Q4.** What is `len("cat")`?
- A) `2`
- B) `3`
- C) `4`
- D) `1`

**Q5.** What does `"Hi".upper()` return?
- A) `"hi"`
- B) `"HI"`
- C) `"Hi"`
- D) It changes `"Hi"` in place and returns nothing

**Q6.** What does `"a-b-c".split("-")` return?
- A) `"abc"`
- B) `["a", "b", "c"]`
- C) `["a-b-c"]`
- D) `"a b c"`

**Q7.** What does `"banana".count("a")` return?
- A) `2`
- B) `3`
- C) `6`
- D) `1`

**Q8.** After `name = "sam"` and then `name.upper()`, what does `print(name)` show?
- A) `SAM`
- B) `sam`
- C) `Sam`
- D) An error

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** Python counts from 0, so index 0 is the first character, `"h"`.

**Q2 — C.** A negative index counts from the end; `-1` is the last character, `"o"`.

**Q3 — A.** A slice stops just before the stop index, so `[1:4]` gives indices 1, 2, 3
of `"python"`, which are `y`, `t`, `h`: `"yth"`.

**Q4 — B.** `"cat"` has three characters, so `len` is `3`.

**Q5 — B.** `.upper()` returns a new uppercase string, `"HI"`.

**Q6 — B.** `.split("-")` breaks the string at each `-`, giving a list of the pieces.

**Q7 — B.** The letter `a` appears three times in `"banana"`.

**Q8 — B.** `.upper()` returns a new string but doesn't change `name`, so it's still
`"sam"`. You'd need `name = name.upper()` to keep the change.
