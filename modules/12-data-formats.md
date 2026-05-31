# Module 12 — Working with Data Formats

## What you'll learn

- What JSON is, and how it mirrors Python dicts and lists
- How to turn data into JSON text with `json.dumps` and back with `json.loads`
- What CSV is, and how it stores rows of comma-separated values
- How to write CSV files with `csv.writer` and read them with `csv.DictReader`
- When to reach for JSON and when to reach for CSV

---

## The concept

Your program holds data in dicts, lists, strings, and numbers. To **save** that data to a
file, or **send** it to another program, you need to turn it into plain text in an agreed
shape. That shape is a **data format**. Two formats cover most everyday needs: JSON and
CSV.

### JSON: text that looks like Python data

**JSON** (JavaScript Object Notation) is a text format that mirrors Python dicts and
lists almost exactly. A JSON object looks like a Python dict; a JSON array looks like a
Python list. This makes it a natural fit for nested data.

```json
{"name": "Alex", "age": 30, "hobbies": ["chess", "code"]}
```

That's a string of text, but you can see the dict inside it. Python's **`json`** module
converts between the two:

- `json.dumps(obj)` — **dump to string**. Takes a Python object, returns JSON **text**.
- `json.loads(text)` — **load from string**. Takes JSON text, returns a Python object.

Remember the `s`: `dumps` and `loads` work with **s**trings. (There's also `json.dump`
and `json.load` without the `s` that work directly with files, but `dumps`/`loads` and
strings are all you need here.)

A round trip should give you back what you started with:

```python
import json
data = {"a": 1, "b": [2, 3]}
text = json.dumps(data)         # '{"a": 1, "b": [2, 3]}'
back = json.loads(text)         # {'a': 1, 'b': [2, 3]}
back == data                    # True
```

### CSV: a grid of rows and columns

**CSV** (Comma-Separated Values) stores a table: rows of values separated by commas. It's
what spreadsheets export. The first row is usually a **header** naming the columns:

```
name,age
Alex,30
Sam,9
```

That's two data rows under a header. CSV is flat — just rows and columns, no nesting —
which makes it perfect for tabular data like a list of people or sales.

Python's **`csv`** module handles the fiddly comma-and-quote details for you:

- `csv.writer(f)` — write rows. Call `.writerow(list)` for each row.
- `csv.DictReader(f)` — read rows. It uses the header row as keys and gives you one
  **dict per data row**.

When you open a file for the `csv` module, pass `newline=""` so line endings behave
correctly across systems:

```python
with open(path, "w", newline="") as f:
    ...
```

### JSON vs CSV: which one?

- Reach for **JSON** when your data is **nested** or mixed — a dict with lists inside,
  settings, an API response.
- Reach for **CSV** when your data is a **flat table** — rows that all share the same
  columns, like a spreadsheet of records.

---

## Show me

### JSON round trip

```python
import json

person = {"name": "Sam", "age": 9, "pets": ["cat"]}

text = json.dumps(person)
print(text)
# {"name": "Sam", "age": 9, "pets": ["cat"]}

back = json.loads(text)
print(back["pets"])
# ['cat']

print(back == person)
# True
```

### Writing a CSV file

```python
import csv

with open("people.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age"])     # header
    writer.writerow(["Alex", 30])       # a data row
    writer.writerow(["Sam", 9])          # another row
```

The file now holds:

```
name,age
Alex,30
Sam,9
```

### Reading a CSV file into dicts

```python
import csv

with open("people.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
# {'name': 'Alex', 'age': '30'}
# {'name': 'Sam', 'age': '9'}
```

Notice `'age': '30'` — a **string**, not the number 30. CSV stores everything as text, so
convert with `int(...)` if you need to do math.

---

## Common mistakes

- **Mixing up `dumps` and `loads`.** `dumps` turns a Python object *into* a JSON string;
  `loads` turns a JSON string *into* a Python object. If you get a `TypeError` or a
  surprising result, check you're going the right direction.
- **Expecting numbers back from CSV.** `csv.DictReader` gives every value as a string.
  `row["age"]` is `"30"`, not `30`. Convert with `int(row["age"])` when you need a number.
- **Forgetting `newline=""` when opening a CSV file.** Without it you can get stray blank
  lines between rows on some systems. Always open CSV files with `newline=""`.

---

## Try it

Open **`labs/12-data-formats/`** and read its `README.md`. You'll complete the functions
in `dataio.py`, then run:

```bash
pytest labs/12-data-formats/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What does `json.dumps(obj)` return?
- A) A Python dict
- B) A JSON string
- C) A file
- D) A list

**Q2.** What does `json.loads(text)` return?
- A) A JSON string
- B) The Python object the JSON text describes
- C) The number of characters
- D) Nothing

**Q3.** JSON is a natural fit for which kind of data?
- A) Flat tables only
- B) Nested data, like a dict with lists inside
- C) Images
- D) Only numbers

**Q4.** In a CSV file, what usually goes in the first row?
- A) The largest value
- B) A header naming the columns
- C) A blank line
- D) The total

**Q5.** What does `csv.DictReader` give you for each data row?
- A) A list of values
- B) A dict keyed by the header
- C) A single string
- D) A number

**Q6.** After reading a CSV, what type is the value `row["age"]`?
- A) `int`
- B) `float`
- C) `str`
- D) `bool`

**Q7.** Which format would you choose for a flat list of records that all share the same
columns?
- A) JSON
- B) CSV
- C) Neither works
- D) A `.py` file

**Q8.** What does `json.loads(json.dumps(data))` give you?
- A) An error
- B) The original `data` back
- C) Always an empty dict
- D) A JSON string

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** `dumps` **dumps** a Python object out to a JSON **string** (note the `s` for
string).

**Q2 — B.** `loads` **loads** a JSON string back into the Python object it represents.

**Q3 — B.** JSON mirrors dicts and lists, so it handles nested and mixed data well.

**Q4 — B.** The first row is typically the header that names each column.

**Q5 — B.** `DictReader` uses the header as keys and returns one dict per data row.

**Q6 — C.** CSV stores everything as text, so values come back as `str`. Convert with
`int(...)` for math.

**Q7 — B.** CSV is built for flat tables where every row shares the same columns.

**Q8 — B.** Dumping to JSON and loading it back is a round trip that returns the original
data.
