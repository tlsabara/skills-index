---
nome: anthropics/skills
url: https://github.com/anthropics/skills
tipo: skills
areas: [referencia, testes, documentos]
harness: [claude-code, codex]
estrelas: 181k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Skills oficiais da Anthropic e a especificação Agent Skills; vale webapp-testing e, no Codex, docx e pdf.'
---

# anthropics/skills

## O que é

Repositório oficial com skills de exemplo, as de documento (docx, pdf, pptx, xlsx, source-available) e a especificação do formato `SKILL.md`.

## Por que é útil

É a referência do formato. As de documento já vêm embutidas no Claude Code (`anthropic-skills:*`), mas não no Codex.

## O que aproveitar

- `skills/webapp-testing`: Playwright em Python, com `scripts/with_server.py` para subir o servidor antes do teste.
- No Codex: `skills/docx` e `skills/pdf`, para relatórios.
- `skills/frontend-design`, `skills/doc-coauthoring` e `skills/mcp-builder`, se um dia for escrever um MCP próprio.

## Como instalar

Copiar as pastas avulsas. O pacote `/plugin install example-skills@anthropic-agent-skills` traz 12 skills, a maioria sem uso aqui (algorithmic-art, slack-gif, brand-guidelines).

## Riscos e custos

Sem hooks nem runtime; só scripts Python rodados sob demanda.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
