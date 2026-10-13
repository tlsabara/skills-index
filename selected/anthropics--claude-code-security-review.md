---
nome: anthropics/claude-code-security-review
url: https://github.com/anthropics/claude-code-security-review
tipo: skill
areas: [seguranca, code-review]
harness: [claude-code]
estrelas: 6.4k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'GitHub Action de revisão de segurança; vale só o comando security-review.md para customizar o /security-review.'
---

# anthropics/claude-code-security-review

## O que é

GitHub Action que roda em cada PR a mesma análise do `/security-review` nativo do Claude Code e comenta os achados no PR.

## Por que é útil

O arquivo `.claude/commands/security-review.md`, copiado para `.claude/commands/` de um projeto, substitui o comando nativo e permite acrescentar regras de falso positivo do stack (FastAPI, Vue, charts Helm).

## O que aproveitar

Só `.claude/commands/security-review.md`.

## Como instalar

Copiar o arquivo para `.claude/commands/` do projeto e editar.

## Riscos e custos

A Action em si não vale: só GitHub, exige API key paga à parte da assinatura, modelo padrão `claude-opus-4-1`, o README avisa que não é protegida contra prompt injection, e o último push foi em 2026-02.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
