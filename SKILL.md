---
name: biblioteca
description: Biblioteca de Estudio — estructura reutilizable para estudiar cualquier disciplina (seguridad, IA, marketing, idiomas, lo que sea) y hacer que lo aprendido sea consultable desde el trabajo diario. Usar cuando el usuario dice "abrir la biblioteca", "biblioteca de estudio", "quiero estudiar X", "nuevo tema de estudio", "explicame X", "qué es X", "enseñame cómo funciona X", "destilar este libro/curso", "tomame un repaso", "quiz de X", "qué estudiamos que aplique a <proyecto>", "cargar material de estudio", o cuando aparece un concepto desconocido en medio de un trabajo real, o un libro/curso/paper que hay que convertir en material accionable.
metadata:
  version: 2.1.0-portable
---

# Biblioteca de Estudio

Sistema para estudiar cualquier disciplina de forma que lo aprendido no se
pierda y sea consultable desde el trabajo real.

**Contrato de estructura:** `references/estructura-canonica.md` — leerlo antes de
crear o modificar cualquier tema. Está incluido en este skill: no depende de
ningún archivo externo.

## Principio

Un tema no es una carpeta de PDFs. Es un ciclo con **dos puertas de entrada**:

```
        fuente ──── destilar ────┐
                                 ├──→ nota → práctica → repaso → aplicación
  trabajo real ─── explicame ────┘
```

Buena parte de lo que se aprende de verdad no entra por un libro: entra porque
algo se rompió, apareció un término desconocido, o hubo que decidir sin entender
del todo. `explicame` captura eso; `destilar` procesa las fuentes.

Si falta `practica/`, es lectura. Si falta `repasos/`, no hay forma de saber si
quedó algo. Si falta `aplicacion/`, es un hobby y no una inversión.

**Frontera dura:** la biblioteca guarda el **aprendizaje**; la carpeta del
proyecto guarda la **operación**. El destilado de un libro de seguridad va acá;
la auditoría de tu servidor con sus hallazgos y fechas va al proyecto.

## Paso 0 — Localizar la biblioteca (SIEMPRE primero)

No asumas rutas. Buscá, en este orden:

1. Variable de entorno `BIBLIO_ROOT`, si está definida.
2. `biblioteca/ESTRUCTURA_CANONICA.md` o `biblioteca/temas/` desde el directorio
   actual y hacia arriba (hasta 3 niveles), y dentro de `projects/`.
3. Si no aparece: **modo bootstrap** (abajo).

```bash
# búsqueda portable
find . -maxdepth 4 -type d -name temas -path "*biblioteca*" 2>/dev/null
```

### Modo bootstrap (no existe todavía)

Preguntar antes de crear nada:

> "No encuentro una biblioteca de estudio acá. ¿La creo en `<ruta propuesta>`?"

Ruta por defecto: `biblioteca/` en la raíz del workspace del usuario, o
`projects/biblioteca/` si existe una carpeta `projects/`. **Nunca** crear fuera
del workspace del usuario ni en su configuración global.

Al crear: `ESTRUCTURA_CANONICA.md` (copiar desde `references/`), `INDEX.md`,
`temas/`. Nada más hasta que haya un tema real.

## El CLI es opcional

Si `scripts/biblio.py` está disponible, acelera todo. Si no, **todas las
operaciones tienen equivalente manual** y el skill funciona igual:

| Operación | Con CLI | Sin CLI |
|-----------|---------|---------|
| Listar temas | `biblio list` | `ls temas/` + leer cada `TEMA.md` |
| Crear tema | `biblio new <slug>` | crear el árbol a mano según el contrato |
| Regenerar índice | `biblio index` | actualizar `INDEX.md` a mano |
| Buscar | `biblio find <q>` | `grep -ri "<q>" temas/` |
| Pendientes de repaso | `biblio pendientes` | leer cada `repasos/INDEX.md` y cada `## Preguntas de control`, juntar los 🔴/🟡 |

Invocación: `python3 scripts/biblio.py <subcomando>` (o `BIBLIO_ROOT=<ruta>
python3 scripts/biblio.py …` si la autodetección falla).

**Nunca instales nada ni modifiques configuración global del usuario.** Este
skill funciona con archivos de texto dentro del workspace y nada más.

## Modos

### 1. Abrir — `/biblioteca` o `/biblioteca <tema>`

Sin argumento: listar temas y reportar estado general.
Con tema: leer `temas/<tema>/TEMA.md` (≤2KB) y reportar fase, pendientes y qué
sigue. No abrir destilados enteros salvo que la pregunta lo exija.

### 2. Nuevo tema — `/biblioteca nuevo <tema>`

