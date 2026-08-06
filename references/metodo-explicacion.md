# Método de explicación

La segunda puerta de entrada de la biblioteca. `destilar` procesa una fuente
(libro, curso, doc). `explicame` procesa **un concepto que apareció trabajando**.

Buena parte de lo que se aprende de verdad no entra por un libro: entra porque
algo se rompió, apareció un término desconocido, o hubo que decidir sin entender
del todo. Este método captura eso.

## Cuándo se usa

- Aparece un concepto desconocido en medio de un trabajo real
- Se tomó una decisión sin entender el fundamento y conviene cerrarlo
- Algo falló y la causa involucra un mecanismo que no está claro
- El usuario pregunta directamente "¿qué es X?" / "explicame X"

## Cómo se explica

**1. Anclar antes de explicar.** Empezar por lo que está pasando ahora, no por
la definición. *"Esto apareció porque el container llegó a una IP que no debería
— vamos a ver por qué puede."* Un concepto anclado a un problema propio se
retiene; una definición suelta, no.

**2. Explicar al nivel del que pregunta.** No al nivel del manual. Si la persona
sabe Linux y no sabe cloud, se apoya en lo que sabe: *"es como un servicio local
que responde en una IP fija"*. La analogía se usa para entrar, y después se
reemplaza por el mecanismo real — nunca se deja la analogía como respuesta final.

**3. Chequear DURANTE, no al final.** Cada 2-3 ideas, una pregunta corta. Si la
respuesta falla, se re-explica ahí mismo antes de seguir: acumular confusión hace
que el resto no entre. Esto no es el quiz — es el termómetro de si vale seguir
hablando.

**4. Pedir la reformulación.** Antes de cerrar: *"decímelo con tus palabras"*.
Es el paso que no se puede saltear. Una explicación que suena clara mientras se
escucha y no se puede reproducir 30 segundos después, no quedó.

**5. Transcribir textual lo que dijo.** Sus palabras exactas, sin corregirle la
redacción. La formulación propia es el dato: revela si el modelo mental es
correcto o solo suena correcto. *"el docker es la receta y el contenedor es
cuando ya esta corriendo"* dice muchísimo más que un ✅.

## Qué queda escrito

En `temas/<tema>/notas/<concepto>.md`:

```markdown
---
tema: <slug>
tipo: nota
tags: [concepto1, concepto2]
aplica_a: [proyecto]
relevancia: alta | media | fondo
estado: completo
fecha: YYYY-MM-DD
---

# <Concepto>

**Apareció en:** qué trabajo real lo trajo (con link al LOG del proyecto si existe)

## El mecanismo
La explicación, en el nivel que se dio. Sin relleno.

## Cómo lo explicó el usuario
> Cita textual de la reformulación.

**Ajuste:** qué faltó o qué estaba torcido (si aplica).

## Preguntas de control

| # | Pregunta | Última respuesta | Fecha | Estado |
|---|----------|------------------|-------|--------|
| 1 | ¿Por qué el container alcanza esa IP? | "comparten kernel y red del host" | 2026-06-12 | 🟢 |
| 2 | ¿Qué entrega el IMDS? | "no recuerdo" | 2026-06-12 | 🔴 |

🟢 sostenida · 🟡 parcial · 🔴 falló · ⬜ sin evaluar
```

## El banco de preguntas

La sección **`## Preguntas de control`** es lo que conecta la explicación con el
repaso. Sin ella, cada quiz inventa preguntas nuevas y nunca se comprueba si lo
explicado quedó.

Reglas:

- Las preguntas se escriben **cuando se explica**, no cuando se toma el quiz.
- 2-5 por concepto. Más que eso, el concepto era en realidad varios.
- Cada una apunta a **un mecanismo**, no a una definición. *"¿Por qué la regla
  funciona aunque el container esté comprometido?"* sirve; *"¿qué es iptables?"*
  no.
- El repaso posterior **saca de este banco** y actualiza la fila: respuesta
  textual nueva, fecha, estado.
- Una pregunta 🔴 vuelve en la ronda siguiente. Dos 🟢 seguidas y descansa.
- `biblio pendientes` las lista junto con los subtemas flojos.

## Anti-patrones

- **Explicar sin anclar.** Arranca en la definición, termina en el olvido.
- **Chequear solo al final.** Si se perdió en el minuto dos, los ocho siguientes
  fueron ruido.
- **Aceptar "sí, entendí".** No es una reformulación. La reformulación tiene que
  ser suya y hay que escucharla.
- **Corregirle la redacción al transcribir.** Se pierde exactamente el dato que
  importa.
- **No dejar preguntas de control.** La explicación queda como texto lindo que
  nadie vuelve a verificar. Es el fallo más común y el más caro.
