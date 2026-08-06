# Método de repaso

Sistema de auto-evaluación ligado a trabajo real. Nació estudiando seguridad de
sistemas y se generalizó a cualquier tema.

## Cuándo se toma

**Después de trabajo real, no después de leer.** El disparador es haber
arreglado algo, lanzado algo o roto algo — no haber terminado un capítulo.

Ejemplos válidos: se corrigió la idempotencia de un bot → quiz de idempotencia.
Se lanzó una campaña con CAPI → quiz de Pixel/atribución.

## De dónde salen las preguntas

**Del banco, no de la imaginación.** Las notas escritas con `explicame` llevan
una sección `## Preguntas de control` con las preguntas que se hicieron mientras
se explicaba, y la respuesta textual de esa vez.

El quiz **saca de ahí**: re-pregunta sobre las mismas formulaciones para ver si
las sostiene semanas después. Esa es la diferencia entre medir comprensión y
medir memoria reciente. Preguntas nuevas se agregan solo si el trabajo real trajo
un ángulo que el banco no cubre.

Al terminar, se actualiza la fila del banco en `notas/<concepto>.md`: respuesta
textual nueva, fecha, estado.

## Antes de armar la ronda

```bash
biblio pendientes
```

Lista, ordenado por antigüedad: los subtemas en 🔴/🟡 de `repasos/INDEX.md`, las
**preguntas de control** en 🔴/🟡 de las notas, y señales de desbalance (leído sin
evaluar, ratio lectura/práctica, temas pausados).

**Los rojos viejos entran sí o sí.** El sistema de repaso es reactivo por diseño
—se dispara con trabajo real— y eso tiene un agujero: un subtema que cayó en
rojo y cuyo tema no se volvió a tocar se queda en rojo para siempre. `biblio
pendientes` es lo que cierra ese agujero. Un rojo de hace 50 días es material
que se dio por estudiado y no lo está.

Mezcla recomendada por ronda: **la mitad de los pendientes viejos, la mitad del
trabajo reciente.**

## Cómo se ejecuta

1. **Una pregunta por vez.** No adelantar la siguiente ni mostrar la lista.
2. **El usuario responde con sus palabras.** **No hay opción múltiple** — el objetivo es
   detectar comprensión, no reconocimiento.
3. **Corrección inmediata** tras cada respuesta: qué estuvo bien, qué faltó, cuál
   era la respuesta completa. Sin suavizar: un ⚠️ dicho como ✅ no sirve.
4. 6-10 preguntas por ronda. Más que eso, cae la calidad de las respuestas.
5. Al final: score, tabla de estado por subtema, y "para reforzar".

## Formato del archivo

`repasos/YYYY-MM-DD-<subtema-principal>.md`

```markdown
---
tema: <slug>
tipo: repaso
tags: [subtema1, subtema2]
aplica_a: [proyecto]
estado: completo
fecha: YYYY-MM-DD
---

# Repaso YYYY-MM-DD — <subtemas>

**Trabajo real que lo originó:** <qué se arregló/lanzó>

## Preguntas

### 1. <pregunta>
**Respuesta del usuario (textual):** ...
**Corrección:** ...
**Repaso:** ...        ← solo si falló: la re-explicación, en el momento
**Resultado:** ✅ / ⚠️ / ❌

## Score
X/10

## Para reforzar
- <subtema> — <qué exactamente falló>
```

La respuesta se transcribe **textual**, no parafraseada. La formulación propia
es el dato: revela si el modelo mental es correcto o solo suena correcto.

El campo **`Repaso:`** aparece solo cuando la respuesta falló, y lleva la
re-explicación dada en el momento. Un ❌ sin `Repaso:` es una nota de que algo no
se sabe; con `Repaso:`, es una segunda oportunidad de que entre. No se posterga
para después: el momento en que quedó expuesto el hueco es el momento en que la
explicación pega.

## Actualizar el INDEX

`repasos/INDEX.md` lleva dos tablas:

1. **Historial** — fecha · subtemas · trabajo real · score · para reforzar
2. **Progreso por subtema** — 🟢 sólido · 🟡 casi · 🔴 reforzar + última eval

Un subtema en 🔴 debe volver a caer en la ronda siguiente. Si aprueba dos rondas
seguidas, pasa a 🟢.

## Anti-patrones

- Preguntar lo que se acaba de leer → mide memoria de corto plazo, no comprensión.
- Aceptar una respuesta parcial como correcta para no frustrar → el sistema pierde
  todo su valor. El score sirve solo si es honesto.
- Quiz sin trabajo real detrás → sin anclaje, se olvida igual.
