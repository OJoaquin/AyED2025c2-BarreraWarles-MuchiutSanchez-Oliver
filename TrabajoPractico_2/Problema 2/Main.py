Muestras = []
from modules.Temperaturas_DB import Temperaturas_DB

with open (r"C:\Marti\facu\Algoritmo\AyED2025c2-BarreraWarles-MuchiutSanchez-Oliver\TrabajoPractico_2\Problema 2\data\muestras.txt", 'r') as file:
    lineas = file.readlines()
    for linea in lineas:
        [fecha, temperatura] = linea.strip().split(';')
        # Base_De_Datos_Temperaturas.guardar_temperatura(float(temperatura), fecha)
        Muestras.append([fecha, float(temperatura)])
        print(Muestras)

