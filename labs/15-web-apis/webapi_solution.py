"""Lab 15 — Web & APIs: reference solution.

Look here only after you've given the lab a real try. Comparing your working answer to
this one is a great way to learn; copying it before you've struggled is not.
"""
from urllib.parse import urlencode


def parse_titles(posts):
    """Return a list of the "title" value from each post dict, in order."""
    return [post["title"] for post in posts]


def posts_by_user(posts, user_id):
    """Return a list of the posts where post["userId"] == user_id, in order."""
    return [post for post in posts if post["userId"] == user_id]


def count_by_user(posts):
    """Return a dict mapping each userId -> the number of posts by that user."""
    counts = {}
    for post in posts:
        uid = post["userId"]
        counts[uid] = counts.get(uid, 0) + 1
    return counts


def build_query_url(base, params):
    """Return base + "?" + a query string from the params dict, with keys sorted
    alphabetically so the result is the same every time."""
    return f"{base}?{urlencode(sorted(params.items()))}"
