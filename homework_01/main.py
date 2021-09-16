"""
Домашнее задание №1
Функции и структуры данных
"""
import math

def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    # Списковым включение набираем квадраты чисел и вызвращаем
    return [number * number for number in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

# Проверка на нечетное
def is_odd(x):
    return x%2 != 0
# Проверка на четное
def is_even(x):
    return x%2 == 0
# Проверка простое число или нет (линейный перебор), возможна оптимизация?
def is_prime(number):
    d = 2
    while number % d != 0:
        d += 1
    return d == number


def filter_numbers(my_list, my_type):
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
        return list(filter(is_odd, my_list))
    elif my_type == "even":
        return list(filter(is_even, my_list))
    elif my_type == "prime":
        return list(filter(is_prime, my_list))