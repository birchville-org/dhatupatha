#!/usr/bin/env python3
"""
scripts/generate_vitepress_dict.py

Generates VitePress dictionary markdown pages from data/dhatupatha_complete.json.
Supports bilingual structure:
- German: docs/gana/01-bhvadi.md ... 10-curadi.md
- English: docs/en/gana/01-bhvadi.md ... 10-curadi.md
Each page contains rich semantic root entries with Devanāgarī, IAST, Aupadeśika citation,
meanings, grammatical badges (pada, settva, karma), and historical scan pagination.
"""
import html
import json
import os
import sys
from pathlib import Path

GANA_METADATA = {
    1: {
        "slug": "01-bhvadi",
        "title_de": "1. Bhvādigaṇaḥ (भ्वादिगणः)",
        "title_en": "1. Bhvādigaṇaḥ (भ्वादिगणः)",
        "iast": "Bhvādigaṇaḥ",
        "deva": "भ्वादिगणः",
        "desc_de": "Thematische Klasse mit śap-Infix (-a-) und Guṇa-Steigerung des Wurzelvokals.",
        "desc_en": "Thematic class with śap infix (-a-) and Guṇa strengthening of the root vowel.",
        "example": "भू (bhū) → भवति (bhavati)"
    },
    2: {
        "slug": "02-adadi",
        "title_de": "2. Adādigaṇaḥ (अदादिगणः)",
        "title_en": "2. Adādigaṇaḥ (अदादिगणः)",
        "iast": "Adādigaṇaḥ",
        "deva": "अदादिगणः",
        "desc_de": "Wurzelflexion ohne Klasseninfix (luk); Endungen treten direkt an die Wurzel.",
        "desc_en": "Root class without class infix (luk); endings attach directly to the root.",
        "example": "अद् (ad) → अत्ति (atti)"
    },
    3: {
        "slug": "03-juhotyadi",
        "title_de": "3. Juhotyādigaṇaḥ (जुहोत्यादिगणः)",
        "title_en": "3. Juhotyādigaṇaḥ (जुहोत्यादिगणः)",
        "iast": "Juhotyādigaṇaḥ",
        "deva": "जुहोत्यादिगणः",
        "desc_de": "Reduplikationsklasse mit ślu-Schwund des Infixes und Stammverdopplung.",
        "desc_en": "Reduplicating class with ślu elision of infix and stem reduplication.",
        "example": "हु (hu) → जुहोति (juhoti)"
    },
    4: {
        "slug": "04-divadi",
        "title_de": "4. Divādigaṇaḥ (दिवादिगणः)",
        "title_en": "4. Divādigaṇaḥ (दिवादिगणः)",
        "iast": "Divādigaṇaḥ",
        "deva": "दिवादिगणः",
        "desc_de": "Thematische Klasse mit śyan-Infix (-ya-) ohne Guṇa-Steigerung.",
        "desc_en": "Thematic class with śyan infix (-ya-) without Guṇa strengthening.",
        "example": "दिव् (div) → दीव्यति (dīvyati)"
    },
    5: {
        "slug": "05-svadi",
        "title_de": "5. Svādigaṇaḥ (स्वादिगणः)",
        "title_en": "5. Svādigaṇaḥ (स्वादिगणः)",
        "iast": "Svādigaṇaḥ",
        "deva": "स्वादिगणः",
        "desc_de": "Klasse mit śnu-Infix (-no-/-nu-); starker Stamm auf -no-, schwacher auf -nu-.",
        "desc_en": "Class with śnu infix (-no-/-nu-); strong stem in -no-, weak stem in -nu-.",
        "example": "सु (su) → सुनोति (sunoti)"
    },
    6: {
        "slug": "06-tudadi",
        "title_de": "6. Tudādigaṇaḥ (तुदादिगणः)",
        "title_en": "6. Tudādigaṇaḥ (तुदादिगणः)",
        "iast": "Tudādigaṇaḥ",
        "deva": "तुदादिगणः",
        "desc_de": "Thematische Klasse mit śa-Infix (-a-) ohne Guṇa-Steigerung.",
        "desc_en": "Thematic class with śa infix (-a-) without Guṇa strengthening.",
        "example": "तुद् (tud) → तुदति (tudati)"
    },
    7: {
        "slug": "07-rudhadi",
        "title_de": "7. Rudhādigaṇaḥ (रुधादिगणः)",
        "title_en": "7. Rudhādigaṇaḥ (रुधादिगणः)",
        "iast": "Rudhādigaṇaḥ",
        "deva": "रुधादिगणः",
        "desc_de": "Nasal-Infix-Klasse (śnam); nasaler Laut wird in die Wurzel eingeschoben.",
        "desc_en": "Nasal infix class (śnam); a nasal sound is inserted into the root.",
        "example": "रुध् (rudh) → रुणद्धि (ruṇaddhi)"
    },
    8: {
        "slug": "08-tanadi",
        "title_de": "8. Tanādigaṇaḥ (तनादिगणः)",
        "title_en": "8. Tanādigaṇaḥ (तनादिगणः)",
        "iast": "Tanādigaṇaḥ",
        "deva": "तनादिगणः",
        "desc_de": "Klasse mit u-Infix (-o-/-u-).",
        "desc_en": "Class with u infix (-o-/-u-).",
        "example": "तन् (tan) → तनोति (tanoti)"
    },
    9: {
        "slug": "09-kryadi",
        "title_de": "9. Kryādigaṇaḥ (क्र्यादिगणः)",
        "title_en": "9. Kryādigaṇaḥ (क्र्यादिगणः)",
        "iast": "Kryādigaṇaḥ",
        "deva": "क्र्यादिगणः",
        "desc_de": "Klasse mit śnā-Infix (-nā-/-nī-).",
        "desc_en": "Class with śnā infix (-nā-/-nī-).",
        "example": "क्री (krī) → क्रीणाति (krīṇāti)"
    },
    10: {
        "slug": "10-curadi",
        "title_de": "10. Curādigaṇaḥ (चुरादिगणः)",
        "title_en": "10. Curādigaṇaḥ (चुरादिगणः)",
        "iast": "Curādigaṇaḥ",
        "deva": "चुरादिगणः",
        "desc_de": "Kausativ- und Nennverbklasse mit ṇic-Infix (-aya-) und obligatorischer Stammsteigerung.",
        "desc_en": "Causative and denominative class with ṇic infix (-aya-) and obligatory stem strengthening.",
        "example": "चुर् (cur) → चोरयति (corayati)"
    }
}


