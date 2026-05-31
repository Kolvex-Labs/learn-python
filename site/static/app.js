/* Python for Beginners — interactive site logic.
   Pure browser JS. Talks to the tiny study.py launcher for files, runs, progress. */

const state = {
  modules: [],
  byNum: {},
  progress: {},   // { "01": {read, quizBest, quizTotal, quizPassed, labPassed} }
  obs: null,      // active scroll-spy IntersectionObserver for the jump bar
  stuckObs: null, // observer that detects when the jump bar pins to the top
};

/* ----------------------------- data loading ----------------------------- */
async function loadCourse() {
  const res = await fetch("/static/course.json");
  const data = await res.json();
  state.modules = data.modules;
  state.byNum = {};
  data.modules.forEach(m => { state.byNum[m.num] = m; });
}

async function loadProgress() {
  try {
    const res = await fetch("/api/progress");
    state.progress = (await res.json()) || {};
  } catch (e) { state.progress = {}; }
}

let saveTimer = null;
function saveProgress() {
  clearTimeout(saveTimer);
  saveTimer = setTimeout(() => {
    fetch("/api/progress", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(state.progress),
    }).catch(() => {});
  }, 250);
}

function prog(num) {
  if (!state.progress[num]) state.progress[num] = {};
  return state.progress[num];
}

/* ----------------------------- the user's name -------------------------- */
// Stored under a "user" key in progress.json (won't collide with module nums),
// so it backs up and syncs along with everything else.
function userMeta() {
  if (!state.progress.user) state.progress.user = {};
  return state.progress.user;
}
function getUserName() { return (state.progress.user && state.progress.user.name) || ""; }

function renderNameChip() {
  const chip = document.getElementById("name-chip");
  const name = getUserName();
  chip.textContent = name ? `Hi, ${name}` : "Set your name";
  chip.classList.toggle("unset", !name);
}

function openNameModal() {
  const modal = document.getElementById("name-modal");
  const input = document.getElementById("name-input");
  input.value = getUserName();
  modal.classList.add("show");
  setTimeout(() => input.focus(), 30);
}
function closeNameModal() { document.getElementById("name-modal").classList.remove("show"); }

function saveName() {
  const meta = userMeta();
  meta.name = document.getElementById("name-input").value.trim().slice(0, 40);
  meta.asked = true;
  saveProgress();
  closeNameModal();
  renderNameChip();
  if ((location.hash || "#/") === "#/") renderOverview(document.getElementById("content"));
}

/* ----------------------------- markdown --------------------------------- */
function renderMarkdown(el, md) {
  el.innerHTML = marked.parse(md || "");
  el.querySelectorAll("pre code").forEach(block => {
    try { hljs.highlightElement(block); } catch (e) {}
  });
}
function inlineMd(text) { return marked.parseInline(text || ""); }

/* ----------------------------- status logic ----------------------------- */
function moduleStatus(m) {
  const p = state.progress[m.num] || {};
  const items = [];
  items.push(!!p.read);
  if (m.quiz && m.quiz.length) items.push(!!p.quizPassed);
  if (m.lab) items.push(!!p.labPassed);
  const done = items.filter(Boolean).length;
  if (done === 0) return "none";
  if (done === items.length) return "done";
  return "partial";
}

function overallPercent() {
  let total = 0, done = 0;
  state.modules.forEach(m => {
    const p = state.progress[m.num] || {};
    total++; if (p.read) done++;
    if (m.quiz && m.quiz.length) { total++; if (p.quizPassed) done++; }
    if (m.lab) { total++; if (p.labPassed) done++; }
  });
  return total ? Math.round((done / total) * 100) : 0;
}

function refreshChrome() {
  const pct = overallPercent();
  document.getElementById("overall-bar").style.width = pct + "%";
  document.getElementById("overall-pct").textContent = pct + "%";
  renderSidebar();
}

