import unittest
def fibonacci(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a,b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


class TestFibonacci(unittest.TestCase):
    def test_fibonacci_zero(self):
        # Teste para F(0) que deve retornar 0
         self.assertEqual(fibonacci(0), 0)
    def test_fibonacci_um(self):
        # Teste para F(1) que deve retornar 1
     self.assertEqual(fibonacci(1), 1)
    def test_fibonacci_seis(self):
        # Teste para F(6) que deve retornar 8
        self.assertEqual(fibonacci(6), 8)
    def test_fibonacci_dez(self):
        # Teste para F(10) que deve retornar 55
        self.assertEqual(fibonacci(10), 55)
    def test_fibonacci_grande(self):
     # Teste para um termo maior da sequência, como F(20)
     self.assertEqual(fibonacci(20), 6765)