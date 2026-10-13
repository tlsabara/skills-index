---
nome: microsoft/playwright-cli
url: https://github.com/microsoft/playwright-cli
tipo: cli
areas: [testes, e2e, navegador]
harness: [claude-code, codex]
estrelas: 14k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'CLI do Playwright com skills para o agente dirigir um navegador gastando menos tokens que o MCP.'
---

# microsoft/playwright-cli

## O que é

CLI irmã do [playwright-mcp](../deprecated/microsoft--playwright-mcp.md), com skills, recomendada pelo próprio README do MCP para agentes de código.

## Por que é útil

Para o agente abrir um app Vue + Vite em dev, reproduzir bug de UI, checar layout mobile e ajudar a escrever testes E2E. Gasta menos tokens que o MCP porque não carrega schema de ferramentas nem árvores de acessibilidade grandes no contexto.

## O que aproveitar

A CLI com as skills.

## Como instalar

```bash
npm install -g @playwright/cli@latest
playwright-cli install --skills
```

## Riscos e custos

- Cada Chromium consome centenas de MB; pesa num WSL com memória limitada.
- No WSL, sem modo headless, tenta abrir janela pelo WSLg.
- Perfil persistente guarda logins; preferir sessão isolada.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
