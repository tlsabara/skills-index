# skills-index

Índice pessoal de skills, plugins, servidores MCP, hooks e ferramentas para agentes de código
(Claude Code, Codex e afins). Cada registro é um arquivo Markdown, e a pasta onde ele está diz em
que ponto da avaliação ele se encontra.

## Categorias

| Pasta | Significado | O que o registro precisa ter |
| --- | --- | --- |
| [`find/`](find/) | Encontrado, ainda sem avaliação. Só a anotação de que existe. | O que é, em poucas linhas, e onde foi encontrado. |
| [`selected/`](selected/) | Interessante e ainda não testado: a ideia foi considerada útil. | Por que é útil, o que aproveitar, como instalar, riscos e custos. |
| [`on_test/`](on_test/) | Em teste e avaliação. | Onde está sendo testado, desde quando e o que está sendo observado. |
| [`approved/`](approved/) | Testado e aprovado. | Resultado do teste, como está configurado e ressalvas. |
| [`deprecated/`](deprecated/) | Desclassificado, em qualquer etapa. | O motivo, para não reavaliar à toa. |

O fluxo normal é `find` → `selected` → `on_test` → `approved`. Qualquer registro pode ir para
`deprecated`, e um `deprecated` pode voltar se o motivo deixar de valer.

## Contexto de quem avalia

As avaliações são feitas para um uso concreto, e um "deprecated" aqui pode ser ótimo em outro cenário:

- DevOps com Kubernetes (OKE na Oracle Cloud), Helm, GitOps e Rancher;
- apps web com Python + FastAPI e Vue 3 + TypeScript + Vite + Tailwind (nada de React), em Docker;
- Claude Code e Codex no WSL, com memória limitada, então serviço pesado em background é custo;
- memória e documentação já curadas num vault Obsidian, por skill própria;
- preferência por processos com TDD, verificação e revisão.

## Como registrar

1. Copie o [`TEMPLATE.md`](TEMPLATE.md) para a pasta da categoria, com o nome `dono--repo.md`
   (em minúsculas). Para uma skill específica dentro de um repositório: `dono--repo--skill.md`.
2. Preencha o frontmatter e as seções que a categoria pede.
3. Rode `python3 scripts/build_index.py` para atualizar o índice abaixo.

Para mudar de categoria, mova o arquivo com `git mv`, atualize o campo `desde` e acrescente uma
linha no `## Histórico` do registro dizendo o que motivou a mudança. Depois, gere o índice de novo.

## Índice

Gerado por `scripts/build_index.py`, não edite à mão. Estrelas e datas são do momento do registro.

<!-- index:start -->
### approved - testados e aprovados (0)

_Nenhum registro._

### on_test - em teste (0)

_Nenhum registro._

### selected - selecionados, ainda não testados (16)

| Registro | Tipo | Áreas | Resumo | Desde |
| --- | --- | --- | --- | --- |
| [affaan-m/ECC](selected/affaan-m--ecc.md) | skills | devops, kubernetes, docker, fastapi, vue, testes | "Everything Claude Code": 311 skills e 71 agentes; vale copiar só as de k8s, Docker, FastAPI e Vue. | 2026-10-13 |
| [akin-ozer/cc-devops-skills](selected/akin-ozer--cc-devops-skills.md) | skills | devops, kubernetes, helm, ci-cd, observabilidade | 31 skills de DevOps em pares gerador/validador: Helm, manifests k8s, CI, Dockerfile, PromQL, LogQL. | 2026-10-13 |
| [anthropics/claude-code-security-review](selected/anthropics--claude-code-security-review.md) | skill | seguranca, code-review | GitHub Action de revisão de segurança; vale só o comando security-review.md para customizar o /security-review. | 2026-10-13 |
| [anthropics/skills](selected/anthropics--skills.md) | skills | referencia, testes, documentos | Skills oficiais da Anthropic e a especificação Agent Skills; vale webapp-testing e, no Codex, docx e pdf. | 2026-10-13 |
| [ccusage/ccusage](selected/ccusage--ccusage.md) | cli | tokens, custo | Relatório local de uso de tokens por dia, sessão e janela de 5 h, lido dos logs do agente. | 2026-10-13 |
| [cloudflare/security-audit-skill](selected/cloudflare--security-audit-skill.md) | skill | seguranca, auditoria, iac | Auditoria de segurança do repositório inteiro em 6 fases, com verificação adversarial dos achados. | 2026-10-13 |
| [jarrodwatts/claude-hud](selected/jarrodwatts--claude-hud.md) | statusline | statusline, tokens | Status line com contexto, limites de 5 h e 7 dias com contagem até o reset, tools e agentes. | 2026-10-13 |
| [kenryu42/cc-safety-net](selected/kenryu42--cc-safety-net.md) | hook | seguranca, guarda, kubernetes | Hook que bloqueia comandos destrutivos, com rulebooks próprios (ex.: kubectl delete em contexto de produção). | 2026-10-13 |
| [ldayton/Dippy](selected/ldayton--dippy.md) | hook | seguranca, guarda, kubernetes, permissoes | Hook que interpreta a linha de comando inteira e aprova leitura de kubectl/helm sozinho, pedindo confirmação para escrita. | 2026-10-13 |
| [mattpocock/skills](selected/mattpocock--skills.md) | skills | engenharia, debugging, adr, git | Skills pequenas e combináveis de engenharia; vale copiar diagnóstico de bugs, ADR/glossário, handoff e git guardrails. | 2026-10-13 |
| [microsoft/playwright-cli](selected/microsoft--playwright-cli.md) | cli | testes, e2e, navegador | CLI do Playwright com skills para o agente dirigir um navegador gastando menos tokens que o MCP. | 2026-10-13 |
| [nextlevelbuilder/ui-ux-pro-max-skill](selected/nextlevelbuilder--ui-ux-pro-max-skill.md) | skill | ui-ux, vue, tailwind, acessibilidade | Skill de design com base local em CSV (estilos, paletas, fontes, guidelines), com stack Vue e checklist de acessibilidade. | 2026-10-13 |
| [obra/superpowers](selected/obra--superpowers.md) | plugin | metodologia, tdd, code-review, debugging | Metodologia em skills: brainstorming, plano, TDD, execução por subagentes e code review. | 2026-10-13 |
| [rtk-ai/rtk](selected/rtk-ai--rtk.md) | cli | tokens, custo | Filtra a saída de comandos de dev antes de chegar ao agente e corta de 60 a 90% dos tokens. | 2026-10-13 |
| [trailofbits/skills](selected/trailofbits--skills.md) | skills | seguranca, supply-chain, python | Plugins de segurança da Trail of Bits; vale supply-chain-risk-auditor, insecure-defaults e modern-python. | 2026-10-13 |
| [upstash/context7](selected/upstash--context7.md) | mcp | documentacao, vue, fastapi | Documentação atualizada de bibliotecas, por versão, entregue no contexto por MCP ou CLI. | 2026-10-13 |

