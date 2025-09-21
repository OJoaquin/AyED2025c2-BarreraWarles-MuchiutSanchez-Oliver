import unittest
import random
from modules.Ordenamiento_Rapido import OrdenamientoRapido, OrdenamientoRapidoAuxiliar, Particion
class TestRapido(unittest.TestCase):
    def setUp(self):
        self.lista = [random.randint(10000,99999) for _ in range(500)]
    def test_rapido(self):
        self.lista_ordenada = sorted(self.lista)
        self.lista_rapido = OrdenamientoRapido(self.lista)
        #print(self.lista_ordenada)
        #print(self.lista_rapido)
        self.assertEqual(self.lista_ordenada,self.lista_rapido)    

if __name__ == '__main__':
    unittest.main()   