# 🛠️ QA & Correction Workflow

This guide details how textual nuances, diacritics, or grammatical classifications in `dhatupatha` are collated, corrected, and deterministically propagated across all edition artifacts.

---

## 🏛️ Architecture Principle: Single Source of Truth

All corrections are applied exclusively to a **single canonical location**:
👉 [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json)

Manual edits in generated output files (such as the Typst book PDF) must never be made, as they are overwritten automatically upon each build run.

```text
                               ┌────────────────────────┐
                               │     Correction in      │
                               │   Master JSON File     │
                               │(dhatupatha_complete)   │
                               └───────────┬────────────┘
                                           │
                      ┌────────────────────┴────────────────────┐
                      ▼                                         ▼
         scripts/build_typeset_edition.py             viewer.html (QA Viewer)
                      │                                         │
                      ▼                                         ▼
          [Dhatu-patha.typeset_edition.pdf]             Visual Verification &
               (Modern Book PDF)                        Instant 10-Gaṇa Filter
```

---

## 🔍 Path 1: Visual Collation with the QA Viewer (Recommended)

To verify roots, meanings, and Gaṇa attributes interactively, the repository includes [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html).

### 1. Launch a Local Web Server
Due to browser CORS restrictions for local file access, launch a simple local server:
```bash
python3 -m http.server 8000
```
Open in your browser: `http://localhost:8000/viewer.html`

### 2. Interface & Features
- **Left Pane (Context & Metadata):** Displays Gaṇa assignment, original print page reference (`[p. XX]`), Pāṇinīya classifications (Pada, Seṭ/Aniṭ, Sakarmaka/Akarmaka), and rapid navigation.
- **Right Pane (Root Editor):** Directly edit the selected root attributes:
  - `dhatu`: Root in Devanāgarī
  - `iast_dhatu`: Scientific IAST transliteration
  - `aupadeshik`: Aupadeśika citation form with anubandha markers
  - `artha`: Traditional Sanskrit locative meaning
  - `artha_english`: English gloss
- **Snippet Toolbar:** Instant buttons to insert Dandas (`॥`, `।`, `ऽ`, `°`), accents (`॑`, `॒`), and all IAST diacritics (`ā`, `ī`, `ū`, `ṛ`, `ñ`, `ṭ`, `ḍ`, `ṇ`, `ś`, `ṣ`).
- **Instant Filters:** Real-time filtering across all 10 Gaṇas and full-text search across Devanāgarī, IAST, and English glosses.

### 3. Saving with Silent Auto-Repair
- Press `Cmd+S` (Mac) / `Ctrl+S` (Windows/Linux) or click **"Speichern (JSON)"**.
- The editor silently applies auto-repair rules (normalizes spacing, converts pipes into Dandas) and writes back directly to `data/dhatupatha_complete.json` via the File System Access API.
- Subtle visual feedback is given by a brief yellow blink of the button, avoiding disrupting modal dialogues.

---

## ⌨️ Path 2: Direct Code-Editor Editing

If you already know the numeric ID (e.g., `1` for *bhū*) or Devanāgarī form:

1. Open `data/dhatupatha_complete.json` in VS Code or your preferred editor.
2. Locate `"id": 1` or `"dhatu": "भू"`.
3. Update the attributes:
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
4. Save the file.

---

## ⚡ Step 3: Recompile the Typst Vector Edition

After updating the data, rebuild the publication:

```bash
python3 scripts/build_typeset_edition.py \
  --input data/dhatupatha_complete.json \
  --output data/pdf/Dhatu-patha.typeset_edition.pdf
```
Rerenders the 229-page print-ready vector PDF in ~2.4 seconds.

---

## 🚀 Step 4: Verify, Commit & Pull Request (Curation Workflow)

The `dhatupatha` edition is managed as a **scientifically curated edition** (Birchville standard).

### 1. Run Local Integrity Check
Ensure all 2,259 roots remain intact:

```bash
python3 -c "
import json
with open('data/dhatupatha_complete.json', encoding='utf-8') as f:
    d = json.load(f)
assert len(d) == 2259, f'Error: Expected 2259 roots, found {len(d)}'
print('Integrity: 100% OK (2,259 roots)')
"
```

### 2. Create Feature Branch & Commit
```bash
git checkout -b fix/root-bhu-1
git add data/dhatupatha_complete.json
git commit -m "fix(root): correct artha reading for dhatu 1 (bhu)"
```

### 3. Push Branch & Open Pull Request
```bash
git push -u origin fix/root-bhu-1
```
Open a Pull Request on GitHub against the `main` branch.

### 4. Review & Merge
Each PR undergoes philological and structural review before merging:
1. **Philological Verification:** Does the reading conform to the historical edition and Pāṇinīya rules?
2. **Structural Consistency:** Are the ID sequence, Gaṇa classification, and anubandhas intact?
3. **Approval:** Upon review, the PR is merged into `main` and new PDF release assets are generated.
