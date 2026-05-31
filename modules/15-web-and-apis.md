# Module 15 — Web & APIs Track

## What you'll learn

- What an API is, in plain language, and what "REST" means
- How to fetch data from the web with the `requests` library
- How to read a JSON response and turn it into Python lists and dicts
- How to be a polite, well-behaved API user

---

## The concept

**An API is a way for one program to ask another program for data.** API stands for
*Application Programming Interface*. Forget the long name. The idea is a waiter at a
restaurant. You don't walk into the kitchen and cook. You tell the waiter what you want,
the waiter brings it back. An API is that waiter between your code and someone else's
data.

A few words you'll see:

- **API** — a doorway another program offers so you can request data from it.
- **HTTP** — the language computers use to talk over the web. When you load a web page,
  your browser speaks HTTP.
- **GET** — the HTTP request that means "give me this data." There are others (POST sends
  data, DELETE removes it), but GET is the one you'll start with.
- **REST** — a common, tidy style of API where each kind of thing has its own web address
  (URL) and you use GET to read it. `/posts` gives you posts, `/posts/1` gives you post
  number 1. That predictable shape is what people mean by "REST".
- **URL** — the web address you send your request to, like
  `https://jsonplaceholder.typicode.com/posts`.
- **JSON** — the text format APIs almost always answer in. It looks exactly like Python
  lists and dicts, which is wonderful for us.
- **Status code** — a number the server sends back saying how it went. `200` means OK.
  `404` means "not found". `500` means the server broke.

### What a JSON response looks like

When you GET that posts URL, the server replies with text shaped like this:

```json
[
  {"userId": 1, "id": 1, "title": "First post", "body": "Hello there"},
  {"userId": 1, "id": 2, "title": "Second post", "body": "More words"}
]
```

That's a **list of dicts**. Once `requests` hands it to Python, it really is a Python
list of Python dicts. Everything you learned about lists and dicts applies. You loop over
it, you read `post["title"]`, you filter and count. The web part is just *getting* the
data. The fun part is *processing* it, and that's all plain Python.

### Being a polite API user

APIs are run by real people and cost real money. Be a good guest:

- **Don't hammer it.** Don't fire thousands of requests in a tight loop.
- **Cache when you can.** If you already fetched the data, reuse it instead of asking again.
- **Check the status code** before trusting the response.
- **Read the docs and respect rate limits.** Many APIs say "no more than N requests per
  minute." Honor that.

This is why the graded lab below uses **saved sample data** instead of the live web. It's
fast, it works on a plane with no wifi, and it never bothers a real server. You'll still
see a real `requests` example here, and an optional live demo you can run yourself.

---

## Show me

### A real request with `requests`

The `requests` library makes web requests simple. Here's a real one against the public
JSONPlaceholder test API:

```python
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts")

print(response.status_code)   # 200   <- 200 means it worked
posts = response.json()       # turn the JSON text into Python data
print(type(posts))            # <class 'list'>
print(len(posts))             # 100
print(posts[0]["title"])      # sunt aut facere repellat provident ... (first post's title)
```

Three pieces do all the work:

- `requests.get(url)` sends the GET request and waits for the reply.
- `response.status_code` is the number telling you how it went (`200` = OK).
- `response.json()` parses the JSON text into a Python list or dict.

> **About the lab:** the real call above needs internet and hits a live server. The graded
> lab instead loads a saved `sample_posts.json` file from the lab folder, so it runs
> instantly and offline. The data has the same shape, so the code you write works either
> way. There's also a `live_demo.py` in the lab you can run for real if you're online.

### Processing the data is just Python

Once you have a list of post dicts, pulling out what you need is ordinary list and dict
work:

```python
posts = [
    {"userId": 1, "id": 1, "title": "First"},
    {"userId": 2, "id": 2, "title": "Second"},
]

titles = [post["title"] for post in posts]
print(titles)   # ['First', 'Second']
```