### find - encontrados, sem avaliação (6)

| Registro | Tipo | Áreas | Resumo | Desde |
| --- | --- | --- | --- | --- |
| [antonbabenko/terraform-skill](find/antonbabenko--terraform-skill.md) | skill | iac, terraform | Skill de Terraform/OpenTofu; exemplos voltados a AWS, Azure e GCP. | 2026-10-13 |
| [congmnguyen/claude-code-wsl2-setup](find/congmnguyen--claude-code-wsl2-setup.md) | hook | wsl, notificacao, statusline | Receitas para Claude Code no WSL2: toast do Windows nos hooks, colar screenshot, status line. | 2026-10-13 |
| [getagentseal/codeburn](find/getagentseal--codeburn.md) | cli | tokens, custo | Aponta desperdício de tokens: MCP sem uso, CLAUDE.md grande, arquivos relidos; tem teto de gasto. | 2026-10-13 |
| [gowtham012/pinpoint](find/gowtham012--pinpoint.md) | mcp | ui-ux, vue, navegador | Extensão Chrome + MCP que leva o componente clicado (com arquivo) ao agente, com suporte a Vue. | 2026-10-13 |
| [hesreallyhim/awesome-claude-code](find/hesreallyhim--awesome-claude-code.md) | lista | lista, curadoria | Awesome-list central do Claude Code: skills, agentes, hooks, status lines, comandos e plugins. | 2026-10-13 |
| [safedep/gryph](find/safedep--gryph.md) | hook | seguranca, auditoria, log | Política YAML para ações do agente e log local em SQLite de tudo que ele executou. | 2026-10-13 |

### deprecated - desclassificados (5)

| Registro | Tipo | Áreas | Resumo | Desde |
| --- | --- | --- | --- | --- |
| [aidenybai/react-grab](deprecated/aidenybai--react-grab.md) | cli | ui-ux, react | Copia o componente clicado para o agente, mas só funciona com React e Solid. | 2026-10-13 |
| [ComposioHQ/awesome-claude-skills](deprecated/composiohq--awesome-claude-skills.md) | lista | lista | Lista de skills dominada por automações que dependem do gateway pago da Composio. | 2026-10-13 |
| [microsoft/playwright-mcp](deprecated/microsoft--playwright-mcp.md) | mcp | testes, e2e, navegador | MCP do Playwright; para agente de código, o próprio README recomenda o playwright-cli. | 2026-10-13 |
| [modelcontextprotocol/servers](deprecated/modelcontextprotocol--servers.md) | mcp | mcp, referencia | Hoje só 7 servidores MCP de referência, todos redundantes com ferramentas nativas do agente. | 2026-10-13 |
| [thedotmack/claude-mem](deprecated/thedotmack--claude-mem.md) | plugin | memoria | Memória automática entre sessões; pesada, com telemetria e dados de sessão saindo para terceiros. | 2026-10-13 |
<!-- index:end -->
