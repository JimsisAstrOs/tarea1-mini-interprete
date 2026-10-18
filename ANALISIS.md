# Análisis — Tarea 1: Mini intérprete

**Integrantes**
1. Flores Corona Astrid
2. Flores Leyva Ivone Alejandra
3. Ortiz Trujillo Jimena

**Fork:** https://github.com/JimsisAstrOs/tarea1-mini-interprete  
**Rama:** `main`

---

## 1. Arquitectura

### 1.1 ¿Cuál es la responsabilidad de cada componente?

| Componente | Qué recibe | Qué entrega | De qué es responsable |
|---|---|---|---|
| `lexer` | Una cadena con una expresión aritmética | Una lista de tokens con tipo, valor y posición | Reconocer números, operadores y paréntesis; ignorar espacios en blanco y reportar caracteres no válidos. |
| `parser` | Una lista de tokens | Un árbol de sintaxis abstracta (AST) | Validar la sintaxis y construir el árbol respetando la precedencia y los paréntesis. |
| `ast` | Los valores y operadores que forman la expresión | Objetos `Numero` y `OperacionBinaria` | Representar la expresión mediante un árbol. |
| `evaluator` | Un AST | Un resultado numérico | Recorrer el árbol, ejecutar las operaciones y reportar errores de evaluación, como la división entre cero. |

### 1.2 ¿Qué recorrido sigue una expresión desde el texto hasta el resultado?

Ejemplo: `(3 + 4) * 2`.

| Etapa | Representación |
|---|---|
| Texto | `"(3 + 4) * 2"` |
| Tokens | `PAR_IZQ("("), NUMERO(3), MAS("+"), NUMERO(4), PAR_DER(")"), POR("*"), NUMERO(2)` |
| AST | `OperacionBinaria("*", OperacionBinaria("+", Numero(3), Numero(4)), Numero(2))` |
| Resultado | `14` |

---

## 2. Las pruebas que ya estaban

### 2.1 ¿Qué pruebas venían incluidas?

| Prueba | Componente | Comportamiento que verifica | Categoría |
|---|---|---|---|
| `test_tokeniza_un_numero_solo` | Lexer | Reconocimiento de un número | Normal |
| `test_tokeniza_una_suma` | Lexer | Reconocimiento y orden de los tokens de una suma | Normal |
| `test_los_espacios_no_producen_tokens` | Lexer | Los espacios no generan tokens | Normal |
| `test_tokeniza_parentesis` | Lexer | Reconocimiento de paréntesis y números | Normal |
| `test_construye_el_arbol_de_una_suma` | Parser | Construcción del AST de una suma | Normal |
| `test_la_multiplicacion_se_agrupa_antes_que_la_suma` | Parser | Precedencia de la multiplicación | Normal |
| `test_los_parentesis_cambian_la_agrupacion` | Parser | Agrupación mediante paréntesis | Normal |
| `test_suma` | Evaluador | Evaluación de una suma | Normal |
| `test_resta` | Evaluador | Evaluación de una resta | Normal |
| `test_multiplicacion` | Evaluador | Evaluación de una multiplicación | Normal |
| `test_division` | Evaluador | Evaluación de una división | Normal |
| `test_precedencia_sin_parentesis` | Evaluador | Precedencia de operaciones | Normal |
| `test_precedencia_con_parentesis` | Evaluador | Agrupación mediante paréntesis | Normal |

### 2.2 ¿Qué comportamientos no estaban probados?

Las pruebas originales se concentraban principalmente en expresiones válidas y sencillas. Faltaba comprobar:

1. **Operaciones y precedencia:** asociatividad de restas y divisiones encadenadas, división con resultado decimal y precedencia de la división sobre la suma.
2. **Números y espacios:** ceros a la izquierda, tabulaciones y diferentes espacios en blanco.
3. **Entradas inválidas:** caracteres no reconocidos, números consecutivos sin operador, expresiones incompletas, paréntesis incorrectos y signo negativo unario.
4. **Errores:** división entre cero y posición reportada por los errores de sintaxis.
5. **Entrada completa:** rechazo de tokens sobrantes después de una expresión aparentemente válida.

---

## 3. Las pruebas que agregamos

### 3.1 ¿Cuáles son casos normales, frontera e inválidos?

| Prueba | Entrada | Resultado esperado | Categoría |
|---|---|---|---|
| `test_division_con_resultado_decimal` | `10 / 4` | `2.5` | Normal |
| `test_precedencia_de_division_sobre_suma` | `8 + 12 / 4` | `11.0` | Normal |
| `test_asociatividad_izquierda_de_la_resta` | `10 - 3 - 2` | `5` | Normal |
| `test_numero_con_ceros_a_la_izquierda` | `007` | `7` | Frontera |
| `test_expresion_con_tabulaciones_y_espacios` | `\t3 \t + \t 4 ` | `7` | Frontera |
| `test_division_entre_cero` | `8 / 0` | `ErrorDeEvaluacion` | Frontera |
| `test_expresion_con_cero` | `0 + 5` | `5` | Frontera |
| `test_caracter_no_reconocido` | `3 @ 4` | `ErrorDeSintaxis` | Inválida |
| `test_numeros_consecutivos_sin_operador` | `3 4` | `ErrorDeSintaxis` | Inválida |
| `test_expresion_incompleta` | `3 +` | `ErrorDeSintaxis` | Inválida |
| `test_parentesis_sin_cerrar` | `(3 + 4` | `ErrorDeSintaxis` | Inválida |
| `test_signo_negativo_unario` | `-3` | `ErrorDeSintaxis` | Inválida |
| `test_parentesis_sin_cerrar_reporta_posicion_final` | `(3 + 4` | `ErrorDeSintaxis` con posición igual a la longitud de la entrada | Inválida |

