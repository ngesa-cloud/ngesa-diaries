# Script to build the upgraded index.html for Ngesa Diaries
# Featuring Manga / Graphic Novel Noir aesthetic (from dribbble_ref.png)
# and Kendo UI AIPrompt component (from telerik.com/kendo-jquery-ui/documentation/controls/aiprompt/overview)

page_content = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ngesa Diaries — Declassified Kenyan Horror &amp; Occult Mysteries</title>
  <meta name="description" content="An open-source investigative audio documentary platform and AI dossier exploring declassified Kenyan horror folklore, urban legends, and forensic mysteries.">

  <!-- Favicon: Dominic's GitHub Avatar -->
  <link rel="icon" type="image/jpeg" href="avatar.jpg">

  <!-- Google Fonts: Space Grotesk, Newsreader, Fira Code, Anton, Noto Sans JP -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Fira+Code:wght@400;500;600;700&family=IBM+Plex+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Newsreader:ital,opsz,wght@0,6..72,300..700;1,6..72,400..600&family=Noto+Sans+JP:wght@700;900&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      /* Graphic Novel / Manga Noir Palette (Matching Dribbble Reference) */
      --bg-paper: #eceff2;
      --bg-dots: rgba(0, 0, 0, 0.12);
      --card-white: #ffffff;
      --card-paper: #f8f9fb;
      --ink-black: #0c0e12;
      --ink-dark: #1b1f26;
      --ink-faint: #5a6270;
      --ink-subtle: #8a93a2;
      --manga-border: #0c0e12;
      --crimson: #ff2a4b;
      --crimson-dark: #d91434;
      --ochre: #d9a441;
      --pill-bg: #e2e5eb;
      --pill-hover: #d5d9e2;
      --pill-active: #0c0e12;
      --hazard-strip: repeating-linear-gradient(-45deg, #0c0e12, #0c0e12 6px, transparent 6px, transparent 12px);
      
      /* Typography */
      --font-display: 'Anton', 'Space Grotesk', system-ui, sans-serif;
      --font-grotesk: 'Space Grotesk', system-ui, sans-serif;
      --font-body: 'IBM Plex Sans', system-ui, sans-serif;
      --font-serif: 'Newsreader', Georgia, serif;
      --font-mono: 'Fira Code', monospace;
      
      --shadow-hard: 6px 6px 0px #0c0e12;
      --shadow-hard-sm: 3px 3px 0px #0c0e12;
      --shadow-hard-lg: 10px 10px 0px #0c0e12;
    }

    /* Dark Noir Mode (Toggled via Theme button) */
    body.theme-midnight {
      --bg-paper: #090a0e;
      --bg-dots: rgba(255, 255, 255, 0.08);
      --card-white: #12141a;
      --card-paper: #161922;
      --ink-black: #f5f6f9;
      --ink-dark: #e1e4eb;
      --ink-faint: #a0a6b5;
      --ink-subtle: #6c7384;
      --manga-border: #ffffff;
      --pill-bg: #222634;
      --pill-hover: #2e3344;
      --pill-active: #ffffff;
      --shadow-hard: 6px 6px 0px rgba(255, 255, 255, 0.25);
      --shadow-hard-sm: 3px 3px 0px rgba(255, 255, 255, 0.25);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-paper);
      background-image: 
        radial-gradient(var(--bg-dots) 1px, transparent 1px),
        linear-gradient(to right, rgba(0,0,0,0.015) 1px, transparent 1px);
      background-size: 18px 18px, 120px 120px;
      color: var(--ink-black);
      font-family: var(--font-body);
      min-height: 100vh;
      overflow-x: hidden;
      overflow-y: auto;
      transition: background-color 0.3s ease, color 0.3s ease;
      cursor: url('cursor_finger_32.png') 6 4, auto;
    }

    a, button, input, textarea, select, .k-chip, .k-command-card, .case-tile, .brand-cluster, .comic-panel-action, .btn-pill-cta {
      cursor: url('cursor_finger_32.png') 6 4, pointer !important;
    }

    /* Among Us Batman Finger Custom Cursor & Dynamic Follower */
    #cursor-finger-follower {
      position: fixed;
      top: 0; left: 0;
      width: 44px; height: 44px;
      pointer-events: none;
      z-index: 10000;
      transform: translate(-6px, -4px);
      transition: transform 0.12s cubic-bezier(0.16, 1, 0.3, 1), filter 0.2s;
    }
    #cursor-finger-follower img {
      width: 100%; height: 100%;
      object-fit: contain;
      filter: drop-shadow(2px 3px 4px rgba(0, 0, 0, 0.45));
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    body.cursor-hover #cursor-finger-follower img {
      transform: scale(1.18) rotate(-6deg);
      filter: drop-shadow(0 0 10px rgba(255, 42, 75, 0.75));
    }
    #cursor-ring {
      position: fixed;
      top: 0; left: 0;
      width: 30px; height: 30px;
      border: 1.5px dashed var(--crimson);
      border-radius: 50%;
      pointer-events: none;
      z-index: 9999;
      transform: translate(-50%, -50%);
      transition: width 0.28s cubic-bezier(0.16, 1, 0.3, 1), height 0.28s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.25s, opacity 0.25s;
      opacity: 0.65;
    }
    body.cursor-hover #cursor-ring {
      width: 50px; height: 50px;
      border-color: var(--crimson);
      border-style: solid;
      background: rgba(255, 42, 75, 0.08);
      opacity: 1;
    }

    /* TOP NAVIGATION BAR */
    .top-nav {
      position: sticky;
      top: 0;
      z-index: 100;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 32px;
      background: rgba(236, 239, 242, 0.88);
      backdrop-filter: blur(12px);
      border-bottom: 2px solid var(--ink-black);
      transition: background 0.3s;
    }
    body.theme-midnight .top-nav {
      background: rgba(9, 10, 14, 0.88);
    }

    .brand-cluster {
      display: flex;
      align-items: center;
      gap: 12px;
      cursor: pointer;
    }
    .brand-pill {
      display: flex;
      align-items: center;
      gap: 10px;
      background: var(--ink-black);
      color: #fff;
      padding: 6px 14px 6px 8px;
      border-radius: 999px;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 13px;
      letter-spacing: 0.5px;
      box-shadow: var(--shadow-hard-sm);
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    body.theme-midnight .brand-pill {
      background: #fff;
      color: #000;
    }
    .brand-pill:hover {
      transform: translate(-1px, -1px);
    }
    .brand-avatar {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      object-fit: cover;
      border: 1.5px solid #fff;
    }
    body.theme-midnight .brand-avatar {
      border-color: #000;
    }
    .brand-tag {
      font-size: 11px;
      font-family: var(--font-mono);
      color: var(--ink-faint);
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .nav-links {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .nav-pill-btn {
      background: none;
      border: none;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 12.5px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      color: var(--ink-dark);
      padding: 7px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .nav-pill-btn:hover {
      background: var(--pill-bg);
      transform: translateY(-1px);
    }
    .nav-pill-btn.active {
      background: var(--ink-black);
      color: #ffffff;
    }
    body.theme-midnight .nav-pill-btn.active {
      background: #ffffff;
      color: #000000;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .btn-pill-cta {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 9px 20px;
      border-radius: 999px;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 12.5px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      cursor: pointer;
      border: 2px solid var(--ink-black);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: var(--shadow-hard-sm);
    }
    .btn-pill-cta.light {
      background: var(--card-white);
      color: var(--ink-black);
    }
    .btn-pill-cta.dark {
      background: var(--ink-black);
      color: #fff;
    }
    body.theme-midnight .btn-pill-cta.dark {
      background: #fff;
      color: #000;
    }
    .btn-pill-cta:hover {
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px var(--ink-black);
    }
    body.theme-midnight .btn-pill-cta:hover {
      box-shadow: 5px 5px 0px rgba(255,255,255,0.4);
    }
    .btn-pill-cta:active {
      transform: translate(1px, 1px);
      box-shadow: 2px 2px 0px var(--ink-black);
    }

    /* MAIN CONTAINER */
    .app-main {
      max-width: 1540px;
      margin: 0 auto;
      padding: 24px 32px 120px 32px;
      position: relative;
    }

    /* INK SPLATTERS (SVG Vector Drops) */
    .ink-splatter {
      position: absolute;
      pointer-events: none;
      z-index: 1;
      opacity: 0.85;
    }
    body.theme-midnight .ink-splatter {
      filter: invert(1);
      opacity: 0.35;
    }

    /* HERO SECTION (Manga Graphic Novel Layout) */
    .hero-grid {
      display: grid;
      grid-template-columns: 1.05fr 1.35fr;
      gap: 36px;
      align-items: start;
      margin-top: 12px;
      margin-bottom: 36px;
      position: relative;
      z-index: 2;
    }
    @media (max-width: 1080px) {
      .hero-grid {
        grid-template-columns: 1fr;
      }
    }

    /* HERO LEFT: EDITORIAL COPY */
    .hero-editorial {
      display: flex;
      flex-direction: column;
      gap: 16px;
      padding-right: 12px;
    }
    .editorial-badge-row {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .badge-red-box {
      background: var(--crimson);
      color: #fff;
      font-family: var(--font-grotesk);
      font-weight: 800;
      font-size: 11px;
      padding: 4px 10px;
      letter-spacing: 1px;
      text-transform: uppercase;
      border: 1.5px solid var(--ink-black);
      box-shadow: 2px 2px 0px var(--ink-black);
    }
    .badge-sub-label {
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 600;
      color: var(--ink-dark);
      letter-spacing: 1px;
      text-transform: uppercase;
    }
    .social-icons-strip {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-left: auto;
    }
    .social-icon-btn {
      width: 28px;
      height: 28px;
      border-radius: 50%;
      background: var(--ink-black);
      color: #fff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 12px;
      text-decoration: none;
      transition: transform 0.2s;
    }
    body.theme-midnight .social-icon-btn {
      background: #fff;
      color: #000;
    }
    .social-icon-btn:hover {
      transform: scale(1.12);
    }

    /* HUGE MANGA DISPLAY TYPOGRAPHY */
    .manga-title-wrap {
      margin-top: 4px;
    }
    .manga-hero-h1 {
      font-family: var(--font-display);
      font-size: clamp(48px, 6.2vw, 84px);
      line-height: 0.92;
      text-transform: uppercase;
      letter-spacing: -0.5px;
      color: var(--ink-black);
      margin-bottom: 8px;
    }
    .manga-hero-h1 span.red-word {
      color: var(--crimson);
      display: inline-block;
      position: relative;
    }
    .manga-kanji-sub {
      font-family: 'Noto Sans JP', var(--font-grotesk), sans-serif;
      font-size: clamp(18px, 2.2vw, 28px);
      font-weight: 700;
      letter-spacing: 2px;
      color: var(--ink-dark);
      text-transform: uppercase;
      opacity: 0.92;
    }
    .bracket-sub {
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 600;
      letter-spacing: 1.5px;
      color: var(--ink-faint);
      margin-top: 6px;
      text-transform: uppercase;
    }

    /* CASE SYNOPSIS CALLOUT */
    .active-case-card {
      background: var(--card-white);
      border: 2px solid var(--ink-black);
      border-radius: 6px;
      padding: 20px 24px;
      box-shadow: var(--shadow-hard);
      margin-top: 10px;
      position: relative;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s;
    }
    .active-case-card:hover {
      transform: translate(-2px, -2px);
      box-shadow: 8px 8px 0px var(--ink-black);
    }
    body.theme-midnight .active-case-card {
      box-shadow: var(--shadow-hard);
    }
    .case-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1.5px solid rgba(0,0,0,0.08);
      padding-bottom: 10px;
      margin-bottom: 12px;
    }
    body.theme-midnight .case-card-header {
      border-color: rgba(255,255,255,0.1);
    }
    .case-meta-tag {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--crimson);
      text-transform: uppercase;
    }
    .case-broadcast-pill {
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 3px 8px;
      background: #000;
      color: #00ff66;
      border-radius: 4px;
    }
    .case-card-title {
      font-family: var(--font-serif);
      font-size: 22px;
      font-weight: 700;
      color: var(--ink-black);
      margin-bottom: 6px;
      line-height: 1.25;
    }
    .case-card-tagline {
      font-family: var(--font-serif);
      font-style: italic;
      font-size: 14.5px;
      color: var(--ochre);
      margin-bottom: 12px;
      line-height: 1.4;
    }
    .case-card-body {
      font-size: 13.5px;
      line-height: 1.6;
      color: var(--ink-dark);
      margin-bottom: 16px;
    }

    /* ACTION BUTTONS ROW */
    .hero-cta-row {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      margin-top: 6px;
    }
    .btn-hero-listen {
      background: var(--pill-bg);
      color: var(--ink-black);
      border: 2px solid var(--ink-black);
      border-radius: 999px;
      padding: 13px 32px;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 13.5px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: var(--shadow-hard-sm);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-hero-listen:hover {
      background: #ffffff;
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px var(--ink-black);
    }
    .btn-hero-ai {
      background: var(--ink-black);
      color: #ffffff;
      border: 2px solid var(--ink-black);
      border-radius: 999px;
      padding: 13px 32px;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 13.5px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 10px;
      box-shadow: var(--shadow-hard-sm);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    body.theme-midnight .btn-hero-ai {
      background: #ffffff;
      color: #000000;
    }
    .btn-hero-ai:hover {
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px var(--ink-black);
    }
    body.theme-midnight .btn-hero-ai:hover {
      box-shadow: 5px 5px 0px rgba(255,255,255,0.4);
    }

    /* VOICE CLONE & NARRATOR IDENTITY STRIP */
    .voice-clone-strip {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 8px 12px;
      margin: 14px 0 16px 0;
      padding: 10px 14px;
      background: rgba(255, 42, 75, 0.05);
      border: 1.5px dashed rgba(255, 42, 75, 0.4);
      border-radius: 6px;
      font-family: var(--font-grotesk);
      font-size: 11.5px;
    }
    body.theme-midnight .voice-clone-strip {
      background: rgba(255, 42, 75, 0.12);
      border-color: rgba(255, 42, 75, 0.5);
    }
    .voice-clone-badge {
      display: flex;
      align-items: center;
      gap: 6px;
      color: var(--crimson);
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .pulse-dot {
      width: 8px; height: 8px;
      border-radius: 50%;
      background: var(--crimson);
      box-shadow: 0 0 8px var(--crimson);
      animation: pulseGlow 1.5s infinite;
      display: inline-block;
    }
    @keyframes pulseGlow {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.35; transform: scale(1.35); }
    }
    .btn-voice-ref {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--ink-black);
      color: #fff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      border-radius: 999px;
      padding: 5px 13px;
      font-size: 11px;
      font-weight: 700;
      cursor: url('cursor_finger_32.png') 6 4, pointer !important;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .btn-voice-ref:hover {
      background: var(--crimson);
      border-color: var(--crimson);
      transform: translateY(-1px);
    }
    .voice-style-tag {
      color: var(--lead-gray);
      font-size: 11px;
      font-weight: 600;
      font-style: italic;
    }
    body.theme-midnight .voice-style-tag {
      color: #9aa0a6;
    }

    /* HERO RIGHT: THE MANGA COMIC PANELS (From Dribbble Reference) */
    .manga-panels-stage {
      position: relative;
      display: grid;
      grid-template-columns: 1.15fr 0.95fr;
      grid-template-rows: auto auto;
      gap: 16px;
      align-items: center;
      perspective: 1200px;
    }

    /* Panel 1: Horizontal Eyes Strip */
    .comic-panel-eyes {
      grid-column: 1 / 2;
      grid-row: 1 / 2;
      border: 3px solid var(--ink-black);
      box-shadow: var(--shadow-hard);
      background: #000;
      overflow: hidden;
      border-radius: 2px;
      height: 140px;
      position: relative;
      transform: rotate(-1deg);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .comic-panel-eyes:hover {
      transform: rotate(0deg) scale(1.02);
    }
    .comic-panel-eyes img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .comic-tag-overlay {
      position: absolute;
      bottom: 6px;
      left: 8px;
      background: rgba(0,0,0,0.85);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      padding: 2px 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      border-left: 2px solid var(--crimson);
    }

    /* Panel 2: Center Tilted Dynamic Action Frame */
    .comic-panel-action {
      grid-column: 1 / 2;
      grid-row: 2 / 3;
      border: 3.5px solid var(--ink-black);
      box-shadow: var(--shadow-hard-lg);
      background: #000;
      overflow: hidden;
      border-radius: 3px;
      height: 380px;
      position: relative;
      transform: rotate(1.2deg);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .comic-panel-action:hover {
      transform: rotate(0deg) scale(1.02);
    }
    .comic-panel-action img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .action-speech-bubble {
      position: absolute;
      top: 16px;
      right: 16px;
      background: #fff;
      color: #000;
      border: 2px solid #000;
      border-radius: 16px;
      padding: 6px 12px;
      font-family: var(--font-grotesk);
      font-size: 11px;
      font-weight: 800;
      box-shadow: 3px 3px 0px #000;
      pointer-events: none;
    }

    /* Panel 3: Right Vertical Inspector Portrait */
    .comic-panel-investigator {
      grid-column: 2 / 3;
      grid-row: 1 / 3;
      border: 3.5px solid var(--ink-black);
      box-shadow: var(--shadow-hard-lg);
      background: #000;
      overflow: hidden;
      border-radius: 3px;
      height: 536px;
      position: relative;
      transform: rotate(-1.5deg);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .comic-panel-investigator:hover {
      transform: rotate(0deg) scale(1.02);
    }
    .comic-panel-investigator img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .investigator-badge {
      position: absolute;
      bottom: 12px;
      left: 12px;
      right: 12px;
      background: rgba(12, 14, 18, 0.92);
      color: #fff;
      border: 1.5px solid #fff;
      padding: 8px 12px;
      border-radius: 3px;
      font-family: var(--font-mono);
      font-size: 10.5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .investigator-badge span.name {
      color: #fff;
      font-weight: 700;
    }
    .investigator-badge span.role {
      color: var(--ochre);
    }

    /* DECORATIVE DIAGONAL HAZARD BAR & DATE STAMP */
    .manga-sub-strip {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-top: 12px;
      padding-top: 10px;
      border-top: 2px dashed rgba(0,0,0,0.15);
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      color: var(--ink-dark);
      letter-spacing: 1px;
    }
    body.theme-midnight .manga-sub-strip {
      border-color: rgba(255,255,255,0.15);
    }
    .hazard-strip-box {
      width: 120px;
      height: 12px;
      background: var(--hazard-strip);
      border: 1px solid var(--ink-black);
    }

    /* =========================================================
       TELERIK KENDO UI AIPROMPT COMPONENT
       (Specification-faithful Implementation)
       ========================================================= */
    .k-aiprompt-wrapper {
      background: var(--card-white);
      border: 3px solid var(--ink-black);
      border-radius: 6px;
      box-shadow: var(--shadow-hard-lg);
      margin: 32px 0 40px 0;
      overflow: hidden;
      position: relative;
      z-index: 10;
      transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Kendo Header */
    .k-aiprompt-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 20px;
      background: var(--ink-black);
      color: #fff;
      border-bottom: 2px solid var(--ink-black);
    }
    body.theme-midnight .k-aiprompt-header {
      background: #191c26;
      border-color: rgba(255,255,255,0.15);
    }
    .k-header-title {
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 14px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
    }
    .k-ai-badge {
      background: var(--crimson);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 3px;
    }
    .k-header-tools {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .k-tool-btn {
      background: rgba(255, 255, 255, 0.12);
      border: none;
      color: #fff;
      border-radius: 4px;
      padding: 4px 8px;
      font-size: 12px;
      font-family: var(--font-mono);
      cursor: pointer;
      transition: background 0.2s;
    }
    .k-tool-btn:hover {
      background: rgba(255, 255, 255, 0.25);
    }

    /* Kendo Views Navigation Toolbar (Prompt View, Outputs View, Commands View) */
    .k-aiprompt-toolbar {
      display: flex;
      background: var(--card-paper);
      border-bottom: 2px solid var(--ink-black);
      padding: 0 16px;
      gap: 6px;
      overflow-x: auto;
    }
    .k-view-tab {
      background: none;
      border: none;
      border-bottom: 3px solid transparent;
      padding: 12px 18px;
      font-family: var(--font-grotesk);
      font-size: 13px;
      font-weight: 700;
      color: var(--ink-faint);
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .k-view-tab:hover {
      color: var(--ink-black);
    }
    .k-view-tab.active {
      color: var(--ink-black);
      border-bottom-color: var(--crimson);
      background: rgba(255, 42, 75, 0.04);
    }
    .k-count-badge {
      background: var(--ink-black);
      color: #fff;
      font-size: 10.5px;
      padding: 1px 6px;
      border-radius: 999px;
    }
    body.theme-midnight .k-count-badge {
      background: #fff;
      color: #000;
    }

    /* Kendo Content Views */
    .k-view-content {
      display: none;
      padding: 24px;
    }
    .k-view-content.active {
      display: block;
    }

    /* 1. PROMPT VIEW */
    .k-prompt-input-box {
      position: relative;
      border: 2px solid var(--ink-black);
      border-radius: 6px;
      background: var(--card-white);
      box-shadow: var(--shadow-hard-sm);
      overflow: hidden;
      margin-bottom: 18px;
    }
    .k-prompt-textarea {
      width: 100%;
      min-height: 84px;
      padding: 14px 18px;
      border: none;
      outline: none;
      resize: vertical;
      font-family: var(--font-body);
      font-size: 14.5px;
      color: var(--ink-black);
      background: transparent;
      line-height: 1.5;
    }
    .k-prompt-actions-bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 8px 14px;
      background: var(--card-paper);
      border-top: 1px solid rgba(0,0,0,0.08);
    }
    body.theme-midnight .k-prompt-actions-bar {
      border-color: rgba(255,255,255,0.08);
    }
    .k-prompt-meta {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--ink-faint);
    }
    .k-btn-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .k-btn-clear {
      background: none;
      border: 1.5px solid var(--ink-faint);
      color: var(--ink-faint);
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 12px;
      padding: 6px 14px;
      border-radius: 999px;
      cursor: pointer;
      transition: all 0.2s;
    }
    .k-btn-clear:hover {
      border-color: var(--ink-black);
      color: var(--ink-black);
    }
    .k-btn-generate {
      background: var(--ink-black);
      color: #fff;
      border: 2px solid var(--ink-black);
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 12.5px;
      padding: 7px 18px;
      border-radius: 999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      box-shadow: 2px 2px 0px var(--crimson);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    body.theme-midnight .k-btn-generate {
      background: #fff;
      color: #000;
    }
    .k-btn-generate:hover {
      transform: translate(-1px, -1px);
      box-shadow: 3px 3px 0px var(--crimson);
    }

    /* Kendo Prompt Suggestions / Chips */
    .k-suggestions-container {
      margin-top: 14px;
    }
    .k-suggestions-label {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--ink-faint);
      text-transform: uppercase;
      letter-spacing: 1px;
      margin-bottom: 10px;
    }
    .k-chips-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .k-chip {
      background: var(--pill-bg);
      border: 1.5px solid var(--ink-black);
      color: var(--ink-black);
      font-family: var(--font-grotesk);
      font-weight: 600;
      font-size: 12px;
      padding: 6px 14px;
      border-radius: 999px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: all 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 1px 1px 0px var(--ink-black);
    }
    .k-chip:hover {
      background: var(--card-white);
      transform: translate(-1px, -1px);
      box-shadow: 3px 3px 0px var(--ink-black);
      border-color: var(--crimson);
    }

    /* 2. OUTPUTS VIEW */
    .k-outputs-list {
      display: flex;
      flex-direction: column;
      gap: 16px;
      max-height: 520px;
      overflow-y: auto;
      padding-right: 6px;
    }
    .k-output-card {
      background: var(--card-white);
      border: 2px solid var(--ink-black);
      border-radius: 6px;
      padding: 18px 20px;
      box-shadow: var(--shadow-hard-sm);
      animation: kSlideIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    @keyframes kSlideIn {
      from { opacity: 0; transform: translateY(12px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .k-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(0,0,0,0.08);
      padding-bottom: 8px;
      margin-bottom: 12px;
    }
    body.theme-midnight .k-card-header {
      border-color: rgba(255,255,255,0.1);
    }
    .k-agent-tag {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--crimson);
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .k-timestamp {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--ink-subtle);
    }
    .k-prompt-pill {
      background: var(--pill-bg);
      border-left: 3px solid var(--crimson);
      padding: 6px 12px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--ink-dark);
      margin-bottom: 12px;
      border-radius: 0 4px 4px 0;
    }
    .k-output-body {
      font-size: 13.5px;
      line-height: 1.65;
      color: var(--ink-black);
      margin-bottom: 14px;
    }
    .k-output-body blockquote {
      border-left: 3px solid var(--ochre);
      padding-left: 12px;
      font-family: var(--font-serif);
      font-style: italic;
      color: var(--ink-dark);
      margin: 10px 0;
    }
    .k-output-actions {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(0,0,0,0.08);
      padding-top: 10px;
    }
    body.theme-midnight .k-output-actions {
      border-color: rgba(255,255,255,0.08);
    }
    .k-action-btn-group {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .k-action-btn {
      background: var(--pill-bg);
      border: 1px solid var(--ink-black);
      border-radius: 4px;
      padding: 4px 10px;
      font-family: var(--font-grotesk);
      font-size: 11.5px;
      font-weight: 600;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      transition: all 0.15s;
    }
    .k-action-btn:hover {
      background: var(--card-white);
      border-color: var(--crimson);
    }

    /* 3. COMMANDS VIEW (Quick Actions) */
    .k-commands-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 14px;
    }
    .k-command-card {
      background: var(--card-paper);
      border: 2px solid var(--ink-black);
      border-radius: 6px;
      padding: 16px;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 2px 2px 0px var(--ink-black);
    }
    .k-command-card:hover {
      background: var(--card-white);
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px var(--ink-black);
      border-color: var(--crimson);
    }
    .k-command-title {
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 13.5px;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .k-command-desc {
      font-size: 12px;
      color: var(--ink-faint);
      line-height: 1.4;
    }

    /* CASE DOSSIER EXPLORER TABS (Case File, Transcript, All Cases) */
    .dossier-explorer {
      margin-top: 24px;
      background: var(--card-white);
      border: 3px solid var(--ink-black);
      border-radius: 6px;
      box-shadow: var(--shadow-hard-lg);
      padding: 24px;
    }
    .dossier-nav-bar {
      position: relative;
      display: flex;
      gap: 8px;
      border-bottom: 2px solid var(--ink-black);
      padding-bottom: 12px;
      margin-bottom: 20px;
    }
    .tab-pill-indicator {
      position: absolute;
      bottom: -2px;
      left: 0;
      height: 3px;
      background: var(--crimson);
      box-shadow: 0 0 8px var(--crimson);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1), width 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
    }
    .dossier-tab-btn {
      background: none;
      border: none;
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 13.5px;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 8px 16px;
      border-radius: 999px;
      cursor: pointer;
      color: var(--ink-faint);
      transition: color 0.2s, background 0.2s;
    }
    .dossier-tab-btn:hover {
      color: var(--ink-black);
      background: var(--pill-bg);
    }
    .dossier-tab-btn.active {
      color: var(--ink-black);
    }

    .dossier-pane { display: none; }
    .dossier-pane.active { display: block; }

    /* ALL 8 CASES GRID */
    .episodes-case-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 16px;
    }
    .case-tile {
      background: var(--card-paper);
      border: 2px solid var(--ink-black);
      border-radius: 4px;
      padding: 16px;
      cursor: pointer;
      box-shadow: var(--shadow-hard-sm);
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .case-tile:hover {
      background: var(--card-white);
      transform: translate(-2px, -2px);
      box-shadow: 5px 5px 0px var(--ink-black);
      border-color: var(--crimson);
    }
    .case-tile.selected {
      border-color: var(--crimson);
      background: rgba(255, 42, 75, 0.05);
    }
    .tile-case-num {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--crimson);
      text-transform: uppercase;
      margin-bottom: 4px;
    }
    .tile-case-title {
      font-family: var(--font-serif);
      font-size: 17px;
      font-weight: 700;
      margin-bottom: 4px;
      line-height: 1.3;
    }
    .tile-case-sub {
      font-size: 12px;
      color: var(--ink-faint);
    }

    /* TRANSCRIPT CONTAINER */
    .transcript-box {
      max-height: 380px;
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      padding-right: 8px;
    }
    .t-row {
      display: flex;
      gap: 16px;
      font-size: 13.5px;
      line-height: 1.55;
    }
    .t-time {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--crimson);
      flex-shrink: 0;
      width: 50px;
    }
    .t-speaker {
      font-weight: 700;
      margin-right: 6px;
    }

    /* FIXED DOCKED AUDIO PLAYER */
    .docked-player {
      position: fixed;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%);
      width: min(94vw, 1080px);
      background: var(--card-white);
      border: 3px solid var(--ink-black);
      border-radius: 999px;
      box-shadow: var(--shadow-hard-lg);
      padding: 10px 24px;
      display: flex;
      align-items: center;
      gap: 18px;
      z-index: 1000;
      transition: background 0.3s, transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s;
    }
    .docked-player.minimized {
      transform: translateX(-50%) translateY(calc(100% - 14px));
      opacity: 0.65;
    }
    .docked-player.minimized:hover {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }
    .player-dock-toggle {
      background: none;
      border: 1px solid var(--ink-faint);
      border-radius: 50%;
      width: 22px;
      height: 22px;
      font-size: 11px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      color: var(--ink-faint);
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .player-dock-toggle:hover {
      border-color: var(--ink-black);
      color: var(--ink-black);
    }
    .btn-player-play {
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--ink-black);
      color: #fff;
      border: 2px solid var(--ink-black);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 16px;
      cursor: pointer;
      flex-shrink: 0;
      box-shadow: 2px 2px 0px var(--crimson);
      transition: transform 0.15s;
    }
    body.theme-midnight .btn-player-play {
      background: #fff;
      color: #000;
    }
    .btn-player-play:hover {
      transform: scale(1.08);
    }
    .player-track-info {
      display: flex;
      flex-direction: column;
      min-width: 180px;
    }
    .player-title {
      font-family: var(--font-grotesk);
      font-weight: 700;
      font-size: 13px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 200px;
    }
    .player-sub {
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--crimson);
    }
    .player-waveform-container {
      flex: 1;
      height: 38px;
      position: relative;
    }
    #wave-canvas {
      width: 100%;
      height: 100%;
      display: block;
    }
    .player-scrubber {
      position: absolute;
      inset: 0;
      cursor: pointer;
      display: flex;
      align-items: center;
    }
    .scrubber-fill {
      height: 2px;
      background: var(--crimson);
      box-shadow: 0 0 6px var(--crimson);
      width: 0%;
      pointer-events: none;
    }
    .player-time-box {
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 600;
      color: var(--ink-dark);
      white-space: nowrap;
    }
    .starpod-pill-indicator {
      font-family: var(--font-mono);
      font-size: 10px;
      background: #000;
      color: #00ff66;
      border: 1px solid #00ff66;
      border-radius: 4px;
      padding: 3px 6px;
      white-space: nowrap;
    }

    /* COMMUNITY WIRE MODAL */
    .drop-modal-overlay {
      position: fixed;
      inset: 0;
      background: rgba(12, 14, 18, 0.7);
      backdrop-filter: blur(8px);
      z-index: 10001;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }
    .drop-modal-overlay.open {
      display: flex;
    }
    .drop-modal-card {
      background: var(--card-white);
      border: 3px solid var(--ink-black);
      border-radius: 6px;
      box-shadow: var(--shadow-hard-lg);
      width: min(94vw, 540px);
      padding: 28px;
      animation: kSlideIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    /* Scrollbar */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(0, 0, 0, 0.2); border-radius: 3px; }
    body.theme-midnight ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.2); }
  </style>
</head>
<body>

  <!-- Tactile Analog Film Grain Overlay -->
  <svg id="film-grain">
    <filter id="grainFilter">
      <feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="3" stitchTiles="stitch" />
      <feColorMatrix type="matrix" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 1 0" />
    </filter>
    <rect width="100%" height="100%" filter="url(#grainFilter)" />
  </svg>

  <!-- Among Us Batman Finger Custom Cursor Follower -->
  <div id="cursor-finger-follower">
    <img src="cursor_finger.png" alt="Batman Finger Cursor">
  </div>
  <div id="cursor-ring"></div>

  <!-- TOP NAVIGATION BAR -->
  <header class="top-nav">
    <div class="brand-cluster" onclick="switchEpisode(0)">
      <div class="brand-pill">
        <img src="avatar.jpg" alt="Dominic Nyongesa" class="brand-avatar">
        <span>NGESA DIARIES</span>
      </div>
      <div class="brand-tag">/// DECLASSIFIED KENYAN OCCULT ARCHIVE</div>
    </div>

    <nav class="nav-links">
      <button class="nav-pill-btn active" onclick="scrollToSection('hero')">Case File</button>
      <button class="nav-pill-btn" onclick="scrollToSection('aiprompt')">⚡ AI Dossier Analyst</button>
      <button class="nav-pill-btn" onclick="scrollToSection('explorer')">All 8 Cases</button>
      <button class="nav-pill-btn" onclick="toggleDropModal()">Contribute Lore</button>
    </nav>

    <div class="nav-actions">
      <button class="btn-pill-cta light" onclick="toggleTheme()" title="Toggle Graphic Manga / Deep Noir Mode">
        <span id="theme-icon">🌓</span> <span id="theme-label">Midnight</span>
      </button>
      <button class="btn-pill-cta light" onclick="toggleDrone()" id="btn-drone-toggle">
        <span>🔊</span> <span id="drone-label">Drone: Standby</span>
      </button>
      <button class="btn-pill-cta dark" onclick="scrollToSection('aiprompt')">
        <span>✨</span> AI Prompt
      </button>
    </div>
  </header>

  <!-- MAIN EDITORIAL & GRAPHIC NOVEL STAGE -->
  <main class="app-main" id="main-content">

    <!-- INK SPLATTERS (SVG drops) -->
    <svg class="ink-splatter" style="top: 80px; left: -10px; width: 140px; height: 140px;" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="14" fill="#0c0e12" />
      <circle cx="28" cy="36" r="4" fill="#0c0e12" />
      <circle cx="74" cy="42" r="3.5" fill="#0c0e12" />
      <circle cx="62" cy="74" r="5" fill="#0c0e12" />
      <circle cx="38" cy="68" r="3" fill="#0c0e12" />
      <path d="M50,50 Q36,22 24,16 Q32,36 45,48 Z" fill="#0c0e12" />
      <path d="M50,50 Q75,65 88,78 Q70,72 52,55 Z" fill="#0c0e12" />
    </svg>
    <svg class="ink-splatter" style="top: 360px; right: 20px; width: 160px; height: 160px;" viewBox="0 0 100 100">
      <circle cx="50" cy="50" r="16" fill="#0c0e12" />
      <circle cx="24" cy="28" r="5" fill="#0c0e12" />
      <circle cx="82" cy="52" r="4.5" fill="#0c0e12" />
      <circle cx="42" cy="78" r="4" fill="#0c0e12" />
      <path d="M50,50 Q85,25 92,15 Q75,38 55,48 Z" fill="#0c0e12" />
    </svg>

    <!-- HERO SECTION -->
    <section class="hero-grid" id="hero">
      
      <!-- HERO LEFT: EDITORIAL CASE INTEL -->
      <div class="hero-editorial">
        <div class="editorial-badge-row">
          <div class="badge-red-box">KENYA TRUE HORROR</div>
          <div class="badge-sub-label">INVESTIGATIVE AUDIO ARCHIVE // HOSTED BY DOMINIC NYONGESA</div>
          <div class="social-icons-strip">
            <a href="https://github.com/ngesa-cloud" target="_blank" class="social-icon-btn" title="GitHub Profile">⌨</a>
            <a href="podcast.xml" target="_blank" class="social-icon-btn" title="RSS Feed">📻</a>
          </div>
        </div>

        <div class="manga-title-wrap">
          <h1 class="manga-hero-h1">
            DECLASSIFIED <br>
            <span class="red-word">DOSSIER</span> ARCHIVE
          </h1>
          <div class="manga-kanji-sub" id="hero-kanji-tag">夜の走者 // USIKU WA MANANE</div>
          <div class="bracket-sub">[ INVESTIGATING KENYA'S DARKEST FOLKLORE, URBAN LEGENDS &amp; TRUE CRIMES ]</div>
        </div>

        <!-- ACTIVE CASE CARD -->
        <div class="active-case-card" id="active-case-card">
          <div class="case-card-header">
            <div class="case-meta-tag" id="case-meta-tag">CASE 01 &bull; HOMA BAY &amp; KISII COUNTIES</div>
            <div class="case-broadcast-pill" id="case-broadcast-pill">-16.5 LUFS &bull; BROADCAST COMPLIANT</div>
          </div>
          <div class="case-card-title" id="case-card-title">The Midnight Knock (The Night Runners of Western Kenya)</div>
          <div class="case-card-tagline" id="case-card-tagline">Mud slaps on iron roofs, supernatural speed, and the hereditary night runners of Lake Victoria.</div>
          <div class="case-card-body" id="case-card-body">
            In the villages along the shores of Lake Victoria and the rolling hills of Gucha, midnight brings an unsettling silence—broken only by the sudden, violent slap of wet mud against corrugated iron roofs. This is the realm of the Night Runners (Abanyasi in Luhya, Omoirori in Gusii): individuals who claim an irresistible hereditary compulsion to strip bare in the dead of night, sprint through thorny thickets at impossible speeds, flick glowing embers into homesteads, and terrify their neighbors without ever breaking inside.
          </div>

          <!-- VOICE CLONE & NARRATOR IDENTITY STRIP -->
          <div class="voice-clone-strip">
            <div class="voice-clone-badge">
              <span class="pulse-dot"></span>
              <span>VOICE CLONE IDENTITY: DOMINIC NYONGESA</span>
            </div>
            <button class="btn-voice-ref" onclick="playVoiceRef(this)" id="btn-voice-ref">
              <span>🔊</span> <span>Play Original Video Audio Sample</span>
            </button>
            <div class="voice-style-tag">Style: Nairobi Sheng Urban Noir • "Eeh, hii ni mwecheche!"</div>
          </div>

          <div class="hero-cta-row">
            <button class="btn-hero-listen" onclick="toggleAudio()" id="btn-hero-listen">
              <span id="hero-play-icon">▶</span> <span id="hero-play-label">LISTEN TO CASE (SPACE)</span>
            </button>
            <button class="btn-hero-ai" onclick="scrollToSection('aiprompt')">
              <span>⚡</span> INTERROGATE WITH AI
            </button>
          </div>
        </div>

        <!-- HAZARD BAR & METADATA -->
        <div class="manga-sub-strip">
          <div class="hazard-strip-box"></div>
          <div>EST. 2026 // MORINGA CYBERSEC LABS</div>
          <div>TARGET SCOPE: 10.20.0.0/24</div>
        </div>
      </div>

      <!-- HERO RIGHT: 3 MANGA COMIC PANELS (From Dribbble Reference) -->
      <div class="manga-panels-stage" id="manga-panels-stage">
        
        <!-- Panel 1: Eyes Strip -->
        <div class="comic-panel-eyes">
          <img src="panel_eyes.jpg" alt="Investigator Eyes">
          <div class="comic-tag-overlay">WITNESS INTEL // 03:15 AM</div>
        </div>

        <!-- Panel 2: Center Tilted Action Panel -->
        <div class="comic-panel-action" id="comic-panel-action">
          <img src="panel_action_ep01.jpg" alt="Case Action Art" id="action-panel-img">
          <div class="action-speech-bubble" id="action-speech-bubble">Twa twa twa! K-Kile kiumbe... Kinarudi!</div>
        </div>

        <!-- Panel 3: Right Inspector Portrait -->
        <div class="comic-panel-investigator">
          <img src="panel_investigator.jpg" alt="Dominic Nyongesa">
          <div class="action-speech-bubble" style="top: 24px; left: -22px; transform: rotate(-3deg); font-size: 13px; max-width: 175px; background: #fff; border: 2.5px solid #000; padding: 6px 12px; border-radius: 12px; font-weight: 800; font-family: var(--font-grotesk); box-shadow: 4px 4px 0 #000; z-index: 10;">
            Giza lina siri... Eeh, mwecheche!
          </div>
          <div class="investigator-badge">
            <span class="name">DOMINIC NYONGESA</span>
            <span class="role">LEAD INVESTIGATOR</span>
          </div>
        </div>

      </div>
    </section>

    <!-- =========================================================
         TELERIK KENDO UI AIPROMPT COMPONENT
         ========================================================= -->
    <section class="k-aiprompt-wrapper" id="aiprompt">
      
      <!-- Kendo AIPrompt Header -->
      <div class="k-aiprompt-header">
        <div class="k-header-title">
          <span>⚡</span>
          <span>Ngesa AI Dossier Analyst</span>
          <span class="k-ai-badge">STARPOD RAG ENGINE</span>
        </div>
        <div class="k-header-tools">
          <button class="k-tool-btn" onclick="clearAIPrompt()">Clear</button>
          <button class="k-tool-btn" onclick="exportDossierReport()">Export Dossier</button>
        </div>
      </div>

      <!-- Kendo AIPrompt Toolbar Tabs -->
      <div class="k-aiprompt-toolbar">
        <button class="k-view-tab active" id="tab-btn-prompt" onclick="switchKendoView('prompt')">
          <span>💬</span> Ask AI
        </button>
        <button class="k-view-tab" id="tab-btn-outputs" onclick="switchKendoView('outputs')">
          <span>📋</span> Dossier Outputs <span class="k-count-badge" id="k-outputs-count">1</span>
        </button>
        <button class="k-view-tab" id="tab-btn-commands" onclick="switchKendoView('commands')">
          <span>⚡</span> Quick Actions
        </button>
      </div>

      <!-- VIEW 1: PROMPT VIEW -->
      <div class="k-view-content active" id="k-view-prompt">
        <div class="k-prompt-input-box">
          <textarea class="k-prompt-textarea" id="k-prompt-input" placeholder="Ask Dominic's AI dossier analyst anything about this case, folklore origins, forensic timelines, or witness reliability..."></textarea>
          <div class="k-prompt-actions-bar">
            <div class="k-prompt-meta">Shift + Enter for new line • Enter to analyze</div>
            <div class="k-btn-group">
              <button class="k-btn-clear" onclick="document.getElementById('k-prompt-input').value=''">Clear</button>
              <button class="k-btn-generate" onclick="handleGenerateAI()">
                <span>➤</span> Analyze Dossier
              </button>
            </div>
          </div>
        </div>

        <!-- Prompt Suggestions (Chips) -->
        <div class="k-suggestions-container">
          <div class="k-suggestions-label">RECOMMENDED INVESTIGATIVE PROMPTS</div>
          <div class="k-chips-grid" id="k-chips-grid">
            <button class="k-chip" onclick="askPresetPrompt('Explain the hereditary compulsion of Night Runners.')">⚡ Night Runner Compulsion</button>
            <button class="k-chip" onclick="askPresetPrompt('What did Mzee Dennis testify regarding thorn thickets?')">🗣️ Elder Witness Deposition</button>
            <button class="k-chip" onclick="askPresetPrompt('Explain the scientific vs occult explanation for this case.')">⚖️ Scientific vs Parapsychological</button>
            <button class="k-chip" onclick="askPresetPrompt('Tell me about the ghost bus KBS 666 on Ngong Road.')">🚌 Ngong Road Ghost Bus</button>
            <button class="k-chip" onclick="askPresetPrompt('What happened at Menengai Crater in 1854?')">🌋 Menengai 1854 Massacre</button>
            <button class="k-chip" onclick="askPresetPrompt('Who is the goat-footed stranger of Mama Ngina waterfront?')">👣 Mama Ngina Cloven Hooves</button>
            <button class="k-chip" onclick="askPresetPrompt('Give me the forensic breakdown of the Shakahola cult files.')">🩸 Shakahola Cult Forensics</button>
            <button class="k-chip" onclick="askPresetPrompt('What is the Chemosit cryptid in Kakamega Forest?')">🐻 Chemosit Forest Cryptid</button>
          </div>
        </div>
      </div>

      <!-- VIEW 2: OUTPUTS VIEW -->
      <div class="k-view-content" id="k-view-outputs">
        <div class="k-outputs-list" id="k-outputs-list">
          <!-- Initial Output Card -->
          <div class="k-output-card">
            <div class="k-card-header">
              <div class="k-agent-tag"><span>⚡</span> NGESA INTEL // CASE FILE 01</div>
              <div class="k-timestamp">2026-09-18 • CONFIDENCE: 99.2%</div>
            </div>
            <div class="k-prompt-pill">Prompt: Initial Case File Briefing (The Night Runners)</div>
            <div class="k-output-body">
              <strong>EXECUTIVE INVESTIGATIVE SUMMARY:</strong><br>
              Case File 01 investigates the phenomenon of nocturnal somnambulism known as <em>Abanyasi</em> (Luhya) or <em>Omoirori</em> (Gusii). Unlike thieves or violent intruders, night runners operate under an inherited compulsion driven by the psychological thrill of fear.
              <blockquote>"Night running is in the blood. The runner doesn't want to steal your cow. Their curse is the thrill of fear. They sprint through thorn thickets without a single scratch." — Mzee Dennis, Village Elder</blockquote>
              <strong>KEY FORENSIC TAKEAWAY:</strong> Modern parapsychology and psychiatric anthropology classify this as a cultural dissociative fugue state reinforced by generational village mythos and nocturnal territorial rituals.
            </div>
            <div class="k-output-actions">
              <div class="k-action-btn-group">
                <button class="k-action-btn" onclick="copyOutput(this)">📋 Copy</button>
                <button class="k-action-btn" onclick="speakOutput(this)">🔊 Read Out</button>
                <button class="k-action-btn" onclick="toggleAudio()">⏱️ Play Episode</button>
              </div>
              <div class="k-action-btn-group">
                <button class="k-action-btn" onclick="rateOutput(this, true)">👍 Helpful</button>
                <button class="k-action-btn" onclick="rateOutput(this, false)">👎 Needs Corroboration</button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- VIEW 3: COMMANDS VIEW -->
      <div class="k-view-content" id="k-view-commands">
        <div class="k-commands-grid">
          <div class="k-command-card" onclick="runCommand('summary')">
            <div class="k-command-title"><span>📑</span> Executive Case Summary</div>
            <div class="k-command-desc">Generate an immediate high-level briefing of the current case, key suspects, and phenomena.</div>
          </div>
          <div class="k-command-card" onclick="runCommand('timeline')">
            <div class="k-command-title"><span>⏱️</span> Chronological Timeline</div>
            <div class="k-command-desc">Reconstruct the 3:00 AM to 4:30 AM sequence of events and auditory contact.</div>
          </div>
          <div class="k-command-card" onclick="runCommand('forensic')">
            <div class="k-command-title"><span>⚖️</span> Forensic vs Folklore Breakdown</div>
            <div class="k-command-desc">Deconstruct superstitious claims against empirical clinical psychology and regional history.</div>
          </div>
          <div class="k-command-card" onclick="runCommand('witness')">
            <div class="k-command-title"><span>🗣️</span> Witness Cross-Examination</div>
            <div class="k-command-desc">Analyze sworn elder depositions, physiological paralysis claims, and physical trace evidence.</div>
          </div>
          <div class="k-command-card" onclick="runCommand('swahili')">
            <div class="k-command-title"><span>🇰🇪</span> Swahili &amp; Sheng Terminology</div>
            <div class="k-command-desc">Decode tribal vernacular: Abanyasi, Omoirori, Majini, Paka wa Dukani, Chemosit.</div>
          </div>
          <div class="k-command-card" onclick="runCommand('location')">
            <div class="k-command-title"><span>📍</span> Geolocation &amp; Corridor Map</div>
            <div class="k-command-desc">Geographical coordinates, road blackspots, and regional terrain mapping.</div>
          </div>
        </div>
      </div>

    </section>

    <!-- CASE DOSSIER & TRANSCRIPT EXPLORER -->
    <section class="dossier-explorer" id="explorer">
      <div class="dossier-nav-bar" id="dossier-nav-bar">
        <div class="tab-pill-indicator" id="dossier-tab-pill"></div>
        <button class="dossier-tab-btn active" onclick="switchDossierTab('cases', this)">All 8 Cases</button>
        <button class="dossier-tab-btn" onclick="switchDossierTab('transcript', this)">Transcript &bull; Synced</button>
        <button class="dossier-tab-btn" onclick="switchDossierTab('witness', this)">Field Dossier &bull; Lore</button>
        <button class="dossier-tab-btn" onclick="switchDossierTab('broadcast', this)">Broadcast Standards</button>
      </div>

      <!-- PANE 1: ALL 8 CASES GRID -->
      <div class="dossier-pane active" id="pane-cases">
        <div class="episodes-case-grid" id="episodes-case-grid"></div>
      </div>

      <!-- PANE 2: TRANSCRIPT -->
      <div class="dossier-pane" id="pane-transcript">
        <div class="transcript-box" id="transcript-list"></div>
      </div>

      <!-- PANE 3: FIELD DOSSIER & LORE -->
      <div class="dossier-pane" id="pane-witness">
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
          <div>
            <h4 style="font-family:var(--font-grotesk);margin-bottom:8px;">CLASSIFIED PHENOMENON</h4>
            <div id="dossier-phenomenon" style="font-size:13.5px;color:var(--ink-dark);line-height:1.6;margin-bottom:14px;">Hereditary Nocturnal Somnambulism</div>
            <h4 style="font-family:var(--font-grotesk);margin-bottom:8px;">REPORTED BEHAVIOR &amp; TRACES</h4>
            <div id="dossier-behavior" style="font-size:13.5px;color:var(--ink-dark);line-height:1.6;">Slapping iron roofs with mud, sprinting through sisal thorns.</div>
          </div>
          <div>
            <h4 style="font-family:var(--font-grotesk);margin-bottom:8px;">SWORN WITNESS DEPOSITION</h4>
            <blockquote id="dossier-witness" style="font-family:var(--font-serif);font-style:italic;font-size:14px;color:var(--ochre);border-left:3px solid var(--ochre);padding-left:12px;margin-bottom:14px;">
              "You hear footsteps circling your hut like a cheetah."
            </blockquote>
            <h4 style="font-family:var(--font-grotesk);margin-bottom:8px;">SCIENTIFIC &amp; FORENSIC AUDIT</h4>
            <div id="dossier-scientific" style="font-size:13.5px;color:var(--ink-dark);line-height:1.6;">
              Psychological manic-dissociative states and generational village superstition.
            </div>
          </div>
        </div>
      </div>

      <!-- PANE 4: BROADCAST STANDARDS -->
      <div class="dossier-pane" id="pane-broadcast">
        <div style="font-family:var(--font-mono);font-size:13px;line-height:1.7;background:var(--card-paper);padding:18px;border:1.5px solid var(--ink-black);border-radius:4px;">
          <div>🎙️ BROADCAST VOICE SPECIFICATION (NAIROBI STANDARD ENGLISH)</div>
          <div>Integrated Loudness: -16.50 LUFS (Pass: -16.0 &plusmn; 1.0)</div>
          <div>True Peak Headroom: -1.70 dBFS (Pass: &le; -1.0 dBFS)</div>
          <div>Vocal Pace: ~135 Words Per Minute (Measured investigative cadence)</div>
          <div>Starpod Audio Engine: Preloading +10s lookahead chunks actively</div>
          <div>Legal Voice Consent: Validated (24-month actor licensing &amp; synthetic safeguards)</div>
        </div>
      </div>
    </section>

  </main>

  <!-- FIXED DOCKED AUDIO PLAYER -->
  <div class="docked-player" id="docked-player">
    <button class="btn-player-play" onclick="toggleAudio()" id="btn-docked-play">
      <span id="docked-play-icon">▶</span>
    </button>
    
    <div class="player-track-info">
      <div class="player-title" id="docked-player-title">EP 01: The Midnight Knock</div>
      <div class="player-sub" id="docked-player-sub">Case File 01 &bull; Active Narration</div>
    </div>

    <div class="player-waveform-container" onclick="seekAudio(event)">
      <canvas id="wave-canvas"></canvas>
      <div class="player-scrubber">
        <div class="scrubber-fill" id="scrubber-fill"></div>
      </div>
    </div>

    <div class="player-time-box">
      <span id="time-curr">00:00</span> / <span id="time-total">38:15</span>
    </div>

    <div class="starpod-pill-indicator">
      STARPOD: READY
    </div>
    <button class="player-dock-toggle" onclick="togglePlayerDock()" title="Minimize / Expand Player">⚊</button>
  </div>

  <!-- COMMUNITY WIRE DROP MODAL -->
  <div class="drop-modal-overlay" id="drop-modal">
    <div class="drop-modal-card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
        <h3 style="font-family:var(--font-display);font-size:22px;letter-spacing:0.5px;">SUBMIT HORROR EVIDENCE</h3>
        <button onclick="toggleDropModal()" style="background:none;border:none;font-size:18px;cursor:pointer;font-weight:700;">✕</button>
      </div>
      <p style="font-size:13px;color:var(--ink-faint);margin-bottom:16px;">
        Contribute declassified recordings, unexplained highway blackspot sightings, or rural folklore depositions to the open-source Ngesa Diaries archive.
      </p>
      <input type="text" id="drop-location" placeholder="County / Highway / Village (e.g. Salgaa or Kakamega)" style="width:100%;padding:10px;margin-bottom:10px;border:2px solid var(--ink-black);border-radius:3px;font-family:var(--font-mono);font-size:12px;">
      <textarea id="drop-desc" placeholder="Describe the sighting, witness accounts, and audio timestamps..." style="width:100%;height:100px;padding:10px;margin-bottom:14px;border:2px solid var(--ink-black);border-radius:3px;font-family:var(--font-body);font-size:13px;resize:none;"></textarea>
      <div id="drop-alert" style="display:none;background:#00ff66;color:#000;font-family:var(--font-mono);font-size:11px;padding:8px;margin-bottom:10px;text-align:center;font-weight:700;">
        ✓ EVIDENCE RECEIVED. LOGGED TO OPEN-SOURCE ARCHIVE.
      </div>
      <button onclick="submitDrop()" style="width:100%;padding:11px;background:var(--ink-black);color:#fff;border:none;border-radius:999px;font-family:var(--font-grotesk);font-weight:700;font-size:13px;text-transform:uppercase;cursor:pointer;">
        Submit Deposition
      </button>
    </div>
  </div>

  <!-- JAVASCRIPT LOGIC & KENDO AIPROMPT ENGINE -->
  <script>
    const EPISODES = [
      {
        id: "ep01",
        num: 1,
        title: "The Midnight Knock (The Night Runners of Western Kenya)",
        category: "FOLKLORE & OCCULT PHENOMENA",
        tagline: "Kulikua na kisa kule Kisii na Homa Bay... Twa twa twa! Eeh, hii ni mwecheche!",
        duration: "33:00",
        location: "Homa Bay & Kisii Counties",
        kanji: "夜の走者 // USIKU WA MANANE",
        speech: "Twa twa twa! K-Kile kiumbe... Kinarudi!",
        actionImg: "panel_action_ep01.jpg",
        audioUrl: "audio/ep001.mp3",
        synopsis: "Kulikua na kisa kule Kisii na Homa Bay... watu wamelala fofofo saa nane za usiku, ghafla unaskia mchanga unamwagwa kwa bati! Twa twa twa! Na unadhani ni mwizi? La hasha! Ni Night Runner akikimbia uchi porini na kurusha cheche za moto! Wanakijiji wakiamka, mbwa hawabweki na hakuna hata unyayo! Wanapita vichakani kwa kasi ya ajabu bila kuchomwa na miiba. Wazee wanasema ni urithi wa damu kutoka vizazi vya kale. Maze, unadhani ni mchezo? Eeh, hii ni mwecheche!",
        field: {
          phenomenon: "Hereditary Nocturnal Somnambulism / Parapsychological Guild",
          behavior: "Throwing gravel on roofs, riding wild leopards and hyenas, racing through dense sisal without thorns piercing skin.",
          witness: "Mzee Ochieng: 'You hear footsteps circling your hut like a cheetah. You shout, but if you step outside and shine a torch in their eyes, your arm goes paralyzed.'",
          scientific: "A combination of hereditary psychological manic-dissociative states, generational superstition, and village psychological warfare."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Kulikua na kisa kule Kisii na Homa Bay... watu wamelala fofofo saa nane za usiku, ghafla unaskia mchanga unamwagwa kwa bati! Twa twa twa!" },
          { time: "00:10", speaker: "Dominic", text: "Na unadhani ni mwizi? La hasha! Ni Night Runner akikimbia uchi porini na kurusha cheche za moto!" },
          { time: "00:20", speaker: "Dominic", text: "Wanakijiji wakiamka, mbwa hawabweki na hakuna hata unyayo! Wanapita vichakani kwa kasi ya ajabu bila kuchomwa na miiba." },
          { time: "00:28", speaker: "Dominic", text: "Wazee wanasema ni urithi wa damu kutoka vizazi vya kale. Maze, unadhani ni mchezo? Eeh, hii ni mwecheche!" }
        ]
      },
      {
        id: "ep02",
        num: 2,
        title: "The Ghost Bus of Ngong Road (KBS 666 & The Red Matatu)",
        category: "URBAN LEGENDS",
        tagline: "Basi nyekundu ya KBS namba 666 inatokea bila sauti ya injini... Bana, hii ni mwecheche!",
        duration: "33:40",
        location: "Ngong Road & Forest Border, Nairobi",
        kanji: "幽霊バス // BASI LA MAZIMWI",
        speech: "Basi halina dereva... Na watu waka-board?!",
        actionImg: "panel_action_ep02.jpg",
        audioUrl: "audio/ep002.mp3",
        synopsis: "Maze skia hii story bana... Ngong Road saa tisa za usiku katikati ya msitu mnene wa Karen. Basi nyekundu ya zamani ya KBS namba 666 inatokea kwenye kona bila taa wala sauti ya injini! Dereva ametazama mbele haongei, makanga amesimama mlangoni hana uso, lakini ndani abiria wamejaa wametulia kimya kabisa. Na watu waka-board hiyo basi! Wanaingia lakini hakuna anayeshuka Nairobi mzima! Asubuhi ikifika, unakuta gari imeyeyuka kwenye ukungu wa msitu. Bana, hii ni mwecheche!",
        field: {
          phenomenon: "Phantom Vehicle Apparition & Collective Urban Anxiety",
          behavior: "Faint engine purr with no tire spray on wet tarmac; interior illuminated by dim amber incandescent bulb; eerie silence inside the cabin.",
          witness: "Taxi Operator Kamau: 'In 2014, I followed an old KBS bus turning into the forest sanctuary at 2:00 AM. There was no road there—just dense eucalyptus. When my headlights hit it, the vehicle dissolved like smoke.'",
          scientific: "Hypnagogic hallucination induced by late-night fatigue and trauma associated with historical fatal crashes along the dark Ngong Road corridor."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Maze skia hii story bana... Ngong Road saa tisa za usiku katikati ya msitu mnene wa Karen." },
          { time: "00:10", speaker: "Dominic", text: "Basi nyekundu ya zamani ya KBS namba 666 inatokea kwenye kona bila taa wala sauti ya injini!" },
          { time: "00:18", speaker: "Dominic", text: "Dereva ametazama mbele haongei, makanga amesimama mlangoni hana uso, lakini ndani abiria wamejaa wametulia kimya kabisa." },
          { time: "00:26", speaker: "Dominic", text: "Na watu waka-board hiyo basi! Wanaingia lakini hakuna anayeshuka Nairobi mzima! Bana, hii ni mwecheche!" }
        ]
      },
      {
        id: "ep03",
        num: 3,
        title: "Kirima kia Ngoma: The Whispers of Menengai Crater",
        category: "HAUNTED GEOGRAPHY",
        tagline: "Kilima cha mashetani ambapo ngoma zinalia chini ya ardhi... Eeh, hii ni mwecheche!",
        duration: "34:10",
        location: "Menengai Caldera, Nakuru",
        kanji: "悪魔の山 // KIRIMA KIA NGOMA",
        speech: "Sauti za ngoma... Kirima kia Ngoma!",
        actionImg: "panel_action_ep01.jpg",
        audioUrl: "audio/ep003.mp3",
        synopsis: "Imagine ukienda Menengai Crater Nakuru... mahali panaitwa Kirima kia Ngoma, kilima cha mashetani! Watu wakitembea jioni wanaskia ngoma zikilia chini ya ardhi na sauti zikiita majina yao. Mwaka wa 1854 maelfu ya mashujaa wa Maasai walisukumwa kwenye kreta hii wakati wa vita. Hadi leo watalii na wachungaji wanapotea bila viatu, na watu wakapiga picha... picha inatoka moshi na vivuli vya kutisha! Watu wa eneo hilo wanajua jioni ikifika, hutakiwi kutazama ndani ya shimo hilo. Eeh, hii ni mwecheche!",
        field: {
          phenomenon: "Geomagnetic Anomalies & Historic Trauma Apparitions",
          behavior: "Disorientation of compasses, sulfurous mist forming humanoid shapes, phantom sounds of roaring farm machinery at night.",
          witness: "Forest Ranger Kiprop: 'We found his backpack and boots neatly stacked on a basalt rock by the rim. No tracks leading down. The crater swallowed him in broad daylight.'",
          scientific: "Geothermal hydrogen sulfide vents causing sudden hypoxic hallucinations and disorientation in the dense caldera basin."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Imagine ukienda Menengai Crater Nakuru... mahali panaitwa Kirima kia Ngoma, kilima cha mashetani!" },
          { time: "00:10", speaker: "Dominic", text: "Watu wakitembea jioni wanaskia ngoma zikilia chini ya ardhi na sauti zikiita majina yao." },
          { time: "00:20", speaker: "Dominic", text: "Hadi leo watalii wanapotea bila viatu, na picha zikitoka ni moshi mtupu!" },
          { time: "00:28", speaker: "Dominic", text: "Jioni ikifika, hutakiwi kutazama ndani ya shimo hilo. Eeh, hii ni mwecheche!" }
        ]
      },
      {
        id: "ep04",
        num: 4,
        title: "The Goat-Footed Stranger of Mama Ngina (The Mombasa Jinn)",
        category: "COASTAL PARANORMAL",
        tagline: "Miguu ya kwato za mbuzi chini ya mchanga... Maze, hii ni mwecheche!",
        duration: "34:50",
        location: "Old Town Mombasa & Mama Ngina Waterfront",
        kanji: "海岸の魔神 // MAJINI YA PWANI",
        speech: "Kwato za mbuzi Mama Ngina... Eeh, mwecheche!",
        actionImg: "panel_action_ep01.jpg",
        audioUrl: "audio/ep004.mp3",
        synopsis: "Mombasa raha, sivyo? Lakini tembea Mama Ngina Waterfront saa nane za usiku uone mambo! Upepo wa bahari unavuma kwa baridi, ghafla unatokeza mwanamume mtanashati mwenye sauti tamu, amevaa kanzu safi ya kizungu na kofia ya heshima. Anakusalimia kwa lugha ya staha. Lakini ukitazama chini kwa mchanga... miguu yake si ya binadamu! Ni kwato mbili za mbuzi zilizogawanyika! Na watu bado wakamsalimia kabla hawajagundua! Ukipiga kelele anayeyuka na kubaki harufu ya udi na ubani. Maze, hii ni mwecheche!",
        field: {
          phenomenon: "Coastal Jinn Folklore & Merchant Wealth Pacts",
          behavior: "Shadow apparitions shifting into black cats (paka wa dukani), sudden overwhelming scent of rosewater followed by sulfur.",
          witness: "Boda rider Ali: 'A customer flagged me down near Fort Jesus. She had an unearthly perfume. When she lifted her dress to get onto the bike, my headlights caught her feet: two hairy goat hooves clicking against asphalt. I dropped the bike and ran.'",
          scientific: "Centuries-old folklore blending Afro-Arabian pre-Islamic jinn mythology with maritime trader urban anxieties."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Mombasa raha, sivyo? Lakini tembea Mama Ngina Waterfront saa nane za usiku uone mambo!" },
          { time: "00:10", speaker: "Dominic", text: "Ghafla unatokeza mwanamume mtanashati mwenye kanzu safi... lakini ukitazama chini kwa mchanga: ni kwato za mbuzi!" },
          { time: "00:20", speaker: "Dominic", text: "Na watu bado wakamsalimia kabla hawajagundua!" },
          { time: "00:28", speaker: "Dominic", text: "Ukipiga kelele anayeyuka na kubaki harufu ya udi na ubani. Maze, hii ni mwecheche!" }
        ]
      },
      {
        id: "ep05",
        num: 5,
        title: "The Dormitory Above the Crypt (Boarding School Hauntings)",
        category: "KENYAN NOSTALGIA HORROR",
        tagline: "Kengele inalia bila umeme na high heels corridor... Eeh, hii ni mwecheche!",
        duration: "33:20",
        location: "Limuru, Kikuyu & Meru Boarding Schools",
        kanji: "宿舎の亡霊 // KENGELE YA USIKU",
        speech: "High heels corridor... Clack! Clack! Clack!",
        actionImg: "panel_action_ep01.jpg",
        audioUrl: "audio/ep005.mp3",
        synopsis: "Kila Mkenya aliyesoma boarding anajua hii story ya kutisha! Bweni la zamani la shule za Limuru na Meru lililojengwa juu ya makaburi ya enzi za ukoloni. Saa tisa za usiku wakati kila mtu amelala, kengele ya chuma inaanza kulia yenyewe! Ding! Dong! Kisha unaskia viatu virefu vya high heels vikitembea polepole kwa corridor tupu ya saruji: Clack! Clack! Clack! Milango inafunguka yenyewe, blanketi zinavutwa kutoka vitandani, na wasichana wakatoroka kupitia madirishani! Asubuhi wakichunguza, hakuna mtu yeyote aliyekuwemo! Eeh, hii ni mwecheche!",
        field: {
          phenomenon: "Institutional Hysteria & Colonial Heritage Apparitions",
          behavior: "Collective sleep paralysis on top bunks, phantom typewriter sounds in locked staffrooms, unpowered bells ringing.",
          witness: "Alumnus Mercy: 'We were locked in House 4. At 3:15 AM, heavy combat boots started marching down the corridor. In the morning, wet boot prints led straight into a locked wall.'",
          scientific: "High teenage academic stress, sleep deprivation during exam cycles, and psychological contagion in isolated communal living."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Kila Mkenya aliyesoma boarding anajua hii story ya kutisha! Bweni la zamani lililojengwa juu ya makaburi." },
          { time: "00:10", speaker: "Dominic", text: "Saa tisa za usiku kengele inagonga yenyewe! Kisha unaskia high heels zikitembea kwa corridor tupu: Clack! Clack! Clack!" },
          { time: "00:20", speaker: "Dominic", text: "Milango inafunguka yenyewe, blanketi zinavutwa vitandani, na wanafunzi wakatoroka madirishani!" },
          { time: "00:28", speaker: "Dominic", text: "Asubuhi hakuna aliyekuwepo. Eeh, hii ni mwecheche!" }
        ]
      },
      {
        id: "ep06",
        num: 6,
        title: "The Vanishing at Kikopey (The Lady in White of Salgaa)",
        category: "HIGHWAY HORROR",
        tagline: "Mwanamke wa nguo nyeupe anaomba lifti kisha anayeyuka... Bana, hii ni mwecheche!",
        duration: "34:40",
        location: "Nakuru-Eldoret Highway & Kikopey Flats",
        kanji: "白い服の女 // DEREVA WA USIKU",
        speech: "Mwanamke wa Kikopey... Breki zikakata!",
        actionImg: "panel_action_ep02.jpg",
        audioUrl: "audio/ep006.mp3",
        synopsis: "Highway ya Nakuru kuelekea Eldoret pale Kikopey Flats... barabara iliyonyooka lakini giza ni totoro. Madereva wa malori ya masafa marefu wanasimulia kisa cha mwanamke aliyevaa gauni jeupe la harusi, amesimama kando ya lami akiinua mkono kuomba lifti kwenye baridi kali. Dereva mwenye huruma akasimamisha gari na kumkaribisha kwenye kiti cha mbele. Baada ya kilomita tano dereva akimtazama, kiti kiko wazi kabisa, lakini harufu ya maua ya makaburini imetanda garini na breki zinakata ghafla! Wengi wamepoteza maisha kwenye kona hiyo. Bana, hii ni mwecheche!",
        field: {
          phenomenon: "Highway Specter & Post-Traumatic Collective Memory",
          behavior: "Apparition vanishing while vehicle is traveling at 80 km/h; sudden inexplicable loss of engine manifold pressure at exact markers.",
          witness: "Transit Driver Hassan: 'I felt the front door slam. I asked her where she was going. No answer. When I glanced left at the Salgaa bend, she was gone, but her seatbelt was still locked across the empty chair.'",
          scientific: "Severe driver highway hypnosis, circadian rhythm crashes, and psychological manifestations of survivor guilt along high-fatality roads."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Highway ya Nakuru kuelekea Eldoret pale Kikopey Flats... barabara iliyonyooka lakini giza ni totoro." },
          { time: "00:10", speaker: "Dominic", text: "Mwanamke mwenye gauni jeupe la harusi amesimama kando ya lami kuomba lifti kwenye baridi kali." },
          { time: "00:20", speaker: "Dominic", text: "Akiingia garini, baada ya kilomita tano unatazama pembeni: kiti kiko wazi lakini harufu ya maua imetanda!" },
          { time: "00:28", speaker: "Dominic", text: "Ghafla breki zinakata kwenye kona! Bana, hii ni mwecheche!" }
        ]
      },
      {
        id: "ep07",
        num: 7,
        title: "The Starvation Woods of Chakama (The Shakahola Cult Files)",
        category: "TRUE CRIME INVESTIGATION",
        tagline: "Ekari mia nane za msitu wa Shakahola... Giza hapa lina siri kubwa!",
        duration: "35:00",
        location: "Shakahola Forest, Chakama Ranch, Kilifi",
        kanji: "沈黙の森 // SIRI YA SHAKAHOLA",
        speech: "Ekari mia nane za Shakahola... Giza lina siri!",
        actionImg: "panel_action_ep01.jpg",
        audioUrl: "audio/ep007.mp3",
        synopsis: "Hii si hadithi ya kubuni, hii ni ukweli mzito na mchungu wa msitu wa Chakama kule Shakahola. Ekari mia nane za msitu wa miiba katika kaunti ya Kilifi, mahali ambapo mamia ya waumini walidanganywa kufunga chakula na maji hadi kufa ili wakutane na muumba wao kabla ya mwisho wa dunia. Wachunguzi walipoingia ndani ya msitu huo, walikuta makaburi ya halaiki yaliyofukiwa kwa siri. Hata baada ya miezi kadhaa, ukimya wa msitu huo unatia hofu moyoni. Ni ushahidi wa jinsi imani potovu inavyoweza kugeuka kuwa mauti ya kutisha. Giza hapa lina siri kubwa!",
        field: {
          phenomenon: "Coercive Mind Control & Extreme Eschatological Mass Suicide",
          behavior: "Armed enforcers preventing mothers and children from drinking water; structured camps named 'Judea' and 'Bethlehem' hidden miles off the tarmac.",
          witness: "Human Rights Investigator Hussein: 'The silence of that forest was heavy. Under every commiphora tree, the ground had been freshly turned. It wasn't folklore; it was human evil disguised as scripture.'",
          scientific: "Systematic charismatic authority exploitation, cognitive isolation, and induced communal delirium."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Hii si hadithi ya kubuni, hii ni ukweli mzito na mchungu wa msitu wa Chakama kule Shakahola." },
          { time: "00:10", speaker: "Dominic", text: "Ekari mia nane za msitu wa Kilifi ambapo mamia walifundishwa kufunga chakula na maji hadi kufa." },
          { time: "00:20", speaker: "Dominic", text: "Wachunguzi walipofika walikuta makaburi ya halaiki yaliyofukiwa kwa siri chini ya mchanga." },
          { time: "00:28", speaker: "Dominic", text: "Ni ushahidi wa hatari ya imani potovu. Giza hapa lina siri kubwa!" }
        ]
      },
      {
        id: "ep08",
        num: 8,
        title: "The Brain-Eater of Kakamega (The Legend of the Chemosit)",
        category: "CRYPTID INVESTIGATION",
        tagline: "Dubu wa Nandi anayeruka kutoka matawi ya miti... Eeh, hii ni mwecheche!",
        duration: "38:40",
        location: "Kakamega & Nandi Rainforest Canopy",
        kanji: "密林の怪物 // DUDU LA KAKAMEGA",
        speech: "Chemosit wa Kakamega... Anayekula ubongo tu!",
        actionImg: "panel_action_ep01.jpg",
        audioUrl: "audio/ep008.mp3",
        synopsis: "Msitu mkubwa wa Kakamega na vilele vya vilima vya Nandi... wazee wa kabila la Nandi na Luhya wanamfahamu kiumbe anayeitwa Chemosit au Nandi Bear! Wanasema ni mnyama mkubwa nusu simba nusu mtu, mwenye manyoya mekundu, anayetembea kwa miguu miwili na kutoa kicheko kama binadamu gizani! Hakai chini bali anajificha juu ya matawi ya miti mirefu akingoja mtu apite peke yake, kisha anaruka na kumpiga kichwani ili ale ubongo tu na kuacha mwili mzima! Watafiti wa Kizungu walijaribu kumwinda miaka ya 1920 lakini wakaishia kukimbia! Maze, unadhani ni hekaya za watoto? Eeh, hii ni mwecheche!",
        field: {
          phenomenon: "Cryptid Lore & Prehistoric Megafauna Survival Legends",
          behavior: "Eerie high-pitched siren calls at midnight, tree canopy stalking, predation targeting solitary gatherers.",
          witness: "Forest elder Wafula: 'It walks on two legs when it stalks, but runs on four when it charges. When you hear the whistle from the high mahogany branches, you don't look up—you drop your axe and run.'",
          scientific: "Folkloric memory of prehistoric giant baboons (Theropithecus oswaldi) or aberrant giant hyenas surviving in isolated montane pockets."
        },
        transcript: [
          { time: "00:00", speaker: "Dominic", text: "Msitu mkubwa wa Kakamega na vilele vya vilima vya Nandi... wazee wanamfahamu kiumbe anayeitwa Chemosit!" },
          { time: "00:10", speaker: "Dominic", text: "Mnyama nusu simba nusu mtu, mwenye manyoya mekundu, anayetembea kwa miguu miwili gizani!" },
          { time: "00:20", speaker: "Dominic", text: "Anajificha juu ya matawi ya miti akingoja mpita njia ili amle ubongo tu na kuacha mwili!" },
          { time: "00:28", speaker: "Dominic", text: "Maze, unadhani ni hekaya za watoto? Eeh, hii ni mwecheche!" }
        ]
      }
    ];

    let currentIdx = 0;
    let audioPlaying = false;
    let audioCtx = null;
    let osc1, osc2, osc3, filterNode, gainNode;
    let persistentPlayer = new Audio();
    let waveCanvas, waveCtx, waveAnim;
    let kendoOutputs = [
      {
        prompt: "Initial Case File Briefing (The Night Runners of Western Kenya)",
        response: `<strong>EXECUTIVE INVESTIGATIVE SUMMARY:</strong><br>
Case File 01 investigates the phenomenon of nocturnal somnambulism known as <em>Abanyasi</em> (Luhya) or <em>Omoirori</em> (Gusii). Unlike thieves or violent intruders, night runners operate under an inherited compulsion driven by the psychological thrill of fear.<br><br>
<blockquote>"Night running is in the blood. The runner doesn't want to steal your cow. Their curse is the thrill of fear. They sprint through thorn thickets without a single scratch." — Mzee Dennis, Village Elder</blockquote>
<strong>KEY FORENSIC TAKEAWAY:</strong> Modern parapsychology and psychiatric anthropology classify this as a cultural dissociative fugue state reinforced by generational village mythos and nocturnal territorial rituals.`,
        time: "03:15:20",
        caseNum: 1
      }
    ];

    function togglePlayerDock() {
      document.getElementById('docked-player').classList.toggle('minimized');
    }

    // INITIALIZATION
    function init() {
      renderCase(0);
      renderCaseGrid();
      initWaveform();
      initCustomCursor();
      init3DCardTilts();
      initMagneticButtons();
      setupKeybindings();
      updateTabPill(document.querySelector('.dossier-tab-btn.active'));
      renderKendoOutputs();

      if (window.location.search.includes('theme=midnight')) {
        toggleTheme();
      }
      if (window.location.hash === '#aiprompt' || window.location.search.includes('view=aiprompt')) {
        setTimeout(() => {
          scrollToSection('aiprompt');
          if (window.location.search.includes('tab=outputs')) {
            switchKendoView('outputs');
          }
        }, 150);
      }
    }

    // SWITCH CASE FILE
    function switchEpisode(idx) {
      if (idx < 0 || idx >= EPISODES.length) return;
      currentIdx = idx;
      renderCase(currentIdx);
      renderCaseGrid();
      
      // Update Audio Source
      const ep = EPISODES[currentIdx];
      persistentPlayer.src = ep.audioUrl;
      if (audioPlaying) {
        persistentPlayer.play().catch(() => {});
      }
      
      // Update Kendo AIPrompt Suggestions for the selected case
      updateKendoChipsForCase(ep);
    }

    // RENDER ACTIVE CASE FILE INTO HERO & DOSSIER
    function renderCase(idx) {
      const ep = EPISODES[idx];
      document.getElementById('case-meta-tag').innerText = `CASE 0${ep.num} • ${ep.location.toUpperCase()}`;
      document.getElementById('case-card-title').innerText = ep.title;
      document.getElementById('case-card-tagline').innerText = ep.tagline;
      document.getElementById('case-card-body').innerText = ep.synopsis;
      document.getElementById('hero-kanji-tag').innerText = ep.kanji;
      document.getElementById('action-speech-bubble').innerText = ep.speech;
      document.getElementById('action-panel-img').src = ep.actionImg;
      
      // Docked Player Track Info
      document.getElementById('docked-player-title').innerText = `EP 0${ep.num}: ${ep.title}`;
      document.getElementById('docked-player-sub').innerText = `Case File 0${ep.num} • ${ep.duration} • ${ep.category}`;
      document.getElementById('time-total').innerText = ep.duration;

      // Dossier Pane fields
      document.getElementById('dossier-phenomenon').innerText = ep.field.phenomenon;
      document.getElementById('dossier-behavior').innerText = ep.field.behavior;
      document.getElementById('dossier-witness').innerText = `"${ep.field.witness}"`;
      document.getElementById('dossier-scientific').innerText = ep.field.scientific;

      // Render Transcript
      const tList = document.getElementById('transcript-list');
      tList.innerHTML = '';
      (ep.transcript || []).forEach(row => {
        const item = document.createElement('div');
        item.className = 't-row';
        item.innerHTML = `<span class="t-time">${row.time}</span><span><span class="t-speaker">${row.speaker}:</span> ${row.text}</span>`;
        tList.appendChild(item);
      });
    }

    // RENDER ALL 8 CASES GRID
    function renderCaseGrid() {
      const grid = document.getElementById('episodes-case-grid');
      if (!grid) return;
      grid.innerHTML = '';
      EPISODES.forEach((ep, idx) => {
        const tile = document.createElement('div');
        tile.className = `case-tile ${idx === currentIdx ? 'selected' : ''}`;
        tile.onclick = () => {
          switchEpisode(idx);
          scrollToSection('hero');
        };
        tile.innerHTML = `
          <div class="tile-case-num">CASE 0${ep.num} &bull; ${ep.location}</div>
          <div class="tile-case-title">${ep.title}</div>
          <div class="tile-case-sub">${ep.duration} &bull; ${ep.category}</div>
        `;
        grid.appendChild(tile);
      });
    }

    // TELERIK KENDO UI AIPROMPT FUNCTIONS
    function switchKendoView(viewName) {
      document.querySelectorAll('.k-view-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.k-view-content').forEach(c => c.classList.remove('active'));
      
      const tabBtn = document.getElementById(`tab-btn-${viewName}`);
      const viewContent = document.getElementById(`k-view-${viewName}`);
      if (tabBtn) tabBtn.classList.add('active');
      if (viewContent) viewContent.classList.add('active');
    }

    function updateKendoChipsForCase(ep) {
      const grid = document.getElementById('k-chips-grid');
      if (!grid) return;
      grid.innerHTML = `
        <button class="k-chip" onclick="askPresetPrompt('Provide a full executive debriefing on ${ep.title}.')">⚡ Summarize Case 0${ep.num}</button>
        <button class="k-chip" onclick="askPresetPrompt('What is the reported behavior of ${ep.field.phenomenon}?')">🔍 Analyze Reported Behavior</button>
        <button class="k-chip" onclick="askPresetPrompt('Evaluate the sworn witness statement for Case 0${ep.num}.')">🗣️ Witness Cross-Examination</button>
        <button class="k-chip" onclick="askPresetPrompt('What is the clinical scientific perspective on ${ep.title}?')">⚖️ Scientific Evaluation</button>
        <button class="k-chip" onclick="askPresetPrompt('Explain the regional taboo and cultural origins in ${ep.location}.')">🇰🇪 Cultural Lore Context</button>
        <button class="k-chip" onclick="askPresetPrompt('What audio evidence does Dominic present in Episode 0${ep.num}?')">🎙️ Audio Tape Intelligence</button>
      `;
    }

    function askPresetPrompt(promptText) {
      document.getElementById('k-prompt-input').value = promptText;
      handleGenerateAI();
    }

    function handleGenerateAI() {
      const input = document.getElementById('k-prompt-input');
      const text = (input.value || '').trim();
      if (!text) return;

      const currEp = EPISODES[currentIdx];
      
      // Synthesize intelligent response from case metadata
      let responseText = "";
      const lower = text.toLowerCase();

      if (lower.includes("behavior") || lower.includes("compulsion") || lower.includes("speed")) {
        responseText = `<strong>ANALYSIS OF REPORTED BEHAVIORS (CASE 0${currEp.num}):</strong><br>
        Field depositions document consistent behavioral anomalies: <em>${currEp.field.behavior}</em>.<br>
        Dominic's field investigations highlight that perpetrators never seek theft or physical murder; the underlying psychological objective is territorial panic and sensory dominance through midnight terror.`;
      } else if (lower.includes("witness") || lower.includes("elder") || lower.includes("testify")) {
        responseText = `<strong>SWORN WITNESS EXAMINATION:</strong><br>
        <blockquote>"${currEp.field.witness}"</blockquote>
        <strong>INVESTIGATIVE VERDICT:</strong> Witness shows high situational consistency with regional historical depositions dating back to 1954 colonial records. Physiological paralysis reports indicate severe circadian fear induction.`;
      } else if (lower.includes("scientific") || lower.includes("psychology") || lower.includes("medical")) {
        responseText = `<strong>SCIENTIFIC &amp; FORENSIC COUNTER-ANALYSIS:</strong><br>
        Clinical breakdown: <em>${currEp.field.scientific}</em>.<br>
        In accordance with modern behavioral forensics, mass nocturnal panics represent cultural somatoform dissociation rather than supernatural entity manifestation.`;
      } else if (lower.includes("bus") || lower.includes("ngong") || lower.includes("kbs 666")) {
        responseText = `<strong>URBAN APPARITION DOSSIER // KBS 666:</strong><br>
        The phantom Kenya Bus Service transit has been documented along the Adams Arcade to Karen Forest sanctuary corridor since 1982. Eyewitness taxi operators verify engine purr without wet tire spray, and incandescent cabin lighting with unblinking passengers. High correlation with historical fatal crashes along the dark Ngong Road forest corridor.`;
      } else if (lower.includes("menengai") || lower.includes("crater") || lower.includes("1854")) {
        responseText = `<strong>GEOGRAPHIC ANOMALY REPORT // KIRIMA KIA NGOMA:</strong><br>
        In 1854, the battle of Menengai between the Ilpurko and Iloikop Maasai resulted in hundreds of warriors driven over the basalt caldera precipice. The sulfuric fumaroles produce localized hypoxic confusion, explaining phantom machinery sounds and hikers walking into the sulfur mist without returning.`;
      } else if (lower.includes("shakahola") || lower.includes("cult") || lower.includes("mackenzie")) {
        responseText = `<strong>FORENSIC PATHOLOGY DECLASSIFICATION // CHAKAMA RANCH:</strong><br>
        Over 400 shallow mass graves mapped across an 800-acre thorny perimeter in Kilifi. Autopsy records confirm forced systematic starvation, mechanical asphyxiation of defectors, and coercive mind control. This case represents extreme human evil disguised as apocalyptic doctrine.`;
      } else {
        responseText = `<strong>INTELLIGENCE DEBRIEFING // ${currEp.title}:</strong><br>
        ${currEp.synopsis}<br><br>
        <strong>FIELD DOSSIER PARAMETERS:</strong>
        <ul>
          <li><strong>Classification:</strong> ${currEp.field.phenomenon}</li>
          <li><strong>Regional Blackspot:</strong> ${currEp.location}</li>
          <li><strong>Broadcast Headroom:</strong> -16.50 LUFS / -1.70 dBFS</li>
        </ul>`;
      }

      // Add to Outputs
      const outputCard = {
        prompt: text,
        response: responseText,
        time: new Date().toLocaleTimeString(),
        caseNum: currEp.num
      };
      kendoOutputs.unshift(outputCard);
      renderKendoOutputs();

      // Switch to outputs view
      switchKendoView('outputs');
      input.value = '';
    }

    function renderKendoOutputs() {
      const list = document.getElementById('k-outputs-list');
      const badge = document.getElementById('k-outputs-count');
      if (badge) badge.innerText = kendoOutputs.length;
      if (!list) return;

      list.innerHTML = '';
      kendoOutputs.forEach((item, idx) => {
        const div = document.createElement('div');
        div.className = 'k-output-card';
        div.innerHTML = `
          <div class="k-card-header">
            <div class="k-agent-tag"><span>⚡</span> NGESA INTEL // CASE 0${item.caseNum}</div>
            <div class="k-timestamp">${item.time} &bull; CONFIDENCE: 98.6%</div>
          </div>
          <div class="k-prompt-pill">Prompt: "${item.prompt}"</div>
          <div class="k-output-body">${item.response}</div>
          <div class="k-output-actions">
            <div class="k-action-btn-group">
              <button class="k-action-btn" onclick="copyOutput(this)">📋 Copy</button>
              <button class="k-action-btn" onclick="speakOutput(this)">🔊 Read Out</button>
              <button class="k-action-btn" onclick="toggleAudio()">⏱️ Play Episode</button>
            </div>
            <div class="k-action-btn-group">
              <button class="k-action-btn" onclick="rateOutput(this, true)">👍 Helpful</button>
              <button class="k-action-btn" onclick="rateOutput(this, false)">👎 Needs Corroboration</button>
            </div>
          </div>
        `;
        list.appendChild(div);
      });
    }

    function runCommand(cmd) {
      const ep = EPISODES[currentIdx];
      if (cmd === 'summary') {
        askPresetPrompt(`Provide a formal executive case summary of Case 0${ep.num}: ${ep.title}`);
      } else if (cmd === 'timeline') {
        askPresetPrompt(`Reconstruct the 3:00 AM timeline and audible events for Case 0${ep.num}`);
      } else if (cmd === 'forensic') {
        askPresetPrompt(`Deconstruct the empirical forensic evidence versus rural folklore for ${ep.title}`);
      } else if (cmd === 'witness') {
        askPresetPrompt(`Cross-examine the witness testimony and physiological paralysis claims for ${ep.title}`);
      } else if (cmd === 'swahili') {
        askPresetPrompt(`Provide an anthropological glossary of Swahili and tribal occult terms in Kenya`);
      } else if (cmd === 'location') {
        askPresetPrompt(`Provide geographical blackspots and terrain intelligence for ${ep.location}`);
      }
    }

    function clearAIPrompt() {
      kendoOutputs = [];
      renderKendoOutputs();
      switchKendoView('prompt');
    }

    function exportDossierReport() {
      const ep = EPISODES[currentIdx];
      const data = `NGESA DIARIES // DECLASSIFIED CASE DOSSIER REPORT
Case File: 0${ep.num} - ${ep.title}
Location: ${ep.location}
Category: ${ep.category}
Phenomenon: ${ep.field.phenomenon}
Reported Behavior: ${ep.field.behavior}
Witness Deposition: ${ep.field.witness}
Scientific Evaluation: ${ep.field.scientific}
Generated via Ngesa Starpod AI Engine.`;
      
      navigator.clipboard.writeText(data);
      alert("✓ Complete Dossier copied to clipboard in markdown format.");
    }

    function copyOutput(btn) {
      const body = btn.closest('.k-output-card').querySelector('.k-output-body');
      navigator.clipboard.writeText(body.innerText);
      btn.innerText = "✓ Copied";
      setTimeout(() => btn.innerText = "📋 Copy", 1500);
    }

    let voiceRefAudio = new Audio('audio/dominic_voice_reference.mp3');
    function playVoiceRef(btn) {
      if (!voiceRefAudio.paused) {
        voiceRefAudio.pause();
        voiceRefAudio.currentTime = 0;
        btn.querySelector('span:last-child').innerText = 'Play Original Video Audio Sample';
      } else {
        voiceRefAudio.play().then(() => {
          btn.querySelector('span:last-child').innerText = '⏹ Stop Sample ("Mwecheche!")';
        }).catch(e => console.warn(e));
        voiceRefAudio.onended = () => {
          btn.querySelector('span:last-child').innerText = 'Play Original Video Audio Sample';
        };
      }
    }

    let aiVoicePlayer = new Audio();
    function speakOutput(btn) {
      if (!aiVoicePlayer.paused) {
        aiVoicePlayer.pause();
        aiVoicePlayer.currentTime = 0;
        btn.innerText = "🔊 Read Out";
        return;
      }
      const epNum = String(currentIdx + 1).padStart(2, '0');
      const voiceSrc = `audio/ai_case${epNum}.mp3`;
      aiVoicePlayer.src = voiceSrc;
      btn.innerText = "🔊 Playing Voice...";
      aiVoicePlayer.play().then(() => {
        btn.innerText = "⏹ Stop Voice";
      }).catch(err => {
        console.warn("Audio file playback fallback to speech synthesis:", err);
        const body = btn.closest('.k-output-card').querySelector('.k-output-body');
        if ('speechSynthesis' in window) {
          window.speechSynthesis.cancel();
          const utter = new SpeechSynthesisUtterance(body.innerText);
          utter.rate = 0.95;
          window.speechSynthesis.speak(utter);
          btn.innerText = "🔊 Speaking...";
          utter.onend = () => btn.innerText = "🔊 Read Out";
        }
      });
      aiVoicePlayer.onended = () => {
        btn.innerText = "🔊 Read Out";
      };
    }

    function rateOutput(btn, isHelpful) {
      btn.style.background = isHelpful ? 'var(--crimson)' : 'var(--ink-black)';
      btn.style.color = '#fff';
    }

    // AUDIO DRONE & NARRATION SYNTHESIZER
    function toggleAudio() {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      if (!audioPlaying) {
        // Start deep D-minor horror drone
        osc1 = audioCtx.createOscillator();
        osc2 = audioCtx.createOscillator();
        osc3 = audioCtx.createOscillator();
        filterNode = audioCtx.createBiquadFilter();
        gainNode = audioCtx.createGain();

        osc1.type = 'sawtooth';
        osc1.frequency.setValueAtTime(36.7, audioCtx.currentTime); // D1 rumble
        osc2.type = 'sine';
        osc2.frequency.setValueAtTime(51.9, audioCtx.currentTime); // Ab1 dissonant tritone
        osc3.type = 'triangle';
        osc3.frequency.setValueAtTime(73.4, audioCtx.currentTime); // D2

        filterNode.type = 'lowpass';
        filterNode.frequency.setValueAtTime(220, audioCtx.currentTime);
        gainNode.gain.setValueAtTime(0.08, audioCtx.currentTime);

        osc1.connect(filterNode);
        osc2.connect(filterNode);
        osc3.connect(filterNode);
        filterNode.connect(gainNode);
        gainNode.connect(audioCtx.destination);

        osc1.start();
        osc2.start();
        osc3.start();

        // Start Persistent Narration Player
        persistentPlayer.src = EPISODES[currentIdx].audioUrl;
        persistentPlayer.play().catch(() => {});

        audioPlaying = true;
        updateAudioUI(true);
      } else {
        if (osc1) osc1.stop();
        if (osc2) osc2.stop();
        if (osc3) osc3.stop();
        persistentPlayer.pause();

        audioPlaying = false;
        updateAudioUI(false);
      }
    }

    function updateAudioUI(playing) {
      const heroIcon = document.getElementById('hero-play-icon');
      const heroLabel = document.getElementById('hero-play-label');
      const dockedIcon = document.getElementById('docked-play-icon');
      const droneLabel = document.getElementById('drone-label');

      if (playing) {
        if (heroIcon) heroIcon.innerText = '⏸';
        if (heroLabel) heroLabel.innerText = 'PAUSE NARRATION (SPACE)';
        if (dockedIcon) dockedIcon.innerText = '⏸';
        if (droneLabel) droneLabel.innerText = 'Drone: Active';
      } else {
        if (heroIcon) heroIcon.innerText = '▶';
        if (heroLabel) heroLabel.innerText = 'LISTEN TO CASE (SPACE)';
        if (dockedIcon) dockedIcon.innerText = '▶';
        if (droneLabel) droneLabel.innerText = 'Drone: Standby';
      }
    }

    function toggleDrone() {
      toggleAudio();
    }

    function seekAudio(e) {
      const rect = e.currentTarget.getBoundingClientRect();
      const pct = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
      document.getElementById('scrubber-fill').style.width = (pct * 100) + '%';
      if (persistentPlayer && persistentPlayer.duration) {
        persistentPlayer.currentTime = pct * persistentPlayer.duration;
      }
    }

    persistentPlayer.ontimeupdate = () => {
      if (!persistentPlayer.duration) return;
      const pct = (persistentPlayer.currentTime / persistentPlayer.duration) * 100;
      document.getElementById('scrubber-fill').style.width = pct + '%';
      
      const m = Math.floor(persistentPlayer.currentTime / 60);
      const s = Math.floor(persistentPlayer.currentTime % 60);
      document.getElementById('time-curr').innerText = `${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
    };

    // BEARPLUS MULTI-HARMONIC FLUID RIBBON WAVEFORM
    function initWaveform() {
      waveCanvas = document.getElementById('wave-canvas');
      waveCtx = waveCanvas.getContext('2d');
      waveCanvas.width = waveCanvas.parentElement.clientWidth;
      waveCanvas.height = waveCanvas.parentElement.clientHeight;
      drawWave();
    }

    function drawWave() {
      waveCtx.clearRect(0, 0, waveCanvas.width, waveCanvas.height);
      const w = waveCanvas.width;
      const h = waveCanvas.height;
      const midY = h / 2;
      const t = Date.now() * 0.0035;

      const grad = waveCtx.createLinearGradient(0, 0, w, 0);
      grad.addColorStop(0, audioPlaying ? 'rgba(217, 164, 65, 0.25)' : 'rgba(0, 0, 0, 0.05)');
      grad.addColorStop(0.5, audioPlaying ? 'rgba(255, 42, 75, 0.45)' : 'rgba(0, 0, 0, 0.08)');
      grad.addColorStop(1, audioPlaying ? 'rgba(217, 164, 65, 0.25)' : 'rgba(0, 0, 0, 0.05)');

      const points = 50;
      const dx = w / points;

      waveCtx.beginPath();
      waveCtx.moveTo(0, midY);
      for (let i = 0; i <= points; i++) {
        const x = i * dx;
        const norm = Math.sin((i / points) * Math.PI);
        let amp = 2;
        if (audioPlaying) {
          amp = (Math.sin(t * 1.6 + i * 0.25) * 6 + Math.cos(t * 2.2 + i * 0.18) * 8) * norm + 2;
        }
        waveCtx.lineTo(x, midY - amp);
      }
      for (let i = points; i >= 0; i--) {
        const x = i * dx;
        const norm = Math.sin((i / points) * Math.PI);
        let amp = 2;
        if (audioPlaying) {
          amp = (Math.sin(t * 1.6 + i * 0.25) * 6 + Math.cos(t * 2.2 + i * 0.18) * 8) * norm + 2;
        }
        waveCtx.lineTo(x, midY + amp);
      }
      waveCtx.closePath();
      waveCtx.fillStyle = grad;
      waveCtx.fill();

      waveCtx.beginPath();
      for (let i = 0; i <= points; i++) {
        const x = i * dx;
        const norm = Math.sin((i / points) * Math.PI);
        let amp = 2;
        if (audioPlaying) {
          amp = (Math.sin(t * 1.6 + i * 0.25) * 6 + Math.cos(t * 2.2 + i * 0.18) * 8) * norm;
        }
        const y = midY - amp;
        if (i === 0) waveCtx.moveTo(x, y); else waveCtx.lineTo(x, y);
      }
      waveCtx.lineWidth = 1.8;
      waveCtx.strokeStyle = audioPlaying ? '#ff2a4b' : '#0c0e12';
      waveCtx.stroke();

      waveAnim = requestAnimationFrame(drawWave);
    }

    // BEARPLUS CUSTOM CURSOR & DYNAMICS
    let mouse = { x: 740, y: 380 };
    let ringPos = { x: mouse.x, y: mouse.y };

    function initCustomCursor() {
      const follower = document.getElementById('cursor-finger-follower');
      const ring = document.getElementById('cursor-ring');
      if (!follower && !ring) return;

      function updateFollower(x, y) {
        if (follower) {
          follower.style.left = `${x}px`;
          follower.style.top = `${y}px`;
        }
      }

      // Initial placement
      updateFollower(mouse.x, mouse.y);
      if (ring) {
        ring.style.left = `${mouse.x}px`;
        ring.style.top = `${mouse.y}px`;
      }

      window.addEventListener('mousemove', (e) => {
        mouse.x = e.clientX;
        mouse.y = e.clientY;
        updateFollower(mouse.x, mouse.y);
      });

      function renderCursor() {
        ringPos.x += (mouse.x - ringPos.x) * 0.18;
        ringPos.y += (mouse.y - ringPos.y) * 0.18;
        if (ring) {
          ring.style.left = `${ringPos.x.toFixed(2)}px`;
          ring.style.top = `${ringPos.y.toFixed(2)}px`;
        }
        requestAnimationFrame(renderCursor);
      }
      renderCursor();

      const hoverTargets = 'a, button, .case-tile, input, textarea, .k-chip, .k-command-card, .comic-panel-action, .btn-pill-cta';
      document.querySelectorAll(hoverTargets).forEach(el => {
        el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
        el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
      });
    }

    // 3D PERSPECTIVE CARD TILTS
    function init3DCardTilts() {
      const cards = document.querySelectorAll('.active-case-card, .comic-panel-action, .k-aiprompt-wrapper');
      cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
          const rect = card.getBoundingClientRect();
          const x = e.clientX - rect.left;
          const y = e.clientY - rect.top;
          const cx = rect.width / 2;
          const cy = rect.height / 2;
          const rotX = ((cy - y) / cy) * 4;
          const rotY = ((x - cx) / cx) * 4;
          card.style.transform = `perspective(1200px) rotateX(${rotX.toFixed(2)}deg) rotateY(${rotY.toFixed(2)}deg) translateZ(4px)`;
        });
        card.addEventListener('mouseleave', () => {
          card.style.transform = 'perspective(1200px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
        });
      });
    }

    // MAGNETIC BUTTONS
    function initMagneticButtons() {
      const magnetics = document.querySelectorAll('.btn-pill-cta, .btn-hero-listen, .btn-hero-ai, .btn-player-play');
      magnetics.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
          const rect = btn.getBoundingClientRect();
          const cx = rect.left + rect.width / 2;
          const cy = rect.top + rect.height / 2;
          const pullX = (e.clientX - cx) * 0.22;
          const pullY = (e.clientY - cy) * 0.22;
          btn.style.transform = `translate(${pullX.toFixed(1)}px, ${pullY.toFixed(1)}px)`;
        });
        btn.addEventListener('mouseleave', () => {
          btn.style.transform = 'translate(0px, 0px)';
        });
      });
    }

    // THEME SWITCHER (Manga Graphic Novel Paper vs Deep Noir Midnight)
    function toggleTheme() {
      document.body.classList.toggle('theme-midnight');
      const isMidnight = document.body.classList.contains('theme-midnight');
      document.getElementById('theme-icon').innerText = isMidnight ? '☀️' : '🌓';
      document.getElementById('theme-label').innerText = isMidnight ? 'Manga Paper' : 'Midnight';
    }

    // TAB INDICATOR FOR DOSSIER EXPLORER
    function updateTabPill(btn) {
      const pill = document.getElementById('dossier-tab-pill');
      if (!pill || !btn) return;
      pill.style.transform = `translateX(${btn.offsetLeft}px)`;
      pill.style.width = `${btn.offsetWidth}px`;
    }

    function switchDossierTab(paneName, btn) {
      document.querySelectorAll('.dossier-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.dossier-pane').forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      document.getElementById(`pane-${paneName}`).classList.add('active');
      updateTabPill(btn);
    }

    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    function toggleDropModal() {
      document.getElementById('drop-modal').classList.toggle('open');
    }

    function submitDrop() {
      const alert = document.getElementById('drop-alert');
      alert.style.display = 'block';
      setTimeout(() => {
        toggleDropModal();
        alert.style.display = 'none';
      }, 2000);
    }

    function setupKeybindings() {
      window.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
        if (e.code === 'Space') {
          e.preventDefault();
          toggleAudio();
        } else if (e.key >= '1' && e.key <= '8') {
          switchEpisode(parseInt(e.key) - 1);
        } else if (e.key.toLowerCase() === 'a') {
          scrollToSection('aiprompt');
        } else if (e.key.toLowerCase() === 't') {
          toggleTheme();
        }
      });
    }

    window.onload = init;
  </script>
</body>
</html>
"""

with open('/home/yourusername/Projects/darknet-kenya/index.html', 'w', encoding='utf-8') as f:
    f.write(page_content)

print("Upgraded index.html successfully generated!")
