from app import *
import unittest


class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello('Hello World'), 'Hello World')

    def test_soma(self):
        self.assertEqual(soma(4, 4), 8)

    def test_is_par(self):
        self.assertEqual(is_par(5), False)
        self.assertEqual(is_par(12), True)

    def test_is_impar(self):
        self.assertEqual(is_impar(5), True)
        self.assertEqual(is_impar(7), True)
        self.assertEqual(is_impar(2), False)

    def test_is_primo(self):
        self.assertEqual(is_primo(7), True)
        self.assertEqual(is_primo(2), True)
        self.assertEqual(is_primo(4), False)
        self.assertEqual(is_primo(200), False)

    def test_quantidade_letras(self):
        self.assertEqual(quantidade_letras('python'), 6)
        self.assertEqual(quantidade_letras('Algoritmos'), 10)

    def test_inserir(self):
        self.assertEqual(inserir('fulano', '12345'), ['fulano', '12345'])
        self.assertEqual(inserir('joão', '345435'), ['joão', '345435'])


    def test_buscar(self):
        self.assertEqual(buscar('Maria'), True)
        self.assertEqual(buscar('Pedro'), True)
        self.assertEqual(buscar('Paulo'), False)

    def test_buscar_numero(self):
        self.assertEqual(buscar_numero('Maria'), '123')
        self.assertEqual(buscar_numero('Pedro'), '345')
        self.assertEqual(buscar_numero('João'), '98786')

if __name__ == '__main__':
    unittest.main()
