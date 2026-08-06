#!/usr/bin/env python3
"""biblio.py — gestion de la Biblioteca de Estudio (version portable).

Subcomandos:
  new <slug>      scaffold de un tema nuevo con la estructura canonica
  list            tabla de temas (--json para machine-readable)
  index           regenera INDEX.md + state/status.json
  find <query>    busca en frontmatter y contenido de todos los temas
  status <slug>   detalle de un tema
  pendientes      subtemas en rojo/amarillo por antiguedad + senales de desbalance

Contrato de estructura: references/estructura-canonica.md (incluido en el skill).

Sin dependencias externas: solo stdlib. No requiere ripgrep.

Localizacion de la biblioteca, en orden:
  1. --root <ruta>
  2. variable de entorno BIBLIO_ROOT
  3. busqueda desde el cwd hacia arriba (hasta 4 niveles) de un directorio
     'biblioteca' que contenga 'temas/' o ESTRUCTURA_CANONICA.md
  4. ./biblioteca  o  ./projects/biblioteca  (se ofrece crear con 'new')
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

MARKERS = ("temas", "ESTRUCTURA_CANONICA.md")


def _es_biblioteca(p):
    return p.is_dir() and any((p / m).exists() for m in MARKERS)


def descubrir_bundle(explicito=None):
    """Devuelve (path, existe). Nunca sale del arbol del usuario."""
    if explicito:
        return Path(explicito).expanduser().resolve(), True
    env = os.environ.get("BIBLIO_ROOT")
    if env:
        return Path(env).expanduser().resolve(), True

    cwd = Path.cwd().resolve()
    for base in [cwd, *cwd.parents[:4]]:
        for cand in (base / "biblioteca", base / "projects" / "biblioteca"):
            if _es_biblioteca(cand):
                return cand, True
        if _es_biblioteca(base) and base.name == "biblioteca":
            return base, True

    # no existe todavia: ruta propuesta para bootstrap
    propuesta = (cwd / "projects" / "biblioteca") if (cwd / "projects").is_dir() else (cwd / "biblioteca")
    return propuesta, False


BUNDLE, BUNDLE_EXISTE = descubrir_bundle()
TEMAS = BUNDLE / "temas"
STATE = BUNDLE / "state" / "status.json"
ROOT = BUNDLE

ESTADOS = ("semilla", "activo", "pausado", "maduro")
DIAS_ACTIVO = 30


def utc_now():
    return datetime.now(timezone.utc)


def stamp():
    return utc_now().strftime("%Y-%m-%dT%H%MZ")


def hoy():
    return utc_now().strftime("%Y-%m-%d")


# --------------------------------------------------------------------------- new

TEMA_MD = """# {titulo}

## Qué es
{objetivo}

## Estado
- Fase actual: **0 — sin arrancar**
- Estado: `semilla`
- Destilados: 0 · Notas: 0 · Repasos: 0

## Por qué lo estudio
{motivo}

## Aplica a
{aplica_md}

## Resume Next
- Definir las fases en `ROADMAP.md`
- Cargar las primeras fuentes en `fuentes/INDEX.md`
"""

ROADMAP_MD = """# Roadmap — {titulo}

**Ritmo:** adaptativo | **Estado:** por definir

## Punto de partida
- Qué ya sé:
- Qué me falta:

## Fases

| # | Fase | Criterio de "hecho" | Estado |
|---|------|---------------------|--------|
| 0 | Fundamentos | | ⬜ |
| 1 | | | ⬜ |
| 2 | | | ⬜ |

⬜ pendiente · 🟡 en curso · ✅ hecho

## Notas de planificación
_(Cómo se decidió el orden de las fases, qué se descartó y por qué.)_
"""

FUENTES_INDEX_MD = """# Fuentes — {titulo}

| Fuente | Tipo | Estado | Destilado |
|--------|------|--------|-----------|

Tipos: `libro` · `curso` · `doc-oficial` · `paper` · `canal` · `newsletter`
Estados: `pendiente` (conseguida, sin procesar) · `destilado` (procesada) · `deseada` (no la tengo)
"""

RECURSOS_MD = """# Recursos online — {titulo}

## Plataformas

## Canales / creadores

## Herramientas

## Cursos gratuitos
"""

GLOSARIO_MD = """---
tema: {slug}
tipo: nota
tags: [glosario]
aplica_a: []
estado: parcial
fecha: {fecha}
---

# Glosario — {titulo}

