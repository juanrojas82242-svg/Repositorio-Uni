#ejemplos recursividad

#Invertir un string
#hola ---> aloh

"""
def invertir_palabra(s):
    if len(s) <= 1:
        return s
    return invertir_palabra(s[1:]) + s [0]
"""
"""
def palindromo(s):
    if len(s) <= 1: #condicion base
        return True
    if s[0] != s[-1]: #primer palabra distinta a la ultima = falso
        return False
    return palindromo(s[1:-1]) #va repitiendo la palabra

print(palindromo("reconocer"))
"""
"""
#contar cuantas veces se repite un caracter en un texto
def caracter_repetido(s, c):
    if len(s) == 0:
        return 0
    suma = 1 if s[0] == c else 0
    return suma + caracter_repetido(s[1:], c)

print(caracter_repetido("recursividad", "a"))
"""
from dbm import ndbm
from time import sleep


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = Nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

#cuantos nodos hay en la lista ligada con recursividad
    def _contar_nodos_recursivos(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_recursivos(nodo.siguiente)

    def contar_nodos(self):
        return self._contar_nodos_recursivos (self.cabeza)

#metodo para buscar dato en lista ligada
    def buscar_dato(self, nodo, dato):
        if nodo is None:
            return False
        elif nodo.dato == dato:
            return True
        return self.buscar_dato(nodo.siguiente, dato)
