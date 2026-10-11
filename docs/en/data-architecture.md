# 🏛️ Data Architecture — dhatupatha

> This document describes the directory structure, the data model, and the processing pipeline of the `dhatupatha` edition.

---

## 1. Project Directory Layout

```text
dhatupatha/
├── assets/
│   └── birchville_logo.png           # Birchville Coat of Arms (Brand Asset)
│
├── data/
│   ├── dhatupatha_canonical.json     # Canonical Pāṇinīya reference database (1.7 MB, 2,259 roots)
│   ├── dhatupatha_complete.json      # Aligner master catalog with page concordance (2.1 MB)
│   ├── fonts/                        # Vendored OpenType fonts (Noto + Libertine)
│   │   ├── NotoSerifDevanagari-Regular.ttf
│   │   ├── NotoSerifDevanagari-Bold.ttf
│   │   ├── LinLibertine_R.otf
│   │   ├── LinLibertine_RB.otf
│   │   └── LinLibertine_RI.otf
│   └── pdf/
│       ├── Dhatu-patha.typeset_edition.pdf # Typographic vector re-edition (2.96 MB, 229 pages)
│       └── Dhatu-patha.typeset.typ         # Typst source code of the edition (1.8 MB)
│
├── docs/                             # Bilingual MkDocs documentation
│   ├── de/                           # German documentation (Default)
│   ├── en/                           # English documentation
│   ├── assets/                       # Logos and brand assets
│   └── stylesheets/                  # Birchville Scholarly Synthesis theme
│
├── scripts/                          # Automation & build scripts
│   ├── build_dhatupatha_groundtruth.py # Generates canonical ground-truth
│   ├── align_dhatupatha.py             # Bilingual facing-page alignment engine
│   └── build_typeset_edition.py        # Typst vector compiler
│
├── viewer.html                       # Standalone QA Viewer (Payer standard)
├── mkdocs.yml                        # Documentation site configuration
├── pyproject.toml                    # Python project configuration
├── requirements.txt                  # Python dependencies
├── LICENSE                           # MIT License
└── README.md                         # Project overview
```

---

## 2. The Four-Layer Data Model

```text
Layer 1 — Facsimile Image Base
  Source:   410 historical book pages
  Purpose:  Visual background layer in 1:1 Sandwich PDF and primary citation reference

Layer 2 — Bilingual OCR & Facing-Page Geometry
  Content:  Parallel text layers of odd (Devanāgarī) and even pages (IAST)
  Purpose:  Cross-validation of degraded lead typography and complex ligatures

Layer 3 — Canonical Master JSON & Ground-Truth
  Storage:  data/dhatupatha_canonical.json & data/dhatupatha_complete.json
  Content:  2,259 structured root objects across all 10 Gaṇas with page concordance
  Status:   100.0% complete (0 duplicates, 0 omissions)

Layer 4 — Target Artifacts & Typographic Re-Edition
  Storage:  data/pdf/Dhatu-patha.typeset_edition.pdf & viewer.html
  Content:  Print-ready 229-page vector PDF in Typst and standalone QA Viewer
```

---

## 3. End-to-End Processing Pipeline

```text
[Historical Scans (410 pages)]
       │
       ▼
[Step 1: Canonical Ground-Truth] ──► scripts/build_dhatupatha_groundtruth.py
       │                                └── data/dhatupatha_canonical.json (2,259 roots)
       ▼
[Step 2: Bilingual Alignment] ─────► scripts/align_dhatupatha.py
       │                                ├── Parallel state machine (Odd Deva / Even IAST)
       │                                └── Page concordance indexing
       ▼
[Step 3: Master Consolidation] ────► data/dhatupatha_complete.json
       │                                (Single Source of Truth, 2,259 entries)
       ▼
[Step 4: Multi-Artifact Build]
       ├── Typst Vector PDF:     data/pdf/Dhatu-patha.typeset_edition.pdf (~2.4s build)
       ├── Typst Source:         data/pdf/Dhatu-patha.typeset.typ
       └── QA Viewer:            viewer.html (Payer standard)
```

---

## 4. Dataset Metrics

| Metric | Value | Comment |
| :--- | :--- | :--- |
| **Scanned Book Pages** | 410 pages | pp. 1–25 (Front Matter), pp. 26–285 (Main Corpus), pp. 286–410 (Back Matter) |
| **Total Root Count** | 2,259 roots | Completely captured across all 10 Gaṇas |
| **Gaṇa Classes** | 10 classes | 1. Bhvādi to 10. Curādi |
| **Duplicates / Missing** | 0 / 0 | 100.0% aligned against the grammatical canon |
| **Typst Book Length** | 229 pages | Section-specific layout (1-column prose / 2-column dictionary) |
| **Typst Compile Time** | ~2.4 seconds | Vector rendering via Typst 0.11+ |
| **Font Vendoring** | 5 OpenType files | Hermetically bundled in `data/fonts/` (Zero Tofu) |

---

## 5. Data Model Specification (`dhatupatha_complete.json`)

Each of the 2,259 entries has the following schema:

```json
{
  "id": 1,
  "gana": 1,
  "gana_name": "भ्वादिगणः",
  "gana_iast": "Bhvādigaṇaḥ",
  "dhatu": "भू",
  "iast_dhatu": "bhū",
  "aupadeshik": "भू",
  "iast_aupadeshik": "bhū",
  "pada": "parasmaipada",
  "settva": "seṭ",
  "karma": "akarmaka",
  "artha": "सत्तायाम्",
  "iast_artha": "sattāyām",
  "artha_english": "to be, to exist",
  "orig_page": 26,
  "commentary_note": ""
}
```

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | Integer | Unique sequential ID (1 to 2,259) |
| `gana` | Integer | Root class number (1 to 10) |
| `gana_name` | String | Gaṇa name in Devanāgarī (e.g., `भ्वादिगणः`) |
| `gana_iast` | String | Gaṇa name in IAST (e.g., `Bhvādigaṇaḥ`) |
| `dhatu` | String | Canonical root in Devanāgarī (e.g., `भू`) |
| `iast_dhatu` | String | Root in scientific IAST transliteration |
| `aupadeshik` | String | Traditional Aupadeśika citation form with anubandha markers |
| `iast_aupadeshik` | String | Aupadeśika form in IAST |
| `pada` | String | Voice classification (`parasmaipada`, `ātmanepada`, `ubhayapada`) |
| `settva` | String | Augment marker (`seṭ`, `aniṭ`, `veṭ`) |
| `karma` | String | Transitivity (`sakarmaka`, `akarmaka`, `dvikarmaka`) |
| `artha` | String | Traditional Sanskrit locative meaning (e.g., `सत्तायाम्`) |
| `iast_artha` | String | Locative meaning in IAST (e.g., `sattāyām`) |
| `artha_english` | String | English gloss of basic meaning |
| `orig_page` | Integer | Historical scan page number (e.g., `26`) |
| `commentary_note` | String | Additional grammatical notes |
