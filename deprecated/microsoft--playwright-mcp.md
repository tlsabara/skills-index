---
nome: microsoft/playwright-mcp
url: https://github.com/microsoft/playwright-mcp
tipo: mcp
areas: [testes, e2e, navegador]
harness: [claude-code, codex]
estrelas: 38k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'MCP do Playwright; para agente de código, o próprio README recomenda o playwright-cli.'
---

# microsoft/playwright-mcp

## O que é

Servidor MCP (Node 18+) que dirige um navegador real por snapshots de acessibilidade: cliques, formulários, abas, rede, PDF.

## Por que foi desclassificado

Substituído pelo [playwright-cli](../selected/microsoft--playwright-cli.md), que o próprio README recomenda para agentes de código por gastar menos tokens. Se precisar do MCP (cliente sem shell, por exemplo), usar no escopo do projeto: `claude mcp add --scope project playwright -- npx @playwright/mcp@latest --headless --isolated`. O README avisa que não é fronteira de segurança.

## Histórico

- 2026-10-13: registrado direto em `deprecated`, a partir da mesma triagem dos `selected`.
