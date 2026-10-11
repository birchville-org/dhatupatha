# ⚖️ Copyright, Public Domain & Provenance

This document clarifies the legal status of the *Pāṇinīya-Dhātupāṭha*, the copyright classification of historical prints and digital scans, and the standards of scholarly practice (provenance and citation).

---

## 1. Public Domain Status of the Original Work

The **Dhātupāṭha** is the ancient grammatical root catalog attributed to Pāṇini (c. 4th–5th century BCE) and forms part of humanity's shared cultural heritage:

* **Authorship:** Root lists trace back to Pāṇini and the ancient Indian grammatical tradition.
* **Historical Prints:** Scholarly prints published in Europe and India during the 19th and early 20th centuries have long passed into the public domain.
* **Statutory Terms:** Under Section 64 UrhG (Germany), Article 9 URG (Switzerland), and Directive 2006/116/EC (European Union), copyright expires 70 years after the death of the author/editor (*post mortem auctoris*).
* **Legal Conclusion:** The text is **wholly free of copyright** (Public Domain). Sanskrit roots, traditional Aupadeśika markers, locative meanings, and grammatical analyses may be freely reproduced, digitized, edited, typeset, and republished for non-commercial and commercial purposes alike.

---

## 2. Legal Status of Digital Reproductions (2D Scans)

Two-dimensional scans of out-of-copyright book pages do not establish new intellectual property rights:

### European and German Law (EU DSM Directive & Section 68 UrhG)
* **EU DSM Directive (EU 2019/790), Article 14:**
  > *"Member States shall provide that, when the term of protection of a work of visual art has expired, any material resulting from an act of reproduction of that work is not subject to copyright or related rights [...]"*
* **German Copyright Act (Section 68 UrhG):**
  Reproductions of public-domain visual works enjoy no protection under neighboring rights (Sections 70, 71, 72, or 73 UrhG).
* **Jurisprudence on 2D Scans:** Pure two-dimensional faithful scans of book pages lack personal intellectual creation (not a work under Section 2 UrhG) and do not grant photographic neighboring rights (Section 72 UrhG) when applied to public domain originals.

Extracting, modifying, and publishing the textual contents infringes no third-party rights.

---

## 3. Removal of Library Watermarks & Artifacts

Historical scans frequently carry administrative stamps and shelf marks:

### Legal Characterization
These stamps serve organizational tracking for holding libraries. They do **not establish copyright** in the underlying text.

### Philological & Technical Necessity
Automated OCR pipelines mistakenly ingest margins and stamps as body text. Clean removal is mandatory:
* **Data Integrity:** Avoids corrupting the grammatical canon with modern institutional markings.
* **Layout Stability:** Prevents grid disruption in the multi-column Typst typesetting pipeline.

---

## 4. Scholarly Provenance & Citation Standards

While the text is free of copyright, **good academic practice** requires transparent attribution of sources:

1. **Typst Book Edition (`Dhatu-patha.typeset_edition.pdf`):**
   The colophon details the historical print editions consulted and alignment methods under the Böhtlingk Standard.
2. **Master JSON Metadata (`dhatupatha_complete.json`):**
   Every root entry records the historical print page via the `orig_page` attribute (`[p. 26]`).

---

## 5. Licensing of the Edition

* **Historical Textual Data:** Public Domain.
* **Pipeline Code & Typst Templates:** Released under the [MIT License](https://github.com/birchville-org/dhatupatha/blob/main/LICENSE).
