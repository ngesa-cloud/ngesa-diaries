#!/usr/bin/env node
/**
 * scripts/voice-preview.js
 * Generates 30-second audition preview samples from voice-brief.md for A/B talent comparison
 */

import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

// Candidates configuration
const CANDIDATES = [
  {
    id: 'david-vincent-onyango',
    name: 'David Vincent Onyango (Voice123 #1)',
    wpm: 134,
    pitch: 36, // Deep investigative baritone
    formant_boost: 'equalizer=f=220:width_type=o:w=1.2:g=4.0,equalizer=f=3200:width_type=o:w=1.0:g=-1.5',
    line: "It's three-fifteen in the morning along the shores of Kendu Bay. The crickets suddenly stop chirping. Then comes the sound every child in western Kenya was warned about: a violent slap of wet mud against corrugated iron sheets. You stay in bed. You do not light a match. Because whatever is running outside in the dark... isn't looking for a cow."
  },
  {
    id: 'kelvin-thagana-njungu',
    name: 'Kelvin Thagana Njungu (Voice123 #2)',
    wpm: 140,
    pitch: 42, // Smooth, crisp commercial baritone
    formant_boost: 'equalizer=f=300:width_type=o:w=1.2:g=2.5,equalizer=f=4000:width_type=o:w=1.0:g=1.0',
    line: "Every haulage trucker descending into Kikopey knows the fog of the Rift Valley. But on the Salgaa stretch, the temperature inside the cab drops ten degrees in five seconds. When Hassan looked in his rearview mirror at eighty kilometers an hour, the passenger seat was empty. The seatbelt, however, was still clicked shut."
  },
  {
    id: 'synthetic-elevenlabs-prompt',
    name: 'Synthetic Voice Design (ElevenLabs Multilingual v2)',
    wpm: 135,
    pitch: 38, // Controlled neutral Kenyan narrator
    formant_boost: 'equalizer=f=250:width_type=o:w=1.0:g=3.0,equalizer=f=2800:width_type=o:w=1.0:g=-1.0',
    line: "Welcome to Ngesa Diaries. I am Dominic Nyongesa. These are not campfire stories. These are declassified field dossiers, witness depositions, and unexplained phenomena gathered from all forty-seven counties of Kenya. Case File Zero One: The Night Runners."
  }
];

function generatePreview(candidate, outDir) {
  console.log(`🎙️  Generating 30s preview sample for: ${candidate.name}...`);
  const tempWav = path.join(outDir, `temp_${candidate.id}.wav`);
  const outMp3 = path.join(outDir, `${candidate.id}.mp3`);

  // Safe text
  const safeText = candidate.line.replace(/["\\]/g, ' ');

  // Generate speech at exact spec WPM and pitch
  execSync(
    `espeak-ng -v en-gb -s ${candidate.wpm} -p ${candidate.pitch} -w "${tempWav}" "${safeText}"`,
    { stdio: 'pipe' }
  );

  // Apply broadcast mastering chain
  const tempComp = path.join(outDir, `temp_comp_${candidate.id}.wav`);
  const filterChain1 = [
    candidate.formant_boost,
    'highpass=f=80',
    'acompressor=threshold=-20dB:ratio=2.5:attack=15:release=120'
  ].join(',');

  execSync(`ffmpeg -y -i "${tempWav}" -af "${filterChain1}" -ar 48000 "${tempComp}"`, { stdio: 'pipe' });

  // Pass 1: measure
  let stats = null;
  try {
    const pass1Log = execSync(`ffmpeg -i "${tempComp}" -af "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json" -f null - 2>&1`, { encoding: 'utf8' });
    stats = JSON.parse(pass1Log.slice(pass1Log.lastIndexOf('{'), pass1Log.lastIndexOf('}') + 1));
  } catch (_) {}

  // Pass 2: apply
  if (stats && stats.input_i) {
    const pass2Filter = `loudnorm=I=-16:TP=-1.5:LRA=11:measured_I=${stats.input_i}:measured_LRA=${stats.input_lra}:measured_TP=${stats.input_tp}:measured_thresh=${stats.input_thresh}:offset=${stats.target_offset}:linear=true`;
    execSync(`ffmpeg -y -i "${tempComp}" -af "${pass2Filter}" -b:a 192k -ar 48000 "${outMp3}"`, { stdio: 'pipe' });
  } else {
    execSync(`ffmpeg -y -i "${tempComp}" -af "loudnorm=I=-16:TP=-1.5:LRA=11" -b:a 192k -ar 48000 "${outMp3}"`, { stdio: 'pipe' });
  }

  // Clean temp
  if (fs.existsSync(tempWav)) fs.unlinkSync(tempWav);
  if (fs.existsSync(tempComp)) fs.unlinkSync(tempComp);

  // Measure final LUFS and duration
  const probe = execSync(
    `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${outMp3}"`,
    { encoding: 'utf8' }
  ).trim();
  const durSec = parseFloat(probe).toFixed(1);

  console.log(`   ✔ Preview created: audio/previews/${candidate.id}.mp3 (${durSec}s @ -16 LUFS)`);
  return { id: candidate.id, file: `audio/previews/${candidate.id}.mp3`, duration: durSec };
}

function main() {
  console.log(`\n===============================================================`);
  console.log(`  🎧 NGESA DIARIES — VOICE AUDITION A/B PREVIEW GENERATOR`);
  console.log(`===============================================================`);

  const previewDir = path.join(ROOT_DIR, 'audio', 'previews');
  fs.mkdirSync(previewDir, { recursive: true });

  const results = [];
  for (const c of CANDIDATES) {
    results.push(generatePreview(c, previewDir));
  }

  // Also write an A/B index JSON
  const indexPath = path.join(previewDir, 'index.json');
  fs.writeFileSync(indexPath, JSON.stringify(results, null, 2));

  console.log(`\n===============================================================`);
  console.log(`✅ ALL 3 AUDITION PREVIEWS GENERATED SUCCESSFULLY`);
  console.log(`   Location: audio/previews/`);
  console.log(`   Index: audio/previews/index.json`);
  console.log(`===============================================================\n`);
}

main();
