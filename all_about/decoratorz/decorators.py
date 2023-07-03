import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f'{time.time() - start}s')
        return res
    return wrapper


@timer
def power(*args):
    time.sleep(1)
    return sum(map(lambda x: x ** x, args))


if __name__ == '__main__':
    power(2, 2)
