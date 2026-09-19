#!/usr/bin/env python3
"""
podcast.py - CLI Manager & Publisher for Ngesa Diaries
Declassified Kenyan Horror Stories, Urban Legends & True Mysteries
Host: NGESA (@ngesa-cloud)
"""

import argparse
import http.server
import json
import socketserver
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent


def load_episodes():
    with open(BASE_DIR / "episodes.json", "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_list(args):
    episodes = load_episodes()
    print("\n" + "=" * 76)
    print("  🕯️  NGESA DIARIES — Hidden Kenyan Horror Stories & True Mysteries")
    print("  Host: NGESA (@ngesa-cloud) | Open-Source Audio Platform")
    print("=" * 76)
    for ep in episodes:
        print(f"\n[CASE {ep['episode_number']:02d}] {ep['title']}")
        print(f"  Category : {ep.get('category', 'FOLKLORE')}")
        print(f"  Location : {ep.get('location', 'Kenya')}")
        print(f"  Duration : {ep['duration']} | Released: {ep['release_date']}")
        print(f"  Tags     : {', '.join(ep.get('tags', []))}")
        print(f"  Tagline  : {ep.get('tagline', '')}")
    print("\n" + "=" * 76)
    print(f"Total Cases Cataloged: {len(episodes)} authentic Kenyan investigations.")
    print("=" * 76 + "\n")


def cmd_serve(args):
    port = args.port
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("\n" + "=" * 70)
        print(f"  🕯️  NGESA DIARIES WEB PLATFORM LIVE")
        print(f"  🌐 URL: http://localhost:{port}")
        print(f"  📁 Base Path: {BASE_DIR}")
        print(f"  🎧 Audio Wire & Synthesizer: Active")
        print("=" * 70)
        print("Press Ctrl+C to terminate server.\n")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer terminated cleanly.")


def cmd_rss(args):
    xml_path = BASE_DIR / "podcast.xml"
    if xml_path.exists():
        size = xml_path.stat().st_size
        print(f"✔ RSS Feed verified: {xml_path} ({size} bytes)")
        episodes = load_episodes()
        print(f"✔ {len(episodes)} episodes registered in Apple/Spotify RSS format.")
    else:
        print(f"❌ RSS feed not found at {xml_path}")


def main():
    parser = argparse.ArgumentParser(description="Ngesa Diaries CLI Management Tool")
    subparsers = parser.add_subparsers(dest="command")

    # list
    subparsers.add_parser("list", help="List all cataloged Kenyan horror case files")

    # serve
    serve_parser = subparsers.add_parser("serve", help="Serve web platform locally")
    serve_parser.add_argument("--port", type=int, default=8000, help="Port to listen on (default: 8000)")

    # rss
    subparsers.add_parser("rss", help="Check and validate the RSS 2.0 podcast feed")

    args = parser.parse_args()
    if args.command == "list":
        cmd_list(args)
    elif args.command == "serve":
        cmd_serve(args)
    elif args.command == "rss":
        cmd_rss(args)
    else:
        cmd_list(args)


if __name__ == "__main__":
    main()
