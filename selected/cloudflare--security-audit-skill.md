---
nome: cloudflare/security-audit-skill
url: https://github.com/cloudflare/security-audit-skill
tipo: skill
areas: [seguranca, auditoria, iac]
harness: [claude-code, codex]
estrelas: 29k (2026-10-13)
registrado: 2026-10-13
desde: 2026-10-13
resumo: 'Auditoria de segurança do repositório inteiro em 6 fases, com verificação adversarial dos achados.'
---

# cloudflare/security-audit-skill

## O que é

Skill que audita o repositório inteiro, não só o diff, em 6 fases: subagentes "hunters", verificadores adversariais e um ledger de cobertura, com execuções que se somam.

## Por que é útil

Bem mais profunda que o `/security-review` nativo. Tem módulos de IaC, containers, ingress e IAM (`CLOUD-AND-DEPLOYMENT.md`), CI e supply chain, web e autenticação. Uso pontual antes de publicar um app.

## O que aproveitar

A skill no perfil `quick`, com escopo e budget de agentes definidos.

## Como instalar

```bash
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

Ou copiar `skills/security-audit` (cerca de 320 KB).

## Riscos e custos

- Consome bastante dos limites de 5 h e semanal.
- Precisa de Node para os validadores.
- Sem sandbox de sistema operacional, não executa o código do alvo e deixa achados como `needs_validation`.

## Histórico

- 2026-10-13: registrado direto em `selected`, a partir de uma triagem que leu README, manifests e hooks pela API do GitHub, sem instalar.