Antes de crear nada, entrevistar corto — **3 preguntas, no más**:

1. ¿Objetivo concreto? — "qué vas a poder hacer que hoy no podés"
2. ¿Por qué ahora? — qué trabajo o decisión lo empuja
3. ¿A qué proyectos aplica? — nombres reales de sus proyectos

Después crear el árbol del contrato y completar `ROADMAP.md` con fases reales:
cada fase con **criterio de "hecho" verificable**, no "entender X". Un roadmap
sin criterio de corte es una lista de deseos.

### 3. Explicame — `/biblioteca explicame <concepto>`

Ver `references/metodo-explicacion.md`. La **segunda puerta de entrada**: no
procesa una fuente, procesa un concepto que apareció trabajando.

Regla corta: anclar al trabajo real antes de definir, chequear comprensión
**durante** y no al final, y cerrar pidiendo la reformulación con sus palabras
— transcrita textual, sin corregirle la redacción.

Salida: `temas/<tema>/notas/<concepto>.md` con el mecanismo, la cita textual de
cómo lo explicó, y una sección **`## Preguntas de control`** (2-5 preguntas sobre
mecanismos, no definiciones). Ese banco es de donde sale el quiz después.

### 4. Destilar — `/biblioteca destilar <fuente>`

Ver `references/metodo-destilado.md`. Regla corta: el destilado no resume el
libro, extrae **lo que cambia una decisión**. Si un capítulo no produce ni un
ítem accionable, se marca y se sigue.

Salida: `temas/<tema>/fuentes/destilados/<fuente-slug>.md` con frontmatter, alta
en `fuentes/INDEX.md`, y los ítems accionables suben a `aplicacion/CHECKLIST.md`.

### 5. Repasar — `/biblioteca repasar <tema>`

Ver `references/metodo-repaso.md`. Regla corta: **una pregunta por vez**,
corrección inmediata, sin adelantar la siguiente. Se toma después de trabajo
real, no después de leer.

Las preguntas salen del **banco** (`## Preguntas de control` de las notas), no de
la imaginación: se re-pregunta sobre las mismas formulaciones para ver si las
sostiene semanas después. Antes de armar la ronda, juntar los pendientes
(`biblio pendientes`, o leyendo los `repasos/INDEX.md` y los bancos).

Los 🔴 viejos entran sí o sí: un subtema en rojo hace 50 días es material que se
dio por estudiado y no lo está.

### 6. Aplicar — `/biblioteca aplicar <tema> <proyecto>`

El puente estudio→trabajo. Buscar qué material aplica:

```bash
grep -rl "aplica_a:.*<proyecto>" temas/
```

Producir un checklist accionable **en la carpeta del proyecto**, citando el
destilado de origen. La biblioteca no lleva el seguimiento de ejecución.

## La regla del filtro que filtra

`aplica_a` admite **1-3 proyectos como máximo**. El criterio no es "¿tiene que
ver con?" sino **"¿cambiaría una decisión concreta en ese proyecto?"**. Si la
respuesta honesta es "en general sí, en particular nada", va `aplica_a: []` +
`relevancia: fondo`.

| relevancia | Cuándo |
|-----------|--------|
| `alta` | Hay un pendiente o decisión concreta hoy que este material toca |
| `media` | Informa criterio, sin acción inmediata |
| `fondo` | Fundamento general, sin destinatario (`aplica_a: []`) |

Un campo que matchea con todo no discrimina nada: si un destilado "aplica" a 5
de 6 proyectos, la búsqueda por proyecto devuelve el catálogo entero y no sirve.

*Calibración de referencia (biblioteca del autor, 32 destilados de seguridad):
12 alta · 8 media · 12 fondo. Si un tema termina con 80% en `alta`, está
inflado.*

## Al cerrar cualquier trabajo en la biblioteca

1. Regenerar el índice (`biblio index`, o a mano).
2. Actualizar el `TEMA.md` del tema tocado: estado, contadores, qué sigue.
3. Si el workspace del usuario tiene su propio checklist de cierre
   (`LOG.md`, `NEXT.md`, etc.), respetarlo — **no imponer uno nuevo**.

## Errores a evitar

- Crear un tema por cada libro. Un tema es una disciplina, no una fuente.
- Meter operación en la biblioteca (auditorías, campañas con presupuesto, incidentes).
- Destilar sin `aplica_a` — un destilado que no apunta a ningún proyecto es
  inencontrable desde el trabajo, que es donde se necesita.
- Editar el `INDEX.md` a mano si el CLI está disponible: lo pisa al regenerar.
- Asumir rutas absolutas. Siempre el paso 0.
