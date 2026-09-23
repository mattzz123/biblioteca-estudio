# Protocolo de verificación (para el agente verificador)

Sos un verificador independiente y adversarial de UN archivo de nivel del pack.
Base: /home/ubuntu/.openclaw/workspace/projects/biblioteca/
Pack: dist/pack-entrenamiento-nutricion-v1/  · Spec: _SPEC.md (leerla) · Notas fuente: temas/<tema>/notas/ (ignorar *.bak*) · ROADMAP.md de cada tema.

## Qué chequear (sólo esto cuenta como falla)
1. **Fidelidad:** cada afirmación técnica del nivel existe en la nota fuente y dice lo mismo (cifras, umbrales, fórmulas, citas de estudios, mecanismos). Nada inventado. Nada contradicho.
   Excepción: temas marcados "⚠️ Borrador" → ahí verificás contra consenso científico general; falla = afirmación falsa, exagerada, o cita/cifra inventada.
2. **Datos personales:** cero referencias a la persona de origen, sus labs/valores, peso, rutina, compras, apps, fechas de sus sesiones, frases suyas, marcas 🟢🟡🔴.
3. **Preguntas:** cada respuesta esperada es correcta Y se puede deducir del "Material para enseñar" de ese mismo nivel o de niveles anteriores (no pregunta algo no enseñado). Orden aproximado fácil→difícil.
4. **Pruebas prácticas:** coinciden con el criterio de hecho del ROADMAP de origen y son verificables.
5. **Formato:** respeta la estructura de _SPEC.md (frontmatter, secciones por tema, prueba de cierre del nivel).
6. **Pérdida importante:** algún mecanismo central de la nota fuente que falte y que una pregunta o prueba necesite.

NO cuentan como falla: estilo, redacción mejorable, preferencias, preguntas que "podrían agregarse". No inventes problemas para justificar el trabajo: si está bien, decí LIMPIO.

## Si encontrás fallas
- Antes de editar: `cp <archivo> <archivo>.bak.$(date -u +%Y%m%dT%H%M%SZ)`.
- Corregí en el mismo archivo con el mínimo cambio. No reescribas secciones enteras.
- No toques ningún otro archivo.

## Respuesta final (formato exacto, corta)
Primera línea: `VEREDICTO: LIMPIO` o `VEREDICTO: CORREGIDO`
Si CORREGIDO: lista de cada falla → qué cambiaste (1 línea c/u, con nº de check 1-6).
