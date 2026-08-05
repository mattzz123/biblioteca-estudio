# Estructura Canónica de un Tema — Contrato de la Biblioteca

Todo tema de estudio, sea cual sea la disciplina, se arma exactamente igual.
Esto no es preferencia estética: es lo que permite que un agente encuentre
material de un tema que nunca vio antes sin explorar el filesystem.

## El ciclo

```
fuente → destilado → nota → práctica → repaso → aplicación
```

| Paso | Pregunta que responde | Carpeta |
|------|----------------------|---------|
| Fuente | ¿de dónde saco el conocimiento? | `fuentes/` |
| Destilado | ¿qué dice, convertido en accionable? | `fuentes/destilados/` |
| Nota | ¿qué aprendí del concepto? | `notas/` |
| Práctica | ¿qué hice de verdad? | `practica/` |
| Repaso | ¿cuánto entendí realmente? | `repasos/` |
| Aplicación | ¿cómo baja esto al negocio? | `aplicacion/` |

Un tema sin `practica/` es lectura, no estudio.
Un tema sin `repasos/` no tiene forma de saber si quedó algo.
Un tema sin `aplicacion/` es un hobby, no una inversión.

## El árbol

```
temas/<slug>/
├── TEMA.md              identidad + estado + fase actual   (≤2KB / ≤40 líneas)
├── tema.json            metadata machine-readable (generado/actualizado por `biblio`)
├── ROADMAP.md           fases 0..N, cada una con criterio de "hecho"
├── fuentes/
│   ├── INDEX.md         catálogo: fuente · tipo · estado (pendiente | destilado)
│   ├── recursos.md      material online gratuito (plataformas, canales, tools)
│   └── destilados/      <fuente-slug>.md
├── notas/
│   ├── glosario.md      términos del dominio
│   └── <subtema>.md     un archivo por concepto, crece con el tiempo
├── repasos/
│   ├── INDEX.md         tabla de quizzes + progreso por subtema (🟢🟡🔴)
│   └── YYYY-MM-DD-<tema>.md
├── practica/            evidencia de trabajo real (writeups, labs, campañas, sesiones)
└── aplicacion/
    ├── CHECKLIST.md     el consolidado accionable del tema
    └── <playbook>.md    guías operativas derivadas del estudio
```

**Opcional — `fases/`:** cuando el roadmap es grande, cada fase puede tener su
propia carpeta con material (`fases/fase-0-fundamentos/`). `ROADMAP.md` sigue
siendo el mapa; `fases/` es el detalle. Solo si hace falta: un tema chico no lo
necesita. *(Ejemplo real en la biblioteca del autor: un tema de seguridad con 7
fases, de fundamentos a especialización.)*

## Frontmatter obligatorio

Todo archivo de `fuentes/destilados/`, `notas/`, `repasos/` y `practica/` abre con:

```yaml
---
tema: seguridad
tipo: destilado          # destilado | nota | repaso | practica | playbook
fuente: "Security Engineering — Ross Anderson"   # solo en destilados
tags: [threat-modeling, crypto]
aplica_a: [mi-saas]      # 1-3 proyectos COMO MÁXIMO, [] si es fundamento general
relevancia: alta         # alta | media | fondo
estado: completo         # completo | parcial | pendiente
fecha: 2026-08-05
---
```

`aplica_a` es el campo que invierte el flujo. Trabajando en un proyecto:

```bash
# con ripgrep
rg -l "aplica_a:.*<proyecto>" temas/ | xargs rg -l "^relevancia: alta"

# sin ripgrep (portable)
grep -rl "aplica_a:.*<proyecto>" temas/ | xargs grep -l "^relevancia: alta"
```

devuelve lo estudiado que aplica a ese proyecto. Sin ese campo, la biblioteca es
un depósito; con él, es consultable desde el trabajo real.

### La regla del filtro que filtra

**`aplica_a` admite 1-3 proyectos, no más.** Un campo que matchea con todo no
discrimina nada: si un destilado "aplica" a 5 de 6 proyectos, la búsqueda por
proyecto devuelve el catálogo entero y no sirve para nada.

El criterio no es "¿tiene que ver con?" sino **"¿cambiaría una decisión concreta
en ese proyecto?"**. Si la respuesta honesta es "en general sí, en particular
nada", va `aplica_a: []` y `relevancia: fondo`.

| relevancia | Significa |
|-----------|-----------|
| `alta` | Hay una decisión o un pendiente concreto hoy que este material toca |
| `media` | Informa criterio para ese proyecto, sin acción inmediata |
| `fondo` | Fundamento general, sin destinatario — va con `aplica_a: []` |

*Calibración de referencia (biblioteca del autor, 32 destilados de seguridad):
12 alta · 8 media · 12 fondo.* Si un tema termina con 80% en `alta`, la
clasificación está inflada y la búsqueda por proyecto deja de discriminar.

## Reglas de naming

- Slugs en minúscula, sin tildes, guiones para separar: `zero-trust-networks.md`
- Destilado = slug de la fuente, no del tema: `practical-malware-analysis.md`
- Repaso = `YYYY-MM-DD-<subtema-principal>.md`
- Nota = nombre del concepto: `networking.md`, `pixel-y-capi.md`
- Nada de `notas-2.md`, `final-v3.md`, `nuevo-*.md`

## Frontera con las carpetas de proyecto

> **La biblioteca guarda el aprendizaje. La carpeta del proyecto guarda la operación.**

| Va a la biblioteca | Va al proyecto |
|--------------------|----------------|
| Destilado de un libro de seguridad | La auditoría de tu servidor con sus hallazgos y fechas |
| Nota sobre cómo funciona el Pixel de Meta | La cuenta de ads del cliente y su performance |
| Quiz sobre contenedores | El Dockerfile que se corrigió |
| Playbook de threat modeling | El incidente del martes y su postmortem |

La diferencia práctica: el material de la biblioteca **sirve igual dentro de seis
meses**; el del proyecto tiene fecha, responsable y estado. Si lo que estás por
guardar tiene un "quién" y un "cuándo", es operación.

Cuando un tema genera operación real y sostenida, el tema **no** se muda: se
queda en la biblioteca y el proyecto le apunta.

## Ciclo de vida de un tema

| Estado | Significa |
|--------|-----------|
| `semilla` | Scaffold creado, ROADMAP sin definir, cero destilados |
| `activo` | Se está estudiando ahora: hay movimiento en los últimos 30 días |
| `pausado` | Material válido, sin actividad reciente |
| `maduro` | Roadmap completo, aplicándose al negocio |

El estado vive en `tema.json` y lo refresca `biblio index`.

## Presupuestos

| Archivo | Budget | Motivo |
|---------|--------|--------|
| `TEMA.md` | ≤2KB / ≤40L | Es lo primero que lee el agente |
| `ROADMAP.md` | ≤8KB | Mapa, no contenido |
| `fuentes/INDEX.md` | sin límite | Tabla, crece linealmente |
| destilados | ≤25KB c/u | Si excede, dividir por parte del libro |

Overflow de `TEMA.md` migra a `ROADMAP.md` o al historial del tema.
