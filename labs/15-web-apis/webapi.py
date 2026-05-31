"""Lab 15 — Web & APIs.

Complete each function below. Replace the `raise NotImplementedError(...)` line with
your code. Run `pytest labs/15-web-apis/` to check your work.

These functions are PURE data processing. They take data that has already been fetched
(a list of post dicts) and work with it. There is NO network call here, which is exactly
how real code should be split: fetch in one place, process in another.

Each post dict is shaped like:
    {"userId": 1, "id": 1, "title": "...", "body": "..."}
"""
from urllib.parse import urlencode


def parse_titles(posts):
    """Return a list of the "title" value from each post dict, in order."""
    # TODO: build and return a list of post["title"] for every post.
    raise NotImplementedError("Complete parse_titles()")


def posts_by_user(posts, user_id):
    """Return a list of the posts where post["userId"] == user_id, in order."""
    # TODO: keep only the posts whose "userId" matches user_id, return that list.
    raise NotImplementedError("Complete posts_by_user()")


def count_by_user(posts):
    """Return a dict mapping each userId -> the number of posts by that user."""
    # TODO: walk the posts and tally how many each userId has. A plain dict with
    #       counts.get(uid, 0) + 1 works well.
    raise NotImplementedError("Complete count_by_user()")


def build_query_url(base, params):
    """Return base + "?" + a query string from the params dict, with keys sorted
    alphabetically so the result is the same every time. Use urlencode on the
    sorted items."""
    # TODO: return f"{base}?{urlencode(sorted(params.items()))}"
    raise NotImplementedError("Complete build_query_url()")
