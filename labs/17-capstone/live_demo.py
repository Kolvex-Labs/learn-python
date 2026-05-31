"""Optional. Requires internet. Not graded.

This script shows the full pipeline running against a REAL API. It fetches records from
the public JSONPlaceholder test API, adapts a few of them into the
{"id", "category", "amount"} shape this lab uses, then feeds them through your real lab
functions summary() and write_report(). Run it yourself if you're online:

    python labs/17-capstone/live_demo.py

No test imports this file, so it never runs during grading.
"""
import requests

from capstone import summary, write_report


def fetch_and_adapt():
    """Fetch some posts and pretend they are orders, so we have real data to process.

    The real API returns posts shaped like {"userId", "id", "title", "body"}. We adapt
    each one into an order: category from the userId, amount from the title length.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    print(f"Fetching {url} ...")
    response = requests.get(url, timeout=10)
    print(f"Status code: {response.status_code}")  # 200 means it worked

    posts = response.json()[:6]   # just the first 6, to keep it small
    orders = []
    for post in posts:
        orders.append({
            "id": post["id"],
            "category": f"user_{post['userId']}",
            "amount": float(len(post["title"])),
        })
    return orders


def main():
    orders = fetch_and_adapt()       # 1. fetch (real network call)
    print("Summary:", summary(orders))  # 2. process

    rows = write_report("live_report.csv", orders)  # 3. report
    print(f"Wrote live_report.csv with {rows} category rows.")


if __name__ == "__main__":
    main()
