# 📜 Pāṇinīya-Dhātupāṭha (Kanonische Neuedition)

> **Kanonische Ground-Truth, bilinguale Facing-Page-Alignment-Pipeline und layouttreue Typst-Vektorneuedition für 2.259 Verbalwurzeln auf 410 Buchseiten nach dem Böhtlingk-Standard.**

![Python](https://img.shields.io/badge/python-3.12%2B-blue)
![Typst](https://img.shields.io/badge/Typst-0.11%2B-orange)
![Wurzelbestand](https://img.shields.io/badge/Wurzeln-2.259%20(100%25)-brightgreen)
![Gaṇas](https://img.shields.io/badge/Gaṇas-10%20Klassen-purple)
![Alignment](https://img.shields.io/badge/Alignment-Facing--Page-blueviolet)

> ℹ️ **Case Study:** Dieses Projekt ist eine Referenz-Fallstudie zur Open-Source-Digitalisierungs-Pipeline **[AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich)** im Verbund mit **[boethlingk](https://github.com/birchville-org/boethlingk)**.

Dieses Repository umfasst die vollständige historische Erschließung, maschinenlesbare Kuration, bilinguale Ausrichtung (Facing-Page-Alignment) und typografische Vektorneuedition des klassischen **Pāṇinīya-Dhātupāṭha** (Verzeichnis aller 2.259 Sanskrit-Verbalwurzeln über alle 10 Gaṇas) auf Basis eines 410-seitigen historischen Drucks.

---

## ✨ Projektergebnisse & Kernartefakte

1. **Kanonisch validierter Master-Datensatz (100,0 %):**
   * Datei: [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json) (2,1 MB) & [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) (1,7 MB)
   * 2.259 Sanskrit-Verbalwurzeln über alle 10 Gaṇas (0 Duplikate, 0 Fehlstellen).
   * Enthält Devanāgarī, wissenschaftliche IAST-Transliteration, traditionelle Aupadeśika-Marker (z. B. `टु`, `डु`, `इर्`), Lokativ-Bedeutungen (*arthas*), englische Übersetzungen, grammatische Klassifikationen (Pada, Seṭ/Aniṭ, Sakarmaka/Akarmaka) und historische Scan-Seitenzahlen.

2. **Neu gesetztes Buch-PDF mit modernen Schriften (Typst-Edition):**
   * Datei: [`data/pdf/Dhatu-patha.typeset_edition.pdf`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset_edition.pdf) (2,96 MB, 229 Seiten)
   * Satzquellcode: [`data/pdf/Dhatu-patha.typeset.typ`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset.typ) (1,8 MB)
   * Sektionsspezifisches Layout: 1-spaltiger Fließtext für Front Matter (S. 1–25); 2-spaltiges Gitter mit vertikaler Trennlinie (`grid.vline`) für das Wörterbuch (S. 26–285).
   * Marginal-Konkordanz: Jede Seite enthält Marginalien mit Bezug zum historischen Druck (`[S. 26]`).
   * Lebende Kolumnentitel: Dynamische Kopfzeilen (gerade Seiten: Buchtitel; ungerade Seiten: Gaṇa-Bezeichnung).
   * Kompiliert in ca. 2,4 Sekunden via [`scripts/build_typeset_edition.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/build_typeset_edition.py) mit dem Satzsystem Typst.

3. **Bilinguale Facing-Page-Alignment-Engine:**
   * Skript: [`scripts/align_dhatupatha.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/align_dhatupatha.py)
   * Parallele Statusmaschine: Gleicht ungerade Seiten (Devanāgarī) und gerade Seiten (IAST-Transliteration) simultan gegen die kanonische Ground-Truth ab.
   * Fehlerkorrektur: Beseitigt Ligaturfehler und typografische Auslassungen des historischen Bleisatzes durch Kreuzvalidierung beider Schriftsysteme.

4. **Hermetisch vendorte Schriften (Zero Tofu):**
   * Verzeichnis: [`data/fonts/`](https://github.com/birchville-org/dhatupatha/tree/main/data/fonts)
   * Enthält *Noto Serif Devanagari* (Regular/Bold) und *Linux Libertine O* (Regular/Bold/Italic).
   * Verhindert Darstellungsfehler (Kästchen / Fragezeichen) in headless Linux- und Docker-Build-Umgebungen.

5. **Autarker QA-Viewer:**
   * Datei: [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html)
   * Split-Pane-Editor nach Payer- und Birchville-Standard mit Snippet-Toolbar, Sofort-Filterung über alle 10 Gaṇas und Silent Auto-Repair beim lokalen Speichern via File System Access API.

---

## 🏛️ Die 4 Säulen des Böhtlingk-Standards

```text
                              ┌──────────────────────┐
                              │  410 Originalscans   │
                              └──────────┬───────────┘
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
   [ SÄULE 1: FAKSIMILE-GARANTIE ]                [ SÄULE 2: KANONISCHES ALIGNMENT ]
   • 1:1 unveränderte Scan-Pixel                  • Abgleich gegen dhatupatha_canonical.json
   • Unsichtbarer Bbox-Textlayer                  • Bilinguale 10-Gaṇa-Statusmaschine
   • Dhatu-patha.perfect_sandwich.pdf             • 100 % lückenloses dhatupatha_complete.json
                                                                 │
                                                                 ▼
   [ SÄULE 4: HERMETISCHES FONT-DEPLOY ]          [ SÄULE 3: TYPST-VEKTORNEUEDITION ]
   • data/fonts/ (Noto + Libertine)               • S. 1–25:  1-Spalten Fließtext
   • APT fonts-noto-extra auf Linux               • S. 26–285: 2-Spalten-Gitter mit grid.vline
   • Null Tofu-Zeichen (?)                        • Marginal-Konkordanz: [S. 26]
```

1. **Säule 1 (Faksimile-Garantie):** Das Sandwich-PDF bewahrt die historische Bildschicht mit 100 % visueller Beweiskraft.
2. **Säule 2 (Kanonisches Alignment):** Eine maschinenlesbare Referenzdatenbank kuratiert den OCR-Datenstrom semantisch und verhindert Textfragmentierung.
3. **Säule 3 (Sektionsspezifische Layouttreue in Typst):** Dynamische Trennung zwischen 1-spaltigem Fließtext (Einleitung) und 2-spaltigem Tabellenlexikon (Hauptteil).
4. **Säule 4 (Hermetisches Font-Vendoring):** Gebündelte OpenType-Schriften garantieren konsistentes Rendern auf allen Plattformen (macOS, Linux, Docker).

---

## 🚀 Schnellstart

### 1. Kanonische Ground-Truth generieren
```bash
python3 scripts/build_dhatupatha_groundtruth.py
```
Erzeugt die standardisierte Referenzdatei [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) mit allen 2.259 Wurzeln.

### 2. Bilinguales Facing-Page-Alignment ausführen
```bash
python3 scripts/align_dhatupatha.py
```
Gleicht Rohdaten gegen die Ground-Truth ab und generiert den Master-Datensatz [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json).

### 3. Typst-Vektorneuedition kompilieren
```bash
python3 scripts/build_typeset_edition.py \
  --input data/dhatupatha_complete.json \
  --output data/pdf/Dhatu-patha.typeset_edition.pdf
```
Rendert die druckreife 229-seitige Gesamtausgabe in ca. 2,4 Sekunden.

---

## 📖 Dokumentationsübersicht

* [Wissenschaftliche Fallstudie (Verfahrensdokumentation)](case-study.md)
* [QA- & Korrektur-Workflow (Single Source of Truth & QA-Viewer)](qa-workflow.md)
* [Urheberrecht, Gemeinfreiheit & Provenienz](copyright-and-provenance.md)
* [Datenarchitektur & 4-Säulen-Modell](data-architecture.md)
* [Konventionen & Technische Spezifikationen](conventions.md)
* [Wiki-Übersicht](wiki-home.md)
