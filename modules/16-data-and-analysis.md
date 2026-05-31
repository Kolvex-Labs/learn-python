# Module 16 — Data & Analysis Track

## What you'll learn

- How to read a CSV file into rows you can work with, using `csv.DictReader`
- Why numbers in a CSV arrive as text, and how to convert them
- How to sum, average, and group rows to find real answers
- How to find the biggest group, like your best-selling product

---

## The concept

**A CSV is a spreadsheet saved as plain text.** CSV stands for *comma-separated values*.
Each line is a row, and commas split the columns. The first line is usually the
**header**, naming each column:

```
product,amount
Widget,10.00
Gadget,25.50
```

That's a header (`product`, `amount`) and two data rows. CSVs are everywhere: exports
from spreadsheets, bank statements, sales reports. Knowing how to read one and pull
insight from it is a genuinely useful skill.

You can do all of this with Python's **standard library** — the tools that ship with
Python, nothing to install. Two modules carry the load:

- **`csv`** — reads and writes CSV files correctly, handling commas and quoting for you.
- **`statistics`** — small math helpers like `mean` (the average).

A few words you'll see:

- **Header** — the first row, naming the columns.
- **Row** — one record, like one sale.
- **`DictReader`** — a reader that turns each row into a dict keyed by the header, so you
  write `row["amount"]` instead of counting commas.
- **Grouping** — bucketing rows by a column's value, like "all the Widget sales together".

### Numbers come in as text

This trips up everyone once. When you read a CSV, every value arrives as a **string**,
even the numbers. `row["amount"]` is `"25.50"`, the text, not the number `25.50`. To do
math you must convert first:

```python
amount = float(row["amount"])   # now it's a real number you can add
```

Use `float(...)` for decimals and `int(...)` for whole numbers. Forget this step and
you'll get text glued together (`"10" + "25" == "1025"`) instead of a sum.

> **What about pandas?** You may have heard of pandas, a popular library for data work.
> It's powerful and worth learning later. But you do **not** need it here, and reaching
> for a big library before you understand the basics hides what's really happening. The
> standard library does everything in this module. Treat pandas as an optional "going
> further" tool once these fundamentals feel easy.

---

## Show me

### Reading rows as dicts

```python
import csv

with open("sales.csv", newline="") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(rows[0])   # {'product': 'Widget', 'amount': '10.00'}
print(rows[0]["product"])   # Widget
print(rows[0]["amount"])    # 10.00   <- still text! note the quotes when you print type
```

`csv.DictReader` reads the header automatically and makes each row a dict. The
`newline=""` in `open(...)` is the recommended way to open CSV files; it lets the `csv`
module handle line endings correctly.

### Summing and averaging

Convert as you go:

```python
amounts = [float(row["amount"]) for row in rows]

total = sum(amounts)
print(total)        # 71.50

import statistics
average = statistics.mean(amounts)
print(average)      # 23.833333333333332
```

`sum(...)` adds a list of numbers. `statistics.mean(...)` gives the average. Both need
real numbers, which is why you converted with `float(...)` first.

### Grouping by a column

To total sales per product, walk the rows and add each amount into a dict bucket:

```python
totals = {}
for row in rows:
    product = row["product"]
    amount = float(row["amount"])
    totals[product] = totals.get(product, 0) + amount

print(totals)   # {'Widget': 30.0, 'Gadget': 25.5, 'Gizmo': 16.0}
```

`totals.get(product, 0)` reads the running total so far, or `0` if this is the first time
you've seen that product. Then you add the new amount.

### Finding the maximum

To pick the product with the highest total, use `max` with a `key`:

```python
top = max(totals, key=totals.get)
print(top)   # Widget
```

`max(totals, key=totals.get)` looks through the product names and picks the one whose
value (its total) is largest.

---

## Common mistakes

- **Forgetting to convert text to numbers.** `row["amount"]` is a string. `sum` of strings
  fails, and `"10" + "25"` gives `"1025"`. Always `float(row["amount"])` before math.
- **Opening the file without `newline=""`.** On some systems this causes blank rows to
  sneak in. The csv docs say to open with `newline=""`, so do that.
- **Reading the file twice.** A file reader is used up after one pass. If you loop over the
  reader and then try again, the second loop is empty. Read into a `list(reader)` once,
  then reuse that list as many times as you like.

---

## Try it

Open **`labs/16-data-analysis/`** and read its `README.md`. You'll complete the functions in
`analysis.py`, then run:

```bash
pytest labs/16-data-analysis/
```

The tests load the saved `sales.csv` from the lab folder, so they're fast and offline.
Make it green before moving on.

---

## Check yourself

**Q1.** What does CSV stand for?
- A) Computed source values
- B) Comma-separated values
- C) Column storage version
- D) Common spreadsheet view

**Q2.** What does `csv.DictReader` give you for each row?
- A) A list of the values, in order
- B) A single string of the whole line
- C) A dict keyed by the header column names
- D) A number

**Q3.** You read `row["amount"]` and get `"25.50"`. What type is it?
- A) `float`
- B) `int`
- C) `str`
- D) `bool`

**Q4.** Why must you call `float(row["amount"])` before adding amounts?
- A) To round the number
- B) Because the value is text, and text can't be summed as numbers
- C) To make the program faster
- D) It isn't necessary

**Q5.** What does `statistics.mean([10, 20, 30])` return?
- A) `60`
- B) `30`
- C) `20`
- D) `10`

**Q6.** What does `totals.get(product, 0)` do when `product` isn't in `totals` yet?
- A) Raises a KeyError
- B) Returns `0`
- C) Returns `None`
- D) Adds the product with value 1

**Q7.** What does `max(totals, key=totals.get)` return?
- A) The largest total amount as a number
- B) The product name whose total is largest
- C) A sorted list of products
- D) The number of products

**Q8.** Do you need pandas to complete this module's lab?
- A) Yes, it's required
- B) No, the standard library `csv` and `statistics` are enough
- C) Only for reading the file
- D) Only for the average

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** CSV is comma-separated values: a spreadsheet saved as plain text with commas
between columns.

**Q2 — C.** `DictReader` uses the header row to make each row a dict, so you access
`row["amount"]` by name.

**Q3 — C.** Everything read from a CSV is text, so it's a `str` until you convert it.

**Q4 — B.** The value is a string. You can't sum strings as numbers, so convert with
`float(...)` first.

**Q5 — C.** The mean of 10, 20, and 30 is their sum (60) divided by the count (3), which
is 20.

**Q6 — B.** `.get(key, default)` returns the default (here `0`) when the key is missing,
which is perfect for a running total.

**Q7 — B.** With `key=totals.get`, `max` compares products by their totals and returns the
product name with the biggest one.

**Q8 — B.** Everything here is done with the standard library. Pandas is an optional
"going further" tool, not a requirement.
