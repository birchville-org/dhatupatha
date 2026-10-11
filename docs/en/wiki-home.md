# Welcome to the Dhātupāṭha Project Wiki

> ℹ️ **Case Study:** The `dhatupatha` project is a comprehensive reference case study for the book digitization pipeline **[AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich)** in conjunction with **[boethlingk](https://github.com/birchville-org/boethlingk)**. It demonstrates bilingual facing-page alignment, solving layout collapse in multi-column lexicons, and section-specific Typst vector re-edition.

This wiki documents the scholarly curation, bilingual alignment, data architecture, and typographic vector re-edition of the **Pāṇinīya-Dhātupāṭha** (2,259 verbal roots across 410 book pages).

---

## 📖 Main Documentation

* 👉 **[Scientific Case Study: Bilingual Facing-Page Alignment & Typst Re-Edition](case-study.md)**
* 👉 **[QA & Correction Workflow (Single Source of Truth & QA Viewer)](qa-workflow.md)**
* 👉 **[Copyright, Public Domain & Provenance](copyright-and-provenance.md)**
* 👉 **[Data Architecture & 4-Pillar Model](data-architecture.md)**
* 👉 **[Conventions & Technical Specifications](conventions.md)**

The documentation details:
1. **Initial State & Problem Statement:** Pitfalls of naive OCR in multi-column lexicons ("digitized without layout").
2. **The Implemented Solution:** The 4-Pillar Böhtlingk Standard (facsimile guarantee, canonical alignment, section-specific Typst re-typesetting, hermetic font deployment).
3. **Bilingual Facing-Page Alignment:** Simultaneous cross-validation of odd Devanāgarī and even IAST pages (2,259 roots without omissions or duplicates).
4. **Typst Vector Re-Edition:** Print-ready volume (229 pages in ~2.4s) with two-column layout, running headers, and original marginal pagination.
5. **Standalone QA Viewer:** Lightweight web-based split-pane editor with silent auto-repair upon local saving and instant 10-Gaṇa filtering.

---

## 🚀 Quick Access to Project Artifacts

| Artifact | Repository Path | Description |
| :--- | :--- | :--- |
| **Typst Vector Edition (PDF)** | [`data/pdf/Dhatu-patha.typeset_edition.pdf`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset_edition.pdf) | Print-ready vector PDF (229 pages, 2.96 MB) |
| **Typst Typesetting Source** | [`data/pdf/Dhatu-patha.typeset.typ`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset.typ) | Complete Typst markup (1.8 MB) |
| **Master Dataset** | [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json) | Structured JSON dataset of all 2,259 roots with page concordance |
| **Canonical Ground-Truth** | [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) | Canonical Pāṇinīya reference catalog (1.7 MB) |
| **Standalone QA Viewer** | [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html) | Split-pane editor following Payer and Birchville standards |
| **Source Repository** | [birchville-org/dhatupatha](https://github.com/birchville-org/dhatupatha) | Pipeline scripts, bundled fonts, and documentation |
