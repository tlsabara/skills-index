---
nome: jarrodwatts/claude-hud
url: https://github.com/jarrodwatts/claude-hud
tipo: statusline
areas: [statusline, tokens]
harness: [claude-code]
estrelas: 28k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Status line com contexto, limites de 5 h e 7 dias com contagem até o reset, tools e agentes.'
---

# jarrodwatts/claude-hud

## O que é

Status line para o Claude Code que mostra uso de contexto, limites de 5 h e 7 dias com contagem até o reset, ferramentas e agentes ativos.

## Por que é útil

Ver o limite chegando antes de bater nele. Detalhe aprendido: o stdin da status line já traz `rate_limits`, então dá para fazer uma versão própria com jq, sem Node.

## O que aproveitar

A ideia e o layout; se a memória apertar, reimplementar com jq.

## Como instalar

Seguir o README do repositório.

## Riscos e custos

Roda a cada atualização da status line; em Node, é mais um processo frequente.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
