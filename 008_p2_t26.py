# Lambda
cuadrado = lambda x: x ** 2
print(cuadrado(4))

# Map con lambda
numeros = [1, 2, 3, 4]
print(list(map(lambda x: x + 10, numeros)))

# Recursividad
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))
