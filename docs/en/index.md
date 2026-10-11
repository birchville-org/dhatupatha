# 📜 Pāṇinīya-Dhātupāṭha (Canonical New Edition)

> **Canonical ground-truth, bilingual facing-page alignment pipeline, and layout-faithful Typst vector new edition for 2,259 verbal roots across 410 book pages following the Böhtlingk standard.**

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Typst](https://img.shields.io/badge/Typst-0.11%2B-orange)
![Root Inventory](https://img.shields.io/badge/Roots-2%2C259%20(100%25)-brightgreen)
![Gaṇas](https://img.shields.io/badge/Gaṇas-10%20Classes-purple)
![Alignment](https://img.shields.io/badge/Alignment-Facing--Page-blueviolet)

> ℹ️ **Case Study:** This project is a reference case study for the open-source book digitization pipeline **[AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich)** in conjunction with **[boethlingk](https://github.com/birchville-org/boethlingk)**.

This repository provides the comprehensive historical processing, machine-readable curation, bilingual facing-page alignment, and typographic vector re-edition of the classical **Pāṇinīya-Dhātupāṭha** (inventory of all 2,259 Sanskrit verbal roots across all 10 Gaṇas) based on a 410-page historical print edition.

---

## ✨ Project Outcomes & Core Artifacts

1. **Canonically Validated Master Dataset (100.0%):**
   * Files: [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json) (2.1 MB) & [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) (1.7 MB)
   * 2,259 Sanskrit verbal roots across all 10 Gaṇas (0 duplicates, 0 omissions).
   * Includes Devanāgarī, scientific IAST transliteration, traditional Aupadeśika markers (e.g., `टु`, `डु`, `इर्`), locative meanings (*arthas*), English translations, grammatical classifications (Pada, Seṭ/Aniṭ, Sakarmaka/Akarmaka), and historical scan page numbers.

2. **Typeset Book PDF with Modern Fonts (Typst Edition):**
   * Output file: [`data/pdf/Dhatu-patha.typeset_edition.pdf`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset_edition.pdf) (2.96 MB, 229 pages)
   * Source code: [`data/pdf/Dhatu-patha.typeset.typ`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset.typ) (1.8 MB)
   * Section-specific layout: Single-column continuous text for front matter (pp. 1–25); two-column grid with vertical divider lines (`grid.vline`) for the dictionary core (pp. 26–285).
   * Marginal concordance: Each page includes marginal references to the historical print edition (`[p. 26]`).
   * Running headers: Dynamic header generation (even pages: book title; odd pages: active Gaṇa designation).
   * Compiles in ~2.4 seconds via [`scripts/build_typeset_edition.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/build_typeset_edition.py) using the Typst typesetting system.

3. **Bilingual Facing-Page Alignment Engine:**
   * Script: [`scripts/align_dhatupatha.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/align_dhatupatha.py)
   * Parallel state machine: Simultaneously aligns odd pages (Devanāgarī) and even pages (IAST transliteration) against canonical ground-truth.
   * Error resilience: Resolves broken ligatures and typesetting omissions from historical lead print through cross-validation of both writing systems.

4. **Hermetically Vendored Fonts (Zero Tofu):**
   * Directory: [`data/fonts/`](https://github.com/birchville-org/dhatupatha/tree/main/data/fonts)
   * Bundles *Noto Serif Devanagari* (Regular/Bold) and *Linux Libertine O* (Regular/Bold/Italic).
   * Guarantees deterministic rendering without box/question-mark artifacts on headless Linux servers and Docker containers.

5. **Standalone QA Viewer:**
   * File: [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html)
   * Split-pane editor conforming to Payer and Birchville standards, featuring a snippet toolbar, instant filtering across all 10 Gaṇas, and silent auto-repair upon local saving via the File System Access API.

---

## 🏛️ The 4 Pillars of the Böhtlingk Standard

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
   • Zero tofu characters (?)                     • pp. 26–285: 2-column grid with grid.vline
   • APT fonts-noto-extra on Linux                • Marginal concordance: [p. 26]
```

1. **Pillar 1 (Facsimile Guarantee):** The Sandwich PDF preserves the historical scan images with complete evidential integrity.
2. **Pillar 2 (Canonical Alignment):** A structured reference database semantically filters the OCR stream to prevent text fragmentation.
3. **Pillar 3 (Section-Specific Layout in Typst):** Dynamically applies single-column layout for introductory text and two-column grid structure for dictionary sections.
4. **Pillar 4 (Hermetic Font Vendoring):** Bundled OpenType fonts ensure identical vector rendering across macOS, Linux, and Docker.

---

## 🚀 Quickstart

### 1. Generate Canonical Ground-Truth
```bash
python3 scripts/build_dhatupatha_groundtruth.py
```
Generates the standardized reference database [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) containing all 2,259 roots.

### 2. Execute Bilingual Facing-Page Alignment
```bash
python3 scripts/align_dhatupatha.py
```
Aligns raw data against ground-truth and outputs the master dataset [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json).

### 3. Compile Typst Vector Re-Edition
```bash
python3 scripts/build_typeset_edition.py \
  --input data/dhatupatha_complete.json \
  --output data/pdf/Dhatu-patha.typeset_edition.pdf
```
Renders the print-ready 229-page edition in ~2.4 seconds.

---

## 📖 Documentation Overview

* [Scientific Case Study (Methodology & Architecture)](case-study.md)
* [QA & Correction Workflow (Single Source of Truth & QA Viewer)](qa-workflow.md)
* [Copyright, Public Domain & Provenance](copyright-and-provenance.md)
* [Data Architecture & 4-Pillar Model](data-architecture.md)
* [Conventions & Technical Specifications](conventions.md)
* [Wiki Overview](wiki-home.md)
