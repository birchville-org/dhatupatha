import { defineConfig } from 'vitepress'

const base = process.env.GITHUB_ACTIONS ? '/dhatupatha/' : '/'

function toAscii(str) {
  if (!str) return ''
  return str
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .replace(/ṃ/g, 'm')
    .replace(/ḥ/g, 'h')
    .replace(/ś/g, 's')
    .replace(/ṣ/g, 's')
    .replace(/ṛ/g, 'r')
    .replace(/ṝ/g, 'r')
    .replace(/ḷ/g, 'l')
    .replace(/ñ/g, 'n')
    .replace(/ṅ/g, 'n')
    .replace(/ṇ/g, 'n')
    .replace(/ṭ/g, 't')
    .replace(/ḍ/g, 'd')
}

function clearHtml(str) {
  return (str || '').replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim()
}

function* splitGanaPage(html) {
  const entryRegex = /<div class="skt-entry" id="entry-([^"]+)">([\s\S]*?)(?=<div class="skt-entry"|$)/g
  const h1Match = html.match(/<h1[^>]*>([\s\S]*?)<\/h1>/i)
  const ganaTitle = h1Match ? clearHtml(h1Match[1]).replace(/​/g, '').trim() : 'Dhātupāṭha'

  const firstEntryIdx = html.indexOf('<div class="skt-entry"')
  if (firstEntryIdx > 0) {
    const introText = clearHtml(html.slice(0, firstEntryIdx)).replace(/​/g, '').trim()
    if (introText) {
      yield {
        anchor: '',
        titles: [ganaTitle, ganaTitle],
        text: introText
      }
    }
  }

  let match
  while ((match = entryRegex.exec(html)) !== null) {
    const eid = match[1]
    const block = match[2]

    const devaMatch = block.match(/<span class="deva"[^>]*>([\s\S]*?)<\/span>/i)
    const iastMatch = block.match(/<span class="iast"[^>]*>([\s\S]*?)<\/span>/i)
    const dhatu = devaMatch ? clearHtml(devaMatch[1]) : ''
    const iast = iastMatch ? clearHtml(iastMatch[1]) : ''

    const entryTitle = (dhatu ? `${dhatu} (${iast})` : iast) + ` #${eid}`
    const rawText = clearHtml(block).replace(/​/g, '').trim()
    const asciiText = toAscii(rawText)
    const text = `${rawText} ${asciiText} ${eid}`

    yield {
      anchor: `entry-${eid}`,
      titles: [ganaTitle, entryTitle],
      text
    }
  }
}

