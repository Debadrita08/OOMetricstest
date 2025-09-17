def factorial(n):
    if n < 0:
        raise ValueError("Negative numbers do not have factorials.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)