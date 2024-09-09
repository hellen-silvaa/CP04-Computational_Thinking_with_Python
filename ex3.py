import math
import unittest
def is_perfect_square(n):
    sqrt_n = int(math.sqrt(n))
    return sqrt_n * sqrt_n == n
def is_fibonacci(number):
    return is_perfect_square(5* number * number + 4) or is_perfect_square(5* number * number - 4)

class TestIsFibonacci(unittest.TestCase):
    def test_fibonacci_numero_pertenece(self):
        # Teste para um número que pertence à sequência de Fibonacci (55)
        self.assertTrue(is_fibonacci(55))
    def test_fibonacci_numero_nao_pertenece(self):
        # Teste para um número que não pertence à sequência de Fibonacci (50)
        self.assertFalse(is_fibonacci(50))
    def test_fibonacci_zero(self):
        # Teste para o número 0, que pertence à sequência de Fibonacci
        self.assertTrue(is_fibonacci(0))
    def test_fibonacci_um(self):
        # Teste para o número 1, que pertence à sequência de Fibonacci
        self.assertTrue(is_fibonacci(1))
    def test_fibonacci_numero_grande(self):
        # Teste para um número grande que pertence à sequência de Fibonacci (144)
        self.assertTrue(is_fibonacci(144))