# Fallstudie & Verfahrensdokumentation: Pāṇinīya-Dhātupāṭha (Böhtlingk-Standard)

> **Kanonische Ground-Truth, bilinguale Facing-Page-Alignment-Pipeline und hybride Typst-Vektorneuedition für 2.259 Verbalwurzeln auf 410 Buchseiten.**
>
> *Dieses Projekt ist eine Referenz-Fallstudie (Case Study) zur Buch-Digitalisierungs-Pipeline [AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich) im Verbund mit dem Referenzprojekt [boethlingk](https://github.com/birchville-org/boethlingk).*

---

## 1. Ausgangslage & Die Kernfrage

### 1.1 Das Phänomen: „Digitalisiert aber ohne Layout“ vs. „Digitalisiert UND Original-Layout“
Bei der Digitalisierung des *Dhātu-Pāṭha* (traditionelles Pāṇinīya-Wurzelverzeichnis) trat ein Phänomen zutage, das für historische Fachliteratur typisch ist:
* Das Schwesterprojekt **Otto von Böhtlingk (1887)** erzeugte durch kanonisches Sūtra-Alignment ein Buchergebnis mit voller Layouttreue und gestochen scharfem Satzbild („digitalisiert UND Original-Layout“).
* Der *Dhātu-Pāṭha* erschien nach einem rein OCR-gestützten Neusatzversuch unstrukturiert: Tabellarische Wurzelspalten brachen auseinander, grammatische Bedeutungen flossen in Absätze zusammen („digitalisiert, aber ohne Layout“).

Die Klärung der Ursachen und die Übertragung des *Böhtlingk-Standards* auf den *Dhātu-Pāṭha* führten zu grundlegenden Erkenntnissen für die gesamte Editionsarchitektur.

### 1.2 Die Struktur des historischen Ausgangswerkes
Das 410-seitige Werk weist eine komplexe zweifache Binnenstruktur auf:
1. **Sektionsstruktur:**
   * **Front Matter (S. 1–25):** Rein einspaltiger Fließtext (Vorwort, grammatische Einführung, Lautgesetze, Erläuterung der It-Marker) in zusammenhängenden Absätzen.
   * **Hauptteil (S. 26–285):** Streng zweispaltiges Wörterbuch- und Tabellenlayout der 10 Gaṇas (Wurzelklassen von Bhvādi bis Curādi).
   * **Back Matter (S. 286–410):** Register, Indizes und Anhangstabellen.
2. **Bilinguale Gegenüberstellung (Facing Pages):**
   * **Ungerade Seiten (rechts):** Primärer Sanskrit-Text in Devanāgarī mit traditionellen Aupadeśika-Markern und Lokativ-Bedeutungen (*arthas*).
   * **Gerade Seiten (links):** Gegenüberliegende wissenschaftliche Transliteration (IAST) mit englischer Übersetzung und grammatischen Attributen (Pada, Seṭ/Aniṭ, Sakarmaka/Akarmaka).

---

## 2. Ursachenanalyse: Warum blindes „Reverse-Layout“ scheitert

Der Versuch, aus rohem OCR-Volltext das Original-Layout rein regelbasiert oder statistisch Seite für Seite zu rekonstruieren, scheitert an zwei strukturellen Hürden:

```text
[Roher OCR-Datenstrom] ──► Sequentielles Auslesen (1D)
                                  │
         ┌────────────────────────┴────────────────────────┐
         ▼                                                 ▼
[Problem 1: Serialisierungsverlust]              [Problem 2: Layout-Zwang]
Zweispaltige Wurzel/Bedeutung-Flucht             Ein globales 2-Spalten-Layout
wird zu flachem 1D-Fließtext reduziert.          zerstört das 1-spaltige Vorwort;
Typst muss Spaltenbrüche raten.                  1-Spalten-Layout zerstört das Lexikon.
```

1. **Serialisierungsverlust:** OCR-Engines lesen Textblöcke primär linear aus. Bei mehrspaltigen Wörterbüchern werden Wurzeln und ihre zugehörigen Übersetzungen zeilenweise vermischt oder in falscher Reihenfolge serialisiert.
2. **Globaler Layout-Zwang:** Wird dem Satzgenerator (Typst) ein starres Spaltenmodell verordnet, entsteht entweder im Vorwort unleserlicher Schmalspaltensatz oder im Hauptteil ein unübersichtlicher Fließtext ohne Spaltentrennung.

---

## 3. Die Lösung: Der 4-Säulen-Böhtlingk-Standard

Um maximale visuelle und philologische Treue zu erzielen, trennt das Projekt strikt zwischen dem Faksimile-Erhalt und der semantisch geführten Neuedition:

```text
                              ┌──────────────────────┐
                              │  Rohscans / Quelle   │
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

### Säule 1: Die Faksimile-Garantie (`*.perfect_sandwich.pdf`)
* Die 410 Originalscans bleiben unverändert und pixelgenau als Bildschicht erhalten.
* Der bereinigte Volltext liegt unsichtbar (PDF Text Rendering Mode 3) exakt auf den Bounding-Boxen der historischen Druckzeilen.
* **Garantie:** 100 % historische Beweiskraft, 0 % Layout-Risiko, vollständige Volltext-Durchsuchbarkeit.

### Säule 2: Kanonische Ground-Truth & Bilinguales Facing-Page-Alignment
Anstatt den unvollkommenen OCR-Text blind zu setzen, wird er über eine zweistufige Pipeline semantisch kuratiert:
1. **Kanonische Referenzdatenbank ([`scripts/build_dhatupatha_groundtruth.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/build_dhatupatha_groundtruth.py)):**
   * Erzeugt [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) (2.259 Wurzeln über alle 10 Gaṇas).
   * Enthält kanonische Devanāgarī, IAST, Aupadeśika-It-Marker (z. B. `टु`, `डु`, `इर्`), Sanskrit-Bedeutungen im Lokativ (`भू सत्तायाम्`), englische Übersetzungen und Pāṇinīya-Klassifikationen.
