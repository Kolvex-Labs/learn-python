# Setup — do this once (about 15 minutes)

This gets Python installed, your workspace ready, and the lab tests running. You only
do it once. Follow it top to bottom and don't skip steps.

You're on a Mac with Apple Silicon and Homebrew already installed. Every command below
goes in the **Terminal** app (find it with Spotlight: press `Cmd+Space`, type
"Terminal", hit Enter).

---

## Step 1 — Install a modern Python

Your Mac ships with an old Python (3.9). We'll install a current one with Homebrew so
everything in this course works.

```bash
brew install python@3.13
```

Check it worked:

```bash
/opt/homebrew/bin/python3.13 --version
```

You should see something like `Python 3.13.13`. (If you already ran this with me, it's
done.)

> **What's Homebrew?** A "package manager" — an app that installs developer tools for
> you with one command. The `brew install` above downloads Python and sets it up.

---

## Step 2 — Open the course folder

```bash
cd ~/Code/python-course
```

`cd` means "change directory" — it moves your Terminal into the course folder. You'll
run every later command from here.

---

## Step 3 — Create a virtual environment

A **virtual environment** ("venv") is a private box for this project's Python and its
add-on packages, so this course never interferes with anything else on your machine.

Create it once:

```bash
/opt/homebrew/bin/python3.13 -m venv .venv
```

This makes a hidden `.venv` folder. You won't touch it directly.

---

## Step 4 — Activate the environment

**You do this every time you open a new Terminal to work on the course:**

```bash
source .venv/bin/activate
```

Your prompt will now start with `(.venv)`. That's how you know the box is active.
To leave it later, type `deactivate`. (If you forget to activate, the `python` and
`pytest` commands below may use the wrong Python — so always look for `(.venv)`.)

---

## Step 5 — Install the course's packages

With `(.venv)` showing:

```bash
pip install -r requirements.txt
```

This installs **pytest** (runs the lab tests) and **requests** (used in the web module).

Check it worked:

```bash
python --version      # -> Python 3.13.x
pytest --version      # -> pytest 9.x
```

---

## Step 6 — Pick an editor

You need somewhere to write code. **VS Code** is the friendly standard:

1. Download from <https://code.visualstudio.com/> and drag it to Applications.
2. Open it, go to the Extensions panel (the squares icon), search **"Python"**, and
   install Microsoft's Python extension.
3. Open the course: in VS Code, `File ▸ Open Folder…` and choose
   `~/Code/python-course`.

You can edit the `.py` files right in VS Code and keep Terminal open alongside it.

---

## Step 7 — Three ways to run Python

You'll use all three during the course:

**1. Run a script file** (most common):
```bash
python hello.py
```

**2. The REPL** — an interactive prompt for trying one line at a time. Start it with:
```bash
python
```
You'll get `>>>`. Type `2 + 2`, press Enter, see `4`. Type `exit()` to leave. Great
for experiments.

**3. Run a lab's tests** — checks your work:
```bash
pytest labs/01-variables/
```
Green = correct. Red = read the message and fix your code.

---

## Daily routine (after setup)

Every time you sit down to study:

```bash
cd ~/Code/python-course
source .venv/bin/activate      # prompt shows (.venv)
```

Then read the next module, do its lab, and run the test. That's it.

---

## Quick troubleshooting

| Problem | Fix |
|---------|-----|
| `command not found: pytest` | You forgot Step 4. Run `source .venv/bin/activate`. |
| `command not found: brew` | Homebrew isn't installed. See <https://brew.sh>. |
| Prompt doesn't show `(.venv)` | Activate it (Step 4), and make sure you're in `~/Code/python-course`. |
| `pip install` errors | Make sure `(.venv)` is showing first, then retry. |
| Edited code but test still fails the same way | Save the file in your editor (`Cmd+S`) before re-running. |

Done? Open **`modules/00-setup.md`** and write your first program.
