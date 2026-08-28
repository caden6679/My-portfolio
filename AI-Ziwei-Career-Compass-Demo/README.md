# AI Ziwei Career Compass

> An evidence-grounded Android research prototype for personalized self-understanding and career exploration.

## Overview

**AI Ziwei Career Compass** is a research prototype that explores how multiple perspectives can be combined to support self-understanding and future career exploration without treating any single source as absolute truth.

The project brings together three complementary perspectives:

1. **Psychological self-report** — an IPIP Big Five questionnaire provides a structured baseline of how a person describes themselves.
2. **Observable smartphone behavior** — locally collected app-usage, activity-recognition, and screen-state data are transformed into daily views, trends, event logs, and candidate behavior patterns.
3. **Zi Wei Dou Shu as a cultural self-reflection framework** — structured chart facts and sourced interpretation rules provide an additional perspective, while the app explicitly avoids presenting divination as scientifically verified fact.

An AI layer then helps users explore these perspectives while keeping **observations, interpretations, uncertainty, and source evidence clearly separated**.

---

## Why I am building this

Career exploration is often based on one-time questionnaires or generic recommendations. I wanted to investigate a different question:

> **What if a career-support system could help people compare how they describe themselves, how they actually behave over time, and how a culturally familiar self-reflection framework describes them — while clearly showing where the evidence comes from?**

The long-term goal is not to predict a person's future. It is to create a tool that helps users notice patterns, ask better questions about themselves, and make more informed career decisions.

---

## Current Prototype

The project is already a working Android research prototype rather than only a concept.

### Behavioral data layer

- Local collection of Android app-usage events
- Activity Recognition events such as still, walking, running, bicycle, and vehicle
- Screen on / screen off / user-present events
- Daily behavior timeline and reconstructed app sessions
- Life Journal / episode-level event logs
- 7-day and 30-day trend views
- Local process-pattern mining for recurring behavior paths
- CSV export for research analysis

### Psychological questionnaire layer

- IPIP Big Five questionnaire
- 50 scored items plus supplementary behavior-comparison questions
- Reverse scoring and five trait scores
- Locked baseline after completion
- Weekly rotating probes that compare self-report with observable behavior
- Results restricted to **consistent / different / insufficient data**, rather than producing a single "true personality" score

### Zi Wei Dou Shu layer

- Structured birth-profile and chart-fact engine
- Twelve palaces, major and supporting stars, Five Element Bureau, transformations, major-fortune and annual layers
- Rule-based interpretation with traceable sources and explicit limitations
- Golden-case tests against reference charts
- No unsupported prediction of health, crime, wealth, or guaranteed future events

### AI layer

- Behavior AI for questions grounded in observable phone data
- Ziwei AI for explanations grounded in the user's calculated chart
- Combined comparison across different perspectives
- AI answers structured around evidence rather than free-form unsupported claims
- Model output can fall back to deterministic local logic when needed

---

## Evidence-Grounded Design

A major design goal is to avoid collapsing different kinds of information into one score.

```text
Self-report (IPIP) ─────────────┐
                               │
Observable behavior ───────────┼──> Evidence bundles ──> AI-assisted dialogue
                               │
Zi Wei perspective ────────────┘
```

The system keeps these categories separate:

- **Fact / observation** — what the device or questionnaire actually recorded
- **Interpretation** — what a rule or model suggests the observation may mean
- **Source / evidence ID** — where the claim came from
- **Limitation / uncertainty** — what the system cannot conclude

For example, frequent use of a communication app may be observable, but it does **not** automatically prove that someone is socially outgoing. The app is designed to preserve that distinction.

---

## Privacy & Responsible AI

The current prototype follows a local-first research approach.

- Behavioral data is stored locally on the Android device.
- Users can export their own research data.
- The prototype includes controls for deleting locally collected data.
- Smartphone signals are not treated as proof of intent, identity, mental state, or complete offline behavior.
- Zi Wei Dou Shu is presented as a cultural/self-reflection perspective rather than verified scientific prediction.
- AI-generated claims are expected to remain traceable to available evidence and disclose uncertainty.

This is currently a **research prototype**, not a clinical, psychological-diagnostic, financial, or medical tool.

---

## Technology

### Mobile

- Kotlin
- Android
- Jetpack Compose
- Room Database
- Android Usage Stats / Activity Recognition / foreground services

### AI & Data

- Gemini API / generative AI integration
- ChatGPT / Codex and Claude-assisted development workflows
- Python
- Data analysis and process-mining experiments
- Evidence-grounded AI response design

### Engineering

- Git / GitHub
- Issue- and PR-based development workflow
- Automated unit tests and golden reference cases
- Device-level verification on Android hardware

---

## Development Approach

The project is developed incrementally with explicit acceptance criteria and verification.

Recent work has included:

- validating continuous multi-day behavioral data collection;
- implementing local data deletion and export safeguards;
- expanding the Zi Wei chart engine and time-layer calculations;
- adding evidence-based AI dialogue;
- comparing self-report and observed behavior without merging them into a single personality score;
- testing chart calculations against reference cases rather than relying only on generated text.

---

## Project Direction

The next phase is to move from a research prototype toward a clearer **AI Career Compass** experience:

- translate behavioral and self-report evidence into understandable career-reflection prompts;
- improve personalized AI dialogue while preserving evidence traceability;
- run a small student pilot and evaluate whether the insights are understandable and useful;
- refine the product into a focused demo for education, career development, and social-impact use cases.

---

## About this public repository

The active implementation is currently maintained in a private research repository while the prototype, data-collection design, and research materials continue to evolve.

This public page is intentionally a **portfolio/demo overview**. It documents the product idea, implemented capabilities, technical approach, and responsible-AI boundaries without exposing participant data or private research materials.

---

## About Me

I am a master's student in Computer Science in Taiwan with a cross-disciplinary background in technology, business, and career development. I am interested in applied AI, mobile systems, behavioral data, and building practical tools that help people understand themselves and make better decisions.

GitHub: [@caden6679](https://github.com/caden6679)
