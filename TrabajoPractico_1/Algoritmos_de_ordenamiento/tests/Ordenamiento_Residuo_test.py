import unittest
import random
from modules.Ordenamiento_Residuo import ordenar_por_residuo
class TestResiduo(unittest.TestCase):
    def setUp(self):
        self.lista = [random.randint(10000,99999) for _ in range(500)]
    def test_residuo(self):
        self.lista_ordenada = sorted(self.lista)
        self.lista_residuo = ordenar_por_residuo(self.lista)
        # print(self.lista_ordenada)
        # print(self.lista_residuo)
        self.assertEqual(self.lista_ordenada,self.lista_residuo)    

if __name__ == '__main__':
    unittest.main()          