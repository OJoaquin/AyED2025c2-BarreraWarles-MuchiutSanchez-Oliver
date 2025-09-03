class Nodo:
    def __init__(self, dato):  
        self.dato = dato
        self.siguiente = None
        self.anterior = None    
class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.tamanio = 0
    
    def Esta_vacia(self):
        if self.cabeza is None:
            print("esta vacia")
        else:
            print("No esta vacia")    

    def agregar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente =self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1
    
    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior =self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamanio += 1

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio: 
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            nuevo_nodo.anterior = actual.anterior
            actual.anterior.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = actual
            actual.anterior = nuevo_nodo
            self.tamanio += 1 
    
    def extraer(self, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            dato = self.cabeza
            self.cabeza = self.cabeza.siguiente
            self.tamanio -= 1
        if posicion == self.tamanio:
            dato = self.cola
            self.cola = self.cola.anterior
            self.tamanio -= 1
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior
            self.tamanio -= 1
        return dato

    def copiar(self):
        copia = ListaDobleEnlazada()
        actual = self.cabeza
        while actual is not None:
            copia.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return copia
    
    def invertir(self):
        actual = self.cabeza
        self.cabeza, self.cola = self.cola, self.cabeza
        while actual:
             actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
             actual = actual.anterior
    
    def concatenar(self, otra_lista):
        
        self.cola.siguiente = otra_lista.cabeza
        otra_lista.cabeza.anterior = self.cola
        self.cola = otra_lista.cola
        self.tamanio += otra_lista.tamanio
        
        return self

    def __len__(self):
        return self.tamanio
 
        
        
    
    
    