/* ----------------------------- sidebar ---------------------------------- */
function renderSidebar() {
  const nav = document.getElementById("sidebar");
  const current = location.hash;
  let html = `<a class="nav-item ${current === '#/' || current === '' ? 'active' : ''}" href="#/">
      <span class="nav-num">★</span><span class="nav-title">Overview</span></a>`;
  html += `<div class="nav-section">Modules</div>`;
  state.modules.forEach(m => {
    const active = current === `#/m/${m.num}` ? "active" : "";
    const st = moduleStatus(m);
    html += `<a class="nav-item ${active}" href="#/m/${m.num}">
        <span class="nav-num">${m.num}</span>
        <span class="nav-title">${escapeHtml(m.title)}</span>
        <span class="dot ${st === 'done' ? 'done' : st === 'partial' ? 'partial' : ''}"></span>
      </a>`;
  });
  html += `<div class="nav-section">Track</div>`;
  html += `<a class="nav-item ${current === '#/progress' ? 'active' : ''}" href="#/progress">
      <span class="nav-num">▣</span><span class="nav-title">My progress</span></a>`;
  nav.innerHTML = html;
}

/* ----------------------------- router ----------------------------------- */
function router() {
  const hash = location.hash || "#/";
  const content = document.getElementById("content");
  content.scrollTop = 0;
  window.scrollTo(0, 0);
  document.getElementById("sidebar").classList.remove("open");

  if (hash.startsWith("#/m/")) {
    const num = hash.slice(4);
    renderModule(state.byNum[num], content);
  } else if (hash === "#/progress") {
    renderProgress(content);
  } else {
    renderOverview(content);
  }
  refreshChrome();
  content.focus();
}

/* ----------------------------- overview --------------------------------- */
function renderOverview(content) {
  let cards = state.modules.map(m => {
    const st = moduleStatus(m);
    return `<a class="mini-card" href="#/m/${m.num}">
        <div class="mc-num">MODULE ${m.num}</div>
        <div class="mc-title">${escapeHtml(m.title)}</div>
        <div class="mc-tags">
          <span class="tag ${st === 'done' ? 'on' : ''}">${st === 'done' ? 'Done' : st === 'partial' ? 'Started' : 'To do'}</span>
        </div>
      </a>`;
  }).join("");

  const name = getUserName();
  const eyebrow = name
    ? `Welcome back, ${escapeHtml(name)} 👋`
    : "Interactive course";

  content.innerHTML = `
    <div class="hero">
      <div class="eyebrow">${eyebrow}</div>
      <h1>Python for Beginners</h1>
      <p class="lede">Read a lesson, take the quiz, then write and run real code right here in your browser. Your progress saves automatically.</p>
    </div>
    <div class="panel">
      <div class="panel-head"><h2>How it works</h2></div>
      <p>Each module has three steps: <strong>read</strong> the lesson, pass the <strong>quiz</strong>, and complete the <strong>lab</strong> by making its tests pass. The dots in the sidebar fill in green as you finish each one.</p>
      <div class="btn-row" style="margin-top:6px">
        <a class="btn primary" href="#/m/00">Start with Module 00 →</a>
        <a class="btn ghost" href="#/progress">See my progress</a>
      </div>
    </div>
    <h2>All modules</h2>
    <div class="card-grid">${cards}</div>`;
}

/* ----------------------------- module ----------------------------------- */
function renderModule(m, content) {
  if (!m) { content.innerHTML = "<p>Module not found.</p>"; return; }
  const p = prog(m.num);
  const hasQuiz = m.quiz && m.quiz.length;

  content.innerHTML = `
    <div class="eyebrow">Module ${m.num}</div>
    <div id="jb-sentinel" aria-hidden="true"></div>
    <nav class="jumpbar" id="jumpbar" aria-label="Jump to section">
      <span class="jb-title">${m.num} — ${escapeHtml(m.title)}</span>
      <div class="jb-pills">
        <a class="jump" data-target="lesson">Lesson</a>
        ${hasQuiz ? '<a class="jump" data-target="quiz-mount">Quiz</a>' : ""}
        ${m.lab ? '<a class="jump" data-target="lab-mount">Lab</a>' : ""}
      </div>
    </nav>
    <div id="lesson" class="prose-narrow content-lesson"></div>
    <div class="panel">
      <label class="toggle"><input type="checkbox" id="mark-read" ${p.read ? "checked" : ""}> I've read this module</label>
    </div>
    <div id="quiz-mount"></div>
    <div id="lab-mount"></div>
    <div class="module-nav">
      ${prevLink(m)}<span></span>${nextLink(m)}
    </div>`;

  renderMarkdown(document.getElementById("lesson"), m.lesson_md);

  document.getElementById("mark-read").addEventListener("change", e => {
    p.read = e.target.checked; saveProgress(); refreshChrome();
  });

  if (hasQuiz) renderQuiz(m, document.getElementById("quiz-mount"));
  if (m.lab) renderLab(m, document.getElementById("lab-mount"));

  setupJumpBar();
}

