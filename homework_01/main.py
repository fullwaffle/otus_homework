"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers: int) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number: int) -> bool:
    """
    функция, которая проверяет простое ли число

    :param number: принимает целое число
    :return: возвращает bool
    """
    if number <= 1:
        return False
    for num in range(2, number):
        if number % num == 0:
            return False
    return True


def filter_numbers(numbers_list: list, filter_type: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == "odd":
        return list(filter(lambda num: num % 2, numbers_list))
    elif filter_type == "even":
        return list(filter(lambda num: num % 2 == 0, numbers_list))
    else:
        return list(filter(is_prime, numbers_list))
