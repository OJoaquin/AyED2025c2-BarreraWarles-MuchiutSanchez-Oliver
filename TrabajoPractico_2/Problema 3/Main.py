from modules.Grafo import Grafo
from modules.Algoritmo_Prim import prim
from modules.Exportar import ExportarGraphviz

def Cargar_datos(ruta_archivo):
    G = Grafo()
    with open("data/aldeas.txt") as f:
        for linea in f:
            partes = linea.strip().split(",")
            if len(partes) == 3:
                origen = partes[0].strip()
                destino = partes[1].strip()
                peso = int(partes[2].strip())
                print(origen, destino, peso)
                G.agregar_arista(origen, destino, peso)
            elif len(partes) == 1:
                # Por si hay una aldea aislada sin conexiones
                G.agregar_vertice(partes[0].strip())
    return G

ruta = r"C:\Marti\facu\Algoritmo\AyED2025c2-BarreraWarles-MuchiutSanchez-Oliver\TrabajoPractico_2\Problema 3\data\aldeas.txt"
Base_de_datos_Palomas = Cargar_datos("aldeas.txt")
inicio = Grafo.obtener_vertice("Peligros")
prim(Base_de_datos_Palomas, inicio)
ExportarGraphviz(Base_de_datos_Palomas, "mst.dot")

