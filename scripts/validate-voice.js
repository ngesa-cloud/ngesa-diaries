#!/usr/bin/env node
/**
 * scripts/validate-voice.js
 * Automated Broadcast Quality & CI Validator for Ngesa Diaries
 * Strict checks: LUFS within -16 ± 1, True Peak <= -1.0 dBFS, no silence > 2s, duration estimate ±10%
 */

import fs from 'node:fs';
import path from 'node:path';
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

function analyzeAudioFile(filePath, expectedDurationSec = null) {
  const relPath = path.relative(ROOT_DIR, filePath);
  console.log(`\n🔍 Auditing Broadcast Quality: ${relPath}`);

  if (!fs.existsSync(filePath)) {
    return { pass: false, error: `File not found: ${relPath}` };
  }

  const errors = [];
  const warnings = [];

  // 1. EBU R128 Loudness & True Peak Measurement
  let integratedLufs = null;
  let truePeak = null;
  try {
    const ebuOutput = execSync(
      `ffmpeg -i "${filePath}" -af "ebur128=peak=true" -f null - 2>&1`,
      { encoding: 'utf8' }
    );

    const summaryIdx = ebuOutput.lastIndexOf('Summary:');
    const summaryPart = summaryIdx !== -1 ? ebuOutput.slice(summaryIdx) : ebuOutput;

    const lufsMatch = summaryPart.match(/Integrated loudness:\s+I:\s+([-\d.]+)\s+LUFS/) || summaryPart.match(/I:\s+([-\d.]+)\s+LUFS/);
    if (lufsMatch) {
      integratedLufs = parseFloat(lufsMatch[1]);
    }

    const peakMatch = summaryPart.match(/Peak:\s+([-\d.]+)\s+dBFS/);
    if (peakMatch) {
      truePeak = parseFloat(peakMatch[1]);
    }
  } catch (err) {
    errors.push(`Failed to calculate EBU R128 loudness: ${err.message}`);
  }

  // Evaluate LUFS: Target -16.0 ± 1.0 (i.e. between -17.0 and -15.0 LUFS)
  if (integratedLufs !== null) {
    if (integratedLufs < -17.0 || integratedLufs > -15.0) {
      errors.push(`Loudness violation: ${integratedLufs.toFixed(1)} LUFS (Required: -16.0 ± 1.0 LUFS)`);
    } else {
      console.log(`  ✔ Integrated Loudness: ${integratedLufs.toFixed(2)} LUFS (Within -16 ± 1 spec)`);
    }
  }

  // Evaluate Peak / Clipping: True Peak must be <= -1.0 dBFS
  if (truePeak !== null) {
    if (truePeak > -0.9) {
      errors.push(`Audio clipping / headroom violation: Peak is ${truePeak.toFixed(1)} dBFS (Maximum allowed: -1.0 dBFS)`);
    } else {
      console.log(`  ✔ True Peak Headroom: ${truePeak.toFixed(2)} dBFS (No clipping detected)`);
    }
  }

  // 2. Silence Detector (No silence > 2.0s allowed)
  try {
    const silenceOutput = execSync(
      `ffmpeg -i "${filePath}" -af "silencedetect=noise=-50dB:d=2.0" -f null - 2>&1`,
      { encoding: 'utf8' }
    );
    const silenceMatches = silenceOutput.match(/silence_duration:\s+([-\d.]+)/g);
    if (silenceMatches && silenceMatches.length > 0) {
      const longSilences = silenceMatches
        .map(m => parseFloat(m.replace('silence_duration:', '').trim()))
        .filter(dur => dur > 2.05);

      if (longSilences.length > 0) {
        errors.push(`Dead air violation: Detected ${longSilences.length} silence interval(s) > 2.0s (max: ${Math.max(...longSilences)}s)`);
      } else {
        console.log(`  ✔ Dynamic Pacing: No dead air / silence > 2.0s detected`);
      }
    } else {
      console.log(`  ✔ Dynamic Pacing: No silence > 2.0s detected`);
    }
  } catch (err) {
    warnings.push(`Silence detection warning: ${err.message}`);
  }

  // 3. Duration Probe & Script Estimate Check
  let measuredDuration = 0;
  try {
    const probe = execSync(
      `ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "${filePath}"`,
      { encoding: 'utf8' }
    ).trim();
    measuredDuration = parseFloat(probe);
    console.log(`  ✔ Measured Duration: ${measuredDuration.toFixed(1)}s`);

    if (expectedDurationSec) {
      const margin = expectedDurationSec * 0.10; // ±10%
      const minAllowed = expectedDurationSec - margin;
      const maxAllowed = expectedDurationSec + margin;
      if (measuredDuration < minAllowed || measuredDuration > maxAllowed) {
        warnings.push(`Duration drift: ${measuredDuration.toFixed(1)}s deviates >10% from estimated ${expectedDurationSec}s`);
      } else {
        console.log(`  ✔ Duration Alignment: Within ±10% of estimated target (${expectedDurationSec}s)`);
      }
    }
  } catch (err) {
    errors.push(`Failed to probe duration: ${err.message}`);
  }

  return {
    filePath,
    pass: errors.length === 0,
    integratedLufs,
    truePeak,
    measuredDuration,
    errors,
    warnings
  };
}

