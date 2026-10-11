# 🛠️ QA- & Korrektur-Workflow

Dieser Leitfaden beschreibt, wie Textungenauigkeiten, Diakritika oder grammatische Attribut-Korrekturen im Projekt `dhatupatha` kollationiert, korrigiert und deterministisch in alle Editions-Artefakte (Typst-Buch-PDF, kanonische Datenbanken) übernommen werden.

---

## 🏛️ Das Architekturprinzip: Single Source of Truth

Alle Korrekturen erfolgen **ausschließlich an einer einzigen zentralen Stelle**:
👉 [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json)

Manuelle Änderungen in generierten Ausgabedateien (wie der Typst-PDF-Ausgabe) sind strikt zu vermeiden, da diese Dateien bei jedem Build-Lauf automatisiert überschrieben werden.

```text
                               ┌────────────────────────┐
                               │     Korrektur in       │
                               │   Master-JSON-Datei    │
                               │(dhatupatha_complete)   │
                               └───────────┬────────────┘
                                           │
                      ┌────────────────────┴────────────────────┐
                      ▼                                         ▼
         scripts/build_typeset_edition.py             viewer.html (QA-Viewer)
                      │                                         │
                      ▼                                         ▼
          [Dhatu-patha.typeset_edition.pdf]             Visuelle Verifikation &
               (Modernes Buch-PDF)                      Sofort-Filter (10 Gaṇas)
```

---

## 🔍 Weg 1: Visuelle Kollationierung mit dem QA-Viewer (Empfohlen)

Für die Überprüfung von Wurzeln, Bedeutungen und Gaṇa-Attributen enthält das Repository den autarken Editor [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html).

### 1. Lokalen Server starten
Aufgrund von Browser-Sicherheitsrichtlinien (CORS) empfiehlt sich ein lokaler Webserver:
```bash
python3 -m http.server 8000
```
Öffnen Sie im Browser: `http://localhost:8000/viewer.html`

### 2. Bedienung & Editor-Funktionen
- **Linker Bereich (Philologischer Kontext & Status):** Zeigt Gaṇa-Zuordnung, Original-Seitenzahl (`[S. XX]`), Pāṇinīya-Klassifikationen (Pada, Seṭ/Aniṭ, Sakarmaka/Akarmaka) sowie Schnellnavigation.
- **Rechter Bereich (Wurzel-Editor):** Die Daten des ausgewählten Eintrags sind direkt editierbar:
  - `dhatu`: Wurzel in Devanāgarī
  - `iast_dhatu`: Wissenschaftliche Transliteration
  - `aupadeshik`: Aupadeśika-Form mit It-Markern
  - `artha`: Sanskrit-Bedeutung im Lokativ
  - `artha_english`: Englische Übersetzung
- **Snippet-Toolbar:** Direkte Schaltflächen zum Einfügen von Dandas (`॥`, `।`, `ऽ`, `°`), Akzenten (`॑`, `॒`) und allen IAST-Diakritika (`ā`, `ī`, `ū`, `ṛ`, `ñ`, `ṭ`, `ḍ`, `ṇ`, `ś`, `ṣ`).
- **Sofort-Filter:** Filterung nach den 10 Gaṇas und Volltextsuche über Wurzeln, Umschriften und Bedeutungen.

### 3. Speichern mit Silent Auto-Repair
- Drücken Sie `Cmd+S` (Mac) bzw. `Ctrl+S` (Windows/Linux) oder klicken Sie auf **„Speichern (JSON)“**.
- Der Editor führt ein unaufdringliches *Silent Auto-Repair* durch (Bereinigung doppelter Leerzeichen, Wandlung von Pipes in Dandas) und speichert den Datensatz direkt über die *File System Access API* in `data/dhatupatha_complete.json`.
- Visuelles Feedback erfolgt durch ein kurzes gelbes Blinken der Schaltfläche ohne störende Popups.

---

## ⌨️ Weg 2: Gezielte Bearbeitung im Code-Editor

Wenn Ihnen die Wurzel-ID (z. B. `1` für *bhū*) oder die Devanāgarī-Form bekannt ist:

1. Öffnen Sie `data/dhatupatha_complete.json` in VS Code oder Ihrem bevorzugten Editor.
2. Suchen Sie nach `"id": 1` oder `"dhatu": "भू"`.
3. Passen Sie die Felder an:
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
4. Datei speichern.

---

## ⚡ Schritt 3: Typst-Buchausgabe neu kompilieren

Nach dem Speichern der Korrektur führen Sie im Terminal das Build-Skript aus:

```bash
python3 scripts/build_typeset_edition.py \
  --input data/dhatupatha_complete.json \
  --output data/pdf/Dhatu-patha.typeset_edition.pdf
```
Kompiliert die druckreife 229-seitige Vektorausgabe in ca. 2,4 Sekunden neu.

---

## 🚀 Schritt 4: Prüfen, Committen & Pull Request (Kuratierungs-Workflow)

Das Projekt `dhatupatha` wird als **wissenschaftlich kuratierte Edition** (Curated Edition, Birchville-Standard) geführt.

### 1. Lokale Integritätsprüfung ausführen
Vor jedem Commit ist sicherzustellen, dass alle 2.259 Wurzeln lückenlos erhalten sind:

```bash
python3 -c "
import json
with open('data/dhatupatha_complete.json', encoding='utf-8') as f:
    d = json.load(f)
assert len(d) == 2259, f'Fehler: Erwartet 2259 Wurzeln, gefunden {len(d)}'
print('Integrität: 100% OK (2.259 Wurzeln)')
"
```

### 2. Feature-Branch erstellen & committen
```bash
git checkout -b fix/root-bhu-1
git add data/dhatupatha_complete.json
git commit -m "fix(root): correct artha reading for dhatu 1 (bhu)"
```

### 3. Branch pushen & Pull Request eröffnen
```bash
git push -u origin fix/root-bhu-1
```
Eröffnen Sie anschließend auf GitHub einen Pull Request gegen den Branch `main`.

### 4. Kuratierung & Review
Jede Korrektur wird vor dem Merge philologisch und datentechnisch geprüft:
1. **Philologische Verifikation:** Stimmt die Korrektur mit der historischen Vorlage und den Pāṇinīya-Regeln überein?
2. **Kanonische Konsistenz:** Bleiben Wurzel-ID, Gaṇa-Nummerierung und Aupadeśika-Marker intakt?
3. **Freigabe:** Nach Bestätigung wird der PR gemergt und neue PDF-Releases werden bereitgestellt.
