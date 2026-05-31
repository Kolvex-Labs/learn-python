# Module 07 — Dictionaries & Sets

## What you'll learn

- How to store labeled values in a dictionary and look them up by key
- How to read safely with `.get`, and how to add or update entries
- How to loop over a dictionary's keys, values, and items
- How to check if a key is present with `in`
- What a set is, and when a dictionary beats a set (and the other way around)

---

## The concept

A **dictionary** (or **dict**) stores values you look up by a label instead of by a
position. The label is called a **key**, and the thing it points to is the **value**.
Together they make a **key-value pair**. You write a dict with curly braces `{ }`, a
colon between each key and value, and commas between pairs:

```python
ages = {"Sam": 9, "Alex": 30}
```

Here `"Sam"` and `"Alex"` are keys, and `9` and `30` are their values. You look up a
value by putting its key in square brackets:

```python
ages["Sam"]     # 9
ages["Alex"]   # 30
```

A list finds things by position (`scores[0]`). A dict finds things by name
(`ages["Sam"]`). Use a dict when each value has a natural label, like a person's name or
a product's id.

A **set** is a collection of **unique** values with **no order**. You make one with curly
braces too, but with only values, no colons:

```python
colors = {"red", "green", "red"}
print(colors)    # {"red", "green"}   <- the duplicate "red" is gone
```

A set automatically drops duplicates. That makes it the perfect tool for "how many
*different* things are here?" Sets have no positions, so you can't do `colors[0]`.

**Dict vs set, in one line:** use a dict when you need to look a value up *by a key*; use
a set when you only care about *which unique values exist*.

---

## Show me

### Creating and reading a dict

```python
prices = {"apple": 1.0, "banana": 0.5}

print(prices["apple"])    # 1.0
print(len(prices))        # 2   (number of pairs)
```

### Reading safely with `.get`

Looking up a key that isn't there with square brackets raises an error:

```python
prices["mango"]   # KeyError: 'mango'
```

`.get` avoids the crash. It returns the value if the key exists, or a default you choose
if it doesn't:

```python
print(prices.get("apple"))         # 1.0
print(prices.get("mango"))         # None        (missing, no default given)
print(prices.get("mango", 0))      # 0           (missing, default is 0)
```

### Adding and updating

Assigning to a key adds it if it's new, or replaces it if it already exists:

```python
prices = {"apple": 1.0}

prices["banana"] = 0.5      # add a new pair
print(prices)               # {'apple': 1.0, 'banana': 0.5}

prices["apple"] = 1.25      # update the existing key
print(prices)               # {'apple': 1.25, 'banana': 0.5}
```

### Looping over a dict

```python
prices = {"apple": 1.0, "banana": 0.5}

for fruit in prices.keys():       # just the keys
    print(fruit)                  # apple, then banana

for price in prices.values():     # just the values
    print(price)                  # 1.0, then 0.5

for fruit, price in prices.items():   # both at once
    print(f"{fruit} costs {price}")
# apple costs 1.0
# banana costs 0.5
```

`.items()` hands you each key-value pair, which you can unpack into two variables.

### Checking for a key with `in`

```python
prices = {"apple": 1.0}
print("apple" in prices)    # True
print("mango" in prices)    # False
```

`in` checks the **keys** of a dict.

### Sets and uniqueness

```python
nums = [1, 2, 2, 3, 3, 3]
unique = set(nums)
print(unique)         # {1, 2, 3}
print(len(unique))    # 3   (three distinct values)
```

`set(...)` turns any list into a set, dropping duplicates. To get a sorted list back,
wrap it in `sorted(...)`:

```python
print(sorted(set([3, 1, 2, 1])))   # [1, 2, 3]
```

---

## Common mistakes

- **Using `[]` on a missing key.** `prices["mango"]` raises `KeyError` if `"mango"`
  isn't there. When a key might be missing, use `prices.get("mango", default)` instead.
- **Thinking a set keeps order or positions.** A set has no index, so `colors[0]` raises
  a `TypeError`. If you need order, sort it into a list: `sorted(colors)`.
- **Mutating an input dict you meant to leave alone.** `merge` should return a *new*
  dict and not touch `d1` or `d2`. Build a fresh dict (start from a copy) instead of
  adding straight into `d1`.

---

## Try it

Open **`labs/07-dicts-sets/`** and read its `README.md`. You'll complete the functions
in `mappings.py`, then run:

```bash
pytest labs/07-dicts-sets/
```

Make it green before moving on.

---

## Check yourself

**Q1.** Given `ages = {"Sam": 9}`, what is `ages["Sam"]`?
- A) `"Sam"`
- B) `9`
- C) `{"Sam": 9}`
- D) An error

**Q2.** What does `ages.get("Ada", 0)` return when `"Ada"` is not a key?
- A) `"Ada"`
- B) `None`
- C) `0`
- D) A `KeyError`

**Q3.** What does `ages["Sam"]` raise if `"Sam"` is not in the dict?
- A) `None`
- B) `KeyError`
- C) `IndexError`
- D) `0`

**Q4.** After `d = {"a": 1}; d["a"] = 5`, what is `d`?
- A) `{"a": 1}`
- B) `{"a": 5}`
- C) `{"a": 1, "a": 5}`
- D) An error

**Q5.** What does `"a" in {"a": 1, "b": 2}` check?
- A) Whether `"a"` is a value
- B) Whether `"a"` is a key
- C) Whether the dict has 2 items
- D) Nothing useful

**Q6.** What is `set([1, 1, 2, 3, 3])`?
- A) `[1, 1, 2, 3, 3]`
- B) `{1, 2, 3}`
- C) `{1, 1, 2, 3, 3}`
- D) `3`

**Q7.** Which `for` loop gives you both the key and the value each time?
- A) `for k in d:`
- B) `for v in d.values():`
- C) `for k, v in d.items():`
- D) `for k in d.keys():`

**Q8.** You want to know how many *different* answers a survey got. Which tool fits best?
- A) A list
- B) A set
- C) A single variable
- D) A tuple

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** Looking up the key `"Sam"` returns its value, `9`.

**Q2 — C.** `.get` returns the default (`0`) when the key is missing, instead of raising.

**Q3 — B.** Square-bracket lookup on a missing key raises `KeyError`.

**Q4 — B.** Assigning to an existing key replaces its value, giving `{"a": 5}`.

**Q5 — B.** `in` on a dict checks the keys.

**Q6 — B.** A set drops duplicates and is written with braces: `{1, 2, 3}`.

**Q7 — C.** `.items()` yields each key-value pair, which you unpack into `k, v`.

**Q8 — B.** A set keeps only distinct values, so its length is the count of different
answers.
