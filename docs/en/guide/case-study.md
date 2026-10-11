# Case Study & Architecture: Pāṇinīya-Dhātupāṭha (Böhtlingk Standard)

> **Canonical ground-truth, bilingual facing-page alignment pipeline, and hybrid Typst vector re-edition for 2,259 verbal roots across 410 book pages.**
>
> *This project is a reference case study for the book digitization pipeline [AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich) in conjunction with the reference project [boethlingk](https://github.com/birchville-org/boethlingk).*

---

## 1. Initial State & The Core Problem

### 1.1 The Phenomenon: "Digitized without Layout" vs. "Digitized AND Original Layout"
During the digitization of the *Dhātu-Pāṭha* (the traditional Pāṇinīya root catalog), a fundamental discrepancy emerged:
* The sister project **Otto von Böhtlingk (1887)** produced a digital edition with complete layout fidelity and sharp typography ("digitized AND original layout").
* The *Dhātu-Pāṭha*, when initially processed through raw OCR-driven re-typesetting, appeared fragmented: tabular root columns fell apart, and lexical meanings merged into unstructured paragraphs ("digitized, but without layout").

Clarifying the root causes and applying the *Böhtlingk Standard* to the *Dhātu-Pāṭha* led to essential architectural insights for dictionary and multilingual book digitization.

### 1.2 Structure of the Historical Source Work
The 410-page volume exhibits a complex two-fold internal organization:
1. **Sectional Structure:**
   * **Front Matter (pp. 1–25):** Single-column continuous prose (preface, grammatical introduction, phonetic rules, anubandha markers) in continuous paragraphs.
   * **Main Corpus (pp. 26–285):** Strictly two-column dictionary and tabular layout for the 10 Gaṇas (root classes from Bhvādi to Curādi).
   * **Back Matter (pp. 286–410):** Alphabetic indices, appendices, and reference tables.
2. **Bilingual Facing Pages:**
   * **Odd Pages (recto):** Primary Sanskrit text in Devanāgarī with traditional Aupadeśika markers and locative meanings (*arthas*).
   * **Even Pages (verso):** Facing scientific transliteration (IAST) with English translations and grammatical attributes (Pada, Seṭ/Aniṭ, Sakarmaka/Akarmaka).

---

## 2. Root Cause Analysis: Why Blind "Reverse-Layout" Fails

Attempting to reconstruct historical print layouts purely by rule-based or statistical reverse-engineering of raw OCR streams inevitably fails due to two structural barriers:

```text
[Raw OCR Data Stream] ──► Sequential Extraction (1D)
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
[Problem 1: Serialization Loss]                  [Problem 2: Layout Constraint]
Multi-column root/meaning alignments             A global 2-column layout destroys
collapse into flat 1D continuous text.           the 1-column preface; a 1-column layout
Typst must guess column boundaries.              destroys the dictionary tabular grid.
```

1. **Serialization Loss:** OCR engines read text blocks linearly. In multi-column lexicons, roots and their corresponding translations become interleaved or serialised out of order.
2. **Global Layout Constraint:** Imposing a single layout model across the entire publication results either in unreadable narrow columns in the preface or an unreadable unstructured wall of text in the dictionary core.

---

## 3. The Solution: The 4-Pillar Böhtlingk Standard

To attain both visual preservation and philological accuracy, the architecture cleanly bifurcates facsimile preservation from semantic re-typesetting:

```text
                              ┌──────────────────────┐
                              │  Raw Scans / Source  │
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

### Pillar 1: The Facsimile Guarantee (`*.perfect_sandwich.pdf`)
* All 410 original scans remain completely untouched and pixel-perfect as the visual background layer.
* The curated full text is layered invisibly (PDF Text Rendering Mode 3) directly upon historical line bounding boxes.
* **Guarantee:** 100% historical evidentiary value, zero layout risk, complete searchability.

### Pillar 2: Canonical Ground-Truth & Bilingual Facing-Page Alignment
Rather than typesetting raw OCR text, it is semantically curated through a two-stage pipeline:
1. **Canonical Reference Database ([`scripts/build_dhatupatha_groundtruth.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/build_dhatupatha_groundtruth.py)):**
   * Generates [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) (2,259 roots across all 10 Gaṇas).
   * Contains canonical Devanāgarī, IAST, Aupadeśika markers, locative meanings (*arthas*), English translations, and Pāṇinīya classifications.
