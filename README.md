# 📜 Pāṇinīya-Dhātupāṭha (Kanonische Neuedition)

> **Kanonische Ground-Truth, bilinguale Facing-Page-Alignment-Pipeline und layouttreue Typst-Vektorneuedition für 2.259 Verbalwurzeln auf 410 Buchseiten nach dem Böhtlingk-Standard.**
> 
> 🌐 **Live QA-Viewer:** [birchville-org.github.io/dhatupatha](https://birchville-org.github.io/dhatupatha/)  
> 🏛️ **Upstream-Pipeline:** [birchville-org/AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich)

---

## 1. Projektübersicht

Dieses Repository enthält die philologisch kuratierte, maschinenlesbare Gesamtedition des klassischen **Pāṇinīya-Dhātupāṭha** (Verzeichnis der 2.259 Sanskrit-Verbalwurzeln über alle 10 Gaṇas).

Das Werk wurde nach dem **Böhtlingk-Standard** (entwickelt im Schwesterprojekt [boethlingk](https://github.com/birchville-org/boethlingk)) aus einem 410-seitigen historischen Druck digitalisiert. Dabei wurde das fundamentale Problem gelöst, warum frühere OCR-Versuche zu unstrukturiertem Text („digitalisiert, aber ohne Layout“) führten:

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

---

## 2. Die 4 Säulen des Böhtlingk-Standards

### 1. Faksimile-Garantie (`Dhatu-patha.perfect_sandwich.pdf`)
* Alle 410 Original-Buchseiten bleiben pixelgenau und ohne Rasterungsverlust als Bildschicht erhalten.
* Der bereinigte Text liegt unsichtbar (PDF Text Rendering Mode 3) exakt auf den historischen Bounding-Boxen.
* **Garantie:** 100 % historische Zitierfähigkeit und Authentizität.

### 2. Kanonisches Ground-Truth-Alignment (`scripts/align_dhatupatha.py`)
* Anstatt fehleranfälligen OCR-Fließtext unstrukturiert zu setzen, gleicht eine Statusmaschine den Text gegen eine maschinenlesbare Referenzdatenbank ([data/dhatupatha_canonical.json](data/dhatupatha_canonical.json), 2.259 Wurzeln) ab.
* **Bilinguale Facing-Page-Heuristik:** Das Werk weist gegenüberliegende Seiten auf (ungerade = Devanāgarī, gerade = IAST-Transliteration). Die Engine gleicht *beide* Schriftsysteme parallel ab; Lesefehler abgenutzter Devanāgarī-Bleitypen werden durch die lateinische Umschrift der Gegenseite bereinigt und umgekehrt.
* **Master-Datenbank:** [data/dhatupatha_complete.json](data/dhatupatha_complete.json) verknüpft jede Wurzel lückenlos mit der historischen Scan-Seitenzahl.

### 3. Sektionsspezifische Layouttreue in Typst (`scripts/build_typeset_edition.py`)
Kein starres globales Spaltenmodell, sondern dynamische Anpassung an die Werkstruktur:
* **Front Matter (S. 1–25):** Großzügiger, 1-spaltiger Fließtext für Vorwort, grammatische Einführung und Lautgesetze mit Originalabsätzen und Scan-Marginalien (`[S. 6]`, `[S. 11]`).
* **Hauptteil / Wörterbuch (S. 26–285):** Zweispaltiges Gitter mit vertikaler Trennlinie (`grid.vline`), zentrierten Gaṇa-Kopfzeilen, fettgesetzten Devanāgarī-Wurzeln, IAST, Lokativ-Bedeutungen (*arthas*), englischer Übersetzung und Marginal-Konkordanz (`[S. 26]`).
* **Lebende Kolumnentitel:** Dynamischer Typst-Header im Code-Modus (gerade Seiten: Buchtitel; ungerade Seiten: Gaṇa-Name + Paginierung).
* **Ergebnis:** [data/pdf/Dhatu-patha.typeset_edition.pdf](data/pdf/Dhatu-patha.typeset_edition.pdf) (229 Seiten in ~2,4 Sekunden gerendert).

### 4. Hermetisches Font-Vendoring & Linux-Härtung
* OpenType-Master-Schriften liegen direkt unter [data/fonts/](data/fonts/):
  * `NotoSerifDevanagari-Regular.ttf` & `NotoSerifDevanagari-Bold.ttf`
  * `LinLibertine_R.otf`, `LinLibertine_RB.otf`, `LinLibertine_RI.otf`
* Automatischer Typst-Aufruf mit `--font-path data/fonts` und universeller Fallback-Kaskade verhindert Tofu-Fragezeichen (`?`) auf Headless-Linux-Servern.

---

## 3. Interaktiver QA-Viewer (`viewer.html`)

Für die philologische Prüfung und dauerhafte Nutzung steht ein autarker Web-Editor nach dem **Payer Global Web Editor Standard** und dem **Birchville Scholarly Synthesis Corporate Design** bereit:

* **Split-Pane:** Links Kontext und philologische Parameter (mit Scan-Seitenzahl `[S. XX]`), rechts der strukturierte Wurzel-Editor.
* **Snippet-Toolbar:** Direkte Einfügemöglichkeit für Dandas (`॥`, `।`, `ऽ`, `°`), Akzentzeichen (`॑`, `॒`) und alle IAST-Diakritika (`ā`, `ī`, `ū`, `ṛ`, `ñ`, `ṭ`, `ḍ`, `ṇ`, `ś`, `ṣ`, etc.).
* **Silent Auto-Repair on Save (`⌘S` / `Ctrl+S`):** Konvertiert Pipes (`||`) lautlos zu Dandas (`॥`), normalisiert Leerzeichen und bereinigt Tippfehler. Visuelles Feedback über sanftes Gelb-Blinken der Speichern-Schaltfläche (keine störenden Modalfenster).
* **Local Storage First & File System Access API:** Speichert Revisionen unmittelbar lokal im Browser und erlaubt das direkte Zurückschreiben via `showSaveFilePicker`.
* **Sofort-Filter:** Filterung über alle 10 Gaṇas und Volltextsuche über Devanāgarī, IAST, Artha und Wurzel-ID.

---

## 4. Datenmodell (`dhatupatha_complete.json`)

Jeder der 2.259 Einträge besitzt folgende Struktur:

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

---

## 5. Repository-Struktur

```text
dhatupatha/
├── assets/
│   └── birchville_logo.png           # Birchville Wappen (Corporate Design)
├── data/
│   ├── dhatupatha_canonical.json     # Kanonische Pāṇinīya-Referenzdatenbank (1,7 MB)
│   ├── dhatupatha_complete.json      # Aligner Masterkatalog mit Seitenkonkordanz (2,1 MB)
│   ├── fonts/                        # Vendorte OpenType-Schriften (Noto + Libertine)
│   └── pdf/
│       ├── Dhatu-patha.typeset_edition.pdf # Typografische Vektor-Neuedition (3,0 MB)
│       └── Dhatu-patha.typeset.typ         # Typst Quellcode der Neuedition (1,8 MB)
├── scripts/
│   ├── build_dhatupatha_groundtruth.py # Generiert kanonische Ground-Truth
│   ├── align_dhatupatha.py             # Bilinguale Facing-Page-Alignment-Engine
│   └── build_typeset_edition.py        # Typst-Vektorsatz-Compiler
├── viewer.html                       # Autarker QA-Viewer (Payer-Standard)
├── index.html                        # GitHub Pages Einstiegspunkt
├── LICENSE                           # MIT Lizenz
└── README.md                         # Diese Dokumentation
```

---

## 6. Verwandte Editionen & Links

* 🏛️ **Digitalisierungs-Pipeline:** [birchville-org/AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich)
* 📖 **Pāṇinis Grammatik (1887):** [birchville-org/boethlingk](https://github.com/birchville-org/boethlingk)
* 📜 **Bṛhadāraṇyaka-Upaniṣad I.4:** [birchville-org/brhadaranyaka](https://github.com/birchville-org/brhadaranyaka)