| Término | Qué es | Por qué importa |
|---------|--------|-----------------|
"""

REPASOS_INDEX_MD = """# Repasos — {titulo}

Ver `../../../ESTRUCTURA_CANONICA.md` para el método. Un quiz se toma
después de trabajo real, no después de leer.

| Fecha | Subtemas | Trabajo real ligado | Score | Para reforzar |
|-------|----------|---------------------|-------|---------------|

## Progreso por subtema

| Subtema | Estado | Última eval |
|---------|--------|-------------|

🟢 sólido · 🟡 casi · 🔴 reforzar
"""

CHECKLIST_MD = """---
tema: {slug}
tipo: playbook
tags: [checklist]
aplica_a: {aplica_json}
estado: parcial
fecha: {fecha}
---

# Checklist accionable — {titulo}

El consolidado de todo lo estudiado, en forma de acciones verificables.
Se llena a medida que los destilados producen ítems concretos.

| # | Acción | Origen (destilado) | Aplica a | Estado |
|---|--------|--------------------|----------|--------|
"""

PRACTICA_README = """# Práctica — {titulo}

Evidencia de trabajo real. Un archivo por sesión/ejercicio/caso.

Naming: `YYYY-MM-DD-<que-hice>.md`

Cada archivo abre con el frontmatter canónico (`tipo: practica`).
"""


def cmd_new(args):
    slug = args.slug.strip().lower()
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", slug):
        sys.exit(f"slug invalido: {slug!r} (solo minusculas, numeros y guiones)")
    dest = TEMAS / slug
    if dest.exists() and not args.force:
        sys.exit(f"el tema ya existe: {dest} (usa --force para re-scaffoldear faltantes)")

    titulo = args.titulo or slug.replace("-", " ").title()
    objetivo = args.objetivo or "_(pendiente de definir)_"
    motivo = args.motivo or "_(pendiente de definir)_"
    aplica = [a.strip() for a in (args.aplica_a or "").split(",") if a.strip()]
    aplica_md = "\n".join(f"- `{a}`" for a in aplica) or "- _(ninguno todavía)_"
    ctx = dict(slug=slug, titulo=titulo, objetivo=objetivo, motivo=motivo,
               aplica_md=aplica_md, aplica_json=json.dumps(aplica), fecha=hoy())

    for sub in ("fuentes/destilados", "notas", "repasos", "practica", "aplicacion"):
        (dest / sub).mkdir(parents=True, exist_ok=True)

    files = {
        "TEMA.md": TEMA_MD,
        "ROADMAP.md": ROADMAP_MD,
        "fuentes/INDEX.md": FUENTES_INDEX_MD,
        "fuentes/recursos.md": RECURSOS_MD,
        "notas/glosario.md": GLOSARIO_MD,
        "repasos/INDEX.md": REPASOS_INDEX_MD,
        "practica/README.md": PRACTICA_README,
        "aplicacion/CHECKLIST.md": CHECKLIST_MD,
    }
    creados = []
    for rel, tpl in files.items():
        path = dest / rel
        if path.exists():
            continue
        path.write_text(tpl.format(**ctx), encoding="utf-8")
        creados.append(rel)

    meta = {
        "slug": slug,
        "titulo": titulo,
        "objetivo": objetivo,
        "estado": "semilla",
        "fase_actual": "0",
        "aplica_a": aplica,
        "creado": hoy(),
        "actualizado": stamp(),
    }
    (dest / "tema.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n",
                                    encoding="utf-8")
    print(f"tema creado: {dest}")
    for c in creados:
        print(f"  + {c}")
    _rebuild_index()


# ------------------------------------------------------------------- scan/index

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def parse_frontmatter(path):
    try:
        head = path.read_text(encoding="utf-8", errors="replace")[:2048]
    except OSError:
        return {}
    m = FM_RE.match(head)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line or line.startswith(" "):
            continue
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip().strip("\"'") for x in v[1:-1].split(",") if x.strip()]
        else:
            v = v.strip("\"'")
        fm[k.strip()] = v
    return fm


def _count(d, pattern="*.md", exclude=("INDEX.md", "README.md", "glosario.md")):
    if not d.is_dir():
        return 0
    return len([p for p in d.glob(pattern) if p.name not in exclude])


def _last_activity(d):
    latest = 0.0
    for p in d.rglob("*"):
        if p.is_file() and not p.name.startswith("."):
            latest = max(latest, p.stat().st_mtime)
    return latest


def scan_temas():
    out = []
    if not TEMAS.is_dir():
        return out
    for d in sorted(TEMAS.iterdir()):
        if not d.is_dir() or d.name.startswith((".", "_")):
            continue
        meta_path = d / "tema.json"
        meta = {}
        if meta_path.exists():
            try:
                meta = json.loads(meta_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                meta = {}
        mtime = _last_activity(d)
        dias = (utc_now().timestamp() - mtime) / 86400 if mtime else 999
        counts = {
            "destilados": _count(d / "fuentes" / "destilados"),
            "notas": _count(d / "notas"),
            "repasos": _count(d / "repasos"),
            "practica": len([p for p in (d / "practica").rglob("*.md")
                             if p.name != "README.md"]) if (d / "practica").is_dir() else 0,
        }
        estado = meta.get("estado")
        if estado not in ESTADOS:
            estado = "semilla" if counts["destilados"] == 0 else "activo"
        if estado in ("activo", "pausado"):
            estado = "activo" if dias <= DIAS_ACTIVO else "pausado"
        out.append({
            "slug": d.name,
            "titulo": meta.get("titulo", d.name),
            "estado": estado,
            "fase_actual": meta.get("fase_actual", "?"),
            "aplica_a": meta.get("aplica_a", []),
            "counts": counts,
            "ultima_actividad": datetime.fromtimestamp(mtime, timezone.utc).strftime("%Y-%m-%d")
            if mtime else "-",
            "dias_sin_actividad": round(dias, 1) if mtime else None,
            "path": str(d.relative_to(ROOT)),
        })
    return out


INDEX_HEADER = """# Biblioteca de Estudio — INDEX

