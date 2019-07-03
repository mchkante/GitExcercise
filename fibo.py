def fib(n):
    """
    Calcule les n premiers nombre de la suite de Fibonacci.
    """
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()