def escape_html(text: str) -> str:
    if not text:
        return ""
    return html.escape(str(text))


def generate_entry_html(entry: dict) -> str:
    eid = escape_html(entry.get("id", ""))
    dhatu = escape_html(entry.get("dhatu", ""))
    iast_dhatu = escape_html(entry.get("iast_dhatu", ""))
    aupadeshik = escape_html(entry.get("aupadeshik", ""))
    iast_aup = escape_html(entry.get("iast_aupadeshik", ""))
    
    pada = escape_html(entry.get("pada", ""))
    settva = escape_html(entry.get("settva", ""))
    karma = escape_html(entry.get("karma", ""))
    
    artha = escape_html(entry.get("artha", ""))
    iast_artha = escape_html(entry.get("iast_artha", ""))
    artha_en = escape_html(entry.get("artha_english", ""))
    
    orig_page = entry.get("orig_page", "")
    comm = escape_html(entry.get("commentary_note", ""))
    tags = escape_html(entry.get("tags", ""))
    sk = escape_html(entry.get("sk_sutra", ""))
    
    lines = []
    lines.append(f'<div class="skt-entry" id="entry-{eid}">')
    lines.append(f'  <h3 class="skt-header-line" id="entry-{eid}-h">')
    lines.append(f'    <span class="deva" lang="sa">{dhatu}</span>')
    lines.append(f'    <span class="iast">{iast_dhatu}</span>')
    lines.append(f'    <span class="skt-id">#{eid}</span>')
    lines.append('    <div class="skt-badges">')
    if pada:
        lines.append(f'      <span class="badge badge-pada">{pada}</span>')
    if settva:
        lines.append(f'      <span class="badge badge-settva">{settva}</span>')
    if karma:
        lines.append(f'      <span class="badge badge-karma">{karma}</span>')
    if orig_page:
        lines.append(f'      <span class="badge badge-page" title="Historischer Druck Seite {orig_page}">S. {orig_page}</span>')
    lines.append('    </div>')
    lines.append(f'    <a class="header-anchor" href="#entry-{eid}">&#x200b;</a>')
    lines.append('  </h3>')
    
    lines.append('  <div class="skt-body">')
    lines.append('    <div class="skt-meaning">')
    if artha:
        lines.append(f'      <span class="deva-artha" lang="sa">{artha}</span>')
    if iast_artha:
        lines.append(f'      <span class="iast-artha">({iast_artha})</span>')
    if artha_en:
        lines.append(f'      <span class="en-artha">— {artha_en}</span>')
    lines.append('    </div>')
    
    # Meta row (Aupadeśika, SK, Tags)
    meta_parts = []
    if aupadeshik and (aupadeshik != dhatu or iast_aup != iast_dhatu):
        meta_parts.append(f'<span class="meta-item"><span class="meta-label">Aupadeśika:</span> <span class="deva" lang="sa">{aupadeshik}</span> ({iast_aup})</span>')
    elif aupadeshik:
        meta_parts.append(f'<span class="meta-item"><span class="meta-label">Upadeśa:</span> <span class="deva" lang="sa">{aupadeshik}</span></span>')
        
    if sk:
        meta_parts.append(f'<span class="meta-item"><span class="meta-label">SK:</span> {sk}</span>')
    if tags:
        clean_tags = " · ".join(t.strip() for t in tags.split(",") if t.strip())
        if clean_tags:
            meta_parts.append(f'<span class="meta-item meta-tags">{clean_tags}</span>')
            
    if meta_parts:
        lines.append(f'    <div class="skt-meta">{" ".join(meta_parts)}</div>')
        
    if comm:
        lines.append(f'    <div class="skt-commentary"><span class="comm-label">Kommentar:</span> {comm}</div>')
        
    lines.append('  </div>')
    lines.append('</div>\n')
    return "\n".join(lines)


