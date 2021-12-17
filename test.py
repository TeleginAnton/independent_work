from time import sleep

import decorators


@decorators.lru_cache()
def bar(a, b):
    sleep(1)
    return a - b


def main():
    print(bar(1, 2))
    print(bar(1, 2))
    print(bar(1, 2))


if __name__ == '__main__':
    main()
