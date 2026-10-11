# 🏛️ Datenarchitektur — dhatupatha

> Dieses Dokument beschreibt die Verzeichnisstruktur, das Datenmodell und die Verarbeitungspipeline der Edition `dhatupatha`.

---

## 1. Projekt- und Verzeichnisstruktur

```text
dhatupatha/
├── assets/
│   └── birchville_logo.png           # Birchville Wappen (Corporate Design)
│
├── data/
│   ├── dhatupatha_canonical.json     # Kanonische Pāṇinīya-Referenzdatenbank (1,7 MB, 2.259 Wurzeln)
│   ├── dhatupatha_complete.json      # Aligner Masterkatalog mit Seitenkonkordanz (2,1 MB)
│   ├── fonts/                        # Vendorte OpenType-Schriften (Noto + Libertine)
│   │   ├── NotoSerifDevanagari-Regular.ttf
│   │   ├── NotoSerifDevanagari-Bold.ttf
│   │   ├── LinLibertine_R.otf
│   │   ├── LinLibertine_RB.otf
│   │   └── LinLibertine_RI.otf
│   └── pdf/
│       ├── Dhatu-patha.typeset_edition.pdf # Typografische Vektor-Neuedition (2,96 MB, 229 Seiten)
│       └── Dhatu-patha.typeset.typ         # Typst Quellcode der Neuedition (1,8 MB)
│
├── docs/                             # Zweisprachige MkDocs-Dokumentation
│   ├── de/                           # Deutsche Dokumentation (Default)
│   ├── en/                           # Englische Dokumentation
│   ├── assets/                       # Logo und Bildressourcen
│   └── stylesheets/                  # Birchville Scholarly Synthesis Theme
│
├── scripts/                          # Automatisierungs- & Build-Skripte
│   ├── build_dhatupatha_groundtruth.py # Generiert kanonische Ground-Truth
│   ├── align_dhatupatha.py             # Bilinguale Facing-Page-Alignment-Engine
│   └── build_typeset_edition.py        # Typst-Vektorsatz-Compiler
│
├── viewer.html                       # Autarker QA-Viewer (Payer Global Web Editor Standard)
├── mkdocs.yml                        # Konfiguration der Dokumentationsseite
├── pyproject.toml                    # Python Projektkonfiguration
├── requirements.txt                  # Python Abhängigkeiten
├── LICENSE                           # MIT Lizenz
└── README.md                         # Projektübersicht
```

---

## 2. Das Vier-Layer-Datenmodell

```text
Layer 1 — Faksimile-Bildbasis
  Quelle:   410 historische Buchseiten
  Zweck:    Visuelle Hintergrundschicht im 1:1 Sandwich-PDF und Primärbeleg für jede Wurzel

Layer 2 — Bilinguale OCR & Facing-Page Geometrie
  Inhalt:   Parallele Textschichten der ungeraden (Devanāgarī) und geraden Seiten (IAST)
  Zweck:    Kreuzvalidierung von abgenutztem Bleisatz und Ligaturen

Layer 3 — Kanonische Master-JSON & Ground-Truth
  Ablage:   data/dhatupatha_canonical.json & data/dhatupatha_complete.json
  Inhalt:   2.259 strukturierte Wurzel-Objekte über alle 10 Gaṇas mit Seitenkonkordanz
  Status:   100,0 % lückenlos (0 Duplikate, 0 Fehlstellen)

Layer 4 — Zielartefakte & Typografischer Neusatz
  Ablage:   data/pdf/Dhatu-patha.typeset_edition.pdf & viewer.html
  Inhalt:   Druckreifes 229-seitiges Vektor-PDF in Typst und autarker QA-Viewer
```

---

## 3. End-to-End Verarbeitungs-Pipeline

```text
[Historische Scans (410 Seiten)]
       │
       ▼
[Schritt 1: Kanonische Ground-Truth] ──► scripts/build_dhatupatha_groundtruth.py
       │                                  └── data/dhatupatha_canonical.json (2.259 Wurzeln)
       ▼
[Schritt 2: Bilinguales Alignment] ────► scripts/align_dhatupatha.py
       │                                  ├── Parallele Statusmaschine (Ungerade Deva / Gerade IAST)
       │                                  └── Seitenkonkordanz-Verknüpfung
       ▼
[Schritt 3: Master-Konsolidierung] ────► data/dhatupatha_complete.json
       │                                  (Single Source of Truth, 2.259 Einträge)
       ▼
[Schritt 4: Multi-Artefakt-Build]
       ├── Typst Vektor-PDF:     data/pdf/Dhatu-patha.typeset_edition.pdf (~2,4 s Build)
       ├── Typst Source:         data/pdf/Dhatu-patha.typeset.typ
       └── QA-Viewer:            viewer.html (Payer-Standard)
```

---

## 4. Kennzahlen des Datenbestands

| Metrik | Wert | Bemerkung |
| :--- | :--- | :--- |
| **Erfasste Buchseiten** | 410 Seiten | S. 1–25 (Front Matter), S. 26–285 (Hauptteil), S. 286–410 (Back Matter) |
| **Gesamte Wurzelanzahl** | 2.259 Wurzeln | Vollständig über alle 10 Gaṇas erfasst |
| **Gaṇa-Klassen** | 10 Klassen | 1. Bhvādi bis 10. Curādi |
| **Duplikate / Fehlstellen** | 0 / 0 | 100,0 % lückenlos abgeglichen |
| **Typst-Buchumfang** | 229 Seiten | Sektionsspezifisches Layout (1-spaltig / 2-spaltig) |
| **Typst-Kompilierungszeit** | ~2,4 Sekunden | Vektorgenerierung via Typst 0.11+ |
| **Schriften-Vendoring** | 5 OpenType-Dateien | Hermetisch in `data/fonts/` (Zero Tofu) |

---

## 5. Datenmodell-Spezifikation (`dhatupatha_complete.json`)

Jeder der 2.259 Einträge besitzt folgendes Schema:

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

| Feld | Typ | Beschreibung |
| :--- | :--- | :--- |
| `id` | Integer | Eindeutige fortlaufende ID (1 bis 2.259) |
| `gana` | Integer | Nummer der Wurzelklasse (1 bis 10) |
| `gana_name` | String | Bezeichnung des Gaṇa in Devanāgarī (z. B. `भ्वादिगणः`) |
| `gana_iast` | String | Bezeichnung des Gaṇa in IAST (z. B. `Bhvādigaṇaḥ`) |
| `dhatu` | String | Kanonische Wurzel in Devanāgarī (z. B. `भू`) |
| `iast_dhatu` | String | Wurzel in wissenschaftlicher IAST-Transliteration |
| `aupadeshik` | String | Traditionelle Aupadeśika-Form mit It-Markern |
| `iast_aupadeshik` | String | Aupadeśika-Form in IAST |
| `pada` | String | Pada-Zuordnung (`parasmaipada`, `ātmanepada`, `ubhayapada`) |
| `settva` | String | It-Charakteristik (`seṭ`, `aniṭ`, `veṭ`) |
| `karma` | String | Valenz / Transitivität (`sakarmaka`, `akarmaka`, `dvikarmaka`) |
| `artha` | String | Traditionelle Sanskrit-Bedeutung im Lokativ (z. B. `सत्तायाम्`) |
| `iast_artha` | String | Lokativ-Bedeutung in IAST (z. B. `sattāyām`) |
| `artha_english` | String | Englische Übersetzung der Grundbedeutung |
| `orig_page` | Integer | Buchseite des historischen Drucks (z. B. `26`) |
| `commentary_note` | String | Zusätzliche grammatische Anmerkungen |
