"""Pruebas adicionales para el mini intérprete."""

import pytest

from mini_interprete.cli import interpretar
from mini_interprete.errores import ErrorDeEvaluacion, ErrorDeSintaxis


# ============================================================
# CASOS NORMALES
# ============================================================

def test_division_con_resultado_decimal():
    """Comprueba que la división produzca resultados decimales."""
    assert interpretar("10 / 4") == 2.5


def test_precedencia_de_division_sobre_suma():
    """Comprueba que la división se evalúe antes que la suma."""
    assert interpretar("8 + 12 / 4") == 11.0


def test_asociatividad_izquierda_de_la_resta():
    """Comprueba que las restas del mismo nivel se agrupen a la izquierda."""
    assert interpretar("10 - 3 - 2") == 5


# ============================================================
# CASOS FRONTERA
# ============================================================

def test_numero_con_ceros_a_la_izquierda():
    """Comprueba que los ceros iniciales no cambien el valor numérico."""
    assert interpretar("007") == 7


def test_expresion_con_tabulaciones_y_espacios():
    """Comprueba que los espacios en blanco se ignoren."""
    assert interpretar("\t3 \t + \t 4 ") == 7


def test_division_entre_cero():
    """Comprueba que dividir entre cero produzca un error de evaluación."""
    with pytest.raises(ErrorDeEvaluacion):
        interpretar("8 / 0")


def test_expresion_con_cero():
    """Comprueba que el cero pueda utilizarse como operando."""
    assert interpretar("0 + 5") == 5


# ============================================================
# ENTRADAS INVÁLIDAS
# ============================================================

def test_caracter_no_reconocido():
    """Comprueba que un carácter inválido produzca un error de sintaxis."""
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 @ 4")


def test_numeros_consecutivos_sin_operador():
    """Comprueba que se rechacen números sin un operador entre ellos."""
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 4")


def test_expresion_incompleta():
    """Comprueba que una expresión sin operando derecho sea rechazada."""
    with pytest.raises(ErrorDeSintaxis):
        interpretar("3 +")


def test_parentesis_sin_cerrar():
    """Comprueba que se rechacen los paréntesis sin cerrar."""
    with pytest.raises(ErrorDeSintaxis):
        interpretar("(3 + 4")


def test_signo_negativo_unario():
    """Comprueba que se rechace el signo negativo unario."""
    with pytest.raises(ErrorDeSintaxis):
        interpretar("-3")


def test_parentesis_sin_cerrar_reporta_posicion_final():
    """El error debe señalar dónde se esperaba el paréntesis de cierre."""
    from mini_interprete.lexer import tokenizar
    from mini_interprete.parser import Parser

    expresion = "(3 + 4"
    parser = Parser(tokenizar(expresion))

    with pytest.raises(ErrorDeSintaxis) as error:
        parser.parsear()

    assert error.value.posicion == len(expresion)
