---
nome: akin-ozer/cc-devops-skills
url: https://github.com/akin-ozer/cc-devops-skills
tipo: skills
areas: [devops, kubernetes, helm, ci-cd, observabilidade]
harness: [claude-code]
estrelas: 321 (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: '31 skills de DevOps em pares gerador/validador: Helm, manifests k8s, CI, Dockerfile, PromQL, LogQL.'
---

# akin-ozer/cc-devops-skills

## O que é

Plugin com 31 skills em `devops-skills-plugin/skills/`, quase todas em pares gerador e validador: Ansible, Azure Pipelines, bash, Dockerfile, Fluent Bit, GitHub Actions, GitLab CI, Helm, Jenkins, k8s YAML, Loki, Makefile, PromQL, LogQL, Terraform, Terragrunt, além de `k8s-debug`.

## Por que é útil

É o achado mais alinhado a trabalho de DevOps com Kubernetes e Helm. Encontrado na [awesome-claude-code](../find/hesreallyhim--awesome-claude-code.md).

## O que aproveitar

- `helm-validator` (kubeconform + `--dry-run=server`)
- `k8s-yaml-validator`
- `k8s-debug` (diagnóstico só leitura antes de drain, restart ou undo, com confirmação)
- `gitlab-ci-validator`, `dockerfile-validator`
- `promql-generator`, `logql-generator`

## Como instalar

Copiar só as pastas escolhidas para `~/.claude/skills/` (e `~/.codex/skills/`), em vez de instalar o plugin com as 31.

## Riscos e custos

Projeto pequeno (321 estrelas, último push em 2026-07). Revisar os comandos que as skills rodam antes de usar contra cluster de produção.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
