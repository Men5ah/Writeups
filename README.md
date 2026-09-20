# Writeups

A collection of my security writeups, CTF solutions, and technical notes — written in [Obsidian](https://obsidian.md) and published as a static site.

**🔗 Live site: [men5ah.github.io/Writeups](https://men5ah.github.io/Writeups/)**

## About this collection

This repository holds my notes as I work through CTF challenges, security exercises, and other technical problems. The goal isn't just to record a solution, but to document the *process* — what I tried, what didn't work, and how I eventually got to an answer. Dead ends are often as instructive as the fix itself, so I try to preserve that reasoning rather than editing it down to a clean final walkthrough after the fact.

Writing things up this way serves two purposes: it forces me to actually understand a problem well enough to explain it, and it gives me something to refer back to later when a similar pattern shows up in a different challenge.

## Philosophy

A few principles guide how I document things here:

- **Process over polish.** A writeup should show how a problem was actually solved, including the wrong turns, not just a clean sequence of correct steps.
- **Write for future-me.** Notes are detailed enough that I can return to a topic months later and pick the reasoning back up quickly.
- **Publish deliberately.** Not everything in my notes vault is meant to be public. Publishing here is opt-in, note by note — see below.

## How this is built

Notes are written in Obsidian and synced directly into this repository (via a symlinked vault folder), then built into a static site using [Quartz](https://quartz.jzhao.xyz/), a static site generator built for Obsidian-flavored markdown. The site is automatically built and deployed to GitHub Pages via GitHub Actions on every push.

Because publishing is opt-in per note (via frontmatter), this repository contains more raw material than what's live on the site — including templates and in-progress notes not yet ready to share.

## Navigating this repo

- **`content/`** — the actual notes, organized by topic/category (e.g. `CTFs/`, `Forage/`)
- **`quartz.config.yaml`** — site configuration and enabled plugins
- **`.github/workflows/`** — CI/CD: build and deployment automation

This repo is a fork/clone of [Quartz](https://github.com/jackyzha0/quartz) by jackyzha0, used here as the site generator — the framework code is theirs; the content in `content/` is mine.

## Note

If you're here from my resume or LinkedIn: this project also involved setting up and debugging the full build/deploy pipeline (CI/CD, environment configuration, cross-platform tooling issues). Happy to talk through that process if useful.
