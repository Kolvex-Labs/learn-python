#!/usr/bin/env python3
"""Launch the interactive local study site for the Python for Beginners course.

    python study.py

Run it from anywhere inside a clone of this course — it finds its own folder.
It is pure standard library: no Flask, no extra dependencies, no build step. It
serves the static site in `site/` and adds a few small endpoints so the page can
load, save, and run your lab code and remember your progress.

Everything stays on your own machine (127.0.0.1). Press Ctrl+C to stop.
"""
import json
import os
import signal
import socket
import subprocess
import sys
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent
SITE = ROOT / "site"
COURSE_JSON = SITE / "static" / "course.json"
PROGRESS = ROOT / "progress.json"
BUILD_SCRIPT = ROOT / "tools" / "build_site_data.py"
RUN_TIMEOUT = int(os.environ.get("STUDY_RUN_TIMEOUT", "30"))  # secs; catches infinite loops

CONTENT_TYPES = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "text/javascript; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".ico": "image/x-icon",
}

LABS = {}  # lab id -> lab metadata, filled at startup from course.json


# --------------------------------------------------------------------------- #
# Setup helpers
# --------------------------------------------------------------------------- #
def venv_python():
    """Return the Path to the venv's python, or None if the venv is missing."""
    for candidate in (ROOT / ".venv" / "bin" / "python",
                      ROOT / ".venv" / "Scripts" / "python.exe"):
        if candidate.exists():
            return candidate
    return None


def ensure_venv():
    """Create the virtual environment and install deps if it isn't there yet."""
    py = venv_python()
    if py:
        return py
    print("No virtual environment found — setting one up (one time, ~1 min)...")
    base = Path("/opt/homebrew/bin/python3.13")
    bootstrap = str(base) if base.exists() else sys.executable
    subprocess.run([bootstrap, "-m", "venv", str(ROOT / ".venv")], check=True)
    py = venv_python()
    subprocess.run([str(py), "-m", "pip", "install", "-q", "--upgrade", "pip"], check=True)
    subprocess.run([str(py), "-m", "pip", "install", "-q", "pytest", "requests"], check=True)
    print("Virtual environment ready.\n")
    return py


def rebuild_and_load(py):
    """Regenerate course.json (and starter snapshots), then load the lab map."""
    subprocess.run([str(py), str(BUILD_SCRIPT)], check=True)
    data = json.loads(COURSE_JSON.read_text(encoding="utf-8"))
    labs = {}
    for module in data["modules"]:
        lab = module.get("lab")
        if lab and "topic" in lab:
            labs[lab["id"]] = lab
    return labs


