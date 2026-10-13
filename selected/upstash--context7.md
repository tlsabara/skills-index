---
nome: upstash/context7
url: https://github.com/upstash/context7
tipo: mcp
areas: [documentacao, vue, fastapi]
harness: [claude-code, codex]
estrelas: 63k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Documentação atualizada de bibliotecas, por versão, entregue no contexto por MCP ou CLI.'
---

# upstash/context7

## O que é

Serviço hospedado da Upstash que entrega documentação de bibliotecas filtrada por versão. Funciona como MCP remoto (`resolve-library-id`, `query-docs`) ou como CLI `ctx7` com skill. O backend é fechado; o repositório só tem o cliente.

## Por que é útil

Ajuda em APIs que mudam rápido: Vue 3, Vite, Tailwind 4, FastAPI, Pydantic, Vitest. Para ferramentas de infra (kubectl, Helm, CLIs de nuvem) o ganho é pequeno frente a WebSearch e WebFetch.

## O que aproveitar

O modo CLI + skill, que pesa menos no contexto que o MCP.

## Como instalar

```bash
npx ctx7 setup --claude   # ou --codex
```

Ou MCP: `claude mcp add --scope user --header "Authorization: Bearer KEY" --transport http context7 https://mcp.context7.com/mcp`.

## Riscos e custos

- As consultas vão para a Upstash.
- Exige conta; o plano grátis tem limite de requisições.
- Documentação enviada pela comunidade, sem garantia de exatidão.
- O setup escreve no CLAUDE.md e no AGENTS.md.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
