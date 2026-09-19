# The Ngesa Chronicle

**POLITICS, DRAWN IN INK.** A mobile-first, non-partisan Kenyan graphic news wire.

This edition ships ten clearly labelled **SAMPLE** civic scenarios. It does not claim to report real events. Official links provide civic context, not corroboration of fictional incidents. Satire and invented archetype dialogue are labelled; no real politician is caricatured or given invented quotes.

## Run and work on it

```sh
npm run dev
# Open http://127.0.0.1:4173
npm test
```

No install or build is required. GitHub Pages can serve the repository root. The political site is authored directly in `index.html`, `styles.css`, `app.js`, `art.js` and `data.js`. The older Python page builders and horror/podcast assets are legacy material and are not used by the new page. Do not regenerate this page with the legacy builders.

## Included

- Cream newsprint and Midnight Noir, responsive layouts, CSS halftone/grain, original inline SVG archetypes, 44px controls, visible focus and reduced-motion support.
- EN / SW / Sheng headlines and 60-second briefs. These preferences, theme, Data Saver and text size persist with guarded local storage.
- Five-panel brief; full-screen 4–6-panel case files with swipe/arrow navigation, dialogue reveal and an article view; source disclosure and timestamps.
- Beat/county/saved filters, load more, reading streak, WhatsApp/X/Facebook/Telegram links, copy link and 1080-square PNG story/panel exports.
- Bunge sample bill trackers; a clearly illustrative public-money chart; all 47 counties; election countdown; example fact-check verdicts; labelled satire; local poll and reader draft.
- Installable PWA, offline edition, and a rolling cache of the last 20 distinct opened stories. Service-worker scope works under `/ngesa-diaries/`. Offline fonts use system fallbacks. Data Saver avoids remote fonts, texture and animations.
- Trust policy, non-partisan pledge, correction log, moderation guidelines and a source-grounded desk demo that abstains on unsupported questions.

## What is a demo, and what needs a service

This is a static front end. There is **no live news feed, live LLM, public voting database, moderator service, newsletter subscription or configured WhatsApp tip/channel**. UI wording states these limits. Polls, reports and contribution drafts stay on the device; nothing is sent or silently published. The desk retrieves prepared explanations from selected sample records and cites their background links. It does not pretend to verify a new claim.

`CONFIG` in `data.js` holds the election date, canonical URL and connection placeholders. Use a server-side service for live AI (never a browser API key) and a reviewed moderation pipeline before allowing public posts. The site must continue to label AI output and uncertainty. Human moderation is required before publication.

## Swappable data layer

`data/stories.json` follows the requested Story shape plus `sample`, `brief` and `ai_assisted`. `data.js::loadStories()` is the only feed entry point. Source dates can be null when the official landing page supplies none, and the UI says so. Each source includes scope and a checked date.

To add a feed adapter, normalize records to this schema, validate source URLs and preserve clear provenance. Use only headlines, licensed snippets and outbound links under each outlet’s terms. Official documents should link to the specific record, not merely a home page, before a real story is marked verified. Never turn SAMPLE fixtures into live news by simply changing the badge.

`art.js` exposes a panel renderer with per-panel `art_note` and a factual ID-card renderer requiring a credited photo or initials. All current cast members are fictional archetypes.

## Civic references

- [IEBC election operation plan](https://www.iebc.or.ke/uploads/resources/tpFfOlBLRh.pdf): scheduled General Election, Tuesday **10 August 2027**. The countdown uses a single EAT config timestamp. Checked 19 September 2026.
- [IEBC registration requirements](https://x.com/IEBCKenya/status/2039724205428646156/photo/1). Current windows and centres must be confirmed through IEBC.
- [How Parliament works](https://www.parliament.go.ke/How_Parliament_Works). The compact tracker is a simplified overview; its note distinguishes early committee scrutiny from Committee of the Whole House/Report stages.
- [Kenya Law](https://new.kenyalaw.org/akn/ke/act/2010/constitution), [Controller of Budget](https://cob.go.ke/) and [Auditor-General](https://www.oagkenya.go.ke/).

## Validation

`npm test` validates sample-data completeness, translations, dates, county coverage, HTML escaping, the startup asset budget and a simulated offline cache, including retention after a new edition arrives. Browser acceptance checks cover 320, 360, 390, 768, 1024, 1440 and 1920px, saved preferences, reader navigation, filtering, sharing and source-only desk replies. A comprehensive accessibility audit and real-device PWA/offline tests remain recommended before a live newsroom launch.

Code and original artwork: MIT. Editor: NGESA.
