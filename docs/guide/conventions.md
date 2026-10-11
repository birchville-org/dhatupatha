# 📐 Konventionen & Technische Spezifikationen — dhatupatha

> Dieses Dokument definiert die Klassifikationsschemata, Sprach-Kennzeichnungen und typografischen Konventionen des Projekts `dhatupatha`.

---

## 1. Die 10 Gaṇas der Pāṇinīya-Tradition

Der Dhātupāṭha gliedert das gesamte Sanskrit-Verbalinventar in 10 kanonische Wurzelklassen (*gaṇas*):

| Nr. | Gaṇa-Name (IAST) | Gaṇa-Name (Devanāgarī) | Kennzeichnendes Merkmal |
| :--- | :--- | :--- | :--- |
| **1** | Bhvādigaṇaḥ | भ्वादिगणः | Thematische Klasse (*śap*-Infix, Guna) |
| **2** | Adādigaṇaḥ | अदादिगणः | Wurzelflexion ohne Klasseninfix (*luk*) |
| **3** | Juhotyādigaṇaḥ | जुहोत्यादिगणः | Reduplikation der Wurzel (*ślu*) |
| **4** | Divādigaṇaḥ | दिवादिगणः | *śyan*-Infix (-ya-) |
| **5** | Svādigaṇaḥ | स्वादिगणः | *śnu*-Infix (-no-/-nu-) |
| **6** | Tudādigaṇaḥ | तुदादिगणः | Thematisch ohne Guna (*śa*) |
| **7** | Rudhādigaṇaḥ | रुधादिगणः | Nasalinfix (*śnam*) |
| **8** | Tanādigaṇaḥ | तनादिगणः | *u*-Infix (*u*) |
| **9** | Kryādigaṇaḥ | क्र्यादिगणः | *śnā*-Infix (-nā-/-nī-) |
| **10** | Curādigaṇaḥ | चुरादिगणः | Kausativ-/Nennverb-Klasse (*ṇic*) |

---

## 2. Aupadeśika-Marker & It-Laute (Anubandhas)

In der Grammatik Pāṇinis werden Wurzeln in ihrer ursprünglichen Lehrform (*upadeśa*) mit diakritischen Hilfslauten (*it* bzw. *anubandha*) versehen, die grammatische Operationen steuern:
* **Präfixale It-Marker:** z. B. `टु` (bewirkt Suffix *-thu*), `डु` (bewirkt Kṛt-Bildungen), `इर्` (zeigt Aoristbildung an).
* **Suffixale It-Marker:** z. B. nasalisierte Vokale oder Konsonanten wie `ञ्` (kennzeichnet Ubhayapada), `ण्` (kennzeichnet Vṛddhi), `क्` (verhindert Guna/Vṛddhi).
* Im Datensatz werden sowohl die kanonische Bereinigungsform (`dhatu`) als auch die traditionelle Aupadeśika-Form (`aupadeshik`) lückenlos vorgehalten.

---

## 3. Sprachkennzeichnung (BCP 47)

* `sa` / `xml:lang="sa"`: Sanskrit-Text in Devanāgarī (z. B. `भू`, `सत्तायाम्`).
* `sa-Latn` / `xml:lang="sa-Latn"`: Sanskrit in wissenschaftlicher IAST-Transliteration (z. B. `bhū`, `sattāyām`).
* `en`: Englische Übersetzung der Wurzelbedeutungen (*arthas*).
* `de`: Begleitende Dokumentation und methodische Leitfäden.

---

## 4. Diakritika- und Schriftenstandard

* **IAST-Transliteration:** Konsequente Verwendung standardisierter Unicode-Punkte:
  * Vokallängen: `ā`, `ī`, `ū`
  * R- und L-Vokale: `ṛ`, `ṝ`, `ḷ`, `ḹ`
  * Retroflexe Konsonanten: `ṭ`, `ḍ`, `ṇ`, `ṣ`
  * Palatale & velare Laute: `ś`, `ñ`, `ṅ`
  * Anusvāra & Visarga: `ṃ`, `ḥ`
* **Satzzeichen:** Verwendung von Unicode-Dandas (`।` = U+0964, `॥` = U+0965) und Avagraha (`ऽ` = U+093D) anstelle von lateinischen Pipes oder Apostrophen.

---

## 5. Typografische Satzkonventionen in Typst

* **Zweispaltiges Tabellengitter:**
  * Trennung der linken und rechten Spalte über eine feine vertikale Haarlinie (`grid.vline(stroke: 0.4pt + luma(180))`).
  * Fette Devanāgarī-Wurzel mit Akzenten, gefolgt von kursivem IAST und englischer Übersetzung.
* **Marginal-Konkordanz:**
  * Jede Seite des Wörterbuchteils weist Marginalien mit der entsprechenden Seitenzahl des historischen Drucks auf (`[S. 26]`).
* **Lebende Kolumnentitel:**
  * Dynamische Kopfzeilen auf Basis des aktuellen Gaṇa-Abschnitts.
