def fatorial(n):
    f = 1
    for i in range(n, 0, -1):
        f *= i
    return f