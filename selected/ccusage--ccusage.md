---
nome: ccusage/ccusage
url: https://github.com/ccusage/ccusage
tipo: cli
areas: [tokens, custo]
harness: [claude-code, codex]
estrelas: 19k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Relatório local de uso de tokens por dia, sessão e janela de 5 h, lido dos logs do agente.'
---

# ccusage/ccusage

## O que é

CLI (binário Rust distribuído pelo npm) que lê os JSONL de sessão do Claude Code (`~/.claude/projects`) e do Codex (`~/.codex/sessions`, beta) e gera relatórios por dia, semana, mês, sessão e bloco de 5 h. Antes ficava em `ryoppippi/ccusage`; o link antigo redireciona.

## Por que é útil

Mostra quais projetos e sessões consomem mais, compara Claude Code com Codex e serve de régua para medir ferramentas de economia como o [rtk](rtk-ai--rtk.md).

## O que aproveitar

Uso sob demanda (`daily`, `session`, `blocks`). O `ccusage statusline` (beta) pode alimentar a barra de status.

## Como instalar

```bash
npx ccusage@latest daily
# ou
npm i -g ccusage
```

## Riscos e custos

- Funciona com assinatura, porque só lê logs locais, mas o valor em USD é estimativa de preço de API, não o que se paga.
- Não conhece o limite real do plano; `blocks --token-limit max` usa o maior bloco anterior como referência. O limite oficial está no `/usage` do Claude Code.
- Busca preços no LiteLLM; `--offline` evita rede. Sem daemon.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
