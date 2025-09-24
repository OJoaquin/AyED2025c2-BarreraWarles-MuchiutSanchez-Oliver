from matplotlib import pyplot as plt #pip install matplotlib
from random import randint
import time
from modules.LDE import ListaDobleEnlazada

tamanio = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

tiempo_invertir = []
tiempo_copiar = []
tiempo_len = []

for n in tamanio:
    lista = ListaDobleEnlazada()

    for _ in range(n):
        dato = randint(1, 100)
        lista.agregar_al_final(dato)
    
    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        lista.__len__()
        fin = time.perf_counter()
        contador += (fin - inicio) / n
    tiempo_len.append(contador)

    contador = 0
    for _ in range(n):
        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        contador += (fin - inicio) / n
    tiempo_invertir.append(contador)
    contador = 0
    
    for _ in range(n):
        inicio = time.perf_counter()
        lista.copiar()
        fin = time.perf_counter()
        contador += (fin - inicio) / n
    tiempo_copiar.append(contador)


# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanio, tiempo_len, marker='o', label="Tiempo len - O(1)")
plt.plot(tamanio, tiempo_invertir, marker='o', label="Tiempo invertir - O(n)")
plt.plot(tamanio, tiempo_copiar, marker='o', label="Tiempo copiar - O(n)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de eliminación')
plt.legend()
plt.grid()
plt.show()