function setupJumpBar() {
  const bar = document.getElementById("jumpbar");
  if (!bar) return;
  const links = Array.from(bar.querySelectorAll(".jump"));
  const targets = links.map(a => document.getElementById(a.dataset.target)).filter(Boolean);

  links.forEach(a => a.addEventListener("click", e => {
    e.preventDefault();
    const el = document.getElementById(a.dataset.target);
    if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
  }));

  const setActive = id => links.forEach(a => a.classList.toggle("active", a.dataset.target === id));
  if (links[0]) setActive(links[0].dataset.target);

  // Highlight whichever section is currently near the top of the viewport.
  if (state.obs) state.obs.disconnect();
  state.obs = new IntersectionObserver(entries => {
    const visible = entries.filter(en => en.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible[0]) setActive(visible[0].target.id);
  }, { rootMargin: "-118px 0px -55% 0px", threshold: 0 });
  targets.forEach(t => state.obs.observe(t));

  // Reveal the module title in the bar once it pins to the top.
  // A 1px sentinel just above the bar: when it scrolls past the sticky line
  // (top bar = 56px), the bar is "stuck".
  if (state.stuckObs) state.stuckObs.disconnect();
  const sentinel = document.getElementById("jb-sentinel");
  if (sentinel) {
    state.stuckObs = new IntersectionObserver(([e]) => {
      bar.classList.toggle("stuck", !e.isIntersecting);
    }, { rootMargin: "-56px 0px 0px 0px", threshold: 0 });
    state.stuckObs.observe(sentinel);
  }
}

function prevLink(m) {
  const i = state.modules.indexOf(m);
  if (i <= 0) return `<a class="btn ghost" href="#/">← Overview</a>`;
  const prev = state.modules[i - 1];
  return `<a class="btn" href="#/m/${prev.num}">← ${escapeHtml(prev.title)}</a>`;
}
function nextLink(m) {
  const i = state.modules.indexOf(m);
  if (i >= state.modules.length - 1) return `<a class="btn" href="#/progress">My progress →</a>`;
  const next = state.modules[i + 1];
  return `<a class="btn primary" href="#/m/${next.num}">${escapeHtml(next.title)} →</a>`;
}

/* ----------------------------- quiz ------------------------------------- */
function renderQuiz(m, mount) {
  const p = prog(m.num);
  let qs = m.quiz.map(q => {
    const opts = ["A", "B", "C", "D"].filter(L => q.options[L] != null).map(L => `
      <label class="quiz-opt" data-letter="${L}">
        <input type="radio" name="q${m.num}_${q.n}" value="${L}">
        <span class="letter">${L}</span>
        <span class="opt-text">${inlineMd(q.options[L])}</span>
      </label>`).join("");
    return `<div class="quiz-q" data-n="${q.n}" data-correct="${q.correct}">
        <div class="qtext">${marked.parse((q.n) + ". " + q.question_md)}</div>
        <div class="quiz-options">${opts}</div>
        <div class="quiz-explain" style="display:none"></div>
      </div>`;
  }).join("");

  mount.innerHTML = `
    <div class="panel">
      <div class="panel-head"><h2>Check yourself</h2></div>
      <p>Pick an answer for each question, then check them. You need them all correct to clear the quiz.</p>
      <div id="quiz-body">${qs}</div>
      <div class="btn-row" style="margin-top:16px">
        <button class="btn primary" id="quiz-check">Check answers</button>
        <span class="quiz-score" id="quiz-score"></span>
      </div>
    </div>`;

  mount.querySelector("#quiz-check").addEventListener("click", () => gradeQuiz(m, mount));
}

