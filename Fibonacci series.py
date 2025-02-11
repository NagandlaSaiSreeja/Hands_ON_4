def fibonacci_series(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_series(n - 1) + fibonacci_series(n - 2)
result = fibonacci_series(5)
print(result)