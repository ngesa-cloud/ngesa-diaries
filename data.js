// Replace loadStories() with a licensed feed adapter. Keep this normalized shape.
// Never imply source landing pages corroborate a reported incident.
export const CONFIG = Object.freeze({
  electionDate: "2027-08-10T00:00:00+03:00",
  electionSource: "https://www.iebc.or.ke/uploads/resources/tpFfOlBLRh.pdf",
  canonicalURL: "https://ngesa-cloud.github.io/ngesa-diaries/",
  whatsappTipURL: null,
  newsletterURL: null,
  whatsappChannelURL: null,
  moderationEndpoint: null,
  aiEndpoint: null,
  sampleEdition: true,
  offlineStoryLimit: 20,
});
export const COUNTIES = [
  "Mombasa",
  "Kwale",
  "Kilifi",
  "Tana River",
  "Lamu",
  "Taita Taveta",
  "Garissa",
  "Wajir",
  "Mandera",
  "Marsabit",
  "Isiolo",
  "Meru",
  "Tharaka Nithi",
  "Embu",
  "Kitui",
  "Machakos",
  "Makueni",
  "Nyandarua",
  "Nyeri",
  "Kirinyaga",
  "Murang’a",
  "Kiambu",
  "Turkana",
  "West Pokot",
  "Samburu",
  "Trans Nzoia",
  "Uasin Gishu",
  "Elgeyo Marakwet",
  "Nandi",
  "Baringo",
  "Laikipia",
  "Nakuru",
  "Narok",
  "Kajiado",
  "Kericho",
  "Bomet",
  "Kakamega",
  "Vihiga",
  "Bungoma",
  "Busia",
  "Siaya",
  "Kisumu",
  "Homa Bay",
  "Migori",
  "Kisii",
  "Nyamira",
  "Nairobi",
];
export const BEATS = [
  "Bunge",
  "Senate",
  "Executive",
  "Counties",
  "Elections",
  "Public Money",
  "Mahakama",
  "Integrity",
  "Citizen Voices",
];
export async function loadStories() {
  const response = await fetch(new URL("./data/stories.json", import.meta.url));
  if (!response.ok) throw new Error("Stories unavailable");
  const records = await response.json();
  if (!Array.isArray(records)) throw new Error("Invalid story feed");
  return records.map((story) => {
    if (
      !story.id ||
      !story.slug ||
      !story.headline?.en ||
      !Array.isArray(story.sources) ||
      story.panels?.length < 4 ||
      story.panels?.length > 6
    )
      throw new Error("Invalid case file");
    return story;
  });
}
export function eatDate(date = new Date()) {
  return new Intl.DateTimeFormat("en-CA", {
    timeZone: "Africa/Nairobi",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(date);
}
export function electionDays(now = Date.now()) {
  return Math.max(
    0,
    Math.ceil((new Date(CONFIG.electionDate).getTime() - now) / 86400000),
  );
}
export function timeAgo(timestamp, now = Date.now()) {
  const minutes = Math.floor((now - new Date(timestamp).getTime()) / 60000);
  if (minutes < 0) return "sample release";
  if (minutes < 60) return `${minutes}m ago`;
  if (minutes < 1440) return `${Math.floor(minutes / 60)}h ago`;
  return `${Math.floor(minutes / 1440)}d ago`;
}
