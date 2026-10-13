---
nome: rtk-ai/rtk
url: https://github.com/rtk-ai/rtk
tipo: cli
areas: [tokens, custo]
harness: [claude-code, codex]
estrelas: 83k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Filtra a saída de comandos de dev antes de chegar ao agente e corta de 60 a 90% dos tokens.'
---

# rtk-ai/rtk

## O que é

Binário único em Rust (Apache-2.0), sem daemon. Resume, agrupa, deduplica e trunca a saída de comandos comuns de desenvolvimento antes de ela entrar no contexto do agente.

## Por que é útil

Saída grande de comando é o que mais enche o contexto no dia a dia. Cobertura conferida em `src/discover/rules.rs`:

- **git:** status, log, diff, show, add, commit, push, pull, branch, fetch, stash.
- **docker:** ps, images, logs (deduplicado), run, exec, build, compose ps/logs/build.
- **pytest:** só as falhas, com traceback encurtado.
- **npm:** só `npm run/exec/x` e `npx`; `npm install` não é coberto. Cobre também vitest, `playwright test`, tsc e eslint.
- **helm:** filtro genérico, tira linhas vazias e corta em 120 colunas.
- **kubectl:** parcial. Só `get pods` e `get svc` ganham resumo; `describe` e `-o json/yaml` passam direto.

## O que aproveitar

O hook global, com `kubectl` excluído (`exclude_commands = ["kubectl"]` no `config.toml`), porque `kubectl logs` passa a ser cortado em `--tail 100`, o que é ruim quando o log é evidência de incidente. Medir antes e depois com o [ccusage](ccusage--ccusage.md).

## Como instalar

Binário da página de releases, em vez do `curl | sh` do README. Depois:

```bash
rtk init -g            # hook PreToolUse no ~/.claude/settings.json + RTK.md no CLAUDE.md
rtk init -g --codex    # hook no hooks.json + AGENTS.md
rtk init -g --uninstall
```

O hook reescreve `git status` para `rtk git status`. Só age no Bash e respeita as regras deny/ask/allow. Comandos sem regra (um wrapper de CLI próprio, por exemplo) passam intocados.

## Riscos e custos

- Guarda em SQLite local a saída completa dos comandos que falharam, que pode conter segredos.
- Telemetria só com opt-in; reforçar com `RTK_TELEMETRY_DISABLED=1`.
- Issue #927: comandos kubectl com `--context` não são reescritos.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