def generate_pages_for_lang(entries_by_gana: dict, output_dir: Path, is_en: bool = False):
    output_dir.mkdir(parents=True, exist_ok=True)
    lang_code = "en" if is_en else "de"
    prev_label = "← Previous Gaṇa" if is_en else "← Vorheriger Gaṇa"
    next_label = "Next Gaṇa →" if is_en else "Nächster Gaṇa →"
    roots_label = "roots" if is_en else "Wurzeln"
    char_label = "Characteristics:" if is_en else "Charakteristik:"
    example_label = "Paradigm formation:" if is_en else "Musterbildung:"
    
    for g_num in range(1, 11):
        g_entries = entries_by_gana.get(g_num, [])
        meta = GANA_METADATA[g_num]
        title = meta["title_en"] if is_en else meta["title_de"]
        desc = meta["desc_en"] if is_en else meta["desc_de"]
        
        md_file = output_dir / f"{meta['slug']}.md"
        
        content = []
        content.append("---")
        content.append(f'title: "{title} — Dhātupāṭha"')
        content.append(f'description: "{desc} ({len(g_entries)} {roots_label})"')
        content.append("outline: false")
        content.append("---\n")
        
        content.append(f'# <span class="deva-large">{meta["deva"]}</span> <span class="iast-large">{meta["iast"]}</span>\n')
        
        content.append('<div class="dict-page-header">')
        content.append(f'  <span class="badge-count">{len(g_entries)} {roots_label}</span>')
        content.append('  <div class="header-nav-links">')
        if g_num > 1:
            prev_slug = GANA_METADATA[g_num - 1]["slug"]
            content.append(f'    <a href="./{prev_slug}" class="nav-prev">{prev_label}</a>')
        if g_num < 10:
            next_slug = GANA_METADATA[g_num + 1]["slug"]
            content.append(f'    <a href="./{next_slug}" class="nav-next">{next_label}</a>')
        content.append('  </div>')
        content.append('</div>\n')
        
        content.append(f'> **{char_label}** {desc}  \n> **{example_label}** `{meta["example"]}`\n')
        content.append('---\n')
        
        for entry in g_entries:
            content.append(generate_entry_html(entry))
            
        with open(md_file, "w", encoding="utf-8") as out:
            out.write("\n".join(content))


def main():
    root = Path(__file__).resolve().parent.parent
    json_path = root / "data" / "dhatupatha_complete.json"
    
    print(f"Loading complete dataset from {json_path}...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    entries = data.get("entries", [])
    print(f"Loaded {len(entries)} entries.")
    
    # Group by Gana
    by_gana = {}
    for e in entries:
        g = e.get("gana", 1)
        by_gana.setdefault(g, []).append(e)
        
    print("Generating German Gaṇa pages (docs/gana/)...")
    generate_pages_for_lang(by_gana, root / "docs" / "gana", is_en=False)
    
    print("Generating English Gaṇa pages (docs/en/gana/)...")
    generate_pages_for_lang(by_gana, root / "docs" / "en" / "gana", is_en=True)
    
    print("All bilingual Gaṇa pages generated successfully.")


if __name__ == "__main__":
    main()
