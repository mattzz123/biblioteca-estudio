# Método de repaso

Sistema de auto-evaluación ligado a trabajo real. Nació estudiando seguridad de
sistemas y se generalizó a cualquier tema.

## Cuándo se toma

**Después de trabajo real, no después de leer.** El disparador es haber
arreglado algo, lanzado algo o roto algo — no haber terminado un capítulo.

Ejemplos válidos: se corrigió la idempotencia de un bot → quiz de idempotencia.
Se lanzó una campaña con CAPI → quiz de Pixel/atribución.

## Antes de armar la ronda

```bash
python3 scripts/biblio.py pendientes     # si el CLI está disponible
grep -rh "🔴\|🟡" temas/*/repasos/INDEX.md   # equivalente manual
```

Lista los subtemas en 🔴/🟡 de todos los temas ordenados por antigüedad, más
señales de desbalance (leído sin evaluar, ratio lectura/práctica, temas pausados).

**Los rojos viejos entran sí o sí.** El sistema de repaso es reactivo por diseño
—se dispara con trabajo real— y eso tiene un agujero: un subtema que cayó en
rojo y cuyo tema no se volvió a tocar se queda en rojo para siempre. `biblio
pendientes` es lo que cierra ese agujero. Un rojo de hace 50 días es material
que se dio por estudiado y no lo está.

Mezcla recomendada por ronda: **la mitad de los pendientes viejos, la mitad del
trabajo reciente.**

## Cómo se ejecuta

1. **Una pregunta por vez.** No adelantar la siguiente ni mostrar la lista.
2. Matías responde con sus palabras. **No hay opción múltiple** — el objetivo es
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
**Respuesta de Matías (textual):** ...
**Corrección:** ...
**Resultado:** ✅ / ⚠️ / ❌

## Score
X/10

## Para reforzar
- <subtema> — <qué exactamente falló>
```

La respuesta se transcribe **textual**, no parafraseada. La formulación propia
es el dato: revela si el modelo mental es correcto o solo suena correcto.

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
