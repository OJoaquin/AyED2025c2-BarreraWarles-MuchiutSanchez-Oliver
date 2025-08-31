class Nodo:
    def __init__(self, dato):  
        self.dato = dato
        self.siguiente = None
        self.anterior = None    
class ListaDobleEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.tamaño = 0

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:  # Si la lista está vacía
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente =self.primero
            self.primero.anterior = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.tamaño += 1
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:  # Si la lista está vacía
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            nuevo_nodo.siguiente =self.ultimo
            self.ultimo.anterior = nuevo_nodo
            self.primero = nuevo_nodo
        self.tamaño += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio: 
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.primero
            for _ in range(posicion):
                nuevo_nodo.anterior = actual.anterior
                nuevo_nodo.siguiente = actual
                actual.anterior.siguiente = nuevo_nodo
                actual.anterior = nuevo_nodo
                self.tamanio += 1
    
    def extraer(self, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
          dato = self.primero.dato
          self.primero = self.primero.siguiente
        if self.primero: 
           self.primero.anterior = None
        else: 
           self.ultimo = None
           self.tamanio -= 1
        return dato

    def copiar(self, copia):
        copia.self = ListaDobleEnlazada()
        actual = self.primero
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia
    
    def invertir(self):
        actual = self.primero
        self.primero, self.ultimo = self.ultimo, self.primero
        while actual:
             actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
             actual = actual.anterior
    
    def concatenar(self, otra_lista):
        
        self.ultimo.siguiente = otra_lista.primero
        otra_lista.primero.anterior = self.ultimo
        self.ultimo = otra_lista.ultimo
        self.tamanio += otra_lista.tamanio
        
        return self

        
        
    
    
    