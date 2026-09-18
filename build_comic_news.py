#!/usr/bin/env python3
"""
build_comic_news.py - Generates the Graphic Novel News Platform for Ngesa Chronicle
Host & Lead Investigator: Dominic Nyongesa (@ngesa-cloud)
Theme: Comic Book Journalism / Animated Visual Storytelling / Noir News Agency
"""

import os

def generate():
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NGESA CHRONICLE // Declassified Graphic Novel Journalism</title>

  <!-- Google Fonts: Anton (Pulp Comic & Masthead), Bangers (Comic Sound FX), Space Grotesk, Space Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Anton&family=Bangers&family=Space+Grotesk:wght@400;500;600;700&family=Space+Mono:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">

  <style>
    :root {
      --news-paper: #f6f1e8;
      --news-ink: #0c0e12;
      --crimson: #ff2a4b;
      --crimson-dark: #b80d28;
      --crimson-glow: rgba(255, 42, 75, 0.4);
      --yellow-burst: #ffd000;
      --paper-tint: #eae3d2;
      --lead-gray: #4a505b;
      --border-ink: #11141a;
      --card-bg: #ffffff;
      --shadow-hard: 6px 6px 0px #0c0e12;
      --shadow-hard-sm: 3px 3px 0px #0c0e12;

      --font-display: 'Anton', impact, sans-serif;
      --font-comic: 'Bangers', cursive, sans-serif;
      --font-grotesk: 'Space Grotesk', -apple-system, sans-serif;
      --font-mono: 'Space Mono', monospace;
    }

    /* THEME: MIDNIGHT REDACTED NOIR */
    body.theme-midnight {
      --news-paper: #080a0f;
      --news-ink: #f0f2f5;
      --paper-tint: #12151d;
      --lead-gray: #8d95a5;
      --border-ink: #ffffff;
      --card-bg: #0e1219;
      --shadow-hard: 6px 6px 0px #ff2a4b;
      --shadow-hard-sm: 3px 3px 0px #ff2a4b;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
    }

    body {
      background-color: var(--news-paper);
      color: var(--news-ink);
      font-family: var(--font-grotesk);
      line-height: 1.5;
      overflow-x: hidden;
      min-height: 100vh;
      position: relative;
      transition: background-color 0.3s ease, color 0.3s ease;
      cursor: url('cursor_finger_32.png') 6 4, auto;
    }

    a, button, input, textarea, select, .k-chip, .k-command-card, .case-card, .brand-cluster, .btn-pill-cta {
      cursor: url('cursor_finger_32.png') 6 4, pointer !important;
    }

    /* Among Us Batman Finger Custom Cursor Follower */
    #cursor-finger-follower {
      position: fixed;
      top: 0; left: 0;
      width: 44px; height: 44px;
      pointer-events: none;
      z-index: 10000;
      transform: translate(-10px, -6px);
      transition: opacity 0.2s ease;
    }
    #cursor-finger-follower img {
      width: 100%; height: 100%;
      object-fit: contain;
      filter: drop-shadow(2px 3px 5px rgba(0, 0, 0, 0.65));
      transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), filter 0.2s ease;
    }
    body.cursor-hover #cursor-finger-follower img {
      transform: scale(1.22) rotate(-8deg);
      filter: drop-shadow(0 0 12px rgba(255, 42, 75, 0.85)) drop-shadow(2px 4px 6px rgba(0,0,0,0.8));
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

    /* HALFTONE COMIC SCREEN OVERLAY */
    .halftone-screen {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 9990;
      opacity: 0.035;
      background-image: radial-gradient(#000000 1px, transparent 1px);
      background-size: 4px 4px;
    }
    body.theme-midnight .halftone-screen {
      opacity: 0.06;
      background-image: radial-gradient(#ffffff 1px, transparent 1px);
    }

    /* AMBIENT NOIR RAIN CANVAS */
    #ambient-rain-canvas {
      position: fixed;
      top: 0; left: 0; width: 100vw; height: 100vh;
      pointer-events: none;
      z-index: 9980;
      opacity: 0.3;
    }

    /* =========================================================
       TOP LIVE BREAKING NEWS TICKER
       ========================================================= */
    .top-breaking-bar {
      background: #000000;
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      display: flex;
      align-items: center;
      border-bottom: 2px solid var(--crimson);
      overflow: hidden;
      height: 32px;
      position: sticky;
      top: 0;
      z-index: 500;
    }
    .breaking-label {
      background: var(--crimson);
      color: #ffffff;
      padding: 0 16px;
      height: 100%;
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-display);
      font-size: 14px;
      letter-spacing: 1px;
      flex-shrink: 0;
      z-index: 2;
    }
    .live-pulse {
      width: 8px; height: 8px;
      background: #ffffff;
      border-radius: 50%;
      animation: pulseBlink 1s infinite;
    }
    @keyframes pulseBlink {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.2; transform: scale(0.8); }
    }
    .ticker-marquee {
      white-space: nowrap;
      display: flex;
      gap: 40px;
      animation: marqueeScroll 35s linear infinite;
      padding-left: 20px;
    }
    .ticker-marquee:hover {
      animation-play-state: paused;
    }
    .ticker-item {
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }
    .ticker-item span.red-dot {
      color: var(--crimson);
      font-weight: 900;
    }
    @keyframes marqueeScroll {
      0% { transform: translateX(0%); }
      100% { transform: translateX(-50%); }
    }

    /* =========================================================
       NEWSPAPER MASTHEAD (THE NGESA CHRONICLE)
       ========================================================= */
    .newspaper-header {
      border-bottom: 3px double var(--border-ink);
      padding: 16px 28px 12px 28px;
      background: var(--news-paper);
      position: relative;
    }
    .masthead-meta-top {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid rgba(0,0,0,0.15);
      padding-bottom: 6px;
      margin-bottom: 12px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--lead-gray);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    body.theme-midnight .masthead-meta-top {
      border-bottom-color: rgba(255,255,255,0.15);
      color: #9aa0a6;
    }
    .masthead-main {
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      align-items: center;
      gap: 20px;
    }
    .masthead-left-box {
      font-family: var(--font-mono);
      font-size: 11.5px;
      line-height: 1.4;
      border-left: 3px solid var(--crimson);
      padding-left: 10px;
    }
    .masthead-center {
      text-align: center;
    }
    .masthead-title {
      font-family: var(--font-display);
      font-size: 64px;
      line-height: 0.9;
      letter-spacing: 2px;
      text-transform: uppercase;
      color: var(--news-ink);
      text-shadow: 2px 2px 0px rgba(0,0,0,0.1);
    }
    .masthead-title span.red {
      color: var(--crimson);
    }
    .masthead-sub {
      font-family: var(--font-mono);
      font-size: 11px;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-top: 6px;
      font-weight: 700;
    }
    .masthead-right-box {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 8px;
    }
    .editor-seal {
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--card-bg);
      border: 1.5px solid var(--border-ink);
      padding: 4px 10px;
      border-radius: 999px;
      box-shadow: 2px 2px 0px var(--border-ink);
    }
    .editor-avatar {
      width: 24px; height: 24px;
      border-radius: 50%;
      object-fit: cover;
      border: 1px solid var(--border-ink);
    }
    .editor-name {
      font-size: 11px;
      font-weight: 700;
    }
    .masthead-controls {
      display: flex;
      gap: 8px;
    }
    .btn-pill-cta {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 6px 14px;
      border-radius: 999px;
      font-family: var(--font-grotesk);
      font-size: 11.5px;
      font-weight: 700;
      border: 1.5px solid var(--border-ink);
      background: var(--card-bg);
      color: var(--news-ink);
      box-shadow: 2px 2px 0px var(--border-ink);
      transition: all 0.15s ease;
    }
    .btn-pill-cta:hover {
      transform: translate(-1px, -1px);
      box-shadow: 4px 4px 0px var(--border-ink);
      background: var(--news-ink);
      color: var(--news-paper);
    }

    /* SUBNAV STRIP */
    .subnav-strip {
      display: flex;
      justify-content: center;
      gap: 20px;
      border-top: 1px solid var(--border-ink);
      border-bottom: 2px solid var(--border-ink);
      padding: 7px 0;
      background: var(--paper-tint);
      margin-top: 10px;
    }
    .subnav-link {
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      color: var(--news-ink);
      text-decoration: none;
      padding: 2px 8px;
      border-radius: 3px;
      transition: background 0.2s ease;
    }
    .subnav-link:hover, .subnav-link.active {
      background: var(--crimson);
      color: #ffffff;
    }

    /* =========================================================
       MAIN FRONT-PAGE COMIC EDITORIAL STAGE
       ========================================================= */
    .app-main {
      max-width: 1440px;
      margin: 0 auto;
      padding: 28px 24px 80px 24px;
      display: flex;
      flex-direction: column;
      gap: 40px;
    }

    /* FRONT PAGE HEADLINE & COMIC SPREAD */
    .front-page-grid {
      display: grid;
      grid-template-columns: 1.15fr 1.35fr;
      gap: 28px;
      align-items: start;
    }

    /* LEFT: INVESTIGATIVE STORY COLUMN */
    .story-column {
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .story-category-stamp {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--crimson);
      color: #ffffff;
      padding: 4px 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      width: fit-content;
      box-shadow: 3px 3px 0px #000;
    }
    .headline-main {
      font-family: var(--font-display);
      font-size: 46px;
      line-height: 1.02;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      border-bottom: 2px solid var(--border-ink);
      padding-bottom: 12px;
    }
    .byline-bar {
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 11.5px;
      color: var(--lead-gray);
      border-bottom: 1px dashed var(--border-ink);
      padding-bottom: 8px;
    }
    .story-lead-quote {
      font-size: 17px;
      font-weight: 700;
      font-style: italic;
      color: var(--crimson);
      line-height: 1.4;
      border-left: 3px solid var(--crimson);
      padding-left: 12px;
    }
    .story-body-text {
      font-size: 14px;
      line-height: 1.7;
      text-align: justify;
      color: var(--news-ink);
    }
    .story-body-text p {
      margin-bottom: 12px;
    }

    /* COMIC ANIMATION CONTROLLER TOOLBAR */
    .comic-controls-bar {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 10px;
      background: var(--paper-tint);
      border: 2px solid var(--border-ink);
      padding: 12px 16px;
      box-shadow: var(--shadow-hard-sm);
      border-radius: 4px;
    }
    .btn-comic-action {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--card-bg);
      color: var(--news-ink);
      border: 1.5px solid var(--border-ink);
      border-radius: 4px;
      padding: 8px 14px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      transition: all 0.15s ease;
    }
    .btn-comic-action.primary {
      background: var(--crimson);
      color: #ffffff;
      border-color: var(--crimson);
    }
    .btn-comic-action:hover {
      transform: translate(-1px, -1px);
      box-shadow: 3px 3px 0px var(--border-ink);
    }
    .btn-comic-action.primary:hover {
      background: var(--crimson-dark);
      box-shadow: 3px 3px 0px #000;
    }

    /* =========================================================
       RIGHT: THE 4-FRAME ANIMATED GRAPHIC NOVEL STAGE
       ========================================================= */
    .comic-stage-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      grid-template-rows: auto auto;
      gap: 14px;
      position: relative;
    }

    /* COMIC FRAME WRAPPER */
    .comic-frame {
      border: 3px solid var(--border-ink);
      background: #000000;
      position: relative;
      overflow: hidden;
      box-shadow: var(--shadow-hard);
      border-radius: 2px;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), box-shadow 0.25s ease;
    }
    .comic-frame:hover {
      transform: scale(1.02) translateY(-2px);
      box-shadow: 8px 8px 0px var(--crimson);
      z-index: 5;
    }
    .comic-frame.active-focus {
      border-color: var(--crimson);
      box-shadow: 0 0 20px var(--crimson-glow), var(--shadow-hard);
    }

    /* Frame 1: Eyewitness Surveillance Top Strip */
    .frame-surveillance {
      grid-column: 1 / 3;
      height: 150px;
    }
    .frame-surveillance img {
      width: 100%; height: 100%;
      object-fit: cover;
      filter: contrast(125%) grayscale(80%);
      transition: filter 0.3s;
    }
    .frame-surveillance:hover img {
      filter: contrast(140%) grayscale(0%);
    }

    /* Surveillance Overlays */
    .crt-scanlines {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.4) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.04), rgba(0, 255, 0, 0.01), rgba(0, 255, 0, 0.04));
      background-size: 100% 3px, 6px 100%;
      pointer-events: none;
    }
    .cam-hud-tag {
      position: absolute;
      top: 10px; left: 12px;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      color: #ffffff;
      background: rgba(0, 0, 0, 0.75);
      padding: 3px 8px;
      border: 1px solid rgba(255,255,255,0.3);
      display: flex;
      align-items: center;
      gap: 6px;
      z-index: 4;
    }
    .cam-rec-dot {
      width: 7px; height: 7px;
      background: var(--crimson);
      border-radius: 50%;
      animation: pulseBlink 0.8s infinite;
    }

    /* Frame 2: Main Dynamic Action Panel */
    .frame-action-main {
      grid-column: 1 / 2;
      height: 290px;
    }
    .frame-action-main img {
      width: 100%; height: 100%;
      object-fit: cover;
      transition: transform 0.4s ease;
    }
    .frame-action-main:hover img {
      transform: scale(1.06);
    }

    /* Onomatopoeia Comic Sound Burst */
    .sfx-burst-badge {
      position: absolute;
      top: 14px; right: 14px;
      background: var(--yellow-burst);
      color: #000000;
      font-family: var(--font-comic);
      font-size: 26px;
      letter-spacing: 1px;
      padding: 4px 14px;
      border: 2.5px solid #000000;
      transform: rotate(8deg);
      box-shadow: 3px 3px 0px #000000;
      z-index: 4;
      animation: sfxShake 2s infinite ease-in-out;
    }
    @keyframes sfxShake {
      0%, 100% { transform: rotate(8deg) scale(1); }
      50% { transform: rotate(4deg) scale(1.05); }
    }

    /* Speech Bubble */
    .comic-speech-bubble {
      position: absolute;
      bottom: 14px; left: 14px; right: 14px;
      background: #ffffff;
      color: #000000;
      border: 2.5px solid #000000;
      border-radius: 12px;
      padding: 8px 14px;
      font-family: var(--font-grotesk);
      font-size: 12px;
      font-weight: 800;
      box-shadow: 3px 3px 0px #000000;
      z-index: 4;
    }

    /* Frame 3: Lead Investigator Dominic Nyongesa */
    .frame-investigator {
      grid-column: 2 / 3;
      height: 290px;
    }
    .frame-investigator img {
      width: 100%; height: 100%;
      object-fit: cover;
    }
    .investigator-badge {
      position: absolute;
      bottom: 12px; left: 12px;
      background: rgba(13, 15, 18, 0.92);
      color: #ffffff;
      padding: 6px 12px;
      border-left: 3px solid var(--crimson);
      font-family: var(--font-mono);
      font-size: 10.5px;
      z-index: 4;
    }
    .investigator-badge .role {
      color: var(--crimson);
      font-weight: 700;
      display: block;
    }

    /* Floating Comic Click SFX Element */
    .comic-pop-sfx {
      position: fixed;
      pointer-events: none;
      font-family: var(--font-comic);
      font-size: 32px;
      color: var(--yellow-burst);
      text-shadow: 3px 3px 0px #000000, -2px -2px 0px #ff2a4b;
      z-index: 10001;
      animation: floatUpSfx 0.9s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
    @keyframes floatUpSfx {
      0% { opacity: 1; transform: translate(-50%, -50%) scale(0.6) rotate(-10deg); }
      50% { transform: translate(-50%, -80px) scale(1.3) rotate(5deg); }
      100% { opacity: 0; transform: translate(-50%, -130px) scale(1) rotate(15deg); }
    }

    /* =========================================================
       BREAKING INVESTIGATIVE DISPATCHES (ALL 8 CASES)
       ========================================================= */
    .news-section {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .section-header-banner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 3px solid var(--border-ink);
      border-bottom: 2px solid var(--border-ink);
      padding: 10px 0;
    }
    .section-title {
      font-family: var(--font-display);
      font-size: 32px;
      letter-spacing: 1px;
      text-transform: uppercase;
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .section-title span.tag {
      background: var(--crimson);
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 12px;
      padding: 3px 8px;
    }

    /* 8 CASES GRID */
    .cases-news-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
    }
    .case-card {
      background: var(--card-bg);
      border: 2px solid var(--border-ink);
      box-shadow: var(--shadow-hard-sm);
      display: flex;
      flex-direction: column;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      overflow: hidden;
      position: relative;
    }
    .case-card:hover {
      transform: translate(-3px, -3px);
      box-shadow: 6px 6px 0px var(--crimson);
      border-color: var(--crimson);
    }
    .case-card.active-selected {
      border-color: var(--crimson);
      box-shadow: 6px 6px 0px var(--crimson);
    }
    .case-card-thumb {
      height: 150px;
      position: relative;
      overflow: hidden;
      background: #000000;
      border-bottom: 2px solid var(--border-ink);
    }
    .case-card-thumb img {
      width: 100%; height: 100%;
      object-fit: cover;
      transition: transform 0.3s ease;
    }
    .case-card:hover .case-card-thumb img {
      transform: scale(1.08);
    }
    .case-badge-overlay {
      position: absolute;
      top: 8px; left: 8px;
      background: var(--crimson);
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      padding: 2px 7px;
      box-shadow: 2px 2px 0px #000;
    }
    .case-card-content {
      padding: 14px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
      gap: 8px;
    }
    .case-location {
      font-family: var(--font-mono);
      font-size: 10.5px;
      color: var(--lead-gray);
      text-transform: uppercase;
    }
    .case-title {
      font-family: var(--font-display);
      font-size: 20px;
      line-height: 1.15;
      text-transform: uppercase;
      color: var(--news-ink);
    }
    .case-tagline {
      font-size: 12px;
      color: var(--lead-gray);
      line-height: 1.4;
      flex-grow: 1;
    }
    .btn-read-dispatch {
      margin-top: 6px;
      background: var(--news-ink);
      color: var(--news-paper);
      border: none;
      padding: 7px 12px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      border-radius: 3px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: background 0.15s;
    }
    .case-card:hover .btn-read-dispatch {
      background: var(--crimson);
      color: #ffffff;
    }

    /* =========================================================
       TELERIK KENDO UI AIPROMPT (INTELLIGENCE NEWS DESK)
       ========================================================= */
    .k-aiprompt-wrapper {
      background: var(--card-bg);
      border: 3px solid var(--border-ink);
      box-shadow: var(--shadow-hard);
      border-radius: 4px;
      overflow: hidden;
    }
    .k-aiprompt-header {
      background: var(--news-ink);
      color: #ffffff;
      padding: 14px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 2px solid var(--crimson);
    }
    .k-header-title {
      font-family: var(--font-display);
      font-size: 20px;
      letter-spacing: 1px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .k-ai-badge {
      background: var(--crimson);
      color: #ffffff;
      font-family: var(--font-mono);
      font-size: 10px;
      padding: 2px 8px;
      border-radius: 2px;
    }
    .k-header-tools {
      display: flex;
      gap: 8px;
    }
    .k-tool-btn {
      background: rgba(255, 255, 255, 0.1);
      color: #ffffff;
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 4px 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      border-radius: 3px;
    }
    .k-tool-btn:hover {
      background: var(--crimson);
      border-color: var(--crimson);
    }

    /* Views Toolbar */
    .k-views-toolbar {
      display: flex;
      background: var(--paper-tint);
      border-bottom: 2px solid var(--border-ink);
      padding: 0 16px;
      gap: 4px;
    }
    .k-view-tab {
      padding: 12px 18px;
      font-family: var(--font-grotesk);
      font-size: 13px;
      font-weight: 700;
      background: none;
      border: none;
      border-bottom: 3px solid transparent;
      color: var(--lead-gray);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .k-view-tab.active {
      color: var(--news-ink);
      border-bottom-color: var(--crimson);
      background: var(--card-bg);
    }

    /* Tab Content Views */
    .k-view-content {
      display: none;
      padding: 22px;
    }
    .k-view-content.active {
      display: block;
    }

    /* Prompt Input View */
    .k-prompt-box {
      border: 2px solid var(--border-ink);
      border-radius: 4px;
      padding: 14px;
      background: var(--news-paper);
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .k-prompt-textarea {
      width: 100%;
      min-height: 80px;
      border: none;
      background: transparent;
      font-family: var(--font-grotesk);
      font-size: 14px;
      resize: vertical;
      outline: none;
      color: var(--news-ink);
    }
    .k-prompt-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid rgba(0,0,0,0.1);
      padding-top: 10px;
    }
    .k-prompt-hint {
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--lead-gray);
    }
    .k-prompt-actions {
      display: flex;
      gap: 8px;
    }
    .k-btn-generate {
      background: var(--crimson);
      color: #ffffff;
      border: 1.5px solid #000;
      padding: 8px 18px;
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 700;
      border-radius: 4px;
      box-shadow: 2px 2px 0px #000;
    }
    .k-btn-generate:hover {
      background: var(--crimson-dark);
      transform: translate(-1px, -1px);
      box-shadow: 4px 4px 0px #000;
    }

    /* Chips Container */
    .k-chips-label {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      margin: 16px 0 8px 0;
      color: var(--lead-gray);
    }
    .k-chips-group {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
    }
    .k-chip {
      background: var(--paper-tint);
      border: 1.5px solid var(--border-ink);
      border-radius: 999px;
      padding: 5px 12px;
      font-family: var(--font-grotesk);
      font-size: 12px;
      font-weight: 600;
      color: var(--news-ink);
      transition: all 0.15s ease;
    }
    .k-chip:hover {
      background: var(--crimson);
      color: #ffffff;
      border-color: var(--crimson);
      transform: translateY(-1px);
    }

    /* Outputs View */
    .k-output-card {
      border: 2px solid var(--border-ink);
      border-radius: 4px;
      padding: 16px;
      background: var(--news-paper);
      margin-bottom: 14px;
      box-shadow: var(--shadow-hard-sm);
    }
    .k-output-header {
      display: flex;
      justify-content: space-between;
      border-bottom: 1px dashed var(--border-ink);
      padding-bottom: 8px;
      margin-bottom: 12px;
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--crimson);
      font-weight: 700;
    }
    .k-output-body {
      font-size: 14px;
      line-height: 1.65;
    }
    .k-output-tools {
      display: flex;
      gap: 10px;
      margin-top: 14px;
      padding-top: 10px;
      border-top: 1px solid rgba(0,0,0,0.1);
    }
    .k-btn-card-tool {
      background: var(--card-bg);
      border: 1px solid var(--border-ink);
      border-radius: 3px;
      padding: 4px 10px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
    }
    .k-btn-card-tool:hover {
      background: var(--news-ink);
      color: #fff;
    }

    /* Commands View */
    .k-commands-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
    }
    .k-command-card {
      border: 2px solid var(--border-ink);
      padding: 14px;
      background: var(--news-paper);
      border-radius: 4px;
      box-shadow: var(--shadow-hard-sm);
      transition: all 0.15s;
    }
    .k-command-card:hover {
      background: var(--crimson);
      color: #ffffff;
      border-color: var(--crimson);
      transform: translate(-2px, -2px);
      box-shadow: 4px 4px 0px #000;
    }
    .k-command-title {
      font-family: var(--font-display);
      font-size: 16px;
      margin-bottom: 4px;
    }
    .k-command-desc {
      font-size: 11.5px;
      opacity: 0.85;
    }

    /* FOOTER */
    .newspaper-footer {
      border-top: 3px double var(--border-ink);
      padding: 30px 24px;
      text-align: center;
      font-family: var(--font-mono);
      font-size: 12px;
      background: var(--paper-tint);
      margin-top: 40px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      align-items: center;
    }

    /* RESPONSIVE DESIGN */
    @media (max-width: 1024px) {
      .front-page-grid {
        grid-template-columns: 1fr;
      }
      .cases-news-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .k-commands-grid {
        grid-template-columns: 1fr;
      }
      .masthead-main {
        grid-template-columns: 1fr;
        text-align: center;
      }
      .masthead-left-box, .masthead-right-box {
        align-items: center;
        text-align: center;
        border-left: none;
      }
    }
    @media (max-width: 640px) {
      .cases-news-grid {
        grid-template-columns: 1fr;
      }
      .headline-main {
        font-size: 34px;
      }
      .masthead-title {
        font-size: 42px;
      }
      .comic-stage-grid {
        grid-template-columns: 1fr;
      }
      .frame-surveillance, .frame-action-main, .frame-investigator {
        grid-column: 1 / 2;
      }
    }
  </style>
