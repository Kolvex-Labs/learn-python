# Module 02 — Operators & Expressions

## What you'll learn

- The arithmetic operators and what each one does: `+ - * / // % **`
- How `/`, `//`, and `%` differ, and when you want each
- How to compare two values with `== != < > <= >=`
- How to combine true/false tests with `and`, `or`, and `not`
- The order Python uses when an expression has several operators

---

## The concept

An **operator** is a symbol that does something to values, like `+` for adding. The
values it works on are called **operands**. Put operators and values together and you
get an **expression** — a piece of code that produces a result.

```python
3 + 4      # an expression; its result is 7
```

### Arithmetic operators

These do math. Most look familiar from a calculator:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | add | `3 + 4` | `7` |
| `-` | subtract | `10 - 4` | `6` |
| `*` | multiply | `3 * 4` | `12` |
| `/` | divide | `7 / 2` | `3.5` |
| `//` | floor divide | `7 // 2` | `3` |
| `%` | remainder (modulo) | `7 % 2` | `1` |
| `**` | power | `2 ** 3` | `8` |

The three division operators are the part people mix up, so let's slow down.

- **`/` is regular division.** It always gives a `float` (a decimal), even when the
  numbers divide evenly. `8 / 2` is `4.0`, not `4`.
- **`//` is floor division.** It divides and throws away anything after the decimal
  point, giving the whole number underneath. `7 // 2` is `3`, because 2 goes into 7
  three full times.
- **`%` is the remainder** (its real name is *modulo*). It tells you what's left over
  after floor division. `7 % 2` is `1`, because 7 is 2×3 with 1 left over.

A clock helps. To turn 130 seconds into minutes and seconds: `130 // 60` is `2` whole
minutes, and `130 % 60` is `10` leftover seconds. So 130 seconds is 2 minutes and 10
seconds. You'll write exactly this in the lab.

One handy trick: `n % 2` is `0` for every even number and `1` for every odd one. That's
the standard way to test "is this even?"

### Comparison operators

These ask a yes/no question about two values and hand back a **bool** (`True` or
`False`):

| Operator | Asks | Example | Result |
|----------|------|---------|--------|
| `==` | are they equal? | `3 == 3` | `True` |
| `!=` | are they different? | `3 != 4` | `True` |
| `<` | is left smaller? | `3 < 4` | `True` |
| `>` | is left bigger? | `3 > 4` | `False` |
| `<=` | smaller or equal? | `3 <= 3` | `True` |
| `>=` | bigger or equal? | `4 >= 3` | `True` |

Note the doubled `==`. One `=` stores a value; two `==` *compare* values. Mixing them up
is one of the most common beginner bugs, so watch for it.

### Boolean operators

These combine true/false values:

- **`and`** is `True` only when *both* sides are true. `(age >= 18) and (age < 65)`
- **`or`** is `True` when *at least one* side is true. `is_weekend or is_holiday`
- **`not`** flips a value. `not True` is `False`.

### Operator precedence

When an expression mixes operators, Python follows an order, just like math class.
Power first, then multiply/divide, then add/subtract, then comparisons, then `not`, then
`and`, then `or`.

```python
2 + 3 * 4     # 14, not 20 — the * happens before the +
```

When in doubt, add parentheses. They force the order *and* make your code clearer:

```python
(2 + 3) * 4   # 20 — the parentheses go first
```

---

## Show me

### The three divisions side by side

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(8 / 2)    # 4.0   <- still a float, even though it's even
```

### Even or odd with the remainder

```python
print(10 % 2)   # 0   <- even
print(7 % 2)    # 1   <- odd
```

### Comparisons return True or False

```python
print(5 > 3)        # True
print(5 == 5)       # True
print(5 != 5)       # False
print(2 <= 2)       # True
```

### Combining tests

```python
age = 20
print(age >= 18 and age < 65)   # True
print(age < 13 or age >= 65)    # False
print(not (age >= 18))          # False
```

### Precedence in action

```python
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20
print(2 ** 3 + 1)     # 9   <- power first (8), then +1
```

---

## Common mistakes

- **Using `=` when you mean `==`.** `if age = 18:` is an error. To *compare*, use two
  equals signs: `if age == 18:`. One sign stores, two signs ask.
- **Expecting `/` to give a whole number.** `10 / 2` is `4.0`, a float. If you want the
  whole number `5`, use floor division: `10 // 2`.
- **Forgetting precedence.** `2 + 3 * 4` is `14`, not `20`, because `*` runs before `+`.
  If you wanted 20, write `(2 + 3) * 4`. When unsure, add parentheses.

---

## Try it

Open **`labs/02-operators/`** and read its `README.md`. You'll complete the functions in
`operators.py`, then run:

```bash
pytest labs/02-operators/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What is the result of `7 / 2`?
- A) `3`
- B) `3.5`
- C) `4`
- D) `1`

**Q2.** What does `7 // 2` give?
- A) `3.5`
- B) `3`
- C) `4`
- D) `1`

**Q3.** What is `7 % 3`?
- A) `2`
- B) `1`
- C) `2.33`
- D) `0`

**Q4.** Which operator tests whether two values are equal?
- A) `=`
- B) `==`
- C) `!=`
- D) `=>`

**Q5.** What does `2 ** 4` produce?
- A) `8`
- B) `16`
- C) `6`
- D) `24`

**Q6.** What is the value of `True and False`?
- A) `True`
- B) `False`
- C) An error
- D) `None`

**Q7.** What does `2 + 3 * 4` evaluate to?
- A) `20`
- B) `14`
- C) `24`
- D) `9`

**Q8.** Which expression is `True` only when `age` is at least 18?
- A) `age = 18`
- B) `age >= 18`
- C) `age > 18`
- D) `age <= 18`

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** `/` is regular division and always gives a float, so `7 / 2` is `3.5`.

**Q2 — B.** `//` is floor division: it drops the decimal part, leaving the whole number
`3`.

**Q3 — B.** `%` is the remainder. 3 goes into 7 twice with `1` left over.

**Q4 — B.** Two equals signs (`==`) compare. A single `=` stores a value instead.

**Q5 — B.** `**` is power. `2 ** 4` is 2×2×2×2, which is `16`.

**Q6 — B.** `and` is `True` only when both sides are true. One side is `False`, so the
result is `False`.

**Q7 — B.** `*` runs before `+`, so it's `2 + 12`, which is `14`.

**Q8 — B.** `>=` means "greater than or equal to," so it's `True` for 18 and every age
above it. `>` alone would exclude 18.
