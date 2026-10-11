---
layout: home

hero:
  name: "Pāṇinīya-Dhātupāṭha"
  text: "Canonical Digital Edition & Interactive Lexicon"
  tagline: "2,259 Sanskrit verbal roots across all 10 Gaṇas with Typst vector typesetting under the Böhtlingk standard"
  actions:
    - theme: brand
      text: "Browse Lexicon →"
      link: "/en/gana/01-bhvadi"
    - theme: alt
      text: "📥 Typeset Edition (PDF, 229 pp.)"
      link: "/Dhatu-patha.typeset_edition.pdf"
      target: "_blank"
    - theme: alt
      text: "📖 Scientific Case Study"
      link: "/en/guide/case-study"

features:
  - icon: "🕉️"
    title: "2,259 Canonical Verbal Roots"
    details: "100% complete coverage across all 10 Gaṇas (Bhvādi to Curādi) with Devanāgarī, scientific IAST transliteration, and Aupadeśika anubandha markers."
  - icon: "🔍"
    title: "Instant Search (⌘K / Ctrl+K)"
    details: "Fast local full-text search across Devanāgarī (भू), IAST (bhū), Sanskrit locative meanings (सत्तायाम्), English glosses, and root IDs."
  - icon: "📑"
    title: "Typst Vector Re-Edition"
    details: "Publication-grade 229-page book PDF with two-column dictionary grid, running headers, and original print page concordance."
  - icon: "🏛️"
    title: "Böhtlingk 4-Pillar Standard"
    details: "Canonical alignment architecture from AlexandriaSandwich: facsimile guarantee, bilingual facing-page heuristics, section-specific layout, and hermetic font vendoring."
---

## The 10 Gaṇas of the Pāṇinīya Tradition

Select a verbal root class to explore all entries:

<GanaIndex />

---

## 🏛️ The 4-Pillar Böhtlingk Standard

```text
                              ┌──────────────────────┐
                              │  410 Original Scans  │
                              └──────────┬───────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
   [ PILLAR 1: FACSIMILE GUARANTEE ]              [ PILLAR 2: CANONICAL ALIGNMENT ]
   • 1:1 unaltered scan pixels                    • Cross-checked against dhatupatha_canonical.json
   • Invisible bbox text layer                    • Bilingual 10-Gaṇa state machine
   • Dhatu-patha.perfect_sandwich.pdf             • 100% complete dhatupatha_complete.json
                                                                 │
                                                                 ▼
   [ PILLAR 4: HERMETIC FONT DEPLOY ]             [ PILLAR 3: TYPST VECTOR RE-EDITION ]
   • data/fonts/ (Noto + Libertine)               • pp. 1–25:  1-column continuous text
   • APT fonts-noto-extra on Linux                • pp. 26–285: 2-column grid with grid.vline
   • Zero tofu characters (?)                     • Marginal concordance: [p. 26]
```

1. **Pillar 1 (Facsimile Guarantee)**: Preserves all 410 historical book pages as pixel-accurate image layers with an invisible bounding-box vector text layer.
2. **Pillar 2 (Canonical Alignment)**: Simultaneous cross-validation of facing pages (odd Devanāgarī, even IAST) via the state machine [`scripts/align_dhatupatha.py`](/en/guide/qa-workflow).
3. **Pillar 3 (Section-Specific Typst Layout)**: 1-column continuous prose for front matter (pp. 1–25), 2-column grid with vertical divider lines for the dictionary core (pp. 26–285).
4. **Pillar 4 (Hermetic Font Vendoring)**: Bundled OpenType fonts (Noto Serif Devanagari and Linux Libertine) ensure zero tofu artifacts across all platforms.

---

## 📖 Documentation & Methodology

* [Scientific Case Study (Methodology & Architecture)](/en/guide/case-study)
* [QA & Correction Workflow (Single Source of Truth & QA Viewer)](/en/guide/qa-workflow)
* [Data Architecture & 4-Pillar Model](/en/guide/data-architecture)
* [Conventions & Technical Specifications](/en/guide/conventions)
* [Copyright, Public Domain & Provenance](/en/guide/copyright-and-provenance)