</head>
<body>

  <!-- HALFTONE SCREEN OVERLAY -->
  <div class="halftone-screen"></div>

  <!-- AMBIENT RAIN CANVAS SHADER -->
  <canvas id="ambient-rain-canvas"></canvas>

  <!-- AMONG US BATMAN GLOVED FINGER CUSTOM CURSOR -->
  <div id="cursor-finger-follower">
    <img src="cursor_finger.png" alt="Batman Finger Pointer">
  </div>
  <div id="cursor-ring"></div>

  <!-- TOP LIVE BREAKING WIRE TICKER -->
  <div class="top-breaking-bar">
    <div class="breaking-label">
      <span class="live-pulse"></span>
      <span>BREAKING WIRE</span>
    </div>
    <div class="ticker-marquee">
      <div class="ticker-item"><span class="red-dot">●</span> 03:15 AM: VIOLENT MUD SLAPS REPORTED ON HOMESTEAD ROOFS IN KISII &amp; HOMA BAY &bull; ELDERS WARN RESIDENTS NOT TO STEP OUTSIDE</div>
      <div class="ticker-item"><span class="red-dot">●</span> 01:20 AM: RED KBS 666 PHANTOM BUS SIGHTED PASSING ADAMS ARCADE CORRIDOR TOWARD KAREN FOREST &bull; NO ENGINE SOUND DETECTED</div>
      <div class="ticker-item"><span class="red-dot">●</span> 04:00 AM: GEOTHERMAL SULFUR VENTS IN MENENGAI CALDERA EMIT HUMAN CHANTING SOUNDS &bull; HIKER TRACKS TERMINATE AT BASALT RIM</div>
      <div class="ticker-item"><span class="red-dot">●</span> 02:45 AM: COASTAL PATROL RECOVERS SPLIT CLOVEN HOOFPRINTS ALONG MAMA NGINA CLIFFSIDE &bull; BODA RIDERS ADVISE AGAINST MIDNIGHT DRIFT</div>
      <div class="ticker-item"><span class="red-dot">●</span> 03:00 AM: ABANDONED LIMURU DORMITORY UNPOWERED BRASS BELL RINGS DURING THUNDERSTORM &bull; HIGH HEEL ACOUSTIC SIGNATURES RECORDED</div>
      <div class="ticker-item"><span class="red-dot">●</span> 02:10 AM: HIGHWAY CAMERAS LOG ANOMALOUS WHITE APPARITION AT KIKOPEY FLATS &bull; LONG-DISTANCE TRUCK BRAKE FAILURES UNDER INQUIRY</div>
      <!-- Duplicate for seamless infinite loop -->
      <div class="ticker-item"><span class="red-dot">●</span> 03:15 AM: VIOLENT MUD SLAPS REPORTED ON HOMESTEAD ROOFS IN KISII &amp; HOMA BAY &bull; ELDERS WARN RESIDENTS NOT TO STEP OUTSIDE</div>
      <div class="ticker-item"><span class="red-dot">●</span> 01:20 AM: RED KBS 666 PHANTOM BUS SIGHTED PASSING ADAMS ARCADE CORRIDOR TOWARD KAREN FOREST &bull; NO ENGINE SOUND DETECTED</div>
    </div>
  </div>

  <!-- NEWSPAPER MASTHEAD (THE NGESA CHRONICLE) -->
  <header class="newspaper-header">
    <div class="masthead-meta-top">
      <div>NAIROBI METROPOLITAN EDITION &bull; VOL. IV NO. 88</div>
      <div>CLASSIFICATION: STRICTLY OPEN-SOURCE DECLASSIFIED // MORINGA CYBERSEC LAB</div>
      <div>SECURITY CLEARANCE: LEVEL 5 // INVESTIGATOR ARCHIVE</div>
    </div>

    <div class="masthead-main">
      <div class="masthead-left-box">
        <div><strong>BUREAU:</strong> NAIROBI / LAKE BASIN / COAST</div>
        <div><strong>INVESTIGATIVE LEAD:</strong> DOMINIC NYONGESA</div>
        <div><strong>FOCUS:</strong> OCCULT FOLKLORE &amp; URBAN HORROR</div>
      </div>

      <div class="masthead-center">
        <h1 class="masthead-title">THE NGESA <span class="red">CHRONICLE</span></h1>
        <div class="masthead-sub">/// DECLASSIFIED GRAPHIC NOVEL JOURNALISM &bull; KENYA HORROR WIRE ///</div>
      </div>

      <div class="masthead-right-box">
        <div class="editor-seal">
          <img src="avatar.jpg" alt="Dominic Nyongesa" class="editor-avatar">
          <span class="editor-name">Dominic Nyongesa, Lead Investigator</span>
        </div>
        <div class="masthead-controls">
          <button class="btn-pill-cta" onclick="toggleTheme()" title="Toggle Newsprint / Midnight Noir Mode">
            <span id="theme-icon">🌓</span> <span id="theme-label">Midnight Noir</span>
          </button>
          <button class="btn-pill-cta" onclick="scrollToSection('aiprompt')">
            <span>⚡</span> AI News Desk
          </button>
        </div>
      </div>
    </div>

    <!-- SUBNAV NAVIGATION STRIP -->
    <nav class="subnav-strip">
      <a href="#front-page" class="subnav-link active">Front Page Strip</a>
      <a href="#breaking-grid" class="subnav-link">8 Declassified Cases</a>
      <a href="#aiprompt" class="subnav-link">⚡ AI Intelligence Desk</a>
      <a href="#evidence-wire" class="subnav-link">Witness Locker</a>
    </nav>
  </header>

  <!-- MAIN EDITORIAL CONTENT -->
  <main class="app-main">

    <!-- FRONT PAGE LEAD STORY & 4-FRAME COMIC STAGE -->
    <section class="front-page-grid" id="front-page">
      
      <!-- LEFT: STORY TEXT & EDITORIAL COLUMN -->
      <div class="story-column">
        <div class="story-category-stamp" id="story-stamp">
          <span>🚨 BREAKING DISPATCH</span> &bull; <span id="story-location-tag">HOMA BAY &amp; KISII COUNTIES</span>
        </div>

        <h2 class="headline-main" id="story-headline">
          THE MIDNIGHT KNOCK: INSIDE THE SECRET GUILD OF WESTERN KENYA'S NIGHT RUNNERS
        </h2>

        <div class="byline-bar">
          <div>BY <strong>DOMINIC NYONGESA</strong> &bull; NAIROBI BUREAU</div>
          <div id="story-timestamp">LOGGED 03:15 AM &bull; SPECIAL VISUAL DISPATCH</div>
        </div>

        <div class="story-lead-quote" id="story-quote">
          "Mud slaps on iron roofs, supersonic speeds through sisal fences, and the unexplainable hereditary compulsion of Lake Victoria's nocturnal runners."
        </div>

        <div class="story-body-text" id="story-body">
          <p>
            In the villages along the shores of Lake Victoria and the rolling mist of Gucha, midnight brings an unsettling silence—broken only by the sudden, violent slap of wet mud against corrugated iron roofs: <em>Twa twa twa!</em> This is the domain of the Night Runners (known locally as <em>Abanyasi</em> in Luhya, and <em>Omoirori</em> in Gusii).
          </p>
          <p>
            Eyewitness testimonies corroborated by community elders establish that these runners strip bare in the dead of night, sprint through dense thorny thickets at impossible speeds without sustaining scratches, flick glowing embers into homesteads, and terrorize neighbors without ever breaking inside. Wazee say it is an ancient hereditary bloodline compulsion passed through generations. Eeh, hii ni mwecheche!
          </p>
        </div>

        <!-- COMIC ANIMATION CONTROLLER TOOLBAR -->
        <div class="comic-controls-bar">
          <button class="btn-comic-action primary" onclick="autoPlayComicSequence()" id="btn-autoplay-comic">
            <span>🎬</span> <span id="label-autoplay">Play Animated Comic Sequence</span>
          </button>
          <button class="btn-comic-action" onclick="stepComicPanel(-1)">
            <span>◀</span> Prev Frame
          </button>
          <button class="btn-comic-action" onclick="stepComicPanel(1)">
            Next Frame <span>▶</span>
          </button>
          <button class="btn-comic-action" onclick="triggerComicBurst(event, 'MWECHECHE!')">
            <span>💥</span> Action FX
          </button>
        </div>
      </div>

      <!-- RIGHT: 4-FRAME ANIMATED GRAPHIC NOVEL STAGE -->
      <div class="comic-stage-grid" id="comic-stage">
        
        <!-- Frame 1: Eyewitness Surveillance Top Strip -->
        <div class="comic-frame frame-surveillance active-focus" id="frame-1" onclick="focusComicFrame(1)">
          <div class="cam-hud-tag">
            <span class="cam-rec-dot"></span>
            <span>SURVEILLANCE CAM 01 &bull; 03:15:42 AM &bull; NIGHT VISION</span>
          </div>
          <img src="panel_eyes.jpg" alt="Eyewitness Surveillance Eyes" id="img-frame-1">
          <div class="crt-scanlines"></div>
          <div class="comic-speech-bubble" style="bottom: 8px; left: 8px; font-size: 11px; padding: 4px 10px; max-width: 80%;">
            "Nilichungulia dirishani nikamwona... macho yake yanang'aa kama ya chui!"
          </div>
        </div>

        <!-- Frame 2: Main Dynamic Action Panel -->
        <div class="comic-frame frame-action-main" id="frame-2" onclick="focusComicFrame(2)">
          <div class="sfx-burst-badge" id="action-sfx-badge">TWA! TWA! TWA!</div>
          <img src="panel_action_ep01.jpg" alt="Case Comic Action Panel" id="img-frame-2">
          <div class="comic-speech-bubble" id="action-speech-bubble">
            Twa twa twa! K-Kile kiumbe... Kinarudi!
          </div>
        </div>

        <!-- Frame 3: Lead Investigator Dominic Nyongesa -->
        <div class="comic-frame frame-investigator" id="frame-3" onclick="focusComicFrame(3)">
          <img src="panel_investigator.jpg" alt="Dominic Nyongesa Lead Investigator" id="img-frame-3">
          <div class="comic-speech-bubble" style="top: 14px; left: -10px; transform: rotate(-3deg); font-size: 12px; max-width: 170px; background: var(--yellow-burst);">
            "Giza lina siri... Eeh, mwecheche!"
          </div>
          <div class="investigator-badge">
            <span class="role">LEAD INVESTIGATOR</span>
            <span>DOMINIC NYONGESA</span>
          </div>
        </div>

      </div>
    </section>

    <!-- =========================================================
         ALL 8 DECLASSIFIED CASES GRID
         ========================================================= -->
    <section class="news-section" id="breaking-grid">
      <div class="section-header-banner">
        <h3 class="section-title">
          <span>INVESTIGATIVE WIRE ARCHIVE</span>
          <span class="tag">8 CASES DECLASSIFIED</span>
        </h3>
        <div style="font-family:var(--font-mono);font-size:12px;color:var(--lead-gray);">
          CLICK ANY STORY TO LOAD ITS ANIMATED COMIC SPREAD
        </div>
      </div>

      <div class="cases-news-grid" id="cases-grid">
        <!-- CASE 01 -->
        <div class="case-card active-selected" data-idx="0" onclick="selectStory(0, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 01 &bull; FOLKLORE &amp; OCCULT</div>
            <img src="panel_action_ep01.jpg" alt="The Midnight Knock">
          </div>
          <div class="case-card-content">
            <div class="case-location">Homa Bay &amp; Kisii Counties</div>
            <h4 class="case-title">The Midnight Knock: Night Runners of Western Kenya</h4>
            <div class="case-tagline">Mud slaps on iron roofs, supersonic speeds, and the ancient Abanyasi guild.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 02 -->
        <div class="case-card" data-idx="1" onclick="selectStory(1, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 02 &bull; URBAN LEGENDS</div>
            <img src="panel_action_ep02.jpg" alt="The Ghost Bus of Ngong Road">
          </div>
          <div class="case-card-content">
            <div class="case-location">Ngong Road &amp; Karen Forest, Nairobi</div>
            <h4 class="case-title">The Ghost Bus of Ngong Road (KBS 666)</h4>
            <div class="case-tagline">The vintage red Kenya Bus that appears past 1:00 AM with no sound of an engine.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 03 -->
        <div class="case-card" data-idx="2" onclick="selectStory(2, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 03 &bull; HAUNTED GEOGRAPHY</div>
            <img src="panel_action_ep03.jpg" alt="Kirima kia Ngoma">
          </div>
          <div class="case-card-content">
            <div class="case-location">Menengai Caldera, Nakuru</div>
            <h4 class="case-title">Kirima kia Ngoma: The Whispers of Menengai Crater</h4>
            <div class="case-tagline">The Hill of Devils where warrior drums echo from the 500-meter volcanic basin.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 04 -->
        <div class="case-card" data-idx="3" onclick="selectStory(3, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 04 &bull; COASTAL PARANORMAL</div>
            <img src="panel_action_ep04.jpg" alt="The Goat-Footed Stranger">
          </div>
          <div class="case-card-content">
            <div class="case-location">Old Town Mombasa &amp; Mama Ngina Waterfront</div>
            <h4 class="case-title">The Goat-Footed Stranger of Mama Ngina</h4>
            <div class="case-tagline">A courteous gentleman in pristine white kanzu—whose feet are two cloven goat hooves.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 05 -->
        <div class="case-card" data-idx="5" onclick="selectStory(4, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 05 &bull; KENYAN NOSTALGIA</div>
            <img src="panel_action_ep05.jpg" alt="The Dormitory Above the Crypt">
          </div>
          <div class="case-card-content">
            <div class="case-location">Limuru, Kikuyu &amp; Meru Boarding Schools</div>
            <h4 class="case-title">The Dormitory Above the Crypt: Boarding School Hauntings</h4>
            <div class="case-tagline">Cold hands on top bunks, marching combat boots, and the unpowered brass bell.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 06 -->
        <div class="case-card" data-idx="5" onclick="selectStory(5, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 06 &bull; HIGHWAY HORROR</div>
            <img src="panel_action_ep06.jpg" alt="The Vanishing at Kikopey">
          </div>
          <div class="case-card-content">
            <div class="case-location">Nakuru-Eldoret Highway &amp; Kikopey Flats</div>
            <h4 class="case-title">The Vanishing at Kikopey (The Lady in White)</h4>
            <div class="case-tagline">The barefoot hitchhiker in white who evaporates from moving transit trucks.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 07 -->
        <div class="case-card" data-idx="6" onclick="selectStory(6, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 07 &bull; TRUE CRIME INVESTIGATION</div>
            <img src="panel_action_ep07.jpg" alt="The Starvation Woods">
          </div>
          <div class="case-card-content">
            <div class="case-location">Shakahola Forest, Chakama Ranch, Kilifi</div>
            <h4 class="case-title">The Starvation Woods of Chakama (Shakahola Files)</h4>
            <div class="case-tagline">The forensic investigation inside 800 acres of terror and apocalyptic deception.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>

        <!-- CASE 08 -->
        <div class="case-card" data-idx="7" onclick="selectStory(7, event)">
          <div class="case-card-thumb">
            <div class="case-badge-overlay">CASE 08 &bull; CRYPTID INVESTIGATION</div>
            <img src="panel_action_ep08.jpg" alt="The Brain-Eater of Kakamega">
          </div>
          <div class="case-card-content">
            <div class="case-location">Kakamega Rainforest &amp; Nandi Hills</div>
            <h4 class="case-title">The Brain-Eater of Kakamega (The Chemosit Beast)</h4>
            <div class="case-tagline">The ferocious arboreal man-beast who scalps prey from high mahogany branches.</div>
            <button class="btn-read-dispatch">
              <span>Read Comic Strip</span>
              <span>⚡</span>
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         TELERIK KENDO UI AIPROMPT (INVESTIGATIVE AI NEWS DESK)
         ========================================================= -->
    <section class="k-aiprompt-wrapper" id="aiprompt">
      <div class="k-aiprompt-header">
        <div class="k-header-title">
          <span>⚡</span>
          <span>Ngesa AI News Intelligence Terminal</span>
          <span class="k-ai-badge">STARPOD GRAPHIC RAG ENGINE</span>
        </div>
        <div class="k-header-tools">
          <button class="k-tool-btn" onclick="clearAIPrompt()">Clear</button>
          <button class="k-tool-btn" onclick="exportDossierReport()">Export Dispatch</button>
        </div>
      </div>

      <!-- Views Navigation -->
      <div class="k-views-toolbar">
        <button class="k-view-tab active" id="tab-btn-prompt" onclick="switchKendoView('prompt')">
          <span>💬</span> Interrogate Case
        </button>
        <button class="k-view-tab" id="tab-btn-outputs" onclick="switchKendoView('outputs')">
          <span>📋</span> Intelligence Outputs (<span id="output-count">1</span>)
        </button>
        <button class="k-view-tab" id="tab-btn-commands" onclick="switchKendoView('commands')">
          <span>⚡</span> Editorial Presets
        </button>
      </div>

      <!-- View 1: Prompt Input View -->
      <div class="k-view-content active" id="k-view-prompt">
        <div class="k-prompt-box">
          <textarea class="k-prompt-textarea" id="kendo-prompt-input" placeholder="Ask Dominic's AI news bureau anything: cross-examine witness testimonies, generate 03:00 AM incident timelines, or analyze folklore contradictions..."></textarea>
          <div class="k-prompt-footer">
            <div class="k-prompt-hint">Shift + Enter for newline &bull; Enter to transmit inquiry</div>
            <div class="k-prompt-actions">
              <button class="btn-pill-cta" onclick="clearPromptInput()">Clear</button>
              <button class="k-btn-generate" onclick="handleKendoSubmit()">⚡ Transmit to News Desk</button>
            </div>
          </div>
        </div>

        <div class="k-chips-label">RECOMMENDED INVESTIGATIVE QUERIES:</div>
        <div class="k-chips-group" id="kendo-chips-container">
          <!-- Dynamically populated based on active case -->
        </div>
      </div>

      <!-- View 2: Outputs View -->
      <div class="k-view-content" id="k-view-outputs">
        <div id="k-outputs-list">
          <!-- Dynamically populated with investigation cards -->
        </div>
      </div>

      <!-- View 3: Commands View (One-Click Presets) -->
      <div class="k-view-content" id="k-view-commands">
        <div class="k-commands-grid">
          <div class="k-command-card" onclick="runPresetCommand('timeline')">
            <div class="k-command-title">⏱️ 03:00 AM Chronological Timeline</div>
            <div class="k-command-desc">Reconstructs the incident step-by-step from twilight to dawn.</div>
          </div>
          <div class="k-command-card" onclick="runPresetCommand('cross_examine')">
            <div class="k-command-title">🗣️ Witness Cross-Examination Audit</div>
            <div class="k-command-desc">Evaluates deposition credibility and identifies conflicting accounts.</div>
          </div>
          <div class="k-command-card" onclick="runPresetCommand('forensic_vs_myth')">
            <div class="k-command-title">⚖️ Forensic vs Folklore Dissection</div>
            <div class="k-command-desc">Separates verifiable physical evidence from rural superstition.</div>
          </div>
          <div class="k-command-card" onclick="runPresetCommand('cultural_lexicon')">
            <div class="k-command-title">🇰🇪 Sheng &amp; Cultural Lexicon</div>
            <div class="k-command-desc">Translates vernacular terms (Abanyasi, Omoirori, Majini, Mwecheche).</div>
          </div>
          <div class="k-command-card" onclick="runPresetCommand('highway_blackspots')">
            <div class="k-command-title">📍 Highway Blackspot Telemetry</div>
            <div class="k-command-desc">Maps GPS coordinates and historical incident clusters across Kenya.</div>
          </div>
          <div class="k-command-card" onclick="runPresetCommand('executive_brief')">
            <div class="k-command-title">📑 Executive Editorial Brief</div>
            <div class="k-command-desc">One-page declassified summary for security analysts and journalists.</div>
          </div>
        </div>
      </div>
    </section>

    <!-- =========================================================
         WITNESS DEPOSITION LOCKER (COMMUNITY EVIDENCE WIRE)
         ========================================================= -->
    <section class="news-section" id="evidence-wire">
      <div class="section-header-banner">
        <h3 class="section-title">
          <span>CLASSIFIED EVIDENCE LOCKER</span>
          <span class="tag">ACTIVE WITNESS REPOSITORY</span>
        </h3>
      </div>

      <div style="background:var(--card-bg);border:2px solid var(--border-ink);padding:20px;box-shadow:var(--shadow-hard-sm);border-radius:4px;display:grid;grid-template-columns:1fr 1fr;gap:20px;">
        <div>
          <h4 style="font-family:var(--font-display);font-size:22px;margin-bottom:10px;text-transform:uppercase;">Eyewitness Depositions</h4>
          <div id="witness-quote-box" style="font-size:14px;line-height:1.6;font-style:italic;background:var(--paper-tint);padding:14px;border-left:3px solid var(--crimson);border-radius:2px;">
            "You hear footsteps circling your hut like a cheetah. You shout, but if you step outside and shine a torch in their eyes, your arm goes paralyzed." — Mzee Ochieng, Homa Bay
          </div>
        </div>
        <div>
          <h4 style="font-family:var(--font-display);font-size:22px;margin-bottom:10px;text-transform:uppercase;">Scientific &amp; Forensic Analysis</h4>
          <div id="scientific-box" style="font-size:14px;line-height:1.6;background:var(--paper-tint);padding:14px;border-left:3px solid var(--border-ink);border-radius:2px;">
            A combination of hereditary psychological manic-dissociative states, generational superstition, and village psychological warfare.
          </div>
        </div>
      </div>
    </section>

  </main>

  <!-- NEWSPAPER FOOTER -->
  <footer class="newspaper-footer">
    <div><strong>THE NGESA CHRONICLE</strong> &bull; DECLASSIFIED KENYAN OCCULT &amp; TRUE CRIME GRAPHIC NOVEL NEWSPAPER</div>
    <div>HOSTED &amp; INVESTIGATED BY <strong>DOMINIC NYONGESA</strong> &bull; MORINGA SCHOOL CYBER SECURITY LAB</div>
    <div style="font-size:11px;color:var(--lead-gray);">EST. 2026 &bull; IN-SCOPE LAB NETWORK: 10.20.0.0/24 &bull; ALL RIGHTS RESERVED</div>
  </footer>

  <!-- =========================================================
       JAVASCRIPT LOGIC & COMIC ENGINE
       ========================================================= -->
  <script>
    const STORIES = [
      {
        id: "case01",
        num: 1,
        title: "The Midnight Knock: Night Runners of Western Kenya",
        category: "FOLKLORE & OCCULT",
        location: "Homa Bay & Kisii Counties",
        tagline: "Mud slaps on iron roofs, supersonic speeds, and the ancient Abanyasi guild.",
        sfx: "TWA! TWA! TWA!",
        speech: "Twa twa twa! K-Kile kiumbe... Kinarudi!",
        investigatorQuote: "Giza lina siri... Eeh, mwecheche!",
        actionImg: "panel_action_ep01.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "Mud slaps on iron roofs, supersonic speeds through sisal fences, and the unexplainable hereditary compulsion of Lake Victoria's nocturnal runners.",
        body: `In the villages along the shores of Lake Victoria and the rolling mist of Gucha, midnight brings an unsettling silence—broken only by the sudden, violent slap of wet mud against corrugated iron roofs: Twa twa twa! This is the domain of the Night Runners (known locally as Abanyasi in Luhya, and Omoirori in Gusii).<br><br>Eyewitness testimonies corroborated by community elders establish that these runners strip bare in the dead of night, sprint through dense thorny thickets at impossible speeds without sustaining scratches, flick glowing embers into homesteads, and terrorize neighbors without ever breaking inside. Wazee say it is an ancient hereditary bloodline compulsion passed through generations. Eeh, hii ni mwecheche!`,
        witness: "Mzee Ochieng: 'You hear footsteps circling your hut like a cheetah. You shout, but if you step outside and shine a torch in their eyes, your arm goes paralyzed.'",
        scientific: "A combination of hereditary psychological manic-dissociative states, generational superstition, and village psychological warfare.",
        chips: [
          "⚡ Night Runner Compulsion Analysis",
          "🗣️ Elder Witness Deposition",
          "⚖️ Scientific vs Parapsychological",
          "🔍 Sisal Fence Scratch Immunity"
        ]
      },
      {
        id: "case02",
        num: 2,
        title: "The Ghost Bus of Ngong Road (KBS 666)",
        category: "URBAN LEGENDS",
        location: "Ngong Road & Karen Forest, Nairobi",
        tagline: "The vintage red Kenya Bus that appears past 1:00 AM with no sound of an engine.",
        sfx: "WHOOSH!",
        speech: "Basi halina dereva... Na watu waka-board?!",
        investigatorQuote: "Bana, hii basi haina mwisho!",
        actionImg: "panel_action_ep02.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "A vintage red Kenya Bus Service matatu with a glowing yellow destination board reading 'TERMINAL' appears on rainy nights.",
        body: `Maze skia hii story bana... Ngong Road saa tisa za usiku katikati ya msitu mnene wa Karen. Basi nyekundu ya zamani ya KBS namba 666 inatokea kwenye kona bila taa wala sauti ya injini! Dereva ametazama mbele haongei, makanga amesimama mlangoni hana uso, lakini ndani abiria wamejaa wametulia kimya kabisa.<br><br>Na watu waka-board hiyo basi! Wanaingia lakini hakuna anayeshuka Nairobi mzima! Asubuhi ikifika, unakuta gari imeyeyuka kwenye ukungu wa msitu. Bana, hii ni mwecheche!`,
        witness: "Taxi Operator Kamau: 'In 2014, I followed an old KBS bus turning into the forest sanctuary at 2:00 AM. There was no road there—just dense eucalyptus. When my headlights hit it, the vehicle dissolved like smoke.'",
        scientific: "Hypnagogic hallucination induced by late-night fatigue and trauma associated with historical fatal crashes along the dark Ngong Road corridor.",
        chips: [
          "🚌 Ngong Road Ghost Bus KBS 666",
          "⏱️ Karen Forest Crash Archive",
          "👥 Phantom Commuter Anomaly",
          "⚖️ Driver Fatigue Hypothesis"
        ]
      },
      {
        id: "case03",
        num: 3,
        title: "Kirima kia Ngoma: The Whispers of Menengai Crater",
        category: "HAUNTED GEOGRAPHY",
        location: "Menengai Caldera, Nakuru",
        tagline: "The Hill of Devils where warrior drums echo from the 500-meter volcanic basin.",
        sfx: "BOOM! BOOM!",
        speech: "Sauti za ngoma... Kirima kia Ngoma!",
        investigatorQuote: "Shimo lina sauti za 1854!",
        actionImg: "panel_action_ep03.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "Locals swear you can hear the chanting of 1854 Maasai warriors echoing underneath the caldera mist.",
        body: `Imagine ukienda Menengai Crater Nakuru... mahali panaitwa Kirima kia Ngoma, kilima cha mashetani! Watu wakitembea jioni wanaskia ngoma zikilia chini ya ardhi na sauti zikiita majina yao. Mwaka wa 1854 maelfu ya mashujaa wa Maasai walisukumwa kwenye kreta hii wakati wa vita.<br><br>Hadi leo watalii na wachungaji wanapotea bila viatu, na watu wakapiga picha... picha inatoka moshi na vivuli vya kutisha! Watu wa eneo hilo wanajua jioni ikifika, hutakiwi kutazama ndani ya shimo hilo. Eeh, hii ni mwecheche!`,
        witness: "Forest Ranger Kiprop: 'We found his backpack and boots neatly stacked on a basalt rock by the rim. No tracks leading down. The crater swallowed him in broad daylight.'",
        scientific: "Geothermal hydrogen sulfide vents causing sudden hypoxic hallucinations and disorientation in the dense caldera basin.",
        chips: [
          "🌋 Menengai 1854 Massacre",
          "🚜 Phantom Farm Machinery Records",
          "🥾 Disappearance of Hiker Kiprop",
          "💨 Sulfur Gas Hallucination Audit"
        ]
      },
      {
        id: "case04",
        num: 4,
        title: "The Goat-Footed Stranger of Mama Ngina",
        category: "COASTAL PARANORMAL",
        location: "Old Town Mombasa & Mama Ngina Waterfront",
        tagline: "A courteous gentleman in pristine white kanzu—whose feet are two cloven goat hooves.",
        sfx: "CLACK! CLACK!",
        speech: "Kwato za mbuzi Mama Ngina... Eeh, mwecheche!",
        investigatorQuote: "Usiongee na wageni Pwani usiku!",
        actionImg: "panel_action_ep04.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "Underneath the hem of his tailored kanzu, the moonlight reveals two split, hairy goat hooves clicking against asphalt.",
        body: `Mombasa raha, sivyo? Lakini tembea Mama Ngina Waterfront saa nane za usiku uone mambo! Upepo wa bahari unavuma kwa baridi, ghafla unatokeza mwanamume mtanashati mwenye sauti tamu, amevaa kanzu safi ya kizungu na kofia ya heshima. Anakusalimia kwa lugha ya staha.<br><br>Lakini ukitazama chini kwa mchanga... miguu yake si ya binadamu! Ni kwato mbili za mbuzi zilizogawanyika! Na watu bado wakamsalimia kabla hawajagundua! Ukipiga kelele anayeyuka na kubaki harufu ya udi na ubani. Maze, hii ni mwecheche!`,
        witness: "Boda rider Ali: 'A customer flagged me down near Fort Jesus. She had an unearthly perfume. When she lifted her dress to get onto the bike, my headlights caught her feet: two hairy goat hooves clicking against asphalt. I dropped the bike and ran.'",
        scientific: "Centuries-old folklore blending Afro-Arabian pre-Islamic jinn mythology with maritime trader urban anxieties.",
        chips: [
          "👣 Mama Ngina Cloven Hooves",
          "🕌 Old Town Jinn Traditions",
          "🌊 Seafront Spirit Manifestation",
          "👁️ Polygraph of Rider Ali"
        ]
      },
      {
        id: "case05",
        num: 5,
        title: "The Dormitory Above the Crypt: Boarding School Hauntings",
        category: "KENYAN NOSTALGIA",
        location: "Limuru, Kikuyu & Meru Boarding Schools",
        tagline: "Cold hands on top bunks, marching combat boots, and the unpowered brass bell.",
        sfx: "DING! DONG!",
        speech: "High heels corridor... Clack! Clack! Clack!",
        investigatorQuote: "Kila mwanafunzi anajua saa 3:00 AM!",
        actionImg: "panel_action_ep05.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "Colonial stone dormitories built atop old settlers' burial grounds where heavy boots march down locked corridors.",
        body: `Kila Mkenya aliyesoma boarding anajua hii story ya kutisha! Bweni la zamani la shule za Limuru na Meru lililojengwa juu ya makaburi ya enzi za ukoloni. Saa tisa za usiku wakati kila mtu amelala, kengele ya chuma inaanza kulia yenyewe! Ding! Dong!<br><br>Kisha unaskia viatu virefu vya high heels vikitembea polepole kwa corridor tupu ya saruji: Clack! Clack! Clack! Milango inafunguka yenyewe, blanketi zinavutwa kutoka vitandani, na wasichana wakatoroka kupitia madirishani! Asubuhi wakichunguza, hakuna mtu yeyote aliyekuwemo! Eeh, hii ni mwecheche!`,
        witness: "Alumnus Mercy: 'We were locked in House 4. At 3:15 AM, heavy combat boots started marching down the corridor. In the morning, wet boot prints led straight into a locked wall.'",
        scientific: "High teenage academic stress, sleep deprivation during exam cycles, and psychological contagion in isolated communal living.",
        chips: [
          "🔔 Unpowered Brass Bell Mystery",
          "👠 High Heels Corridor Acoustic Log",
          "🏫 Colonial Crypt Archival Survey",
          "🧠 Mass Sleep Paralysis Factors"
        ]
      },
      {
        id: "case06",
        num: 6,
        title: "The Vanishing at Kikopey (The Lady in White)",
        category: "HIGHWAY HORROR",
        location: "Nakuru-Eldoret Highway & Kikopey Flats",
        tagline: "The barefoot hitchhiker in white who evaporates from moving transit trucks.",
        sfx: "SKRRRT!",
        speech: "Mwanamke wa Kikopey... Breki zikakata!",
        investigatorQuote: "Kona ya Salgaa ina macho!",
        actionImg: "panel_action_ep06.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "Long-haul truckers describe picking up a stranded bride on the foggy shoulder—only for her seat to turn ice cold at 80 km/h.",
        body: `Highway ya Nakuru kuelekea Eldoret pale Kikopey Flats... barabara iliyonyooka lakini giza ni totoro. Madereva wa malori ya masafa marefu wanasimulia kisa cha mwanamke aliyevaa gauni jeupe la harusi, amesimama kando ya lami akiinua mkono kuomba lifti kwenye baridi kali.<br><br>Dereva mwenye huruma akasimamisha gari na kumkaribisha kwenye kiti cha mbele. Baada ya kilomita tano dereva akimtazama, kiti kiko wazi kabisa, lakini harufu ya maua ya makaburini imetanda garini na breki zinakata ghafla! Wengi wamepoteza maisha kwenye kona hiyo. Bana, hii ni mwecheche!`,
        witness: "Transit Driver Hassan: 'I felt the front door slam. I asked her where she was going. No answer. When I glanced left at the Salgaa bend, she was gone, but her seatbelt was still locked across the empty chair.'",
        scientific: "Severe driver highway hypnosis, circadian rhythm crashes, and psychological manifestations of survivor guilt along high-fatality roads.",
        chips: [
          "🚗 Salgaa-Kikopey Blackspot Map",
          "👰 Lady in White Trucker Testimony",
          "⛓️ Locked Seatbelt Phenomenon",
          "📉 Highway Hypnosis Telemetry"
        ]
      },
      {
        id: "case07",
        num: 7,
        title: "The Starvation Woods of Chakama (Shakahola Files)",
        category: "TRUE CRIME INVESTIGATION",
        location: "Shakahola Forest, Chakama Ranch, Kilifi",
        tagline: "The forensic investigation inside 800 acres of terror and apocalyptic deception.",
        sfx: "EERIE SILENCE...",
        speech: "Ekari mia nane za Shakahola... Giza lina siri!",
        investigatorQuote: "Ushahidi wa mauti chini ya miti.",
        actionImg: "panel_action_ep07.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "How forensic pathologists and local trackers excavated over 400 shallow mass graves beneath the dry commiphora thorns.",
        body: `Hii si hadithi ya kubuni, hii ni ukweli mzito na mchungu wa msitu wa Chakama kule Shakahola. Ekari mia nane za msitu wa miiba katika kaunti ya Kilifi, mahali ambapo mamia ya waumini walidanganywa kufunga chakula na maji hadi kufa ili wakutane na muumba wao kabla ya mwisho wa dunia.<br><br>Wachunguzi walipoingia ndani ya msitu huo, walikuta makaburi ya halaiki yaliyofukiwa kwa siri. Hata baada ya miezi kadhaa, ukimya wa msitu huo unatia hofu moyoni. Ni ushahidi wa jinsi imani potovu inavyoweza kugeuka kuwa mauti ya kutisha. Giza hapa lina siri kubwa!`,
        witness: "Human Rights Investigator Hussein: 'The silence of that forest was heavy. Under every commiphora tree, the ground had been freshly turned. It wasn't folklore; it was human evil disguised as scripture.'",
        scientific: "Systematic charismatic authority exploitation, cognitive isolation, and induced communal delirium.",
        chips: [
          "🩸 Shakahola 800-Acre Cult Timeline",
          "⚰️ Exhumation Forensic Protocols",
          "🧠 Coercive Mind Control Profiling",
          "⚖️ State Prosecutorial Evidence"
        ]
      },
      {
        id: "case08",
        num: 8,
        title: "The Brain-Eater of Kakamega (The Chemosit Beast)",
        category: "CRYPTID INVESTIGATION",
        location: "Kakamega Rainforest & Nandi Hills",
        tagline: "The ferocious arboreal man-beast who scalps prey from high mahogany branches.",
        sfx: "ROAAR!",
        speech: "Chemosit wa Kakamega... Anayekula ubongo tu!",
        investigatorQuote: "Akilia juu ya matawi, kimbia!",
        actionImg: "panel_action_ep08.jpg",
        surveillanceImg: "panel_eyes.jpg",
        leadQuote: "Colonial naturalists and Nandi trackers documented a giant bipedal carnivore with a siren-like whistle that scalped solitary gatherers.",
        body: `Msitu mkubwa wa Kakamega na vilele vya vilima vya Nandi... wazee wa kabila la Nandi na Luhya wanamfahamu kiumbe anayeitwa Chemosit au Nandi Bear! Wanasema ni mnyama mkubwa nusu simba nusu mtu, mwenye manyoya mekundu, anayetembea kwa miguu miwili na kutoa kicheko kama binadamu gizani!<br><br>Hakai chini bali anajificha juu ya matawi ya miti mirefu akingoja mtu apite peke yake, kisha anaruka na kumpiga kichwani ili ale ubongo tu na kuacha mwili mzima! Watafiti wa Kizungu walijaribu kumwinda miaka ya 1920 lakini wakaishia kukimbia! Maze, unadhani ni hekaya za watoto? Eeh, hii ni mwecheche!`,
        witness: "Forest elder Wafula: 'It walks on two legs when it stalks, but runs on four when it charges. When you hear the whistle from the high mahogany branches, you don't look up—you drop your axe and run.'",
        scientific: "Folkloric memory of prehistoric giant baboons (Theropithecus oswaldi) or aberrant giant hyenas surviving in isolated montane pockets.",
        chips: [
          "🐻 Chemosit / Nandi Bear Taxonomy",
          "🌲 Kakamega Canopy Hunting Routes",
          "📜 Colonial Officer Hobley Report (1922)",
          "🦴 Prehistoric Megafauna Fossil Match"
        ]
      }
    ];

    let currentStoryIdx = 0;
    let currentComicFrame = 1;
    let autoPlayInterval = null;

    // RENDER ACTIVE STORY ONTO FRONT PAGE COMIC
    function renderStory(idx) {
      currentStoryIdx = idx;
      const s = STORIES[idx];

      document.getElementById('story-stamp').innerText = `🚨 BREAKING DISPATCH • ${s.category}`;
      document.getElementById('story-location-tag').innerText = s.location.toUpperCase();
      document.getElementById('story-headline').innerText = s.title.toUpperCase();
      document.getElementById('story-quote').innerText = `"${s.leadQuote}"`;
      document.getElementById('story-body').innerHTML = s.body;

      // Frames art
      document.getElementById('img-frame-2').src = s.actionImg;
      document.getElementById('action-sfx-badge').innerText = s.sfx;
      document.getElementById('action-speech-bubble').innerText = s.speech;

      // Evidence locker
      document.getElementById('witness-quote-box').innerText = s.witness;
      document.getElementById('scientific-box').innerText = s.scientific;

      // Update Kendo Prompt chips
      updateKendoChips(s);

      // Highlight in grid
      document.querySelectorAll('.case-card').forEach((card, i) => {
        card.classList.toggle('active-selected', i === idx);
      });
    }

    // SELECT AND ACTIVATE CASE STORY
    function selectStory(idx, e) {
      renderStory(idx);
      scrollToSection('front-page');
      if (e) triggerComicBurst(e, STORIES[idx].sfx);
    }

    // UPDATE ALL 8 STORIES IN GRID
    function renderCasesGrid() {
      document.querySelectorAll('.case-card').forEach((card, i) => {
        card.classList.toggle('active-selected', i === currentStoryIdx);
      });
    }

    // INTERACTIVE COMIC FRAME FOCUS & ANIMATION
    function focusComicFrame(frameNum) {
      currentComicFrame = frameNum;
      document.querySelectorAll('.comic-frame').forEach((f, idx) => {
        f.classList.toggle('active-focus', idx + 1 === frameNum);
      });
    }

    function stepComicPanel(dir) {
      currentComicFrame += dir;
      if (currentComicFrame > 3) currentComicFrame = 1;
      if (currentComicFrame < 1) currentComicFrame = 3;
      focusComicFrame(currentComicFrame);
    }

    function autoPlayComicSequence() {
      const btn = document.getElementById('btn-autoplay-comic');
      const label = document.getElementById('label-autoplay');

      if (autoPlayInterval) {
        clearInterval(autoPlayInterval);
        autoPlayInterval = null;
        label.innerText = "Play Animated Comic Sequence";
        btn.classList.remove('primary');
      } else {
        label.innerText = "⏹ Stop Comic Sequence";
        btn.classList.add('primary');
        autoPlayInterval = setInterval(() => {
          stepComicPanel(1);
        }, 2200);
      }
    }

    // COMIC SOUND EFFECT POPUP GENERATOR
    function triggerComicBurst(e, text = "TWA!") {
      const burst = document.createElement('div');
      burst.className = 'comic-pop-sfx';
      burst.innerText = text;
      
      const x = e ? (e.clientX || window.innerWidth / 2) : window.innerWidth / 2;
      const y = e ? (e.clientY || window.innerHeight / 2) : window.innerHeight / 2;

      burst.style.left = `${x}px`;
      burst.style.top = `${y}px`;

      document.body.appendChild(burst);
      setTimeout(() => burst.remove(), 950);
    }

    // TELERIK KENDO UI AIPROMPT FUNCTIONS
    function switchKendoView(viewName) {
      document.querySelectorAll('.k-view-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.k-view-content').forEach(c => c.classList.remove('active'));

      const tab = document.getElementById(`tab-btn-${viewName}`);
      const view = document.getElementById(`k-view-${viewName}`);
      if (tab) tab.classList.add('active');
      if (view) view.classList.add('active');
    }

    function updateKendoChips(story) {
      const container = document.getElementById('kendo-chips-container');
      container.innerHTML = '';
      (story.chips || []).forEach(chipText => {
        const chip = document.createElement('button');
        chip.className = 'k-chip';
        chip.innerText = chipText;
        chip.onclick = () => {
          document.getElementById('kendo-prompt-input').value = chipText;
          handleKendoSubmit();
        };
        container.appendChild(chip);
      });
    }

    let outputIdCounter = 1;
    function handleKendoSubmit() {
      const input = document.getElementById('kendo-prompt-input');
      const q = input.value.trim();
      if (!q) return;

      const story = STORIES[currentStoryIdx];
      const newCard = document.createElement('div');
      newCard.className = 'k-output-card';
      newCard.innerHTML = `
        <div class="k-output-header">
          <span>CLASSIFIED INTEL REPORT #0${outputIdCounter++} &bull; ${story.title.toUpperCase()}</span>
          <span>CONFIDENCE: 99.4% &bull; CORROBORATED</span>
        </div>
        <div class="k-output-body">
          <strong>INQUIRY:</strong> "${q}"<br><br>
          <strong>INVESTIGATIVE VERDICT:</strong> Our intelligence analysis of <em>${story.location}</em> confirms anomalous pattern clustering around 03:00 AM. Verifiable eyewitness testimonies corroborate the phenomenon while dismissing generic burglary hypotheses. Recommended action: Maintain field surveillance and archive graphic depositions.
        </div>
        <div class="k-output-tools">
          <button class="k-btn-card-tool" onclick="copyCard(this)">📋 Copy Report</button>
          <button class="k-btn-card-tool" onclick="exportDossierReport()">📑 Export Dossier</button>
        </div>
      `;

      const list = document.getElementById('k-outputs-list');
      list.prepend(newCard);
      document.getElementById('output-count').innerText = list.children.length;

      input.value = '';
      switchKendoView('outputs');
      triggerComicBurst(null, "ANALYZED!");
    }

    function runPresetCommand(type) {
      const story = STORIES[currentStoryIdx];
      let query = "";
      if (type === 'timeline') query = `Reconstruct chronological 03:00 AM timeline for ${story.title}`;
      else if (type === 'cross_examine') query = `Cross-examine witness testimonies for ${story.title}`;
      else if (type === 'forensic_vs_myth') query = `Forensic vs folklore breakdown for ${story.title}`;
      else if (type === 'cultural_lexicon') query = `Explain cultural Sheng and Swahili terminology for ${story.title}`;
      else if (type === 'highway_blackspots') query = `Map GPS blackspots and risk metrics for ${story.location}`;
      else query = `Executive editorial brief for Case 0${story.num}`;

      document.getElementById('kendo-prompt-input').value = query;
      handleKendoSubmit();
    }

    function clearAIPrompt() {
      document.getElementById('k-outputs-list').innerHTML = '';
      document.getElementById('output-count').innerText = '0';
    }

    function clearPromptInput() {
      document.getElementById('kendo-prompt-input').value = '';
    }

    function copyCard(btn) {
      const text = btn.closest('.k-output-card').querySelector('.k-output-body').innerText;
      navigator.clipboard.writeText(text);
      btn.innerText = "✓ Copied";
      setTimeout(() => btn.innerText = "📋 Copy Report", 1500);
    }

    function exportDossierReport() {
      const s = STORIES[currentStoryIdx];
      const data = `THE NGESA CHRONICLE // DECLASSIFIED GRAPHIC NOVEL INTELLIGENCE
Case: 0${s.num} - ${s.title}
Location: ${s.location}
Category: ${s.category}
Lead Byline: Dominic Nyongesa
Deposition: ${s.witness}
Scientific Evaluation: ${s.scientific}
Generated via Ngesa Starpod Intelligence Engine.`;
      navigator.clipboard.writeText(data);
      alert("✓ Complete comic dossier exported to clipboard!");
    }

    // THEME SWITCHER
    function toggleTheme() {
      document.body.classList.toggle('theme-midnight');
      const isMidnight = document.body.classList.contains('theme-midnight');
      document.getElementById('theme-icon').innerText = isMidnight ? '☀️' : '🌓';
      document.getElementById('theme-label').innerText = isMidnight ? 'Newsprint Mode' : 'Midnight Noir';
    }

    function scrollToSection(id) {
      const el = document.getElementById(id);
      if (el) el.scrollIntoView({ behavior: 'smooth' });
    }

    // AMONG US BATMAN FINGER CUSTOM CURSOR & DYNAMICS
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

      const hoverTargets = 'a, button, .case-card, input, textarea, .k-chip, .k-command-card, .comic-frame';
      document.querySelectorAll(hoverTargets).forEach(el => {
        el.addEventListener('mouseenter', () => document.body.classList.add('cursor-hover'));
        el.addEventListener('mouseleave', () => document.body.classList.remove('cursor-hover'));
      });
    }

    // AMBIENT NOIR RAIN SHADER (CANVAS)
    function initRainShader() {
      const canvas = document.getElementById('ambient-rain-canvas');
      if (!canvas) return;
      const ctx = canvas.getContext('2d');
      let w = canvas.width = window.innerWidth;
      let h = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        w = canvas.width = window.innerWidth;
        h = canvas.height = window.innerHeight;
      });

      const drops = [];
      const numDrops = 60;
      for (let i = 0; i < numDrops; i++) {
        drops.push({
          x: Math.random() * w,
          y: Math.random() * h,
          l: Math.random() * 18 + 8,
          s: Math.random() * 8 + 4
        });
      }

      function drawRain() {
        ctx.clearRect(0, 0, w, h);
        ctx.strokeStyle = document.body.classList.contains('theme-midnight') ? 'rgba(255, 42, 75, 0.25)' : 'rgba(13, 15, 18, 0.15)';
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        for (let i = 0; i < numDrops; i++) {
          const d = drops[i];
          ctx.moveTo(d.x, d.y);
          ctx.lineTo(d.x - 2, d.y + d.l);
          d.y += d.s;
          d.x -= 0.8;
          if (d.y > h) {
            d.y = -20;
            d.x = Math.random() * w;
          }
        }
        ctx.stroke();
        requestAnimationFrame(drawRain);
      }
      drawRain();
    }

    // INITIALIZATION
    function initApp() {
      renderStory(0);
      renderCasesGrid();
      initCustomCursor();
      initRainShader();

      // Click on comic stage to trigger onomatopoeia sound burst
      const stage = document.getElementById('comic-stage');
      if (stage) {
        stage.addEventListener('click', (e) => {
          triggerComicBurst(e, STORIES[currentStoryIdx].sfx);
        });
      }
    }

    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initApp);
    } else {
      initApp();
    }
  </script>
</body>
</html>
'''
    with open('/home/yourusername/Projects/darknet-kenya/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully built index.html for Graphic Novel News Platform!")

if __name__ == '__main__':
    generate()
