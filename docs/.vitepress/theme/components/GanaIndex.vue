<script setup>
import { computed } from 'vue'
import { withBase, useData } from 'vitepress'

const { site, lang } = useData()

const isEn = computed(() => lang.value === 'en-US')

function getUrl(slug) {
  const ext = site.value.cleanUrls ? '' : '.html'
  const prefix = isEn.value ? '/en' : ''
  return withBase(`${prefix}/gana/${slug}${ext}`)
}

const ganas = computed(() => [
  {
    num: 1,
    slug: '01-bhvadi',
    deva: 'भ्वादिगणः',
    iast: '1. Bhvādigaṇaḥ',
    count: 1166,
    desc: isEn.value ? 'Thematic class (śap, Guṇa)' : 'Thematisch (śap, Guṇa)',
    example: 'भू → भवति'
  },
  {
    num: 2,
    slug: '02-adadi',
    deva: 'अदादिगणः',
    iast: '2. Adādigaṇaḥ',
    count: 77,
    desc: isEn.value ? 'Athematic root inflection (luk)' : 'Athematisch wurzelflektierend (luk)',
    example: 'अद् → अत्ति'
  },
  {
    num: 3,
    slug: '03-juhotyadi',
    deva: 'जुहोत्यादिगणः',
    iast: '3. Juhotyādigaṇaḥ',
    count: 26,
    desc: isEn.value ? 'Reduplication (ślu)' : 'Reduplikation (ślu)',
    example: 'हु → जुहोति'
  },
  {
    num: 4,
    slug: '04-divadi',
    deva: 'दिवादिगणः',
    iast: '4. Divādigaṇaḥ',
    count: 163,
    desc: isEn.value ? 'Thematic class (śyan, -ya-)' : 'Thematisch (śyan, -ya-)',
    example: 'दिव् → दीव्यति'
  },
  {
    num: 5,
    slug: '05-svadi',
    deva: 'स्वादिगणः',
    iast: '5. Svādigaṇaḥ',
    count: 38,
    desc: isEn.value ? 'Infix class (śnu, -no-/-nu-)' : 'Infix (śnu, -no-/-nu-)',
    example: 'सु → सुनोति'
  },
  {
    num: 6,
    slug: '06-tudadi',
    deva: 'तुदादिगणः',
    iast: '6. Tudādigaṇaḥ',
    count: 174,
    desc: isEn.value ? 'Thematic without Guṇa (śa)' : 'Thematisch ohne Guṇa (śa)',
    example: 'तुद् → तुदति'
  },
  {
    num: 7,
    slug: '07-rudhadi',
    deva: 'रुधादिगणः',
    iast: '7. Rudhādigaṇaḥ',
    count: 25,
    desc: isEn.value ? 'Nasal infix (śnam, -na-/-n-)' : 'Nasalinfix (śnam, -na-/-n-)',
    example: 'रुध् → रुणद्धि'
  },
  {
    num: 8,
    slug: '08-tanadi',
    deva: 'तनादिगणः',
    iast: '8. Tanādigaṇaḥ',
    count: 10,
    desc: isEn.value ? 'Infix class (u, -o-/-u-)' : 'Infix (u, -o-/-u-)',
    example: 'तन् → तनोति'
  },
  {
    num: 9,
    slug: '09-kryadi',
    deva: 'क्र्यादिगणः',
    iast: '9. Kryādigaṇaḥ',
    count: 71,
    desc: isEn.value ? 'Infix class (śnā, -nā-/-nī-)' : 'Infix (śnā, -nā-/-nī-)',
    example: 'क्री → क्रीणाति'
  },
  {
    num: 10,
    slug: '10-curadi',
    deva: 'चुरादिगणः',
    iast: '10. Curādigaṇaḥ',
    count: 509,
    desc: isEn.value ? 'Causative / Denominative (ṇic, -aya-)' : 'Kausativ/Nennverb (ṇic, -aya-)',
    example: 'चुर् → चोरयति'
  }
])
</script>

<template>
  <div class="gana-grid-container">
    <div class="gana-grid">
      <a
        v-for="g in ganas"
        :key="g.slug"
        :href="getUrl(g.slug)"
        class="gana-card"
      >
        <div class="card-top">
          <span class="card-num">Gaṇa {{ g.num }}</span>
          <span class="card-count">{{ g.count.toLocaleString(isEn ? 'en-US' : 'de-CH') }} {{ isEn ? 'roots' : 'Wurzeln' }}</span>
        </div>
        <div class="card-deva">{{ g.deva }}</div>
        <div class="card-iast">{{ g.iast }}</div>
        <div class="card-desc">{{ g.desc }}</div>
        <div class="card-example"><code>{{ g.example }}</code></div>
      </a>
    </div>
  </div>
</template>

<style scoped>
.gana-grid-container {
  margin: 1.5rem 0 3rem 0;
}

.gana-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 16px;
}

.gana-card {
  display: flex;
  flex-direction: column;
  padding: 16px 18px;
  background-color: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-border);
  border-radius: 10px;
  text-decoration: none;
  transition: all 0.2s ease;
}

.gana-card:hover {
  border-color: var(--vp-c-brand-1);
  background-color: var(--vp-c-brand-soft);
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.06);
}

.card-top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 6px;
}

.card-num {
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--vp-c-brand-1);
}

.card-count {
  font-size: 0.78rem;
  font-weight: 600;
  padding: 2px 8px;
  border-radius: 12px;
  background: var(--vp-c-brand-soft);
  color: var(--vp-c-brand-1);
}

.card-deva {
  font-family: var(--skt-deva-font);
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  line-height: 1.2;
}

.card-iast {
  font-size: 1rem;
  font-weight: 600;
  color: var(--vp-c-brand-1);
  margin-top: 2px;
}

.card-desc {
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
  margin-top: 8px;
  line-height: 1.4;
  flex-grow: 1;
}

.card-example {
  margin-top: 10px;
  padding-top: 8px;
  border-top: 1px dashed var(--vp-c-divider);
  font-size: 0.8rem;
}

.card-example code {
  font-family: var(--skt-deva-font), monospace;
  background: transparent;
  padding: 0;
  color: var(--vp-c-text-1);
}
</style>
