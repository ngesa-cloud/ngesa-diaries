const VERSION = "ngesa-politics-v3";
const SHELL = VERSION + "-shell",
  READS = "ngesa-politics-reads";
const ASSETS = [
  "./",
  "./index.html",
  "./styles.css",
  "./app.js",
  "./data.js",
  "./art.js",
  "./data/stories.json",
  "./manifest.webmanifest",
  "./assets/ngesa-logo.jpg",
  "./assets/icon-192.png",
  "./assets/icon-512.png",
];
const resolve = (path) => new URL(path, self.registration.scope).href;
self.addEventListener("install", (event) =>
  event.waitUntil(
    caches
      .open(SHELL)
      .then((cache) => cache.addAll(ASSETS))
      .then(() => self.skipWaiting()),
  ),
);
self.addEventListener("activate", (event) =>
  event.waitUntil(
    caches
      .keys()
      .then((keys) =>
        Promise.all(
          keys
            .filter(
              (key) =>
                key.startsWith("ngesa-politics-") &&
                key !== SHELL &&
                key !== READS,
            )
            .map((key) => caches.delete(key)),
        ),
      )
      .then(() => self.clients.claim()),
  ),
);
async function offlineStories(cache) {
  const editionResponse = await cache.match(resolve("./data/stories.json"));
  const edition = editionResponse ? await editionResponse.json() : [];
  const reads = await caches.open(READS),
    records = [];
  for (const key of await reads.keys()) {
    const response = await reads.match(key);
    records.push(await response.json());
  }
  // Keep current edition ordering; preserve any previously opened item no longer in the feed.
  const ids = new Set(edition.map((s) => s.id));
  return new Response(
    JSON.stringify([...edition, ...records.filter((s) => !ids.has(s.id))]),
    { headers: { "Content-Type": "application/json" } },
  );
}
self.addEventListener("fetch", (event) => {
  const req = event.request,
    url = new URL(req.url);
  if (req.method !== "GET" || url.origin !== self.location.origin) return;
  const allowed = ASSETS.map(
    (asset) => new URL(asset, self.registration.scope).pathname,
  );
  if (req.mode !== "navigate" && !allowed.includes(url.pathname)) return;
  event.respondWith(
    (async () => {
      const cache = await caches.open(SHELL);
      try {
        const response = await fetch(req);
        if (response.ok) await cache.put(req, response.clone());
        return response;
      } catch {
        if (
          url.pathname ===
          new URL("./data/stories.json", self.registration.scope).pathname
        )
          return offlineStories(cache);
        const cached = await cache.match(req);
        if (cached) return cached;
        if (req.mode === "navigate")
          return await cache.match(resolve("./index.html"));
        return new Response("Offline resource unavailable", { status: 503 });
      }
    })(),
  );
});
let readQueue = Promise.resolve();
self.addEventListener("message", (event) => {
  if (event.data?.type !== "READ_STORY") return;
  const story = event.data.story;
  if (!story?.id || !story?.slug) return;
  readQueue = readQueue
    .catch(() => {})
    .then(async () => {
      const cache = await caches.open(READS),
        key = resolve("./__offline_story__/" + encodeURIComponent(story.id));
      await cache.delete(key);
      await cache.put(
        key,
        new Response(JSON.stringify(story), {
          headers: { "Content-Type": "application/json" },
        }),
      );
      const keys = await cache.keys();
      while (keys.length > 20) await cache.delete(keys.shift());
    });
  event.waitUntil(readQueue);
});
