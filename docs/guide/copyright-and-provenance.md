# ⚖️ Urheberrecht, Gemeinfreiheit & Provenienz

Dieses Dokument erläutert den rechtlichen Status des Werkes *Pāṇinīya-Dhātupāṭha*, die urheberrechtliche Einordnung der zugrundeliegenden historischen Drucke und Digitalisate sowie die Standards guter wissenschaftlicher Praxis (Provenienz und Zitation).

---

## 1. Gemeinfreiheit des Originalwerks (Public Domain)

Der **Dhātupāṭha** ist der traditionelle Wurzelkanon der altindischen Grammatik des Pāṇini (ca. 4.–5. Jh. v. Chr.) und gehört zum weltweiten Kulturerbe der Menschheit:

* **Urheber:** Die Wurzel-Listen gehen auf Pāṇini und die vorangehende grammative Tradition des alten Indiens zurück.
* **Historische Drucke:** Die im 19. und frühen 20. Jahrhundert in Europa und Indien erschienenen wissenschaftlichen Druckausgaben sind längst gemeinfrei.
* **Gesetzliche Schutzfrist:** Gemäß § 64 UrhG (Deutschland), Art. 9 URG (Schweiz) sowie Richtlinie 2006/116/EG (EU) erlischt das Urheberrecht 70 Jahre nach dem Tod des Urhebers bzw. Bearbeiters (*post mortem auctoris*).
* **Rechtsfolge:** Das Werk ist **vollständig frei von Urheberrechten** (Public Domain). Der Text, die Devanāgarī-Wurzeln, traditionelle Aupadeśika-Marker, Bedeutungen und Kommentare dürfen von jedermann ohne Einschränkungen vervielfältigt, digitalisiert, verändert, neu gesetzt und öffentlich zugänglich gemacht werden (sowohl nicht-kommerziell als auch kommerziell).

---

## 2. Status der Digitalisate (2D-Scans)

Für die digitale Erfassung und Textausrichtung (OCR & Alignment) werden zweidimensionale Reproduktionsscans historischer Buchseiten genutzt. Auch hier entsteht **kein neues Schutzrecht**:

### Europäisches und deutsches Recht (EU-DSM-Richtlinie & § 68 UrhG)
* **EU-DSM-Richtlinie (EU 2019/790), Artikel 14:**
  > *„Die Mitgliedstaaten sehen vor, dass nach Ablauf der Schutzdauer eines Werkes der bildenden Künste Material, das im Zuge einer Vervielfältigung dieses Werkes entstanden ist, weder dem Urheberrecht noch verwandten Schutzrechten unterliegt [...]“*
* **Deutsches Urheberrechtsgesetz (§ 68 UrhG):**
  Reproduktionen gemeinfreier visueller Werke genießen keinen Schutz nach verwandten Schutzrechten (§§ 70, 71, 72 oder 73 UrhG).
* **Rechtsprechung zu 2D-Scans:** Reine zweidimensionale, originalgetreue Reproduktionsscans von Textseiten entbehren einer persönlichen geistigen Schöpfung (kein Werk im Sinne von § 2 UrhG) und begründen bei gemeinfreien Vorlagen auch kein Leistungsschutzrecht für Lichtbilder (§ 72 UrhG).

Die freie Nachnutzung, Extraktion, Bearbeitung und Veröffentlichung des darin enthaltenen Textes verletzt folglich keine Rechte Dritter.

---

## 3. Bereinigung von Bibliotheksstempeln & Rauschen

Auf historischen Scans befinden sich häufig Bibliotheksstempel, handschriftliche Signaturen und Inventarnummern:

### Rechtliche Einordnung
Diese Vermerke dienen organisatorischen Zwecken der haltenden Institutionen. Sie begründen **kein Urheberrecht** am historischen Text.

### Philologische & technische Notwendigkeit
In automatisierten OCR-Pipelines werden Randnotizen und Bibliotheksstempel fälschlicherweise als Textteile erfasst und in Wortlisten eingestreut. Für eine saubere digitale Edition ist die rückstandslose Entfernung unerlässlich:
* **Datenintegrität:** Keine Verfälschung des kanonischen Wurzelverzeichnisses durch moderne Bibliotheksstempel.
* **Layout-Präzision:** Verhindert das Auseinanderbrechen der zweispaltigen Gitterstruktur in der Typst-Neuedition.

---

## 4. Wissenschaftliche Provenienz & Zitationspraxis

Während der Text frei von Urheberrechten ist, gebietet die **gute wissenschaftliche Praxis**, die Herkunft der Textdaten transparent auszuweisen:

1. **Typst-Buchausgabe (`Dhatu-patha.typeset_edition.pdf`):**
   Das Impressum dokumentiert die zugrundeliegenden Quellen und die Ausrichtung nach dem Böhtlingk-Standard.
2. **Master-JSON-Metadaten (`dhatupatha_complete.json`):**
   Jeder Wurzeleintrag verweist über das Attribut `orig_page` auf die entsprechende historische Buchseite (`[S. 26]`).

---

## 5. Lizenz der Neuausgabe

* **Historischer Textbestand:** Public Domain (Gemeinfreiheit).
* **Pipeline-Code & Typst-Satzvorlagen:** Veröffentlicht unter der [MIT License](https://github.com/birchville-org/dhatupatha/blob/main/LICENSE).
