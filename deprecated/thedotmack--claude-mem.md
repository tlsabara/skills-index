---
nome: thedotmack/claude-mem
url: https://github.com/thedotmack/claude-mem
tipo: plugin
areas: [memoria]
harness: [claude-code, codex]
estrelas: 100k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Memória automática entre sessões; pesada, com telemetria e dados de sessão saindo para terceiros.'
---

# thedotmack/claude-mem

## O que é

Memória persistente automática: hooks capturam todo uso de ferramenta, uma IA comprime em observações (SQLite + Chroma) e reinjeta o contexto relevante em sessões futuras.

## Por que foi desclassificado

- Duplica a memória já curada num vault Obsidian, com qualidade pior e em inglês por padrão.
- Sobe worker Bun em background com servidor HTTP e web viewer, mais Chroma via uv/Python, e instala Bun e uv sozinho. Custo alto num WSL com memória limitada.
- Hooks PreToolUse e PostToolUse com matcher `*` rodam `node` a cada ferramenta.
- Telemetria PostHog ligada por padrão.
- O instalador puxa login no serviço hospedado ou provedores terceiros (OpenRouter, Gemini), mandando conteúdo de sessão para fora.

## Histórico

- 2026-10-13: registrado direto em `deprecated`, a partir da mesma triagem dos `selected`.
