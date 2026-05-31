# Module 17 — Capstone Project

## What you'll learn

- How the three tracks fit together into one real pipeline: fetch, process, report
- How to load records from JSON and total them by category
- How to build a small summary of a dataset
- How to write your results out as a clean CSV report

---

## The concept

This is the capstone. You've learned automation (working with files), web and APIs
(fetching data), and data analysis (turning numbers into answers). A huge amount of real
programming is just those three steps chained together:

**Fetch the records → process them → write a report.**

That's a *pipeline*. Picture an assembly line. Raw material comes in at one end (data from
an API or a file). In the middle, you shape it (clean it, total it, summarize it). At the
far end, a finished product rolls out (a CSV report, a chart, an email). Almost every data
job you'll ever write is some version of this line.

Let's walk the whole thing slowly, because this is the biggest lab in the course.

### Step 1 — Fetch the records

In the real world you'd call an API, get back JSON, and have a list of dicts. You did
exactly this in the Web & APIs track:

```python
import requests
response = requests.get("https://some-store.example.com/orders")
orders = response.json()   # a list of order dicts
```

For the **graded lab**, you don't fetch over the network. Instead you load a saved
`orders.json` file from the lab folder. Same shape, but fast, offline, and predictable, so
the tests always agree on the answer. There's an optional `live_demo.py` in the lab that
does a real fetch if you're online and curious.

Either way, after step 1 you hold a list of order dicts. Each order in this lab looks like:

```python
{"id": 1, "category": "books", "amount": 12.99}
```

### Step 2 — Process the records

Now you shape the data. You'll write the same kinds of functions you practiced in the data
track:

- **Total by category.** Group the orders and add up the amounts per category.
- **Summarize.** How many orders are there? What's the grand total? What categories exist?

This is plain Python: loop, convert, tally, sort. No magic.

### Step 3 — Write the report

Finally you save your results so a human (or another program) can use them. A CSV is a
great, universal choice. You'll write a file with a header and one row per category:

```
category,total
books,25.98
food,7.50
toys,40.00
```

You'll sort the categories alphabetically so the report comes out the same every time.
That predictability is the same lesson from every track in this part of the course: sort
your output, and your program behaves identically everywhere.

### Putting it together

Here's the shape of the whole pipeline, using the functions you'll build in the lab:

```python
orders = load_orders("orders.json")      # 1. fetch (here, load from file)
print(summary(orders))                   # 2. process: a quick overview
write_report("report.csv", orders)       # 3. report: save totals per category
```

Three lines. Fetch, process, report. That's a real program.

---

## Show me

### Loading JSON records

JSON on disk loads straight into Python lists and dicts:

```python
import json

with open("orders.json") as f:
    orders = json.load(f)

print(len(orders))         # 6
print(orders[0])           # {'id': 1, 'category': 'books', 'amount': 12.99}
print(orders[0]["amount"]) # 12.99   <- already a float here, since JSON keeps number types
```

Unlike a CSV, JSON remembers types, so `amount` comes back as a real number, not text. One
less conversion to worry about.

### Totalling by category

Same grouping pattern as the data track:

```python
totals = {}
for order in orders:
    category = order["category"]
    totals[category] = totals.get(category, 0) + order["amount"]

print(totals)   # {'books': 25.98, 'toys': 40.0, 'food': 7.5}
```

### A small summary

A dict makes a tidy summary you can print or pass along:

```python
summary = {
    "count": len(orders),
    "total": sum(order["amount"] for order in orders),
    "categories": sorted({order["category"] for order in orders}),
}
print(summary)
# {'count': 6, 'total': 73.48, 'categories': ['books', 'food', 'toys']}
```

`{order["category"] for order in orders}` is a **set comprehension**: it collects the
distinct categories (a set drops duplicates). Wrapping it in `sorted(...)` turns that set
into a predictable, alphabetical list.

### Writing a CSV report

Use `csv.writer` to write a header and one row per category, sorted:

