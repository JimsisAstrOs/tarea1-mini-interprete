# Análisis — Tarea 1

**Integrantes:**
1. Flores Corona Astrid
2. Flores Leyva Ivone Alejandra
3. Ortiz Trujillo Jimena

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | Una cadena con una expresión aritmética | Una lista de tokens con su tipo, valor y posición en el texto | Reconocer números, operadores y paréntesis; ignorar espacios en blanco y convertir el texto en tokens |
| `parser` | Una lista de tokens que genera el lexer | Un AST que representa la expresión | Analizar la estructura de la expresión, comprobar la sintaxis y respetar la precedencia de los operadores y la agrupación indicada por los paréntesis |
| `ast` | Los valores de los números y las operaciones que se deben representar | Objetos que representan números (Numero) y operaciones binarias (OperacionBinaria) | Definir las estructuras de datos que permiten representar la expresión mediante un árbol |
| `evaluator` | Los valores de los números y las operaciones que se deben representar | El resultado numérico de evaluar la expresión | Recorrer el árbol, ejecutar las operaciones aritméticas y generar un ErrorDeEvaluacion cuando se intenta dividir entre cero |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | [PAR_IZQ("("), NUMERO(3), MAS("+"), NUMERO(4), PAR_DER(")"), POR("*"), NUMERO(2)] |
| AST | OperacionBinaria("*", OperacionBinaria("+", Numero(3), Numero(4)), Numero(2)) |
| resultado | 14 |

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
|---|---|---|---|---|
| test_tokeniza_un_numero_solo | Lexer | Reconocimiento de un número y comprobación del token completo | 0 | Normal|
| test_tokeniza_una_suma | Lexer | Reconocimiento y orden de los tokens de una suma; comprueba valores y posiciones | 1 | Normal |
| test_los_espacios_no_producen_tokens | Lexer | Los espacios no aumentan la cantidad de tokens | 1 | Normal |
| test_tokeniza_parentesis | Lexer | Reconocimiento y orden de los tipos de token de los paréntesis y el número | 0 | Normal |
| test_construye_el_arbol_de_una_suma | Parser | Construcción del AST de una suma. | 1 | Normal |
| test_la_multiplicacion_se_agrupa_antes_que_la_suma | Parser | Comprueba la precedencia de la multiplicación sobre la suma en el AST. | 2 | Normal |
| test_los_parentesis_cambian_la_agrupacion | Parser | Comprueba que los paréntesis cambien la estructura del AST. | 2 | Normal |
| test_suma | Evaluador | Evalúa correctamente una suma. | 1 | Normal |
| test_resta | Evaluador | Evalúa correctamente una resta. | 1 | Normal |
| test_multiplicacion | Evaluador | Evalúa correctamente una multiplicación. | 1 | Normal |
| test_division | Evaluador | Evalúa correctamente una división. | 1 | Normal |
| test_precedencia_sin_parentesis | Evaluador | Respeta la precedencia de la multiplicación sobre la suma. | 2 | Normal |
| test_precedencia_con_parentesis | Evaluador | Respeta la agrupación indicada por los paréntesis. | 2 | Normal |


### 2.2 ¿Qué comportamientos **no** estaban probados?
 Los principales casos que no estaban probados son los siguientes:

1. Operaciones aritméticas y reglas de agrupación

* No se comprueba si las operaciones de la misma precedencia se evalúan de izquierda a derecha, como, 10 - 3 - 2 o 16 / 4 / 2.
* No se comprueba la precedencia de la división sobre la suma o la resta.
* No se prueba la división con un resultado decimal, por ejemplo, 10 / 4, que se espera 2.5.
* No se comprueba qué sucede cuando se intenta dividir entre cero, por ejemplo, 8 / 0, debe producirse un ErrorDeEvaluacion.

2. Números y espacios en blanco

* No se comprueba que los números con ceros a la izquierda conserven su valor numérico, por ejemplo, que 007 se interprete como 7.
* Aunque existe una prueba sobre los espacios, no se comprueba si se ignoran otros espacios en blanco, como tabulaciones o saltos de línea, en diferentes posiciones de una expresión.

3. Entradas inválidas y errores de sintaxis

* No se comprueba qué sucede cuando se introduce un carácter no reconocido, como @.
* No se comprueba si el intérprete rechaza expresiones con números consecutivos sin un operador, como 3 4.
* No se prueban expresiones vacías o formadas únicamente por espacios.
* No se comprueba el comportamiento ante paréntesis sin cerrar o paréntesis de cierre sin apertura, por ejemplo, (3 + 4 o 3 + 4).
* No se verifica que se rechacen expresiones incompletas, como 3 +, ni que se rechace el signo negativo unario, como en -3, ya que no está admitido.
* No se comprueba que los errores de sintaxis indiquen correctamente la posición del texto donde se encuentra el problema.

