from collections import OrderedDict
from time import sleep
from typing import Callable


def lru_cache(max_items: int = 10):
    """
    some doc string
    :param max_items:
    :return:
    """
    def decorator(fn: Callable):
        cache = OrderedDict()

        def wrapper(*args):
            if args not in cache:
                cache[args] = fn(*args)

            if len(cache) > max_items:
                cache.popitem(last=False)
            return cache[args]

        return wrapper

    return decorator


@lru_cache(max_items=25)
def foo(a, b):
    sleep(1)
    return a + b


@lru_cache()
def _bar(a, b):
    sleep(1)
    return a - b


# @lru_cache
# def car(a, b):
#     sleep(1)
#     return a - b


def main():
    print(foo(1, 5))
    print(foo(1, 3))
    print(foo(1, 2))
    # print(car(1, 2))
    print(foo(1, 3))
    print(foo(1, 2))


if __name__ == '__main__':
    main()
