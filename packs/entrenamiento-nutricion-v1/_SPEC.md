# Spec — pack entrenamiento + nutrición desde cero (v1)

Destino: una persona que arranca de CERO (no sabe qué es una serie, una repetición, una caloría).
La enseña un agente con la skill /biblioteca. El archivo de nivel es el material del docente.

## Reglas de contenido
- CERO datos personales de la persona de origen: nada de sus labs (LDL, HbA1c, B12, vit D), su peso, su rutina A/B/C,
  sus compras, su app, sus fechas, sus frases ("Cómo lo explicó la persona de origen" NO se copia), marcas 🟢🟡🔴,
  nombres de personas. Donde la nota trae un valor personal de LDL → generalizar ("si tu LDL subió...").
- Se conserva TODO el mecanismo y los datos técnicos/científicos (cifras de estudios, umbrales, fórmulas).
- Preguntas generalizadas (sin el caso específico de la persona de origen). Se pueden usar "vos" y el caso del alumno en genérico.
- Ordenar preguntas de fácil (definición/mecanismo básico) a difícil (aplicación/deducción).
- Cada pregunta lleva su respuesta esperada corta (1-3 líneas) para que el docente corrija.
- Español rioplatense (voseo), igual que las notas.
- No inventar contenido que no esté en las notas fuente, salvo en temas marcados "sin contenido previo".

## Formato del archivo de nivel (`NIVEL_N_<slug>.md`)

```
---
pack: entrenamiento-nutricion
version: 1
nivel: N
titulo: "<título>"
requisito: "Nivel N-1 cerrado (prueba de cierre cumplida)"   # nivel 1: "ninguno"
---

# Nivel N — <título>

**Para qué sirve este nivel:** 1-2 líneas.
**Al terminar, el alumno puede:** 3-5 bullets verificables.

---

## Tema N.1 — <título>
*Origen: `temas/<tema>/notas/<archivo>.md`*

### Vocabulario nuevo
- término — definición en una línea (sólo lo que aparece por primera vez)

### Material para enseñar
Pasos numerados, UNA idea por paso. Cada paso: la idea + el porqué (mecanismo).
Donde ayude, `> Ancla observable:` algo que el alumno puede ver/probar en su casa o gimnasio.

### Preguntas de repaso (fácil → difícil)
1. <pregunta>
   **Respuesta esperada:** <...>

### Prueba práctica del tema
Tarea en la vida real con criterio verificable (del ROADMAP de origen).

---
(siguiente tema)

## Prueba de cierre del nivel
Qué tiene que demostrar para pasar al nivel siguiente (combina las del nivel).
```

## Cómo se enseña (vale para todos los niveles — va en README, no repetir)
Una idea por mensaje + confirmación · si no entiende, anclar a algo observable (no simplificar más el texto) ·
cerrar pidiendo que lo explique con sus palabras · preguntas de a una, corrección inmediata ·
el repaso se toma después de practicar, no después de leer.