4. Procesamiento de la expresión completa

* No se comprueba que el intérprete procese todos los tokens de la entrada y rechace aquellos que queden sin utilizar.
* No se prueban combinaciones más variadas de operadores, números y paréntesis que permitan verificar conjuntamente las reglas de precedencia y agrupación.

En conclusión, las pruebas originales se concentran principalmente en expresiones válidas y sencillas. Faltan pruebas para los casos límite, las entradas inválidas y algunas reglas específicas del proyecto. Estos comportamientos constituyen candidatos para diseñar nuevas pruebas, detectar posibles defectos y comprobar que el intérprete cumple las especificaciones.

---

## 3. Las pruebas que agregaron

### 3.1 ¿Cuáles son casos normales, cuáles frontera y cuáles inválidos?

| Prueba (archivo::nombre) | Entrada |	Esperado |	Categoría |	¿Por qué esa categoría? |
|---|---|---|---|---|
| test_casos_adicionales.py::test_division_con_resultado_decimal |  10 / 4 |  Resultado 2.5. | Normal | Comprueba el funcionamiento habitual de la división cuando el resultado es decimal.|
|test_casos_adicionales.py::test_precedencia_de_division_sobre_suma | 8 + 12 / 4 |  Resultado 11.0. | Normal | Comprueba que la división se realice antes que la suma, de acuerdo con las reglas de precedencia.|
| test_casos_adicionales.py::test_asociatividad_izquierda_de_la_resta | 10 - 3 - 2 |  Resultado 5. |  Normal | Comprueba la agrupación de operaciones consecutivas de resta. Aunque es una expresión válida, también permite detectar un posible defecto en el parser. |
| test_casos_adicionales.py::test_numero_con_ceros_a_la_izquierda | 007 | Resultado 7. |  Frontera | Comprueba un formato especial de número: los ceros iniciales no deben modificar su valor numérico. |
| test_casos_adicionales.py::test_expresion_con_tabulaciones_y_espacios | 3   +   4 | Resultado 7. |  Frontera  | Comprueba el tratamiento de distintos espacios en blanco y su ubicación dentro de una expresión. |
|test_casos_adicionales.py::test_division_entre_cero  | 8 / 0 | Se lanza ErrorDeEvaluacion. | Frontera  | Comprueba el caso especial en el que el divisor es cero, condición que debe generar un error de evaluación. | 
| test_casos_adicionales.py::test_expresion_con_cero  | 0 + 5 | Resultado 5.  | Frontera  | Comprueba que el cero se acepte como operando y se procese correctamente. |
| test_casos_adicionales.py::test_caracter_no_reconocido  | 3 @ 4 | Se lanza ErrorDeSintaxis. | Inválida  | Contiene un carácter que no pertenece al lenguaje admitido; la expresión debe rechazarse. |
| test_casos_adicionales.py::test_numeros_consecutivos_sin_operador | 3 4 | Se lanza ErrorDeSintaxis. | Inválida  | Contiene dos números consecutivos sin un operador que los conecte. |
| test_casos_adicionales.py::test_expresion_incompleta  | 3 + | Se lanza ErrorDeSintaxis. | Inválida  | La expresión termina sin incluir el operando derecho requerido por el operador +. |
| test_casos_adicionales.py::test_parentesis_sin_cerrar | (3 + 4  | Se lanza ErrorDeSintaxis. | Inválida  | Falta el paréntesis de cierre necesario para completar la expresión. |
| test_casos_adicionales.py::test_signo_negativo_unario | -3  | Se lanza ErrorDeSintaxis. | Inválida  | El signo negativo unario no está admitido por las especificaciones del intérprete. |
---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

1. El `lexer` ignoraba caracteres inválidos (como `@`) y el `parser` no comprobaba si quedaban tokens sin consumir al final (`3 4`).
2. El `parser` asociaba la resta y la división encadenadas hacia la derecha (`10 - 3 - 2`).
### 4.2 ¿Por qué el comportamiento observado era incorrecto?
1. `"3 @ 4"` devolvía `3` porque el lexer simplemente ignoraba el caracter no reconocido en su cláusula `else` y el parser devolvía el primer número sin verificar el resto de la entrada.
2. `"10 - 3 - 2"` devolvía `9` en lugar de `5` porque `_expresion()` realizaba recursión hacia la derecha, agrupando la expresión como `10 - (3 - 2)`.
### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar |
|---|---|---|---|
| Caracter no reconocido ignorado | `3 @ 4` | 3 | ErrorDeSintaxis |
| Tokens sobrantes no validados | `3 4` | 3 | ErrorDeSintaxis |
| Expresión incompleta causa crash | `3 +` | IndexError | ErrorDeSintaxis |
| Asociatividad a la derecha | `10 - 3 - 2` | 9 | 5 |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

Porque la corrección atacó la raíz del problema en la arquitectura:
- Se reemplazó la recursión a la derecha por bucles `while` iterativos que encadenan los nodos a la izquierda sin importar cuántas operaciones consecutivas existan.
- Se agregó una validación explícita al final de `parsear()` que garantiza que el 100% de los tokens consumidos pertenezcan a la expresión válida.
- Se agregaron comprobaciones de límites en `_avanzar()` para lanzar `ErrorDeSintaxis` controlado en lugar de dejar escapar excepciones nativas de Python (`IndexError`).

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

1. **Duplicación de código en `Parser`:** Los métodos `_expresion()` y `_termino()` tenían la misma estructura iterativa repetida para asociar operandos y operadores de un mismo nivel.
2. **Rigidez / Múltiples condicionales en `Evaluator`:** En `evaluator.py`, la función `evaluar()` usa bloques `if` encadenados para determinar la operación según la cadena del operador, lo que dificulta extender nuevos operadores sin modificar el evaluador directo.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?
Se aplicó **Extract Method** en `Parser`, creando la función auxiliar `_parsear_operacion_binaria()`. Conserva el comportamiento exactamente igual porque procesa los mismos tokens y genera la misma estructura de nodos `OperacionBinaria` en el AST, garantizando que todas las pruebas existentes sigan pasando (`pytest` en verde).

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?
**Ninguno es pertinente.**
- **Factory Method:** La creación de nodos del AST (`Numero`, `OperacionBinaria`) y `Token` es directa, simple y concreta. No hay familias de objetos ni subclases dinámicas que justifiquen este patrón.
- **Adapter:** No existen librerías de terceros ni interfaces externas incompatibles que requieran una adaptación.
### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?
El **Parser** y el **Evaluator**:
1. En `tokens.py` y `lexer.py`: Definir el nuevo tipo de token y su mapeo.
2. En `parser.py`: Agregar el token a las tuplas de operadores o definir una nueva regla de precedencia.
3. En `evaluator.py`: Modificar el bloque condicional en `evaluar()` para dar soporte al nuevo símbolo.
## Antes de la declaración: inténtenlo primero ustedes

Usar IA o no es decisión de cada quien, y el curso la permite. Pero **les
pedimos, por favor, que primero hagan el análisis por su cuenta.**

No es una prueba de honestidad. Es que el orden cambia lo que aprenden:

1. **Primero ustedes.** Lean el código, corran las pruebas, escriban sus
   respuestas. Aunque queden incompletas, aunque no encuentren todo.

2. **Después, si quieren, la IA** — pero como contraste, no como sustituto.
   Y entonces contesten dos preguntas, en `DECLARACION_IA.md`:

   - **¿Qué encontró que ustedes no habían notado?**
     Eso es aprendizaje, y se declara sin ninguna pena.

   - **¿Qué *no* encontró, que en este curso sí consideramos un problema?**
     Ésta es la interesante. Una herramienta suele decir que el código
     "funciona bien" y no señalar, por ejemplo, la **duplicación** — porque
     duplicar no rompe nada, el programa corre igual. Pero ustedes ya saben
     por qué eso sí es un mal diseño, y saben nombrarlo. La herramienta no
     tomó esa clase.

> Si invierten el orden se pierden justamente lo segundo: **no se puede notar
> lo que a una herramienta le faltó si uno nunca se formó una opinión propia
> antes de preguntarle.** Y que un programa funcione no implica que esté bien
> diseñado — eso lo dijimos en clase mucho antes de esta tarea.

---

## Declaración de uso de Inteligencia Artificial

Va en `DECLARACION_IA.md`, no aquí. Es obligatoria, pero **no da ni quita
puntos**: es un reporte adicional que se revisa aparte y se les devuelve con
comentarios.

**No se evalúa cuánta IA usaron.** Se evalúa si pueden dar cuenta de lo que
entregaron. *"No usamos"* es una declaración válida y completa; *"lo
descartamos porque..."* es de las mejores respuestas posibles.