export default defineConfig({
  base,
  title: "Pāṇinīya-Dhātupāṭha",
  description: "Kanonische Neuedition aller 2.259 Sanskrit-Verbalwurzeln nach dem Böhtlingk-Standard mit interaktivem Lexikon und Typst-Vektorsatz",
  head: [
    ['meta', { name: 'google', content: 'notranslate' }],
    ['link', { rel: 'icon', href: `${base}birchville_logo.png` }],
    ['link', { rel: 'apple-touch-icon', href: `${base}og-icon.png` }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:image', content: 'https://birchville-org.github.io/dhatupatha/og-icon.png' }],
    ['meta', { property: 'og:image:width', content: '128' }],
    ['meta', { property: 'og:image:height', content: '128' }],
    ['meta', { name: 'twitter:card', content: 'summary' }],
    ['meta', { name: 'twitter:image', content: 'https://birchville-org.github.io/dhatupatha/og-icon.png' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.googleapis.com' }],
    ['link', { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: '' }],
    ['link', { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Serif+Devanagari:wght@400;600;700&display=swap' }]
  ],
  transformPageData(pageData) {
    if (pageData.frontmatter?.hero?.actions) {
      for (const action of pageData.frontmatter.hero.actions) {
        if (action.link && action.link.endsWith('.pdf')) {
          if (base !== '/' && !action.link.startsWith(base)) {
            action.link = `${base}${action.link.replace(/^\//, '')}`
          }
        }
      }
    }
  },
  transformHtml(code) {
    code = code.replace('<html', '<html translate="no" class="notranslate"')
    if (base !== '/') {
      code = code.replaceAll('href="/Dhatu-patha.typeset_edition.pdf"', `href="${base}Dhatu-patha.typeset_edition.pdf"`)
      code = code.replaceAll('href="/birchville_logo.png"', `href="${base}birchville_logo.png"`)
    }
    return code
  },
  locales: {
    root: {
      label: 'Deutsch',
      lang: 'de-CH',
      title: "Pāṇinīya-Dhātupāṭha",
      description: "Kanonische Neuedition aller 2.259 Sanskrit-Verbalwurzeln nach dem Böhtlingk-Standard mit interaktivem Lexikon und Typst-Vektorsatz",
      themeConfig: {
        nav: [
          { text: 'Startseite', link: '/' },
          { text: '10 Gaṇas (2.259 Wurzeln)', link: '/gana/01-bhvadi' },
          { text: 'Dokumentation', link: '/guide/case-study' },
          { text: '📥 Typst-Buchausgabe (PDF)', link: '/Dhatu-patha.typeset_edition.pdf', target: '_blank' },
          { text: 'GitHub', link: 'https://github.com/birchville-org/dhatupatha' }
        ],
        sidebar: {
          '/gana/': [
            {
              text: 'Die 10 Gaṇas (Wurzelklassen)',
              collapsed: false,
              items: [
                { text: '1. Bhvādigaṇaḥ (1.166 Wurzeln)', link: '/gana/01-bhvadi' },
                { text: '2. Adādigaṇaḥ (77 Wurzeln)', link: '/gana/02-adadi' },
                { text: '3. Juhotyādigaṇaḥ (26 Wurzeln)', link: '/gana/03-juhotyadi' },
                { text: '4. Divādigaṇaḥ (163 Wurzeln)', link: '/gana/04-divadi' },
                { text: '5. Svādigaṇaḥ (38 Wurzeln)', link: '/gana/05-svadi' },
                { text: '6. Tudādigaṇaḥ (174 Wurzeln)', link: '/gana/06-tudadi' },
                { text: '7. Rudhādigaṇaḥ (25 Wurzeln)', link: '/gana/07-rudhadi' },
                { text: '8. Tanādigaṇaḥ (10 Wurzeln)', link: '/gana/08-tanadi' },
                { text: '9. Kryādigaṇaḥ (71 Wurzeln)', link: '/gana/09-kryadi' },
                { text: '10. Curādigaṇaḥ (509 Wurzeln)', link: '/gana/10-curadi' }
              ]
            },
            {
              text: 'Wissenschaftliche Dokumentation',
              collapsed: true,
              items: [
                { text: 'Fallstudie & Architektur', link: '/guide/case-study' },
                { text: 'QA- & Korrektur-Workflow', link: '/guide/qa-workflow' },
                { text: 'Datenarchitektur & 4-Säulen-Modell', link: '/guide/data-architecture' },
                { text: 'Konventionen & Spezifikationen', link: '/guide/conventions' },
                { text: 'Urheberrecht & Provenienz', link: '/guide/copyright-and-provenance' }
              ]
            }
          ],
          '/guide/': [
            {
              text: 'Wissenschaftliche Dokumentation',
              collapsed: false,
              items: [
                { text: 'Fallstudie & Architektur', link: '/guide/case-study' },
                { text: 'QA- & Korrektur-Workflow', link: '/guide/qa-workflow' },
                { text: 'Datenarchitektur & 4-Säulen-Modell', link: '/guide/data-architecture' },
                { text: 'Konventionen & Spezifikationen', link: '/guide/conventions' },
                { text: 'Urheberrecht & Provenienz', link: '/guide/copyright-and-provenance' }
              ]
            },
            {
              text: 'Die 10 Gaṇas (Lexikon)',
              collapsed: true,
              items: [
                { text: '1. Bhvādigaṇaḥ (1.166)', link: '/gana/01-bhvadi' },
                { text: '2. Adādigaṇaḥ (77)', link: '/gana/02-adadi' },
                { text: '3. Juhotyādigaṇaḥ (26)', link: '/gana/03-juhotyadi' },
                { text: '4. Divādigaṇaḥ (163)', link: '/gana/04-divadi' },
                { text: '5. Svādigaṇaḥ (38)', link: '/gana/05-svadi' },
                { text: '6. Tudādigaṇaḥ (174)', link: '/gana/06-tudadi' },
                { text: '7. Rudhādigaṇaḥ (25)', link: '/gana/07-rudhadi' },
                { text: '8. Tanādigaṇaḥ (10)', link: '/gana/08-tanadi' },
                { text: '9. Kryādigaṇaḥ (71)', link: '/gana/09-kryadi' },
                { text: '10. Curādigaṇaḥ (509)', link: '/gana/10-curadi' }
              ]
            }
          ]
        },
        footer: {
          message: 'Kanonische digitale Neuedition nach dem Böhtlingk-Standard · Birchville Scholarly Synthesis',
          copyright: 'Public Domain (Kanon) / MIT Lizenz (Pipeline & Typst-Satz)'
        },
        darkModeSwitchLabel: 'Erscheinungsbild',
        lightModeSwitchTitle: 'Zum hellen Design wechseln',
        darkModeSwitchTitle: 'Zum dunklen Design wechseln',
        sidebarMenuLabel: 'Menü',
        returnToTopLabel: 'Zurück nach oben',
        langMenuLabel: 'Sprache'
      }
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      title: "Pāṇinīya-Dhātupāṭha",
      description: "Canonical digital edition of all 2,259 Sanskrit verbal roots according to the Böhtlingk standard with interactive lexicon and Typst vector typesetting",
      themeConfig: {
        nav: [
          { text: 'Home', link: '/en/' },
          { text: '10 Gaṇas (2,259 Roots)', link: '/en/gana/01-bhvadi' },
          { text: 'Documentation', link: '/en/guide/case-study' },
          { text: '📥 Typst Book Edition (PDF)', link: '/Dhatu-patha.typeset_edition.pdf', target: '_blank' },
          { text: 'GitHub', link: 'https://github.com/birchville-org/dhatupatha' }
        ],
        sidebar: {
          '/en/gana/': [
            {
              text: 'The 10 Gaṇas (Root Classes)',
              collapsed: false,
              items: [
                { text: '1. Bhvādigaṇaḥ (1,166 roots)', link: '/en/gana/01-bhvadi' },
                { text: '2. Adādigaṇaḥ (77 roots)', link: '/en/gana/02-adadi' },
                { text: '3. Juhotyādigaṇaḥ (26 roots)', link: '/en/gana/03-juhotyadi' },
                { text: '4. Divādigaṇaḥ (163 roots)', link: '/en/gana/04-divadi' },
                { text: '5. Svādigaṇaḥ (38 roots)', link: '/en/gana/05-svadi' },
                { text: '6. Tudādigaṇaḥ (174 roots)', link: '/en/gana/06-tudadi' },
                { text: '7. Rudhādigaṇaḥ (25 roots)', link: '/en/gana/07-rudhadi' },
                { text: '8. Tanādigaṇaḥ (10 roots)', link: '/en/gana/08-tanadi' },
                { text: '9. Kryādigaṇaḥ (71 roots)', link: '/en/gana/09-kryadi' },
                { text: '10. Curādigaṇaḥ (509 roots)', link: '/en/gana/10-curadi' }
              ]
            },
            {
              text: 'Scholarly Documentation',
              collapsed: true,
              items: [
                { text: 'Case Study & Architecture', link: '/en/guide/case-study' },
                { text: 'QA & Proofreading Workflow', link: '/en/guide/qa-workflow' },
                { text: 'Data Architecture & 4-Pillar Model', link: '/en/guide/data-architecture' },
                { text: 'Conventions & Specifications', link: '/en/guide/conventions' },
                { text: 'Copyright & Provenance', link: '/en/guide/copyright-and-provenance' }
              ]
            }
          ],
          '/en/guide/': [
            {
              text: 'Scholarly Documentation',
              collapsed: false,
              items: [
                { text: 'Case Study & Architecture', link: '/en/guide/case-study' },
                { text: 'QA & Proofreading Workflow', link: '/en/guide/qa-workflow' },
                { text: 'Data Architecture & 4-Pillar Model', link: '/en/guide/data-architecture' },
                { text: 'Conventions & Specifications', link: '/en/guide/conventions' },
                { text: 'Copyright & Provenance', link: '/en/guide/copyright-and-provenance' }
              ]
            },
            {
              text: 'The 10 Gaṇas (Lexicon)',
              collapsed: true,
              items: [
                { text: '1. Bhvādigaṇaḥ (1,166)', link: '/en/gana/01-bhvadi' },
                { text: '2. Adādigaṇaḥ (77)', link: '/en/gana/02-adadi' },
                { text: '3. Juhotyādigaṇaḥ (26)', link: '/en/gana/03-juhotyadi' },
                { text: '4. Divādigaṇaḥ (163)', link: '/en/gana/04-divadi' },
                { text: '5. Svādigaṇaḥ (38)', link: '/en/gana/05-svadi' },
                { text: '6. Tudādigaṇaḥ (174)', link: '/en/gana/06-tudadi' },
                { text: '7. Rudhādigaṇaḥ (25)', link: '/en/gana/07-rudhadi' },
                { text: '8. Tanādigaṇaḥ (10)', link: '/en/gana/08-tanadi' },
                { text: '9. Kryādigaṇaḥ (71)', link: '/en/gana/09-kryadi' },
                { text: '10. Curādigaṇaḥ (509)', link: '/en/gana/10-curadi' }
              ]
            }
          ]
        },
        footer: {
          message: 'Canonical digital edition according to the Böhtlingk standard · Birchville Scholarly Synthesis',
          copyright: 'Public Domain (Canon) / MIT License (Pipeline & Typst Typesetting)'
        },
        darkModeSwitchLabel: 'Appearance',
        lightModeSwitchTitle: 'Switch to light theme',
        darkModeSwitchTitle: 'Switch to dark theme',
        sidebarMenuLabel: 'Menu',
        returnToTopLabel: 'Return to top',
        langMenuLabel: 'Language'
      }
    }
  },
  themeConfig: {
    logo: '/birchville_logo.png',
    siteTitle: 'Dhātupāṭha',
    search: {
      provider: 'local',
      options: {
        detailedView: true,
        miniSearch: {
          searchOptions: {
            fuzzy(term) {
              return term.length > 4 ? 0.2 : false
            },
            prefix: true,
            boost: {
              title: 4,
              text: 1
            },
            combineWith: 'AND'
          },
          _splitIntoSections(file, html) {
            if (!file.includes('/gana/') && !file.includes('\\gana\\')) {
              return null
            }
            return splitGanaPage(html)
          }
        },
        locales: {
          root: {
            translations: {
              button: {
                buttonText: 'Suchen',
                buttonAriaLabel: 'In den 2.259 Wurzeln suchen (⌘K)'
              },
              modal: {
                displayDetails: 'Details anzeigen',
                resetButtonTitle: 'Suche zurücksetzen',
                backButtonTitle: 'Suche schließen',
                noResultsText: 'Keine Ergebnisse für',
                footer: {
                  selectText: 'zum Auswählen',
                  selectKeyAriaLabel: 'Eingabe',
                  navigateText: 'zum Navigieren',
                  navigateUpKeyAriaLabel: 'Pfeil hoch',
                  navigateDownKeyAriaLabel: 'Pfeil runter',
                  closeText: 'zum Schließen',
                  closeKeyAriaLabel: 'Esc'
                }
              }
            }
          },
          en: {
            translations: {
              button: {
                buttonText: 'Search',
                buttonAriaLabel: 'Search across 2,259 roots (⌘K)'
              },
              modal: {
                displayDetails: 'Display detailed list',
                resetButtonTitle: 'Reset search',
                backButtonTitle: 'Close search',
                noResultsText: 'No results for',
                footer: {
                  selectText: 'to select',
                  selectKeyAriaLabel: 'Enter',
                  navigateText: 'to navigate',
                  navigateUpKeyAriaLabel: 'Arrow up',
                  navigateDownKeyAriaLabel: 'Arrow down',
                  closeText: 'to close',
                  closeKeyAriaLabel: 'Esc'
                }
              }
            }
          }
        }
      }
    }
  }
})