```python
import csv

totals = {"toys": 40.0, "books": 25.98, "food": 7.5}

with open("report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "total"])        # the header
    for category in sorted(totals):               # sorted -> same order every run
        writer.writerow([category, totals[category]])
```

That produces the clean, alphabetized `report.csv` shown earlier. `writer.writerow(...)`
takes a list of values and writes them as one comma-separated line. Opening with
`newline=""` is the recommended way to write CSV files.

---

## Common mistakes

- **Re-fetching or re-reading inside a loop.** Load the orders once into a list, then loop
  over that list as many times as you need. Re-reading a file or re-calling an API on every
  pass is slow and, for an API, rude.
- **Forgetting to sort the report rows.** If you write categories in dict order, the file
  can come out differently on different runs, which makes it hard to compare reports or
  test them. Sort the categories before writing.
- **Opening the CSV without `newline=""`.** Writing a CSV without `newline=""` can insert
  blank lines between rows on some systems. Always open CSV files for writing with
  `open(path, "w", newline="")`.

---

## Try it

Open **`labs/17-capstone/`** and read its `README.md`. This is the biggest lab. You'll
complete the functions in `capstone.py`, then run:

```bash
pytest labs/17-capstone/
```

The read tests load the saved `orders.json` from the lab folder, and the write test uses a
temporary folder, so everything is offline and safe. Make it green to finish the course.
If you're online, try `python labs/17-capstone/live_demo.py` to see a real fetch feed the
same pipeline.

---

## Check yourself

**Q1.** What three steps make up the pipeline this capstone teaches?
- A) Install, configure, deploy
- B) Fetch, process, report
- C) Open, edit, save
- D) Read, delete, undo

**Q2.** Why does the graded lab load `orders.json` from a file instead of calling an API?
- A) APIs can't return JSON
- B) So the tests are fast, offline, and always agree on the answer
- C) Because `requests` is not installed
- D) JSON files are the only data format Python understands

**Q3.** After `json.load(f)` on this lab's file, what type is `order["amount"]`?
- A) `str`, like CSV values
- B) `float`, because JSON keeps number types
- C) `bool`
- D) A list

**Q4.** What does `totals.get(category, 0) + order["amount"]` accomplish?
- A) Replaces the total with the newest amount
- B) Adds this order's amount onto the running total for its category
- C) Deletes the category
- D) Counts the categories

**Q5.** What does `sorted({order["category"] for order in orders})` produce?
- A) A count of orders
- B) The total amount
- C) A sorted list of the distinct category names
- D) The first category only

**Q6.** Why sort the categories before writing the CSV report?
- A) It makes the file smaller
- B) So the report comes out the same every run and is easy to compare and test
- C) It's required by the csv module
- D) It converts the numbers to text

**Q7.** What does `writer.writerow(["category", "total"])` write?
- A) Two separate files
- B) One CSV line: `category,total`
- C) A dict
- D) Nothing until you close the file

**Q8.** Why open a CSV file for writing with `newline=""`?
- A) To make it write faster
- B) To avoid stray blank lines between rows on some systems
- C) To encrypt the file
- D) It has no effect

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** Fetch the records, process them, write a report. That pipeline underlies a huge
amount of real programming.

**Q2 — B.** A saved file keeps the tests fast, offline, and deterministic, so they always
expect the same result.

**Q3 — B.** JSON preserves number types, so `amount` loads as a `float`. CSV, by contrast,
gives you text.

**Q4 — B.** `.get(category, 0)` reads the running total (or 0 if new), and you add this
order's amount to it.

**Q5 — C.** The set comprehension collects distinct categories, and `sorted(...)` returns
them as an alphabetical list.

**Q6 — B.** Sorting makes the output identical every run, which is easy to compare across
runs and easy to test.

**Q7 — B.** `writerow` takes a list and writes it as one comma-separated line, here the
header `category,total`.

**Q8 — B.** Opening CSV files with `newline=""` prevents extra blank lines between rows on
some platforms.
