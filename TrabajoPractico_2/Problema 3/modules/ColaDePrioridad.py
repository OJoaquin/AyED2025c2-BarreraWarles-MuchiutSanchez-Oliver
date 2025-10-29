from modules.Monticulo import Monticulo_Binario
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
    
    def __iter__(self):
        return iter(self.monticulo)
    
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