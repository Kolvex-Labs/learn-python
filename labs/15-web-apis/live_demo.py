"""Optional. Requires internet. Not graded.

This script makes a REAL web request to the public JSONPlaceholder test API, then reuses
your lab function `parse_titles` to pull out the titles. Run it yourself if you're online:

    python labs/15-web-apis/live_demo.py

No test imports this file, so it never runs during grading.
"""
import requests

from webapi import parse_titles


def main():
    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"Fetching {url} ...")

    response = requests.get(url, timeout=10)
    print(f"Status code: {response.status_code}")  # 200 means it worked

    posts = response.json()          # parse the JSON into a Python list of dicts
    print(f"Got {len(posts)} posts.")

    titles = parse_titles(posts)     # the same function the graded lab tests
    print("First few titles:")
    for title in titles[:5]:
        print(f"  - {title}")


if __name__ == "__main__":
    main()