La última prueba comprueba, además de que se rechace la expresión, que la posición reportada corresponda al lugar donde se esperaba el paréntesis de cierre.

---

## 4. Los defectos

### 4.1 ¿Qué defectos identificamos?

Durante el análisis de las pruebas adicionales se consideraron los siguientes problemas:

1. El lexer podía ignorar caracteres no reconocidos, como `@`, en la versión inicial.
2. El parser podía aceptar una expresión sin consumir todos los tokens, como `3 4`.
3. Una expresión incompleta, como `3 +`, podía provocar una excepción nativa de Python en lugar de un error de sintaxis controlado.
4. Las operaciones consecutivas del mismo nivel debían asociarse a la izquierda. Por ejemplo, `10 - 3 - 2` debe interpretarse como `(10 - 3) - 2`.
5. Al faltar un paréntesis de cierre, debía reportarse la posición donde se esperaba el cierre.

### 4.2 ¿Por qué eran incorrectos esos comportamientos?

- `3 @ 4` debe rechazarse porque `@` no pertenece al lenguaje admitido.
- `3 4` debe rechazarse porque dos números consecutivos no forman una expresión válida sin un operador.
- `3 +` debe generar `ErrorDeSintaxis`, no una excepción interna de Python.
- `10 - 3 - 2` debe producir `5`, de acuerdo con la asociatividad izquierda.
- `(3 + 4` debe generar un error que señale dónde se esperaba `)`.

### 4.3 ¿Qué cambios realizamos?

| Problema | Corrección |
|---|---|
| Caracteres no reconocidos | El lexer debe generar un error de sintaxis ante caracteres no admitidos. |
| Tokens sobrantes | `parsear()` verifica si quedan tokens después de analizar la expresión. |
| Expresiones incompletas | Se agregaron comprobaciones para producir errores de sintaxis controlados. |
| Asociatividad incorrecta | Se utiliza un recorrido iterativo que construye las operaciones de izquierda a derecha. |
| Paréntesis sin cerrar | Se ajustó el reporte de posición para señalar el final de la entrada cuando falta el cierre. |

### 4.4 ¿Cómo sabemos que las correcciones son generales y no solo sirven para un ejemplo?

Las pruebas cubren diferentes expresiones válidas, casos límite y entradas inválidas. Además, el parser utiliza un método auxiliar para procesar operaciones binarias de un mismo nivel, en lugar de repetir esa lógica en cada nivel de precedencia.

La ejecución local reportada de `python -m pytest -v` terminó con **26 pruebas aprobadas**. Este resultado confirma que esas pruebas pasan en el entorno utilizado, aunque por sí solo no demuestra que se hayan cubierto todos los casos posibles.

---

## 5. Diseño

### 5.1 ¿Qué duplicación o señal de mal diseño encontramos?

1. **Duplicación en el parser:** los métodos que analizan expresiones y términos necesitaban recorrer operadores y construir nodos binarios mediante una lógica similar.
2. **Condicionales en el evaluador:** el método `evaluar()` determina la operación mediante condiciones para cada operador. Esto funciona, pero obliga a modificar esa función al agregar nuevas operaciones.

### 5.2 ¿Qué refactorización realizamos y por qué conserva el comportamiento?

Aplicamos **Extract Method** en `Parser`, mediante el método auxiliar `_parsear_operacion_binaria()`.

Este método recibe la función encargada de analizar el siguiente nivel de precedencia y los operadores permitidos. Así, se reutiliza la lógica para construir operaciones binarias y se mantiene la asociatividad a la izquierda.

La refactorización conserva el comportamiento esperado porque mantiene las reglas de precedencia y la estructura de los nodos del AST. Las pruebas sirven para comprobar que los casos cubiertos siguen funcionando.

### 5.3 ¿Sería pertinente usar Factory Method, Adapter o ninguno?

Consideramos que **ninguno de los dos patrones es necesario para el diseño actual**.

- **Factory Method:** la creación de `Numero`, `OperacionBinaria` y los tokens es directa. No se observa una necesidad concreta de delegar la creación de familias de objetos mediante subclases.
- **Adapter:** no identificamos interfaces externas incompatibles que requieran una adaptación.

Introducir alguno de estos patrones sin una necesidad concreta agregaría complejidad sin resolver un problema actual del intérprete.

### 5.4 ¿Qué parte sería más difícil de modificar si agregáramos un operador?

Principalmente, el lexer, el parser y el evaluador:

1. En `tokens.py` y `lexer.py`, habría que definir y reconocer el nuevo operador.
2. En `parser.py`, habría que incorporarlo a la regla de precedencia correspondiente o crear un nuevo nivel.
3. En `evaluator.py`, habría que implementar su operación y asociarla con el símbolo correspondiente.

La dificultad depende del operador: uno con una precedencia nueva requeriría más cambios que uno que se incorpore a un nivel existente.

---

## Conclusión

Las pruebas adicionales permitieron examinar comportamientos que no estaban cubiertos por las pruebas originales, especialmente los errores de sintaxis, la asociatividad y los casos límite. La refactorización del parser reduce la duplicación y facilita mantener las reglas de precedencia. La elección de no introducir Factory Method ni Adapter se basa en que el diseño actual no presenta una necesidad concreta para esos patrones.