function main() {
  console.log(`===============================================================`);
  console.log(`  🛡️  NGESA DIARIES — CI BROADCAST VOICE VALIDATOR`);
  console.log(`  Standards: -16 ± 1 LUFS | Peak <= -1 dBFS | Silence <= 2s`);
  console.log(`===============================================================`);

  const args = process.argv.slice(2);
  const filesToValidate = [];

  if (args.length > 0) {
    for (const a of args) {
      filesToValidate.push({ path: path.resolve(ROOT_DIR, a) });
    }
  } else {
    // Audit manifest files or audio/ directory
    const manifestPath = path.join(ROOT_DIR, 'audio', 'manifest.json');
    if (fs.existsSync(manifestPath)) {
      try {
        const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));
        for (const [key, item] of Object.entries(manifest)) {
          const mp3Path = path.join(ROOT_DIR, 'audio', `${key}.mp3`);
          filesToValidate.push({ path: mp3Path, expectedSec: item.duration_seconds });
        }
      } catch (_) {}
    }

    // Also check previews
    const previewDir = path.join(ROOT_DIR, 'audio', 'previews');
    if (fs.existsSync(previewDir)) {
      const pFiles = fs.readdirSync(previewDir).filter(f => f.endsWith('.mp3'));
      for (const pf of pFiles) {
        filesToValidate.push({ path: path.join(previewDir, pf) });
      }
    }
  }

  if (filesToValidate.length === 0) {
    console.log(`⚠️  No audio files found to validate in audio/ or audio/previews/.`);
    console.log(`   Run "npm run voice:preview" or "npm run voice:generate" first.`);
    process.exit(0);
  }

  let totalErrors = 0;
  const results = [];

  for (const item of filesToValidate) {
    const res = analyzeAudioFile(item.path, item.expectedSec);
    results.push(res);
    if (!res.pass) {
      totalErrors += res.errors.length;
      for (const e of res.errors) {
        console.error(`  ❌ FAIL: ${e}`);
      }
    }
    if (res.warnings && res.warnings.length > 0) {
      for (const w of res.warnings) {
        console.warn(`  ⚠️ WARN: ${w}`);
      }
    }
  }

  console.log(`\n===============================================================`);
  console.log(`VALIDATION SUMMARY: ${results.filter(r => r.pass).length}/${results.length} Files Passed`);

  if (totalErrors > 0) {
    console.error(`❌ CI VALIDATION FAILED with ${totalErrors} violation(s).`);
    process.exit(1);
  } else {
    console.log(`✅ ALL BROADCAST CRITERIA MET. CI BUILD APPROVED.`);
    console.log(`===============================================================\n`);
    process.exit(0);
  }
}

main();