### Building a URL with query parameters

Many APIs let you filter with **query parameters** in the URL, the part after a `?`:
`/posts?userId=1`. Don't glue these together by hand. Use `urllib.parse.urlencode`, and
sort the keys so the result is the same every time:

```python
from urllib.parse import urlencode

params = {"userId": 1, "limit": 5}
query = urlencode(sorted(params.items()))
print(query)   # limit=5&userId=1   <- keys sorted alphabetically
```

Sorting matters for the same reason as in the automation track: a predictable result is
testable and behaves the same everywhere.

---

## Common mistakes

- **Forgetting to call `.json()`.** `response` is not your data; it's a wrapper around the
  reply. You must call `response.json()` (or `response.text`) to get the actual content.
  `response["title"]` is an error.
- **Trusting a request without checking the status.** A `404` or `500` still returns a
  response object. If you skip the status check and call `.json()` on an error page, you
  get confusing crashes. Look at `response.status_code` first.
- **Hammering the API in a loop.** Sending the same request hundreds of times is slow,
  rude, and can get you blocked. Fetch once, store the result, and work from the stored
  copy. That's exactly why this lab uses a saved file.

---

## Try it

Open **`labs/15-web-apis/`** and read its `README.md`. You'll complete the functions in
`webapi.py`, then run:

```bash
pytest labs/15-web-apis/
```

The tests load the saved `sample_posts.json`, so they're fast and offline. Make it green
before moving on. If you're online and curious, run `python labs/15-web-apis/live_demo.py`
to see a real request.

---

## Check yourself

**Q1.** In plain terms, what is an API?
- A) A kind of database file
- B) A way for one program to request data from another program
- C) A programming language
- D) A type of web browser

**Q2.** Which HTTP request means "give me this data"?
- A) GET
- B) POST
- C) DELETE
- D) STORE

**Q3.** What does the status code `200` mean?
- A) The server is down
- B) The page was not found
- C) The request worked
- D) You sent too many requests

**Q4.** What does `response.json()` return for the posts endpoint?
- A) The raw HTTP headers
- B) A Python list of dicts
- C) A single string of HTML
- D) The status code

**Q5.** What shape is a typical JSON API response of many records?
- A) A single number
- B) A list of dicts
- C) A plain sentence
- D) A folder of files

**Q6.** Why does the graded lab use a saved JSON file instead of the live API?
- A) The live API costs money per call to the student
- B) So the tests are fast, offline, and don't bother a real server
- C) Because `requests` doesn't work in tests
- D) Because JSON can't be sent over the web

**Q7.** Why call `urlencode(sorted(params.items()))` instead of building the URL by hand?
- A) It encrypts the parameters
- B) It produces a correct, predictable query string every time
- C) It's the only way to send a GET request
- D) It removes the parameters entirely

**Q8.** Which is the polite way to use an API?
- A) Send as many requests as fast as possible
- B) Fetch once, reuse the result, and respect rate limits
- C) Ignore the status code
- D) Never read the documentation

---

<!-- ANSWER KEY — try the quiz before reading -->

---

## Answer key

**Q1 — B.** An API is a doorway one program offers so another can request its data, like
a waiter between you and the kitchen.

**Q2 — A.** GET means "read this." POST sends data, DELETE removes it.

**Q3 — C.** `200` is the "OK" status. `404` is not found, `500` is a server error.

**Q4 — B.** `.json()` parses the JSON text into Python data; for this endpoint that's a
list of dicts.

**Q5 — B.** Collections of records arrive as a JSON array of objects, which becomes a
Python list of dicts.

**Q6 — B.** Saved data keeps the tests fast, offline, and deterministic, and avoids
pestering a real server.

**Q7 — B.** `urlencode` handles correct formatting, and sorting the items makes the output
identical every run, which is testable.

**Q8 — B.** Fetch once, reuse, check status codes, and respect rate limits. That's a good
API citizen.
