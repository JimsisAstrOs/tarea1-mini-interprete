# Análisis — Tarea 1

**Integrantes:**
1.
2.
3.

**Fork:**
**Rama:**

> Contesten en este archivo. Respuestas breves y concretas: se califica que
> hayan entendido, no la extensión.

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | | | |
| `parser` | | | |
| `ast` | | | |
| `evaluator` | | | |

### 1.2 ¿Qué recorrido sigue una expresión desde que se recibe como texto hasta que produce un resultado?

> Usen `(3 + 4) * 2` como ejemplo y muestren cómo se ve entre etapa y etapa.

| Etapa | Cómo se ve `(3 + 4) * 2` aquí |
|---|---|
| texto | `"(3 + 4) * 2"` |
| tokens | |
| AST | |
| resultado | |

> Para el renglón del AST, dibújenlo **primero ustedes** y después comprueben
> con `python3 interprete.py --arbol "(3 + 4) * 2"`. Si su dibujo y el del
> programa no coinciden, uno de los dos está mal, y averiguar cuál es
> justamente el trabajo.

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | ¿Cuántos operadores usa? | ¿Normal, frontera o inválida? |
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

> Llenen la tabla **completa**, con las 13. Es tediosa a propósito: la única
> forma de saber qué no está cubierto es caracterizar sistemáticamente lo que
> sí. Cuando terminen, léanla como columna, no como renglones, y pregúntense
> qué combinación **no aparece nunca**.

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

| Prueba (archivo::nombre) | Entrada | Esperado | Categoría | ¿Por qué esa categoría? |
|---|---|---|---|---|
| | | | | |

---

## 4. Los defectos

### 4.1 ¿Qué defecto reveló primero una prueba nueva?

Cómo se tokeniza un simbolo no válido, por ejemplo **@**, no emite ningún error, lo ignora y al final solo devuelve el primer número.

### 4.2 ¿Por qué el comportamiento observado era incorrecto?

Porque no se hace saber que hay un error de sintáxis y al final la expresión podría no ser correcta o no la requerida. Se ejecutó **3 @ 4** y el intérprete solo devolvió **3**, cuando debería especificar un error, como _el simbolo no es válido_, esto pasa porque en el código lo que no sea simbolo o numero, se ignora con un espacio.

### 4.3 ¿Qué cambio realizaron?

| Defecto | Entrada que lo revela | Daba | Debería dar | Commit rojo | Commit verde |
| Lexer gnora operadores no válidos y Parser no comprueba que se hayan consumido todos los tokens | 3 @ 4 | 3 | ErrorDeSintaxis |---|---|
|  |  |  |  |  |  |

### 4.4 ¿Cómo saben que la corrección es general y no sólo hace pasar ese ejemplo?

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontraron?

> Al menos dos. Usen el vocabulario de clase: duplicación, rigidez,
> acoplamiento alto, condicionales repetidos, amplificación del cambio.

### 5.2 ¿Qué refactorización realizaron, y por qué conserva el comportamiento?

> "Las pruebas siguen pasando" es parte de la respuesta, pero no toda.
> ¿Por qué el cambio es equivalente?

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

> Justifiquen. **"Ninguno" puede ser la respuesta correcta.** Si dicen que sí,
> digan qué problema concreto resuelve y qué costo tiene. Si dicen que no,
> digan qué tendría que cambiar en el sistema para que empezara a convenir.

### 5.4 ¿Qué parte del sistema sería más difícil de modificar si se agregara un operador nuevo?

> Por ejemplo `%`. ¿Cuántos archivos hay que tocar? ¿Por qué?

---

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