function gradeQuiz(m, mount) {
  let correct = 0;
  const total = m.quiz.length;
  let answeredAll = true;

  mount.querySelectorAll(".quiz-q").forEach(qEl => {
    const want = qEl.dataset.correct;
    const chosen = qEl.querySelector("input:checked");
    const explain = qEl.querySelector(".quiz-explain");
    const qData = m.quiz.find(q => String(q.n) === qEl.dataset.n);

    qEl.querySelectorAll(".quiz-opt").forEach(o => o.classList.remove("correct", "wrong"));

    if (!chosen) { answeredAll = false; }
    const got = chosen ? chosen.value : null;

    qEl.querySelectorAll(".quiz-opt").forEach(o => {
      if (o.dataset.letter === want) o.classList.add("correct");
      if (got && o.dataset.letter === got && got !== want) o.classList.add("wrong");
    });

    if (got === want) correct++;
    explain.style.display = "block";
    explain.className = "quiz-explain " + (got === want ? "correct" : "wrong");
    const verdict = got === want ? "Correct. " : (got ? "Not quite. " : "No answer chosen. ");
    explain.innerHTML = `<strong>${verdict}</strong>` + inlineMd(qData.explanation || ("The answer is " + want + "."));
  });

  const scoreEl = mount.querySelector("#quiz-score");
  scoreEl.textContent = `${correct} / ${total} correct`;

  const p = prog(m.num);
  p.quizTotal = total;
  p.quizBest = Math.max(p.quizBest || 0, correct);
  if (answeredAll && correct === total) {
    p.quizPassed = true;
    scoreEl.textContent += "  ✓ quiz cleared!";
  }
  saveProgress(); refreshChrome();
}

/* ----------------------------- lab -------------------------------------- */
async function renderLab(m, mount) {
  const lab = m.lab;
  mount.innerHTML = `
    <div class="panel">
      <div class="panel-head"><h2>Lab — ${escapeHtml(lab.topic)}.py</h2></div>
      <p>Complete the functions below, then <strong>Save &amp; Run</strong> to check them against the tests. Edits save to <code>${escapeHtml(lab.learner_file)}</code>.</p>
      <div id="editor-host"></div>
      <div class="btn-row" style="margin-top:14px">
        <button class="btn primary" id="lab-run"><span id="run-label">Save &amp; Run ▶</span></button>
        <button class="btn" id="lab-reset">Reset to starter</button>
        <button class="btn ghost" id="lab-solution">View solution</button>
      </div>
      <div class="lab-result" id="lab-result">
        <div class="lab-banner" id="lab-banner"></div>
        <pre class="lab-output" id="lab-output"></pre>
      </div>
    </div>`;

  // Load current learner code, then mount CodeMirror.
  let code = "";
  try {
    const res = await fetch(`/api/lab/${lab.id}/file`);
    code = (await res.json()).code || "";
  } catch (e) {}

  const cm = CodeMirror(mount.querySelector("#editor-host"), {
    value: code, mode: "python", theme: "eclipse",
    lineNumbers: true, indentUnit: 4, matchBrackets: true,
  });

  const runBtn = mount.querySelector("#lab-run");
  const runLabel = mount.querySelector("#run-label");
  const resultBox = mount.querySelector("#lab-result");
  const banner = mount.querySelector("#lab-banner");
  const output = mount.querySelector("#lab-output");

  runBtn.addEventListener("click", async () => {
    runBtn.disabled = true;
    runLabel.innerHTML = `<span class="spinner"></span> Running…`;
    try {
      const res = await fetch(`/api/lab/${lab.id}/run`, {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: cm.getValue() }),
      });
      const data = await res.json();
      resultBox.classList.add("show");
      resultBox.classList.toggle("pass", !!data.passed);
      resultBox.classList.toggle("fail", !data.passed);
      banner.textContent = data.passed
        ? "✓ All tests passed — lab complete!"
        : "✗ " + (data.summary || "Some tests failed");
      output.textContent = data.output || "";
      if (data.passed) { prog(m.num).labPassed = true; saveProgress(); refreshChrome(); }
    } catch (e) {
      resultBox.classList.add("show", "fail");
      banner.textContent = "Could not reach the lab runner.";
      output.textContent = String(e);
    } finally {
      runBtn.disabled = false;
      runLabel.innerHTML = "Save &amp; Run ▶";
    }
  });

  mount.querySelector("#lab-reset").addEventListener("click", async () => {
    if (!confirm("Reset this lab back to the starter code? Your current edits will be lost.")) return;
    const res = await fetch(`/api/lab/${lab.id}/reset`, { method: "POST" });
    const data = await res.json();
    if (data.code != null) cm.setValue(data.code);
    resultBox.classList.remove("show");
  });

  mount.querySelector("#lab-solution").addEventListener("click", async () => {
    if (!confirm("Show the reference solution? Try it yourself first — you learn more that way.")) return;
    const res = await fetch(`/api/lab/${lab.id}/solution`);
    const data = await res.json();
    output.textContent = data.code || "(no solution found)";
    resultBox.classList.add("show");
    resultBox.classList.remove("pass", "fail");
    banner.textContent = "Reference solution (read, don't just copy)";
  });
}