2. **Bilinguale Alignment-Engine ([`scripts/align_dhatupatha.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/align_dhatupatha.py)):**
   * Da der Druck gegenüberliegende Seiten nutzt (ungerade Devanāgarī, gerade IAST), gleicht die Statusmaschine die Erkennung gegen **beide** Schriftsysteme parallel ab.
   * Unleserliche Devanāgarī-Ligaturen werden durch die lateinische Transliteration der Gegenseite verifiziert und umgekehrt.
   * **Ergebnis:** [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json) (100 % lückenloser Masterkatalog, vollständig mit den Original-Seitenzahlen verknüpft).

### Säule 3: Sektionsspezifische Layouttreue in Typst ([`scripts/build_typeset_edition.py`](https://github.com/birchville-org/dhatupatha/blob/main/scripts/build_typeset_edition.py))
Die Vektorneuedition passt ihr Layout dynamisch an die logischen Abschnitte des Werkes an:
* **Front Matter (S. 1–25):**
  * Einspaltiger, eleganter Fließtext in Standardbreite.
  * Erhalt der originalen Absätze, Paragraphen und Gliederungspunkte.
  * Randnotizen mit Scan-Konkordanz (`[S. 6]`, `[S. 11]`).
* **Hauptteil / Wörterbuch (S. 26–285):**
  * Zweispaltiges Tabellengitter mit vertikaler Trennlinie (`grid.vline`).
  * Zentrierte Gaṇa-Kopfzeilen (z. B. *1. Bhvādigaṇaḥ* / *भ्वादिगणः*).
  * Fette Devanāgarī-Wurzel mit Akzenten, daneben kursive IAST-Umschrift, Lokativ-Bedeutung und englische Übersetzung.
  * Marginalien zur schnellen Orientierung (`[S. 26]`).
* **Lebende Kolumnentitel (Running Headers):**
  * Dynamischer Typst-Header: Gerade Seiten tragen den Buchtitel; ungerade Seiten zeigen den aktuellen Gaṇa-Namen und die Seitenzahl.

### Säule 4: Cross-Platform Font-Vendoring & Linux-Tofu-Fix
Ein kritischer Befund bei der Portierung von macOS auf Linux-Produktionsserver:
* **Das Problem:** Unter macOS renderte Typst fehlerfrei, da macOS indische Systemschriften vorhält (`Devanagari MT`, `Kohinoor Devanagari`). Im Linux-Worker-Container erschienen jedoch alle Devanāgarī-Zeichen als Fragezeichen in Kästchen (`?`, Tofu).
* **Die Lösung:**
  1. **Hermetisches Font-Vendoring:** Open-Source-Schriften liegen direkt im Repository unter [`data/fonts/`](https://github.com/birchville-org/dhatupatha/tree/main/data/fonts):
     * `NotoSerifDevanagari-Regular.ttf` & `NotoSerifDevanagari-Bold.ttf`
     * `LinLibertine_R.otf`, `LinLibertine_RB.otf`, `LinLibertine_RI.otf`
  2. **Automatischer Font-Pfad:** Übergabe von `--font-path data/fonts` beim Typst-Aufruf.
  3. **Universelle Schriftkaskade:**
     ```typst
     #set text(
       font: ("Linux Libertine O", "Baskerville", "Times New Roman", "Noto Serif Devanagari", "Devanagari MT", "Kohinoor Devanagari"),
       size: 10pt,
       lang: "de"
     )
     ```

---

## 4. Validierung & Ergebnisse

| Eigenschaft | Roher OCR-Neusatz (initial) | Böhtlingk-Standard (dhatupatha) |
| :--- | :--- | :--- |
| **Faksimile-Ebene** | Fehlend oder ungenau | **100 % 1:1 Scan-Faksimile** (`*.perfect_sandwich.pdf`) |
| **Layout Front Matter** | Fälschlich 2-spaltig gequetscht | **1-spaltiger eleganter Fließtext** mit Scan-Referenzen |
| **Layout Wörterbuch** | 1-spaltig vermischt | **2-spaltiges Gitter** mit `grid.vline` & Gaṇa-Hierarchie |
| **Wurzelbestand** | ~1.850 Fragmente mit OCR-Fehlern | **2.259 Wurzeln (100 % lückenlos, 0 Duplikate)** |
| **Devanāgarī-Rendering** | Tofu-Fragezeichen (`?`) auf Linux | **100 % saubere Vektorglyphen** (Noto Serif Devanagari) |
| **Kompilierungszeit** | Mehrere Minuten | **~2,4 Sekunden** für 229 Seiten (Typst 0.11.1) |
| **Dateigröße Neusatz** | Unbereinigt | **2,96 MB Vektor-PDF** (durchsuchbar, gestochen scharf) |
| **Zitierfähigkeit** | Seitenbezug ging verloren | **Marginal-Konkordanz `[S. XX]`** auf jeder Seite |

---

## 5. Autarker QA-Viewer (`viewer.html`)

Für die philologische Revision und dauerhafte Prüfung wurde [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html) nach dem **Payer Global Web Editor Standard** implementiert:
* **Split-Pane:** Links Kontext und philologische Parameter (mit Scan-Seitenzahl `[S. XX]`), rechts der strukturierte Wurzel-Editor.
* **Snippet-Toolbar:** Direkte Schaltflächen für Dandas (`॥`, `।`, `ऽ`, `°`), Akzentzeichen (`॑`, `॒`) und alle IAST-Diakritika (`ā`, `ī`, `ū`, `ṛ`, `ñ`, `ṭ`, `ḍ`, `ṇ`, `ś`, `ṣ`).
* **Silent Auto-Repair on Save:** Beim Speichern (`⌘S` / `Ctrl+S`) werden Pipes (`||`) lautlos zu Dandas (`॥`) gewandelt, doppelte Leerzeichen normalisiert und fehlerhafte Steuerzeichen entfernt. Visuelle Rückmeldung erfolgt unaufdringlich durch kurzes Gelb-Blinken der Schaltfläche ohne Modal-Popups.
* **Local Storage First & File System Access API:** Ermöglicht direktes lokales Speichern in `data/dhatupatha_complete.json`.

---

## 6. Zusammenfassendes Fazit

Die Qualität des Endprodukts entsteht nicht durch den Versuch, ein gedrucktes Layout aus unstrukturiertem OCR-Text „rückwärts zu erraten“ (*Reverse-Layout*), sondern durch das Zusammenspiel zweier autarker Pfade:
1. Das **Sandwich-PDF** archiviert und schützt das historische Originalbild mit absoluter 1:1-Treue.
2. Die **Typst-Neuedition** baut auf einer kanonisch verifizierten Datenbasis auf und wendet professionelle typografische Regeln sektionsspezifisch an.
