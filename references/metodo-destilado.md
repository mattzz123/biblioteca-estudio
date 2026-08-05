# Método de destilado

El estándar que produjo los 32 destilados del tema de seguridad de la biblioteca
original (13.111 líneas de material accionable).

## Qué es un destilado

**No** es un resumen. Un resumen conserva la estructura del autor; un destilado
conserva solo **lo que cambia una decisión propia**.

Prueba de corte para cada párrafo candidato: *"¿esto haría que hagamos algo
distinto en algún proyecto?"* Si la respuesta es no, no entra.

## Estructura

```markdown
---
tema: <slug>
tipo: destilado
fuente: "Título — Autor"
tags: [tag1, tag2]
aplica_a: [proyecto1]        # 1-3 máximo, [] si es fundamento general
relevancia: alta | media | fondo
estado: completo | parcial
fecha: YYYY-MM-DD
---

# <Título> — destilado

**Fuente:** autor, año, edición
**Por qué este libro:** 1-2 líneas — qué problema nuestro resuelve
**Veredicto:** vale / vale por partes / no vale (y por qué)

## Ideas centrales
Las 3-7 tesis del autor, en una frase cada una.

## Lo accionable
| # | Acción | Aplica a | Prioridad |
|---|--------|----------|-----------|
Cada fila debe ser verificable: "rotar credenciales de X" sí,
"mejorar la seguridad" no.

## Conceptos que hay que entender
Los que requieren estudio aparte → generan archivo en `notas/`.

## Lo que NO aplica a nosotros
Explícito. Ahorra releer el libro para descubrir lo mismo.

## Citas que valen textual
Solo si la formulación exacta importa.
```

## Reglas

1. **Un destilado por fuente**, nombre = slug de la fuente, no del tema.
2. **≤25KB.** Si excede, dividir por parte del libro (`-parte-1.md`).
3. **`aplica_a`: 1-3 proyectos como máximo.** El criterio es "¿cambiaría una
   decisión concreta ahí?", no "¿tiene que ver con?". Un campo que matchea con
   todos los proyectos no discrimina nada y rompe la búsqueda por proyecto.
   Fundamento general → `aplica_a: []` + `relevancia: fondo`. Eso no es un
   defecto del destilado: hay material que se estudia para tener criterio, no
   para ejecutar algo el martes.
4. **Los ítems de "Lo accionable" suben** a `aplicacion/CHECKLIST.md` del tema,
   citando el destilado de origen.
5. **Alta en `fuentes/INDEX.md`** con estado `destilado` en la misma sesión.
6. Si un capítulo no produce nada accionable, decirlo: *"cap. 7-9: teoría de
   fondo, sin ítems"*. Es información útil.

## Fuentes que no son libros

| Tipo | Qué cambia |
|------|-----------|
| Curso | "Lo accionable" sale de los ejercicios, no de las clases |
| Doc oficial | El veredicto incluye versión/fecha — envejece rápido |
| Paper | Agregar sección "qué se probó y con qué muestra" |
| Canal/creador | No se destila por video: se destila el criterio recurrente |
| Research interno | Conservar el método de verificación en el frontmatter |

## Anti-patrones

- Destilar mientras se lee por primera vez → sale un resumen, no un destilado.
- Copiar el índice del libro como esqueleto → estructura del autor, no propia.
- "Interesante para el futuro" sin proyecto → ruido inencontrable.
