// Lightweight, original archetype artwork. Never a likeness of a real public figure.
const bodies = {
  Mwananchi: `<path d="M95 210q3-64 42-81l48 1q38 17 45 80" fill="var(--paper)"/><path d="M137 132l24 34 24-34M159 166v44M128 151l-6 58M192 150l11 59"/><path d="M106 191l-43-29 14-18 53 28" fill="var(--paper)"/><path d="M52 129l35 7-6 37-35-7z" fill="var(--marigold)"/>`,
  "Mama Mboga": `<path d="M93 213q7-66 42-83h50q36 23 44 83" fill="var(--paper)"/><path d="M131 131l29 30 28-29 17 78H112z" fill="var(--paper-2)"/><path d="M140 158h39v43h-39z" fill="var(--marigold)"/><path d="M26 212h252v24H26z" fill="var(--paper)"/><path d="M39 211q7-36 27-7 17-37 32 7M213 211q13-32 28-6 19-31 30 6" fill="var(--paper-2)"/><path d="M52 185l10 13m-5-19 4 18m167-14 7 12"/>`,
  Mheshimiwa: `<path d="M89 214l15-62 38-23h36l38 23 17 62" fill="currentColor"/><path d="M140 128l20 48 20-48-4 83h-33z" fill="var(--paper)"/><path d="M156 145h9l4 40-9 17-8-17z" fill="currentColor"/><path d="M126 138l-10 32 20 8-13 18m71-58 12 32-20 8 14 18" stroke="var(--paper)"/><circle cx="193" cy="156" r="4" fill="var(--marigold)"/><path d="M53 213h211v24H53z" fill="var(--paper-2)"/><path d="M216 213v-31l-13-17"/>`,
  Mzee: `<path d="M96 213q2-60 42-81h40q40 15 47 81" fill="var(--paper)"/><path d="M135 134l25 30 25-30m-26 30v50"/><path d="M128 139l-14 74h28l-3-59m43-14 17 73h-24l-1-61" fill="var(--paper-2)"/><path d="M239 236v-70q0-18-13-10" fill="none"/>`,
  "The Auditor": `<path d="M90 213l14-58 33-22h43l29 21 23 59" fill="var(--paper)"/><path d="M137 135l22 28 22-28m-22 28v50M107 174l28 8-8 21-29-8"/><path d="M191 168l34-24 11 15-36 35" fill="var(--paper-2)"/><circle cx="235" cy="121" r="25" fill="var(--paper)"/><circle cx="235" cy="121" r="17" fill="var(--marigold)"/><path d="M222 144l-13 27" stroke-width="8"/>`,
};
export function illustration(character = "Mwananchi") {
  const head =
    character === "Mama Mboga"
      ? `<path d="M128 94q-8-42 30-44 38-3 36 41l-14 14-43-2z" fill="var(--marigold)"/><path d="M130 72l62 14m-60-21 38 20"/><path d="M136 91v20q23 35 45 0V91" fill="currentColor"/>`
      : character === "Mzee"
        ? `<path d="M130 79q5-23 28-22 28 1 30 23z" fill="var(--paper-2)"/><path d="M134 83h50v27l-12 22h-25l-13-22z" fill="currentColor"/><path d="M143 111l16 21 17-21" fill="var(--paper)"/>`
        : `<path d="M132 88q-4-36 26-36 35-2 32 36l-7 28-23 15-23-16z" fill="currentColor"/>`;
  return `<svg class="illustration" viewBox="0 0 310 240" aria-hidden="true" focusable="false" xmlns="http://www.w3.org/2000/svg"><g fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"><g opacity=".24"><path d="M7 92l81 26M20 32l86 57M84 9l31 58M279 29l-62 48M300 77l-71 25M14 148l73 5M260 182l43 14M44 228h220"/><path d="M26 113h38m190-64 16-10M58 71l21 10"/></g>${bodies[character] || bodies.Mwananchi}${head}<path d="M142 122v13m35-14v13"/></g></svg>`;
}
export const escapeHTML = (value) =>
  String(value ?? "").replace(
    /[&<>"']/g,
    (c) =>
      ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[
        c
      ],
  );
export function panelMarkup(panel, index = 0, options = {}) {
  const esc = escapeHTML;
  return `<div class="comic-panel ${options.large ? "wide-art" : ""}" role="img" aria-label="${esc(`Panel ${index + 1}. Fictional ${panel.character}. ${panel.caption} Dialogue: ${panel.bubble}`)}" data-art-note="${esc(panel.art_note)}"><span class="panel-number" aria-hidden="true">${String(index + 1).padStart(2, "0")}</span>${illustration(panel.character)}<span class="speech ${esc(panel.type || "speak")}" ${options.hideBubble ? "hidden" : ""} aria-hidden="true">“${esc(panel.bubble)}”</span>${panel.sfx ? `<span class="sfx" aria-hidden="true">${esc(panel.sfx)}</span>` : ""}<span class="caption" aria-hidden="true">${esc(panel.caption)}</span></div>`;
}
// For future factual profiles: no portrait or identity is invented.
export function idCardMarkup({ name, office, party, initials, photo, credit }) {
  const e = escapeHTML;
  const safePhoto = photo && /^https:\/\//.test(photo) && credit;
  return `<article class="id-card" aria-label="Factual officeholder profile"><div>${
    safePhoto
      ? `<img loading="lazy" width="64" height="64" src="${e(photo)}" alt="${e(name)}">`
      : `<span class="initials" aria-hidden="true">${e(
          initials ||
            name
              .split(" ")
              .map((n) => n[0])
              .slice(0, 2)
              .join(""),
        )}</span>`
  }</div><div><b>${e(name)}</b><p class="meta">${e(office)}</p>${party ? `<span class="chip">${e(party)}</span>` : ""}${safePhoto ? `<p class="meta">Photo: ${e(credit)}</p>` : ""}</div></article>`;
}
