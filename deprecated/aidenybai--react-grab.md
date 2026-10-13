---
nome: aidenybai/react-grab
url: https://github.com/aidenybai/react-grab
tipo: cli
areas: [ui-ux, react]
harness: [claude-code]
estrelas: 7.7k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Copia o componente clicado para o agente, mas só funciona com React e Solid.'
---

# aidenybai/react-grab

## O que é

Passa o mouse num elemento, Ctrl+C, e cola no agente o componente com arquivo e linha de origem.

## Por que foi desclassificado

Não funciona com Vue 3. Depende do `bippy` (internals de fiber do React); no `main` só há React e Solid. O PR #228, que adiciona Vue e Svelte, está aberto desde 2026-03, e a issue #247 (Nuxt sem framework detectado) segue aberta. Alternativa para Vue: [pinpoint](../find/gowtham012--pinpoint.md).

## Histórico

- 2026-10-13: registrado direto em `deprecated`, a partir da mesma triagem dos `selected`.
