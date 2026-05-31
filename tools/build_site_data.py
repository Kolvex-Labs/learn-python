#!/usr/bin/env python3
"""Build the interactive site's data file from the course modules.

Reads every modules/NN-*.md, splits each into:
  - the lesson (everything before "## Check yourself"), kept as raw Markdown
    so the browser can render it with marked.js,
  - the quiz questions (parsed into structured options A-D),
  - the answer key (correct letter + explanation per question),
and matches each module to its lab folder. Writes site/static/course.json.

Pure standard library. Run it with:
    ./.venv/bin/python tools/build_site_data.py
(study.py runs this for you automatically.)
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MODULES_DIR = ROOT / "modules"
LABS_DIR = ROOT / "labs"
STARTERS_DIR = ROOT / "starters"
OUT = ROOT / "site" / "static" / "course.json"

# A question begins:  **Q1.** text...
Q_START = re.compile(r"^\*\*Q(\d+)\.\*\*\s*(.*)$")
# An option line:     - A) text...
OPTION = re.compile(r"^-\s*([A-D])\)\s*(.*)$")
# An answer line:     **Q1 — B.** explanation   (em dash or hyphen)
ANSWER = re.compile(r"^\*\*Q(\d+)\s*[—-]\s*([A-D])\.\*\*\s*(.*)$")
# Module title:       # Module 01 — Title
TITLE = re.compile(r"^#\s*Module\s*\d+\s*[—–-]\s*(.*)$", re.M)


def split_sections(text):
    """Return (lesson_md, quiz_block, answer_block)."""
    quiz_split = re.split(r"^##\s*Check yourself\s*$", text, maxsplit=1, flags=re.M)
    lesson = quiz_split[0].strip()
    quiz_block, answer_block = "", ""
    if len(quiz_split) == 2:
        rest = quiz_split[1]
        ans_split = re.split(r"^##\s*Answer key\s*$", rest, maxsplit=1, flags=re.M)
        quiz_block = ans_split[0]
        if len(ans_split) == 2:
            answer_block = ans_split[1]
    return lesson, quiz_block, answer_block


def parse_questions(quiz_block):
    """Parse the Check-yourself block into a list of question dicts."""
    lines = quiz_block.splitlines()
    questions = []
    current = None          # the question being built
    mode = None             # "question" while collecting the stem, "options" after
    for line in lines:
        m = Q_START.match(line)
        if m:
            if current:
                questions.append(current)
            current = {"n": int(m.group(1)),
                       "question_lines": [m.group(2)] if m.group(2) else [],
                       "options": {}}
            mode = "question"
            continue
        if current is None:
            continue
        opt = OPTION.match(line)
        if opt:
            current["options"][opt.group(1)] = opt.group(2).strip()
            mode = "options"
            continue
        # Non-option line: part of the question stem only while still collecting it.
        if mode == "question":
            current["question_lines"].append(line)
    if current:
        questions.append(current)

    for q in questions:
        q["question_md"] = "\n".join(q["question_lines"]).strip()
        del q["question_lines"]
    return questions


def parse_answers(answer_block):
    """Map question number -> {'correct': letter, 'explanation': text}."""
    answers = {}
    current_n = None
    for line in answer_block.splitlines():
        m = ANSWER.match(line)
        if m:
            current_n = int(m.group(1))
            answers[current_n] = {"correct": m.group(2),
                                  "explanation_lines": [m.group(3)]}
        elif current_n is not None and line.strip():
            answers[current_n]["explanation_lines"].append(line.strip())
        elif current_n is not None and not line.strip():
            # Blank line ends an explanation paragraph.
            current_n = None
    for a in answers.values():
        a["explanation"] = " ".join(a.pop("explanation_lines")).strip()
    return answers


def lab_for(num):
    """Find the lab folder whose name starts with this module number.

    Returns the lab id, its topic module name, and the learner/solution file
    names, plus snapshots the pristine starter the first time it is seen.
    """
    for d in sorted(LABS_DIR.iterdir()):
        if not (d.is_dir() and d.name.startswith(f"{num}-")):
            continue
        sols = list(d.glob("*_solution.py"))
        if not sols:
            return {"id": d.name, "dir": f"labs/{d.name}"}
        topic = sols[0].name[: -len("_solution.py")]
        learner = d / f"{topic}.py"

        # Snapshot the pristine starter ONCE, while it is still the stub.
        # The guard means a learner's later edits are never captured here.
        if learner.exists():
            STARTERS_DIR.mkdir(exist_ok=True)
            snap = STARTERS_DIR / f"{d.name}__{topic}.py"
            if not snap.exists():
                snap.write_text(learner.read_text(encoding="utf-8"), encoding="utf-8")

        return {
            "id": d.name,
            "dir": f"labs/{d.name}",
            "topic": topic,
            "learner_file": f"labs/{d.name}/{topic}.py",
            "solution_file": f"labs/{d.name}/{topic}_solution.py",
            "starter_snapshot": f"starters/{d.name}__{topic}.py",
        }
    return None


def build():
    modules = []
    for path in sorted(MODULES_DIR.glob("*.md")):
        num = path.name[:2]                       # "00".."17"
        text = path.read_text(encoding="utf-8")
        title_match = TITLE.search(text)
        title = title_match.group(1).strip() if title_match else path.stem

        lesson, quiz_block, answer_block = split_sections(text)
        questions = parse_questions(quiz_block)
        answers = parse_answers(answer_block)

        quiz = []
        for q in questions:
            ans = answers.get(q["n"], {})
            quiz.append({
                "n": q["n"],
                "question_md": q["question_md"],
                "options": q["options"],
                "correct": ans.get("correct"),
                "explanation": ans.get("explanation", ""),
            })

        modules.append({
            "num": num,
            "title": title,
            "slug": path.stem,
            "lesson_md": lesson,
            "quiz": quiz,
            "lab": lab_for(num),
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"modules": modules}, indent=2), encoding="utf-8")

    # A short build report so problems are obvious.
    total_q = sum(len(m["quiz"]) for m in modules)
    missing = [(m["num"], q["n"]) for m in modules for q in m["quiz"]
               if not q["correct"] or not q["options"]]
    print(f"Wrote {OUT.relative_to(ROOT)}")
    print(f"  modules: {len(modules)}   quiz questions: {total_q}")
    print(f"  labs linked: {sum(1 for m in modules if m['lab'])}")
    if missing:
        print(f"  WARNING: {len(missing)} questions missing an answer or options: {missing}")
    else:
        print("  every quiz question has options and a correct answer.")


if __name__ == "__main__":
    build()
