#!/usr/bin/env python3
"""
scripts/generate_vitepress_dict.py

Generates VitePress dictionary markdown pages from data/dhatupatha_complete.json.
Follows the Heritage Dictionnaire & Birchville Scholarly Synthesis pattern:
- 10 structured Gaṇa pages (docs/gana/01-bhvadi.md to 10-curadi.md)
- Rich semantic entries with Devanāgarī, IAST, Aupadeśika citation, meanings,
  grammatical badges (pada, settva, karma), and historical scan pagination.
"""
import html
import json
import os
import sys
from pathlib import Path

GANA_METADATA = {
    1: {
        "slug": "01-bhvadi",
        "title": "1. Bhvādigaṇaḥ (भ्वादिगणः)",
        "iast": "Bhvādigaṇaḥ",
        "deva": "भ्वादिगणः",
        "desc": "Thematische Klasse mit śap-Infix (-a-) und Guṇa-Steigerung des Wurzelvokals.",
        "example": "भू (bhū) → भवति (bhavati)"
    },
    2: {
        "slug": "02-adadi",
        "title": "2. Adādigaṇaḥ (अदादिगणः)",
        "iast": "Adādigaṇaḥ",
        "deva": "अदादिगणः",
        "desc": "Wurzelflexion ohne Klasseninfix (luk); Endungen treten direkt an die Wurzel.",
        "example": "अद् (ad) → अत्ति (atti)"
    },
    3: {
        "slug": "03-juhotyadi",
        "title": "3. Juhotyādigaṇaḥ (जुहोत्यादिगणः)",
        "iast": "Juhotyādigaṇaḥ",
        "deva": "जुहोत्यादिगणः",
        "desc": "Reduplikationsklasse mit ślu-Schwund des Infixes und Stammverdopplung.",
        "example": "हु (hu) → जुहोति (juhoti)"
    },
    4: {
        "slug": "04-divadi",
        "title": "4. Divādigaṇaḥ (दिवादिगणः)",
        "iast": "Divādigaṇaḥ",
        "deva": "दिवादिगणः",
        "desc": "Thematische Klasse mit śyan-Infix (-ya-) ohne Guṇa-Steigerung.",
        "example": "दिव् (div) → दीव्यति (dīvyati)"
    },
    5: {
        "slug": "05-svadi",
        "title": "5. Svādigaṇaḥ (स्वादिगणः)",
        "iast": "Svādigaṇaḥ",
        "deva": "स्वादिगणः",
        "desc": "Klasse mit śnu-Infix (-no-/-nu-); starker Stamm auf -no-, schwacher auf -nu-.",
        "example": "सु (su) → सुनोति (sunoti)"
    },
    6: {
        "slug": "06-tudadi",
        "title": "6. Tudādigaṇaḥ (तुदादिगणः)",
        "iast": "Tudādigaṇaḥ",
        "deva": "तुदादिगणः",
        "desc": "Thematische Klasse mit śa-Infix (-a-) ohne Guṇa-Steigerung.",
        "example": "तुद् (tud) → तुदति (tudati)"
    },
    7: {
        "slug": "07-rudhadi",
        "title": "7. Rudhādigaṇaḥ (रुधादिगणः)",
        "iast": "Rudhādigaṇaḥ",
        "deva": "रुधादिगणः",
        "desc": "Nasal-Infix-Klasse (śnam); nasaler Laut wird in die Wurzel eingeschoben.",
        "example": "रुध् (rudh) → रुणद्धि (ruṇaddhi)"
    },
    8: {
        "slug": "08-tanadi",
        "title": "8. Tanādigaṇaḥ (तनादिगणः)",
        "iast": "Tanādigaṇaḥ",
        "deva": "तनादिगणः",
        "desc": "Klasse mit u-Infix (-o-/-u-).",
        "example": "तन् (tan) → तनोति (tanoti)"
    },
    9: {
        "slug": "09-kryadi",
        "title": "9. Kryādigaṇaḥ (क्र्यादिगणः)",
        "iast": "Kryādigaṇaḥ",
        "deva": "क्र्यादिगणः",
        "desc": "Klasse mit śnā-Infix (-nā-/-nī-).",
        "example": "क्री (krī) → क्रीणाति (krīṇāti)"
    },
    10: {
        "slug": "10-curadi",
        "title": "10. Curādigaṇaḥ (चुरादिगणः)",
        "iast": "Curādigaṇaḥ",
        "deva": "चुरादिगणः",
        "desc": "Kausativ- und Nennverbklasse mit ṇic-Infix (-aya-) und obligatorischer Stammsteigerung.",
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
    lines.append('  <div class="skt-header-line">')
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
    lines.append('  </div>')
    
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
        # Format tags cleanly
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


def main():
    root = Path(__file__).resolve().parent.parent
    json_path = root / "data" / "dhatupatha_complete.json"
    gana_dir = root / "docs" / "gana"
    gana_dir.mkdir(parents=True, exist_ok=True)
    
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
        
    for g_num in range(1, 11):
        g_entries = by_gana.get(g_num, [])
        meta = GANA_METADATA.get(g_num, {
            "slug": f"{g_num:02d}-gana",
            "title": f"Gaṇa {g_num}",
            "iast": f"Gaṇa {g_num}",
            "deva": "",
            "desc": "",
            "example": ""
        })
        
        md_file = gana_dir / f"{meta['slug']}.md"
        print(f"Generating {md_file.name} ({len(g_entries)} roots)...")
        
        content = []
        content.append("---")
        content.append(f'title: "{meta["title"]} — Dhātupāṭha"')
        content.append(f'description: "{meta["desc"]} ({len(g_entries)} Wurzeln)"')
        content.append("outline: [2, 3]")
        content.append("---\n")
        
        content.append(f'# <span class="deva-large">{meta["deva"]}</span> <span class="iast-large">{meta["iast"]}</span>\n')
        
        content.append('<div class="dict-page-header">')
        content.append(f'  <span class="badge-count">{len(g_entries)} Wurzeln ({meta["slug"].split("-")[1]})</span>')
        content.append('  <div class="header-nav-links">')
        if g_num > 1:
            prev_slug = GANA_METADATA[g_num - 1]["slug"]
            content.append(f'    <a href="./{prev_slug}" class="nav-prev">← Vorheriger Gaṇa</a>')
        if g_num < 10:
            next_slug = GANA_METADATA[g_num + 1]["slug"]
            content.append(f'    <a href="./{next_slug}" class="nav-next">Nächster Gaṇa →</a>')
        content.append('  </div>')
        content.append('</div>\n')
        
        content.append(f'> **Charakteristik:** {meta["desc"]}  \n> **Musterbildung:** `{meta["example"]}`\n')
        content.append('---\n')
        
        # Render entries
        for entry in g_entries:
            content.append(generate_entry_html(entry))
            
        with open(md_file, "w", encoding="utf-8") as out:
            out.write("\n".join(content))
            
    print("All 10 Gana pages generated successfully.")


if __name__ == "__main__":
    main()