def read_progress():
    if PROGRESS.exists():
        try:
            return json.loads(PROGRESS.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def write_progress(obj):
    PROGRESS.write_text(json.dumps(obj, indent=2), encoding="utf-8")


def summary_line(output):
    """The last non-empty line of pytest output is its one-line summary."""
    lines = [ln for ln in output.splitlines() if ln.strip()]
    return lines[-1] if lines else ""


# --------------------------------------------------------------------------- #
# HTTP handler
# --------------------------------------------------------------------------- #
class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass  # keep the terminal quiet

    # -- small response helpers --
    def _json(self, obj, status=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_body(self):
        length = int(self.headers.get("Content-Length", 0) or 0)
        if not length:
            return {}
        raw = self.rfile.read(length)
        try:
            return json.loads(raw or b"{}")
        except json.JSONDecodeError:
            return {}

    # -- routing --
    def do_GET(self):
        path = urlparse(self.path).path
        if path.startswith("/api/"):
            return self._api_get(path)
        return self._serve_static(path)

    def do_POST(self):
        path = urlparse(self.path).path
        if path.startswith("/api/"):
            return self._api_post(path)
        return self._json({"error": "not found"}, 404)

    # -- static files (confined to site/) --
    def _serve_static(self, path):
        if path in ("/", ""):
            path = "/index.html"
        target = (SITE / path.lstrip("/")).resolve()
        site_root = SITE.resolve()
        if not str(target).startswith(str(site_root)) or not target.is_file():
            return self._json({"error": "not found"}, 404)
        body = target.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type",
                         CONTENT_TYPES.get(target.suffix, "application/octet-stream"))
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # -- API: GET --
    def _api_get(self, path):
        if path == "/api/progress":
            return self._json(read_progress())
        parts = path.strip("/").split("/")  # ["api", "lab", "<id>", "<action>"]
        if len(parts) == 4 and parts[1] == "lab":
            lab = LABS.get(parts[2])
            if not lab:
                return self._json({"error": "unknown lab"}, 404)
            if parts[3] == "file":
                p = ROOT / lab["learner_file"]
                return self._json({"code": p.read_text(encoding="utf-8") if p.exists() else ""})
            if parts[3] == "solution":
                p = ROOT / lab["solution_file"]
                return self._json({"code": p.read_text(encoding="utf-8") if p.exists() else ""})
        return self._json({"error": "not found"}, 404)

    # -- API: POST --
    def _api_post(self, path):
        if path == "/api/progress":
            write_progress(self._read_body())
            return self._json({"ok": True})
        parts = path.strip("/").split("/")
        if len(parts) == 4 and parts[1] == "lab":
            lab = LABS.get(parts[2])
            if not lab:
                return self._json({"error": "unknown lab"}, 404)
            if parts[3] == "run":
                code = self._read_body().get("code", "")
                (ROOT / lab["learner_file"]).write_text(code, encoding="utf-8")
                return self._run_lab(lab)
            if parts[3] == "reset":
                snap = ROOT / lab["starter_snapshot"]
                if not snap.exists():
                    return self._json({"error": "no starter snapshot"}, 404)
                text = snap.read_text(encoding="utf-8")
                (ROOT / lab["learner_file"]).write_text(text, encoding="utf-8")
                return self._json({"ok": True, "code": text})
        return self._json({"error": "not found"}, 404)

    def _run_lab(self, lab):
        py = venv_python()
        try:
            proc = subprocess.run(
                [str(py), "-m", "pytest", lab["dir"], "-q"],
                cwd=str(ROOT), capture_output=True, text=True, timeout=RUN_TIMEOUT)
        except subprocess.TimeoutExpired:
            return self._json({
                "passed": False, "timeout": True,
                "summary": "Timed out",
                "output": (f"Your code ran longer than {RUN_TIMEOUT} seconds and was "
                           "stopped. That usually means an infinite loop — check the "
                           "conditions on your while/for loops."),
            })
        output = (proc.stdout + proc.stderr).strip()
        return self._json({
            "passed": proc.returncode == 0,
            "summary": summary_line(output),
            "output": output,
        })


# --------------------------------------------------------------------------- #
# Entrypoint
# --------------------------------------------------------------------------- #
def backup_on_exit():
    """Run the save-progress script so stopping the site backs up your work."""
    script = ROOT / "save-progress"
    if not script.exists():
        return
    print("\nBacking up your work to GitHub...", flush=True)
    try:
        subprocess.run(["bash", str(script)], cwd=str(ROOT), timeout=90)
    except Exception as e:
        print(f"(Backup skipped: {e}. Your work is still saved on disk.)", flush=True)


def _raise_interrupt(signum, frame):
    raise KeyboardInterrupt


def find_port(start=8000):
    for port in range(start, start + 50):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise SystemExit("Could not find a free port between 8000 and 8049.")


def main():
    global LABS
    py = ensure_venv()
    print("Preparing your course...")
    LABS = rebuild_and_load(py)
    port = find_port()
    url = f"http://127.0.0.1:{port}/"
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)

    # Stopping the site (Ctrl+C, or a kill signal) triggers an automatic backup.
    signal.signal(signal.SIGTERM, _raise_interrupt)

    print("\n  Your Python course is ready.", flush=True)
    print(f"  Open:  {url}", flush=True)
    print("  Press Ctrl+C here to stop (your work backs up automatically).\n", flush=True)
    if not os.environ.get("STUDY_NO_BROWSER"):
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.shutdown()
        backup_on_exit()
        print("Stopped. See you next time.", flush=True)


if __name__ == "__main__":
    main()
