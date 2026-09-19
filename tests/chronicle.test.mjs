import test from "node:test";
import assert from "node:assert/strict";
import { readFile, stat } from "node:fs/promises";
import vm from "node:vm";
import { COUNTIES, CONFIG, eatDate, electionDays } from "../data.js";
import { panelMarkup, idCardMarkup } from "../art.js";
const stories = JSON.parse(
  await readFile(new URL("../data/stories.json", import.meta.url), "utf8"),
);
test("Ten explicit fictional stories have complete translated headlines, briefs, evidence and 4–6 accessible panels", () => {
  assert.equal(stories.length, 10);
  assert.equal(new Set(stories.map((s) => s.slug)).size, 10);
  for (const s of stories) {
    assert.equal(s.sample, true);
    assert.equal(s.verification.status, "UNVERIFIED");
    assert.match(s.published_at, /\+03:00$/);
    for (const lang of ["en", "sw", "sheng"]) {
      assert.ok(s.headline[lang]);
      assert.ok(s.brief[lang]);
    }
    assert.ok(s.panels.length >= 4 && s.panels.length <= 6);
    assert.ok(s.body.length >= 4);
    assert.ok(s.sources.length);
    for (const src of s.sources) {
      assert.equal(new URL(src.url).protocol, "https:");
      assert.match(src.scope, /background/i);
    }
    for (const county of s.counties)
      assert.ok(COUNTIES.includes(county) || county === "All counties");
    for (const p of s.panels) {
      assert.ok(p.art_note);
      assert.match(panelMarkup(p), /role="img" aria-label=/);
    }
  }
});
test("47 distinct counties and date calculations use EAT and one election constant", () => {
  assert.equal(COUNTIES.length, 47);
  assert.equal(new Set(COUNTIES).size, 47);
  assert.equal(COUNTIES[46], "Nairobi");
  assert.equal(eatDate(new Date("2026-09-18T21:15:00Z")), "2026-09-19");
  assert.equal(electionDays(Date.parse(CONFIG.electionDate)), 0);
  assert.equal(electionDays(Date.parse(CONFIG.electionDate) - 86400000), 1);
  assert.equal(electionDays(Date.parse(CONFIG.electionDate) + 86400000), 0);
});
test("Untrusted story text is escaped and credited factual profiles never invent portraits", () => {
  const html = panelMarkup({
    caption: "<script>x</script>",
    bubble: '" onclick="x',
    character: "Mwananchi",
    art_note: "<x>",
  });
  assert.ok(!html.includes("<script>"));
  assert.match(html, /&lt;script&gt;/);
  const profile = idCardMarkup({
    name: "Example Person",
    office: "Example office",
    party: "Example",
    photo: "javascript:alert(1)",
  });
  assert.ok(!profile.includes("<img"));
  assert.match(profile, /EP/);
});
test("Static startup assets stay below 275KB before remote fonts", async () => {
  const files = [
    "index.html",
    "styles.css",
    "app.js",
    "art.js",
    "data.js",
    "data/stories.json",
    "assets/ngesa-logo.jpg",
    "manifest.webmanifest",
    "sw.js",
    "assets/icon.svg",
    "assets/icon-192.png",
    "assets/icon-512.png",
  ];
  let bytes = 0;
  for (const file of files)
    bytes += (await stat(new URL("../" + file, import.meta.url))).size;
  assert.ok(bytes < 275_000, `Startup assets: ${bytes}`);
});
function workerHarness() {
  const stores = new Map(),
    events = {};
  let online = false;
  const key = (req) => (typeof req === "string" ? req : req.url);
  const caches = {
    async open(name) {
      if (!stores.has(name)) stores.set(name, new Map());
      const map = stores.get(name);
      return {
        async addAll() {},
        async put(req, res) {
          map.set(key(req), res.clone());
        },
        async match(req) {
          return map.get(key(req))?.clone();
        },
        async delete(req) {
          return map.delete(key(req));
        },
        async keys() {
          return [...map.keys()].map((url) => ({ url }));
        },
      };
    },
    async keys() {
      return [...stores.keys()];
    },
    async delete(name) {
      return stores.delete(name);
    },
  };
  const scope = "https://example.test/ngesa-diaries/";
  const self = {
    registration: { scope },
    location: { origin: "https://example.test" },
    clients: { async claim() {} },
    async skipWaiting() {},
    addEventListener(name, fn) {
      events[name] = fn;
    },
  };
  const fetch = async () => {
    if (!online) throw Error("Offline");
    return new Response(
      JSON.stringify([
        { ...stories[0], id: "new-edition", slug: "new-edition" },
      ]),
    );
  };
  return {
    stores,
    events,
    caches,
    scope,
    self,
    fetch,
    setOnline(v) {
      online = v;
    },
  };
}
test("Offline cache retains the last 20 distinct opened stories, including after an online edition refresh", async () => {
  const h = workerHarness();
  vm.runInNewContext(
    await readFile(new URL("../sw.js", import.meta.url), "utf8"),
    {
      self: h.self,
      caches: h.caches,
      fetch: h.fetch,
      URL,
      Response,
      Set,
      Promise,
    },
  );
  const install = [];
  h.events.install({ waitUntil: (p) => install.push(p) });
  await Promise.all(install);
  for (let i = 0; i < 25; i++) {
    let pending;
    h.events.message({
      data: {
        type: "READ_STORY",
        story: { ...stories[0], id: `read-${i}`, slug: `read-${i}` },
      },
      waitUntil: (p) => (pending = p),
    });
    await pending;
  }
  const reads = await h.caches.open("ngesa-politics-reads");
  assert.equal((await reads.keys()).length, 20);
  assert.ok(!(await reads.keys()).some((k) => k.url.endsWith("/read-4")));
  let responsePromise;
  const request = {
    url: h.scope + "data/stories.json",
    method: "GET",
    mode: "cors",
  };
  h.setOnline(true);
  h.events.fetch({ request, respondWith: (p) => (responsePromise = p) });
  await responsePromise;
  h.setOnline(false);
  h.events.fetch({ request, respondWith: (p) => (responsePromise = p) });
  const result = await (await responsePromise).json();
  assert.equal(result.length, 21);
  assert.equal(result[0].id, "new-edition");
  assert.ok(result.some((s) => s.id === "read-24"));
  assert.ok(result.some((s) => s.id === "read-5"));
});
