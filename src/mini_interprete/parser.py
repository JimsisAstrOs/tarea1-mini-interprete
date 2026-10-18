
"""De los tokens al AST.

La gramatica que reconoce este parser es:

    expresion := termino  (('+' | '-') termino)*
    termino   := factor   (('*' | '/') factor)*
    factor    := NUMERO | '(' expresion ')'
"""

from .ast import Numero, OperacionBinaria
from .errores import ErrorDeSintaxis
from .tokens import TipoToken

OPERADORES_SUMA = (TipoToken.MAS, TipoToken.MENOS)
OPERADORES_PRODUCTO = (TipoToken.POR, TipoToken.ENTRE)


class Parser:

    def __init__(self, tokens: list):
        self.tokens = tokens
        self.pos = 0

    def parsear(self):
        """Construye el AST y comprueba que no queden tokens sobrantes."""
        if not self.tokens:
            raise ErrorDeSintaxis("expresion vacia", 0)

        nodo = self._expresion()

        actual = self._actual()
        if actual is not None:
            raise ErrorDeSintaxis(
                f"token inesperado {actual.valor!r}",
                actual.posicion,
            )

        return nodo

    def _actual(self):
        """Regresa el token actual o None si ya no quedan tokens."""
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def _avanzar(self):
        """Consume el token actual y lo regresa."""
        if self.pos >= len(self.tokens):
            pos_error = self.tokens[-1].posicion + 1 if self.tokens else 0
            raise ErrorDeSintaxis("expresion incompleta", pos_error)

        token = self.tokens[self.pos]
        self.pos += 1
        return token

    def _parsear_operacion_binaria(
        self,
        funcion_siguiente_nivel,
        operadores_permitidos,
    ):
        """Construye operaciones binarias asociadas a la izquierda."""
        nodo = funcion_siguiente_nivel()

        while (
            self._actual() is not None
            and self._actual().tipo in operadores_permitidos
        ):
            operador = self._avanzar()
            derecha = funcion_siguiente_nivel()
            nodo = OperacionBinaria(operador.valor, nodo, derecha)

        return nodo

    def _expresion(self):
        return self._parsear_operacion_binaria(
            self._termino,
            OPERADORES_SUMA,
        )

    def _termino(self):
        return self._parsear_operacion_binaria(
            self._factor,
            OPERADORES_PRODUCTO,
        )

    def _factor(self):
        if self._actual() is None:
            pos_error = self.tokens[-1].posicion + 1 if self.tokens else 0
            raise ErrorDeSintaxis(
                "se esperaba una expresion u operando",
                pos_error,
            )

        token = self._avanzar()

        if token.tipo == TipoToken.NUMERO:
            return Numero(token.valor)

        if token.tipo == TipoToken.PAR_IZQ:
            nodo = self._expresion()
            actual = self._actual()

            if actual is None or actual.tipo != TipoToken.PAR_DER:
                if actual is not None:
                    pos = actual.posicion
                else:
                    # El cierre se esperaba al final de la entrada.
                    pos = self.tokens[-1].posicion + 1

                raise ErrorDeSintaxis("se esperaba ')'", pos)

            self._avanzar()
            return nodo

        raise ErrorDeSintaxis(
            f"token inesperado {token.valor!r}",
            token.posicion,
        )
