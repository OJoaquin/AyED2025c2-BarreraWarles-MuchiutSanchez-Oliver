from matplotlib import pyplot as plt #pip install matplotlib
from random import randint
import time
from modules.Ordenamiento_Burbuja import OrdenamientoBurbuja
from modules.Ordenamiento_Rapido import OrdenamientoRapido
from modules.Ordenamiento_Residuo import ordenar_por_residuo
tamanio = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

tiempo_burbuja = []
tiempo_rapido = []
tiempo_residuo = []
tiempo_sorted = []

for n in tamanio:
    lista = []

    for _ in range(n):
        dato = randint(1, 100)
        lista.append(dato)
    #Ordenamiento sorted python
    inicio = time.perf_counter()
    sorted(lista)
    fin = time.perf_counter()
    tiempo_sorted.append(fin-inicio)
    #Ordenamiento Burbuja
    inicio = time.perf_counter()
    OrdenamientoBurbuja(lista)
    fin = time.perf_counter()
    tiempo_burbuja.append(fin-inicio)

    #Ordenamiento Rapido
    inicio = time.perf_counter()
    OrdenamientoRapido(lista)
    fin = time.perf_counter()
    tiempo_rapido.append(fin-inicio)
    
    #Ordenamiento Residuo
    inicio = time.perf_counter()
    ordenar_por_residuo(lista)
    fin = time.perf_counter()
    tiempo_residuo.append(fin-inicio)


# Gráfico para inserción
plt.figure(figsize=(10, 6))
plt.plot(tamanio, tiempo_burbuja, marker='o', label="Tiempo burbuja - O(n^2)")
plt.plot(tamanio, tiempo_rapido, marker='o', label="Tiempo Rapido - O(nlog(n))")
plt.plot(tamanio, tiempo_residuo, marker='o', label="Tiempo Residuo - O(n)")
plt.plot(tamanio, tiempo_sorted, marker='o', label="Tiempo sorted - O(n)")
plt.xlabel('Tamaño de la lista')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de tiempos de eliminación')
plt.legend()
plt.grid()
plt.show()