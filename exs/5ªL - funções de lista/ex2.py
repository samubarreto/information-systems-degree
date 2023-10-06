def quadrado(x):
    return x ** 2

def quadrados(n):
    return list(map(quadrado, range(1, n + 1)))
