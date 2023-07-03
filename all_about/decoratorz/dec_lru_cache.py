# Вот пример реализации собственного декоратора lru_cache (Least Recently Used Cache),
# который кэширует результаты вызова функции и повторно использует их при повторных вызовах с теми же аргументами:

from functools import wraps


def lru_cache(max_size):
    cache = {}
    cache_order = []

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (*args, frozenset(kwargs.items()))

            if key in cache:
                # Если результат уже в кэше, возвращаем его
                cache_order.remove(key)
                cache_order.append(key)
                return cache[key]

            result = func(*args, **kwargs)

            # Если размер кэша превышен, удаляем самый старый элемент
            if len(cache) >= max_size:
                oldest_key = cache_order[0]
                del cache[oldest_key]
                cache_order.pop(0)

            # Добавляем результат в кэш
            cache[key] = result
            cache_order.append(key)

            return result

        return wrapper

    return decorator


# Пример использования:

@lru_cache(max_size=2)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Вызов функции с аргументом 5
print(fibonacci(3))  # Вызов функции с аргументом 3 (возвращается из кэша)
print(fibonacci(4))  # Вызов функции с аргументом 4
print(fibonacci(5))  # Вызов функции с аргументом 5 (возвращается из кэша)
# В этом примере декоратор lru_cache принимает аргумент max_size, который определяет максимальный размер кэша.
# Если размер кэша превышен, то самый старый элемент удаляется. Ключом кэша является кортеж из аргументов функции
# и их значений по ключевым аргументам, а значение кэша - результат вызова функции.

# При вызове функции fibonacci, результаты вызовов кэшируются и
# повторно используются для повторных вызовов с теми же аргументами.

