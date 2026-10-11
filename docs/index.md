---
layout: home

hero:
  name: "Pāṇinīya-Dhātupāṭha"
  text: "Kanonische Neuedition & Interaktives Lexikon"
  tagline: "2.259 Sanskrit-Verbalwurzeln über alle 10 Gaṇas mit Typst-Vektorsatz nach dem Böhtlingk-Standard"
  actions:
    - theme: brand
      text: "Lexikon durchsuchen →"
      link: "/gana/01-bhvadi"
    - theme: alt
      text: "📥 Typst-Buchausgabe (PDF, 229 S.)"
      link: "/Dhatu-patha.typeset_edition.pdf"
      target: "_blank"
    - theme: alt
      text: "📖 Wissenschaftliche Fallstudie"
      link: "/guide/case-study"

features:
  - icon: "🕉️"
    title: "2.259 Kanonische Verbalwurzeln"
    details: "100% lückenlose Erfassung aller 10 Gaṇas (Bhvādi bis Curādi) mit Devanāgarī, wissenschaftlicher IAST-Transliteration und Aupadeśika-It-Markern."
  - icon: "🔍"
    title: "Sofortsuche (⌘K / Ctrl+K)"
    details: "Blitzschnelle lokale Client-Side-Volltextsuche in Devanāgarī (भू), IAST (bhū), Sanskrit-Bedeutungen (सत्तायाम्), Englisch und nach Wurzel-IDs."
  - icon: "📑"
    title: "Typst-Vektorneuedition"
    details: "Druckreifes 229-seitiges Buch-PDF mit zweispaltigem Wörterbuchgitter, dynamischen Kolumnentiteln und Marginal-Konkordanz zum historischen Druck."
  - icon: "🏛️"
    title: "Böhtlingk 4-Säulen-Standard"
    details: "Kanonisches Alignment aus AlexandriaSandwich: Faksimile-Garantie, bilinguale Facing-Page-Heuristik, layouttreuer Neusatz und hermetisches Font-Vendoring."
---

## Die 10 Gaṇas der Pāṇinīya-Tradition

Wählen Sie eine Wurzelklasse zur direkten Ansicht aller Einträge:

<GanaIndex />

---

## 🏛️ Der 4-Säulen-Böhtlingk-Standard

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

1. **Säule 1 (Faksimile-Garantie)**: 1:1 Erhalt aller 410 historischen Originalseiten als pixelgenaue Bildschicht mit unsichtbarem Bounding-Box-Textlayer.
2. **Säule 2 (Kanonisches Alignment)**: Kreuzvalidierung gegenüberliegender Seiten (ungerade Devanāgarī, gerade IAST) über die Statusmaschine [`scripts/align_dhatupatha.py`](/guide/qa-workflow).
3. **Säule 3 (Sektionsspezifische Typst-Neuedition)**: 1-spaltiger Fließtext für die Einführung (S. 1–25), zweispaltiges Gitter mit vertikaler Trennlinie für das Wörterbuch (S. 26–285).
4. **Säule 4 (Hermetisches Font-Vendoring)**: Bündelung von Noto Serif Devanagari und Linux Libertine garantiert fehlerfreies Rendern ohne Tofu-Zeichen auf allen Betriebssystemen.

---

## 📖 Dokumentation & Methodik

* [Wissenschaftliche Fallstudie (Verfahrensdokumentation)](/guide/case-study)
* [QA- & Korrektur-Workflow (Single Source of Truth & QA-Viewer)](/guide/qa-workflow)
* [Datenarchitektur & 4-Säulen-Modell](/guide/data-architecture)
* [Konventionen & Technische Spezifikationen](/guide/conventions)
* [Urheberrecht, Gemeinfreiheit & Provenienz](/guide/copyright-and-provenance)
