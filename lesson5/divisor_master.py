import collections
from math import sqrt


def simple_numbers_list(n):
    """
    Список простых чисел в диапазоне от 2 до num
    :param n: int
    :return: list
    """
    nums = [1]
    nums.extend([i for i in range(2, n + 1) if is_simple_number(i)])
    return nums

def is_simple_number(n):
    """
    Проверяем является ли число простым
    :param n: int
    :return: bool
    """
    for d in range(2, n + 1):
        if d > sqrt(n):
            break
        if n % d == 0:
            return False

    return True

def dividers(n, simple_numbers):
    """
    Получаем список с делителями числа
    :param n: int
    :param simple_numbers: list
    :return: list
    """
    if n in simple_numbers:
        return [n]
    return [i for i in range(2, n) if n % i == 0]

def simple_multipliers(n, simple_numbers):
    """
    Каноническое разложение числа на простые множители
    :param n: int
    :param simple_numbers: list
    :return: str
    """
    if n in simple_numbers:
        return n

    d = 2
    c = collections.Counter()

    while True:
        if d not in simple_numbers:
            d += 1
            continue
        if n % d == 0:
            c[d] += 1
            n = n / d
        else:
            d += 1
        # условие выхода из безконечного цикла
        if 1 == n:
            break

    return ' * '.join(list(map(lambda x: f'{x[0]}**{x[1]}' if x[1] > 1 else f'{x[0]}', list(c.items()))))

def max_simple_divider(simple_numbers, divs):
    """
    Наибольший простой делитель
    :param simple_numbers: list
    :param divs: list
    :return: int
    """
    return max(list(filter(lambda x: x in simple_numbers, divs)))

def max_divider(divs):
    """
    Наибольший делитель
    :param divs: list
    :return: int
    """
    return max(divs)
