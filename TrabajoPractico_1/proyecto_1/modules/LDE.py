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
            self.cabeza.anterior = None
        if posicion == self.tamanio:
            dato = self.cola
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.tamanio -= 1
        else:
            actual = self.cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente , actual.siguiente.anterior = actual.siguiente , actual.anterior
            actual = actual.siguiente
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
        actual = self.cola
        self.cabeza, self.cola = self.cola, self.cabeza
        for _ in range(self.tamanio+1):
            if actual is not None:
                actual.siguiente, actual.anterior = actual.anterior, actual.siguiente
                actual = actual.siguiente
        return
    def concatenar(self, lista):
        actual = lista.cabeza
        if lista.cabeza is None:
            return
        while actual:
            self.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return self

    def __len__(self):
        return self.tamanio
    
    def __add__(self, Lista):
        nueva_lista = ListaDobleEnlazada()
        nueva_lista = self.copiar()
        nueva_lista.concatenar(Lista)
        return nueva_lista
    
    def __iter__(self,lista):
        actual = self.cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente

    def __str__(self):
        #sirve para poder mostrar el contenido de una LDE por consola con la función print
        elementos = []
        actual = self.cabeza
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

if __name__ == "__main__":
    lde1 = ListaDobleEnlazada()
    lde1.agregar_al_final(1)
    lde1.agregar_al_final(2)
    lde1.agregar_al_final(3)
    lde1.agregar_al_final(4)
    lde1.agregar_al_final(5)
    print(lde1)
    lde1.extraer(1)
    print(lde1)

    



