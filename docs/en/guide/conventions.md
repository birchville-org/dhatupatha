# 📐 Conventions & Technical Specifications — dhatupatha

> This document defines the classification schemes, language tagging, and typographic conventions of the `dhatupatha` edition.

---

## 1. The 10 Gaṇas of the Pāṇinīya Tradition

The Dhātupāṭha groups the entire Sanskrit verbal inventory into 10 canonical root classes (*gaṇas*):

| No. | Gaṇa Name (IAST) | Gaṇa Name (Devanāgarī) | Distinguishing Feature |
| :--- | :--- | :--- | :--- |
| **1** | Bhvādigaṇaḥ | भ्वादिगणः | Thematic class (*śap* infix, Guṇa strengthening) |
| **2** | Adādigaṇaḥ | अदादिगणः | Root inflection without class infix (*luk*) |
| **3** | Juhotyādigaṇaḥ | जुहोत्यादिगणः | Reduplicated root class (*ślu*) |
| **4** | Divādigaṇaḥ | दिवादिगणः | *śyan* infix (-ya-) |
| **5** | Svādigaṇaḥ | स्वादिगणः | *śnu* infix (-no-/-nu-) |
| **6** | Tudādigaṇaḥ | तुदादिगणः | Thematic without Guṇa (*śa*) |
| **7** | Rudhādigaṇaḥ | रुधादिगणः | Nasal infix (*śnam*) |
| **8** | Tanādigaṇaḥ | तनादिगणः | *u* infix (*u*) |
| **9** | Kryādigaṇaḥ | क्र्यादिगणः | *śnā* infix (-nā-/-nī-) |
| **10** | Curādigaṇaḥ | चुरादिगणः | Causative/denominative class (*ṇic*) |

---

## 2. Aupadeśika Markers & Anubandhas (It-Letters)

In Pāṇini's grammatical metalanguage, roots in their primitive canonical form (*upadeśa*) are augmented with auxiliary markers (*it* / *anubandha*) that govern morphological operations:
* **Prefixal markers:** e.g., `टु` (triggers suffix *-thu*), `डु` (conditions Kṛt derivation), `इर्` (indicates aorist stem formation).
* **Suffixal markers:** e.g., nasalized vowels or consonants such as `ञ्` (indicates Ubhayapada voice), `ण्` (triggers Vṛddhi), `क्` (blocks Guṇa and Vṛddhi).
* The dataset records both the canonical stripped root form (`dhatu`) and the traditional citation form with markers (`aupadeshik`).

---

## 3. Language Tagging (BCP 47)

* `sa` / `xml:lang="sa"`: Sanskrit text in Devanāgarī (e.g., `भू`, `सत्तायाम्`).
* `sa-Latn` / `xml:lang="sa-Latn"`: Sanskrit in scientific IAST transliteration (e.g., `bhū`, `sattāyām`).
* `en`: English translations of verbal meanings (*arthas*).
* `de`: Accompanying German documentation and methodology notes.

---

## 4. Diacritics and Font Standards

* **IAST Transliteration:** Rigorous adherence to standard Unicode code points:
  * Long vowels: `ā`, `ī`, `ū`
  * Vocalic liquids: `ṛ`, `ṝ`, `ḷ`, `ḹ`
  * Retroflex consonants: `ṭ`, `ḍ`, `ṇ`, `ṣ`
  * Palatal & velar stops/nasals: `ś`, `ñ`, `ṅ`
  * Anusvāra & Visarga: `ṃ`, `ḥ`
* **Punctuation:** Native Unicode Dandas (`।` = U+0964, `॥` = U+0965) and Avagraha (`ऽ` = U+093D) are used instead of ASCII vertical pipes or apostrophes.

---

## 5. Typographic Conventions in Typst

* **Two-Column Tabular Grid:**
  * Clean separation of columns with a subtle vertical line (`grid.vline(stroke: 0.4pt + luma(180))`).
  * Bold Devanāgarī root with pitch accents, followed by italicized IAST and English translation.
* **Marginal Concordance:**
  * Every dictionary page features outer-margin notes referencing the historical print page (`[p. 26]`).
* **Running Headers:**
  * Dynamic header labels generated from the active Gaṇa section.
