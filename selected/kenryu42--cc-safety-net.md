---
nome: kenryu42/cc-safety-net
url: https://github.com/kenryu42/cc-safety-net
tipo: hook
areas: [seguranca, guarda, kubernetes]
harness: [claude-code, codex]
estrelas: 1.6k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Hook que bloqueia comandos destrutivos, com rulebooks próprios (ex.: kubectl delete em contexto de produção).'
---

# kenryu42/cc-safety-net

## O que é

Hook PreToolUse que bloqueia comandos destrutivos de git, `rm` e leitura de segredos, e aceita rulebooks em JSON próprio. Antes se chamava `claude-code-safety-net`.

## Por que é útil

Guarda contra erro do agente em namespaces de produção: dá para escrever regras que bloqueiem `kubectl delete` e `helm uninstall` em contextos de cluster específicos. Alternativa: [Dippy](ldayton--dippy.md); escolher um dos dois.

## O que aproveitar

O hook com um rulebook próprio para os contextos de produção.

## Como instalar

Seguir o README do repositório; funciona também no Codex.

## Riscos e custos

Sobe um processo Node a cada chamada de ferramenta. Bloqueio por padrão de texto pode deixar passar variações do comando; não substitui RBAC no cluster.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