Generado por `biblio index` — no editar a mano.
Actualizado: {ts}

## Rutas
- Raíz: `{root}`
- Temas: `temas/<slug>/`
- Contrato de estructura: el skill, en `references/estructura-canonica.md`
- Estado machine-readable: `state/status.json`

## Temas

| Tema | Estado | Fase | Destilados | Notas | Repasos | Práctica | Últ. actividad |
|------|--------|------|-----------:|------:|--------:|---------:|----------------|
"""

INDEX_FOOTER = """
Estados: `semilla` (scaffold, sin material) · `activo` (movimiento <30d) · `pausado` · `maduro`

## Cómo buscar

```bash
python3 scripts/biblio.py find <query>        # busca en toda la biblioteca
python3 scripts/biblio.py pendientes          # qué hay que reforzar
grep -rl "aplica_a:.*<proyecto>" temas/       # lo que aplica a un proyecto
grep -rl "^tags:.*<tag>" temas/               # por tag
```

## Cómo se usa desde un proyecto

Trabajando en un proyecto, la pregunta útil es "¿qué de lo estudiado aplica
acá?" → `grep -rl "aplica_a:.*<proyecto>" temas/`.
El estudio no se consulta por tema, se consulta por problema.
"""


def _rebuild_index():
    temas = scan_temas()
    rows = []
    for t in temas:
        c = t["counts"]
        icon = {"semilla": "🌱", "activo": "🟢", "pausado": "⏸", "maduro": "🏛"}.get(t["estado"], "·")
        rows.append(
            f"| [`{t['slug']}`](temas/{t['slug']}/TEMA.md) | {icon} {t['estado']} | "
            f"{t['fase_actual']} | {c['destilados']} | {c['notas']} | {c['repasos']} | "
            f"{c['practica']} | {t['ultima_actividad']} |"
        )
    body = INDEX_HEADER.format(ts=stamp(), root=BUNDLE) + "\n".join(rows) + "\n" + INDEX_FOOTER
    (BUNDLE / "INDEX.md").write_text(body, encoding="utf-8")

    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({
        "generated_at": utc_now().isoformat(),
        "bundle_root": str(BUNDLE),
        "total_temas": len(temas),
        "totales": {
            k: sum(t["counts"][k] for t in temas)
            for k in ("destilados", "notas", "repasos", "practica")
        },
        "temas": temas,
    }, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return temas


def cmd_index(args):
    temas = _rebuild_index()
    print(f"INDEX.md + {STATE.name} regenerados — {len(temas)} temas")


def cmd_list(args):
    temas = scan_temas()
    if args.json:
        print(json.dumps(temas, indent=2, ensure_ascii=False))
        return
    if not temas:
        print("(sin temas)")
        return
    w = max(len(t["slug"]) for t in temas)
    print(f"{'TEMA'.ljust(w)}  ESTADO    FASE  DEST  NOT  REP  PRA  ULT.ACT")
    for t in temas:
        c = t["counts"]
        print(f"{t['slug'].ljust(w)}  {t['estado']:<8}  {str(t['fase_actual']):<4}  "
              f"{c['destilados']:>4}  {c['notas']:>3}  {c['repasos']:>3}  {c['practica']:>3}  "
              f"{t['ultima_actividad']}")


def cmd_status(args):
    for t in scan_temas():
        if t["slug"] == args.slug:
            print(json.dumps(t, indent=2, ensure_ascii=False))
            tema_md = TEMAS / args.slug / "TEMA.md"
            if tema_md.exists() and not args.json:
                print("\n--- TEMA.md ---")
                print(tema_md.read_text(encoding="utf-8")[:1800])
            return
    sys.exit(f"tema no encontrado: {args.slug}")


def cmd_find(args):
    if not TEMAS.is_dir():
        sys.exit("no hay temas")
    # busqueda en stdlib: no depende de grep/ripgrep, funciona en Windows
    needle = args.query.lower()
    hits = []
    for p in sorted(TEMAS.rglob("*.md")):
        try:
            if needle in p.read_text(encoding="utf-8", errors="replace").lower():
                hits.append(p)
        except OSError:
            continue
    if not hits:
        print(f"sin resultados para {args.query!r}")
        return
    print(f"{len(hits)} archivo(s):\n")
    for p in hits[:args.limit]:
        fm = parse_frontmatter(p)
        rel = p.relative_to(TEMAS)
        tipo = fm.get("tipo", "-")
        aplica = fm.get("aplica_a") or []
        aplica = ",".join(aplica) if isinstance(aplica, list) else aplica
        extra = f" · aplica_a: {aplica}" if aplica else ""
        print(f"  [{tipo}] {rel}{extra}")
    if len(hits) > args.limit:
        print(f"  ... +{len(hits) - args.limit} más")


# -------------------------------------------------------------------- pendientes

ROW_RE = re.compile(r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$")
FECHA_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")


def _dias_desde(texto):
    m = FECHA_RE.search(texto or "")
    if not m:
        return None
    try:
        d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), tzinfo=timezone.utc)
    except ValueError:
        return None
    return int((utc_now() - d).total_seconds() // 86400)


def _parse_progreso(path, slug):
    """Extrae filas de la seccion '## Progreso por ...' de un repasos/INDEX.md."""
    if not path.exists():
        return []
    lineas = path.read_text(encoding="utf-8", errors="replace").splitlines()
    dentro, filas = False, []
    for ln in lineas:
        if ln.startswith("## "):
            dentro = ln.lower().startswith("## progreso por")
            continue
        if not dentro:
            continue
        m = ROW_RE.match(ln)
        if not m:
            continue
        subtema, estado, ultima = (g.strip() for g in m.groups())
        if not subtema or subtema.lower() in ("subtema", "tema") or set(subtema) <= set("-: "):
            continue
        if "🔴" in estado:
            nivel = "rojo"
        elif "🟡" in estado:
            nivel = "amarillo"
        else:
            continue
        filas.append({
            "tema": slug,
            "subtema": subtema,
            "nivel": nivel,
            "detalle": re.sub(r"^[🔴🟡🟢]\s*", "", estado),
            "ultima_eval": ultima or "-",
            "dias": _dias_desde(ultima),
        })
    return filas


def _parse_banco(nota, slug):
    """Extrae la seccion '## Preguntas de control' de una nota."""
    try:
        lineas = nota.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []
    dentro, filas = False, []
    for ln in lineas:
        if ln.startswith("## "):
            dentro = "preguntas de control" in ln.lower()
            continue
        if not dentro or not ln.startswith("|"):
            continue
        cols = [c.strip() for c in ln.strip().strip("|").split("|")]
        if len(cols) < 5:
            continue
        _num, pregunta, respuesta, fecha, estado = cols[:5]
        if not pregunta or pregunta.lower() == "pregunta" or set(pregunta) <= set("-: "):
            continue
        if "🔴" in estado:
            nivel = "rojo"
        elif "🟡" in estado:
            nivel = "amarillo"
        else:
            continue
        filas.append({
            "tema": slug,
            "subtema": f"{nota.stem} · {pregunta[:44]}",
            "nivel": nivel,
            "detalle": f'última respuesta: "{respuesta[:60]}"',
            "ultima_eval": fecha or "-",
            "dias": _dias_desde(fecha),
            "origen": "banco",
        })
    return filas


def cmd_pendientes(args):
    temas = scan_temas()
    filas, senales = [], []
    for t in temas:
        d = TEMAS / t["slug"]
        filas += _parse_progreso(d / "repasos" / "INDEX.md", t["slug"])
        notas_dir = d / "notas"
        if notas_dir.is_dir():
            for nota in sorted(notas_dir.glob("*.md")):
                filas += _parse_banco(nota, t["slug"])
        c = t["counts"]
        if c["destilados"] and not c["repasos"]:
            senales.append(f"{t['slug']}: {c['destilados']} destilado(s), 0 repasos — leído sin evaluar")
        if c["destilados"] >= 5 and c["practica"] * 3 < c["destilados"]:
            ratio = c["destilados"] / c["practica"] if c["practica"] else float("inf")
            r = "∞" if c["practica"] == 0 else f"{ratio:.1f}"
            senales.append(f"{t['slug']}: ratio lectura/práctica {r}:1 "
                           f"({c['destilados']} destilados, {c['practica']} prácticas) — se lee más de lo que se practica")
        if t["estado"] == "pausado":
            senales.append(f"{t['slug']}: sin actividad hace {t['dias_sin_actividad']:.0f} días")

    filas.sort(key=lambda f: (f["nivel"] != "rojo", -(f["dias"] or 0)))

    if args.json:
        print(json.dumps({"pendientes": filas, "senales": senales}, indent=2, ensure_ascii=False))
        return

    if filas:
        print("SUBTEMAS PENDIENTES DE REFUERZO\n")
        wt = max(len(f["tema"]) for f in filas)
        ws = max(len(f["subtema"]) for f in filas)
        for f in filas:
            icon = "🔴" if f["nivel"] == "rojo" else "🟡"
            dias = f"{f['dias']}d" if f["dias"] is not None else "-"
            print(f"  {icon} {f['tema'].ljust(wt)}  {f['subtema'].ljust(ws)}  {dias:>5}  ({f['ultima_eval']})")
        rojos = [f for f in filas if f["nivel"] == "rojo"]
        if rojos:
            viejo = max((f["dias"] or 0) for f in rojos)
            print(f"\n  → {len(rojos)} en rojo, el más viejo hace {viejo} días.")
    else:
        print("Sin subtemas en rojo/amarillo.")

    if senales:
        print("\nSEÑALES\n")
        for s in senales:
            print(f"  · {s}")


def main():
    ap = argparse.ArgumentParser(prog="biblio", description="Biblioteca de Estudio (portable)")
    ap.add_argument("--root", help="raíz de la biblioteca (default: autodetectar)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("new", help="scaffold de un tema nuevo")
    p.add_argument("slug")
    p.add_argument("--titulo")
    p.add_argument("--objetivo")
    p.add_argument("--motivo")
    p.add_argument("--aplica-a", dest="aplica_a", help="slugs separados por coma")
    p.add_argument("--force", action="store_true")
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("list", help="tabla de temas")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("index", help="regenera INDEX.md + status.json")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("find", help="busca en la biblioteca")
    p.add_argument("query")
    p.add_argument("--limit", type=int, default=25)
    p.set_defaults(func=cmd_find)

    p = sub.add_parser("status", help="detalle de un tema")
    p.add_argument("slug")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("pendientes", help="subtemas en rojo/amarillo + señales")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_pendientes)

    args = ap.parse_args()

    if getattr(args, "root", None):
        global BUNDLE, TEMAS, STATE, ROOT, BUNDLE_EXISTE
        BUNDLE, BUNDLE_EXISTE = descubrir_bundle(args.root)
        TEMAS, STATE, ROOT = BUNDLE / "temas", BUNDLE / "state" / "status.json", BUNDLE

    if not BUNDLE_EXISTE and args.cmd != "new":
        print(f"No encontré una biblioteca de estudio.\n"
              f"  Ruta propuesta: {BUNDLE}\n"
              f"  Para crearla:   python3 {Path(__file__).name} new <tema>\n"
              f"  O indicá dónde: --root <ruta>  |  BIBLIO_ROOT=<ruta>",
              file=sys.stderr)
        sys.exit(2)

    args.func(args)


if __name__ == "__main__":
    main()
