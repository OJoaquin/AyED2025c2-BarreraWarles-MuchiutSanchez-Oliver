from modules.LDE import ListaDobleEnlazada
from modules.carta import Carta

class DequeEmptyError(Exception):
    pass  # Define una excepción personalizada para cuando el mazo está vacío

class Mazo:
    def __init__(self):
        self.mazo = ListaDobleEnlazada()

    def __len__(self):
        return self.mazo.tamanio
    
    def poner_carta_arriba(self, carta):
        self.mazo.agregar_al_final(carta)

    def poner_carta_abajo(self, carta):
        self.mazo.agregar_al_inicio(carta)
    
    def sacar_carta_arriba(self, mostrar = False):
        nodo_carta = self.mazo.cabeza
        if nodo_carta != None:
            nodo_carta.dato.visible = mostrar
            carta = self.mazo.extraer()
        else:
            raise DequeEmptyError("El mazo está vacío")
        return carta  # Elimina y devuelve la carta en la posición 0 (parte superior

    def sacar_carta_arriba(self, mostrar = False):
        nodo_carta = self.mazo.cabeza
        if nodo_carta != None:
            nodo_carta.dato.visible = mostrar
            carta = self.mazo.extraer()
        else:
            raise DequeEmptyError("El mazo está vacío")
        return carta  # Elimina y devuelve la carta en la posición 0 (parte superior)

    def esta_vacio(self):
        if self.mazo.tamanio == 0:
            return "Esta vacio"

if __name__ == "__main__":
    mazo = Mazo()
    carta1 = Carta('♣', '5')
    carta2 = Carta('♦', 'K')
    mazo.poner_carta_arriba(carta1)
    mazo.poner_carta_abajo(carta2)
    print(mazo.sacar_carta_arriba())  # Debería imprimir '5♣'
    print(mazo.sacar_carta_arriba())  # Debería imprimir 'K♦'
    print(mazo.esta_vacio())          # Debería imprimir True