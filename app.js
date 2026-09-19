import {
  CONFIG,
  COUNTIES,
  BEATS,
  loadStories,
  eatDate,
  electionDays,
  timeAgo,
} from "./data.js";
import { panelMarkup, escapeHTML as esc } from "./art.js";
const $ = (s) => document.querySelector(s);
const read = (key, fallback) => {
  try {
    const v = localStorage.getItem("ngesa:" + key);
    return v ? JSON.parse(v) : fallback;
  } catch {
    return fallback;
  }
};
const write = (key, value) => {
  try {
    localStorage.setItem("ngesa:" + key, JSON.stringify(value));
    return true;
  } catch {
    return false;
  }
};
const preferences = {
  theme: "light",
  lang: "en",
  saver: false,
  text: "normal",
  ...read("preferences", {}),
};
if (!["en", "sw", "sheng"].includes(preferences.lang)) preferences.lang = "en";
let stories = [],
  limit = 6,
  savedOnly = false,
  selectedCounty = "Nairobi",
  activeStory = null,
  panelIndex = 0,
  readerMode = "comic",
  shareStory = null,
  sharePanel = null;
const storedSaved = read("saved", []);
let saved = new Set(Array.isArray(storedSaved) ? storedSaved : []);
let speaking = false,
  installPrompt = null,
  toastTimer;
const headline = (s) => s.headline[preferences.lang] || s.headline.en;
const langAttr = () => (preferences.lang === "en" ? "en" : "sw");
const stamp = (s) =>
  `<span class="stamp ${s.verification.status.toLowerCase()}">${s.sample ? "SAMPLE · " : ""}${esc(s.verification.status)}</span>`;
const safeURL = (url) => {
  try {
    const u = new URL(url);
    return ["https:", "http:"].includes(u.protocol) ? u.href : "#";
  } catch {
    return "#";
  }
};
const sourceChips = (s) =>
  s.sources
    .map(
      (source) =>
        `<a class="source-chip" href="${esc(safeURL(source.url))}" target="_blank" rel="noopener">${esc(source.name)}</a>`,
    )
    .join("");
const timestamp = (s) =>
  `<time datetime="${esc(s.published_at)}" title="${esc(new Date(s.published_at).toLocaleString("en-GB", { timeZone: "Africa/Nairobi" }))} EAT">${timeAgo(s.published_at)}</time>`;
function toast(message) {
  $("#toast").textContent = message;
  $("#toast").classList.add("show");
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => $("#toast").classList.remove("show"), 4500);
}
function persistPreferences() {
  write("preferences", preferences);
}
function loadFonts() {
  if (preferences.saver || $("#news-fonts")) return;
  const link = document.createElement("link");
  link.id = "news-fonts";
  link.rel = "stylesheet";
  link.href =
    "https://fonts.googleapis.com/css2?family=Anton&family=Bangers&family=Newsreader:ital,wght@0,400;1,400&family=Space+Mono:wght@400;700&display=swap";
  document.head.append(link);
}
function applyPreferences() {
  document.documentElement.dataset.theme = preferences.theme;
  document.documentElement.dataset.saver = preferences.saver;
  document.documentElement.dataset.text = preferences.text;
  $("#theme").textContent =
    preferences.theme === "dark" ? "◐ Newsprint" : "◐ Midnight Noir";
  $("#theme").setAttribute("aria-pressed", preferences.theme === "dark");
  $("#saver").textContent = `Data Saver: ${preferences.saver ? "on" : "off"}`;
  $("#saver").setAttribute("aria-pressed", preferences.saver);
  $("#text-size").setAttribute("aria-pressed", preferences.text === "large");
  $("#text-size").textContent =
    preferences.text === "large" ? "Aa Standard text" : "Aa Larger text";
  document.querySelector("meta[name=theme-color]").content =
    preferences.theme === "dark" ? "#0E0E12" : "#F4EEDF";
  document
    .querySelectorAll("[data-lang]")
    .forEach((b) =>
      b.setAttribute("aria-pressed", b.dataset.lang === preferences.lang),
    );
  if (preferences.saver) $("#news-fonts")?.remove();
  else loadFonts();
}
applyPreferences();
$("#year").textContent = new Date().getFullYear();
const dateParts = eatDate().split("-");
const issue =
  Math.floor(
    (Date.parse(dateParts.join("-")) - Date.UTC(Number(dateParts[0]), 0, 1)) /
      86400000,
  ) + 1;
$("#edition-date").textContent =
  `${new Intl.DateTimeFormat("en-GB", { timeZone: "Africa/Nairobi", day: "numeric", month: "short", year: "numeric" }).format(new Date()).toUpperCase()} · VOL ${Math.max(1, Number(dateParts[0]) - 2025)} / NO ${String(issue).padStart(3, "0")}`;
