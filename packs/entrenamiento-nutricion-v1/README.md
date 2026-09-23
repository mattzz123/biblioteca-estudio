# Pack — Entrenamiento de fuerza + Nutrición, desde cero (v1)

Curso escalonado para una persona que **arranca de cero**: no sabe qué es una serie,
una repetición ni una caloría. Primero construye el modelo de cuerpo, biología y
nutrición; el gimnasio queda deliberadamente para el último tramo.

Lo enseña un agente con la skill `/biblioteca`. Cada `NIVEL_N_*.md` es el material
del docente: qué explicar, en qué orden, las preguntas con su respuesta esperada y
la prueba práctica que cierra cada tema.

## Recorrido pedagógico

Los archivos de nivel son módulos de contenido. El docente los recorre así:

1. **Cuerpo y energía:** energía, macros, gasto del cuerpo y micronutrientes (`N1.2 → N3.4 → N6.1`).
2. **Nutrición:** proteína, calidad de la comida, carbohidratos, fibra, fruta, etiquetas y restaurantes (`N2.3–N2.4 → N4.1–N4.4`).
3. **Biología cotidiana:** sueño, hidratación, recuperación, timing, alcohol y lectura prudente de análisis (`N3.2–N3.3 → N6.3–N6.4`).
4. **Cocina segura:** conservación, microbios y envases (`N5.1–N5.3`).
5. **Recién al final, gimnasio:** crecimiento muscular, rutinas, ejercicios, fatiga, fallo, RIR, progresión y registro (`N1.1/N1.3 → N2.1–N2.2 → N3.1 → N6.2`).

No se deben enseñar los bloques del punto 5 antes de cerrar los cuatro primeros.

## Los 6 módulos

| Nivel | Para qué | Temas |
|---|---|---|
| **1 · Arrancar** | Lo mínimo antes de pisar el gimnasio | Por qué crece el músculo · calorías y macros · volumen, intensidad y frecuencia |
| **2 · Armar la semana** | Leer o armar una rutina y un plan de comida | Rutina por grupos vs cuerpo completo · elegir ejercicios · qué mirar primero al comer · calidad de la proteína |
| **3 · Sostenerlo** | Recuperarse y no abandonar | Fatiga y fallo (reps en reserva) · sueño · hidratación · cuánto gasta el cuerpo |
| **4 · Decidir solo** | Supermercado y restaurantes | Leer etiquetas · comer afuera · carbohidratos · fruta y fibra |
| **5 · Cocina y preparación** | Preparar comida sin enfermarse | Conservación · microbios en la comida · envases |
| **6 · Avanzado** | El cuerpo como sistema | Vitaminas y minerales · progresión · horarios de comida y alcohol · leer un análisis de sangre |

**Regla de avance:** no se pasa de nivel sin cumplir la *prueba de cierre* del nivel.
Leer no cierra nada; lo cierra hacer algo en la vida real.

**Temas con requisito de tiempo** (nivel 6):
- *Progresión* necesita 3-4 semanas registrando cada serie (fecha, ejercicio, peso, reps).
- *Análisis de sangre* necesita un análisis nuevo para comparar con uno anterior.

Los temas 6.2, 6.3 y 6.4 nacieron como borradores, pero ya fueron revisados contra
fuentes y corregidos. El docente debe conservar la secuencia pedagógica anterior.

## Cómo se enseña (lo que hace que funcione)

Esto no está en ningún archivo de nivel porque vale para todos:

1. **Una idea por mensaje.** Explicar una sola cosa y confirmar que la entendió antes
   de sumar la siguiente. No apilar dos metáforas para el mismo concepto.
2. **Si dice "no entendí", no repetir más simple de un tirón.** Partirlo en preguntas
   cortas de una sola idea ("¿la fibra suma calorías o no?") y avanzar sólo cuando confirma.
3. **Si todavía no prende, anclar a algo que pueda ver o probar él mismo.**
   Ejemplo: grasas → "¿es sólida o líquida a temperatura ambiente?" (manteca vs aceite),
   y recién después el porqué molecular. Las `> Ancla observable:` de cada nivel son eso.
4. **Anclar a su propio caso.** Antes de explicar, preguntar por su rutina, su comida,
   su objetivo, y usar esos datos como ejemplo. Guardarlos en su memoria, no en el pack.
5. **Cerrar pidiendo que lo explique con sus palabras.** Transcribirlo textual en su
   nota, sin corregirle la redacción; corregir sólo el concepto si está mal.
6. **Repaso: una pregunta por vez**, corrección inmediata, sin adelantar la siguiente.
   Se toma **después de practicar**, no después de leer. Marcar 🟢 sólido · 🟡 casi · 🔴 reforzar.

## Límites de seguridad

- La dosis de cualquier suplemento la define el médico, no el curso.
- Las primeras 4-6 semanas **no se fuerza el peso**: el tendón se adapta en semanas,
  el músculo en meses. El punto permanente es dejar 2-3 repeticiones en reserva, no el fallo.
- Rangos de laboratorio: los del propio laboratorio y la lectura del médico.
- Nada de déficit calórico agresivo: comer menos de lo que se gasta, no "no comer".

## Instalar

Copiar la carpeta dentro de la biblioteca de la persona y crear los dos temas con
`biblio new entrenamiento ...` y `biblio new nutricion ...`. A medida que avanza, sus
propias notas (con sus datos y sus reformulaciones) van en `temas/<tema>/notas/` —
el pack queda intacto como material de referencia.