2. **Bilingual Alignment Engine ([`scripts/align_dhatupatha.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/align_dhatupatha.py)):**
   * Because the original uses facing pages (odd Devanāgarī, even IAST), the engine aligns both scripts simultaneously.
   * Damaged Devanāgarī ligatures in the lead print are resolved using the Latin transliteration on the facing page, and vice versa.
   * **Result:** [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json) (100% complete master catalog, fully linked with historical scan page numbers).

### Pillar 3: Section-Specific Layout in Typst ([`scripts/build_typeset_edition.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/build_typeset_edition.py))
The vector re-edition adapts its layout dynamically according to section semantics:
* **Front Matter (pp. 1–25):**
  * Single-column, readable prose in standard width.
  * Preservation of historical paragraphs, section markers, and scan marginalia (`[p. 6]`, `[p. 11]`).
* **Main Corpus / Dictionary (pp. 26–285):**
  * Two-column grid with a subtle vertical divider (`grid.vline`).
  * Centered Gaṇa headers (e.g., *1. Bhvādigaṇaḥ* / *भ्वादिगणः*).
  * Bold Devanāgarī root with accents, italicized IAST, locative meaning, and English translation.
  * Marginal references for fast navigation (`[p. 26]`).
* **Running Headers:**
  * Dynamic header generation: even pages show the book title; odd pages show the active Gaṇa name and pagination.

### Pillar 4: Cross-Platform Font Vendoring & Linux Tofu Fix
* **The Problem:** On macOS, Typst rendered flawlessly due to system fonts (`Devanagari MT`, `Kohinoor Devanagari`). In headless Linux worker containers, all Devanāgarī glyphs rendered as missing character boxes (`?`, tofu).
* **The Solution:**
  1. **Hermetic Font Vendoring:** Open-source fonts are bundled directly in the repository under [`data/fonts/`](https://github.com/birchville-org/dhatupatha/tree/main/data/fonts):
     * `NotoSerifDevanagari-Regular.ttf` & `NotoSerifDevanagari-Bold.ttf`
     * `LinLibertine_R.otf`, `LinLibertine_RB.otf`, `LinLibertine_RI.otf`
  2. **Automated Font Path:** Passes `--font-path data/fonts` to Typst invocations.
  3. **Universal Font Cascade:**
     ```typst
     #set text(
       font: ("Linux Libertine O", "Baskerville", "Times New Roman", "Noto Serif Devanagari", "Devanagari MT", "Kohinoor Devanagari"),
       size: 10pt,
       lang: "de"
     )
     ```

---

## 4. Validation & Results

| Characteristic | Raw OCR Re-Typesetting (Initial) | Böhtlingk Standard (dhatupatha) |
| :--- | :--- | :--- |
| **Facsimile Layer** | Missing or misaligned | **100% 1:1 Scan Facsimile** (`*.perfect_sandwich.pdf`) |
| **Front Matter Layout** | Forcibly squeezed into 2 columns | **1-column elegant continuous text** with scan citations |
| **Dictionary Layout** | Mixed into 1 column | **2-column grid** with `grid.vline` & Gaṇa hierarchy |
| **Root Inventory** | ~1,850 fragments with OCR defects | **2,259 roots (100% complete, 0 duplicates)** |
| **Devanāgarī Rendering** | Tofu question marks (`?`) on Linux | **100% clean vector glyphs** (Noto Serif Devanagari) |
| **Compilation Speed** | Several minutes | **~2.4 seconds** for 229 pages (Typst 0.11.1) |
| **Output File Size** | Uncompressed | **2.96 MB Vector PDF** (searchable, razor-sharp) |
| **Citing Precision** | Historical pagination lost | **Marginal concordance `[p. XX]`** on every page |

---

## 5. Standalone QA Viewer (`viewer.html`)

For philological curation and continuous verification, [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html) was developed following the **Payer Global Web Editor Standard**:
* **Split-Pane:** Left pane provides philological context and attributes (with scan page reference `[p. XX]`); right pane provides the structured root editor.
* **Snippet Toolbar:** Direct buttons for inserting Dandas (`॥`, `।`, `ऽ`, `°`), accents (`॑`, `॒`), and all IAST diacritics (`ā`, `ī`, `ū`, `ṛ`, `ñ`, `ṭ`, `ḍ`, `ṇ`, `ś`, `ṣ`).
* **Silent Auto-Repair on Save:** Saving (`⌘S` / `Ctrl+S`) silently converts pipes (`||`) into Dandas (`॥`), normalizes spacing, and eliminates control noise. Subtle visual feedback is provided through a brief yellow blink of the save button without modal interruptions.
* **Local Storage First & File System Access API:** Enables direct, secure local file updates to `data/dhatupatha_complete.json`.

---

## 6. Summary & Conclusion

Quality in digitized scholarly editions is not achieved by attempting to "reverse-guess" layout from unstructured OCR text. It arises from two complementary, independent workflows:
1. The **Sandwich PDF** archives and protects the historical source image with absolute 1:1 evidential integrity.
2. The **Typst Vector Edition** builds upon canonically verified data to render modern typography tailored specifically to each section of the work.
