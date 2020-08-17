def factorial(n):
    """Calcula el factorial de n

    Args:
        n int : entero mayor a cero
        returns n!
    """
    print(n)
    if n == 1:
        return 1

    return n * factorial(n -1)

n = int(input('Escribe un entero para saber su factorial: '))

print(factorial(n))