# Lab 15 — Web & APIs

**Module:** 15 — Web & APIs Track

## Goal

Practice the part of API work that matters most: processing the data you get back. You'll
turn a list of post dicts into titles, filters, counts, and a clean query URL — all pure
Python, no network needed.

## Your task

Open **`webapi.py`**. It has four functions with `# TODO` markers. Complete each one so it
does what its description says. Don't change the function names or their inputs — the tests
rely on them. Each post dict looks like
`{"userId": 1, "id": 1, "title": "...", "body": "..."}`.

1. `parse_titles(posts)` — return a list of every post's `"title"`.
2. `posts_by_user(posts, user_id)` — return the posts where `post["userId"] == user_id`.
3. `count_by_user(posts)` — return a dict mapping each userId to how many posts they have.
4. `build_query_url(base, params)` — return `base + "?" + query string`, with the params'
   keys sorted alphabetically (use `urllib.parse.urlencode`).

The tests load the saved `sample_posts.json` from this folder, so they run instantly and
offline.

## Run the test

From the course folder, with your venv active:

```bash
pytest labs/15-web-apis/
```

- **Green** → all four work. Tick it off in `PROGRESS.md` and move on.
- **Red** → read the message; it names the function and what it expected. Fix `webapi.py`
  and run again.

Want to see a real request? If you're online, run `python labs/15-web-apis/live_demo.py`.
It's optional and not graded.

## Stuck?

Ask the tutor agent for a hint, or open `webapi_solution.py` as a last resort.
