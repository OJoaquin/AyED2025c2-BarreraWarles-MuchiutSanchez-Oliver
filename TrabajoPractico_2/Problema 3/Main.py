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
inicio = Base_de_datos_Palomas.obtener_vertice("Peligros")
prim(Base_de_datos_Palomas, inicio)

if __name__ == "__main__":
    #Aldeas en orden alfabetico
    print("Lista de aldeas en orden alfabetico: ")
    for v in sorted(Base_de_datos_Palomas, key=lambda x: x.id):
        print(v.id)
    ExportarGraphviz(Base_de_datos_Palomas, "mst.dot")
    #Para cada aldea, mostrar de qué vecina debería recibir la noticia,
    #y a qué vecinas debería enviar réplicas, siendo que se está enviando el mensaje
    #de la forma más eficiente a las 21 aldeas.
    #Tomar en cuenta que desde Peligros solamente se envían noticias a una o más aldeas vecinas.
    replica = {v.id: [] for v in Base_de_datos_Palomas}
    for v in Base_de_datos_Palomas:
        if v.predecesor:
            replica[v.predecesor.id].append(v.id)
    print("\nrutas optimas de mensaje partiendo desde Peligros:\n")
    for v in sorted(Base_de_datos_Palomas, key=lambda x: x.id):
        if v.predecesor:
            print(f"{v.id} debe recibir el mensaje desde {v.predecesor.id}")
        else:
            print(f"{v.id} (Inicio - envía mensajes)")
        if replica[v.id]:
            print(f"  → Y debe enviarlo a: {', '.join(sorted(replica[v.id]))}") 

    #Para el envío de una noticia, mostrar la suma de todas las distancias recorridas
    #por todas las palomas enviadas desde cada palomar. 
    total_de_distancias = 0
    for v in Base_de_datos_Palomas:
        if v.predecesor:
            total_de_distancias += v.obtener_ponderacion(v.predecesor)

    print(f"\nLa distancia total recorrida por las palomas: {total_de_distancias} leguas")    

    #Exportar el grafo a Graphviz para verificar el árbol de expansión mínima
    #Que todas las aldeas están conectadas, que no se cree ningún ciclo,
    #Que la distancia total esté bien y que se parta desde Peligros
    ExportarGraphviz(Base_de_datos_Palomas, "mst.dot")

