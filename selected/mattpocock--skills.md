---
nome: mattpocock/skills
url: https://github.com/mattpocock/skills
tipo: skills
areas: [engenharia, debugging, adr, git]
harness: [claude-code, codex]
estrelas: 288k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Skills pequenas e combináveis de engenharia; vale copiar diagnóstico de bugs, ADR/glossário, handoff e git guardrails.'
---

# mattpocock/skills

## O que é

Skills do diretório `.agents` do Matt Pocock: grilling, spec, tickets, implement, TDD, code review, diagnóstico de bugs e modelagem de domínio com GLOSSARY.md e ADRs.

## Por que é útil

Leves, sem hooks e sem runtime, fáceis de ler e adaptar.

## O que aproveitar

- `skills/engineering/diagnosing-bugs`
- `skills/engineering/grill-with-docs` (GLOSSARY.md e ADRs)
- `skills/engineering/wizard` (gera script bash de provisionamento de infra e credenciais; bom para runbook)
- `skills/productivity/handoff`
- `skills/productivity/grill-me`
- `skills/misc/git-guardrails-claude-code`

## Como instalar

Copiar as pastas acima. O plugin inteiro existe (`claude plugin install mattpocock-skills@claude-plugins-official`; no Codex `codex plugin marketplace add mattpocock/skills`), mas se atualiza sozinho, sem revisão do que muda.

## Riscos e custos

`tdd` e `code-review` se sobrepõem ao [superpowers](obra--superpowers.md). `setup-matt-pocock-skills` precisa rodar uma vez por repositório.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
