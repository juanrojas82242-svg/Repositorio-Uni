#invertir un string
""""
def invertir_palabra(s): 
    if len(s) <= 1 : 
        return s
    return invertir_palabra(s[1: ]) + s[0]     

print(invertir_palabra("hola"))
"""
"""
#Verificar que una palabra sea palindromo
def palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False

    return palindromo(s[1:-1 ])

print(palindromo("hola"))
"""
"""
#contar cuantas veces se repite un caracter en un texto
def contar(s, c):
    if len(s) == 0:
        return 0
    cuenta = 1 if s[0] == c else 0
    return cuenta + contar(s[1:], c)
"""
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
            self.cabeza = nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nodo

#Implementa una función recursiva que reciba la cabeza de una lista ligada y retorne la suma de todos sus elementos.
    def suma_elementos(self, cabeza):
        if cabeza is None:
            return 0
        return cabeza.dato + self.suma_elementos(cabeza.siguiente)
    
#Contar ocurrencias
#Dada una lista ligada y un valor x, implementa una función recursiva que retorne cuántas veces aparece x.    
    def contar_x(self, cabeza, x):
        if cabeza is None:
            return 0
    
        if cabeza.dato == x:
            return 1 + self.contar_x(cabeza.siguiente, x)
        else:
            return self.contar_x(cabeza.siguiente, x)

#Buscar elemento (booleano)
#Implementa una función recursiva que devuelva true si un valor existe en la lista y false si no.
    def valor_existe(self, cabeza, x):
        if cabeza is None:
            return False
        if cabeza.dato == x:
            return True
        return self.valor_existe(cabeza.siguiente, x)

#Obtener el máximo recursivamente
#Implementa una función que retorne el valor máximo de la lista usando recursividad
    def maximo(self, cabeza):
        if cabeza is None:
            return float('-inf')  # Representa un valor muy pequeño
    
        max_resto = self.maximo(cabeza.siguiente)  # Recursión
        return cabeza.dato if cabeza.dato > max_resto else max_resto

#Calcular la longitud recursivamente
#Implementa una función que retorne la cantidad de nodos usando recursión.
    def longitud_nodos(self, cabeza):
        if cabeza is None:
            return 0
        longitud = self.longitud_nodos(cabeza.siguiente) + 1
        return longitud

#Suma de los elementos pares
    def suma_pares(self, cabeza):
        if cabeza is None:
            return 0
        if cabeza.dato % 2 == 0:
            return cabeza.dato + self.suma_pares(cabeza.siguiente) 
        else:
            return self.suma_pares(cabeza.siguiente)
        
############################################################################
############################################################################


#Eliminación e inserción recursiva
#Eliminar todas las ocurrencias de un valor x
    def eliminar_x(self, cabeza, x):
        if cabeza is None:
            return None
        # Si el nodo actual tiene el valor x, lo eliminamos
        if cabeza.dato == x:
            return self.eliminar_x(cabeza.siguiente, x)
        # Si no, lo conservamos y seguimos con el siguiente
        cabeza.siguiente = self.eliminar_x(cabeza.siguiente, x)
        return cabeza


#Insertar en lista ordenada
    def insertar_ordenado(self, cabeza, dato):
        # Caso base: fin de la lista o valor menor que el nodo actual
        if cabeza is None or dato < cabeza.dato:
            nuevo = Nodo(dato)
            nuevo.siguiente = cabeza
            return nuevo
        # Recorremos recursivamente
        cabeza.siguiente = self.insertar_ordenado(cabeza.siguiente, dato)
        return cabeza

#Eliminar ultimo nodo recursicamente
    def eliminar_ultimo(self, cabeza):
        if cabeza is None:
            return None
        if cabeza.siguiente is None:
            return None  # Eliminamos el último
        cabeza.siguiente = self.eliminar_ultimo(cabeza.siguiente)
        return cabeza

#Invertir completamente la lista
    def invertir_lista(self, cabeza):
        if cabeza is None or cabeza.siguiente is None:
            return cabeza
        resto = self.invertir_lista(cabeza.siguiente)
        cabeza.siguiente.siguiente = cabeza
        cabeza.siguiente = None
        return resto

##Verificar si es palindromo
    def es_palindromo(self):
        izquierda = [self.cabeza]

        def aux(derecha):
            if derecha is None:
                return True

            if not aux(derecha.siguiente):
                return False

            iguales = izquierda[0].dato == derecha.dato
            izquierda[0] = izquierda[0].siguiente
            return iguales

        return aux(self.cabeza)
    
#Intercalar dos listas recursivamente Dadas dos listas: A: 1 → 3 → 5 B: 2 → 4 → 6
#Generar: 1 → 2 → 3 → 4 → 5 → 6
    def intercalar(self, otra_lista):

        def aux(A, B):
            if A is None:
                return B
            if B is None:
                return A

            temp = A.siguiente
            A.siguiente = B
            B.siguiente = aux(temp, B.siguiente)
            return A

        self.cabeza = aux(self.cabeza, otra_lista.cabeza)

    """
Eliminar duplicados consecutivos (lista ordenada)

Dada una lista ordenada, elimina nodos duplicados consecutivos de forma recursiva.

Ejemplo:

1 → 1 → 2 → 2 → 2 → 3 → 4 → 4
Resultado:
1 → 2 → 3 → 4
"""
    
    def eliminar_duplicados(self, cabeza):
        if cabeza is None or cabeza.siguiente is None:
            return cabeza

        cabeza.siguiente = self.eliminar_duplicados(cabeza.siguiente)

        if cabeza.dato == cabeza.siguiente.dato:
            cabeza.siguiente = cabeza.siguiente.siguiente

        return cabeza
    
#Separar pares e impares (recursivo)
    def separar_pares_impares(self):

        pares = []
        impares = []

        def aux(nodo):
            if nodo is None:
                return

            aux(nodo.siguiente)

            if nodo.dato % 2 == 0:
                nodo.siguiente = pares[0] if pares else None
                pares[:] = [nodo]
            else:
                nodo.siguiente = impares[0] if impares else None
                impares[:] = [nodo]

        aux(self.cabeza)

        if not pares:
            self.cabeza = impares[0] if impares else None
            return

        temp = pares[0]
        while temp.siguiente:
            temp = temp.siguiente

        temp.siguiente = impares[0] if impares else None
        self.cabeza = pares[0]

#Eliminar nodo central
    def eliminar_en_pos(self, cabeza, pos):
        if cabeza is None:
            return None

        if pos == 0:
            return cabeza.siguiente

        cabeza.siguiente = self.eliminar_en_pos(cabeza.siguiente, pos - 1)
        return cabeza


    def eliminar_central(self):
        n = self.longitud_nodos(self.cabeza)
        pos = n // 2
        self.cabeza = self.eliminar_en_pos(self.cabeza, pos)

####################################################################################################
###################################################################################################

lista = Lista()
lista.agregar(10)
lista.agregar(20)
lista.agregar(30)
lista.agregar(10)
lista.agregar(67)
print(lista.suma_elementos(lista.cabeza))
print(lista.contar_x(lista.cabeza, 10))
print(lista.valor_existe(lista.cabeza, 10))
print(lista.maximo(lista.cabeza))
print(lista.longitud_nodos(lista.cabeza))
print(lista.suma_pares(lista.cabeza))