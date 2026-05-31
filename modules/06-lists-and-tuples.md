# Module 06 — Lists & Tuples

## What you'll learn

- How to build a list and reach individual items by their position (index)
- How to grow and shrink a list with `append`, `insert`, `remove`, and `pop`
- How to count items, loop over them, and slice out a piece
- How to check if something is in a list with `in`
- What a tuple is, why it can't change, and how tuple unpacking works
- A first taste of list comprehensions

---

## The concept

A **list** is an ordered collection of values held in one variable. Instead of ten
separate variables for ten scores, you keep them in one list. You make a list with
square brackets `[ ]`, separating items with commas:

```python
scores = [90, 85, 72, 100]
names = ["Sam", "Alex", "Ada"]
```

A list keeps its items **in order**, and that order matters. Each item has an **index**,
which is its position. Python counts positions starting at **0**, not 1. So in
`names = ["Sam", "Alex", "Ada"]`, `"Sam"` is at index 0, `"Alex"` at index 1, and
`"Ada"` at index 2.

You reach an item by putting its index in square brackets:

```python
names[0]    # "Sam"
names[1]    # "Alex"
names[-1]   # "Ada"   <- negative counts from the end; -1 is the last item
```

Lists can **change**. You can add items, remove items, and replace items. This is called
being **mutable** ("able to be changed").

A **tuple** is like a list that can never change. You make one with parentheses `( )`:

```python
point = (3, 4)
```

Once a tuple exists, you cannot add to it, remove from it, or replace an item. This is
called being **immutable** ("not able to be changed"). Tuples are handy when a group of
values belongs together and shouldn't be edited, like a pair of coordinates.

You still read tuple items by index, exactly like a list:

```python
point[0]   # 3
point[1]   # 4
```

---

## Show me

### Building a list and reaching items

```python
fruits = ["apple", "banana", "cherry"]

print(fruits[0])     # apple
print(fruits[2])     # cherry
print(fruits[-1])    # cherry   (last item)
print(len(fruits))   # 3        (len = how many items)
```

`len(...)` tells you how many items a list holds.

### Changing a list

```python
fruits = ["apple", "banana"]

fruits.append("cherry")     # add to the end
print(fruits)               # ['apple', 'banana', 'cherry']

fruits.insert(0, "kiwi")    # put "kiwi" at index 0
print(fruits)               # ['kiwi', 'apple', 'banana', 'cherry']

fruits.remove("banana")     # remove the first "banana"
print(fruits)               # ['kiwi', 'apple', 'cherry']

last = fruits.pop()         # remove AND return the last item
print(last)                 # cherry
print(fruits)               # ['kiwi', 'apple']
```

`append` adds to the end. `insert` adds at a position. `remove` deletes by value.
`pop` deletes by position and hands you the value it removed (the end, if you don't
say where).

### Looping over a list

```python
scores = [90, 85, 100]
for score in scores:
    print(score)
# 90
# 85
# 100
```

Each time around, `score` becomes the next item.

### Slicing: grabbing a piece

A **slice** copies part of a list. The form is `list[start:stop]`. It starts at `start`
and stops **just before** `stop`:

```python
letters = ["a", "b", "c", "d", "e"]
print(letters[1:3])   # ['b', 'c']   (index 1 and 2, not 3)
print(letters[:2])    # ['a', 'b']   (from the start)
print(letters[2:])    # ['c', 'd', 'e']  (to the end)
```

### Checking membership with `in`

```python
fruits = ["apple", "banana"]
print("apple" in fruits)    # True
print("mango" in fruits)    # False
```

### Tuples and unpacking

A tuple groups values that travel together. You can pull them apart into separate
variables in one line. This is **tuple unpacking**:

```python
pair = (3, 4)
x, y = pair        # x gets 3, y gets 4
print(x)           # 3
print(y)           # 4
```

The number of names on the left must match the number of items in the tuple.

### A gentle intro to list comprehensions

A **list comprehension** builds a new list in one line. Read it as "give me `expression`
for each `item` in the list":

```python
numbers = [1, 2, 3, 4]
doubled = [n * 2 for n in numbers]
print(doubled)     # [2, 4, 6, 8]
```

You can add a condition with `if` to keep only some items:

```python
numbers = [1, 2, 3, 4]
evens = [n for n in numbers if n % 2 == 0]
print(evens)       # [2, 4]
```

That last line reads: "keep `n` for each `n` in numbers where `n` is even." You'll use
this exact pattern in the lab.

---

## Common mistakes

- **Counting from 1 instead of 0.** The first item is `list[0]`, not `list[1]`. Asking
  for `list[3]` of a 3-item list raises `IndexError: list index out of range`, because
  the valid indexes are 0, 1, and 2.
- **Trying to change a tuple.** `point = (3, 4)` then `point[0] = 9` raises
  `TypeError: 'tuple' object does not support item assignment`. Tuples never change.
  If you need to change it, use a list instead.
- **Mutating a list when you meant to copy it.** `reverse_list` should return a *new*
  list and leave the original alone. `items.reverse()` flips the original in place,
  which is not what you want here. Use `items[::-1]` or `list(reversed(items))` to make
  a fresh, reversed copy.

---

## Try it

Open **`labs/06-lists-tuples/`** and read its `README.md`. You'll complete the functions
in `sequences.py`, then run:

```bash
pytest labs/06-lists-tuples/
```

Make it green before moving on.

---

## Check yourself

**Q1.** Given `colors = ["red", "green", "blue"]`, what is `colors[1]`?
- A) `"red"`
- B) `"green"`
- C) `"blue"`
- D) An error

**Q2.** What does `colors[-1]` give for that same list?
- A) `"red"`
- B) `"green"`
- C) `"blue"`
- D) An error

**Q3.** After `nums = [1, 2]; nums.append(3)`, what is `nums`?
- A) `[1, 2]`
- B) `[3, 1, 2]`
- C) `[1, 2, 3]`
- D) `[1, 3, 2]`

**Q4.** What does `len([10, 20, 30])` return?
- A) `2`
- B) `3`
- C) `30`
- D) `60`

**Q5.** What is `["a", "b", "c", "d"][1:3]`?
- A) `["a", "b"]`
- B) `["b", "c"]`
- C) `["b", "c", "d"]`
- D) `["a", "b", "c"]`

**Q6.** Why does `point = (3, 4); point[0] = 9` raise an error?
- A) `point` has too many items
- B) Tuples are immutable and can't be changed
- C) `9` is not a valid number
- D) You can't index a tuple

**Q7.** After `a, b = (5, 8)`, what is `b`?
- A) `5`
- B) `8`
- C) `(5, 8)`
- D) An error

**Q8.** What does `[n for n in [1, 2, 3, 4] if n % 2 == 0]` produce?
- A) `[1, 3]`
- B) `[2, 4]`
- C) `[1, 2, 3, 4]`
- D) `[]`

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** Indexes start at 0, so index 1 is the second item, `"green"`.

**Q2 — C.** A negative index counts from the end; `-1` is the last item, `"blue"`.

**Q3 — C.** `append` adds to the end, giving `[1, 2, 3]`.

**Q4 — B.** `len` returns the number of items, which is 3.

**Q5 — B.** A slice starts at `start` and stops just before `stop`, so `[1:3]` is
indexes 1 and 2: `["b", "c"]`.

**Q6 — B.** Tuples are immutable. Assigning to an item raises a `TypeError`.

**Q7 — B.** Tuple unpacking matches by position: `a` gets 5, `b` gets 8.

**Q8 — B.** The comprehension keeps only even numbers, giving `[2, 4]`.
