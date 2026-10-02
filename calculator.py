"""Business logic for the unit-testing lab."""
from math import isqrt


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError('Деление на ноль')
        return a / b

    @staticmethod
    def is_prime_number(number):
        if isinstance(number, bool) or not isinstance(number, int):
            raise TypeError('Ожидается целое число')
        if number < 2:
            return False
        return all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))
