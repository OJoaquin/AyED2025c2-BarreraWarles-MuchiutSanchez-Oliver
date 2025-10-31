from modules.Monticulo import Monticulo_Binario
from modules.Vertice import Vertice
class Cola_De_Prioridad:
    def __init__(self):
        self.monticulo = Monticulo_Binario()

    def estaVacia(self):
        return self.monticulo.tamanoActual == 0

    def agregar(self, item):
        self.monticulo.insertar(item)

    def avanzar(self):
        return self.monticulo.eliminarMin()

    def tamano(self):
        return self.monticulo.tamanoActual
    
    def contiene(self, vertice):
        for i in range(1, self.monticulo.tamanomonticulo() + 1):
            if self.monticulo.listaMonticulo[i][1] == vertice:
                return True
        return False
    
    def decrementar_clave(self, vertice, nuevo_valor):
        for i in range(1, self.monticulo.tamanomonticulo() + 1):
            if self.monticulo.listaMonticulo[i][1] == vertice:
                self.monticulo.listaMonticulo[i] = (nuevo_valor, vertice)
                self.monticulo.infiltArriba(i)
                break 
    
    def __iter__(self):
        return iter(self.monticulo)
    def construir_Monticulo(self, unaLista):
        self.monticulo.construirMonticulo(unaLista)
    
if __name__ == '__main__':
    Cola = Cola_De_Prioridad()
    Cola.agregar(5)
    Cola.agregar(3)
    Cola.agregar(8)
    print (Cola.estaVacia())
    print (Cola.tamano())
    print (Cola.avanzar())
    print (Cola.avanzar())
    print (Cola.avanzar())
    print (Cola.estaVacia())
    print ("HOla")
    # for x in Cola:
    #     print(x)
    # for x in range(10):
    #     print(Cola.avanzar())