/* ----------------------------- progress page ---------------------------- */
function renderProgress(content) {
  const rows = state.modules.map(m => {
    const p = state.progress[m.num] || {};
    const cell = (on, label) => `<span class="tag ${on ? 'on' : ''}">${label}</span>`;
    return `<tr>
      <td><a href="#/m/${m.num}">${m.num} — ${escapeHtml(m.title)}</a></td>
      <td>${cell(p.read, "Read")}</td>
      <td>${m.quiz && m.quiz.length ? cell(p.quizPassed, p.quizBest != null ? `Quiz ${p.quizBest}/${p.quizTotal || m.quiz.length}` : "Quiz") : "—"}</td>
      <td>${m.lab ? cell(p.labPassed, "Lab") : "—"}</td>
    </tr>`;
  }).join("");

  content.innerHTML = `
    <div class="eyebrow">Your journey</div>
    <h1>My progress</h1>
    <div class="panel">
      <div class="panel-head"><h2>${overallPercent()}% complete</h2></div>
      <div class="topbar-progress" style="margin:0"><div class="bar" style="width:100%"><div class="bar-fill" style="width:${overallPercent()}%"></div></div></div>
      <table style="margin-top:18px">
        <thead><tr><th>Module</th><th>Read</th><th>Quiz</th><th>Lab</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
    </div>`;
}

/* ----------------------------- utils ------------------------------------ */
function escapeHtml(s) {
  return (s || "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
}

/* ----------------------------- boot ------------------------------------- */
async function boot() {
  document.getElementById("menu-toggle").addEventListener("click", () => {
    document.getElementById("sidebar").classList.toggle("open");
  });

  // Name prompt wiring
  document.getElementById("name-chip").addEventListener("click", openNameModal);
  document.getElementById("name-save").addEventListener("click", saveName);
  document.getElementById("name-skip").addEventListener("click", () => {
    userMeta().asked = true; saveProgress(); closeNameModal();
  });
  document.getElementById("name-input").addEventListener("keydown", e => {
    if (e.key === "Enter") saveName();
    if (e.key === "Escape") closeNameModal();
  });

  window.addEventListener("hashchange", router);
  await loadCourse();
  await loadProgress();
  renderNameChip();
  router();

  // First visit: gently ask their name (only once — respect "Maybe later").
  if (!getUserName() && !(state.progress.user && state.progress.user.asked)) {
    openNameModal();
  }
}
boot();