$("#countdown").textContent = electionDays();
$("#election-source").href = CONFIG.electionSource;
function renderHero() {
  const s = stories[0];
  $("#hero").innerHTML =
    `<div class="lead-copy"><span class="dispatch">BREAKING DISPATCH · ${esc(s.beat.toUpperCase())} · SAMPLE</span><h1 lang="${langAttr()}">${esc(headline(s))}</h1><p class="deck">${esc(s.deck)}</p><div class="byline">BY ${esc(s.byline.toUpperCase())}<br><span class="live-dot red" aria-hidden="true"></span> SAMPLE FEED · ${timestamp(s)} · ${s.read_mins} MIN READ · EAT</div><div class="verification">${stamp(s)}<span class="meta">FICTIONAL SCENARIO<br>REAL CIVIC QUESTIONS</span></div><div class="source-chips">${sourceChips(s)}</div><p class="meta">Official source = background, not proof of a sample event.</p><div class="reading-actions"><button class="button-ink" data-open="${s.id}" data-mode="comic">▦ Read as Comic ↗</button><button data-open="${s.id}" data-mode="article">≡ Read as Article</button><button data-share="${s.id}" aria-label="Share lead story">↗</button></div></div><div class="hero-art"><div class="mosaic">${s.panels
      .slice(0, 3)
      .map((p, i) => panelMarkup(p, i, { large: i === 0 }))
      .join(
        "",
      )}</div><div class="hero-asides"><div class="mini-note"><h3>Today in 60 seconds ↘</h3><p>Five stories. The context. The receipts.</p><a href="#brief">Get the short version →</a></div><div class="mini-note"><h3>Ukweli Meter ↘</h3><p>Before you forward it, let’s check it.</p><a href="#ukweli">Tetesi vs ukweli →</a></div></div></div>`;
}
function renderTicker() {
  const links = stories
    .slice(0, 5)
    .map(
      (s) =>
        `<a href="#story=${s.slug}" data-open="${s.id}" lang="${langAttr()}"><b>SAMPLE</b> ${esc(headline(s))}</a>`,
    )
    .join("");
  $("#ticker-track").innerHTML =
    `<div class="ticker-group">${links}</div><div class="ticker-group" aria-hidden="true" inert>${links}</div>`;
}
function renderBrief() {
  $("#brief-strip").innerHTML = stories
    .slice(0, 5)
    .map(
      (s, i) =>
        `<article class="brief-card"><div class="brief-top"><b>0${i + 1}</b><span>${esc(s.beat.toUpperCase())} · SAMPLE</span></div>${panelMarkup({ ...s.panels[0], caption: "SAMPLE / " + s.beat, bubble: s.brief[preferences.lang], sfx: "" }, i)}<h3 lang="${langAttr()}">${esc(headline(s))}</h3><p lang="${langAttr()}">${esc(s.brief[preferences.lang])}</p><button data-open="${s.id}">Open case file ↗</button></article>`,
    )
    .join("");
}
function filteredStories() {
  const beat = $("#beat-filter").value,
    county = $("#county-filter").value;
  return stories.filter(
    (s) =>
      (!beat || s.beat === beat) &&
      (!county ||
        s.counties.includes(county) ||
        s.counties.includes("All counties")) &&
      (!savedOnly || saved.has(s.id)),
  );
}
function renderWire() {
  const filtered = filteredStories();
  $("#wire-count").textContent =
    `${filtered.length} SAMPLE CASE FILE${filtered.length === 1 ? "" : "S"}`;
  $("#saved-count").textContent = saved.size;
  $("#wire-grid").innerHTML =
    filtered
      .slice(0, limit)
      .map(
        (s, i) =>
          `<article class="story-card ink-in" style="--delay:${Math.min(i, 5) * 60}ms"><div class="card-layout">${panelMarkup(s.panels[0])}<div class="card-content"><div class="card-topline"><span class="eyebrow">${esc(s.beat.toUpperCase())}</span><span class="sample-label">SAMPLE</span></div><h3 lang="${langAttr()}"><button class="card-title" data-open="${s.id}">${esc(headline(s))}</button></h3><div class="meta">${timestamp(s)} · ${s.read_mins} MIN READ · EAT</div><div class="source-chips">${s.counties.map((c) => `<span class="chip">${esc(c)}</span>`).join("")}${s.parties.map((p) => `<span class="chip">${esc(p)}</span>`).join("")}</div><div class="source-chips">${sourceChips(s)}</div></div></div><div class="card-actions"><span class="status">○ ${esc(s.verification.status)}</span><button data-save="${s.id}" aria-label="${saved.has(s.id) ? "Unsave" : "Save"} ${esc(s.headline.en)}" aria-pressed="${saved.has(s.id)}">${saved.has(s.id) ? "◆" : "◇"}</button><button data-share="${s.id}" aria-label="Share ${esc(s.headline.en)}">↗</button></div></article>`,
      )
      .join("") ||
    '<div class="empty"><h3 lang="sw">Kimya kabisa. Hakuna habari mpya.</h3><p>No sample stories match. Try another filter or save a story first.</p></div>';
  $("#load-more").hidden = filtered.length <= limit;
  $("#saved-filter").setAttribute("aria-pressed", savedOnly);
}
function renderBills() {
  const stages = [
    "First Reading",
    "Committee",
    "Second Reading",
    "Third Reading",
    "Assent",
  ];
  $("#bill-trackers").innerHTML = [
    {
      title: "Market Services Bill",
      stage: 1,
      story: stories[0],
      meaning:
        "For this fictional bill: check who would pay, how much, and whether small traders were heard.",
    },
    {
      title: "County Reporting Bill",
      stage: 2,
      story: stories[5],
      meaning:
        "For this fictional bill: clearer reporting would let residents follow the same project over time.",
    },
  ]
    .map(
      (b) =>
        `<article class="panel bill"><div><span class="sample-label">SAMPLE BILL · NOT A REAL PARLIAMENTARY RECORD</span><h3>${b.title}</h3><div class="bill-stages" aria-label="Illustrative bill progress">${stages.map((stage, i) => `<div class="stage ${i === b.stage ? "current" : ""}" ${i === b.stage ? 'aria-current="step"' : ""}><span>0${i + 1}${i === b.stage ? " · NOW" : ""}</span>${stage}</div>`).join("")}</div><p class="meta">Simplified overview: committee scrutiny follows First Reading; Committee of the Whole House and Report Stage follow Second Reading. Other steps can apply.</p><button data-open="${b.story.id}" data-mode="article">Read the context ↗</button></div><div class="speech"><span class="eyebrow">WHAT THIS MEANS FOR YOU</span>${b.meaning}</div></article>`,
    )
    .join("");
}
function renderBudget() {
  $("#budget-bars").innerHTML = [
    ["Health", 35],
    ["Roads", 25],
    ["Water", 20],
    ["Other services", 20],
  ]
    .map(
      ([name, value]) =>
        `<div class="budget-row"><a href="#budget-source" data-budget-source><span>${name}</span><b>${value} / 100 KSh ↗</b></a><div class="bar-track" role="img" aria-label="Illustrative ${name} share ${value} percent"><div class="bar-fill" style="--value:${value}%"></div></div></div>`,
    )
    .join("");
}
function renderCounties() {
  $("#county-grid").innerHTML = COUNTIES.map(
    (c, i) =>
      `<button data-county="${esc(c)}" aria-pressed="${selectedCounty === c}" aria-label="${String(i + 1).padStart(3, "0")} ${esc(c)} county"><span>${String(i + 1).padStart(2, "0")}</span>${esc(c)}</button>`,
  ).join("");
  const local = stories.filter((s) => s.counties.includes(selectedCounty));
  $("#county-detail").innerHTML =
    `<span class="eyebrow">COUNTY ${String(COUNTIES.indexOf(selectedCounty) + 1).padStart(3, "0")} / SAMPLE DESK</span><h3>${esc(selectedCounty)}</h3><h4>Governor & assembly</h4><p>Live officeholder and assembly reporting is not connected. No named politician is being depicted.</p><h4>Local case files</h4>${local.length ? local.map((s) => `<p><button class="card-title" data-open="${s.id}">${esc(headline(s))} ↗</button></p>`).join("") : '<p lang="sw">Kimya kabisa. Hakuna habari mpya.</p>'}<h4>Bills & budget highlights</h4><p>No verified local bill or budget feed yet. Start with the <a href="https://cob.go.ke/" target="_blank" rel="noopener">Controller of Budget</a> and the county’s official records.</p><button data-filter-county="${esc(selectedCounty)}" class="button-ink">Browse this county’s wire →</button>`;
}
const factChecks = [
  {
    verdict: "VERIFIED",
    claim: "“The sample chart adds up to 100.”",
    answer:
      "Ukweli: 35 + 25 + 20 + 20 = 100. Verified arithmetic in our illustrative chart, not a claim about a real budget.",
    source: "#money",
    label: "Illustrative chart on this page",
  },
  {
    verdict: "MISLEADING",
    claim: "“That sample allocation is money already spent.”",
    answer:
      "Ukweli: our example is labelled a planned allocation. Presenting it as expenditure changes its meaning.",
    source: "#money",
    label: "Sample chart and its labels",
  },
  {
    verdict: "FALSE",
    claim: "“This sample market-fee bill is already law.”",
    answer:
      "Ukweli: the bill is fictional. It has no official bill number and has not been enacted.",
    source: "#bunge",
    label: "Sample bill tracker",
  },
  {
    verdict: "UNVERIFIED",
    claim: "“This undated screenshot proves a scandal.”",
    answer:
      "Ukweli: the fictional screenshot has no original document or date attached. We cannot establish the claim.",
    source: "#story=viral-screenshot",
    label: "Case file: viral screenshot",
  },
];
function renderFacts() {
  $("#fact-grid").innerHTML = factChecks
    .map(
      (f) =>
        `<article class="panel fact-card"><span class="eyebrow">TETESI / SAMPLE CLAIM</span><h3>${esc(f.claim)}</h3><span class="stamp ${f.verdict.toLowerCase()}" data-stamp>${f.verdict}</span><p>${esc(f.answer)}</p><details><summary>↶ Reveal the source</summary><a href="${f.source}">${esc(f.label)} ↗</a><p class="meta">Checked: 19 Sep 2026 · sample evidence only.</p></details></article>`,
    )
    .join("");
  const observer = new IntersectionObserver(
    (entries) =>
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("slam");
          observer.unobserve(entry.target);
        }
      }),
    { threshold: 0.5 },
  );
  document
    .querySelectorAll("[data-stamp]")
    .forEach((el) => observer.observe(el));
}
function renderSatire() {
  $("#satire-strip").innerHTML = [
    {
      caption: "SATIRE · THE ANNOUNCEMENT",
      bubble: "We have a plan for the plan!",
      sfx: "BAM!",
      character: "Mheshimiwa",
      type: "shout",
    },
    {
      caption: "SATIRE · AT THE MARKET",
      bubble: "Lovely. Can I pay rent with the plan?",
      sfx: "ATI NINI?!",
      character: "Mama Mboga",
      type: "speak",
    },
    {
      caption: "SATIRE · THE FOLLOW-UP",
      bubble: "Let’s start with one receipt.",
      sfx: "WUEH!",
      character: "The Auditor",
      type: "think",
    },
  ]
    .map((p, i) =>
      panelMarkup(
        { ...p, art_note: "Satirical fictional archetype; not a real person." },
        i,
      ),
    )
    .join("");
}
function renderPoll() {
  const key = "poll:" + eatDate();
  const vote = read(key, null);
  $("#poll-options").innerHTML = ["Health", "Water", "Roads", "Education"]
    .map(
      (option) =>
        `<button class="poll-option" data-vote="${option}" style="--value:${vote === option ? "100" : "0"}%" aria-pressed="${vote === option}">${option}${vote === option ? "<b>✓ YOUR VOTE</b>" : ""}</button>`,
    )
    .join("");
  $("#poll-note").textContent = vote
    ? "Your one local vote is saved. Choose another option to change it. No public totals are collected."
    : "One tap. One vote on this device. No simulated audience results.";
}
function updateStreak(mark = false) {
  let streak = read("streak", { last: null, count: 0 });
  const today = eatDate();
  if (mark && streak.last !== today) {
    const yesterday = new Date(Date.parse(today) - 86400000)
      .toISOString()
      .slice(0, 10);
    streak = {
      last: today,
      count: streak.last === yesterday ? streak.count + 1 : 1,
    };
    write("streak", streak);
  }
  $("#streak").textContent = streak.count
    ? `Siku ${streak.count} mfululizo! · ${streak.count}-day reading streak`
    : "Open a case file to start your reading streak.";
}
function showDialog(id) {
  const dialog = $(id);
  if (!dialog.open) dialog.showModal();
  document.body.style.overflow = "hidden";
}
function closeDialog(dialog) {
  dialog.close();
  if (!document.querySelector("dialog[open]"))
    document.body.style.overflow = "";
  if (dialog.id === "reader" && location.hash.startsWith("#story="))
    history.replaceState(
      null,
      "",
      location.pathname + location.search + "#wire",
    );
}
function openStory(id, mode = "comic", index = 0) {
  const s = stories.find((s) => s.id === id || s.slug === id);
  if (!s) return;
  activeStory = s;
  readerMode = mode;
  panelIndex = Math.max(0, Math.min(index, s.panels.length - 1));
  renderReader();
  showDialog("#reader");
  history.replaceState(
    null,
    "",
    `#story=${s.slug}${index ? `&panel=${index + 1}` : ""}`,
  );
  updateStreak(true);
  navigator.serviceWorker?.controller?.postMessage({
    type: "READ_STORY",
    story: s,
  });
}
function renderReader() {
  const s = activeStory;
  if (!s) return;
  $("#reader-content").innerHTML =
    `<h2 id="reader-title" lang="${langAttr()}">${esc(headline(s))}</h2><div class="meta">${esc(s.byline)} · ${new Date(s.published_at).toLocaleString("en-GB", { timeZone: "Africa/Nairobi" })} EAT · ${s.read_mins} MIN READ</div><div class="reader-tabs" role="group" aria-label="Reading format"><button data-reader-mode="comic" aria-pressed="${readerMode === "comic"}">▦ Read as Comic</button><button data-reader-mode="article" aria-pressed="${readerMode === "article"}">≡ Read as Article</button></div>${readerMode === "comic" ? `<div id="reader-panel" class="page-flip">${panelMarkup(s.panels[panelIndex], panelIndex, { large: true, hideBubble: true })}</div><div class="reader-controls"><button id="prev-panel" ${panelIndex === 0 ? "disabled" : ""}>← Previous</button><button id="reveal-bubble">Reveal speech bubble</button><button id="next-panel" ${panelIndex === s.panels.length - 1 ? "disabled" : ""}>Next →</button><div class="progress-dots" aria-label="Comic panel navigation">${s.panels.map((_, i) => `<button data-panel="${i}" aria-label="Panel ${i + 1} of ${s.panels.length}" aria-current="${i === panelIndex}">${i === panelIndex ? "●" : "○"}</button>`).join("")}</div></div><p class="meta">Panel ${panelIndex + 1} of ${s.panels.length} · Swipe or use arrow keys. Tap the panel to reveal dialogue. Fictional characters; invented dialogue.</p>` : `<article class="article"><p class="sample-label">SAMPLE · AI-ASSISTED · NOT REPORTED NEWS</p>${s.body.map((p, i) => `<p>${esc(p)}</p>${i === 1 ? `<blockquote>“${esc(s.pull_quote)}”</blockquote>` : ""}`).join("")}</article>`}<div class="actions"><button data-save="${s.id}" aria-pressed="${saved.has(s.id)}">${saved.has(s.id) ? "◆ Saved" : "◇ Save story"}</button><button data-share="${s.id}">Share story ↗</button>${readerMode === "comic" ? `<button data-share="${s.id}" data-share-panel="${panelIndex}">Share this panel ↗</button>` : ""}<button data-listen-story="${s.id}" ${"speechSynthesis" in window ? "" : "hidden"}>▷ Listen</button><button data-desk data-context="${s.id}">Ask the Desk</button></div><details class="reader-sources"><summary>Reveal the sources & verification note</summary>${stamp(s)}<p>${esc(s.verification.note)}</p><ul>${s.sources.map((source) => `<li><a href="${esc(safeURL(source.url))}" target="_blank" rel="noopener">${esc(source.name)} ↗</a><span class="meta">${esc(source.scope)}<br>Source published: ${source.published_at ? esc(source.published_at.slice(0, 10)) : "not supplied by source"} · link checked ${esc(source.checked_at)}</span></li>`).join("")}</ul><a href="#corrections" data-close-reader>Corrections log</a></details>`;
}
function changePanel(index) {
  if (!activeStory) return;
  panelIndex = Math.max(0, Math.min(index, activeStory.panels.length - 1));
  renderReader();
  history.replaceState(
    null,
    "",
    `#story=${activeStory.slug}&panel=${panelIndex + 1}`,
  );
  $("#reveal-bubble").focus({ preventScroll: true });
}
function revealBubble() {
  const bubble = $("#reader-panel .speech");
  if (!bubble) return;
  bubble.hidden = false;
  $("#reveal-bubble").textContent = "Speech bubble revealed";
  $("#reveal-bubble").setAttribute("aria-pressed", "true");
}
function storyURL(s, panel = null) {
  return (
    CONFIG.canonicalURL +
    `#story=${encodeURIComponent(s.slug)}${panel === null ? "" : `&panel=${panel + 1}`}`
  );
}
function openShare(s, panel = null) {
  shareStory = s;
  sharePanel = panel;
  const url = storyURL(s, panel);
  const text = `SAMPLE EXPLAINER · ${headline(s)}${panel === null ? "" : ` — panel ${panel + 1}`} | The Ngesa Chronicle. Fictional scenario, not live news.`;
  $("#share-content").innerHTML =
    `<p lang="${langAttr()}">${esc(headline(s))}</p><span class="sample-label">${panel === null ? "STORY" : `PANEL ${panel + 1}`} · SAMPLE</span><div class="share-options"><a target="_blank" rel="noopener" href="https://wa.me/?text=${encodeURIComponent(text + " " + url)}">WhatsApp ↗</a><a target="_blank" rel="noopener" href="https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}">X ↗</a><a target="_blank" rel="noopener" href="https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}">Facebook ↗</a><a target="_blank" rel="noopener" href="https://t.me/share/url?url=${encodeURIComponent(url)}&text=${encodeURIComponent(text)}">Telegram ↗</a><button id="copy-link">Copy link</button><button id="download-card">↓ 1080 × 1080 card</button></div><p class="meta">Download the card for WhatsApp, TikTok or your story. The image includes its SAMPLE label and source link. Social links open your composer; nothing posts automatically.</p><label for="share-url">Direct link</label><input id="share-url" readonly value="${esc(url)}">`;
  showDialog("#share");
}
async function downloadCard() {
  const s = shareStory;
  if (!s) return;
  const canvas = document.createElement("canvas");
  canvas.width = canvas.height = 1080;
  const ctx = canvas.getContext("2d");
  ctx.fillStyle = "#F4EEDF";
  ctx.fillRect(0, 0, 1080, 1080);
  ctx.strokeStyle = "#0B0B0B";
  ctx.lineWidth = 9;
  ctx.strokeRect(28, 28, 1024, 1024);
  ctx.fillStyle = "#0B0B0B";
  ctx.font = "bold 35px monospace";
  ctx.fillText("THE NGESA", 65, 100);
  ctx.fillStyle = "#B21035";
  ctx.fillText("CHRONICLE", 65, 150);
  ctx.fillStyle = "#FFC61A";
  ctx.fillRect(65, 185, 950, 50);
  ctx.fillStyle = "#0B0B0B";
  ctx.font = "bold 24px monospace";
  ctx.fillText("SAMPLE · FICTIONAL EXPLAINER · NOT LIVE NEWS", 80, 219);
  const text = sharePanel === null ? headline(s) : s.panels[sharePanel].caption;
  ctx.font = "bold 62px sans-serif";
  let y = 325;
  function wrap(text, x, y, maxWidth, lineHeight) {
    let line = "";
    for (const word of text.split(" ")) {
      const test = line + word + " ";
      if (ctx.measureText(test).width > maxWidth && line) {
        ctx.fillText(line, x, y);
        line = word + " ";
        y += lineHeight;
      } else line = test;
    }
    ctx.fillText(line, x, y);
    return y + lineHeight;
  }
  y = wrap(text.toUpperCase(), 65, y, 950, 75);
  ctx.fillStyle = "#E9E0CB";
  ctx.fillRect(65, y + 15, 950, 260);
  ctx.strokeRect(65, y + 15, 950, 260);
  ctx.font = "italic 34px Georgia";
  ctx.fillStyle = "#0B0B0B";
  wrap(
    sharePanel === null
      ? s.brief[preferences.lang]
      : `“${s.panels[sharePanel].bubble}” — ${s.panels[sharePanel].character} (fictional)`,
    90,
    y + 85,
    900,
    47,
  );
  ctx.font = "20px monospace";
  ctx.fillText("POLITICS, DRAWN IN INK. / SOURCES IN THE CASE FILE", 65, 910);
  ctx.font = "18px monospace";
  wrap(storyURL(s, sharePanel), 65, 957, 950, 26);
  canvas.toBlob((blob) => {
    if (!blob) {
      toast("Could not create the card. Try again.");
      return;
    }
    const a = document.createElement("a");
    const url = URL.createObjectURL(blob);
    a.href = url;
    a.download = `ngesa-${s.slug}${sharePanel === null ? "" : `-panel-${sharePanel + 1}`}.png`;
    a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  }, "image/png");
}
function openDesk(context) {
  if (context) $("#desk-story").value = context;
  showDialog("#desk");
}
function answerDesk(question) {
  const s = stories.find((s) => s.id === $("#desk-story").value) || stories[0];
  const query = question.toLowerCase();
  let answer;
  if (/county|kaunti/.test(query))
    answer = `For ${selectedCounty}: this is a generic fictional explainer, not a local finding. ${s.brief.en} No live county records are attached, so the desk cannot claim a local impact.`;
  else if (/bill|mswada/.test(query))
    answer =
      s.beat === "Bunge" || s.beat === "Senate"
        ? `This sample bill is fictional. ${s.brief.en} Its displayed stage is illustrative, not an official Parliamentary status. Read the legislative-process source below.`
        : "This case file is not a bill. Select a Bunge or Senate case file for the sample legislative explanation.";
  else if (/explain|summari|5|five|eleza|summary/.test(query))
    answer = s.brief.en + " " + s.body[2];
  else
    answer =
      "I cannot establish that from the attached sample material. I will not invent a fact or quote. Try one of the prepared questions, or read the official background source below.";
  const message = document.createElement("div");
  message.className = "desk-message";
  message.innerHTML = `<span class="eyebrow">AI-GENERATED · SOURCE-ONLY DEMO</span><p><b>${esc(question)}</b></p><p>${esc(answer)}</p><p class="meta">Context: SAMPLE / ${esc(s.headline.en)}. Prepared extract, not a live AI response.</p>${sourceChips(s)}`;
  $("#desk-messages").append(message);
  message.scrollIntoView({ block: "nearest" });
  $("#desk-question").value = "";
}
function listen(text) {
  if (!("speechSynthesis" in window)) return;
  if (speaking) {
    speechSynthesis.cancel();
    speaking = false;
    $("#listen").textContent = "▷ Listen";
    return;
  }
  const u = new SpeechSynthesisUtterance(text);
  u.lang = preferences.lang === "en" ? "en-KE" : "sw-KE";
  u.rate = 0.92;
  u.onend = u.onerror = () => {
    speaking = false;
    $("#listen").textContent = "▷ Listen";
  };
  speechSynthesis.speak(u);
  speaking = true;
  $("#listen").textContent = "■ Stop listening";
}
function info(kind) {
  let title, html;
  if (kind === "tip") {
    title = "Got a claim?";
    html =
      '<p>The WhatsApp tip line is a placeholder in this sample edition. A newsroom number has not been configured.</p><p>Do not send sensitive or private information here. No claim will be submitted.</p><button id="copy-tip-template">Copy a claim-check template</button>';
  } else {
    title = "Stay in the loop.";
    html =
      "<p>The newsletter and WhatsApp channel are not connected yet. No email addresses are collected in this preview.</p><p>You can install the Chronicle for offline reading or save case files on this device.</p>";
  }
  $("#info-title").textContent = title;
  $("#info-content").innerHTML = html;
  showDialog("#info");
}
async function copy(text) {
  try {
    await navigator.clipboard.writeText(text);
    toast("Copied. Sasa, share the receipts.");
  } catch {
    toast("Copy is unavailable. Select and copy the visible link.");
    $("#share-url")?.select();
  }
}
function route() {
  const match = location.hash.match(/^#story=([^&]+)(?:&panel=(\d+))?/);
  if (match) {
    const s = stories.find((s) => s.slug === decodeURIComponent(match[1]));
    if (s) openStory(s.id, "comic", Number(match[2] || 1) - 1);
  } else {
    const target = document.getElementById(location.hash.slice(1));
    if (target?.tagName === "DETAILS") target.open = true;
  }
}
function refreshLanguage() {
  renderHero();
  renderTicker();
  renderBrief();
  renderWire();
  renderCounties();
  if (activeStory) renderReader();
  $("#desk-story").innerHTML = stories
    .map((s) => `<option value="${s.id}">${esc(headline(s))}</option>`)
    .join("");
}
document.addEventListener("click", (e) => {
  const el = e.target.closest("button,a");
  if (!el) return;
  if (el.hasAttribute("data-close")) {
    closeDialog(el.closest("dialog"));
    return;
  }
  if (el.dataset.lang) {
    preferences.lang = el.dataset.lang;
    applyPreferences();
    persistPreferences();
    refreshLanguage();
    return;
  }
  if (el.dataset.open) {
    e.preventDefault();
    openStory(el.dataset.open, el.dataset.mode || "comic");
    return;
  }
  if (el.dataset.save) {
    saved.has(el.dataset.save)
      ? saved.delete(el.dataset.save)
      : saved.add(el.dataset.save);
    write("saved", [...saved]);
    renderWire();
    if ($("#reader").open) renderReader();
    const saveScope = $("#reader").open ? "#reader" : "#wire-grid";
    document
      .querySelector(
        `${saveScope} [data-save="${CSS.escape(el.dataset.save)}"]`,
      )
      ?.focus({ preventScroll: true });
    toast(
      saved.has(el.dataset.save)
        ? "Saved on this device."
        : "Removed from saved stories.",
    );
    return;
  }
  if (el.dataset.share) {
    openShare(
      stories.find((s) => s.id === el.dataset.share),
      el.hasAttribute("data-share-panel")
        ? Number(el.dataset.sharePanel)
        : null,
    );
    return;
  }
  if (el.hasAttribute("data-desk")) {
    openDesk(el.dataset.context);
    return;
  }
  if (el.dataset.readerMode) {
    readerMode = el.dataset.readerMode;
    renderReader();
    document
      .querySelector(`[data-reader-mode="${readerMode}"]`)
      ?.focus({ preventScroll: true });
    return;
  }
  if (el.hasAttribute("data-panel")) {
    changePanel(Number(el.dataset.panel));
    return;
  }
  if (el.dataset.county) {
    selectedCounty = el.dataset.county;
    renderCounties();
    document
      .querySelector(`[data-county="${CSS.escape(selectedCounty)}"]`)
      ?.focus({ preventScroll: true });
    return;
  }
  if (el.dataset.filterCounty) {
    $("#county-filter").value = el.dataset.filterCounty;
    limit = 6;
    renderWire();
    $("#wire").scrollIntoView();
    return;
  }
  if (el.dataset.beat) {
    $("#beat-filter").value = el.dataset.beat;
    limit = 6;
    renderWire();
  }
  if (el.dataset.vote) {
    write("poll:" + eatDate(), el.dataset.vote);
    renderPoll();
    document
      .querySelector(`[data-vote="${CSS.escape(el.dataset.vote)}"]`)
      ?.focus({ preventScroll: true });
    return;
  }
  if (el.dataset.prompt) {
    answerDesk(el.dataset.prompt);
    return;
  }
  if (el.dataset.info) {
    info(el.dataset.info);
    return;
  }
  if (el.dataset.report) {
    write("reports", [
      ...read("reports", []),
      { item: el.dataset.report, at: new Date().toISOString() },
    ]);
    toast("Flag saved on this device. No report was sent to a newsroom.");
    return;
  }
  if (el.dataset.listenStory) {
    const s = stories.find((s) => s.id === el.dataset.listenStory);
    listen(`Sample fictional explainer. ${headline(s)}. ${s.body.join(" ")}`);
    return;
  }
  if (el.hasAttribute("data-budget-source")) {
    e.preventDefault();
    const details = $("#money details");
    details.id = "budget-source";
    details.open = true;
    details.scrollIntoView({ block: "center" });
    return;
  }
  if (el.hasAttribute("data-close-reader")) {
    closeDialog($("#reader"));
    $("#corrections").open = true;
  }
  switch (el.id) {
    case "theme":
      preferences.theme = preferences.theme === "dark" ? "light" : "dark";
      applyPreferences();
      persistPreferences();
      break;
    case "saver":
      preferences.saver = !preferences.saver;
      applyPreferences();
      persistPreferences();
      break;
    case "text-size":
      preferences.text = preferences.text === "normal" ? "large" : "normal";
      applyPreferences();
      persistPreferences();
      break;
    case "ticker-pause": {
      const paused = $(".ticker").classList.toggle("paused");
      el.setAttribute("aria-pressed", paused);
      el.setAttribute(
        "aria-label",
        paused ? "Resume breaking wire" : "Pause breaking wire",
      );
      el.textContent = paused ? "▷" : "Ⅱ";
      break;
    }
    case "load-more":
      limit += 6;
      renderWire();
      break;
    case "saved-filter":
      savedOnly = !savedOnly;
      limit = 6;
      renderWire();
      break;
    case "prev-panel":
      changePanel(panelIndex - 1);
      break;
    case "next-panel":
      changePanel(panelIndex + 1);
      break;
    case "reveal-bubble":
      revealBubble();
      break;
    case "copy-link":
      copy(storyURL(shareStory, sharePanel));
      break;
    case "download-card":
      downloadCard();
      break;
    case "copy-tip-template":
      copy(
        "Claim to check:\nOriginal source/link:\nDate seen:\nWhat needs verification:\nPublic evidence (no private data):",
      );
      break;
    case "listen":
      listen(
        "Sample edition. " +
          stories
            .slice(0, 5)
            .map((s) => s.brief[preferences.lang])
            .join(" "),
      );
      break;
    case "brief-share": {
      const text =
        "SAMPLE EDITION · Today in 60 seconds: " +
        stories
          .slice(0, 5)
          .map((s) => s.brief[preferences.lang])
          .join(" ") +
        " " +
        CONFIG.canonicalURL +
        "#brief";
      window.open(
        "https://wa.me/?text=" + encodeURIComponent(text),
        "_blank",
        "noopener",
      );
      break;
    }
    case "install":
      if (installPrompt) {
        installPrompt.prompt();
        installPrompt.userChoice.then(() => {
          installPrompt = null;
          el.hidden = true;
        });
      }
      break;
    case "retry-load":
      init();
      break;
  }
});
$("#filters").addEventListener("change", () => {
  limit = 6;
  renderWire();
});
$("#filters").addEventListener("reset", () => {
  setTimeout(() => {
    savedOnly = false;
    limit = 6;
    renderWire();
  }, 0);
});
$("#desk-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const q = $("#desk-question").value.trim();
  if (q) answerDesk(q);
});
$("#voice-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const text = $("#voice").value.trim();
  if (!text) return;
  const ok = write("voice-draft", {
    text,
    status: "awaiting local review",
    at: new Date().toISOString(),
  });
  $("#voice-status").textContent = ok
    ? "Draft saved on this device. A newsroom connection is needed before submission or moderation."
    : "Storage is unavailable. Copy your draft before leaving this page.";
});
$("#voice").value = read("voice-draft", {}).text || "";
document.querySelectorAll("dialog").forEach((dialog) => {
  dialog.addEventListener("close", () => {
    if (!document.querySelector("dialog[open]"))
      document.body.style.overflow = "";
    if (dialog.id === "reader") {
      if (location.hash.startsWith("#story="))
        history.replaceState(
          null,
          "",
          location.pathname + location.search + "#wire",
        );
      if ("speechSynthesis" in window) speechSynthesis.cancel();
      speaking = false;
    }
  });
});
document.addEventListener("keydown", (e) => {
  if (
    !$("#reader").open ||
    $("#desk").open ||
    $("#share").open ||
    readerMode !== "comic" ||
    /INPUT|TEXTAREA|SELECT/.test(e.target.tagName)
  )
    return;
  if (e.key === "ArrowRight") {
    e.preventDefault();
    changePanel(panelIndex + 1);
  }
  if (e.key === "ArrowLeft") {
    e.preventDefault();
    changePanel(panelIndex - 1);
  }
});
let touchStart = null;
$("#reader").addEventListener(
  "touchstart",
  (e) => {
    if (e.target.closest("#reader-panel"))
      touchStart = {
        x: e.changedTouches[0].clientX,
        y: e.changedTouches[0].clientY,
      };
  },
  { passive: true },
);
$("#reader").addEventListener(
  "touchend",
  (e) => {
    if (!touchStart) return;
    const dx = e.changedTouches[0].clientX - touchStart.x,
      dy = e.changedTouches[0].clientY - touchStart.y;
    touchStart = null;
    if (Math.abs(dx) > 55 && Math.abs(dx) > Math.abs(dy))
      changePanel(panelIndex + (dx < 0 ? 1 : -1));
  },
  { passive: true },
);
$("#reader").addEventListener("click", (e) => {
  if (e.target.closest("#reader-panel")) revealBubble();
});
window.addEventListener("hashchange", route);
window.addEventListener("beforeinstallprompt", (e) => {
  e.preventDefault();
  installPrompt = e;
  $("#install").hidden = false;
});
function networkStatus() {
  $("#offline-status").textContent = navigator.onLine
    ? "Online · offline reading available after cache setup"
    : "Offline · showing saved sample edition";
}
window.addEventListener("online", networkStatus);
window.addEventListener("offline", networkStatus);
networkStatus();
async function init() {
  try {
    stories = await loadStories();
    $("#beat-filter").innerHTML =
      '<option value="">All beats</option>' +
      BEATS.map((b) => `<option>${esc(b)}</option>`).join("");
    $("#county-filter").innerHTML =
      '<option value="">All 47 counties</option>' +
      COUNTIES.map((c) => `<option>${esc(c)}</option>`).join("");
    refreshLanguage();
    renderBills();
    renderBudget();
    renderFacts();
    renderSatire();
    renderPoll();
    updateStreak();
    $("#listen").hidden = !("speechSynthesis" in window);
    route();
    if ("serviceWorker" in navigator) {
      try {
        const reg = await navigator.serviceWorker.register("./sw.js");
        await navigator.serviceWorker.ready;
        $("#offline-status").textContent =
          "Offline reading ready · last 20 opened stories";
        reg.active?.postMessage({ type: "EDITION_READY" });
        if (activeStory)
          reg.active?.postMessage({ type: "READ_STORY", story: activeStory });
      } catch {
        $("#offline-status").textContent =
          "Offline cache unavailable in this browser";
      }
    }
  } catch (error) {
    $("#hero").innerHTML =
      '<div class="empty"><h1 lang="sw">Wueh! Network imekataa.</h1><p lang="sw">Jaribu tena.</p><button id="retry-load">Try again</button></div>';
    console.error(error);
  }
}
init();
