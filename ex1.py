import math
import unittest
def verificar_primo(n):


    if n <= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i:
            return True
        else:
            return False
    return True


class TestVerificarPrimo(unittest.TestCase):
 def test_numero_primo(self):
    # Teste para um número primo (5)
    self.assertTrue(verificar_primo(5))
 def test_numero_nao_primo(self):
    # Teste para um número não primo (4)
    self.assertFalse(verificar_primo(4))
 def test_numero_um(self):
    # Teste para o número 1, que não é primo
    self.assertFalse(verificar_primo(1))
 def test_numero_primo_grande(self):
    # Teste para um número primo grande (29)
    self.assertTrue(verificar_primo(29))
 def test_numero_negativo(self):
    # Teste para um número negativo, que não é primo
    self.assertFalse(verificar_primo(-7))