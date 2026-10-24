# Changelog

Alle relevanten Änderungen am Projekt **Pāṇinīya-Dhātupāṭha** werden in dieser Datei dokumentiert.

Das Format basiert auf [Keep a Changelog](https://keepachangelog.com/de/1.0.0/),
und dieses Projekt folgt [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.2.0] - 2026-10-24

### Hinzugefügt
- **AlexandriaSandwich v1.7.0 Pipeline-Integration**:
  - **Content-Aware Margin Masking**: Bereinigung aller 410 Faksimile-Seiten von Buchfalzen, Bundstegschatten und Scannerrändern außerhalb des Satzspiegels (`Dhatu-patha.perfect_sandwich.pdf`).
  - **Layout-Profilierung (`data/layout.profile.json`)**: Präzise 2D-Vermessung von Satzspiegel, Randproportionen und asymmetrischem Bundsteg (`inside: 60.1pt, outside: 53.2pt`).
- **Typografisch veredelter Neusatz (`Dhatu-patha.typeset_edition.pdf`)**:
  - Zentrierte Haupttitel und strukturierter Erstzeileneinzug (`1.5em`).
  - Symmetrische Dreispaltengitter mit nativer Ziffern-Parität.
  - Kompilierung von 29.972 Zeilen Typst-Code ohne Schriftsatz-Warnungen.

### Geändert
- **Publikations-Artefakte**:
  - Aktualisiertes Vektordokument in `docs/public/Dhatu-patha.typeset_edition.pdf` (2.96 MB).
  - Bereinigtes Faksimile auf 94.02 MB optimiert (zlib FlateDecode, 28% Größenreduktion gegenüber Vorversion).

## [1.1.0] - 2026-10-16

### Hinzugefügt
- **Deklaratives Job-Profil (`data/job.config.json`)**: Volle Spezifikationskonformität mit dem `AlexandriaSandwich v1.5.0` Schema inklusive Heuristiken (`two_column`, `strip_running_headers`, `strip_library_boilerplates`, `strip_rogue_scripts`, `typeset_mode: dictionary_grid`) und IIIF-Auflösungstemplates.
- **Hierarchische PDF-Gliederung (Bookmarks)**: 
  - Vektor-Neuausgabe (`Dhatu-patha.typeset_edition.pdf`): 12 saubere Lesezeichen (Vorwort, Einführung, 10 Gaṇas) mit vollständigen Dokumentmetadaten (Titel, Autor, Keywords).
  - Faksimile-Sandwich (`Dhatu-patha.perfect_sandwich.pdf`): 39 strukturierte Lesezeichen mit hierarchischer Verankerung der 10 Gaṇas auf ihren historischen Startseiten (S. 27–105).

### Geändert
- **Typst-Neusatz & Vektorausgabe**:
  - Deduplizierung von Kopfzeilen-Artefakten im Front-Matter (Verhinderung wiederholter Einführungstitel auf Folgeseiten).
  - Einbindung der vendorten Schriften (`Noto Serif Devanagari`, `Linux Libertine O`) via `--font-path data/fonts` ohne Font-Warnungen.
  - Bereitstellung der aktualisierten Vektor-PDF in `docs/public/Dhatu-patha.typeset_edition.pdf` und im Upstream-Archiv.
- **VitePress-Dokumentationsplattform**:
  - Erfolgreicher Produktions-Build (`vitepress build docs`) in 4,69s.
