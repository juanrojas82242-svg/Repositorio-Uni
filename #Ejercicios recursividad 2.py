#Ejercicios recursividad 2
"""
#se ejecuta n veces
def potencia(a, b):
    if b == 0:
        return 1
    return a * potencia(a, b -1)

#algoritmo mas eficiente ahorrando mitad de llamados recursivos
def potencia_optimizada(a, b):
    if b == 0:
        return 1
    if b % 2 == 0: #numero par
        mitad = potencia_optimizada(a, b // 2)
        return mitad*mitad
    else:
        return a * potencia_optimizada(a, b -1)
"""

"""
#suma de todos los digitos de un numero
#cualquier numero que se le saque mod 10 da el ultimo digito
def suma_digitos(a):
    if a == 0:             #tambien puede ser if n < 10:
        return 0           #                     return n
    digito = a % 10
    return digito + suma_digitos(a // 10)

print(suma_digitos(1503))
"""

"""
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(6))
"""

def suma(n):
    if n == 0:
        return 0
    return n + suma(n - 1)


def buscar(lista, numero):
    # Caso base: lista vacía
    if len(lista) == 0:
        return False
    
    # Si el primer elemento es el número
    if lista[0] == numero:
        return True
    
    # Llamada recursiva con el resto de la lista
    return buscar(lista[1:], numero)


print(buscar([4, 7, 2, 9, 5], 9))   # True
print(buscar([4, 7, 2, 9, 5], 3))   # False
