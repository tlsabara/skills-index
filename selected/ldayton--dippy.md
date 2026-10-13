---
nome: ldayton/Dippy
url: https://github.com/ldayton/Dippy
tipo: hook
areas: [seguranca, guarda, kubernetes, permissoes]
harness: [claude-code]
estrelas: 243 (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Hook que interpreta a linha de comando inteira e aprova leitura de kubectl/helm sozinho, pedindo confirmação para escrita.'
---

# ldayton/Dippy

## O que é

Hook de permissão que analisa a linha de comando inteira, inclusive pipes, com handlers próprios para kubectl, helm e terraform.

## Por que é útil

Menos prompts em troubleshooting de Kubernetes: aprova sozinho `get`, `describe` e `logs` e pede confirmação para `apply`, `delete`, `exec` e `rollout`. Alternativa: [cc-safety-net](kenryu42--cc-safety-net.md); escolher um dos dois.

## O que aproveitar

O hook, com atenção ao ponto abaixo sobre `kubectl config`.

## Como instalar

Seguir o README do repositório.

## Riscos e custos

- Trata `kubectl config` como seguro, e `kubectl config use-context` troca o contexto ativo, o que pode apontar o próximo comando para outro cluster.
- Um processo a cada comando.
- Último push em 2026-06.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
