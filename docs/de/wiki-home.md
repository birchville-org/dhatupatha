# Willkommen im Wiki des Dhātupāṭha-Projekts

> ℹ️ **Case Study:** Das Projekt `dhatupatha` ist eine vollständige Referenz-Fallstudie zur Buch-Digitalisierungs-Pipeline **[AlexandriaSandwich](https://github.com/birchville-org/AlexandriaSandwich)** im Verbund mit **[boethlingk](https://github.com/birchville-org/boethlingk)**. Es demonstriert das bilinguale Facing-Page-Alignment, die Lösung des Layout-Verlust-Problems bei Wörterbüchern und die sektionsspezifische Typst-Neuedition.

Dieses Wiki dokumentiert die wissenschaftliche Erschließung, bilinguale Ausrichtung, Datenarchitektur und typografische Vektorneuedition des **Pāṇinīya-Dhātupāṭha** (2.259 Verbalwurzeln auf 410 Buchseiten).

---

## 📖 Hauptdokumentation

* 👉 **[Wissenschaftliche Fallstudie: Bilinguales Facing-Page-Alignment & Typst-Neuedition](case-study.md)**
* 👉 **[QA- & Korrektur-Workflow (Single Source of Truth & QA-Viewer)](qa-workflow.md)**
* 👉 **[Urheberrecht, Gemeinfreiheit & Provenienz](copyright-and-provenance.md)**
* 👉 **[Datenarchitektur & 4-Säulen-Modell](data-architecture.md)**
* 👉 **[Konventionen & Technische Spezifikationen](conventions.md)**

Die Dokumentation umfasst:
1. **Ausgangslage & Problemstellung:** Grenzen unstrukturierter OCR bei mehrspaltigen Wörterbüchern („digitalisiert, aber ohne Layout“).
2. **Die Implementierte Lösung:** Der 4-Säulen-Böhtlingk-Standard (Faksimile-Garantie, kanonisches Alignment, sektionsspezifische Typst-Neuedition, hermetisches Font-Vendoring).
3. **Bilinguales Facing-Page-Alignment:** Paralleler Abgleich von ungeraden Devanāgarī- und geraden IAST-Seiten (2.259 Wurzeln lückenlos, 0 Duplikate).
4. **Typst-Vektorneuedition:** Druckreife Neuausgabe (229 Seiten in ~2,4 s) mit zweispaltigem Gitter, dynamischen Kolumnentiteln und Original-Marginalien.
5. **Autarker QA-Viewer:** Webbasierter Split-Pane-Editor mit Silent Auto-Repair beim lokalen Speichern und Sofort-Filterung aller 10 Gaṇas.

---

## 🚀 Schnellzugriff auf Projektergebnisse

| Artefakt | Pfad im Repository | Beschreibung |
| :--- | :--- | :--- |
| **Typst-Neuausgabe (PDF)** | [`data/pdf/Dhatu-patha.typeset_edition.pdf`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset_edition.pdf) | Druckreifes Vektor-PDF (229 Seiten, 2,96 MB) |
| **Typst-Quellcode** | [`data/pdf/Dhatu-patha.typeset.typ`](https://github.com/birchville-org/dhatupatha/blob/main/data/pdf/Dhatu-patha.typeset.typ) | Vollständiger typografischer Satzcode (1,8 MB) |
| **Master-Datensatz** | [`data/dhatupatha_complete.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_complete.json) | Strukturierte JSON-Daten aller 2.259 Wurzeln mit Seitenkonkordanz |
| **Kanonische Ground-Truth** | [`data/dhatupatha_canonical.json`](https://github.com/birchville-org/dhatupatha/blob/main/data/dhatupatha_canonical.json) | Kanonische Pāṇinīya-Referenzdatenbank (1,7 MB) |
| **Autarker QA-Viewer** | [`viewer.html`](https://github.com/birchville-org/dhatupatha/blob/main/viewer.html) | Split-Pane-Editor nach Payer- und Birchville-Standard |
| **Code-Repository** | [birchville-org/dhatupatha](https://github.com/birchville-org/dhatupatha) | Pipeline-Skripte, Schriften und Dokumentation |
