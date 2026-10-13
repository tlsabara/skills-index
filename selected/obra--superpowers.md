---
nome: obra/superpowers
url: https://github.com/obra/superpowers
tipo: plugin
areas: [metodologia, tdd, code-review, debugging]
harness: [claude-code, codex]
estrelas: 298k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Metodologia em skills: brainstorming, plano, TDD, execução por subagentes e code review.'
---

# obra/superpowers

## O que é

Plugin com 15 skills que encadeiam brainstorming, worktree, plano, execução por subagentes com revisão, TDD red-green, code review e fechamento da branch. Plugin oficial no Claude Code e no Codex.

## Por que é útil

É o que mais se aproxima de um processo com TDD, verificação e revisão embutidos no agente.

## O que aproveitar

- `skills/test-driven-development`
- `skills/systematic-debugging`
- `skills/verification-before-completion`
- `skills/requesting-code-review` e `skills/receiving-code-review`
- `skills/writing-plans` (se sobrepõe a uma skill própria de plano inicial de app)

## Como instalar

```text
/plugin install superpowers@claude-plugins-official
```

No Codex, pelo `/plugins` (marketplace oficial). Testar primeiro num repositório de app web, não globalmente.

## Riscos e custos

- Um hook SessionStart em bash injeta cerca de 3 KB (`using-superpowers`) em startup, clear e compact.
- O brainstorming dispara antes de qualquer construção; pode atrapalhar tarefa rápida de operação. É o principal ponto a observar no teste.
- O visual companion carrega um logo do site da Prime Radiant, que funciona como telemetria leve; desligar com `SUPERPOWERS_DISABLE_TELEMETRY=1`.
- Não instalar junto com o [mattpocock/skills](mattpocock--skills.md) inteiro: TDD e code review se sobrepõem.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
