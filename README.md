# Biblioteca de Estudio

Un método para estudiar cualquier tema —anuncios, automatizaciones, inglés, lo
que sea— y que lo aprendido no termine en una carpeta de PDFs que nadie vuelve a
abrir.

No es un curso. Es un sistema que tu asistente de IA aplica: vos le pasás un
libro, un curso o la documentación de algo, y él lo convierte en material
accionable, te toma quiz cuando corresponde, y después podés preguntarle *"¿qué
de lo que estudié me sirve para esto?"* mientras trabajás.

## Cómo instalarlo

Abrí **[MASTERPROMPT.md](MASTERPROMPT.md)** y seguí lo que dice. Son dos pasos.

## Qué hay acá

| Archivo | Qué es |
|---------|--------|
| [`SKILL.md`](SKILL.md) | El método que aplica tu asistente |
| [`references/estructura-canonica.md`](references/estructura-canonica.md) | Cómo se arma un tema de estudio |
| [`references/metodo-destilado.md`](references/metodo-destilado.md) | Cómo convertir un libro en algo accionable |
| [`references/metodo-repaso.md`](references/metodo-repaso.md) | Cómo tomarte un quiz honesto |
| [`scripts/biblio.py`](scripts/biblio.py) | Opcional — acelera, no es necesario |

**Podés leer todo desde acá antes de instalar nada.** Los archivos están
escritos para ser leídos, no solo ejecutados. Si tu asistente quiere revisarlos
primero, mejor.

## Qué no hace

Importa tanto como lo que sí hace:

- **No toca tu configuración.** Ni `~/.claude/`, ni el PATH, ni variables de entorno.
- **No instala dependencias.** El script usa solo la librería estándar de Python. Sin `pip`, sin internet.
- **No ejecuta nada al copiarse.** No hay instalador ni scripts de arranque.
- **No toca tus archivos.** Crea una carpeta nueva y trabaja solo ahí.
- **No manda nada afuera.** Todo queda en tu disco.

## Cómo funciona

Un tema no es una carpeta de PDFs. Es un ciclo:

```
fuente → destilado → nota → práctica → repaso → aplicación
```

Si falta la **práctica**, es lectura. Si faltan los **repasos**, no hay forma de
saber si quedó algo. Si falta la **aplicación**, es un hobby y no una inversión.

Cada tema se arma igual, sea seguridad informática o inglés de negocios:

```
temas/<tema>/
├── TEMA.md            qué es, en qué fase estás
├── ROADMAP.md         las fases, cada una con criterio de "hecho"
├── fuentes/           el catálogo + los destilados
├── notas/             qué aprendiste de cada concepto
├── repasos/           cuánto entendiste de verdad (con score)
├── practica/          qué hiciste realmente
└── aplicacion/        cómo baja esto a tu trabajo
```

## Las tres reglas

1. **Un tema no es un libro, es una disciplina.** Los libros son fuentes; el tema
   es lo que querés poder hacer.
2. **Lo que se estudia se practica y se evalúa.** Un tema sin práctica ni quizzes
   es lectura disfrazada de estudio.
3. **Lo aprendido apunta a tus proyectos.** Cada cosa que guardás lleva un campo
   `aplica_a`, así después podés preguntar *"¿qué sé que me sirva para esto?"* en
   vez de tener que acordarte.

## Requisitos

Un asistente de IA con acceso a los archivos de tu computadora (Claude Code,
Claude Desktop con acceso a carpetas, o similar). Python 3 es opcional.

## Licencia

MIT — ver [LICENSE](LICENSE).
