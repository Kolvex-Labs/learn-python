# Module 05 — Loops

## What you'll learn

- How to repeat work with a `for` loop over `range()` and over a list
- How to keep looping while a condition holds with a `while` loop
- How to control a count with `range(start, stop, step)`
- How to leave a loop early with `break` and skip an item with `continue`
- The accumulator pattern: building up a running total
- How to avoid loops that never end

---

## The concept

A **loop** repeats a block of code. Instead of writing the same line ten times, you
write it once and tell Python to run it ten times. There are two kinds you'll use every
day: `for` and `while`.

### for loops over a range

`range(n)` produces the numbers `0, 1, 2, ... up to but not including n`. A `for` loop
walks through them one at a time:

```python
for i in range(3):
    print(i)
# 0
# 1
# 2
```

Read it as: "for each number `i` in the range, run the indented body." The variable `i`
takes each value in turn. Like `if`, the header ends with `:` and the body is indented.

Note `range(3)` stops *before* 3, just like slicing stops before its end number. So
`range(3)` gives `0, 1, 2` — three numbers.

### range with start, stop, and step

`range` can take more numbers: `range(start, stop, step)`.

```python
range(2, 6)       # 2, 3, 4, 5            (start at 2, stop before 6)
range(0, 10, 2)   # 0, 2, 4, 6, 8        (step by 2)
range(5, 0, -1)   # 5, 4, 3, 2, 1        (count down with a negative step)
```

The **step** is how much to jump each time. A negative step counts down — handy for a
countdown.

### for loops over a list

A `for` loop also walks straight through the items of a list, no numbers needed:

```python
fruits = ["apple", "pear", "plum"]
for fruit in fruits:
    print(fruit)
# apple
# pear
# plum
```

### The accumulator pattern

A very common job: add up or build up a result as you loop. You start with an empty
total *before* the loop, then update it each time through. This is the **accumulator
pattern**:

```python
total = 0                 # start empty, before the loop
for n in range(1, 5):     # 1, 2, 3, 4
    total = total + n     # add each number to the running total
print(total)              # 10
```

The same idea works for building a string or a list — start empty, add on each pass.

### while loops

A `while` loop keeps going *as long as* its condition is true. Use it when you don't
know in advance how many times to repeat:

```python
count = 3
while count > 0:
    print(count)
    count = count - 1     # move toward the stopping point
print("Liftoff!")
# 3
# 2
# 1
# Liftoff!
```

**The critical line is `count = count - 1`.** Something inside the loop must change so
the condition eventually becomes false. If nothing changes, the loop runs forever — an
**infinite loop**. If your program seems frozen, you probably have one; press
`Ctrl + C` to stop it.

### break and continue

Two keywords steer a loop from the inside:

- **`break`** leaves the loop immediately, skipping anything left.
- **`continue`** skips the rest of *this* pass and jumps to the next item.

```python
for n in range(10):
    if n == 5:
        break          # stop the whole loop when n is 5
    print(n)
# 0 1 2 3 4
```

```python
for n in range(5):
    if n % 2 == 0:
        continue       # skip even numbers
    print(n)
# 1 3
```

---

## Show me

### Summing with an accumulator

```python
total = 0
for n in range(1, 6):     # 1, 2, 3, 4, 5
    total = total + n
print(total)              # 15
```

### Counting down with a negative step

```python
for n in range(5, 0, -1):
    print(n)
# 5
# 4
# 3
# 2
# 1
```

### A while loop with a clear stop

```python
n = 1
while n <= 4:
    print(n)
    n = n + 1
# 1 2 3 4
```

### break to stop early

```python
numbers = [4, 9, 6, 7]
for num in numbers:
    if num % 3 == 0:
        print(num)        # 9   <- the first multiple of 3
        break
```

---

## Common mistakes

- **The infinite loop.** A `while` loop whose condition never becomes false runs
  forever. Always change something inside the loop that moves toward the stop, like
  `count = count - 1`. Press `Ctrl + C` to break out of a stuck program.
- **Off-by-one with `range`.** `range(1, 5)` is `1, 2, 3, 4` — it stops *before* 5. If
  you want to include 5, write `range(1, 6)`.
- **Resetting the accumulator inside the loop.** Put `total = 0` *before* the loop, not
  inside it. Inside, it would reset to 0 every pass and you'd lose your running total.

---

## Try it

Open **`labs/05-loops/`** and read its `README.md`. You'll complete the functions in
`loops.py`, then run:

```bash
pytest labs/05-loops/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What numbers does `range(3)` produce?
- A) `1, 2, 3`
- B) `0, 1, 2, 3`
- C) `0, 1, 2`
- D) `0, 1, 2, 3, 4`

**Q2.** What does this print?
```python
total = 0
for n in range(1, 4):
    total = total + n
print(total)
```
- A) `3`
- B) `6`
- C) `10`
- D) `0`

**Q3.** What does `range(0, 10, 2)` produce?
- A) `0, 2, 4, 6, 8`
- B) `0, 2, 4, 6, 8, 10`
- C) `2, 4, 6, 8, 10`
- D) `0, 1, 2, ... 10`

**Q4.** What does `break` do inside a loop?
- A) Skips the current item and continues
- B) Leaves the loop immediately
- C) Restarts the loop
- D) Pauses for a second

**Q5.** What does `continue` do inside a loop?
- A) Leaves the loop immediately
- B) Skips the rest of this pass and moves to the next item
- C) Ends the program
- D) Repeats the current item

**Q6.** What causes an infinite `while` loop?
- A) Using `range`
- B) Nothing inside the loop ever makes the condition false
- C) Using `break`
- D) Indenting the body

**Q7.** Where should you put `total = 0` for an accumulator?
- A) Inside the loop body
- B) Before the loop starts
- C) After the loop ends
- D) It doesn't matter

**Q8.** What does `range(5, 0, -1)` produce?
- A) `5, 4, 3, 2, 1`
- B) `5, 4, 3, 2, 1, 0`
- C) `0, 1, 2, 3, 4, 5`
- D) `1, 2, 3, 4, 5`

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — C.** `range(3)` starts at 0 and stops before 3, giving `0, 1, 2`.

**Q2 — B.** The loop adds 1, 2, and 3 to `total`, giving `6`. (`range(1, 4)` stops
before 4.)

**Q3 — A.** Start at 0, stop before 10, step by 2: `0, 2, 4, 6, 8`.

**Q4 — B.** `break` exits the loop right away, skipping any remaining passes.

**Q5 — B.** `continue` skips the rest of the current pass and jumps to the next item.

**Q6 — B.** If nothing inside the loop moves the condition toward false, it never stops.
Change a value each pass to avoid it.

**Q7 — B.** Initialize the accumulator before the loop. Inside, it would reset every
pass and lose the running total.

**Q8 — A.** A negative step counts down: `5, 4, 3, 2, 1`, stopping before 0.
