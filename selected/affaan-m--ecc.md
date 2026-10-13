---
nome: affaan-m/ECC
url: https://github.com/affaan-m/ECC
tipo: skills
areas: [devops, kubernetes, docker, fastapi, vue, testes]
harness: [claude-code, codex]
estrelas: 278k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: '"Everything Claude Code": 311 skills e 71 agentes; vale copiar só as de k8s, Docker, FastAPI e Vue.'
---

# affaan-m/ECC

## O que é

Sistema de harness enorme: 311 skills, 71 agentes, 97 comandos, rules, memória, "instincts" e o scanner AgentShield. Funciona no Claude Code, no Codex (plugin nativo) e em mais uns 10 harnesses.

## Por que é útil

Entre as centenas de skills há algumas sólidas para Kubernetes, Docker, FastAPI e Vue + Vite. A de k8s cobre probes, RBAC, HPA, CrashLoop e OOMKilled; a de FastAPI cobre Pydantic v2, DI e testes com httpx. Não há nada de Helm, GitOps, Rancher ou OCI.

## O que aproveitar

- `skills/kubernetes-patterns`
- `skills/docker-patterns`
- `skills/deployment-patterns`
- `skills/fastapi-patterns`
- `skills/python-testing`
- `skills/vue-patterns`
- `skills/vite-patterns`
- `skills/e2e-testing`

## Como instalar

Copiar só as pastas acima para `~/.claude/skills/` e `~/.codex/skills/`. **Não** instalar o plugin (`/plugin marketplace add https://github.com/affaan-m/ECC`).

## Riscos e custos

O plugin inteiro traz 27 hooks `node -e` (PreToolUse em todas as ferramentas, 8 no Stop, UserPromptSubmit, SessionStart injetando até 8000 caracteres), um MCP chrome-devtools via npx, 311 descrições de skill no contexto, sugestão de trocar o modelo para Sonnet e os subagentes para Haiku, e upsell do ECC Pro.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
