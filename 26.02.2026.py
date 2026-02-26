def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_memo(n,cache={}):
    if n <= 1:
        return n
    
    if n in cache:
        return cache[n]
    
    cache[n] = fibonacci_memo(n-1,cache) + fibonacci_memo(n-2, cache)
    return cache[n]

print(fibonacci_memo(5))

def calc_menor(n, cache={}):
    if n <= 1:
        return 1
    
    if n in cache:
        return cache[n]
    
    cache[n] = calc_menor(cache)

def cambio(cantidad, monedas):
    if cantidad == 0:
        return 0
    if cantidad < 0:
        return float('inf')
    
    minimo = float('inf')
    for moneda in monedas:
        resultado = cambio(cantidad-moneda, monedas)
        minimo = min(resultado + 1,minimo)
    
    return minimo
monedas = [1, 5, 10, 25]
print(cambio(10,monedas))