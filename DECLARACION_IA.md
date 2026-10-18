# Declaración de uso de Inteligencia Artificial

# Actividad: Tarea 1 - Mini interprete
# Integrantes:
1. Flores Corona Astrid
2. Flores Leyva Ivone Alejandra
3. Ortiz Trujillo Jimena

# Fecha: 18/10/2026

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [ ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [ ✓ ] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta | Versión o modelo, si lo saben |
| ChatGPT | GPT-6,gratuito |
| | |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos | En qué parte del entregable |
| Organizar la división del trabajo entre los integrates y aclara las responsabilidades de cada parte. | Planificación de la Tarea 1.|
| Comprender los errores de las pruebas de Pytest y distinguir qué componente del intérprete podría estar relacionado con ellos. | Análisis de errores y revisión del parser, lexter y evaluator. |

> Sean específicos. *"Para la tarea"* no dice nada.
> *"Para generar las pruebas de `minimo_de_llaves`"* sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
(prompt 1)
Tengo este error en Pytest: AssertionError: assert 9 == 5 en test_asociatividad_izquierda_de_la_resta y un IndexError: list index out of range al probar expresiones incompletas en mi mini intérprete. No me des la solución completa directamente; explícame conceptualmente en qué componente del flujo (lexer, parser o evaluator) se está generando este comportamiento y qué concepto deberia revisar
```

```
(prompt 2)
Actúa como asesor de organización de proyectos académicos. Divide la **Tarea 1: Mini intérprete de expresiones** entre 3 integrantes de forma equilibrada, asegurando que todos participen en el análisis, las pruebas, el código y Git.

Considera los requisitos de la tarea: analizar lexer, parser, AST y evaluador; clasificar pruebas existentes; agregar pruebas normales, de límites y entradas inválidas; detectar y corregir errores; identificar 2 problemas de diseño e implementar una refactorización; evaluar Factory Method, Adapter o ninguno; completar `ANALISIS.md` y `DECLARACION_IA.md`; y entregar un PR con CI exitoso antes del 19 de octubre de 2026.

Entrega:
1. Responsabilidades de cada integrante.
2. Plan de trabajo y coordinación.
3. Checklist final de entrega.
4. Un prompt individual para cada integrante con instrucciones claras y paso a paso.

No inventes detalles del repositorio ni entregues toda la solución hecha. Prioriza la colaboración, los commits pequeños y descriptivos y la revisión mutua.
```

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta | ¿Aceptado, modificado o descartado? | Por qué | Dónde quedó (archivo / commit) |
| Una propuesta para dividir el trabajo de la Tarea 1 entre tres integrantes | Aceptada como propuesta de organización | Permitió estableceer responsabilidades para distribuir el análisis, las pruebas, las correcciónes, la refactorización y la documentación. La distribución se debe contrastar con el trabajo que realmente realizó cada integrante. | Organización del equipo; no corresponde necesariamente a un archivo o commit. |
| Una explicación conceptual de los errores de asociatividad de la resta y de las expresiones incompletas | Utilizada como orientación | Ayudó a identificar el parser como componente que debía investigarse y los conceptos de asociatividad y validación del final de la entrada. La explicación no sustituye la comprobación del código. | Análisis de errores y pruebas del intérprete; identificar los archivos y commits definitivos. |

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

| | |
|---|---|
| ¿Qué encontró la herramienta que ustedes **no** habían notado? | La consulta ayudó a relacionar el resultado incorrecto de la resta con la asociatividad de los operadores y el error de índice con el manejo de expresiones incompletas. Debemos confirmar qué aspectos no habíamos identificado antes de consultar la herramienta. |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | La explicación conceptual no demuestra por sí sola que el código esté bien diseñado ni que todos los defectos estén corregidos. También es necesario revisar la duplicación de código, la mantenibilidad y la correspondencia entre el análisis y la implementación. |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban *"no aplica"*.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Para verificar la correcta integración y funcionamiento del código, nosotras realizamos de manera autónoma el análisis de la lógica, la identificación y corrección de los errores, así como la incorporación de las pruebas necesarias. La IA se limitó estrictamente a las consultas específicas expresadas en los prompts anteriores (para resolver dudas conceptuales sobre fallos en las pruebas y organizar la dinámica de trabajo del equipo).

Para comprobar que el comportamiento del programa fuera el esperado, ejecutamos de forma local la suite de pruebas mediante el comando:
python -m pytest -v
Con esto obtuvimos 26 pruebas aprobadas, verificando que cada uno de los casos contemplados pasó exitosamente en nuestro entorno de desarrollo. Cabe destacar que somos conscientes de que el éxito de estas pruebas no garantiza de forma absoluta la cobertura total de posibles errores en el intérprete, pero nos dio la certeza de que los requerimientos evaluados funcionan correctamente.
---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

La IA nos ayudó a organizar las responsabilidades del equipo y a comprender conceptualmente los errores detectados en las pruebas del mini intérprete, como el problema de asociatividad de la resta y el manejo de expresiones incompletas. Sin embargo, sus explicaciones no sustituyen la revisión del código, ya que fue necesario identificar qué componentes estaban relacionados con los errores y comprobar el comportamiento del programa mediante las pruebas.

### 5.2 ¿Qué harían distinto la próxima vez?

En una próxima actividad, continuaremos trabajando de manera autónoma, analizando el código, realizando las pruebas e identificando los errores por nuestra cuenta. Después, consultaríamos a la IA para aclarar las dudas que surgieran durante l proceso y comprender mejor los conceptos relacionados con el lexer, el parser y el evaluador. De esta manera, fortaleceríamos nuestros conocimientos y utilizaríamos la IA como una herramienta de apoyo para confirmar o complementar nuestro análisis, en lugar de depender de ella para resolver los problemas.

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre | Número de cuenta |
|---|---|
| Flores Corona Astrid | |
|---|---|

|Flores Leyva Ivone Alejandra | 323129668 |
|---|---|

| Jimena Ortiz Trujillo | 323041991 |
|---|---|


