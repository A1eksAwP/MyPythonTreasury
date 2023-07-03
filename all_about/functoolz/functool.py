# https://docs.python.org/3.11/library/functools.html

from functools import lru_cache, partial


@lru_cache(maxsize=128)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))  # Вывод: 55
print(fibonacci(10))  # Вывод: 55


def multiply(a, b):
    return a * b


double = partial(multiply, b=2)
triple = partial(multiply, b=3)

print(double(5))  # Вывод: 10
print(triple(5))  # Вывод: 15
