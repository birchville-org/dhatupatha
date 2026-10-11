import { defineConfig } from 'vitepress'

const base = process.env.GITHUB_ACTIONS ? '/dhatupatha/' : '/'

export default defineConfig({
  base,
  title: "Pāṇinīya-Dhātupāṭha",
  description: "Kanonische Neuedition aller 2.259 Sanskrit-Verbalwurzeln nach dem Böhtlingk-Standard mit interaktivem Lexikon und Typst-Vektorsatz",
  lang: 'de-CH',
  head: [
    ['meta', { name: 'google', content: 'notranslate' }],
    ['link', { rel: 'icon', href: `${base}birchville_logo.png` }],
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
  themeConfig: {
    logo: '/birchville_logo.png',
    siteTitle: 'Dhātupāṭha',
    search: {
      provider: 'local',
      options: {
        detailedView: true,
        miniSearch: {
          searchOptions: {
            fuzzy: 0.2,
            prefix: true,
            boost: {
              title: 4,
              text: 1
            }
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
          }
        }
      }
    },
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
    }
  }
})
