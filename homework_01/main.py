"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers():
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number * number for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_odd(x):
    return True if (x%2 != 0) else False
def is_even(x):
    return not is_odd(x)
def is_prime( number):
    if number <= 1: return False
    if number == 2: return True
    if (number % 2) == 0:return False
    boundary = math.floor(math.sqrt(number));

    for i in range(boundary+1,2):
        if (number % i) == 0:
            return False
    return True

def filter_numbers():
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if my_type == "odd":
        return [filter(is_odd, my_list)]
    elif my_type == "even":
        return [filter(is_even, my_list)]
    elif my_type == "prime":
        return [filter(is_prime, my_list)]