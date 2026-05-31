# Module 13 — Object-Oriented Programming

## What you'll learn

- What an object is: data and behavior bundled together
- The difference between a class (the blueprint) and an instance (a real thing)
- How `__init__` and `self` set up each new object
- How attributes hold data and methods do work
- How `__str__` gives your object a friendly printed form

---

## The concept

So far you've kept data in variables and written separate functions to act on it. **Object-
oriented programming** (OOP) bundles the two together. An **object** is data *and* the
behavior that goes with it, in one package.

Think of a dog. It has data: a name, an age. It has behavior: it can bark, it can sit.
An object lets you keep the name, the age, and the bark all in one place, because they
belong together.

### Class vs instance

A **class** is a blueprint. It describes what every object of that kind has and can do. An
**instance** is one actual object built from that blueprint.

The blueprint "Dog" is the class. *Your* dog, Rex, is an instance. My dog, Bella, is
another instance. Same blueprint, two separate dogs with their own data.

```python
class Dog:
    ...

rex = Dog()      # an instance
bella = Dog()    # a different instance
```

### `__init__` and `self`

When you create an instance, Python calls a special method named **`__init__`** (two
underscores on each side) to set it up. This is where you give the new object its starting
data.

The first parameter of every method is **`self`** — it refers to *this particular
instance*. You attach data to `self` so each object remembers its own values.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name      # store name on THIS dog
        self.age = age        # store age on THIS dog

rex = Dog("Rex", 3)
print(rex.name)               # Rex
print(rex.age)                # 3
```

`Dog("Rex", 3)` builds a new dog and runs `__init__` with `name="Rex"` and `age=3`. You
don't pass `self` yourself — Python fills it in with the new object.

### Attributes and methods

- An **attribute** is a piece of data on an object, reached with a dot: `rex.name`.
- A **method** is a function defined inside the class. It always takes `self` first, so it
  can use the object's own data:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says woof!"

rex = Dog("Rex")
print(rex.bark())             # Rex says woof!
```

`rex.bark()` runs the `bark` method with `self` set to `rex`, so `self.name` is `"Rex"`.

### `__str__`: a friendly printed form

By default, printing an object shows something ugly like `<__main__.Dog object at 0x...>`.
Define a **`__str__`** method to control what `print` shows:

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Dog named {self.name}"

print(Dog("Rex"))             # Dog named Rex
```

### Why OOP helps

When your program models real things — a bank account, a shopping cart, a game character —
OOP lets you keep each thing's data and actions together. The account knows its own balance
*and* how to deposit. That keeps related code in one place and makes it easier to reason
about.

---

## Show me

### A Rectangle class

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

r = Rectangle(4, 3)
print(r.area())          # 12
print(r.perimeter())     # 14
```

`r` carries its own `width` and `height`. The methods use them through `self`.

### A BankAccount with behavior and a guard

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

acct = BankAccount()       # balance starts at 0
acct.deposit(100)
print(acct.balance)        # 100
acct.withdraw(30)
print(acct.balance)        # 70
```

Trying to overdraw raises an error instead of going negative:

```python
acct.withdraw(1000)        # ValueError: insufficient funds
```

The account guards its own balance. The rule lives with the data it protects — that's the
OOP idea at work.

---

## Common mistakes

- **Forgetting `self` on a method.** Every method's first parameter must be `self`. Writing
  `def area(width, height):` inside a class will not work the way you expect — use
  `def area(self):` and reach the data through `self.width`.
- **Forgetting `self.` when storing data.** Inside `__init__`, `name = name` just makes a
  local variable that vanishes. You need `self.name = name` so the value sticks to the
  object.
- **Calling a method without parentheses.** `r.area` gives you the method itself, not the
  result. You must call it: `r.area()`.

---

## Try it

Open **`labs/13-oop/`** and read its `README.md`. You'll complete the classes in
`shapes.py`, then run:

```bash
pytest labs/13-oop/
```

Make it green before moving on.

---

## Check yourself

**Q1.** What is an object?
- A) A type of number
- B) Data and behavior bundled together
- C) A file on disk
- D) A loop

**Q2.** What's the difference between a class and an instance?
- A) They're the same thing
- B) A class is the blueprint; an instance is one actual object built from it
- C) An instance is the blueprint; a class is the object
- D) A class can only make one instance

**Q3.** When is `__init__` called?
- A) Every time you print the object
- B) When you create a new instance
- C) Only when the program ends
- D) Never automatically

**Q4.** What does `self` refer to inside a method?
- A) The class blueprint
- B) The particular instance the method was called on
- C) The first argument the user typed
- D) A global variable

**Q5.** In `__init__`, which line correctly stores `name` on the object?
- A) `name = name`
- B) `self.name = name`
- C) `self = name`
- D) `Dog.name = name`

**Q6.** What does `r.area` (no parentheses) give you?
- A) The result of area
- B) The method itself, not its result
- C) An error
- D) `None`

**Q7.** What does defining `__str__` let you control?
- A) How the object is created
- B) What `print(object)` displays
- C) How fast methods run
- D) The object's memory address

**Q8.** Given the BankAccount above, what happens on `acct.withdraw(1000)` when the balance
is 70?
- A) The balance becomes -930
- B) Nothing happens
- C) It raises `ValueError("insufficient funds")`
- D) It returns 0

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** An object packages data together with the behavior that acts on it.

**Q2 — B.** The class is the blueprint; each instance is a separate real object built from
that blueprint, with its own data.

**Q3 — B.** `__init__` runs automatically when you create a new instance, to set it up.

**Q4 — B.** `self` is the particular instance the method is running on, so `self.x` reaches
that object's own data.

**Q5 — B.** `self.name = name` attaches the value to the object. A plain `name = name` just
makes a local variable that disappears.

**Q6 — B.** Without parentheses you get the method object itself. Call it with `r.area()`
to get the result.

**Q7 — B.** `__str__` defines what `print(object)` shows, replacing the default ugly form.

**Q8 — C.** Withdrawing more than the balance raises `ValueError("insufficient funds")`, so
the balance never goes negative.
