#!/usr/bin/env python3
"""Gera o índice do README.md a partir dos registros de cada categoria.

Cada registro é um .md com frontmatter simples (chave: valor, listas em [a, b],
texto com ": " entre aspas simples).
A pasta onde o arquivo está define a categoria. Uso:

    python3 scripts/build_index.py          # reescreve o índice no README.md
    python3 scripts/build_index.py --check  # falha se o README estiver desatualizado
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATEGORIES = ["approved", "on_test", "selected", "find", "deprecated"]
TITLES = {
    "approved": "approved - testados e aprovados",
    "on_test": "on_test - em teste",
    "selected": "selected - selecionados, ainda não testados",
    "find": "find - encontrados, sem avaliação",
    "deprecated": "deprecated - desclassificados",
}
REQUIRED = ["nome", "url", "tipo", "resumo", "registrado", "desde"]
START, END = "<!-- index:start -->", "<!-- index:end -->"


def parse(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: sem frontmatter")
    meta = {}
    for line in lines[1:]:
        if line == "---":
            break
        key, _, value = line.partition(":")
        value = value.strip()
        if len(value) > 1 and value[0] == value[-1] and value[0] in "'\"":
            q = value[0]
            value = value[1:-1].replace(q * 2, q) if q == "'" else value[1:-1]
        elif value.startswith("[") and value.endswith("]"):
            value = [v.strip() for v in value[1:-1].split(",") if v.strip()]
        meta[key.strip()] = value
    missing = [k for k in REQUIRED if not meta.get(k)]
    if missing:
        raise ValueError(f"{path}: faltam {', '.join(missing)}")
    return meta


def cell(value):
    if isinstance(value, list):
        value = ", ".join(value)
    return str(value).replace("|", "\\|")


def render():
    out = []
    for cat in CATEGORIES:
        files = sorted(p for p in (ROOT / cat).glob("*.md") if p.name != "README.md")
        out.append(f"### {TITLES[cat]} ({len(files)})\n")
        if not files:
            out.append("_Nenhum registro._\n")
            continue
        out.append("| Registro | Tipo | Áreas | Resumo | Desde |")
        out.append("| --- | --- | --- | --- | --- |")
        for p in files:
            m = parse(p)
            out.append(
                f"| [{cell(m['nome'])}]({cat}/{p.name}) | {cell(m['tipo'])} "
                f"| {cell(m.get('areas', ''))} | {cell(m['resumo'])} | {m['desde']} |"
            )
        out.append("")
    return "\n".join(out).rstrip("\n")


def main():
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    head, _, rest = text.partition(START)
    _, _, tail = rest.partition(END)
    new = f"{head}{START}\n{render()}\n{END}{tail}"
    if "--check" in sys.argv:
        if new != text:
            sys.exit("README.md desatualizado: rode python3 scripts/build_index.py")
        return
    readme.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
