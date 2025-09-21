import unittest
import random
from modules.Ordenamiento_Burbuja import OrdenamientoBurbuja
class TestBurbuja(unittest.TestCase):
    def setUp(self):
        self.lista = [random.randint(10000,99999) for _ in range(500)]
    def test_burbuja(self):
        self.lista_ordenada = sorted(self.lista)
        self.lista_burbuja = OrdenamientoBurbuja(self.lista)
        # print(self.lista_ordenada)
        # print(self.lista_burbuja)
        self.assertEqual(self.lista_ordenada,self.lista_burbuja)    

if __name__ == '__main__':
    unittest.main()            
       
    